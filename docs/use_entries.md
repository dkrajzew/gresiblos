# Entry Definition

## Basics

Well, basically, you may feed __gresiblos__ with plain text files.

You may as well give it markdown files setting the option __--markdown__.

Or you have pre-formatted HTML files. They also can be used to build your blog / static side pages.

In any case, the contents of these files will be embedded into the [template](use_template.md) at the place denoted with the tag __[[:content:]]__.

Some meta information is derived automatically, if not given. See section [Automatically derived meta information](use_entries.md#automatically-derived-meta-information) below.


## Meta information

Additional meta data can be given in each entry in form of key/value pairs. __gresiblos__ recognizes the existence of meta data when the first line contains a &#8216;:&#8217;. Each key/value pair is  written into a single line, divided by a &#8216;:&#8217;. Multi-line values start with a new line after the key and the &#8216;:&#8217; and are closed with &#8216;===&#8217;.

Meta data enrich the appearence of a blog entry and can be used for sorting the entries.

An example looks like:

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

Again, the content may be plain text, markdown, or HTML.


### Automatically derived meta information

Some meta information is derived from the given entries and does not have to be explicitly given - though it may make sense to define it explicitely.

This information includes:

* **filename**: If not given as meta information, the filename of the original entry is kept (without the extension); please note that Python's urllib.parse.quote method is applied to obtain a URL-valid name
* **date**: The entry file's modification date is used if no explicit meta information about the creaion date is given
* **title**: The entry file name is used as title if no meta information about the title is given


### Standard meta information

The choice of the key/value pairs mainly depends on your template and what is used in here.

As soon as you plan to use the supported files ```index.php``` and ```feed.php```, you must include the following meta information in your entries:

* **date**: The publishing date; assumed to be in ISO-format (e.g. ```2025-01-08 19:26:00```), but may be adapted using the option __--date-format *&lt;DATE_FORMAT&gt;*__
* **title**: The title of the blog post
* **filename**: The filename of the blog post (without the path and the extension)

It does make sense to add the following meta information:

* **topics**: The topics of the blog post (a list of topics, divided by ',')
* **abstract**: A short description of the post or a short introduction (should be probably one sentence or a small paragraph long)


### Further Fields

I personally use some additional fields, e.g. ```includes``` and ```js_inits``` which are then included at the proper place in the template so that I can use custom JavaScript-scripts in a page, see, e.g., [my Moirée test](https://www.krajzewicz.de/blog/moiree-test1.php).




