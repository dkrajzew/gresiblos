#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""gresiblos - greyrat's simple blog system.

gresiblos is implemented in Python. It is started on the command line.

gresiblos reads one or multiple blog entry files and embeds them into a template. The template file to use is defined using the option --template <TEMPLATE\> / -t <TEMPLATE\>.

Generated pages are saved as .html-files per default. You may change it (e.g. to php) using the option --extension <EXTENSION\> / -e <EXTENSION\>.

The entries may include the meta-information state. You may filter entries to process by setting the option --state <STATE\> / -s <STATE\> to the one that shall be processed.

The path to store the generated pages into can be defined using the option --destination <PATH\> / -d <PATH\>. The default is ./.

Besides the generated entries, _gresiblos__ may generate a json-index file that lists the entries with some meta-information. The option --index-output <FILE\> will generate the index and save it under the given file name. The index is usually stored as plain json in a single line. For a prettier output, the indentation can be changed using the option --index-indent <INT\>.

In addition, files that contain the list of entries embedded into the content section of the template file can be generated. Use the option --chrono-output <FILE\> to generate a file with the entries sorted in chronological order and/or the option --alpha-output <FILE\> with the entries sorted alphabetically.

To convert contents from markdown to HTML before embedding them, use the option --markdown. When set, the content, the title, and the abstract will be converted. Use the option --degrotesque to apply the degrotesque type setter on the contents before embedding them. Please note that you need to install markdown and/or degrotesque by yourself.

When embedding the meta-information of single blog entries into the template, the topics are split and rendered individually before being embedded. To allow for using them as links, the rendering format can be set using the option --topic-format <TOPIC_FORMAT\>. Please note that this string should include something like “[[:topic:]]”, what is replaced by the topic itself. The date meta information is assumed to be in ISO-format (e.g. 2025-01-08 19:26:00), but may be adapted using the option --date-format <DATE_FORMAT\>.

The entry/entries to process are given as the last parameter. Multiple entries can be given divided by a ‘,’. Wildcards are accepted as well, so giving ./entries/*.txt will process all files with the extension .txt within the folder entries.

The options can be stored in a configuration file which can be passed to gresiblos using the option --config <CONFIGURATION\> / -c <CONFIGURATION\>. Options given on the command line will overwrite the options set in the configuration file.
Examples

python gresiblos ./entries/*

Generates pages using the default template ./data/template.html and the blog entries located in entries and writes them to ./.

python gresiblos --template mytemplate.html --state release ./entries/*

Generates pages using the template mytemplate.html and the blog entries located in entries and writes them to ./. Processes only entries with state=release.
Command line arguments

The script can be started on the command line with the following options:

* --config <CFG_FILE\> / -c <CFG_FILE\>: Reads the named configuration file
* --template <TEMPLATE_FILE\> / -t <TEMPLATE_FILE\>: Uses the named template file
* --extension <EXTENSION\> / -e <EXTENSION\>: The extension to use for the generated files
* --state <STATE\> / -s <STATE\>: The state the entries must have for being processed
* --destination <PATH\> / -d <PATH\>: The path to save the generated file(s) into
* --index-output <FILE\>: The name of the file to write the index containing information about the entries to
* --chrono-output <FILE\>: The name of the file with the list of entries, sorted in chronological order, embedded into the template to
* --alpha-output <FILE\>: The name of the file with the list of entries, sorted in alphabetically, embedded into the template to
* --markdown: When set, the contents, the title, and the abstract are converted from markdown to HTML
* --degrotesque: When set, the degrotesque type setter is applied
* --topic-format <TOPIC_FORMAT\>: Defines how each of the topics is rendered
* --index-indent <INT\>: Defines the indent used for the index file
* --date-format <DATE_FORMAT\>: Defines the time format used
* --help / -h: Show a help message
* --version: Show the version information

gresiblos requires one parameter:

* input: The files (entries) to read, separated by ‘,’; accepts wildcards as well
"""
# ===========================================================================
__author__     = "Daniel Krajzewicz"
__copyright__  = "Copyright 2016-2025, Daniel Krajzewicz"
__credits__    = "Daniel Krajzewicz"
__license__    = "BSD"
__version__    = "0.4.2"
__maintainer__ = "Daniel Krajzewicz"
__email__      = "daniel@krajzewicz.de"
__status__     = "Production"
# ===========================================================================
# - https://github.com/dkrajzew/gresiblos
# - http://www.krajzewicz.de
# ===========================================================================


# --- imports ---------------------------------------------------------------
import os
import shutil
import time
import sys
import argparse
import configparser
import glob
import json
import re
import datetime
import urllib.parse
from typing import List
from typing import Dict
_have_degrotesque = False
try: 
    import degrotesque
    _have_degrotesque = True
except: pass
_have_markdown = False
try: 
    import markdown
    _have_markdown = True
except: pass


# --- class definitions -----------------------------------------------------
class Entry:
    """
    Represents a blog entry with metadata and content.

    Attributes:
        _fields (Dict[str, str]): A dictionary to store entry fields.
    """

    def __init__(self, fields : Dict[str, str]=None):
        """
        Initializes an Entry object with default values.

        Args:
            fields (Dict[str, str]): The entry's meta data and content.
        """
        self._fields = {} if fields is None else fields.copy()


    def get(self, key : str) -> str:
        """
        Returns the value of a field by key.

        Args:
            key (str): The key of the field to retrieve.

        Returns:
            (str): The value of the field.
        """
        return self._fields[key]


    def has_key(self, key : str) -> bool:
        """
        Returns whether the key is known.

        Args:
            key (str): The key of the field to check for.

        Returns:
            (bool): Whether the named field is stored.
        """
        return key in self._fields


    def get_isodate(self, date_format : str) -> str:
        """
        Returns the date in isoformat, if given. Otherwise return None.

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


    def load(self, filename : str):
        """
        Loads entry data from a filename.

        Args:
            filename (str): The path to the filename containing entry data.
        """
        self._fields = {}
        # load
        with open(filename, mode="r", encoding="utf-8") as fd:
            is_multi_line = False
            first = True
            for line in fd:
                ls = line.strip()
                if is_multi_line:
                    if ls=='===':
                        is_multi_line = False
                        continue
                    self._fields[key] = self._fields[key] + line
                    continue
                if len(ls)==0:
                    continue
                if first and line.find(":")<0:
                    is_multi_line = True
                    key = "content"
                    self._fields[key] = line
                    first = False
                    continue
                first = False
                if ls[-1]!=':':
                    vs = ls.split(":")
                    self._fields[vs[0]] = ":".join(vs[1:])
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


    def embed(self, template : str, topics_format : str, apply_markdown : bool=False, prettifier : degrotesque.Degrotesque=None) -> str:
        """
        Embeds entry data into a template.

        Args:
            template (str): The HTML template to embed data into.
            topics_format (str): The format for topics in the template.
            apply_markdown (bool): Whether the content/title/abstract shall be parsed as markdown.
            prettifier (degrotesque.Degrotesque): The degrotesque instance to prettify the content/title/abstract.

        Returns:
            (str): The template with embedded entry data.
        """
        # remove optional fields
        b = template.find("[[:?")
        while b>=0:
            e = template.find(":]]", b+4)
            if e<0:
                print (f"gresiblos: error: Missing ':]]' at the begin tag of an optional document part that starts at {b}", file=sys.stderr)
                raise SystemExit(3)
            field_key = template[b+4:e]
            b2 = template.find("[[:" + field_key + "?:]]")
            if b2<0:
                print (f"gresiblos: error: Missing closing tag of an optional document part that starts at {b}; field_key='{field_key}'", file=sys.stderr)
                raise SystemExit(3)
            if field_key not in self._fields:
                template = template[:b] + template[b2+len(field_key)+7:]
                b = template.find("[[:?", b)
            else:
                template = template[:b2] + template[b2+len(field_key)+7:]
                template = template[:b] + template[b+len(field_key)+7:]
                b = template.find("[[:?", b)
        # replace plain, given fields
        for field_key in self._fields:
            value = self._fields[field_key]
            if field_key=="content" or field_key=="title" or field_key=="abstract":
                if apply_markdown:
                    value = markdown.markdown(value)
                    if value.startswith("<p>") and value.endswith("</p>"):
                        value = value[3:-4]
                if prettifier is not None:
                    value = prettifier.prettify(value, True)
            if field_key=="topics":
                topics = self._fields[field_key].split(",")
                html = []
                for t in topics:
                    t = t.strip()
                    t = topics_format.replace("[[:topic:]]", t)
                    html.append(t)
                value = ", ".join(html)
            elif field_key=="title" and "state" in self._fields and self._fields["state"]!="release":
                value = "(Draft) " + self._fields[field_key]
            template = template.replace("[[:"+field_key+":]]", value)
        # remove plain, not given fields
        empty_regex = re.compile(r"(\[\[\:[a-zA-Z0-9_]+?\:\]\])", flags=re.MULTILINE)
        template = empty_regex.sub("", template)
        # check for replacements with defaults
        opt_regex = re.compile(r"\[\[\:([a-zA-Z0-9_]+?)\|([^\:\]\]]+?)\:\]\]", flags=re.MULTILINE)
        # https://stackoverflow.com/questions/69376798/python3-replace-string-using-dict-with-regex
        template = opt_regex.sub(lambda x: self._fields[x.group(1)] if x.group(1) in self._fields else x.group(2), template)
        return template



class PlainStorage:
    """
    Stores metadata of blog entries.

    Attributes:
        _meta (Dict[str, Dict[str, str]]): A dictionary to store metadata of entries.
    """

    def __init__(self):
        """Initializes a PlainStorage object."""
        self._meta = {}


    def add(self, filename : str, entry : Entry, date_format : str):
        """
        Adds an entry's metadata to the storage.

        Args:
            filename (str): The filename of the entry.
            entry (Entry): The Entry object containing metadata.
            date_format (str): The date format if it differs from ISO
        """
        self._meta[filename] = {}
        if entry.has_key("date"):
            self._meta[filename]["date"] = entry.get_isodate(date_format)
        if entry.has_key("title"):
            self._meta[filename]["title"] = entry.get("title")
        if entry.has_key("topics"):
            topics = entry.get("topics")
            self._meta[filename]["topics"] = topics.split(",") if len(topics)!=0 else []
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



def write_list(title : str, dest_path : str, template : str, entries : List[Dict[str, str]], topic_format : str, apply_markdown : bool, prettifier : degrotesque.Degrotesque):
    """
    Generates an unordered list from the given list of entry metadata, embeds
    it into the given template, and saves the result under the given path.

    Args:
        title (str): The title to apply.
        dest_path (str): The filename of the entry.
        template (str): The template to fill.
        entries (List[Dict[str, str]]): A list of entry metadata.
        topic_format (str): The format of topics to use.
        apply_markdown (bool): Whether markdown shall be applied.
        prettifier (degrotesque.Degrotesque): The prettyfier to use.
    """
    content = "<ul>\n"
    for entry in entries:
        content = content + f'  <li><a href="{entry["filename"]}">{entry["title"]}</a>'
        if "date" in entry and len(entry["date"])>0:
            content = content + f' ({entry["date"]})'
        if "abstract" in entry and len(entry["abstract"])>0:
            content = content + f'<br>{entry["abstract"]}'
        content = content + '</li>\n'
    content += "</ul>\n"
    fields = {
        "title": title,
        "content": content
    }
    entry = Entry(fields)
    c = entry.embed(template, topic_format, apply_markdown, prettifier)
    with open(dest_path, "w", encoding="utf-8") as fdo:
        fdo.write(c)


def main(arguments : List[str] = []) -> int:
    """
    The main method using parameters from the command line.

    Args:
        arguments (List[str]): A list of command line arguments.

    Returns:
        (int): The exit code (0 for success).
    """
    # parse options
    # https://stackoverflow.com/questions/3609852/which-is-the-best-way-to-allow-configuration-options-be-overridden-at-the-comman
    defaults = {}
    conf_parser = argparse.ArgumentParser(prog='gresiblos', add_help=False)
    conf_parser.add_argument("-c", "--config", metavar="FILE", help="Reads the named configuration file")
    args, remaining_argv = conf_parser.parse_known_args(arguments)
    if args.config is not None:
        if not os.path.exists(args.config):
            print ("gresiblos: error: configuration file '%s' does not exist" % str(args.config), file=sys.stderr)
            raise SystemExit(2)
        config = configparser.ConfigParser()
        config.read([args.config])
        defaults.update(dict(config.items("gresiblos")))
    parser = argparse.ArgumentParser(prog='gresiblos', parents=[conf_parser],
                                     description='greyrat\'s simple blog system',
                                     epilog='(c) Daniel Krajzewicz 2016-2025')
    parser.add_argument("input")
    parser.add_argument('--version', action='version', version='%(prog)s 0.4.2')
    parser.add_argument("-t", "--template", default=None, help="Defines the template to use")
    parser.add_argument("-e", "--extension", default="html", help="Sets the extension of the built file(s)")
    parser.add_argument("-s", "--state", default=None, help="Use only files with the given state(s)")
    parser.add_argument("-d", "--destination", default="./gresiblos_out", help="Sets the path to store the generated file(s) into")
    parser.add_argument("--index-output", default=None, help="Writes the index to the named file")
    parser.add_argument("--chrono-output", default=None, help="Writes the named file with entries in chronological order")
    parser.add_argument("--alpha-output", default=None, help="Writes the named file with entries in alphabetical order")
    parser.add_argument("--markdown", action="store_true", help="If set, markdown is applied on the contents")
    parser.add_argument("--degrotesque", action="store_true", help="If set, degrotesque is applied on the contents and the title")
    parser.add_argument("--topic-format", default="[[:topic:]]", help="Defines how each of the topics is rendered")
    parser.add_argument("--index-indent", type=int, default=None, help="Defines the indent used for the index file")
    parser.add_argument("--date-format", default=None, help="Defines the time format used")
    parser.set_defaults(**defaults)
    args = parser.parse_args(remaining_argv)
    # check
    ok = True
    if not _have_degrotesque and args.degrotesque:
        print ("gresiblos: error: degrotesque application is set, but degrotesque is not installed", file=sys.stderr)
        ok = False
    if not _have_markdown and args.markdown:
        print ("gresiblos: error: markdown application is set, but markdown is not installed", file=sys.stderr)
        ok = False
    if not ok:
        raise SystemExit(2)
    # collect files; https://stackoverflow.com/questions/4568580/python-glob-multiple-filetypes
    files = args.input.split(",")
    nfiles = []
    for file in files:
        if os.path.isfile(file):
            nfiles.append(file)
        else:
            nfiles.extend(glob.glob(file, recursive=True))
    files = nfiles
    files.sort()
    # load template file
    template_path = args.template
    if template_path is None:
        template_path = os.path.join(os.path.split(__file__)[0], "..", "data", "template.html")
    template = ""
    with open(template_path, mode="r", encoding="utf-8") as fd:
        template = fd.read()
    # process files
    prettifier = None if not _have_degrotesque or not args.degrotesque else degrotesque.Degrotesque()
    #if prettifier:
    #    prettifier.set_format("html")
    apply_markdown = _have_markdown and args.markdown
    storage = PlainStorage()
    for file in files:
        print (f"Processing '{file}'")
        entry = Entry()
        entry.load(file)
        if args.state is not None and args.state!=entry.get("state"):
            print (f" ... skipped for state='{entry.get('state')}'")
            continue
        c = entry.embed(template, args.topic_format, apply_markdown, prettifier)
        # write file
        filename = f"{entry.get('filename')}.{args.extension}"
        dest_path = os.path.join(args.destination, filename)
        os.makedirs(os.path.join(os.path.split(dest_path)[0]), exist_ok=True)
        print (f"Writing to {dest_path}")
        with open(dest_path, mode="w", encoding="utf-8") as fdo:
            fdo.write(c)
        # add to topics
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
        print (f"Writing chronological list to '{dest_path}'")
        entries = storage.get_entries_chronological()
        write_list("entries by name", dest_path, template, entries, args.topic_format, apply_markdown, prettifier)
    # (optional) write alphabetical entries list
    if args.alpha_output:
        dest_path = os.path.join(args.destination, args.alpha_output)
        print (f"Writing alphabetical list to '{dest_path}'")
        entries = storage.get_entries_alphabetical()
        write_list("entries by publication date", dest_path, template, entries, args.topic_format, apply_markdown, prettifier)
    return 0


# -- main check
if __name__ == '__main__':
    ret = main(sys.argv[1:]) # pragma: no cover
    sys.exit(ret) # pragma: no cover

