#!/usr/bin/env python
"""gresiblos - Tests for the main method - examples application."""
# =============================================================================
__author__     = "Daniel Krajzewicz"
__copyright__  = "Copyright 2024-2026, Daniel Krajzewicz"
__credits__    = ["Daniel Krajzewicz"]
__license__    = "GPL-3.0"
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
def test_rss_plain(capsys, tmp_path):
    """Generating RSS with no further arguments"""
    copy_files_and_template(tmp_path, ["entry1.txt", "entry2.txt"])
    ret = gresiblos.main(["--template", str(tmp_path / "template.html"), "-d", str(tmp_path), str(tmp_path / "entry*.txt"), "--rss-output", str(tmp_path / "rss.xml")])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/entry1.txt'
Writing to <DIR>/my-first-blog-entry.html
Processing '<DIR>/entry2.txt'
Writing to <DIR>/my-second-blog-entry.html
Writing RSS feed to '<DIR>/rss.xml'
"""
    assert pname(captured.err, tmp_path) == ""
    assert fread(tmp_path / "my-first-blog-entry.html") == fread(Path(TEST_PATH) / "my-first-blog-entry.html")
    assert fread(tmp_path / "my-second-blog-entry.html") == fread(Path(TEST_PATH) / "my-second-blog-entry.html")
    assert fread(tmp_path / "rss.xml") == fread(Path(TEST_PATH) / "rss_plain.xml")


def test_rss_ext(capsys, tmp_path):
    """Generating RSS with additional arguments"""
    copy_files_and_template(tmp_path, ["entry1.txt", "entry2.txt"])
    ret = gresiblos.main(["--template", str(tmp_path / "template.html"), "-d", str(tmp_path), str(tmp_path / "entry*.txt"), "--rss-output", str(tmp_path / "rss.xml"), "--feed-title", "foo_title", "--feed-site", "foo_site", "--feed-description", "foo_desc", "--feed-editor", "foo_editor", "--feed-language", "foo_lang", "--feed-copyright", "foo_copy"])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/entry1.txt'
Writing to <DIR>/my-first-blog-entry.html
Processing '<DIR>/entry2.txt'
Writing to <DIR>/my-second-blog-entry.html
Writing RSS feed to '<DIR>/rss.xml'
"""
    assert pname(captured.err, tmp_path) == ""
    assert fread(tmp_path / "my-first-blog-entry.html") == fread(Path(TEST_PATH) / "my-first-blog-entry.html")
    assert fread(tmp_path / "my-second-blog-entry.html") == fread(Path(TEST_PATH) / "my-second-blog-entry.html")
    assert fread(tmp_path / "rss.xml") == fread(Path(TEST_PATH) / "rss_ext.xml")





def test_atom_plain(capsys, tmp_path):
    """Generating Atom with no further arguments"""
    copy_files_and_template(tmp_path, ["entry1.txt", "entry2.txt"])
    ret = gresiblos.main(["--template", str(tmp_path / "template.html"), "-d", str(tmp_path), str(tmp_path / "entry*.txt"), "--atom-output", str(tmp_path / "atom.xml")])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/entry1.txt'
Writing to <DIR>/my-first-blog-entry.html
Processing '<DIR>/entry2.txt'
Writing to <DIR>/my-second-blog-entry.html
Writing Atom feed to '<DIR>/atom.xml'
"""
    c = fread(tmp_path / "atom.xml")
    with open("d:\\atom_plain.xml", "w") as fd:
        fd.write(c)
    assert pname(captured.err, tmp_path) == ""
    assert fread(tmp_path / "my-first-blog-entry.html") == fread(Path(TEST_PATH) / "my-first-blog-entry.html")
    assert fread(tmp_path / "my-second-blog-entry.html") == fread(Path(TEST_PATH) / "my-second-blog-entry.html")
    assert fread(tmp_path / "atom.xml", True) == fread(Path(TEST_PATH) / "atom_plain.xml", True)


def test_atom_ext(capsys, tmp_path):
    """Generating Atom with no additional arguments"""
    copy_files_and_template(tmp_path, ["entry1.txt", "entry2.txt"])
    ret = gresiblos.main(["--template", str(tmp_path / "template.html"), "-d", str(tmp_path), str(tmp_path / "entry*.txt"), "--atom-output", str(tmp_path / "atom.xml"), "--feed-title", "foo_title", "--feed-site", "foo_site", "--feed-description", "foo_desc", "--feed-editor", "foo_editor", "--feed-language", "foo_lang", "--feed-copyright", "foo_copy"])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/entry1.txt'
Writing to <DIR>/my-first-blog-entry.html
Processing '<DIR>/entry2.txt'
Writing to <DIR>/my-second-blog-entry.html
Writing Atom feed to '<DIR>/atom.xml'
"""
    c = fread(tmp_path / "atom.xml")
    with open("d:\\atom_ext.xml", "w") as fd:
        fd.write(c)
    assert pname(captured.err, tmp_path) == ""
    assert fread(tmp_path / "my-first-blog-entry.html") == fread(Path(TEST_PATH) / "my-first-blog-entry.html")
    assert fread(tmp_path / "my-second-blog-entry.html") == fread(Path(TEST_PATH) / "my-second-blog-entry.html")
    assert fread(tmp_path / "atom.xml", True) == fread(Path(TEST_PATH) / "atom_ext.xml", True)


