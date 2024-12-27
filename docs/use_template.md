# Template definition

## Basics

The template is a plain HTML file, set up as you like it.

The entry's data will be inserted into the file at places marked by **%*&lt;FIELD_NAME&gt;*%**.

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
 <head><title>%title% &mdash; A sample blog</title>
%includes%
 </head>


 <body>
  <div id="title">My new blog</div>

<h1>%title%</h1>
<div><p><b>Abstract:</b> %abstract%</p></div>
<div><p><b>Topics:</b> %topics%</p></div>
<div id="blogCopy">&copy; Copyright %author%, %date%</div>
%content%
<div id="footer">&copy; Copyright %copyright_date% %author%</div>

 </body>
</html>
```

you will get 

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
 <head><title>My first blog entry &mdash; A sample blog</title>
%includes%
 </head>


 <body>
  <div id="title">My new blog</div>

<h1>My first blog entry</h1>
<div><p><b>Abstract:</b> A very first introduction into blogging</p></div>
<div><p><b>Topics:</b> blog, example</p></div>
<div id="blogCopy">&copy; Copyright Daniel Krajzewicz, 26.12.2024 19:25</div>
<b>Hello there!</b><br/>
This is my very first blog post!
<div id="footer">&copy; Copyright %copyright_date% Daniel Krajzewicz</div>

 </body>
</html>
```