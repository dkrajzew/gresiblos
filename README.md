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


## Background

I wanted to have a blog and I wanted it to use static pages. That&#39;s why I wrote it. __gresiblos__ has some additional features &#8212; like the inclusion of custom JavaScript and CSS files &#8212; I needed for [my own blog](https://www.krajzewicz.de/blog/index.php).


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

## License

__gresiblos__ is licensed under the [BSD license](license.md).



## Installing gresiblos

The __current version__ is [gresiblos-0.4.2](https://github.com/dkrajzew/gresiblos/releases/tag/0.4.2).

You may __install gresiblos__ using

```console
python -m pip install gresiblos
```

You may __download a copy or fork the code__ at [gresiblos&apos;s github page](https://github.com/dkrajzew/gresiblos).

Besides, you may __download the current release__ here:

* [gresiblos-0.4.2.zip](https://github.com/dkrajzew/gresiblos/archive/refs/tags/0.4.2.zip)
* [gresiblos-0.4.2.tar.gz](https://github.com/dkrajzew/gresiblos/archive/refs/tags/0.4.2.tar.gz)



## Further Documentation

* A complete documentation is located at <https://gresiblos.readthedocs.io/en/latest/>
* Discussions are open at <https://github.com/dkrajzew/gresiblos/discussions>
* The github repository is located at: <https://github.com/dkrajzew/gresiblos>
* The issue tracker is located at: <https://github.com/dkrajzew/gresiblos/issues>
* The PyPI page is located at: <https://pypi.org/project/gresiblos/>



## Status

__gresiblos__ works as intended for me, but lacks quite some features of enterprise systems.

The next steps to release 1.0 will involve some refactorings, including API changes.

Please let me know if you have any idea / feature request / question / whatever or contribute to __gresiblos__...



## Examples

__gresiblos__ is used at the following pages:

* <https://www.krajzewicz.de/blog/index.php>: my own blog



## ChangeLog

## gresiblos-0.6.0 (to come)
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



## Older versions

You may find the complete change log at [the gresiblos documentation pages](https://gresiblos.readthedocs.io/en/latest/).



## Closing

Well, have fun. If you have any comments / ideas / issues, please submit them to [gresiblos' issue tracker](https://github.com/dkrajzew/gresiblos/issues) on github or drop me a mail.

Don't forget to spend a star!


