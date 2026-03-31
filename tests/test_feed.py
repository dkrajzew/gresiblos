#!/usr/bin/env python
"""gresiblos - Tests for feed export."""
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
    assert fpread(tmp_path / "my-first-blog-entry.html") == fpread(Path(TEST_PATH) / "my-first-blog-entry.html")
    assert fpread(tmp_path / "my-second-blog-entry.html") == fpread(Path(TEST_PATH) / "my-second-blog-entry.html")
    assert fpread(tmp_path / "rss.xml") == fpread(Path(TEST_PATH) / "rss_plain.xml")


def test_rss_ext(capsys, tmp_path):
    """Generating RSS with additional arguments"""
    copy_files_and_template(tmp_path, ["entry1.txt", "entry2.txt"])
    ret = gresiblos.main(["--template", str(tmp_path / "template.html"), "-d", str(tmp_path), str(tmp_path / "entry*.txt"), "--rss-output", str(tmp_path / "rss.xml"), "--feed-title", "foo_title", "--feed-site", "foo_site", "--feed-description", "foo_desc", "--feed-editor-email", "foo_editor_email", "--feed-editor-name", "foo_editor_name", "--feed-language", "foo_lang", "--feed-copyright", "foo_copy"])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/entry1.txt'
Writing to <DIR>/my-first-blog-entry.html
Processing '<DIR>/entry2.txt'
Writing to <DIR>/my-second-blog-entry.html
Writing RSS feed to '<DIR>/rss.xml'
"""
    assert pname(captured.err, tmp_path) == ""
    assert fpread(tmp_path / "my-first-blog-entry.html") == fpread(Path(TEST_PATH) / "my-first-blog-entry.html")
    assert fpread(tmp_path / "my-second-blog-entry.html") == fpread(Path(TEST_PATH) / "my-second-blog-entry.html")
    assert fpread(tmp_path / "rss.xml") == fpread(Path(TEST_PATH) / "rss_ext.xml")


def test_rss_dateformat(capsys, tmp_path):
    """Generating RSS with a different date format in entries"""
    copy_files_and_template(tmp_path, ["entry1_dateformat2.txt"])
    ret = gresiblos.main(["--template", str(tmp_path / "template.html"), "-d", str(tmp_path), str(tmp_path / "entry*.txt"), "--rss-output", str(tmp_path / "rss.xml"), "--date-format", "%d.%m.%Y %H:%M:%S"])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/entry1_dateformat2.txt'
Writing to <DIR>/my-first-blog-entry.html
Writing RSS feed to '<DIR>/rss.xml'
"""
    assert pname(captured.err, tmp_path) == ""
    assert fpread(tmp_path / "my-first-blog-entry.html") == fpread(Path(TEST_PATH) / "my-first-blog-entry_dateformat.html")
    assert fpread(tmp_path / "rss.xml") == fpread(Path(TEST_PATH) / "rss_plain_dateformat.xml")



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
    c = fpread(tmp_path / "atom.xml")
    with open("d:\\atom.xml", "w") as fdo:
        fdo.write(c)
    assert pname(captured.err, tmp_path) == ""
    assert fpread(tmp_path / "my-first-blog-entry.html") == fpread(Path(TEST_PATH) / "my-first-blog-entry.html")
    assert fpread(tmp_path / "my-second-blog-entry.html") == fpread(Path(TEST_PATH) / "my-second-blog-entry.html")
    assert fpread(tmp_path / "atom.xml") == fpread(Path(TEST_PATH) / "atom_plain.xml")


def test_atom_ext(capsys, tmp_path):
    """Generating Atom with no additional arguments"""
    copy_files_and_template(tmp_path, ["entry1.txt", "entry2.txt"])
    ret = gresiblos.main(["--template", str(tmp_path / "template.html"), "-d", str(tmp_path), str(tmp_path / "entry*.txt"), "--atom-output", str(tmp_path / "atom.xml"), "--feed-title", "foo_title", "--feed-site", "foo_site", "--feed-description", "foo_desc", "--feed-editor-email", "foo_editor_email", "--feed-editor-name", "foo_editor_name", "--feed-language", "foo_lang", "--feed-copyright", "foo_copy"])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/entry1.txt'
Writing to <DIR>/my-first-blog-entry.html
Processing '<DIR>/entry2.txt'
Writing to <DIR>/my-second-blog-entry.html
Writing Atom feed to '<DIR>/atom.xml'
"""
    assert pname(captured.err, tmp_path) == ""
    assert fpread(tmp_path / "my-first-blog-entry.html") == fpread(Path(TEST_PATH) / "my-first-blog-entry.html")
    assert fpread(tmp_path / "my-second-blog-entry.html") == fpread(Path(TEST_PATH) / "my-second-blog-entry.html")
    assert fpread(tmp_path / "atom.xml") == fpread(Path(TEST_PATH) / "atom_ext.xml")


def test_atom_dateformat(capsys, tmp_path):
    """Generating Atom with a different date format in entries"""
    copy_files_and_template(tmp_path, ["entry1_dateformat2.txt"])
    ret = gresiblos.main(["--template", str(tmp_path / "template.html"), "-d", str(tmp_path), str(tmp_path / "entry*.txt"), "--atom-output", str(tmp_path / "atom.xml"), "--date-format", "%d.%m.%Y %H:%M:%S"])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/entry1_dateformat2.txt'
Writing to <DIR>/my-first-blog-entry.html
Writing Atom feed to '<DIR>/atom.xml'
"""
    assert pname(captured.err, tmp_path) == ""
    assert fpread(tmp_path / "my-first-blog-entry.html") == fpread(Path(TEST_PATH) / "my-first-blog-entry_dateformat.html")
    assert fpread(tmp_path / "atom.xml") == fpread(Path(TEST_PATH) / "atom_plain_dateformat.xml")


def test_feed_bad_values(capsys, tmp_path):
    """Generating Atom with a different date format in entries"""
    copy_files_and_template(tmp_path, ["entry1_bad_topics.txt", "bad_values.cfg"])
    ret = gresiblos.main(["--template", str(tmp_path / "template.html"), "-d", str(tmp_path), str(tmp_path / "entry*.txt"), "-c", str(tmp_path / "bad_values.cfg"), "--atom-output", str(tmp_path / "atom_bad_values.xml"), "--rss-output", str(tmp_path / "rss_bad_values.xml")])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/entry1_bad_topics.txt'
Writing to <DIR>/my-first-blog-entry_bad_topics.html
Writing RSS feed to '<DIR>/rss_bad_values.xml'
Writing Atom feed to '<DIR>/atom_bad_values.xml'
"""
    assert pname(captured.err, tmp_path) == ""
    assert fpread(tmp_path / "my-first-blog-entry_bad_topics.html") == fpread(Path(TEST_PATH) / "my-first-blog-entry_bad_topics.html")
    assert fpread(tmp_path / "atom_bad_values.xml") == fpread(Path(TEST_PATH) / "atom_bad_values.xml")
    assert fpread(tmp_path / "rss_bad_values.xml") == fpread(Path(TEST_PATH) / "rss_bad_values.xml")


