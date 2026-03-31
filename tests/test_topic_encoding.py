#!/usr/bin/env python
"""gresiblos - Tests for topic encoding."""
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
from pathlib import Path
from util import pname, copy_files_and_template, fread, fpread, TEST_PATH
import gresiblos



# --- test functions ----------------------------------------------------------
def test_topic_encoding_entry1_plain(capsys, tmp_path):
    """Parsing first example (by name) with default format"""
    copy_files_and_template(tmp_path, ["entry1.txt"])
    ret = gresiblos.main(["--template", str(tmp_path / "template.html"), "-d", str(tmp_path), str(tmp_path / "entry1.txt")])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/entry1.txt'
Writing to <DIR>/my-first-blog-entry.html
"""
    assert pname(captured.err, tmp_path) == ""
    assert fpread(tmp_path / "my-first-blog-entry.html") == fpread(Path(TEST_PATH) / "my-first-blog-entry.html")


def test_topic_encoding_entry1_format(capsys, tmp_path):
    """Parsing first example (by name) with given format"""
    copy_files_and_template(tmp_path, ["entry1.txt"])
    ret = gresiblos.main(["--topic-format", "<a href=\"index.php?topic=[[:topic:]]\">[[:topic:]]</a>", "--template", str(tmp_path / "template.html"), "-d", str(tmp_path), str(tmp_path / "entry1.txt")])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/entry1.txt'
Writing to <DIR>/my-first-blog-entry.html
"""
    assert pname(captured.err, tmp_path) == ""
    assert fpread(tmp_path / "my-first-blog-entry.html") == fpread(Path(TEST_PATH) / "my-first-blog-entry_phpindex.html")
