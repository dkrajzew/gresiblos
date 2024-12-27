[![License: GPL](https://img.shields.io/badge/License-GPL-green.svg)](https://github.com/dkrajzew/degrotesque/blob/master/LICENSE)
[![PyPI version](https://badge.fury.io/py/gresiblos.svg)](https://pypi.python.org/pypi/gresiblos)
![test](https://github.com/dkrajzew/gresiblos/actions/workflows/test.yml/badge.svg)
[![Downloads](https://pepy.tech/badge/gresiblos)](https://pepy.tech/project/gresiblos)
[![Downloads](https://static.pepy.tech/badge/gresiblos/week)](https://pepy.tech/project/gresiblos)
[![Coverage Status](https://coveralls.io/repos/github/dkrajzew/gresiblos/badge.svg?branch=main)](https://coveralls.io/github/dkrajzew/gresiblos?branch=main)
[![Documentation Status](https://readthedocs.org/projects/gresiblos/badge/?version=latest)](https://gresiblos.readthedocs.io/en/latest/?badge=latest)
[![Dependecies](https://img.shields.io/badge/dependencies-none-green)](https://img.shields.io/badge/dependencies-none-green)


[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=GVQQWZKB6FDES)


Introduction
------------

__gresiblos__ is the acronym for __*gre*yrat's *si*mple *blo*g *s*ystem__. It is a simple blogging system written in [Python](https://www.python.org/) that generates static HTML pages from blog content definitions.

In the current stage (v0.2.0), __gresiblos__ reads a file with blog entry contents and meta information and embeds it into a template.


Background
----------

I wanted to have a blog and I wanted it to use static pages. That's why I wrote it.


Usage
-----

Write your blog entries as HTML contents/snippets (may be extended to .md etc. in the future) with some additional meta information, e.g. 'entry1.txt':

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

All information starts with a key that is separated from the value by a ':'. Multi-line values start with a blank line after the key and are closed with '==='.

Then run __gresiblos__ on it:

```shell
python src\gresiblos.py entry1.txt
```

... and it will convert it into a complete HTML page using the default template stored in ```./data/```.



License
-------

__gresiblos__ is licensed under the [BSD license](license.md).


Status
------

__gresiblos__ works as intended for me, but lacks quite some features of enterprise systems.

I may extend it in the future, but that mainly depends on my motivation and your interaction with me.

Ideas for extensions are:

* support different input formats
* support listing entries by date and topic
* support searching in entries
