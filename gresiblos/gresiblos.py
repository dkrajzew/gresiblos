#!/usr/bin/env python
"""gresiblos - greyrat's simple blog system."""
# ===========================================================================
__author__     = "Daniel Krajzewicz"
__copyright__  = "Copyright 2016-2026, Daniel Krajzewicz"
__credits__    = "Daniel Krajzewicz"
__license__    = "GPL-3.0"
__version__    = "0.8.0"
__maintainer__ = "Daniel Krajzewicz"
__email__      = "daniel@krajzewicz.de"
__status__     = "Production"
# ===========================================================================
# - https://github.com/dkrajzew/gresiblos
# - http://www.krajzewicz.de
# ===========================================================================


# --- imports ---------------------------------------------------------------
import os
import sys
import argparse
import configparser
import glob
import json
import re
import datetime
import urllib.parse
import email.utils
import html
from pathlib import Path
from typing import List, Dict, Any
_HAVE_DEGROTESQUE = False
try:
    import degrotesque
    _HAVE_DEGROTESQUE = True
except ModuleNotFoundError:
    pass
_HAVE_MARKDOWN = False
try:
    import markdown
    _HAVE_MARKDOWN = True
except ModuleNotFoundError:
    pass


# --- class definitions -----------------------------------------------------
class Template:
    """A class realising a template with optional fields and fields to replace
    by given values"""

    def __init__(self, template: str) -> None:
        """
        Initialize a Template object with a given string template.

        Args:
            template (str): The string template to be used by the Template object.
        """
        self._template = template


    def process_optional_fields(self, tpl: str, values: dict) -> str:
        """
        Remove optional fields from the template string.
        Optional fields are enclosed in [[[:?key:?]] ... [[key?:]].

        Args:
            self: The instance of the class.
            tpl (str): The template string containing optional fields.
            values (dict): A dictionary containing the values for the optional fields.

        Returns:
            str: The modified template string with optional
                 fields removed or replaced by their corresponding values.

        Raises:
            SystemExit: If a missing closing tag is detected,
                        the function will exit with an error code 3.
        """
        # remove optional fields (begin tags with [[:?key:]] ... [[:key?:]])
        b = tpl.find("[[:?")
        while b >= 0:
            e = tpl.find(":]]", b + 4)
            if e < 0:
                print("gresiblos: error: "
                      + "Missing ':]]' at the begin tag of an optional "
                      + f"document part that starts at {b}",
                      file=sys.stderr)
                raise SystemExit(3)
            field_key = tpl[b + 4:e]
            b2 = tpl.find("[[:" + field_key + "?:]]")
            if b2 < 0:
                print("gresiblos: error: "
                      + "Missing closing tag of an optional document "
                      + f"part that starts at {b}; field_key='{field_key}'",
                      file=sys.stderr)
                raise SystemExit(3)
            if field_key not in values:
                tpl = tpl[:b] + tpl[b2 + len(field_key) + 7:]
                b = tpl.find("[[:?", b)
            else:
                tpl = tpl[:b2] + tpl[b2 + len(field_key) + 7:]
                tpl = tpl[:b] + tpl[b + len(field_key) + 7:]
                b = tpl.find("[[:?", b)
        return tpl


    def encode_topics(self, values: dict, topics_format: str) -> str:
        """
        Encodes the 'topics' field from a dictionary into
        HTML format based on a given format string.

        Args:
            values (dict): The input dictionary containing
                           the 'topics' field.
            topics_format (str): A format string that includes
                           '[[:topic:]]' as a placeholder for each topic.

        Returns:
            str: A comma-separated string of HTML-encoded topics.
        """
        if "topics" not in values:
            return ""
        topics = values["topics"].split(",")
        html_topics = [topics_format.replace("[[:topic:]]", t.strip()) for t in topics]
        return ", ".join(html_topics)


    def embed(self, values: Dict[str, str], topics_format: str) -> str:
        """
        Embeds the given values into a template.

        Args:
          values (Dict[str, str]): The values to embed.
          topics_format (str): The format of the topics.
          apply_markdown (bool): Whether to apply markdown. Defaults to False.
          prettifier (Any): The prettifier to use. Defaults to None.
        """
        encoded_topics = self.encode_topics(values, topics_format)
        tpl = self.process_optional_fields(self._template, values)
        # replace plain, given fields
        for field_key in values:
            value = values[field_key]
            is_draft = "state" in values and values.get("state") != "release"
            if field_key == "topics":
                value = encoded_topics
            if field_key == "title" and is_draft:
                value = "(Draft) " + values[field_key]
            tpl = tpl.replace("[[:" + field_key + ":]]", value)
        # remove plain, not given fields
        empty_regex = re.compile(r"(\[\[\:[a-zA-Z0-9_]+?\:\]\])", flags=re.MULTILINE)
        tpl = empty_regex.sub("", tpl)
        # check for replacements with defaults
        opt = re.compile(r"\[\[\:([a-zA-Z0-9_]+?)\|([^\:\]\]]+?)\:\]\]", flags=re.MULTILINE)
        # https://stackoverflow.com/questions/69376798/python3-replace-string-using-dict-with-regex
        tpl = opt.sub(lambda x: values[x.group(1)] if x.group(1) in values else x.group(2), tpl)
        return tpl


class Entry:
    """
    Represents a blog entry with metadata and content.

    Attributes:
        _fields (Dict[str, str]): A dictionary to store entry fields.
        _date (datetime.datetime): The date the entry was written at.
        _destination (str): The path and complete filename the entry shall be written to.
    """
    _fields: Dict[str, str] = {}
    _date = None
    _destination = None


    def __init__(self, fields: Dict[str, str] = None) -> None:
        """
        Initializes an Entry object with default values.

        Args:
            fields (Dict[str, str]): The entry's meta data and content.
        """
        self._fields = {} if fields is None else fields.copy()
        self._date = None
        self._destination = None


    def get_date(self) -> datetime.datetime:
        """
        Returns the date the entry was written at.

        Returns:
            (datetime.datetime): The date the entry was written at.
        """
        return self._date


    def get_destination(self) -> str:
        """
        Returns the path and complete filename the entry shall be written to.

        Returns:
            (str): The path and complete filename the entry shall be written to.
        """
        return self._destination


    def get(self, key: str) -> str:
        """
        Returns the value of a field by key.

        Args:
            key (str): The key of the field to retrieve.

        Returns:
            (str): The value of the field.
        """
        return self._fields[key]


    def has_key(self, key: str) -> bool:
        """
        Returns whether the key is known.

        Args:
            key (str): The key of the field to check for.

        Returns:
            (bool): Whether the named field is stored.
        """
        return key in self._fields


    def _consolidate(self, filename: str, date_format: str, extension: str):
        """
        Consolidates the entry fields from a file.

        Args:
          filename (str): The path to the file.
          date_format (str): The format of the date in the file.
                             If None, it will be parsed as ISO 8601.
          extension (str): The file extension.
        """
        # - filename
        if "filename" not in self._fields:
            fn = os.path.splitext(os.path.split(filename)[1])[0]
            fn = urllib.parse.quote(fn)
            self._fields["filename"] = fn
        # - title
        if "title" not in self._fields:
            self._fields["title"] = os.path.splitext(os.path.split(filename)[1])[0]
        # - date
        if "date" not in self._fields:
            t = os.path.getmtime(filename)
            self._date = datetime.datetime.fromtimestamp(t)
        elif date_format is not None:
            self._date = datetime.datetime.strptime(self._fields["date"], date_format)
        else:
            self._date = datetime.datetime.fromisoformat(self._fields["date"])
        if date_format is not None:
            self._fields["date"] = self._date.strftime(date_format)
        else:
            self._fields["date"] = self._date.isoformat(' ')
        # - destination
        self._destination = f"{self._fields['filename']}.{extension}"


    def load(self, filename: str, date_format: str, extension: str) -> None:
        """
        Loads entry data from a filename.

        Args:
            filename (str): The path to the filename containing entry data.
            date_format (str): The date format used in the file.
            extension (str): The extension the result shall have.
        """
        self._fields = {}
        # load file
        with open(filename, mode="r", encoding="utf-8") as fd:
            is_multi_line = False
            first = True
            key = None
            for line in fd:
                ls = line.strip()
                if is_multi_line:
                    if ls == '===':
                        is_multi_line = False
                        continue
                    self._fields[key] = self._fields[key] + line
                    continue
                if len(ls) == 0:
                    continue
                if first and line.find(":") < 0:
                    is_multi_line = True
                    key = "content"
                    self._fields[key] = line
                    first = False
                    continue
                first = False
                if ls[-1] != ':':
                    vs = ls.split(":")
                    self._fields[vs[0]] = ":".join(vs[1:]).strip()
                    continue
                key = ls[:-1]
                self._fields[key] = ""
                is_multi_line = True
        # add missing fields / set needed information
        self._consolidate(filename, date_format, extension)


    def apply_processors(self, apply_markdown: bool, prettifier: Any) -> None:
        """
        Applies text processors optionally:
        a) converts markdown to HTML
        b) applies degrotesque

        Args:
            apply_markdown (bool): If set, markdown is applied.
            prettifier (Any): If given, the prettifier is applied.
        """
        for field in ["content", "title", "abstract"]:
            if field not in self._fields:
                continue
            value = self._fields[field]
            if apply_markdown:
                value = markdown.markdown(value)
                if value.startswith("<p>") and value.endswith("</p>"):
                    value = value[3:-4]
            if prettifier is not None:
                value = prettifier.prettify(value, True)
            self._fields[field] = value


class PlainStorage:
    """
    Stores blog entries.

    Attributes:
        _entries (Dict[str, Entry]): A dictionary to store entries by filename.
    """
    _entries: Dict[str, Entry] = {}


    def __init__(self) -> None:
        """
        Initialize a new instance of PlainStorage.

        This method initializes an empty dictionary to store entries.
        """
        self._entries = {}


    def add(self, entry: Entry) -> bool:
        """
        Adds an entry's metadata to the storage.

        Args:
            entry (Entry): The Entry object containing metadata.

        Returns:
            (bool): False if an entry with same output name already exists.
        """
        if entry.get("filename") in self._entries:
            return False
        self._entries[entry.get("filename")] = entry
        return True


    def get_entries(self) -> List[Entry]:
        """
        Returns all stored entries' metadata as a list.

        Returns:
            (List[Entry]): The list of entries.
        """
        ret = [entry for filename, entry in self._entries.items()]
        return ret


    def as_json(self, index_indent: int) -> str:
        """
        Returns all stored entries' metadata as a list.

        Args:
            index_indent (int): The indentation level to use for JSON encoding

        Returns:
            (str): Metadata of all entries in JSON format.
        """
        entries = []
        for _, entry in self._entries.items():
            desc = {"date": entry.get_date().isoformat(' '), "title": entry.get("title")}
            if entry.has_key("topics"):
                desc["topics"] = [t.strip() for t in entry.get("topics").split(",")]
            if entry.has_key("abstract"):
                desc["abstract"] = entry.get("abstract")
            desc["filename"] = entry.get_destination()
            entries.append(desc)
        return json.dumps(entries, indent=index_indent)


def load_template(path: str, filename: str):
    """
    Loads a template either from a given path or from
    the data folder.

    Args:
        path (str): The title to apply.
        filename (str): The filename of the entry.

    Returns:
        Template: The loaded template.
    """
    if path is not None:
        template_path = Path(path)
    else:
        template_path = Path(__file__).resolve().parent / "data" / filename
    return Template(template_path.read_text(encoding="utf8"))


def write_list(title: str, dest_path: str, template: Template,
               entries: List[Entry], topic_format: str) -> None:
    """
    Generates an unordered list from the given list of entry metadata,
    embeds it into the given template, and saves the result under the given path.

    Args:
        title (str): The title to apply.
        dest_path (str): The filename of the entry.
        template (Template): The template to fill.
        entries (List[Entry]): A list of entry metadata.
        topic_format (str): The format of topics to use.
        apply_markdown (bool): Whether markdown shall be applied.
        prettifier (Any): The prettyfier to use.
    """
    content = "<ul>\n"
    for entry in entries:
        content += f'  <li><a href="{entry.get_destination()}">{entry.get("title")}</a>'
        content += f' ({entry.get("date")})'
        if entry.has_key("abstract"):
            content += f'<br>{entry.get("abstract")}'
        content += '</li>\n'
    content += "</ul>\n"
    entry_obj = Entry({ "title": title, "content": content })
    rendered = template.embed(entry_obj._fields, topic_format)
    with open(dest_path, "w", encoding="utf-8") as fdo:
        fdo.write(rendered)


def write_feed(storage: PlainStorage, feed_type: str, args: argparse.Namespace,
               dest_path: str) -> None:
    """
    Generates a simple RSS 2.0 or Atom feed listing the entries stored
    in the given storage.

    Args:
        storage (PlainStorage): The storage containing all entries.
        feed_type (str): The type of the feed ('rss' / 'atom').
        args: Additional arguments required for generating the feed.
        dest_path (str): The path to write the RSS feed to.
    """
    templates = [
        load_template(None, f"{feed_type}_head_template.txt"),
        load_template(None, f"{feed_type}_entry_template.txt"),
        load_template(None, f"{feed_type}_foot_template.txt")
    ]
    ident = '  ' if feed_type=='rss' else ''
    #
    params = {k: v for k, v in vars(args).items() if v is not None and isinstance(v, str)}
    params["now"] = email.utils.format_datetime(datetime.datetime.now())
    params["feed_language_short"] = args.feed_language[:2]
    feed_site = args.feed_site.rstrip("/") if args.feed_site is not None else ""
    #
    entries = storage.get_entries()
    entries.sort(key=lambda a:a.get_date())
    #
    feed = templates[0].embed(params, "[[:topic:]]")
    for entry in reversed(entries):
        values = {}
        values["title"] = html.escape(entry.get("title"))
        values["link"] = entry.get_destination()
        if feed_site:
            values["link"] = f"{feed_site}/{entry.get_destination()}"
        if entry.has_key("abstract"):
            values["abstract"] = entry.get("abstract")
        values["date"] = email.utils.format_datetime(entry.get_date())
        if entry.has_key("topics"):
            topics = entry.get("topics").split(",")
            topics = [f'{ident}    <category>{html.escape(topic)}</category>' for topic in topics]
            values["encoded_categories"] = "\n".join(topics)
        entry_rep = templates[1].embed(values, "[[:topic:]]")
        feed += "\n" + entry_rep
    feed += "\n" + templates[2].embed([], "")
    with open(dest_path, "w", encoding="utf-8") as fdo:
        fdo.write(feed)


def get_args(arguments: List[str] = None) -> argparse.Namespace:
    """
    Parse command line arguments.

    Args:
        arguments (List[str]): Command line arguments to parse.

    Returns:
        argparse.Namespace: Parsed command line arguments.
    """
    defaults: Dict[str, Any] = {}
    # parse options
    # https://stackoverflow.com/questions/3609852/which-is-the-best-way-to-allow-configuration-options-be-overridden-at-the-comman
    conf_parser = argparse.ArgumentParser(prog='gresiblos', add_help=False)
    conf_parser.add_argument("-c", "--config", metavar="FILE",
                             help="Reads the named configuration file")
    args, remaining_argv = conf_parser.parse_known_args(arguments)
    if args.config is not None:
        if not os.path.exists(args.config):
            print(f"gresiblos: error: configuration file '{args.config}' does not exist",
                  file=sys.stderr)
            raise SystemExit(2)
        config = configparser.ConfigParser()
        config.read([args.config])
        defaults.update(dict(config.items("gresiblos")))
    parser = argparse.ArgumentParser(prog='gresiblos',
                                     parents=[conf_parser],
                                     description="greyrat's simple blog system",
                                     epilog='(c) Daniel Krajzewicz 2016-2026')
    parser.add_argument("input" if "input" not in defaults else "--input")
    parser.add_argument("-d", "--destination", default="./gresiblos_out",
                        help="Sets the path to store the generated file(s) into")
    parser.add_argument("-t", "--template", default=None,
                        help="Defines the template to use")
    parser.add_argument("-e", "--extension", default="html",
                        help="Sets the extension of the built file(s)")
    parser.add_argument("-s", "--state", default=None,
                        help="Use only files with the given state(s)")
    parser.add_argument("--index-output", default=None,
                        help="Writes the index to the named file")
    parser.add_argument("--chrono-output", default=None,
                        help="Writes the named file with entries in chronological order")
    parser.add_argument("--alpha-output", default=None,
                        help="Writes the named file with entries in alphabetical order")
    parser.add_argument("--markdown", action="store_true",
                        help="If set, markdown is applied on the contents")
    parser.add_argument("--degrotesque", action="store_true",
                        help="If set, degrotesque is applied on the contents and the title")
    parser.add_argument("--topic-format", default="[[:topic:]]",
                        help="Defines how each of the topics is rendered")
    parser.add_argument("--index-indent", type=int, default=None,
                        help="Defines the indent used for the index file")
    parser.add_argument("--date-format", default=None,
                        help="Defines the time format used")
    parser.add_argument("--rss-output", default=None,
                        help="Writes an RSS 2.0 feed to the named file")
    parser.add_argument("--atom-output", default=None,
                        help="Writes an Atom feed to the named file")
    parser.add_argument("--feed-title", default="My Blog",
                        help="Title to use for the feed")
    parser.add_argument("--feed-site", default="",
                        help="Base URL used to prefix entry filenames in the feed")
    parser.add_argument("--feed-description", default=None,
                        help="The feed description")
    parser.add_argument("--feed-editor", default=None,
                        help="The editor of the feed (e-mail)")
    parser.add_argument("--feed-language", default="en-en",
                        help="The language of the feed")
    parser.add_argument("--feed-copyright", default=None,
                        help="The copyright information about the feed")
    parser.add_argument('--version', action='version', version='%(prog)s 0.8.0')
    parser.set_defaults(**defaults)
    args = parser.parse_args(remaining_argv)
    # check
    errors = []
    if not _HAVE_DEGROTESQUE and args.degrotesque:
        errors.append("degrotesque application is set, but degrotesque is not installed")
    if not _HAVE_MARKDOWN and args.markdown:
        errors.append("markdown application is set, but markdown is not installed")
    if len(errors)!=0:
        for error in errors:
            print (f"gresiblos: error: {error}", file=sys.stderr)
        raise SystemExit(2)
    return args


def collect_files_sorted(input_arg: str) -> List[str]:
    """
    Collects the files defined by the given input definition.

    Args:
        input_arg (str): The definition of the files to load.

    Returns:
        (List[str]): The list of collected file names.
    """
    #  https://stackoverflow.com/questions/4568580/python-glob-multiple-filetypes
    input_argument = input_arg.split(",")
    input_file_names: List[str] = []
    for entry in input_argument:
        if os.path.isfile(entry):
            input_file_names.append(entry)
        else:
            input_file_names.extend(glob.glob(entry, recursive=True))
    input_file_names.sort()
    return input_file_names


def main(arguments: List[str] = None) -> int:
    """
    The main method using parameters from the command line.

    Args:
        arguments (List[str]): A list of command line arguments.

    Returns:
        (int): The exit code (0 for success).
    """
    args = get_args(arguments)
    # collect files
    input_file_names = collect_files_sorted(args.input)
    # load template file
    template = load_template(args.template, "template.html")
    # process files
    prettifier = None
    if _HAVE_DEGROTESQUE and args.degrotesque:
        prettifier = degrotesque.Degrotesque()
    apply_markdown = _HAVE_MARKDOWN and args.markdown
    storage = PlainStorage()
    for file in input_file_names:
        print(f"Processing '{file}'")
        entry = Entry()
        entry.load(file, args.date_format, args.extension)
        if args.state is not None and args.state != entry.get("state"):
            print(f" ... skipped for state='{entry.get('state')}'")
            continue
        entry.apply_processors(apply_markdown, prettifier)
        # add to storage
        if not storage.add(entry):
            print ("gresiblos: error: "
                + f"A page with name '{entry.get('filename')}' was already added",
                file=sys.stderr)
            raise SystemExit(1)
        rendered = template.embed(entry._fields, args.topic_format)
        # write file
        dest_path = os.path.join(args.destination, entry.get_destination())
        os.makedirs(os.path.join(os.path.split(dest_path)[0]), exist_ok=True)
        print(f"Writing to {dest_path}")
        with open(dest_path, mode="w", encoding="utf-8") as fdo:
            fdo.write(rendered)
    # (optional) write metadata to a JSON file
    if args.index_output:
        dest_path = os.path.join(args.destination, args.index_output)
        with open(dest_path, "w", encoding="utf-8") as fdo:
            fdo.write(storage.as_json(args.index_indent))
    # (optional) write chronological entries list
    if args.chrono_output:
        dest_path = os.path.join(args.destination, args.chrono_output)
        print(f"Writing chronological list to '{dest_path}'")
        entries = storage.get_entries()
        entries.sort(key=lambda a:a.get_date())
        write_list("entries by publication date", dest_path, template,
            entries, args.topic_format)
    # (optional) write alphabetical entries list
    if args.alpha_output:
        dest_path = os.path.join(args.destination, args.alpha_output)
        print(f"Writing alphabetical list to '{dest_path}'")
        entries = storage.get_entries()
        entries.sort(key=lambda a: a.get("title"))
        write_list("entries by title", dest_path, template,
            entries, args.topic_format)
    # optional: write RSS/Atom feed
    if args.rss_output:
        print(f"Writing RSS feed to '{args.rss_output}'")
        write_feed(storage, "rss", args, args.rss_output)
    if args.atom_output:
        print(f"Writing Atom feed to '{args.atom_output}'")
        write_feed(storage, "atom", args, args.atom_output)
    return 0


def script_run() -> int:
    """Execute from command line."""
    sys.exit(main(sys.argv[1:])) # pragma: no cover


# -- main check
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:])) # pragma: no cover
