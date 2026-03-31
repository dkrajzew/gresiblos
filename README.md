# gresiblos

[![License: GPL-3.0](https://img.shields.io/badge/License-GPL-green.svg)](https://github.com/dkrajzew/gresiblos/blob/main/LICENSE)
[![PyPI version](https://badge.fury.io/py/gresiblos.svg)](https://pypi.org/project/gresiblos/)
![test](https://github.com/dkrajzew/gresiblos/actions/workflows/test.yml/badge.svg)
[![Downloads](https://static.pepy.tech/badge/gresiblos)](https://pepy.tech/projects/gresiblos)
[![Downloads](https://static.pepy.tech/badge/gresiblos/week)](https://pepy.tech/projects/gresiblos)
[![Coverage Status](https://coveralls.io/repos/github/dkrajzew/gresiblos/badge.svg?branch=main)](https://coveralls.io/github/dkrajzew/gresiblos?branch=main)
[![Documentation Status](https://readthedocs.org/projects/gresiblos/badge/?version=latest)](https://gresiblos.readthedocs.io/en/latest/?badge=latest)
[![Dependecies](https://img.shields.io/badge/dependencies-none-green)](#)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=GVQQWZKB6FDES)

#

__gresiblos__ &#8212; a simple private blogging system.

## Introduction

__gresiblos__ is a radically simple static site generator / blogging system written in [Python](https://www.python.org/). It generates static HTML pages from text or markdown files, or HTML contents. It has no dependencies and no server backend is needed. __gresiblos__ is the acronym for __<u>gre</u>yrat&#39;s <u>si</u>mple <u>blo</u>g <u>s</u>ystem__.

__gresiblos__ reads blog entries from files that may include some meta information and embeds their contents into a template. Optionally, it additionally generates: a) a JSON-file with meta information about the entries, b) lists of the entries sorted alphabetically or chronologically, c) RSS 2.0 and Atom feed files. __gresiblos__ comes with a basic php-file that realizes browsing by topic and/or entries.


## Usage

__gresiblos__ is started on the command line. Write your blog entries as text, markdown, or HTML.

Assuming they are stored in the &#8216;blog&#8217; folder, run __gresiblos__ on them like:

```shell
gresiblos ./blog/*.txt
```

&#8230; and it will convert them into complete HTML pages using a default template and store them into the folder &#8216;gresiblos_out&#8217;.

You may as well add some meta data, storing the blog entry contents under the ```contents``` key:

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

All information starts with a key that is separated from the value by a &#8216;:&#8217;. Multi-line values start with a new line after the key and the &#8216;:&#8217; and are closed with &#8216;===&#8217;. Please note that the content is kept as-is in the current version.

Again, when starting gresiblos, the meta information and the contents will be stored at marked places within the template.

__gresiblos__ templates support placeholders that be filled by meta information, as well as optional fields.

You may find further information at [the gresiblos documentation pages](https://gresiblos.readthedocs.io/en/latest/).


## Documentation

__gresiblos__ is meant to be run on the command line. The documentation consists of a [user manual](https://gresiblos.readthedocs.io/en/latest/usage.html) and a [man-page like call documentation](https://gresiblos.readthedocs.io/en/latest/cmd.html) (yet incomplete).

If you want to contribute, you may check the [API documentation](https://gresiblos.readthedocs.io/en/latest/api_gresiblos.html) or visit [gresiblos on github](https://github.com/dkrajzew/gresiblos) where besides the code you may find the [gresiblos issue tracker](https://github.com/dkrajzew/gresiblos/issues) or a [discussions about gresiblos section](https://github.com/dkrajzew/gresiblos/discussions).

Additional documentation includes a page with relevant [links](https://gresiblos.readthedocs.io/en/latest/links.html) or the [ChangeLog](https://gresiblos.readthedocs.io/en/latest/changes.html). You may find the complete documentation at the [gresiblos readthedocs pages](https://gresiblos.readthedocs.io/).



## License

__gresiblos__ is licensed under the [GPL-3.0 license](license.md).


## Installation

The current version is 0.10.0. You may install the latest release using pip:

```console
python -m pip install gresiblos
```

Or download the [latest release](https://github.com/dkrajzew/gresiblos/releases/tag/0.10.0) from github. You may as well clone or download the [gresiblos git repository](https://github.com/dkrajzew/gresiblos.git). There is also a page about [installing gresiblos](https://gresiblos.readthedocs.io/en/latest/install.html) which lists further options.


## Background

I wanted to have a blog and I wanted it to use static pages. That&#39;s why I wrote __gresiblos__. It has some specific features &#8212; like the inclusion of custom JavaScript and CSS files &#8212; I needed for [my own blog](https://www.krajzewicz.de/blog/index.php).



## Status &amp; Contributing

__gresiblos__ works as intended for me, but lacks quite some features of enterprise systems.

Please let me know if you have any idea / feature request / question / whatever or contribute to __gresiblos__ by [adding an issue](https://github.com/dkrajzew/gresiblos/issues) or by dropping me a mail.



## Examples

__gresiblos__ is used at the following pages:

* <https://www.krajzewicz.de/blog/index.php>: my own blog



## Changes

## gresiblos-0.10.0 (to come)

* changed the license from BSD to GPL-3.0


### gresiblos-0.8.0 (05.07.2025)

* improved installation (can be now included as a module and executed on the command line after being installed with pip
* the default template is now included in the package
* some linting
* corrected documentation


### Older versions

You may find the complete change log at [the gresiblos documentation pages](https://gresiblos.readthedocs.io/en/latest/).


## Background

I wanted to have a blog and I wanted it to use static pages. That&#39;s why I wrote it. __gresiblos__ has some additional features &#8212; like the inclusion of custom JavaScript and CSS files &#8212; I needed for [my own blog](https://www.krajzewicz.de/blog/index.php).


## Closing

Well, have fun. If you have any comments / ideas / issues, please submit them to [gresiblos&apos; issue tracker](https://github.com/dkrajzew/gresiblos/issues) on github or drop me a mail.

Don&apos;t forget to spend a star!


