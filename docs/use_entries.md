# Entry Definition

## Basics

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

## Meta Information

The choice of the key/value pairs mainly depends on your template and what is used in here.

Some information is though mandatory:

* **filename**

Some meta information is used by the php file that reads the generated json-file with all entries' meta information and should be thereby included. The according keys are:

* **title**
* **filename**
* **topics**
* **date**
* **abstract**

I personally use some further key/value pairs, as visible in the [example template](./use_template.md):

* **copyright_date**
* **author**



