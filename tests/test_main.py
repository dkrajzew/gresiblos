#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
"""gresiblos - Tests for the main method."""
# =============================================================================
__author__     = "Daniel Krajzewicz"
__copyright__  = "Copyright 2024-2025, Daniel Krajzewicz"
__credits__    = ["Daniel Krajzewicz"]
__license__    = "BSD"
__version__    = "0.8.0"
__maintainer__ = "Daniel Krajzewicz"
__email__      = "daniel@krajzewicz.de"
__status__     = "Production"
# ===========================================================================
# - https://github.com/dkrajzew/gresiblos
# - http://www.krajzewicz.de
# ===========================================================================


# --- imports ---------------------------------------------------------------
import sys
import os
sys.path.append(os.path.join(os.path.split(__file__)[0], "..", "gresiblos"))
from util import pname
import gresiblos



# --- test functions ----------------------------------------------------------
def test_main_empty1(capsys):
    """Test behaviour if no arguments are given"""
    try:
        ret = gresiblos.main([])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==2
    captured = capsys.readouterr()
    assert pname(captured.err) == """usage: gresiblos [-h] [-c FILE] [--version] [-t TEMPLATE] [-e EXTENSION]
                 [-s STATE] [-d DESTINATION] [--index-output INDEX_OUTPUT]
                 [--chrono-output CHRONO_OUTPUT] [--alpha-output ALPHA_OUTPUT]
                 [--markdown] [--degrotesque] [--topic-format TOPIC_FORMAT]
                 [--index-indent INDEX_INDENT] [--date-format DATE_FORMAT]
                 input
gresiblos: error: the following arguments are required: input
"""
    assert pname(captured.out) == ""
    

def test_main_empty2(capsys):
    """Test behaviour if no arguments are given"""
    try:
        ret = gresiblos.main()
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==2
    captured = capsys.readouterr()
    assert pname(captured.err) == """usage: gresiblos [-h] [-c FILE] [--version] [-t TEMPLATE] [-e EXTENSION]
                 [-s STATE] [-d DESTINATION] [--index-output INDEX_OUTPUT]
                 [--chrono-output CHRONO_OUTPUT] [--alpha-output ALPHA_OUTPUT]
                 [--markdown] [--degrotesque] [--topic-format TOPIC_FORMAT]
                 [--index-indent INDEX_INDENT] [--date-format DATE_FORMAT]
                 input
gresiblos: error: the following arguments are required: input
"""
    assert pname(captured.out) == ""


def test_main_help(capsys):
    """Test behaviour when help is wished"""
    try:
        gresiblos.main(["--help"])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==0
    captured = capsys.readouterr()
    assert pname(captured.out) == """usage: gresiblos [-h] [-c FILE] [--version] [-t TEMPLATE] [-e EXTENSION]
                 [-s STATE] [-d DESTINATION] [--index-output INDEX_OUTPUT]
                 [--chrono-output CHRONO_OUTPUT] [--alpha-output ALPHA_OUTPUT]
                 [--markdown] [--degrotesque] [--topic-format TOPIC_FORMAT]
                 [--index-indent INDEX_INDENT] [--date-format DATE_FORMAT]
                 input

greyrat's simple blog system

positional arguments:
  input

options:
  -h, --help            show this help message and exit
  -c FILE, --config FILE
                        Reads the named configuration file
  --version             show program's version number and exit
  -t TEMPLATE, --template TEMPLATE
                        Defines the template to use
  -e EXTENSION, --extension EXTENSION
                        Sets the extension of the built file(s)
  -s STATE, --state STATE
                        Use only files with the given state(s)
  -d DESTINATION, --destination DESTINATION
                        Sets the path to store the generated file(s) into
  --index-output INDEX_OUTPUT
                        Writes the index to the named file
  --chrono-output CHRONO_OUTPUT
                        Writes the named file with entries in chronological
                        order
  --alpha-output ALPHA_OUTPUT
                        Writes the named file with entries in alphabetical
                        order
  --markdown            If set, markdown is applied on the contents
  --degrotesque         If set, degrotesque is applied on the contents and the
                        title
  --topic-format TOPIC_FORMAT
                        Defines how each of the topics is rendered
  --index-indent INDEX_INDENT
                        Defines the indent used for the index file
  --date-format DATE_FORMAT
                        Defines the time format used

(c) Daniel Krajzewicz 2016-2025
"""
    assert pname(captured.err) == ""


def test_main_version(capsys):
    """Test behaviour when version information is wished"""
    try:
        gresiblos.main(["--version"])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==0
    captured = capsys.readouterr()
    assert pname(captured.out) == """gresiblos 0.8.0
"""
    assert pname(captured.err) == ""
