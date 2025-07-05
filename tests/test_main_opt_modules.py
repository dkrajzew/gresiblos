#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
"""gresiblos - Tests for the main method - examples application."""
# =============================================================================
__author__     = "Daniel Krajzewicz"
__copyright__  = "Copyright 2025, Daniel Krajzewicz"
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
from unittest.mock import patch
from importlib import reload
from pathlib import Path
from util import pname, copy_files_and_template, fread, pdate, TEST_PATH
import gresiblos



# --- test functions ----------------------------------------------------------
def test_main_entry3_plain(capsys, tmp_path):
    """Parsing first example (by name)"""
    copy_files_and_template(tmp_path, ["entry3_optional.txt"])
    ret = gresiblos.main(["--template", str(tmp_path / "template.html"), "--index-output", "entries.json", "-d", str(tmp_path), str(tmp_path / "entry3_optional.txt")])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/entry3_optional.txt'
Writing to <DIR>/entry3_optional.html
"""
    assert pname(captured.err, tmp_path) == ""
    assert fread(tmp_path / "entry3_optional.html", True) == fread(Path(TEST_PATH) / "entry3_optional_plain.html")
    assert fread(tmp_path / "entries.json", True) == fread(Path(TEST_PATH) / "entry3_sum.json")


def test_main_entry3_degrotesque_missing(capsys, tmp_path):
    """Parsing first example (by name)"""
    # https://stackoverflow.com/questions/51044068/test-for-import-of-optional-dependencies-in-init-py-with-pytest-python-3-5
    with patch.dict(sys.modules, {'degrotesque': None}):
        reload(sys.modules['gresiblos'])
        copy_files_and_template(tmp_path, ["entry3_optional.txt"])
        try:
            ret = gresiblos.main(["--template", str(tmp_path / "template.html"), "--degrotesque", "--index-output", "entries.json", "-d", str(tmp_path), str(tmp_path / "entry3_optional.txt")])
            assert False # pragma: no cover
        except SystemExit as e:
            assert type(e)==type(SystemExit())
            assert e.code==2
    reload(sys.modules['gresiblos'])
    captured = capsys.readouterr()
    assert pname(captured.err, tmp_path) == """gresiblos: error: degrotesque application is set, but degrotesque is not installed
"""
    assert pname(captured.out, tmp_path) == ""


def test_main_entry3_degrotesque(capsys, tmp_path):
    """Parsing first example (by name)"""
    copy_files_and_template(tmp_path, ["entry3_optional.txt"])
    ret = gresiblos.main(["--template", str(tmp_path / "template.html"), "--degrotesque", "--index-output", "entries.json", "-d", str(tmp_path), str(tmp_path / "entry3_optional.txt")])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/entry3_optional.txt'
Writing to <DIR>/entry3_optional.html
"""
    assert pname(captured.err, tmp_path) == ""
    assert fread(tmp_path / "entry3_optional.html", True) == fread(Path(TEST_PATH) / "entry3_optional_degrotesque.html")
    assert fread(tmp_path / "entries.json", True) == fread(Path(TEST_PATH) / "entry3_sum.json")


def test_main_entry3_markdown_missing(capsys, tmp_path):
    """Parsing first example (by name)"""
    # https://stackoverflow.com/questions/51044068/test-for-import-of-optional-dependencies-in-init-py-with-pytest-python-3-5
    with patch.dict(sys.modules, {'markdown': None}):
        reload(sys.modules['gresiblos'])
        copy_files_and_template(tmp_path, ["entry3_optional.txt"])
        try:
            ret = gresiblos.main(["--template", str(tmp_path / "template.html"), "--markdown", "--index-output", "entries.json", "-d", str(tmp_path), str(tmp_path / "entry3_optional.txt")])
            assert False # pragma: no cover
        except SystemExit as e:
            assert type(e)==type(SystemExit())
            assert e.code==2
    reload(sys.modules['gresiblos'])
    captured = capsys.readouterr()
    assert pname(captured.err, tmp_path) == """gresiblos: error: markdown application is set, but markdown is not installed
"""
    assert pname(captured.out, tmp_path) == ""


def test_main_entry3_markdown(capsys, tmp_path):
    """Parsing first example (by name)"""
    copy_files_and_template(tmp_path, ["entry3_optional.txt"])
    ret = gresiblos.main(["--template", str(tmp_path / "template.html"), "--markdown", "--index-output", "entries.json", "-d", str(tmp_path), str(tmp_path / "entry3_optional.txt")])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/entry3_optional.txt'
Writing to <DIR>/entry3_optional.html
"""
    assert pname(captured.err, tmp_path) == ""
    assert fread(tmp_path / "entry3_optional.html", True) == fread(Path(TEST_PATH) / "entry3_optional_markdown.html")
    assert fread(tmp_path / "entries.json", True) == fread(Path(TEST_PATH) / "entry3_sum.json")
    
    
def test_main_entry3_missing2(capsys, tmp_path):
    """Parsing first example (by name)"""
    # https://stackoverflow.com/questions/51044068/test-for-import-of-optional-dependencies-in-init-py-with-pytest-python-3-5
    with patch.dict(sys.modules, {'degrotesque': None, 'markdown': None}):
        reload(sys.modules['gresiblos'])
        copy_files_and_template(tmp_path, ["entry3_optional.txt"])
        try:
            ret = gresiblos.main(["--template", str(tmp_path / "template.html"), "--markdown", "--degrotesque", "--index-output", "entries.json", "-d", str(tmp_path), str(tmp_path / "entry3_optional.txt")])
            assert False # pragma: no cover
        except SystemExit as e:
            assert type(e)==type(SystemExit())
            assert e.code==2
    reload(sys.modules['gresiblos'])
    captured = capsys.readouterr()
    assert pname(captured.err, tmp_path) == """gresiblos: error: degrotesque application is set, but degrotesque is not installed
gresiblos: error: markdown application is set, but markdown is not installed
"""
    assert pname(captured.out, tmp_path) == ""


def test_main_entry3_both(capsys, tmp_path):
    """Parsing first example (by name)"""
    copy_files_and_template(tmp_path, ["entry3_optional.txt"])
    ret = gresiblos.main(["--template", str(tmp_path / "template.html"), "--degrotesque", "--markdown", "--index-output", "entries.json", "-d", str(tmp_path), str(tmp_path / "entry3_optional.txt")])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/entry3_optional.txt'
Writing to <DIR>/entry3_optional.html
"""
    assert pname(captured.err, tmp_path) == ""
    assert fread(tmp_path / "entry3_optional.html", True) == fread(Path(TEST_PATH) / "entry3_optional_both.html")
    assert fread(tmp_path / "entries.json", True) == fread(Path(TEST_PATH) / "entry3_sum.json")
