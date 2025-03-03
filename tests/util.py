#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
"""gresiblos - Utility functions for tests."""
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
import os
import shutil
import re
TEST_PATH = os.path.split(__file__)[0]



# --- imports ---------------------------------------------------------------
def pname(string, path="<DIR>"):
    string = string.replace(str(path), "<DIR>").replace("\\", "/")
    return string.replace("__main__.py", "gresiblos").replace("pytest", "gresiblos").replace("optional arguments", "options")


def pdate(string):
    # https://www.google.com/search?client=firefox-b-d&q=pytthon+isoformat+regex
    regex = r'(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9]) (2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[0-3]|[01][0-9]):[0-5][0-9])?'
    return re.sub(regex, "<DATE>", string)


def copy_from_data(tmp_path, files):
    for file in files:
        shutil.copy(os.path.join((TEST_PATH), "..", "data", file), str(tmp_path / file))


    
    