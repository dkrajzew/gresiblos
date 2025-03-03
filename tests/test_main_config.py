#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
"""gresiblos - Tests for the main method - configuration."""
# =============================================================================
__author__     = "Daniel Krajzewicz"
__copyright__  = "Copyright 2024-2025, Daniel Krajzewicz"
__credits__    = ["Daniel Krajzewicz"]
__license__    = "GPLv3"
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
import shutil
from pathlib import Path
from util import pname, copy_from_data, TEST_PATH
import gresiblos



# --- test functions ----------------------------------------------------------
def test_main_missing_config(capsys, tmp_path):
    """Parsing first example (by name)"""
    copy_from_data(tmp_path, ["template.html", "entry1.txt"])
    try:
        ret = gresiblos.main(["--config", str(tmp_path / "cfg1.cfg"), "--template", str(tmp_path / "template.html"), "--index-output", "entries.json", "-d", str(tmp_path), str(tmp_path / "entry1.txt")])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==2
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == ""
    assert pname(captured.err, tmp_path) == """gresiblos: error: configuration file '<DIR>/cfg1.cfg' does not exist
"""


def test_main_entry1_by_name(capsys, tmp_path):
    """Parsing first example (by name)"""
    shutil.copy(os.path.join((TEST_PATH), "cfg1.cfg"), str(tmp_path / "cfg1.cfg"))
    copy_from_data(tmp_path, ["template.html", "entry1.txt"])
    ret = gresiblos.main(["--config", str(tmp_path / "cfg1.cfg"), "--template", str(tmp_path / "template.html"), "--index-output", "entries.json", "-d", str(tmp_path), str(tmp_path / "entry1.txt")])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/entry1.txt'
Writing to <DIR>/my-first-blog-entry.php
"""
    assert pname(captured.err, tmp_path) == ""
    p1g = tmp_path / "my-first-blog-entry.php"
    p1o = Path(TEST_PATH) / "my-first-blog-entry.html"
    assert p1g.read_text() == p1o.read_text()
    psg = tmp_path / "entries.json"
    pso = Path(TEST_PATH) / "entry1_sum_php.json"
    assert psg.read_text() == pso.read_text()


def test_main_two_entries_by_name(capsys, tmp_path):
    """Parsing first example (by name)"""
    shutil.copy(os.path.join((TEST_PATH), "cfg1.cfg"), str(tmp_path / "cfg1.cfg"))
    copy_from_data(tmp_path, ["template.html", "entry1.txt", "entry2.txt"])
    ret = gresiblos.main(["--config", str(tmp_path / "cfg1.cfg"), "--template", str(tmp_path / "template.html"), "--index-output", "entries.json", "-d", str(tmp_path), str(tmp_path / "entry*.txt")])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/entry1.txt'
Writing to <DIR>/my-first-blog-entry.php
Processing '<DIR>/entry2.txt'
Writing to <DIR>/my-second-blog-entry.php
"""
    assert pname(captured.err, tmp_path) == ""
    p1g = tmp_path / "my-first-blog-entry.php"
    p1o = Path(TEST_PATH) / "my-first-blog-entry.html"
    assert p1g.read_text() == p1o.read_text()
    p2g = tmp_path / "my-second-blog-entry.php"
    p2o = Path(TEST_PATH) / "my-second-blog-entry.html"
    assert p2g.read_text() == p2o.read_text()
    psg = tmp_path / "entries.json"
    pso = Path(TEST_PATH) / "entries_sum_php.json"
    assert psg.read_text() == pso.read_text()


def test_main_two_entries_by_name_filter_state(capsys, tmp_path):
    """Parsing first example (by name)"""
    shutil.copy(os.path.join((TEST_PATH), "cfg2.cfg"), str(tmp_path / "cfg2.cfg"))
    copy_from_data(tmp_path, ["template.html", "entry1.txt", "entry2.txt"])
    ret = gresiblos.main(["--config", str(tmp_path / "cfg2.cfg"), "--template", str(tmp_path / "template.html"), "--index-output", "entries.json", "-d", str(tmp_path), str(tmp_path / "entry*.txt")])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/entry1.txt'
Writing to <DIR>/my-first-blog-entry.php
Processing '<DIR>/entry2.txt'
 ... skipped for state=work
"""
    assert pname(captured.err, tmp_path) == ""
    p1g = tmp_path / "my-first-blog-entry.php"
    p1o = Path(TEST_PATH) / "my-first-blog-entry.html"
    assert p1g.read_text() == p1o.read_text()
    psg = tmp_path / "entries.json"
    pso = Path(TEST_PATH) / "entry1_sum_php.json"
    assert psg.read_text() == pso.read_text()
