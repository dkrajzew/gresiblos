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
from pathlib import Path
from util import pname, copy_files, copy_files_and_template, fread, TEST_PATH
import gresiblos

import shutil

# --- test functions ----------------------------------------------------------
def test_main_entry1_by_name(capsys, tmp_path):
    """Parsing first example twice"""
    copy_files_and_template(tmp_path, ["entry1.txt"])
    try:
        ret = gresiblos.main(["-d", str(tmp_path), str(tmp_path / "entry1.txt")+","+str(tmp_path / "entry1.txt")])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==1
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/entry1.txt'
Writing to <DIR>/my-first-blog-entry.html
Processing '<DIR>/entry1.txt'
"""
    assert pname(captured.err, tmp_path) == """gresiblos: error: A page with name 'my-first-blog-entry' was already added
"""
