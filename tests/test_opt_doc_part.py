#!/usr/bin/env python
"""gresiblos - Tests for the main method - examples application."""
# =============================================================================
__author__     = "Daniel Krajzewicz"
__copyright__  = "Copyright 2024-2026, Daniel Krajzewicz"
__credits__    = ["Daniel Krajzewicz"]
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
import sys
import os
sys.path.append(os.path.join(os.path.split(__file__)[0], "..", "gresiblos"))
import gresiblos



# --- test functions ----------------------------------------------------------
def test_opt_text(capsys):
    """Replace optional with given value"""
    entry = gresiblos.Entry({"foo": "bar"})
    template = gresiblos.Template("[[:?foo:]]here[[:foo?:]]")
    assert template.embed(entry._fields, "[[:topic:]]")=="here"


def test_opt_field(capsys):
    """Replace optional with placeholder with given value"""
    entry = gresiblos.Entry({"foo": "bar"})
    template = gresiblos.Template("[[:?foo:]][[:foo:]][[:foo?:]]")
    assert template.embed(entry._fields, "[[:topic:]]")=="bar"


def test_err_not_start_closed1(capsys):
    """Error: not properly closed optional opening"""
    entry = gresiblos.Entry({"foo": "bar"})
    template = gresiblos.Template("[[:?foo[[:foo:]][[:foo?:]]")
    try:
        assert template.embed(entry._fields, "[[:topic:]]")=="bar"
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==3
    captured = capsys.readouterr()
    assert captured.err == """gresiblos: error: Missing closing tag of an optional document part that starts at 0; field_key='foo[[:foo'
"""
    assert captured.out == ""


def test_err_not_start_closed2(capsys):
    """Error: not properly closed optional opening"""
    entry = gresiblos.Entry({"foo": "bar"})
    template = gresiblos.Template("[[:?foo")
    try:
        assert template.embed(entry._fields, "[[:topic:]]")=="bar"
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==3
    captured = capsys.readouterr()
    assert captured.err == """gresiblos: error: Missing ':]]' at the begin tag of an optional document part that starts at 0
"""
    assert captured.out == ""


