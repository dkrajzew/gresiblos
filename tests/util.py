#!/usr/bin/env python
"""gresiblos - Utility functions for tests."""
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
import gresiblos
import shutil
import re
TEST_PATH = os.path.split(__file__)[0]
TEMPLATE_PATH = os.path.split(gresiblos.__file__)[0]



# --- imports ---------------------------------------------------------------
def pname(string, path="<DIR>"):
    """Unify the script name and the reported folder"""
    string = string.replace(str(path), "<DIR>").replace("\\", "/")
    return string.replace("__main__.py", "gresiblos").replace("pytest", "gresiblos").replace("optional arguments", "options")


def pdate(s):
    """Unify dates"""
    # https://www.google.com/search?client=firefox-b-d&q=pytthon+isoformat+regex
    regex1 = r'(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9]) (2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[0-3]|[01][0-9]):[0-5][0-9])?'
    s = re.sub(regex1, "<DATE1>", s)
    regex2 = r'\w\w\w\, \d\d \w\w\w \d\d\d\d \d\d:\d\d:\d\d [-+]\d\d\d\d'
    s = re.sub(regex2, "<DATE2>", s)
    regex3 = r'\d\d\d\d\-\d\d\-\d\d \d\d:\d\d:\d\d'
    s = re.sub(regex3, "<DATE3>", s)
    regex4 = r'\d\d\.\d\d\.\d\d\d\d \d\d:\d\d:\d\d'
    s = re.sub(regex4, "<DATE4>", s)
    regex5 = r'\d\d\d\d\-\d\d\-\d\dT\d\d:\d\d:\d\d(\.\d+)?[\+\-]\d\d:\d\d'
    s = re.sub(regex5, "<DATE5>", s)
    return s


def fread(filepath):
    """Read a file"""
    return filepath.read_text()

def fpread(filepath):
    """Read a file and dates"""
    c1 = filepath.read_text()
    return pdate(c1)


def copy_template(tmp_path):
    """Copy the template to the test path"""
    shutil.copy(os.path.join((TEMPLATE_PATH), "data", "template.html"), str(tmp_path / "template.html"))


def copy_files(tmp_path, files):
    """Copy named files to the test folder"""
    for file in files:
        shutil.copy(os.path.join((TEST_PATH), file), str(tmp_path / file))


def copy_files_and_template(tmp_path, files):
    """Copy the template and named files to the test folder"""
    copy_template(tmp_path)
    copy_files(tmp_path, files)



