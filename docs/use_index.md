# Entry Index

When run, __gresiblos__ builds a json file with some meta information about the processed entries. This file can be used for building a page that lists the entries, the topics, or other information, e.g. entries that address a specific topic. The file is saved into the same folder as the generated pages (option **--destination *&lt;PATH&gt;*** / **-d *&lt;PATH&gt;***).

## Index Contents

Currently, the index contains the following information about each entry:

* **date**: The publishing date
* **title**: The title of the blog post
* **topics**: The topics of the blog post
* **abstract**: A short description of the post or a short introduction (should be probably one sentence or a small paragraph long)
* **filename**: The filename of the blog post (without the extension)

All values are strings despite the topics, which are a list of strings for each blog entry.

Please note that this information must be given in each entry&#39;s meta-data.


## php Index Browser

A very simple (and probably very naive) php page for listing entries, topics, an topic entries is included and can be found at  [***&lt;GRESIBLOS&gt;*/tools/index.php**](https://github.com/dkrajzew/gresiblos/tree/main/tools/index.php).

## php RSS/Atom Feed Generator

A script that generates an RSS or an Atom feed using the index is given included and can be found at [***&lt;GRESIBLOS&gt;*/tools/feed.php**](https://github.com/dkrajzew/gresiblos/tree/main/tools/feed.php).

