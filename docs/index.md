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

__gresiblos__ is a radically simple static site generator / blogging system written in [Python](https://www.python.org/). It generates static HTML pages by embedding the contents of text, markdown, or HTML-snippet files into a template. It has no dependencies and no server backend is needed. __gresiblos__ is the acronym for __<u>gre</u>yrat&#39;s <u>si</u>mple <u>blo</u>g <u>s</u>ystem__.

__gresiblos__ reads blog entries from files that may include some meta information and embeds their contents into a template. It optionally generates: a) a JSON-file with meta information about the entries, b) lists of the entries sorted alphabetically or chronologically, c) RSS 2.0 and Atom feed files. __gresiblos__ comes with a basic php-file that realizes browsing by topic and/or entries.

You may see it&#39;s results here: <https://www.krajzewicz.de/blog/index.php>.


## Installation

The current version is 0.10.0. You may install the latest release using pip:

```console
python -m pip install gresiblos
```

There is a page about [installing gresiblos](install.md) that lists further options.


## Usage

__gresiblos__ is started on the command line. Write your blog [entries](./use_entries.md) as text, markdown, or HTML.

Assuming they are stored in the &#8216;blog&#8217; folder, run __gresiblos__ on them like:

```shell
gresiblos ./blog/*.txt --to-html
```

and it will apply a basic conversion to HTML, embed them into the default [template](./use_templates.md) and store them into the folder &#8216;gresiblos_out&#8217;.

Of course, it makes sense to use markdown or even plain HTML snippets if you want to run a real blog&#8230;

For even more &#8220;complete&#8221; blogs &mdash; including authors, abstracts, release dates, etc. &mdash; the [entries](./use_entries.md) can be enriched by meta information. __gresiblos__ [templates](./use_templates.md) support placeholders that are filled with the meta information given in an [entry](./use_entries.md), as well as optional fields. 


## Documentation

The documentation consists of a [user manual](use_basics.md) and a [man-page like call documentation](man.md).

If you want to contribute, you may check the [API documentation](api_gresiblos.md) or visit [gresiblos on github](https://github.com/dkrajzew/gresiblos) where besides the code you may find the [gresiblos issue tracker](https://github.com/dkrajzew/gresiblos/issues) or a [discussions about gresiblos section](https://github.com/dkrajzew/gresiblos/discussions).

Additional documentation includes a page with relevant [links](links.md) or the [ChangeLog](changes.md). You may find the complete documentation at the [gresiblos readthedocs pages](https://gresiblos.readthedocs.io/).



## License

__gresiblos__ is licensed under the [GPL-3.0 license](license.md).


## Background

I wanted to have a blog and I wanted it to use static pages. That&#39;s why I wrote __gresiblos__. It has some specific features &#8212; like the inclusion of custom JavaScript and CSS files &#8212; I needed for [my own blog](https://www.krajzewicz.de/blog/index.php).



## Status &amp; Contributing

__gresiblos__ works as intended for me, but lacks quite some features of enterprise systems.

Please let me know if you have any idea / feature request / question / whatever or contribute to __gresiblos__ by [adding an issue](https://github.com/dkrajzew/gresiblos/issues) or by dropping me a mail.



