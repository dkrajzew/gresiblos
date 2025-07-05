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
def test_main_no_list(capsys, tmp_path):
    """Parsing secomd example (by name)"""
    copy_files_and_template(tmp_path, ["entry1.txt", "entry2.txt"])
    ret = gresiblos.main(["--template", str(tmp_path / "template.html"), "-d", str(tmp_path), str(tmp_path / "entry*.txt")])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/entry1.txt'
Writing to <DIR>/my-first-blog-entry.html
Processing '<DIR>/entry2.txt'
Writing to <DIR>/my-second-blog-entry.html
"""
    assert pname(captured.err, tmp_path) == ""
    assert fread(tmp_path / "my-first-blog-entry.html") == fread(Path(TEST_PATH) / "my-first-blog-entry.html")
    assert fread(tmp_path / "my-second-blog-entry.html") == fread(Path(TEST_PATH) / "my-second-blog-entry.html")


def test_main_list_alpha(capsys, tmp_path):
    """Parsing secomd example (by name)"""
    copy_files_and_template(tmp_path, ["entry1.txt", "entry2.txt"])
    ret = gresiblos.main(["--template", str(tmp_path / "template.html"), "--alpha-output", "alpha.html", "-d", str(tmp_path), str(tmp_path / "entry*.txt")])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/entry1.txt'
Writing to <DIR>/my-first-blog-entry.html
Processing '<DIR>/entry2.txt'
Writing to <DIR>/my-second-blog-entry.html
Writing alphabetical list to '<DIR>/alpha.html'
"""
    assert pname(captured.err, tmp_path) == ""
    assert fread(tmp_path / "my-first-blog-entry.html") == fread(Path(TEST_PATH) / "my-first-blog-entry.html")
    assert fread(tmp_path / "my-second-blog-entry.html") == fread(Path(TEST_PATH) / "my-second-blog-entry.html")
    assert fread(tmp_path / "alpha.html") == fread(Path(TEST_PATH) / "alpha_both.html")


def test_main_list_chrono(capsys, tmp_path):
    """Parsing secomd example (by name)"""
    copy_files_and_template(tmp_path, ["entry1.txt", "entry2.txt"])
    ret = gresiblos.main(["--template", str(tmp_path / "template.html"), "--chrono-output", "chrono.html", "-d", str(tmp_path), str(tmp_path / "entry*.txt")])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/entry1.txt'
Writing to <DIR>/my-first-blog-entry.html
Processing '<DIR>/entry2.txt'
Writing to <DIR>/my-second-blog-entry.html
Writing chronological list to '<DIR>/chrono.html'
"""
    assert pname(captured.err, tmp_path) == ""
    assert fread(tmp_path / "my-first-blog-entry.html") == fread(Path(TEST_PATH) / "my-first-blog-entry.html")
    assert fread(tmp_path / "my-second-blog-entry.html") == fread(Path(TEST_PATH) / "my-second-blog-entry.html")
    assert fread(tmp_path / "chrono.html") == fread(Path(TEST_PATH) / "chrono_both.html")


def test_main_list_both(capsys, tmp_path):
    """Parsing secomd example (by name)"""
    copy_files_and_template(tmp_path, ["entry1.txt", "entry2.txt"])
    ret = gresiblos.main(["--template", str(tmp_path / "template.html"), "--alpha-output", "alpha.html", "--chrono-output", "chrono.html", "-d", str(tmp_path), str(tmp_path / "entry*.txt")])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/entry1.txt'
Writing to <DIR>/my-first-blog-entry.html
Processing '<DIR>/entry2.txt'
Writing to <DIR>/my-second-blog-entry.html
Writing chronological list to '<DIR>/chrono.html'
Writing alphabetical list to '<DIR>/alpha.html'
"""
    assert pname(captured.err, tmp_path) == ""
    assert fread(tmp_path / "my-first-blog-entry.html") == fread(Path(TEST_PATH) / "my-first-blog-entry.html")
    assert fread(tmp_path / "my-second-blog-entry.html") == fread(Path(TEST_PATH) / "my-second-blog-entry.html")
    assert fread(tmp_path / "alpha.html") == fread(Path(TEST_PATH) / "alpha_both.html")
    assert fread(tmp_path / "chrono.html") == fread(Path(TEST_PATH) / "chrono_both.html")

