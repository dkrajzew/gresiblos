#!/usr/bin/env python
"""gresiblos - Tests for templates prcoessing - basic replacement."""
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
def test_replace_plain_given(capsys, tmp_path):
    """Replace placeholder with given value"""
    template = gresiblos.Template("[[:foo:]]")
    entry = gresiblos.Entry({"foo": "bar"})
    assert template.embed(entry._fields, "[[:topic:]]")=="bar"


def test_replace_plain_missing(capsys, tmp_path):
    """Replace placeholder with missing value"""
    template = gresiblos.Template("[[:bar:]]")
    entry = gresiblos.Entry({"foo": "bar"})
    assert template.embed(entry._fields, "[[:topic:]]")==""


def test_replace_opt_given(capsys, tmp_path):
    """Replace placeholder with default with given value"""
    template = gresiblos.Template("[[:foo|foo:]]")
    entry = gresiblos.Entry({"foo": "bar"})
    assert template.embed(entry._fields, "[[:topic:]]")=="bar"


def test_replace_opt_missing(capsys, tmp_path):
    """Parsing placeholder with default with missing value"""
    template = gresiblos.Template("[[:bar|foo:]]")
    entry = gresiblos.Entry({"foo": "bar"})
    assert template.embed(entry._fields, "[[:topic:]]")=="foo"
