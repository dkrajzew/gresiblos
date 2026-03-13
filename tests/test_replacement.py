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
def test_replace_plain_given(capsys, tmp_path):
    """Parsing first example (by name)"""
    entry = gresiblos.Entry({"foo": "bar"})
    assert entry.embed("[[:foo:]]", "")=="bar"


def test_replace_plain_missing(capsys, tmp_path):
    """Parsing first example (by name)"""
    entry = gresiblos.Entry({"foo": "bar"})
    assert entry.embed("[[:bar:]]", "")==""


def test_replace_opt_given(capsys, tmp_path):
    """Parsing first example (by name)"""
    entry = gresiblos.Entry({"foo": "bar"})
    assert entry.embed("[[:foo|foo:]]", "")=="bar"


def test_replace_opt_missing(capsys, tmp_path):
    """Parsing first example (by name)"""
    entry = gresiblos.Entry({"foo": "bar"})
    assert entry.embed("[[:bar|foo:]]", "")=="foo"
