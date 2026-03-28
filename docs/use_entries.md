# Usage - Entries

Up to now, we processed plain text files. Yet, you may want to format your entries and/or give them some styling. As well, a blog may have different authors, the date may be wanted to be fixed, the title may be more complex than the file name, etc. In the following, some possibilities for enriching your entries are given.

## Markdown

You may use markdown to format your files. For applying markdown use the __--markdown__ option:

```shell
> gresiblos --markdown blog/*.txt
```

The contents of the files will be converted from markdown to HTML first, and then embedded into the template. Markdown will be applied on the __title__, the __abstract__ and the __contents__ parts of your entries (see also below).

Please note that the __markdown__ module is not part of the standard installation. You have to install it by yourself, see [markdown installation](./install.md#installing-markdown).


## Plain HTML

You may as well write your entries in plain HTML - I use HTML with additional meta information.

No options have to be set, the entries' HTML contents are simply embedded into the template. Please note that your entries should contain only the content - no header / body tags...


## Meta information

You may add meta information to your files. __gresiblos__ assumes that your files have meta information embedded if the first line contains a &lsquo;:&rsquo;.

### Defining meta information

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

So a complete blog entry with meta information may look like this:

```
state:release
title:My first blog entry
filename:my-first-blog-entry
author:Daniel Krajzewicz
date:2024-01-02 19:25:00
topics:blog,example
abstract:A very first introduction into blogging
content:
<b>Hello there!</b><br/>
This is my very first blog post!
===
```


### Automatically derived meta information

Some meta information will be derived from the given entries if you do not define them. This includes:

* **filename**: If not given as meta information, the filename of the original entry is kept (without the extension); please note that Python&apos;s ```urllib.parse.quote``` method is applied to obtain a URL-valid name;
* **date**: The entry file&apos;s modification date is used if no explicit meta information about the creation date is given;
* **title**: The entry file name is used as title if no meta information about the title is given.


### Choosing meta information

You may include any meta information you like. The choice of the key/value pairs mainly depends on your [template](./use_templates.md) and what is used in here.

As soon as you plan to use the supported ```index.php``` file, you must include the following meta information in your entries:

* **date**: The publishing date; assumed to be in ISO-format (e.g. ```2025-01-08 19:26:00```), but this may be adapted using the option __--date-format *&lt;DATE_FORMAT&gt;*__. I am using the German date format (```08.01.2025 19:26:00```) in my blog;
* **title**: The title of the blog post;
* **filename**: The filename of the blog post (**without the path and the extension**).

It does make sense to add the following meta information:

* **topics**: The topics of the blog post (a list of topics, divided by &lsquo;,&rsquo;);
* **abstract**: A short description of the post or a short introduction (should be probably one sentence or a small paragraph long).


### Further meta information

I personally use some additional fields, e.g. ```includes``` and ```js_inits``` which are then included at the proper place in the template so that I can use custom JavaScript-scripts in a page, see, e.g., [my Moirée test](https://www.krajzewicz.de/blog/moiree-test1.php).

