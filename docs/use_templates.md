# Usage - Templates

The template is a HTML file with placeholders. Set up as you like it. Let __gresiblos__ use your template using the __--template *&lt;TEMPLATE_FILE&gt;*__ (or __-t *&lt;TEMPLATE_FILE&gt;*__ for short) option where __*&lt;TEMPLATE_FILE&gt;*__ is the path to your template.

The [entry&#39;s meta data](./use_entries.md#meta-information) will be inserted into the file at places marked by **\[\[:*&lt;FIELD_NAME&gt;*:\]\]**.

So given the entry:

```
state:release
title:My first blog entry
filename:my-first-blog-entry
author:John Doe
date:2025-01-02 19:25:00
topics:blog,example
abstract:A very first introduction into blogging
content:
<b>Hello there!</b><br/>
This is my very first blog post!
===
```

and the template:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>[[:title:]] &mdash; A sample blog</title>
</head>
<body>
    <header>
        <h1>[[:title:]]</h1>[[:?date:]]
        <p class="date">Published on [[:date:]]</p>[[:date?:]]
    </header>

    <!-- Optional topics section -->
[[:?topics:]]<div class="topics">Topics: [[:topics:]]</div>[[:topics?:]]
    <!-- Optional abstract section -->
[[:?abstract:]]<div class="abstract">[[:abstract:]]</div>[[:abstract?:]]

    <!-- Main content -->
    <article>
[[:content:]]
    </article>
    <div id="footer">&copy; Copyright [[:author2|John Doe:]]</div>
</body>
</html>
```

you will get

```html
<!DOCTYPE html>
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>My first blog entry &mdash; A sample blog</title>
</head>
<body>
    <header>
        <h1>My first blog entry</h1>
        <p class="date">Published on <DATE1></p>
    </header>

    <!-- Optional topics section -->
<div class="topics">Topics: blog, example</div>
    <!-- Optional abstract section -->
<div class="abstract">A very first introduction into blogging</div>

    <!-- Main content -->
    <article>
<b>Hello there!</b><br/>
This is my very first blog post!

    </article>
    <div id="footer">&copy; Copyright John Doe</div>
</body>
</html>
```


## Default values

Replacements defined using __\[\[:*&lt;FIELD_NAME&gt;*:\]\]__ with no value in their meta data for ***&lt;FIELD_NAME&gt;*** will be replaced by an empty string (will be removed). In the example above, **\[\[:includes:\]\]** is such a case.

You though may define defaults for the values using the format __\[\[:*&lt;FIELD_NAME&gt;*|*&lt;DEFAULT&gt;*:\]\]__. In this case, this part will be replaced by the value from the blog entry data if the meta data ***&lt;FIELD_NAME&gt;*** is set. Otherwise, ***&lt;DEFAULT&gt;*** will be inserted. In the example above, **\[\[:author2|Daniel Krajzewicz:\]\]** is such a case, as **author2** is not given in the meta data.



## Optional parts

In some cases, it is not sufficient to use defaults. If, e.g., no topics are given, it would not make sense to have a default:

```html
...
<div class="topics">Topics: </div>
...
```

__gresiblos__ allows to tag parts of the document if a certain meta data is not given. The begin of the optional document part is marked using __\[\[:?*&lt;FIELD_NAME&gt;*:\]\]__, the end using __\[\[:*&lt;FIELD_NAME&gt;*?:\]\]__. The contents between those markers are removed if __&lt;FIELD_NAME&gt;__ is not given in the meta information. So

```html
...
    <!-- Optional topics section -->
[[:?topics:]]<div class="topics">Topics: [[:topics:]]</div>[[:topics?:]]
    <!-- Optional abstract section -->
[[:?abstract:]]<div class="abstract">[[:abstract:]]</div>[[:abstract?:]]
...
```

will &mdash; in the case ___topics___ is not given within the meta information &mdash; become

```html
...
    <!-- Optional topics section -->

    <!-- Optional abstract section -->
[[:?abstract:]]<div class="abstract">[[:abstract:]]</div>[[:abstract?:]]
...
```

This means that the part enclosed in **\[\[:?topics:\]\]** and **\[\[:topics?:\]\]** is removed if the meta information ___topics___ is not defined.

