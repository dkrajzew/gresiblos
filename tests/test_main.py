#!/usr/bin/env python
"""gresiblos - Tests for the main method."""
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
from util import pname
import gresiblos



# --- test functions ----------------------------------------------------------
def test_main_empty1(capsys):
    """Test behaviour if no arguments are given"""
    try:
        ret = gresiblos.main([])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==2
    captured = capsys.readouterr()
    assert pname(captured.err) == """usage: gresiblos [-h] [-c FILE] [-d DESTINATION] [-t TEMPLATE] [-e EXTENSION]
                 [-s STATE] [--index-output INDEX_OUTPUT]
                 [--chrono-output CHRONO_OUTPUT] [--alpha-output ALPHA_OUTPUT]
                 [--to-html] [--markdown] [--degrotesque]
                 [--topic-format TOPIC_FORMAT] [--index-indent INDEX_INDENT]
                 [--date-format DATE_FORMAT] [--rss-output RSS_OUTPUT]
                 [--atom-output ATOM_OUTPUT] [--feed-title FEED_TITLE]
                 [--feed-site FEED_SITE] [--feed-description FEED_DESCRIPTION]
                 [--feed-editor-email FEED_EDITOR_EMAIL]
                 [--feed-editor-name FEED_EDITOR_NAME]
                 [--feed-language FEED_LANGUAGE]
                 [--feed-copyright FEED_COPYRIGHT] [--feed-utz FEED_UTZ]
                 [--version]
                 input
gresiblos: error: the following arguments are required: input
"""
    assert pname(captured.out) == ""


def test_main_empty2(capsys):
    """Test behaviour if no arguments are given"""
    try:
        ret = gresiblos.main()
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==2
    captured = capsys.readouterr()
    assert pname(captured.err) == """usage: gresiblos [-h] [-c FILE] [-d DESTINATION] [-t TEMPLATE] [-e EXTENSION]
                 [-s STATE] [--index-output INDEX_OUTPUT]
                 [--chrono-output CHRONO_OUTPUT] [--alpha-output ALPHA_OUTPUT]
                 [--to-html] [--markdown] [--degrotesque]
                 [--topic-format TOPIC_FORMAT] [--index-indent INDEX_INDENT]
                 [--date-format DATE_FORMAT] [--rss-output RSS_OUTPUT]
                 [--atom-output ATOM_OUTPUT] [--feed-title FEED_TITLE]
                 [--feed-site FEED_SITE] [--feed-description FEED_DESCRIPTION]
                 [--feed-editor-email FEED_EDITOR_EMAIL]
                 [--feed-editor-name FEED_EDITOR_NAME]
                 [--feed-language FEED_LANGUAGE]
                 [--feed-copyright FEED_COPYRIGHT] [--feed-utz FEED_UTZ]
                 [--version]
                 input
gresiblos: error: the following arguments are required: input
"""
    assert pname(captured.out) == ""


def test_main_help(capsys):
    """Test behaviour when help is wished"""
    try:
        gresiblos.main(["--help"])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==0
    captured = capsys.readouterr()
    assert pname(captured.out) == PRE_3_13_HELP if sys.version_info[1] < 13 else POST_3_13_HELP
    assert pname(captured.err) == ""


def test_main_version(capsys):
    """Test behaviour when version information is wished"""
    try:
        gresiblos.main(["--version"])
        assert False # pragma: no cover
    except SystemExit as e:
        assert type(e)==type(SystemExit())
        assert e.code==0
    captured = capsys.readouterr()
    assert pname(captured.out) == """gresiblos 0.10.0
"""
    assert pname(captured.err) == ""


PRE_3_13_HELP = """usage: gresiblos [-h] [-c FILE] [-d DESTINATION] [-t TEMPLATE] [-e EXTENSION]
                 [-s STATE] [--index-output INDEX_OUTPUT]
                 [--chrono-output CHRONO_OUTPUT] [--alpha-output ALPHA_OUTPUT]
                 [--to-html] [--markdown] [--degrotesque]
                 [--topic-format TOPIC_FORMAT] [--index-indent INDEX_INDENT]
                 [--date-format DATE_FORMAT] [--rss-output RSS_OUTPUT]
                 [--atom-output ATOM_OUTPUT] [--feed-title FEED_TITLE]
                 [--feed-site FEED_SITE] [--feed-description FEED_DESCRIPTION]
                 [--feed-editor-email FEED_EDITOR_EMAIL]
                 [--feed-editor-name FEED_EDITOR_NAME]
                 [--feed-language FEED_LANGUAGE]
                 [--feed-copyright FEED_COPYRIGHT] [--feed-utz FEED_UTZ]
                 [--version]
                 input

greyrat's simple blog system

positional arguments:
  input

options:
  -h, --help            show this help message and exit
  -c FILE, --config FILE
                        Reads the named configuration file
  -d DESTINATION, --destination DESTINATION
                        The path to store the generated file(s) into
  -t TEMPLATE, --template TEMPLATE
                        Defines the template file to use
  -e EXTENSION, --extension EXTENSION
                        The extension of the built file(s)
  -s STATE, --state STATE
                        The state the entries must have for being processed
  --index-output INDEX_OUTPUT
                        Writes the index to the named file
  --chrono-output CHRONO_OUTPUT
                        Writes the named file with entries in chronological
                        order
  --alpha-output ALPHA_OUTPUT
                        Writes the named file with entries in alphabetical
                        order
  --to-html             If set, basic HTML tags are added
  --markdown            If set, markdown is applied on the contents
  --degrotesque         If set, degrotesque is applied on contents, abstract,
                        and title
  --topic-format TOPIC_FORMAT
                        Defines how each of the topics is rendered
  --index-indent INDEX_INDENT
                        Defines the indent used for the index file
  --date-format DATE_FORMAT
                        Defines the time format used
  --rss-output RSS_OUTPUT
                        Writes an RSS 2.0 feed to the named file
  --atom-output ATOM_OUTPUT
                        Writes an Atom feed to the named file
  --feed-title FEED_TITLE
                        Title to use for the feed
  --feed-site FEED_SITE
                        Base URL used to prefix entry filenames in the feed
  --feed-description FEED_DESCRIPTION
                        The feed description
  --feed-editor-email FEED_EDITOR_EMAIL
                        The email of the feed editor
  --feed-editor-name FEED_EDITOR_NAME
                        The name of the feed editor
  --feed-language FEED_LANGUAGE
                        The language of the feed
  --feed-copyright FEED_COPYRIGHT
                        The copyright information about the feed
  --feed-utz FEED_UTZ   The feed's time zone
  --version             show program's version number and exit

(c) Daniel Krajzewicz 2016-2026
"""


POST_3_13_HELP = """usage: gresiblos [-h] [-c FILE] [-d DESTINATION] [-t TEMPLATE] [-e EXTENSION]
                 [-s STATE] [--index-output INDEX_OUTPUT]
                 [--chrono-output CHRONO_OUTPUT] [--alpha-output ALPHA_OUTPUT]
                 [--markdown] [--degrotesque] [--topic-format TOPIC_FORMAT]
                 [--index-indent INDEX_INDENT] [--date-format DATE_FORMAT]
                 [--rss-output RSS_OUTPUT] [--atom-output ATOM_OUTPUT]
                 [--feed-title FEED_TITLE] [--feed-site FEED_SITE]
                 [--feed-description FEED_DESCRIPTION]
                 [--feed-editor-email FEED_EDITOR_EMAIL]
                 [--feed-editor-name FEED_EDITOR_NAME]
                 [--feed-language FEED_LANGUAGE]
                 [--feed-copyright FEED_COPYRIGHT] [--feed-utz FEED_UTZ]
                 [--version]
                 input

greyrat's simple blog system

positional arguments:
  input

options:
  -h, --help            show this help message and exit
  -c, --config FILE     Reads the named configuration file
  -d, --destination DESTINATION
                        The path to store the generated file(s) into
  -t, --template TEMPLATE
                        Defines the template file to use
  -e, --extension EXTENSION
                        The extension of the built file(s)
  -s, --state STATE     The state the entries must have for being processed
  --index-output INDEX_OUTPUT
                        Writes the index to the named file
  --chrono-output CHRONO_OUTPUT
                        Writes the named file with entries in chronological
                        order
  --alpha-output ALPHA_OUTPUT
                        Writes the named file with entries in alphabetical
                        order
  --to-html             If set, basic HTML tags are added
  --markdown            If set, markdown is applied on the contents
  --degrotesque         If set, degrotesque is applied on contents, abstract,
                        and title
  --topic-format TOPIC_FORMAT
                        Defines how each of the topics is rendered
  --index-indent INDEX_INDENT
                        Defines the indent used for the index file
  --date-format DATE_FORMAT
                        Defines the time format used
  --rss-output RSS_OUTPUT
                        Writes an RSS 2.0 feed to the named file
  --atom-output ATOM_OUTPUT
                        Writes an Atom feed to the named file
  --feed-title FEED_TITLE
                        Title to use for the feed
  --feed-site FEED_SITE
                        Base URL used to prefix entry filenames in the feed
  --feed-description FEED_DESCRIPTION
                        The feed description
  --feed-editor-email FEED_EDITOR_EMAIL
                        The email of the feed editor
  --feed-editor-name FEED_EDITOR_NAME
                        The name of the feed editor
  --feed-language FEED_LANGUAGE
                        The language of the feed
  --feed-copyright FEED_COPYRIGHT
                        The copyright information about the feed
  --feed-utz FEED_UTZ   The feed's time zone
  --version             show program's version number and exit

(c) Daniel Krajzewicz 2016-2026
"""