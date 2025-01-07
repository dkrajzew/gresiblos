# Entry Definition

## Basics

Each blog entry is stored in a single text file with an arbitrary extension. An entry consists of key/value pairs. The key and the value are written into a single line, divided by a &#8216;:&#8217;.

Multi-line values start with a new line after the key and the &#8216;:&#8217; and are closed with &#8216;===&#8217;.

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

Please note that the content is kept as-is in the current version.


## Meta Information

The choice of the key/value pairs mainly depends on your template and what is used in here.

Some information is though mandatory:

* **filename** (without the extension)

... and well, yes, you should have some content :-)

As soon as you plan to use the supported files ```index.php``` and ```feed.php```, you must include the following meta information in your entries:

* **date**: The publishing date
* **title**: The title of the blog post
* **topics**: The topics of the blog post
* **abstract**: A short description of the post or a short introduction (should be probably one sentence or a small paragraph long)
* **filename**: The filename of the blog post (without the extension)


## Further Fields

I personally use some additional fields, e.g. ```includes``` and ```js_inits``` which are then included at the proper place in the template so that I can use custom JavaScript-scripts in a page, see, e.g., [my Moirée test](https://www.krajzewicz.de/blog/moiree-test1.php). 




