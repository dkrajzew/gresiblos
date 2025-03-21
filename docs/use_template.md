# Template definition

## Basics

The template is a plain HTML file. Set up as you like it.

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



## Default values

Parts of the template with replacements defined using __\[\[:*&lt;FIELD_NAME&gt;*:\]\]__ with no value in their data for ***&lt;FIELD_NAME&gt;*** will be replaced by an empty string (will be removed). In the example above, **\[\[:includes:\]\]** is such a case.

But you may define defaults for the values using the format __\[\[:*&lt;FIELD_NAME&gt;*|*&lt;DEFAULT&gt;*:\]\]__. In this case, this part will be replaced by the according value from the blog entry data if ***&lt;FIELD_NAME&gt;*** is set. Otherwise, ***&lt;DEFAULT&gt;*** will be inserted. In the example above, **\[\[:author2|Daniel Krajzewicz:\]\]** is such a case, as **author2** is not set.



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

will - in the case ___topics___ is not within the meta information - become

```html
...
<div><p><b>Abstract:</b> A very first introduction into blogging</p></div>

<div id="blogCopy">&copy; Copyright Daniel Krajzewicz, 26.12.2024 19:25</div>
...
```



