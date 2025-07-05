#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
"""gresiblos - Tests for the main method - examples application."""
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
import gresiblos



# --- test functions ----------------------------------------------------------
def test_opt_text(capsys):
    """Parsing first example (by name)"""
    entry = gresiblos.Entry({"foo": "bar"})
    assert entry.embed("[[:?foo:]]here[[:foo?:]]", "")=="here"


def test_opt_field(capsys):
    """Parsing first example (by name)"""
    entry = gresiblos.Entry({"foo": "bar"})
    assert entry.embed("[[:?foo:]][[:foo:]][[:foo?:]]", "")=="bar"


def test_err_not_start_closed1(capsys):
    """Parsing first example (by name)"""
    entry = gresiblos.Entry({"foo": "bar"})
    try:
        assert entry.embed("[[:?foo[[:foo:]][[:foo?:]]", "")=="bar"
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==3
    captured = capsys.readouterr()
    assert captured.err == """gresiblos: error: Missing closing tag of an optional document part that starts at 0; field_key='foo[[:foo'
"""
    assert captured.out == ""


def test_err_not_start_closed2(capsys):
    """Parsing first example (by name)"""
    entry = gresiblos.Entry({"foo": "bar"})
    try:
        assert entry.embed("[[:?foo", "")=="bar"
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==3
    captured = capsys.readouterr()
    assert captured.err == """gresiblos: error: Missing ':]]' at the begin tag of an optional document part that starts at 0
"""
    assert captured.out == ""


