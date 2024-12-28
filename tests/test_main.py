#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
"""gresiblos - Tests for the main method."""
# =============================================================================
__author__     = "Daniel Krajzewicz"
__copyright__  = "Copyright 2020-2024, Daniel Krajzewicz"
__credits__    = ["Daniel Krajzewicz"]
__license__    = "GPLv3"
__version__    = "0.4.0"
__maintainer__ = "Daniel Krajzewicz"
__email__      = "daniel@krajzewicz.de"
__status__     = "Development"
# ===========================================================================
# - https://github.com/dkrajzew/gresiblos
# - http://www.krajzewicz.de/docs/gresiblos/index.html
# - http://www.krajzewicz.de
# ===========================================================================


# --- imports ---------------------------------------------------------------
import sys
import os
sys.path.append(os.path.join(os.path.split(__file__)[0], "..", "src"))
import gresiblos



# --- helper functions ------------------------------------------------------
def patch(string):
    return string.replace("__main__.py", "gresiblos").replace("pytest", "gresiblos").replace("optional arguments", "options")



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
    assert patch(captured.err) == """usage: gresiblos [-h] [-c FILE] [--version] [-t TEMPLATE] [-e EXTENSION]
                 [-s STATE] [-d DESTINATION] [--have-php-index]
                 [--default-author DEFAULT_AUTHOR]
                 [--default-copyright-date DEFAULT_COPYRIGHT_DATE]
                 [--default-state DEFAULT_STATE]
                 input
gresiblos: error: the following arguments are required: input
"""
    assert patch(captured.out) == ""


def test_main_empty2(capsys):
    """Test behaviour if no arguments are given"""
    try:
        ret = gresiblos.main()
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==2
    captured = capsys.readouterr()
    assert patch(captured.err) == """usage: gresiblos [-h] [-c FILE] [--version] [-t TEMPLATE] [-e EXTENSION]
                 [-s STATE] [-d DESTINATION] [--have-php-index]
                 [--default-author DEFAULT_AUTHOR]
                 [--default-copyright-date DEFAULT_COPYRIGHT_DATE]
                 [--default-state DEFAULT_STATE]
                 input
gresiblos: error: the following arguments are required: input
"""
    assert patch(captured.out) == ""


def test_main_help(capsys):
    """Test behaviour when help is wished"""
    try:
        gresiblos.main(["--help"])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==0
    captured = capsys.readouterr()
    assert patch(captured.out) == """usage: gresiblos [-h] [-c FILE] [--version] [-t TEMPLATE] [-e EXTENSION]
                 [-s STATE] [-d DESTINATION] [--have-php-index]
                 [--default-author DEFAULT_AUTHOR]
                 [--default-copyright-date DEFAULT_COPYRIGHT_DATE]
                 [--default-state DEFAULT_STATE]
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
  --have-php-index      References topics to index.php if set
  --default-author DEFAULT_AUTHOR
                        Sets the default author
  --default-copyright-date DEFAULT_COPYRIGHT_DATE
                        Sets the default copyright date
  --default-state DEFAULT_STATE
                        Sets the default state

(c) Daniel Krajzewicz 2014-2024
"""
    assert captured.err == ""


def test_main_version(capsys):
    """Test behaviour when version information is wished"""
    try:
        gresiblos.main(["--version"])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==0
    captured = capsys.readouterr()
    assert patch(captured.out) == """gresiblos 0.4.0
"""
    assert patch(captured.err) == ""
