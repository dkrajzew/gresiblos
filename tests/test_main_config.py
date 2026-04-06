#!/usr/bin/env python
"""gresiblos - Tests for the main method - configuration."""
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
import shutil
from pathlib import Path
from util import pname, copy_files_and_template, fread, fpread, TEST_PATH
import gresiblos



# --- test functions ----------------------------------------------------------
def test_main_missing_config(capsys, tmp_path):
    """Using a non-existing configuration file"""
    copy_files_and_template(tmp_path, ["entry1.txt"])
    try:
        ret = gresiblos.main(["--config", str(tmp_path / "cfg1.cfg")])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==2
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == ""
    assert pname(captured.err, tmp_path) == """gresiblos: error: configuration file '<DIR>/cfg1.cfg' does not exist
"""


def test_main_entry1_by_name(capsys, tmp_path):
    """Using a given configuration file with first example"""
    shutil.copy(os.path.join((TEST_PATH), "cfg1.cfg"), str(tmp_path / "cfg1.cfg"))
    copy_files_and_template(tmp_path, ["entry1.txt"])
    ret = gresiblos.main(["--config", str(tmp_path / "cfg1.cfg"), "--template", str(tmp_path / "template.html"), "--index-output", "entries.json", "-d", str(tmp_path), str(tmp_path / "entry1.txt")])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/entry1.txt'
Writing to <DIR>/my-first-blog-entry.php
"""
    assert pname(captured.err, tmp_path) == ""
    assert fpread(tmp_path / "my-first-blog-entry.php") == fpread(Path(TEST_PATH) / "my-first-blog-entry.html")
    assert fread(tmp_path / "entries.json") == fread(Path(TEST_PATH) / "entry1_sum_php.json")


def test_main_two_entries_by_name(capsys, tmp_path):
    """Using a given configuration file with both examples"""
    shutil.copy(os.path.join((TEST_PATH), "cfg1.cfg"), str(tmp_path / "cfg1.cfg"))
    copy_files_and_template(tmp_path, ["entry1.txt", "entry2.txt"])
    ret = gresiblos.main(["--config", str(tmp_path / "cfg1.cfg"), "--template", str(tmp_path / "template.html"), "--index-output", "entries.json", "-d", str(tmp_path), str(tmp_path / "entry*.txt")])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/entry1.txt'
Writing to <DIR>/my-first-blog-entry.php
Processing '<DIR>/entry2.txt'
Writing to <DIR>/my-second-blog-entry.php
"""
    assert pname(captured.err, tmp_path) == ""
    assert fpread(tmp_path / "my-first-blog-entry.php") == fpread(Path(TEST_PATH) / "my-first-blog-entry.html")
    assert fpread(tmp_path / "my-second-blog-entry.php") == fpread(Path(TEST_PATH) / "my-second-blog-entry.html")
    assert fread(tmp_path / "entries.json") == fread(Path(TEST_PATH) / "entries_sum_php.json")


def test_main_two_entries_by_name_filter_state(capsys, tmp_path):
    """Using a given configuration file with both examples and state filter"""
    shutil.copy(os.path.join((TEST_PATH), "cfg2.cfg"), str(tmp_path / "cfg2.cfg"))
    copy_files_and_template(tmp_path, ["entry1.txt", "entry2.txt"])
    ret = gresiblos.main(["--config", str(tmp_path / "cfg2.cfg"), "--template", str(tmp_path / "template.html"), "--index-output", "entries.json", "-d", str(tmp_path), str(tmp_path / "entry*.txt")])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/entry1.txt'
Writing to <DIR>/my-first-blog-entry.php
Processing '<DIR>/entry2.txt'
 ... skipped for state='work'
"""
    assert pname(captured.err, tmp_path) == ""
    assert fpread(tmp_path / "my-first-blog-entry.php") == fpread(Path(TEST_PATH) / "my-first-blog-entry.html")
    assert fread(tmp_path / "entries.json") == fread(Path(TEST_PATH) / "entry1_sum_php.json")

