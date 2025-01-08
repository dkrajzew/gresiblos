#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
"""gresiblos - Tests for the main method - examples application."""
# =============================================================================
__author__     = "Daniel Krajzewicz"
__copyright__  = "Copyright 2024-2025, Daniel Krajzewicz"
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
import sys
import os
sys.path.append(os.path.join(os.path.split(__file__)[0], "..", "src"))
TEST_PATH = os.path.split(__file__)[0]
import shutil
from pathlib import Path
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
