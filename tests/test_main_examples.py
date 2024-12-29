#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
"""gresiblos - Tests for the main method - examples application."""
# =============================================================================
__author__     = "Daniel Krajzewicz"
__copyright__  = "Copyright 2020-2024, Daniel Krajzewicz"
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



# --- helper functions ------------------------------------------------------
def patch(string, path):
    string = string.replace(str(path), "<DIR>").replace("\\", "/")
    return string.replace("__main__.py", "gresiblos").replace("pytest", "gresiblos").replace("optional arguments", "options")

def copy_from_data(tmp_path, files):
    for file in files:
        shutil.copy(os.path.join((TEST_PATH), "..", "data", file), str(tmp_path / file))


# --- test functions ----------------------------------------------------------
def test_main_entry1_by_name(capsys, tmp_path):
    """Parsing first example (by name)"""
    copy_from_data(tmp_path, ["template.html", "entry1.txt"])
    ret = gresiblos.main(["--template", str(tmp_path / "template.html"), "-d", str(tmp_path), str(tmp_path / "entry1.txt")])
    captured = capsys.readouterr()
    assert patch(captured.out, tmp_path) == """Processing '<DIR>/entry1.txt'
Writing to <DIR>/my-first-blog-entry.html
"""
    assert patch(captured.err, tmp_path) == ""
    p1g = tmp_path / "my-first-blog-entry.html"
    p1o = Path(TEST_PATH) / "my-first-blog-entry.html"
    assert p1g.read_text() == p1o.read_text()
    psg = tmp_path / "entries.json"
    pso = Path(TEST_PATH) / "entry1_sum.json"
    assert psg.read_text() == pso.read_text()


def test_main_entry2_by_name(capsys, tmp_path):
    """Parsing secomd example (by name)"""
    copy_from_data(tmp_path, ["template.html", "entry2.txt"])
    ret = gresiblos.main(["--template", str(tmp_path / "template.html"), "-d", str(tmp_path), str(tmp_path / "entry2.txt")])
    captured = capsys.readouterr()
    assert patch(captured.out, tmp_path) == """Processing '<DIR>/entry2.txt'
Writing to <DIR>/my-second-blog-entry.html
"""
    assert patch(captured.err, tmp_path) == ""
    p2g = tmp_path / "my-second-blog-entry.html"
    p2o = Path(TEST_PATH) / "my-second-blog-entry.html"
    assert p2g.read_text() == p2o.read_text()
    psg = tmp_path / "entries.json"
    pso = Path(TEST_PATH) / "entry2_sum.json"
    assert psg.read_text() == pso.read_text()


def test_main_both_entries_by_name(capsys, tmp_path):
    """Parsing secomd example (by name)"""
    copy_from_data(tmp_path, ["template.html", "entry1.txt", "entry2.txt"])
    ret = gresiblos.main(["--template", str(tmp_path / "template.html"), "-d", str(tmp_path), str(tmp_path / "entry1.txt")+","+str(tmp_path / "entry2.txt")])
    captured = capsys.readouterr()
    assert patch(captured.out, tmp_path) == """Processing '<DIR>/entry1.txt'
Writing to <DIR>/my-first-blog-entry.html
Processing '<DIR>/entry2.txt'
Writing to <DIR>/my-second-blog-entry.html
"""
    assert patch(captured.err, tmp_path) == ""
    p1g = tmp_path / "my-first-blog-entry.html"
    p1o = Path(TEST_PATH) / "my-first-blog-entry.html"
    assert p1g.read_text() == p1o.read_text()
    p2g = tmp_path / "my-second-blog-entry.html"
    p2o = Path(TEST_PATH) / "my-second-blog-entry.html"
    assert p2g.read_text() == p2o.read_text()
    psg = tmp_path / "entries.json"
    pso = Path(TEST_PATH) / "entries_sum.json"
    assert psg.read_text() == pso.read_text()


def test_main_both_entries_by_extension_glob(capsys, tmp_path):
    """Parsing secomd example (by name)"""
    copy_from_data(tmp_path, ["template.html", "entry1.txt", "entry2.txt"])
    ret = gresiblos.main(["--template", str(tmp_path / "template.html"), "-d", str(tmp_path), str(tmp_path / "entry*.txt")])
    captured = capsys.readouterr()
    assert patch(captured.out, tmp_path) == """Processing '<DIR>/entry1.txt'
Writing to <DIR>/my-first-blog-entry.html
Processing '<DIR>/entry2.txt'
Writing to <DIR>/my-second-blog-entry.html
"""
    assert patch(captured.err, tmp_path) == ""
    p1g = tmp_path / "my-first-blog-entry.html"
    p1o = Path(TEST_PATH) / "my-first-blog-entry.html"
    assert p1g.read_text() == p1o.read_text()
    p2g = tmp_path / "my-second-blog-entry.html"
    p2o = Path(TEST_PATH) / "my-second-blog-entry.html"
    assert p2g.read_text() == p2o.read_text()
    psg = tmp_path / "entries.json"
    pso = Path(TEST_PATH) / "entries_sum.json"
    assert psg.read_text() == pso.read_text()


def test_main_state_release_by_extension_glob(capsys, tmp_path):
    """Parsing secomd example (by name)"""
    copy_from_data(tmp_path, ["template.html", "entry1.txt", "entry2.txt"])
    ret = gresiblos.main(["--state", "release", "--template", str(tmp_path / "template.html"), "-d", str(tmp_path), str(tmp_path / "entry*.txt")])
    captured = capsys.readouterr()
    assert patch(captured.out, tmp_path) == """Processing '<DIR>/entry1.txt'
Writing to <DIR>/my-first-blog-entry.html
Processing '<DIR>/entry2.txt'
 ... skipped for state=work
"""
    assert patch(captured.err, tmp_path) == ""
    p1g = tmp_path / "my-first-blog-entry.html"
    p1o = Path(TEST_PATH) / "my-first-blog-entry.html"
    assert p1g.read_text() == p1o.read_text()
    psg = tmp_path / "entries.json"
    pso = Path(TEST_PATH) / "entry1_sum.json"
    assert psg.read_text() == pso.read_text()

