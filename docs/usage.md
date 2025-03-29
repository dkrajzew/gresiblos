# Usage

## Basics

Assume you would have diverse text files with notes stored in a folder named &ldquo;blog&rdquo;. You can use __gresiblos__ to turn them into browseable set of HTML pages with the following call:

```shell
> gresiblos blog/*.txt
```

The contents of the text files will be embedded into the default template and written to the destination folder **./gresiblos_out**.

The generated files will be named as your text files, though Python&apos;s ```urllib.parse.quote``` is applied to encode characters that are not compliant for being the part of an URL. Some further information is extracted from the files: the __date__ using the file&apos;s change date, and the __title__ using the file&apos;s file name.

In the following, you will find some information about how the entries and the template can be enriched for obtaining full-fledged blog pages.


## Entries

Up to now, we processed plain text files. But a blog may have different authors, the date may be wanted to be fixed, the title may be more complex than the file name, etc. In the following, some possibilities for enriching files are given, realising a real blog.

### Markdown

You may use markdown to format your files. For applying markdown use the __--markdown__ option:

```shell
> gresiblos --markdown blog/*.txt
```

The contents of the files will be converted from markdown to HTML first, and then embedded into the template. Markdown will be applied on the __title__, the __abstract__ (see below) and the __contents__.

Please note that the __markdown__ module is not part of the standard installation. You have to install it by yourself, see [markdown installation](./install.md#installing-markdown).

### Meta information

You may add meta information to your files. __gresiblos__ recognises / assumes that your files have meta information embedded if the first line contains a &lsquo;:&rsquo;.

#### Defining meta information

Meta information is stored in the files to process. Each meta information is stored as a key/value pair, separated by a &lsquo;:&rsquo;, e.g.:

```
author: Daniel Krajzewicz
date: 2025-03-23
```

You may as well include multi-line fields. In this case, the key is stored in one line and the line is closed with a &lsquo;:&rsquo;. The following lines are interpreted as the respective value until a line that contains &ldquo;===&rdquo; only occurs:

```
references:
[1] my first reference
[2] my second reference
===
```

__Please note that the content itself has to be named in the same way when using meta data:__

```
content:
This is my first blog entry. I am so excited!
===
```

#### Automatically derived meta information

Some meta information will be derived from the given entries if you do not define it. This includes:

* **filename**: If not given as meta information, the filename of the original entry is kept (without the extension); please note that Python&apos;s ```urllib.parse.quote``` method is applied to obtain a URL-valid name
* **date**: The entry file&apos;s modification date is used if no explicit meta information about the creation date is given
* **title**: The entry file name is used as title if no meta information about the title is given


#### Choosing meta information

You may include any meta information you like. The choice of the key/value pairs mainly depends on your template and what is used in here.

As soon as you plan to use the supported files ```index.php``` and ```feed.php```, you must include the following meta information in your entries:

* **date**: The publishing date; assumed to be in ISO-format (e.g. ```2025-01-08 19:26:00```), but may be adapted using the option __--date-format *&lt;DATE_FORMAT&gt;*__
* **title**: The title of the blog post
* **filename**: The filename of the blog post (without the path and the extension)

It does make sense to add the following meta information:

* **topics**: The topics of the blog post (a list of topics, divided by &lsquo;,&rsquo;)
* **abstract**: A short description of the post or a short introduction (should be probably one sentence or a small paragraph long)



#### Further meta information

I personally use some additional fields, e.g. ```includes``` and ```js_inits``` which are then included at the proper place in the template so that I can use custom JavaScript-scripts in a page, see, e.g., [my Moirée test](https://www.krajzewicz.de/blog/moiree-test1.php).



### Further options for entries

I personally code my contents in HTML directly, allowing me to use everything HTML supports.




## Own templates

### Basics

The template is a plain HTML file. Set up as you like it. Let __gresiblos__ use your template using the __--template *&lt;TEMPLATE_FILE&gt;*__ (or __-t *&lt;TEMPLATE_FILE&gt;*__ for short) option

The entry&#39;s meta data will be inserted into the file at places marked by **\[\[:*&lt;FIELD_NAME&gt;*:\]\]**.

So given the entry:

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

and the template:

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
 <head><title>[[:title:]] &mdash; A sample blog</title>
[[:includes:]]
 </head>

 <body>
  <div id="title">My new blog</div>
<h1>[[:title:]]</h1>
<div><p><b>Abstract:</b> [[:abstract:]]</p></div>
<div><p><b>Topics:</b> [[:topics:]]</p></div>
<div id="blogCopy">&copy; Copyright [[:author:]], [[:date:]]</div>
[[:content:]]
<div id="footer">&copy; Copyright [[:author2|Daniel Krajzewicz:]]</div>
 </body>

</html>
```

you will get

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
 <head><title>My first blog entry &mdash; A sample blog</title>
 </head>

 <body>
  <div id="title">My new blog</div>
<h1>My first blog entry</h1>
<div><p><b>Abstract:</b> A very first introduction into blogging</p></div>
<div><p><b>Topics:</b> blog, example</p></div>
<div id="blogCopy">&copy; Copyright Daniel Krajzewicz, 26.12.2024 19:25</div>
<b>Hello there!</b><br/>
This is my very first blog post!
<div id="footer">&copy; Copyright Daniel Krajzewicz</div>
 </body>

</html>
```



### Default values

Parts of the template with replacements defined using __\[\[:*&lt;FIELD_NAME&gt;*:\]\]__ with no value in their data for ***&lt;FIELD_NAME&gt;*** will be replaced by an empty string (will be removed). In the example above, **\[\[:includes:\]\]** is such a case.

But you may define defaults for the values using the format __\[\[:*&lt;FIELD_NAME&gt;*|*&lt;DEFAULT&gt;*:\]\]__. In this case, this part will be replaced by the according value from the blog entry data if ***&lt;FIELD_NAME&gt;*** is set. Otherwise, ***&lt;DEFAULT&gt;*** will be inserted. In the example above, **\[\[:author2|Daniel Krajzewicz:\]\]** is such a case, as **author2** is not set.



### Optional parts

In some cases, it is not sufficient to use defaults. If, e.g., no topics are given, it would not make sense to have a default:

```html
...
<div><p><b>Topics:</b> </p></div>
...
```

__gresiblos__ allows to tag parts of the document if a certain meta data is not given. The begin of the optional document part is marked using __\[\[:?*&lt;FIELD_NAME&gt;*:\]\]__, the end using __\[\[:*&lt;FIELD_NAME&gt;*?:\]\]__. The contents between those markers are removed if __&lt;FIELD_NAME&gt;__ is not given in the meta information. So

```html
...
<div><p><b>Abstract:</b> [[:abstract:]]</p></div>
[[:?topics:]]<div><p><b>Topics:</b> [[:topics:]]</p></div>[[:topics?:]]
<div id="blogCopy">&copy; Copyright [[:author:]], [[:date:]]</div>
...
```

will &mdash; in the case ___topics___ is not within the meta information &mdash; become

```html
...
<div><p><b>Abstract:</b> A very first introduction into blogging</p></div>

<div id="blogCopy">&copy; Copyright Daniel Krajzewicz, 26.12.2024 19:25</div>
...
```

This means that the part enclosed in **\[\[:?topics:\]\]** and **\[\[:topics?:\]\]** is removed if the meta information ```topics``` is not defined.


## Lists and indices

### Static entry lists

You may additionally generate a list of files using the **--chrono-output *&lt;OUTPUT&gt;*** option:

```shell
> gresiblos --chrono-output list_chrono.html blog/*.txt
```

This will generate a file named **list_chrono.html** that contains a list of entries sorted chronologically. The generated list will be embedded into the template and stored under the given name.

To get a list sorted alphabetically by the title use the option **--alpha-output *&lt;OUTPUT&gt;***: 

```shell
> gresiblos --alpha-output list_chrono.html blog/*.txt
```

### Index file

When run, __gresiblos__ builds optionally a json file with some meta information about the processed entries. This file can be used for building a page that lists the entries, the topics, or other information, e.g. entries that address a specific topic. The index file is generated using the **--index-output *&lt;OUTPUT&gt;*** option:

```shell
> gresiblos --index-output entries.json blog/*.txt
```

#### Index Contents

Currently, the index contains the following information about each entry:

* **date**: The publishing date
* **title**: The title of the blog post
* **topics**: The topics of the blog post
* **abstract**: A short description of the post or a short introduction (should be probably one sentence or a small paragraph long)
* **filename**: The filename of the blog post (without the extension)

All values are strings despite the topics, which are a list of strings for each blog entry.

Please note that this information must be given in each entry&#39;s meta-data.


#### php Index Browser

A very simple (and probably very naive) php page for listing entries, topics, an topic entries is included and can be found at  [***&lt;GRESIBLOS&gt;*/tools/index.php**](https://github.com/dkrajzew/gresiblos/tree/main/tools/index.php).

#### php RSS/Atom Feed Generator

A script that generates an RSS or an Atom feed using the index is given included and can be found at [***&lt;GRESIBLOS&gt;*/tools/feed.php**](https://github.com/dkrajzew/gresiblos/tree/main/tools/feed.php).

