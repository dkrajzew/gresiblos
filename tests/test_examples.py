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
from util import pname, copy_files_and_template, copy_files, copy_template, fread, fpread, TEST_PATH
import gresiblos



# --- test functions ----------------------------------------------------------
def test_plain_examples(capsys, tmp_path):
    """Generating RSS with no further arguments"""
    os.makedirs(tmp_path / "blog")
    copy_files(tmp_path / "blog", ["plain-example1.txt", "plain-example2.txt"])
    copy_template(tmp_path)
    ret = gresiblos.main(["-d", str(tmp_path), str(tmp_path / "blog/*.txt")])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/blog/plain-example1.txt'
Writing to <DIR>/plain-example1.html
Processing '<DIR>/blog/plain-example2.txt'
Writing to <DIR>/plain-example2.html
"""
    assert pname(captured.err, tmp_path) == ""
    assert fpread(tmp_path / "plain-example1.html") == fpread(Path(TEST_PATH) / "plain-example1.html")
    assert fpread(tmp_path / "plain-example2.html") == fpread(Path(TEST_PATH) / "plain-example2.html")

def test_plain_examples_markdown(capsys, tmp_path):
    """Generating RSS with no further arguments"""
    os.makedirs(tmp_path / "blog")
    copy_files(tmp_path / "blog", ["plain-example1.txt", "plain-example2.txt"])
    copy_template(tmp_path)
    ret = gresiblos.main(["-d", str(tmp_path), "--markdown", str(tmp_path / "blog/*.txt")])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/blog/plain-example1.txt'
Writing to <DIR>/plain-example1.html
Processing '<DIR>/blog/plain-example2.txt'
Writing to <DIR>/plain-example2.html
"""
    assert pname(captured.err, tmp_path) == ""
    assert fpread(tmp_path / "plain-example1.html") == fpread(Path(TEST_PATH) / "plain-example1_md.html")
    assert fpread(tmp_path / "plain-example2.html") == fpread(Path(TEST_PATH) / "plain-example2_md.html")

def test_full_examples_markdown(capsys, tmp_path):
    """Generating RSS with no further arguments"""
    os.makedirs(tmp_path / "blog")
    copy_files(tmp_path / "blog", ["full-example1.txt", "full-example2.txt"])
    copy_template(tmp_path)
    ret = gresiblos.main(["-d", str(tmp_path), "--markdown", str(tmp_path / "blog/*.txt")])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/blog/full-example1.txt'
Writing to <DIR>/my-first-blog-entry-example.html
Processing '<DIR>/blog/full-example2.txt'
Writing to <DIR>/my-second-blog-entry-example.html
"""
    assert pname(captured.err, tmp_path) == ""
    assert fpread(tmp_path / "my-first-blog-entry-example.html") == fpread(Path(TEST_PATH) / "my-first-blog-entry-example.html")
    assert fpread(tmp_path / "my-second-blog-entry-example.html") == fpread(Path(TEST_PATH) / "my-second-blog-entry-example.html")

def test_full_examples_template(capsys, tmp_path):
    """Generating RSS with no further arguments"""
    os.makedirs(tmp_path / "blog")
    copy_files(tmp_path / "blog", ["full-example1_tpl1.txt", "full-example2_tpl1.txt"])
    copy_files(tmp_path, ["example-template.txt"])
    ret = gresiblos.main(["--template", str(tmp_path / "example-template.txt"), "-d", str(tmp_path), str(tmp_path / "blog/*.txt")])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/blog/full-example1_tpl1.txt'
Writing to <DIR>/my-first-blog-entry-example_tpl1.html
Processing '<DIR>/blog/full-example2_tpl1.txt'
Writing to <DIR>/my-second-blog-entry-example_tpl1.html
"""
    assert pname(captured.err, tmp_path) == ""
    assert fpread(tmp_path / "my-first-blog-entry-example_tpl1.html") == fpread(Path(TEST_PATH) / "my-first-blog-entry-example_tpl1.html")
    assert fpread(tmp_path / "my-second-blog-entry-example_tpl1.html") == fpread(Path(TEST_PATH) / "my-second-blog-entry-example_tpl1.html")

def test_full_examples_rss(capsys, tmp_path):
    """Generating RSS with no further arguments"""
    os.makedirs(tmp_path / "blog")
    copy_files(tmp_path / "blog", ["full-example1_tpl1.txt", "full-example2_tpl1.txt"])
    copy_files(tmp_path, ["example-template.txt"])
    ret = gresiblos.main(["--template", str(tmp_path / "example-template.txt"), "-d", str(tmp_path), str(tmp_path / "blog/*.txt"), "--rss-output", str(tmp_path / "rss-example.xml"),
    "--feed-title", "Collected Notes", "--feed-site", "http://john.doe.org", "--feed-description", "Notes collected in the past time", "--feed-editor-email", "john@doe.org", "--feed-editor-name", "John Doe", "--feed-copyright", "(c) John Doe 2026"])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/blog/full-example1_tpl1.txt'
Writing to <DIR>/my-first-blog-entry-example_tpl1.html
Processing '<DIR>/blog/full-example2_tpl1.txt'
Writing to <DIR>/my-second-blog-entry-example_tpl1.html
Writing RSS feed to '<DIR>/rss-example.xml'
"""
    assert pname(captured.err, tmp_path) == ""
    assert fpread(tmp_path / "my-first-blog-entry-example_tpl1.html") == fpread(Path(TEST_PATH) / "my-first-blog-entry-example_tpl1.html")
    assert fpread(tmp_path / "my-second-blog-entry-example_tpl1.html") == fpread(Path(TEST_PATH) / "my-second-blog-entry-example_tpl1.html")
    assert fpread(tmp_path / "rss-example.xml") == fpread(Path(TEST_PATH) / "rss_example.xml")

def test_full_examples_atom(capsys, tmp_path):
    """Generating RSS with no further arguments"""
    os.makedirs(tmp_path / "blog")
    copy_files(tmp_path / "blog", ["full-example1_tpl1.txt", "full-example2_tpl1.txt"])
    copy_files(tmp_path, ["example-template.txt"])
    ret = gresiblos.main(["--template", str(tmp_path / "example-template.txt"), "-d", str(tmp_path), str(tmp_path / "blog/*.txt"), "--atom-output", str(tmp_path / "atom-example.xml"),
    "--feed-title", "Collected Notes", "--feed-site", "http://john.doe.org", "--feed-description", "Notes collected in the past time", "--feed-editor-email", "john@doe.org", "--feed-editor-name", "John Doe", "--feed-copyright", "(c) John Doe 2026"])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/blog/full-example1_tpl1.txt'
Writing to <DIR>/my-first-blog-entry-example_tpl1.html
Processing '<DIR>/blog/full-example2_tpl1.txt'
Writing to <DIR>/my-second-blog-entry-example_tpl1.html
Writing Atom feed to '<DIR>/atom-example.xml'
"""
    assert pname(captured.err, tmp_path) == ""
    assert fpread(tmp_path / "my-first-blog-entry-example_tpl1.html") == fpread(Path(TEST_PATH) / "my-first-blog-entry-example_tpl1.html")
    assert fpread(tmp_path / "my-second-blog-entry-example_tpl1.html") == fpread(Path(TEST_PATH) / "my-second-blog-entry-example_tpl1.html")
    assert fpread(tmp_path / "atom-example.xml") == fpread(Path(TEST_PATH) / "atom_example.xml")

def test_full_examples_feed_config(capsys, tmp_path):
    """Generating RSS with no further arguments"""
    os.makedirs(tmp_path / "blog")
    copy_files(tmp_path / "blog", ["full-example1_tpl1.txt", "full-example2_tpl1.txt"])
    copy_files(tmp_path, ["example-template.txt", "examples.cfg"])
    ret = gresiblos.main(["--template", str(tmp_path / "example-template.txt"), "-d", str(tmp_path), str(tmp_path / "blog/*.txt"), "-c", str(tmp_path / "examples.cfg"), "--rss-output", str(tmp_path / "rss-example.xml"), "--atom-output", str(tmp_path / "atom-example.xml")])
    captured = capsys.readouterr()
    assert pname(captured.out, tmp_path) == """Processing '<DIR>/blog/full-example1_tpl1.txt'
Writing to <DIR>/my-first-blog-entry-example_tpl1.html
Processing '<DIR>/blog/full-example2_tpl1.txt'
Writing to <DIR>/my-second-blog-entry-example_tpl1.html
Writing RSS feed to '<DIR>/rss-example.xml'
Writing Atom feed to '<DIR>/atom-example.xml'
"""
    assert pname(captured.err, tmp_path) == ""
    assert fpread(tmp_path / "my-first-blog-entry-example_tpl1.html") == fpread(Path(TEST_PATH) / "my-first-blog-entry-example_tpl1.html")
    assert fpread(tmp_path / "my-second-blog-entry-example_tpl1.html") == fpread(Path(TEST_PATH) / "my-second-blog-entry-example_tpl1.html")
    assert fpread(tmp_path / "atom-example.xml") == fpread(Path(TEST_PATH) / "atom_example.xml")
    assert fpread(tmp_path / "rss-example.xml") == fpread(Path(TEST_PATH) / "rss_example.xml")
