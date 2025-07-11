[![License: BSD](https://img.shields.io/badge/License-BSD-green.svg)](https://github.com/dkrajzew/gresiblos/blob/main/LICENSE)
[![PyPI version](https://badge.fury.io/py/gresiblos.svg)](https://pypi.org/project/gresiblos/)
![test](https://github.com/dkrajzew/gresiblos/actions/workflows/test.yml/badge.svg)
[![Downloads](https://pepy.tech/badge/gresiblos)](https://pepy.tech/projects/gresiblos)
[![Downloads](https://static.pepy.tech/badge/gresiblos/week)](https://pepy.tech/projects/gresiblos)
[![Coverage Status](https://coveralls.io/repos/github/dkrajzew/gresiblos/badge.svg?branch=main)](https://coveralls.io/github/dkrajzew/gresiblos?branch=main)
[![Documentation Status](https://readthedocs.org/projects/gresiblos/badge/?version=latest)](https://gresiblos.readthedocs.io/en/latest/?badge=latest)
[![Dependecies](https://img.shields.io/badge/dependencies-none-green)](https://img.shields.io/badge/dependencies-none-green)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=GVQQWZKB6FDES)

#

__gresiblos__ - a simple private blogging system

## Introduction

__gresiblos__ is a simple blogging system written in [Python](https://www.python.org/).  __gresiblos__ generates static HTML pages from optionally annotated text, markdown, or HTML files. __gresiblos__ is the acronym for __*gre*yrat&#39;s *si*mple *blo*g *s*ystem__.

__gresiblos__ reads blog entries from files that may include some meta information and embeds the contents into a template. Optionally, in addition, it generates a json-file with meta information about the entries. __gresiblos__ comes with a php-file that realises browsing, as well as with a php-file that generates rss and atom feeds.


## Usage

Write your blog entries as text, markdown or HTML.

Then run __gresiblos__ on them:

```shell
gresiblos ./blog/*.txt
```

&#8230; and it will convert them into complete HTML pages using a default template.

For more complete blogs &mdash; including authors, abstracts, release dates, etc., the entries can be enriched by meta information. __gresiblos__ templates support placeholders that are filled with given meta information, as well as optional fields.

You may find further information at [the gresiblos documentation pages](https://gresiblos.readthedocs.io/en/latest/).


## Documentation

__gresiblos__ is meant to be run on the command line. The documentation consists of a [user manual](usage.md) and a [man-page like call documentation](cmd.md).

If you want to contribute, you may check the [API documentation](api_gresiblos.md) or visit [gresiblos on github](https://github.com/dkrajzew/gresiblos) where besides the code you may find the [gresiblos issue tracker](https://github.com/dkrajzew/gresiblos/issues) or a [discussions about gresiblos](https://github.com/dkrajzew/gresiblos/discussions) sections.

Additional documentation includes a page with relevant [links](links.md), the [ChangeLog](changes.md), as well as the [license](license.md). __gresiblos__ is licensed under the [BSD license](license.md).


## Background

I wanted to have a blog and I wanted it to use static pages. That&#39;s why I wrote it. __gresiblos__ has some additional features &#8212; like the inclusion of custom JavaScript and CSS files &#8212; I needed for [my own blog](https://www.krajzewicz.de/blog/index.php).



## Status &amp; Contributing

__gresiblos__ works as intended for me, but lacks quite some features of enterprise systems. The next steps to release 1.0 will involve some refactorings, including API changes.

Please let me know if you have any idea / feature request / question / whatever or contribute to __gresiblos__&hellip;



