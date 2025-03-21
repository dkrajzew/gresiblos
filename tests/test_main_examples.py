#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
"""gresiblos - Tests for the main method - examples application."""
# =============================================================================
__author__     = "Daniel Krajzewicz"
__copyright__  = "Copyright 2024-2025, Daniel Krajzewicz"
__credits__    = ["Daniel Krajzewicz"]
__license__    = "BSD"
__version__    = "0.4.2"
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
sys.path.append(os.path.join(os.path.split(__file__)[0], "..", "src"))
from pathlib import Path
from util import pname, copy_from_data, fread, TEST_PATH
import gresiblos



# --- test functions ----------------------------------------------------------
def test_main_entry1_by_name(capsys, tmp_path):
    """Parsing first example (by name)"""
    copy_from_data(tmp_path, ["template.html", "entry1.txt"])
    ret = gresiblos.main(["--template", str(tmp_path / "template.html"), "--index-output", "entries.json", "-d", str(tmp_path), str(tmp_path / "entry1.txt")])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/entry1.txt'
Writing to <DIR>/my-first-blog-entry.html
"""
    assert pname(captured.err, tmp_path) == ""
    assert fread(tmp_path / "my-first-blog-entry.html") == fread(Path(TEST_PATH) / "my-first-blog-entry.html")
    assert fread(tmp_path / "entries.json") == fread(Path(TEST_PATH) / "entry1_sum.json")


def test_main_entry2_by_name(capsys, tmp_path):
    """Parsing secomd example (by name)"""
    copy_from_data(tmp_path, ["template.html", "entry2.txt"])
    ret = gresiblos.main(["--template", str(tmp_path / "template.html"), "--index-output", "entries.json", "-d", str(tmp_path), str(tmp_path / "entry2.txt")])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/entry2.txt'
Writing to <DIR>/my-second-blog-entry.html
"""
    assert pname(captured.err, tmp_path) == ""
    assert fread(tmp_path / "my-second-blog-entry.html") == fread(Path(TEST_PATH) / "my-second-blog-entry.html")
    assert fread(tmp_path / "entries.json") == fread(Path(TEST_PATH) / "entry2_sum.json")


def test_main_both_entries_by_name(capsys, tmp_path):
    """Parsing secomd example (by name)"""
    copy_from_data(tmp_path, ["template.html", "entry1.txt", "entry2.txt"])
    ret = gresiblos.main(["--template", str(tmp_path / "template.html"), "--index-output", "entries.json", "-d", str(tmp_path), str(tmp_path / "entry1.txt")+","+str(tmp_path / "entry2.txt")])
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


def test_main_both_entries_by_extension_glob(capsys, tmp_path):
    """Parsing secomd example (by name)"""
    copy_from_data(tmp_path, ["template.html", "entry1.txt", "entry2.txt"])
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


def test_main_state_release_by_extension_glob(capsys, tmp_path):
    """Parsing secomd example (by name)"""
    copy_from_data(tmp_path, ["template.html", "entry1.txt", "entry2.txt"])
    ret = gresiblos.main(["--state", "release", "--template", str(tmp_path / "template.html"), "--index-output", "entries.json", "-d", str(tmp_path), str(tmp_path / "entry*.txt")])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/entry1.txt'
Writing to <DIR>/my-first-blog-entry.html
Processing '<DIR>/entry2.txt'
 ... skipped for state='work'
"""
    assert pname(captured.err, tmp_path) == ""
    assert fread(tmp_path / "my-first-blog-entry.html") == fread(Path(TEST_PATH) / "my-first-blog-entry.html")
    assert fread(tmp_path / "entries.json") == fread(Path(TEST_PATH) / "entry1_sum.json")


def test_main_dateformat_by_name(capsys, tmp_path):
    """Parsing first example (by name)"""
    copy_from_data(tmp_path, ["template.html", "entry1_dateformat2.txt"])
    ret = gresiblos.main(["--date-format", "%d.%m.%Y %H:%M:%S", "--template", str(tmp_path / "template.html"), "--index-output", "entries.json", "-d", str(tmp_path), str(tmp_path / "entry1_dateformat2.txt")])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/entry1_dateformat2.txt'
Writing to <DIR>/my-first-blog-entry.html
"""
    assert pname(captured.err, tmp_path) == ""
    assert fread(tmp_path / "my-first-blog-entry.html") == fread(Path(TEST_PATH) / "my-first-blog-entry_dateformat.html")
    assert fread(tmp_path / "entries.json") == fread(Path(TEST_PATH) / "entry1_sum.json")


def test_main_entries_by_extension_glob_recursive(capsys, tmp_path):
    """Parsing secomd example (by name)"""
    copy_from_data(tmp_path, ["template.html", "entry1.txt"])
    os.makedirs(tmp_path / "sub")
    copy_from_data(tmp_path / "sub", ["entry2.txt"])
    ret = gresiblos.main(["--template", str(tmp_path / "template.html"), "--index-output", "entries.json", "-d", str(tmp_path), str(tmp_path / "./**/entry*.txt")])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/entry1.txt'
Writing to <DIR>/my-first-blog-entry.html
Processing '<DIR>/sub/entry2.txt'
Writing to <DIR>/my-second-blog-entry.html
"""
    assert pname(captured.err, tmp_path) == ""
    assert fread(tmp_path / "my-first-blog-entry.html") == fread(Path(TEST_PATH) / "my-first-blog-entry.html")
    assert fread(tmp_path / "my-second-blog-entry.html") == fread(Path(TEST_PATH) / "my-second-blog-entry.html")
    assert fread(tmp_path / "entries.json") == fread(Path(TEST_PATH) / "entries_sum.json")


