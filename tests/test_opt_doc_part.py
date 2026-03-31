#!/usr/bin/env python
"""gresiblos - Tests for templates prcoessing - optional fields."""
# ===========================================================================
# - https://github.com/dkrajzew/gresiblos
# - http://gresiblos.readthedocs.org/
# - http://www.krajzewicz.de/docs/gresiblos/index.html
# - http://www.krajzewicz.de
# - contact me: daniel@krajzewicz.de
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


def test_opt_text_missing(capsys):
    """Replace optional with missing value"""
    entry = gresiblos.Entry({})
    template = gresiblos.Template("[[:?foo:]]here[[:foo?:]]")
    assert template.embed(entry._fields, "[[:topic:]]")==""


def test_opt_field(capsys):
    """Replace optional with placeholder with given value"""
    entry = gresiblos.Entry({"foo": "bar"})
    template = gresiblos.Template("[[:?foo:]][[:foo:]][[:foo?:]]")
    assert template.embed(entry._fields, "[[:topic:]]")=="bar"


def test_opt_field_missing(capsys):
    """Replace optional with placeholder with missing value"""
    entry = gresiblos.Entry({})
    template = gresiblos.Template("[[:?foo:]][[:foo:]][[:foo?:]]")
    assert template.embed(entry._fields, "[[:topic:]]")==""


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


def test_err_missing_end(capsys):
    """Error: not properly closed optional opening"""
    entry = gresiblos.Entry({"foo": "bar"})
    template = gresiblos.Template("[[:?foo:]][[:foo:]]")
    try:
        assert template.embed(entry._fields, "[[:topic:]]")=="bar"
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==3
    captured = capsys.readouterr()
    assert captured.err == """gresiblos: error: Missing closing tag of an optional document part that starts at 0; field_key='foo'
"""
    assert captured.out == ""


