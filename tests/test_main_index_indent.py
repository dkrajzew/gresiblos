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
from pathlib import Path
from util import pname, copy_files_and_template, fread, TEST_PATH
import gresiblos



# --- test functions ----------------------------------------------------------
def test_main_indent_default(capsys, tmp_path):
    """Parsing secomd example (by name)"""
    copy_files_and_template(tmp_path, ["entry1.txt", "entry2.txt"])
    ret = gresiblos.main(["--template", str(tmp_path / "template.html"), "--index-output", "entries.json", "-d", str(tmp_path), str(tmp_path / "entry*.txt")])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/entry1.txt'
Writing to <DIR>/my-first-blog-entry.html
Processing '<DIR>/entry2.txt'
Writing to <DIR>/my-second-blog-entry.html
"""
    assert pname(captured.err, tmp_path) == ""
    assert fread(tmp_path / "my-first-blog-entry.html") == fread(Path(TEST_PATH) / "my-first-blog-entry.html")
    assert fread(tmp_path / "my-second-blog-entry.html") == fread(Path(TEST_PATH) / "my-second-blog-entry.html")
    assert fread(tmp_path / "entries.json") == fread(Path(TEST_PATH) / "entries_sum.json")


def test_main_indent_0(capsys, tmp_path):
    """Parsing secomd example (by name)"""
    copy_files_and_template(tmp_path, ["entry1.txt", "entry2.txt"])
    ret = gresiblos.main(["--index-indent", "0", "--template", str(tmp_path / "template.html"), "--index-output", "entries.json", "-d", str(tmp_path), str(tmp_path / "entry*.txt")])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/entry1.txt'
Writing to <DIR>/my-first-blog-entry.html
Processing '<DIR>/entry2.txt'
Writing to <DIR>/my-second-blog-entry.html
"""
    assert pname(captured.err, tmp_path) == ""
    assert fread(tmp_path / "my-first-blog-entry.html") == fread(Path(TEST_PATH) / "my-first-blog-entry.html")
    assert fread(tmp_path / "my-second-blog-entry.html") == fread(Path(TEST_PATH) / "my-second-blog-entry.html")
    assert fread(tmp_path / "entries.json") == fread(Path(TEST_PATH) / "entries_sum_ident0.json")


def test_main_indent_2(capsys, tmp_path):
    """Parsing secomd example (by name)"""
    copy_files_and_template(tmp_path, ["entry1.txt", "entry2.txt"])
    ret = gresiblos.main(["--index-indent", "2", "--template", str(tmp_path / "template.html"), "--index-output", "entries.json", "-d", str(tmp_path), str(tmp_path / "entry*.txt")])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/entry1.txt'
Writing to <DIR>/my-first-blog-entry.html
Processing '<DIR>/entry2.txt'
Writing to <DIR>/my-second-blog-entry.html
"""
    assert pname(captured.err, tmp_path) == ""
    assert fread(tmp_path / "my-first-blog-entry.html") == fread(Path(TEST_PATH) / "my-first-blog-entry.html")
    assert fread(tmp_path / "my-second-blog-entry.html") == fread(Path(TEST_PATH) / "my-second-blog-entry.html")
    assert fread(tmp_path / "entries.json") == fread(Path(TEST_PATH) / "entries_sum_ident2.json")

