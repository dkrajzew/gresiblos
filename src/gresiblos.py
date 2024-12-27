#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
# ===========================================================================
"""gresiblos - greyrat's simple blog system."""
# ===========================================================================
__author__     = "Daniel Krajzewicz"
__copyright__  = "Copyright 2014-2024, Daniel Krajzewicz"
__credits__    = ["Daniel Krajzewicz"]
__license__    = "BSD"
__version__    = "0.2.0"
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
from typing import List


# --- defaults --------------------------------------------------------------
class Entry:
    def __init__(self, default_author, default_copyright_date, default_state):
        self._default_author = default_author
        self._default_copyright_date = default_copyright_date
        self._default_state = default_state
        self._init_fields()
        
        
    def _init_fields(self):
        self._fields = {}
        self._fields["state"] = self._default_state
        self._fields["includes"] = ""
        self._fields["js_inits"] = ""
        self._fields["copyright_date"] = self._default_copyright_date
        self._fields["author"] = self._default_author

    def get(self, key):
        return self._fields[key]


    def load(self, file):
        self._init_fields()
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


    def embed(self, template):
        topcis = []
        for f in self._fields:
            if f=="topics":
                topics = self._fields[f].split(",")
                html = []
                for t in topics:
                    t = t.strip()
                    # !!! html.append('<a href="topic_%s.html">%s</a>' % (t, t))
                    html.append(t)
                html = ", ".join(html)
                template = template.replace("%"+f+"%", html)
            elif f=="title" and self._fields["state"]!="release":
                template = template.replace("%"+f+"%", "(Draft) " + self._fields[f])
            else:
                template = template.replace("%"+f+"%", self._fields[f])
        return template, topics




def main(arguments : List[str] = []) -> int:
    """The main method using parameter from the command line.

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
    parser.add_argument('--version', action='version', version='%(prog)s 0.2.0')
    parser.add_argument("-t", "--template", default="data/template.html", help="Defines the template to use")
    parser.add_argument("-e", "--extension", default="html", help="Sets the extension of the built file(s)")
    parser.add_argument("-s", "--state", default=None, help="Use only files with the given state(s)")
    parser.add_argument("-d", "--destination", default="./", help="Sets the path to store the generated file(s) into")
    parser.add_argument("--default-author", default="", help="Sets the default author")
    parser.add_argument("--default-copyright-date", default="", help="Sets the default copyright date")
    parser.add_argument("--default-state", default="", help="Sets the default state")
    parser.set_defaults(**defaults)
    args = parser.parse_args(remaining_argv)
    # collect files; https://stackoverflow.com/questions/4568580/python-glob-multiple-filetypes
    files = args.input.split(",")
    nfiles = []
    for glob_pattern in files:
        if os.path.isfile(glob_pattern):
            nfiles.append(glob_pattern)
        else:
            nfiles.extend(glob.glob(glob_pattern))
    files = nfiles
    # load files
    template = ""
    with open(args.template, mode="r", encoding="utf-8") as fd:
        template = fd.read()
    # process files
    topics = {}
    for file in files:
        print ("Processing '%s'" % file)
        entry = Entry(args.default_author, args.default_copyright_date, args.default_state)
        entry.load(file)
        if args.state is not None and args.state!=entry.get("state"):
            print (" ... skipped for state=%s" % entry.get("state"))
            continue
        c, doc_topics = entry.embed(template)
        # write file
        filename = f"{entry.get('filename')}.{args.extension}"
        dest_path = os.path.join(args.destination, filename)
        print (f"Writing to {dest_path}")
        with open(dest_path, mode="w", encoding="utf-8") as fdo:
            fdo.write(c)
        # add to topics
        for topic in doc_topics:
            if topic not in topics:
                topics[topic] = []
            topics[topic].append(filename)
    return 0


# -- main check
if __name__ == '__main__':
    ret = main(sys.argv[1:]) # pragma: no cover
    sys.exit(ret) # pragma: no cover
