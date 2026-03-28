# Usage - Templates

The template is a HTML file with placeholders. Set up as you like it. Let __gresiblos__ use your template using the __--template *&lt;TEMPLATE_FILE&gt;*__ (or __-t *&lt;TEMPLATE_FILE&gt;*__ for short) option where __*&lt;TEMPLATE_FILE&gt;*__ is the path to your template.

The [entry&#39;s meta data](./use_entries.md#meta-information) will be inserted into the file at places marked by **\[\[:*&lt;FIELD_NAME&gt;*:\]\]**.

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


## Default values

Replacements defined using __\[\[:*&lt;FIELD_NAME&gt;*:\]\]__ with no value in their meta data for ***&lt;FIELD_NAME&gt;*** will be replaced by an empty string (will be removed). In the example above, **\[\[:includes:\]\]** is such a case.

You though may define defaults for the values using the format __\[\[:*&lt;FIELD_NAME&gt;*|*&lt;DEFAULT&gt;*:\]\]__. In this case, this part will be replaced by the value from the blog entry data if the meta data ***&lt;FIELD_NAME&gt;*** is set. Otherwise, ***&lt;DEFAULT&gt;*** will be inserted. In the example above, **\[\[:author2|Daniel Krajzewicz:\]\]** is such a case, as **author2** is not given in the meta data.



## Optional parts

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

will &mdash; in the case ___topics___ is not given within the meta information &mdash; become

```html
...
<div><p><b>Abstract:</b> A very first introduction into blogging</p></div>

<div id="blogCopy">&copy; Copyright Daniel Krajzewicz, 26.12.2024 19:25</div>
...
```

This means that the part enclosed in **\[\[:?topics:\]\]** and **\[\[:topics?:\]\]** is removed if the meta information ___topics___ is not defined.

