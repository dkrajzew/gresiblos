# gresiblos

[![License: GPL](https://img.shields.io/badge/License-GPL-green.svg)](https://github.com/dkrajzew/gresiblos/blob/master/LICENSE)
[![PyPI version](https://badge.fury.io/py/gresiblos.svg)](https://pypi.python.org/pypi/gresiblos)
![test](https://github.com/dkrajzew/gresiblos/actions/workflows/test.yml/badge.svg)
[![Downloads](https://pepy.tech/badge/gresiblos)](https://pepy.tech/project/gresiblos)
[![Downloads](https://static.pepy.tech/badge/gresiblos/week)](https://pepy.tech/project/gresiblos)
[![Coverage Status](https://coveralls.io/repos/github/dkrajzew/gresiblos/badge.svg?branch=main)](https://coveralls.io/github/dkrajzew/gresiblos?branch=main)
[![Documentation Status](https://readthedocs.org/projects/gresiblos/badge/?version=latest)](https://gresiblos.readthedocs.io/en/latest/?badge=latest)
[![Dependecies](https://img.shields.io/badge/dependencies-none-green)](https://img.shields.io/badge/dependencies-none-green)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=GVQQWZKB6FDES)


## Introduction

__gresiblos__ is the acronym for __*gre*yrat&#39;s *si*mple *blo*g *s*ystem__. It is a simple blogging system written in [Python](https://www.python.org/) that generates static HTML pages from blog content definitions.

In the current stage (v0.4.0), __gresiblos__ reads a file with blog entry contents and meta information and embeds it into a template. It generates a json-file with meta information about the entries for generating lists of topics, entries, or entries with a named topic. __gresiblos__ comes with a php-file that realises browsing entries and topics, and a php-file that generates rss and atom feeds.


## Background

I wanted to have a blog and I wanted it to use static pages. That&#39;s why I wrote it. There are some features &#8212; like the inclusion of custon JavaScript and CSS files &#8212; I needed for [my own blog](https://www.krajzewicz.de/blog/index.php).


## Usage

Write your blog entries as HTML contents/snippets (may be extended to .md etc. in the future) with some additional meta information, e.g. &#8216;entry1.txt&#8217;:

```
state:release
title:My first blog entry
filename:my-first-blog-entry
author:Daniel Krajzewicz
date:26.12.2024 19:25
topics:blog,example
abstract:A very first introduction into blogging
content:
<b>Hello there!</b><br/>
This is my very first blog post!
===
```

All information starts with a key that is separated from the value by a &#8216;:&#8217;. Multi-line values start with a blank line after the key and are closed with &#8216;===&#8217;. More information about the format of the entries is given on the [&#39;Entry Definition&#39; page](./docs/use_entries.md).

Then run __gresiblos__ on it:

```console
python src\gresiblos.py entry1.txt
```

&#8230; and it will convert it into a complete HTML page using the default template stored in ```./data/```. The command line options and the usage is described on the [&#39;Running on the Command Line&#39; page](./docs/use_cmd.md).



## License

__gresiblos__ is licensed under the [GPLv3 license](license.md).



## Installing gresiblos

The __current version__ is [gresiblos-0.4.0](https://github.com/dkrajzew/gresiblos/releases/tag/0.4.0).

You may __install gresiblos__ using

```console
python -m pip install gresiblos
```

You may __download a copy or fork the code__ at [gresiblos&apos;s github page](https://github.com/dkrajzew/gresiblos).

Besides, you may __download the current release__ here:

* [gresiblos-0.4.0.zip](https://github.com/dkrajzew/gresiblos/archive/refs/tags/0.4.0.zip)
* [gresiblos-0.4.0.tar.gz](https://github.com/dkrajzew/gresiblos/archive/refs/tags/0.4.0.tar.gz)



## Further Documentation

* A complete documentation is located at <https://gresiblos.readthedocs.io/en/latest/>
* Discussions are open at <https://github.com/dkrajzew/gresiblos/discussions>
* The github repository is located at: <https://github.com/dkrajzew/gresiblos>
* The issue tracker is located at: <https://github.com/dkrajzew/gresiblos/issues>
* The PyPI page is located at: <https://pypi.org/project/gresiblos/>



## Status

__gresiblos__ works as intended for me, but lacks quite some features of enterprise systems.

I may extend it in the future, but that mainly depends on my motivation and your interaction with me.


## ChangeLog

### gresiblos-0.4.0 (to come)

* support for entry index (using json and php)
  * generates a json-file with entries
  * added a php-file which lists entries or topics

### gresiblos-0.2.0 (27.12.2024)

* Initial version
  * processes entries and saves them




