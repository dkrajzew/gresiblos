# Entry definition

Each blog entry is stored in a single text file with an arbotrary extension. An entry consists of key/value pairs. The key and the value are written into a single line, divided by a ':'.

Multi-line values start with a blank line after the key and are closed with '==='.

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
