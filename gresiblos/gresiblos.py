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
from typing import List, Dict, Any
_HAVE_DEGROTESQUE = False
try:
    import degrotesque
    _HAVE_DEGROTESQUE = True
except Exception:
    pass
_HAVE_MARKDOWN = False
try:
    import markdown
    _HAVE_MARKDOWN = True
except Exception:
    pass


# --- class definitions -----------------------------------------------------
class Template:
    def __init__(self, template: str):
        self._template = template

    def embed(self, fields, topics_format: str,
              apply_markdown: bool = False, prettifier: Any = None) -> str:
        # remove optional fields (begin tags with [[:?key:]] ... [[:key?:]])
        entry = self._template
        b = entry.find("[[:?")
        while b >= 0:
            e = entry.find(":]]", b + 4)
            if e < 0:
                print(f"gresiblos: error: Missing ':]]' at the begin tag of an optional document part that starts at {b}", file=sys.stderr)
                raise SystemExit(3)
            field_key = entry[b + 4:e]
            b2 = entry.find("[[:" + field_key + "?:]]")
            if b2 < 0:
                print(f"gresiblos: error: Missing closing tag of an optional document part that starts at {b}; field_key='{field_key}'", file=sys.stderr)
                raise SystemExit(3)
            if field_key not in fields:
                entry = entry[:b] + entry[b2 + len(field_key) + 7:]
                b = entry.find("[[:?", b)
            else:
                entry = entry[:b2] + entry[b2 + len(field_key) + 7:]
                entry = entry[:b] + entry[b + len(field_key) + 7:]
                b = entry.find("[[:?", b)
        # replace plain, given fields
        for field_key in fields:
            value = fields[field_key]
            if field_key in ["content", "title", "abstract"]:
                if apply_markdown:
                    value = markdown.markdown(value)
                    if value.startswith("<p>") and value.endswith("</p>"):
                        value = value[3:-4]
                if prettifier is not None:
                    value = prettifier.prettify(value, True)
            if field_key == "topics":
                topics = fields[field_key].split(",")
                html_topics = []
                for t in topics:
                    t = t.strip()
                    t = topics_format.replace("[[:topic:]]", t)
                    html_topics.append(t)
                value = ", ".join(html_topics)
            elif field_key == "title" and "state" in fields and fields.get("state") != "release":
                value = "(Draft) " + fields[field_key]
            entry = entry.replace("[[:" + field_key + ":]]", value)
        # remove plain, not given fields
        empty_regex = re.compile(r"(\[\[\:[a-zA-Z0-9_]+?\:\]\])", flags=re.MULTILINE)
        entry = empty_regex.sub("", entry)
        # check for replacements with defaults
        opt_regex = re.compile(r"\[\[\:([a-zA-Z0-9_]+?)\|([^\:\]\]]+?)\:\]\]", flags=re.MULTILINE)
        # https://stackoverflow.com/questions/69376798/python3-replace-string-using-dict-with-regex
        entry = opt_regex.sub(lambda x: fields[x.group(1)] if x.group(1) in fields else x.group(2), entry)
        return entry


class Entry:
    """
    Represents a blog entry with metadata and content.

    Attributes:
        _fields (Dict[str, str]): A dictionary to store entry fields.
    """

    def __init__(self, fields: Dict[str, str] = {}):
        """
        Initializes an Entry object with default values.

        Args:
            fields (Dict[str, str]): The entry's meta data and content.
        """
        self._fields = {} if fields is None else fields.copy()


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


    def get_isodate(self, date_format: str) -> str:
        """
        Returns the date in ISO format, if given. Otherwise return None.

        Args:
            date_format (str): The date format if it differs from ISO

        Returns:
            (str): The date in isoformat.
        """
        if "date" not in self._fields:
            return None # pragma: no cover
        if date_format is None:
            return self._fields["date"]
        return datetime.datetime.strptime(self._fields["date"], date_format).isoformat(' ')


    def load(self, filename: str) -> None:
        """
        Loads entry data from a filename.

        Args:
            filename (str): The path to the filename containing entry data.
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
                    # split the line at the first colon. values may contain
                    # additional colons, so join the remainder back together.
                    vs = ls.split(":")
                    # remove leading/trailing whitespace from the value portion.
                    self._fields[vs[0]] = ":".join(vs[1:]).strip()
                    continue
                key = ls[:-1]
                self._fields[key] = ""
                is_multi_line = True
        # add missing fields
        if "filename" not in self._fields:
            fn = os.path.splitext(os.path.split(filename)[1])[0]
            fn = urllib.parse.quote(fn)
            self._fields["filename"] = fn
        if "title" not in self._fields:
            self._fields["title"] = os.path.splitext(os.path.split(filename)[1])[0]
        if "date" not in self._fields:
            t = os.path.getmtime(filename)
            self._fields["date"] = datetime.datetime.fromtimestamp(t).isoformat(' ')


class PlainStorage:
    """
    Stores metadata of blog entries.

    Attributes:
        _meta (Dict[str, Dict[str, str]]): A dictionary to store metadata of entries.
    """

    def __init__(self) -> None:
        """Initializes a PlainStorage object."""
        self._meta: Dict[str, Dict[str, str]] = {}


    def add(self, filename: str, entry: Entry, date_format: str) -> None:
        """
        Adds an entry's metadata to the storage.

        Args:
            filename (str): The filename of the entry.
            entry (Entry): The Entry object containing metadata.
            date_format (str): The date format if it differs from ISO.
        """
        self._meta[filename] = {}
        if entry.has_key("date"):
            self._meta[filename]["date"] = entry.get_isodate(date_format)
        if entry.has_key("title"):
            self._meta[filename]["title"] = entry.get("title")
        if entry.has_key("topics"):
            topics = entry.get("topics")
            self._meta[filename]["topics"] = topics.split(",") if len(topics) != 0 else []
        if entry.has_key("abstract"):
            self._meta[filename]["abstract"] = entry.get("abstract")
        self._meta[filename]["filename"] = filename


    def get_meta(self) -> Dict[str, Dict[str, str]]:
        """
        Returns all stored metadata.

        Returns:
            (Dict[str, Dict[str, str]]): A dictionary of all stored metadata.
        """
        return self._meta


    def _get_entries(self) -> List[Dict[str, str]]:
        """
        Returns all stored entries' metadata as a list.

        Returns:
            (List[Dict[str, str]]): A list of entry metadata
        """
        ret = []
        for f in self._meta:
            ret.append(self._meta[f])
        return ret


    def get_entries_chronological(self) -> List[Dict[str, str]]:
        """
        Returns all stored entries' metadata as a list, sorted by date.

        Returns:
            (List[Dict[str, str]]): A list of entry metadata
        """
        ret = self._get_entries()
        ret.sort(key=lambda a: datetime.datetime.fromisoformat(a["date"]))
        return ret


    def get_entries_alphabetical(self) -> List[Dict[str, str]]:
        """
        Returns all stored entries' metadata as a list, sorted by title (alphabetic).

        Returns:
            (List[Dict[str, str]]): A list of entry metadata
        """
        ret = self._get_entries()
        ret.sort(key=lambda a: a["title"])
        return ret


def write_list(title: str, dest_path: str, template: Template,
               entries: List[Dict[str, str]], topic_format: str,
               apply_markdown: bool, prettifier: Any) -> None:
    """
    Generates an unordered list from the given list of entry metadata,
    embeds it into the given template, and saves the result under the given path.

    Args:
        title (str): The title to apply.
        dest_path (str): The filename of the entry.
        template (str): The template to fill.
        entries (List[Dict[str, str]]): A list of entry metadata.
        topic_format (str): The format of topics to use.
        apply_markdown (bool): Whether markdown shall be applied.
        prettifier (Any): The prettyfier to use.
    """
    content = "<ul>\n"
    for entry in entries:
        content += f'  <li><a href="{entry["filename"]}">{entry["title"]}</a>'
        if "date" in entry and entry["date"]:
            content += f' ({entry["date"]})'
        if "abstract" in entry and entry["abstract"]:
            content += f'<br>{entry["abstract"]}'
        content += '</li>\n'
    content += "</ul>\n"
    fields = {
        "title": title,
        "content": content
    }
    entry_obj = Entry(fields)
    rendered = template.embed(entry_obj._fields, topic_format, apply_markdown, prettifier)
    with open(dest_path, "w", encoding="utf-8") as fdo:
        fdo.write(rendered)


def write_rss(dest_path, entries: List[Dict[str, Any]], args) -> None:
    """
    Generates a simple RSS 2.0 feed from the given list of entry metadata and writes it to dest_path.

    Args:
        entries (List[Dict[str, Any]]): A list of entry metadata dictionaries.
    """
    feed_site = args.feed_site.rstrip("/") if args.feed_site is not None else ""
    lines: List[str] = []
    lines.append('<?xml version="1.0" encoding="UTF-8"?>')
    lines.append('<rss version="2.0">')
    lines.append('  <channel>')
    lines.append(f'    <title>{html.escape(args.feed_title)}</title>')
    lines.append(f'    <link>{html.escape(feed_site)}/</link>')
    if args.feed_description is not None:
        lines.append(f'    <description>{html.escape(args.feed_description)}</description>')
    if args.feed_editor is not None:
        lines.append(f'    <managingEditor>{html.escape(args.feed_editor)}</managingEditor>')
    if args.feed_language is not None:
        lines.append(f'    <language>{html.escape(args.feed_language)}</language>')
    if args.feed_copyright is not None:
        lines.append(f'    <copyright>{html.escape(args.feed_copyright)}</copyright>')
    # Most recent entries first
    for entry in reversed(entries):
        if "title" not in entry or "filename" not in entry:
            continue # pragma: no cover
        lines.append('    <item>')
        lines.append(f'      <title>{html.escape(entry["title"])}</title>')
        link = entry["filename"]
        if feed_site:
            link = f"{feed_site}/{link}"
        lines.append(f'      <link>{html.escape(link)}</link>')
        if "abstract" in entry and entry["abstract"]:
            lines.append(f'      <description>{html.escape(entry["abstract"])}</description>')
        if "date" in entry and entry["date"] is not None:
            try:
                dt = datetime.datetime.fromisoformat(entry["date"])
                pub_date = email.utils.format_datetime(dt)
                lines.append(f'      <pubDate>{pub_date}</pubDate>')
            except Exception: # pragma: no cover
                pass # pragma: no cover
        if "topics" in entry:
            topics = entry["topics"] if isinstance(entry["topics"], list) else entry["topics"].split(",")
            for topic in topics:
                topic = topic.strip()
                if topic:
                    lines.append(f'      <category>{html.escape(topic)}</category>')
        lines.append('    </item>')
    lines.append('  </channel>')
    lines.append('</rss>')
    lines.append('')
    with open(dest_path, "w", encoding="utf-8") as fdo:
        fdo.write('\n'.join(lines))


def write_atom(dest_path, entries: List[Dict[str, Any]], args) -> None:
    """
    Generates a simple Atom feed from the given list of entry metadata and writes it to dest_path.

    Args:
        entries (List[Dict[str, Any]]): A list of entry metadata dictionaries.
    """
    feed_site = args.feed_site.rstrip("/") if args.feed_site is not None else ""
    lines: List[str] = []
    lines.append('<?xml version="1.0" encoding="utf-8"?>')
    lines.append('<feed xmlns="http://www.w3.org/2005/Atom">')
    lines.append(f'  <title type="text">{html.escape(args.feed_title)}</title>')
    lines.append(f'  <updated>{email.utils.format_datetime(datetime.datetime.now())}</updated>')
    lines.append(f'  <link href="{html.escape(feed_site)}"/>')
    lines.append(f'  <link rel="alternate" type="text/html" hreflang="{html.escape(args.feed_language[:2])}" href="{html.escape(feed_site)}"/>')
    if args.feed_editor is not None:
        lines.append(f'    <author><email>{html.escape(args.feed_editor)}</email></author>')
    if args.feed_copyright is not None:
        lines.append(f'    <rights>{html.escape(args.feed_copyright)}</rights>')
    lines.append(f'  <generator uri="https://github.com/dkrajzew/gresiblos/" version="0.10.0">gresiblos</generator>')
    # Most recent entries first
    for entry in reversed(entries):
        if "title" not in entry or "filename" not in entry:
            continue # pragma: no cover
        lines.append('  <entry>')
        lines.append(f'    <title type="text">{html.escape(entry["title"])}</title>')
        link = entry["filename"]
        if feed_site:
            link = f"{feed_site}/{link}"
        lines.append(f'    <link href="{html.escape(link)}"/>')
        if "abstract" in entry and entry["abstract"]:
            lines.append(f'    <summary>{html.escape(entry["abstract"])}</summary>')
        if "date" in entry and entry["date"] is not None:
            try:
                dt = datetime.datetime.fromisoformat(entry["date"])
                pub_date = email.utils.format_datetime(dt)
                lines.append(f'    <published>{pub_date}</published>')
            except Exception: # pragma: no cover
                pass # pragma: no cover
        if "topics" in entry:
            topics = entry["topics"] if isinstance(entry["topics"], list) else entry["topics"].split(",")
            for topic in topics:
                topic = topic.strip()
                if topic:
                    lines.append(f'    <category>{html.escape(topic)}</category>')
        lines.append('  </entry>')
    lines.append('</rss>')
    lines.append('')
    with open(dest_path, "w", encoding="utf-8") as fdo:
        fdo.write('\n'.join(lines))
        
        
        
def main(arguments: List[str] = None) -> int:
    """
    The main method using parameters from the command line.

    Args:
        arguments (List[str]): A list of command line arguments.

    Returns:
        (int): The exit code (0 for success).
    """
    defaults: Dict[str, Any] = {}
    # parse options
    # https://stackoverflow.com/questions/3609852/which-is-the-best-way-to-allow-configuration-options-be-overridden-at-the-comman
    conf_parser = argparse.ArgumentParser(prog='gresiblos', add_help=False)
    conf_parser.add_argument("-c", "--config", metavar="FILE", help="Reads the named configuration file")
    args, remaining_argv = conf_parser.parse_known_args(arguments)
    if args.config is not None:
        if not os.path.exists(args.config):
            print(f"gresiblos: error: configuration file '{args.config}' does not exist", file=sys.stderr)
            raise SystemExit(2)
        config = configparser.ConfigParser()
        config.read([args.config])
        defaults.update(dict(config.items("gresiblos")))
    parser = argparse.ArgumentParser(prog='gresiblos',
                                     parents=[conf_parser],
                                     description="greyrat's simple blog system",
                                     epilog='(c) Daniel Krajzewicz 2016-2026')
    parser.add_argument("input" if "input" not in defaults else "--input")
    parser.add_argument("-d", "--destination", default="./gresiblos_out", help="Sets the path to store the generated file(s) into")
    parser.add_argument("-t", "--template", default=None, help="Defines the template to use")
    parser.add_argument("-e", "--extension", default="html", help="Sets the extension of the built file(s)")
    parser.add_argument("-s", "--state", default=None, help="Use only files with the given state(s)")
    parser.add_argument("--index-output", default=None, help="Writes the index to the named file")
    parser.add_argument("--chrono-output", default=None, help="Writes the named file with entries in chronological order")
    parser.add_argument("--alpha-output", default=None, help="Writes the named file with entries in alphabetical order")
    parser.add_argument("--markdown", action="store_true", help="If set, markdown is applied on the contents")
    parser.add_argument("--degrotesque", action="store_true", help="If set, degrotesque is applied on the contents and the title")
    parser.add_argument("--topic-format", default="[[:topic:]]", help="Defines how each of the topics is rendered")
    parser.add_argument("--index-indent", type=int, default=None, help="Defines the indent used for the index file")
    parser.add_argument("--date-format", default=None, help="Defines the time format used")
    parser.add_argument("--rss-output", default=None, help="Writes an RSS 2.0 feed to the named file")
    parser.add_argument("--atom-output", default=None, help="Writes an Atom feed to the named file")
    parser.add_argument("--feed-title", default="My Blog", help="Title to use for the feed")
    parser.add_argument("--feed-site", default="", help="Base URL used to prefix entry filenames in the feed")
    parser.add_argument("--feed-description", default=None, help="The feed description")
    parser.add_argument("--feed-editor", default=None, help="The editor of the feed (e-mail)")
    parser.add_argument("--feed-language", default="en-en", help="The language of the feed")
    parser.add_argument("--feed-copyright", default=None, help="The copyright information about the feed")
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
    # collect files; https://stackoverflow.com/questions/4568580/python-glob-multiple-filetypes
    input_argument = args.input.split(",")
    input_file_names: List[str] = []
    for entry in input_argument:
        if os.path.isfile(entry):
            input_file_names.append(entry)
        else:
            input_file_names.extend(glob.glob(entry, recursive=True))
    input_file_names.sort()
    # load template file
    template_path = args.template
    if template_path is None:
        template_path = os.path.join(os.path.split(__file__)[0], "data", "template.html")
    template_str = ""
    with open(template_path, mode="r", encoding="utf-8") as fd:
        template_str = fd.read()
    template = Template(template_str)
    # process files
    prettifier = None if (not _HAVE_DEGROTESQUE or not args.degrotesque) else degrotesque.Degrotesque()
    apply_markdown = _HAVE_MARKDOWN and args.markdown
    storage = PlainStorage()
    for file in input_file_names:
        print(f"Processing '{file}'")
        entry = Entry()
        entry.load(file)
        if args.state is not None and args.state != entry.get("state"):
            print(f" ... skipped for state='{entry.get('state')}'")
            continue
        rendered = template.embed(entry._fields, args.topic_format, apply_markdown, prettifier)
        # write file
        filename = f"{entry.get('filename')}.{args.extension}"
        dest_path = os.path.join(args.destination, filename)
        os.makedirs(os.path.join(os.path.split(dest_path)[0]), exist_ok=True)
        print(f"Writing to {dest_path}")
        with open(dest_path, mode="w", encoding="utf-8") as fdo:
            fdo.write(rendered)
        # add to storage
        storage.add(filename, entry, args.date_format)
    # (optional) write metadata to a JSON file
    if args.index_output:
        dest_path = os.path.join(args.destination, args.index_output)
        meta = storage.get_meta()
        with open(dest_path, "w", encoding="utf-8") as fdo:
            fdo.write(json.dumps(meta, indent=args.index_indent))
    # (optional) write chronological entries list
    if args.chrono_output:
        dest_path = os.path.join(args.destination, args.chrono_output)
        print(f"Writing chronological list to '{dest_path}'")
        entries = storage.get_entries_chronological()
        write_list("entries by publication date", dest_path, template, entries, args.topic_format, apply_markdown, prettifier)
    # (optional) write alphabetical entries list
    if args.alpha_output:
        dest_path = os.path.join(args.destination, args.alpha_output)
        print(f"Writing alphabetical list to '{dest_path}'")
        entries = storage.get_entries_alphabetical()
        write_list("entries by title", dest_path, template, entries, args.topic_format, apply_markdown, prettifier)
    # optional: write RSS/Atom feed
    if args.rss_output:
        dest_path = os.path.join(args.destination, args.rss_output)
        entries = storage.get_entries_chronological()
        write_rss(dest_path, entries, args)
        print(f"Writing RSS feed to '{dest_path}'")
    if args.atom_output:
        dest_path = os.path.join(args.destination, args.atom_output)
        entries = storage.get_entries_chronological()
        write_atom(dest_path, entries, args)
        print(f"Writing Atom feed to '{dest_path}'")
    return 0


def script_run() -> int:
    """Execute from command line."""
    sys.exit(main(sys.argv[1:])) # pragma: no cover


# -- main check
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:])) # pragma: no cover
