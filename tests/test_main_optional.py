#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
"""gresiblos - Tests for the main method - examples application."""
# =============================================================================
__author__     = "Daniel Krajzewicz"
__copyright__  = "Copyright 2025, Daniel Krajzewicz"
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
TEST_PATH = os.path.split(__file__)[0]
import shutil
import re
from unittest.mock import patch
from importlib import reload
from pathlib import Path
import gresiblos



# --- helper functions ------------------------------------------------------
def patch_output(string, path):
    string = string.replace(str(path), "<DIR>").replace("\\", "/")
    return string.replace("__main__.py", "gresiblos").replace("pytest", "gresiblos").replace("optional arguments", "options")

def copy_from_data(tmp_path, files):
    for file in files:
        shutil.copy(os.path.join((TEST_PATH), "..", "data", file), str(tmp_path / file))

def patch_date(string):
    # https://www.google.com/search?client=firefox-b-d&q=pytthon+isoformat+regex
    regex = r'(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9]) (2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[0-3]|[01][0-9]):[0-5][0-9])?'
    return re.sub(regex, "<DATE>", string)




# --- test functions ----------------------------------------------------------
def test_main_entry3_plain(capsys, tmp_path):
    """Parsing first example (by name)"""
    copy_from_data(tmp_path, ["template.html", "entry3_optional.txt"])
    ret = gresiblos.main(["--template", str(tmp_path / "template.html"), "-d", str(tmp_path), str(tmp_path / "entry3_optional.txt")])
    captured = capsys.readouterr()
    assert patch_output(captured.out, tmp_path) == """Processing '<DIR>/entry3_optional.txt'
Writing to <DIR>/entry3_optional.html
"""
    assert patch_output(captured.err, tmp_path) == ""
    p1g = tmp_path / "entry3_optional.html"
    p1o = Path(TEST_PATH) / "entry3_optional_plain.html"
    assert patch_date(p1g.read_text()) == p1o.read_text()
    psg = tmp_path / "entries.json"
    pso = Path(TEST_PATH) / "entry3_sum.json"
    assert patch_date(psg.read_text()) == pso.read_text()


def test_main_entry3_degrotesque_missing(capsys, tmp_path):
    """Parsing first example (by name)"""
    # https://stackoverflow.com/questions/51044068/test-for-import-of-optional-dependencies-in-init-py-with-pytest-python-3-5
    with patch.dict(sys.modules, {'degrotesque': None}):
        reload(sys.modules['gresiblos'])
        copy_from_data(tmp_path, ["template.html", "entry3_optional.txt"])
        try:
            ret = gresiblos.main(["--template", str(tmp_path / "template.html"), "--degrotesque", "-d", str(tmp_path), str(tmp_path / "entry3_optional.txt")])
            assert False # pragma: no cover
        except SystemExit as e:
            assert type(e)==type(SystemExit())
            assert e.code==2
    reload(sys.modules['gresiblos'])
    captured = capsys.readouterr()
    assert patch_output(captured.err, tmp_path) == """gresiblos: error: degrotesque application is set, but degrotesque is not installed
"""
    assert patch_output(captured.out, tmp_path) == ""


def test_main_entry3_degrotesque(capsys, tmp_path):
    """Parsing first example (by name)"""
    copy_from_data(tmp_path, ["template.html", "entry3_optional.txt"])
    ret = gresiblos.main(["--template", str(tmp_path / "template.html"), "--degrotesque", "-d", str(tmp_path), str(tmp_path / "entry3_optional.txt")])
    captured = capsys.readouterr()
    assert patch_output(captured.out, tmp_path) == """Processing '<DIR>/entry3_optional.txt'
Writing to <DIR>/entry3_optional.html
"""
    assert patch_output(captured.err, tmp_path) == ""
    p1g = tmp_path / "entry3_optional.html"
    p1o = Path(TEST_PATH) / "entry3_optional_degrotesque.html"
    assert patch_date(p1g.read_text()) == p1o.read_text()
    psg = tmp_path / "entries.json"
    pso = Path(TEST_PATH) / "entry3_sum.json"
    assert patch_date(psg.read_text()) == pso.read_text()


def test_main_entry3_markdown_missing(capsys, tmp_path):
    """Parsing first example (by name)"""
    # https://stackoverflow.com/questions/51044068/test-for-import-of-optional-dependencies-in-init-py-with-pytest-python-3-5
    with patch.dict(sys.modules, {'markdown': None}):
        reload(sys.modules['gresiblos'])
        copy_from_data(tmp_path, ["template.html", "entry3_optional.txt"])
        try:
            ret = gresiblos.main(["--template", str(tmp_path / "template.html"), "--markdown", "-d", str(tmp_path), str(tmp_path / "entry3_optional.txt")])
            assert False # pragma: no cover
        except SystemExit as e:
            assert type(e)==type(SystemExit())
            assert e.code==2
    reload(sys.modules['gresiblos'])
    captured = capsys.readouterr()
    assert patch_output(captured.err, tmp_path) == """gresiblos: error: markdown application is set, but markdown is not installed
"""
    assert patch_output(captured.out, tmp_path) == ""


def test_main_entry3_markdown(capsys, tmp_path):
    """Parsing first example (by name)"""
    copy_from_data(tmp_path, ["template.html", "entry3_optional.txt"])
    ret = gresiblos.main(["--template", str(tmp_path / "template.html"), "--markdown", "-d", str(tmp_path), str(tmp_path / "entry3_optional.txt")])
    captured = capsys.readouterr()
    assert patch_output(captured.out, tmp_path) == """Processing '<DIR>/entry3_optional.txt'
Writing to <DIR>/entry3_optional.html
"""
    assert patch_output(captured.err, tmp_path) == ""
    p1g = tmp_path / "entry3_optional.html"
    p1o = Path(TEST_PATH) / "entry3_optional_markdown.html"
    assert patch_date(p1g.read_text()) == p1o.read_text()
    psg = tmp_path / "entries.json"
    pso = Path(TEST_PATH) / "entry3_sum.json"
    assert patch_date(psg.read_text()) == pso.read_text()
    
    
def test_main_entry3_missing2(capsys, tmp_path):
    """Parsing first example (by name)"""
    # https://stackoverflow.com/questions/51044068/test-for-import-of-optional-dependencies-in-init-py-with-pytest-python-3-5
    with patch.dict(sys.modules, {'degrotesque': None, 'markdown': None}):
        reload(sys.modules['gresiblos'])
        copy_from_data(tmp_path, ["template.html", "entry3_optional.txt"])
        try:
            ret = gresiblos.main(["--template", str(tmp_path / "template.html"), "--markdown", "--degrotesque", "-d", str(tmp_path), str(tmp_path / "entry3_optional.txt")])
            assert False # pragma: no cover
        except SystemExit as e:
            assert type(e)==type(SystemExit())
            assert e.code==2
    reload(sys.modules['gresiblos'])
    captured = capsys.readouterr()
    assert patch_output(captured.err, tmp_path) == """gresiblos: error: degrotesque application is set, but degrotesque is not installed
gresiblos: error: markdown application is set, but markdown is not installed
"""
    assert patch_output(captured.out, tmp_path) == ""


def test_main_entry3_both(capsys, tmp_path):
    """Parsing first example (by name)"""
    copy_from_data(tmp_path, ["template.html", "entry3_optional.txt"])
    ret = gresiblos.main(["--template", str(tmp_path / "template.html"), "--degrotesque", "--markdown", "-d", str(tmp_path), str(tmp_path / "entry3_optional.txt")])
    captured = capsys.readouterr()
    assert patch_output(captured.out, tmp_path) == """Processing '<DIR>/entry3_optional.txt'
Writing to <DIR>/entry3_optional.html
"""
    assert patch_output(captured.err, tmp_path) == ""
    p1g = tmp_path / "entry3_optional.html"
    p1o = Path(TEST_PATH) / "entry3_optional_both.html"
    assert patch_date(p1g.read_text()) == p1o.read_text()
    psg = tmp_path / "entries.json"
    pso = Path(TEST_PATH) / "entry3_sum.json"
    assert patch_date(psg.read_text()) == pso.read_text()
