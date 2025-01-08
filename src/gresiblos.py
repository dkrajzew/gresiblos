#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
# ===========================================================================
"""gresiblos - greyrat's simple blog system."""
# ===========================================================================
__author__     = "Daniel Krajzewicz"
__copyright__  = "Copyright 2014-2024, Daniel Krajzewicz"
__credits__    = ["Daniel Krajzewicz"]
__license__    = "GPLv3"
__version__    = "0.4.2"
__maintainer__ = "Daniel Krajzewicz"
__email__      = "daniel@krajzewicz.de"
__status__     = "Development"
# ===========================================================================
# - https://github.com/dkrajzew/gresiblos
# - http://www.krajzewicz.de/docs/gresiblos/index.html
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
from typing import List


# --- class definitions -----------------------------------------------------
class Entry:
    """
    Represents a blog entry with metadata and content.

    Attributes:
        _default_author (str): The default author of the entry.
        _default_copyright_date (str): The default copyright date.
        _default_state (str): The default state of the entry.
        _fields (dict): A dictionary to store entry fields.
    """

    def __init__(self, fields=None):
        """
        Initializes an Entry object with default values.

        Args:
            default_author (str): The default author of the entry.
            default_copyright_date (str): The default copyright date.
            default_state (str): The default state of the entry.
        """
        self._fields = {} if fields is None else fields.copy()
        
        
        
    def get(self, key):
        """
        Gets the value of a field by key.

        Args:
            key (str): The key of the field to retrieve.

        Returns:
            str: The value of the field.
        """
        return self._fields[key]


        
    def has_key(self, key):
        """
        Gets the value of a field by key.

        Args:
            key (str): The key of the field to retrieve.

        Returns:
            str: The value of the field.
        """
        return key in self._fields


        
        

    def get_isodate(self, date_format):
        if "date" not in self._fields:
            return None # pragma: no cover
        if date_format is None:
            return self._fields["date"]
        return datetime.datetime.strptime(self._fields["date"], date_format).isoformat(' ')




    def load(self, file):
        """
        Loads entry data from a file.

        Args:
            file (str): The path to the file containing entry data.
        """
        self._fields = {}
        # load
        with open(file, mode="r", encoding="utf-8") as fd:
            is_multi_line = False
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
                if ls[-1]!=':':
                    vs = ls.split(":")
                    self._fields[vs[0]] = ":".join(vs[1:])
                    continue
                key = ls[:-1]
                self._fields[key] = ""
                is_multi_line = True


    def embed(self, template, topics_format):
        """
        Embeds entry data into a template.

        Args:
            template (str): The HTML template to embed data into.
            topics_format (str): The format for topics in the template.

        Returns:
            str: The template with embedded entry data.
        """
        # replace plain, given fields
        for f in self._fields:
            value = self._fields[f]
            if f=="topics":
                topics = self._fields[f].split(",")
                html = []
                for t in topics:
                    t = t.strip()
                    t = topics_format.replace("[[:topic:]]", t)
                    html.append(t)
                value = ", ".join(html)
            elif f=="title" and self._fields["state"]!="release":
                value = "(Draft) " + self._fields[f]
            template = template.replace("[[:"+f+":]]", value)
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
        _meta (dict): A dictionary to store metadata of entries.
    """

    def __init__(self):
        """Initializes a PlainStorage object."""
        self._meta = {}


    def add(self, filename, entry, date_format):
        """
        Adds an entry's metadata to the storage.

        Args:
            filename (str): The filename of the entry.
            entry (Entry): The Entry object containing metadata.
        """
        self._meta[filename] = { }
        if entry.has_key("date"):
            self._meta[filename]["date"] = entry.get_isodate(date_format)
        if entry.has_key("title"):
            self._meta[filename]["title"] = entry.get("title")
        if entry.has_key("topics"):
            self._meta[filename]["topics"] = entry.get("topics").split(",")
        if entry.has_key("abstract"):
            self._meta[filename]["abstract"] = entry.get("abstract")
        self._meta[filename]["filename"] = filename


    def get(self):
        """
        Gets all stored metadata.

        Returns:
            dict: A dictionary of all stored metadata.
        """
        return self._meta



def main(arguments : List[str] = []) -> int:
    """
    The main method using parameters from the command line.

    Args:
        arguments (List[str]): A list of command line arguments.

    Returns:
        int: The exit code (0 for success).
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
                                     epilog='(c) Daniel Krajzewicz 2014-2024')
    parser.add_argument("input")
    parser.add_argument('--version', action='version', version='%(prog)s 0.4.2')
    parser.add_argument("-t", "--template", default="data/template.html", help="Defines the template to use")
    parser.add_argument("-e", "--extension", default="html", help="Sets the extension of the built file(s)")
    parser.add_argument("-s", "--state", default=None, help="Use only files with the given state(s)")
    parser.add_argument("-d", "--destination", default="./", help="Sets the path to store the generated file(s) into")
    parser.add_argument("--topic-format", default="[[:topic:]]", help="Defines how each of the topics is rendered")
    parser.add_argument("--index-indent", type=int, default=None, help="Defines the indent used for the index file")
    parser.add_argument("--date-format", default=None, help="Defines the time format used")
    parser.set_defaults(**defaults)
    args = parser.parse_args(remaining_argv)
    # collect files; https://stackoverflow.com/questions/4568580/python-glob-multiple-filetypes
    files = args.input.split(",")
    nfiles = []
    for file in files:
        if os.path.isfile(file):
            nfiles.append(file)
        else:
            nfiles.extend(glob.glob(file))
    files = nfiles
    files.sort()
    # load template file
    template = ""
    with open(args.template, mode="r", encoding="utf-8") as fd:
        template = fd.read()
    # process files
    storage = PlainStorage()
    for file in files:
        print ("Processing '%s'" % file)
        entry = Entry()
        entry.load(file)
        if args.state is not None and args.state!=entry.get("state"):
            print (" ... skipped for state=%s" % entry.get("state"))
            continue
        c = entry.embed(template, args.topic_format)
        # write file
        filename = f"{entry.get('filename')}.{args.extension}"
        dest_path = os.path.join(args.destination, filename)
        print (f"Writing to {dest_path}")
        with open(dest_path, mode="w", encoding="utf-8") as fdo:
            fdo.write(c)
        # add to topics
        storage.add(filename, entry, args.date_format)
    # write metadata to a JSON file
    dest_path = os.path.join(args.destination, "entries.json")
    meta = storage.get()
    with open(dest_path, "w", encoding="utf-8") as fdo:
        fdo.write(json.dumps(meta, indent=args.index_indent))
    return 0


# -- main check
if __name__ == '__main__':
    ret = main(sys.argv[1:]) # pragma: no cover
    sys.exit(ret) # pragma: no cover

