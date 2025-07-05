# gresiblos

[![License: BSD](https://img.shields.io/badge/License-BSD-green.svg)](https://github.com/dkrajzew/gresiblos/blob/master/LICENSE)
[![PyPI version](https://badge.fury.io/py/gresiblos.svg)](https://pypi.python.org/pypi/gresiblos)
![test](https://github.com/dkrajzew/gresiblos/actions/workflows/test.yml/badge.svg)
[![Downloads](https://pepy.tech/badge/gresiblos)](https://pepy.tech/project/gresiblos)
[![Downloads](https://static.pepy.tech/badge/gresiblos/week)](https://pepy.tech/project/gresiblos)
[![Coverage Status](https://coveralls.io/repos/github/dkrajzew/gresiblos/badge.svg?branch=main)](https://coveralls.io/github/dkrajzew/gresiblos?branch=main)
[![Documentation Status](https://readthedocs.org/projects/gresiblos/badge/?version=latest)](https://gresiblos.readthedocs.io/en/latest/?badge=latest)
[![Dependecies](https://img.shields.io/badge/dependencies-none-green)](https://img.shields.io/badge/dependencies-none-green)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=GVQQWZKB6FDES)


## Introduction

__gresiblos__ is a simple blogging system written in [Python](https://www.python.org/).  __gresiblos__ generates static HTML pages from optionally annotated text, markdown, or HTML files. __gresiblos__ is the acronym for __*gre*yrat&#39;s *si*mple *blo*g *s*ystem__.

__gresiblos__ reads blog entries from files that may include some meta information and embeds the contents into a template. Optionally, in addition, it generates a json-file with meta information about the entries. __gresiblos__ comes with a php-file that realises browsing, as well as with a php-file that generates rss and atom feeds.


## Usage

Write your blog entries as text, markdown or HTML.

Then run __gresiblos__ on it:

```shell
python src\gresiblos.py entry1.txt
```

&#8230; and it will convert it into a complete HTML page using the default template stored in ```./data/```.

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

If you want to contribute, you may check the [API documentation](https://gresiblos.readthedocs.io/en/latest/api_gresiblos.html) or visit [gresiblos on github](https://github.com/dkrajzew/gresiblos) where besides the code you may find the [gresiblos issue tracker](https://github.com/dkrajzew/gresiblos/issues) or [discussions about gresiblos](https://github.com/dkrajzew/gresiblos/discussions).

Additional documentation includes a page with relevant [links](https://gresiblos.readthedocs.io/en/latest/links.html) or the [ChangeLog](https://gresiblos.readthedocs.io/en/latest/changes.html).



## License

__gresiblos__ is licensed under the [BSD license](license.md).


## Installation

The __current version__ is [gresiblos-0.8.0](https://github.com/dkrajzew/gresiblos/releases/tag/0.8.0).

You may __install gresiblos__ using

```console
python -m pip install gresiblos
```

Or download the [latest release](https://github.com/dkrajzew/gresiblos/releases/tag/0.8.0) from github. You may as well clone or download the [gresiblos git repository](https://github.com/dkrajzew/gresiblos.git). There is also a page about [installing gresiblos](https://gresiblos.readthedocs.io/en/latest/install.html) which lists further options.


## Status

__gresiblos__ works as intended for me, but lacks quite some features of enterprise systems.

The next steps to release 1.0 will involve some refactorings, including API changes.

Please let me know if you have any idea / feature request / question / whatever or contribute to __gresiblos__&hellip;



## Examples

__gresiblos__ is used at the following pages:

* <https://www.krajzewicz.de/blog/index.php>: my own blog



## Changes

### gresiblos-0.8.0 (05.07.2025)
* improved installation (can be now included as a module and executed on the command line after being installed with pip
* the default template is now included in the package
* some linting
* corrected documentation

### gresiblos-0.6.0 (30.03.2025)
* improving the documentation
* changed the license from GPLv3 to BSD
* changes:
    * **important**: the replacement pattern for values within the template changed from __%*&lt;FIELD_NAME&gt;*%__ to __\[\[:*&lt;FIELD_NAME&gt;*:\]\]__
    * topics are stored as list in the index file
    * the filenames in the index now include the extension
    * the **state** attribute was removed from the index file
    * replaced option **--have-php-index** by the option **--topic-format *&lt;FORMAT&gt;*** which directly defines how each of a blog entries topics shall be rendered when embedding it into the template
    * removed options **--default-author *&lt;NAME&gt;***, **--default-copyright-date *&lt;DATE&gt;***, **--default-state *&lt;STATE&gt;*** and introduced replacements with defaults instead
* new
    * the indentation level of the index file can now be set using the option **--index-indent *&lt;INT&gt;***
    * you may use a different format for the date in your entries than the ISO-format by defining it using **--date-format *&lt;DATE_FORMAT&gt;***
    * added the possibility to skip document parts using the begin/end tags __\[\[:?*&lt;FIELD_NAME&gt;*:\]\]__ and __\[\[:*&lt;FIELD_NAME&gt;*?:\]\]__ if __*&lt;FIELD_NAME&gt;*__ is not set

### Older versions

You may find the complete change log at [the gresiblos documentation pages](https://gresiblos.readthedocs.io/en/latest/).


## Background

I wanted to have a blog and I wanted it to use static pages. That&#39;s why I wrote it. __gresiblos__ has some additional features &#8212; like the inclusion of custom JavaScript and CSS files &#8212; I needed for [my own blog](https://www.krajzewicz.de/blog/index.php).


## Closing

Well, have fun. If you have any comments / ideas / issues, please submit them to [gresiblos&apos; issue tracker](https://github.com/dkrajzew/gresiblos/issues) on github or drop me a mail.

Don&apos;t forget to spend a star!


