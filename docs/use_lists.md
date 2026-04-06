# Usage &#8212; Lists and Indices

## Static entry lists

You may generate a list of files using the **--chrono-output *&lt;OUTPUT&gt;*** option:

```shell
gresiblos --chrono-output list_chrono.html blog/*.txt
```

This will generate a file named **list_chrono.html** that contains a list of entries sorted in chronological order.

The generated list is be embedded into the template and stored under the given name.

To get a list sorted alphabetically by the title use the option **--alpha-output *&lt;OUTPUT&gt;***: 

```shell
gresiblos --alpha-output list_chrono.html blog/*.txt
```

## Index file

When run, __gresiblos__ optionally builds a JSON file with some meta information about the processed entries. This file can be used for building a page that lists the entries, the topics, or other summaries. The index file is generated using the **--index-output *&lt;OUTPUT&gt;*** option:

```shell
gresiblos --index-output entries.json blog/*.txt
```

### Index Contents

Currently, the index contains the following information about each entry:

* **date**: The publishing date
* **title**: The title of the blog post
* **topics**: The topics of the blog post
* **abstract**: A short description of the post or a short introduction (should be probably one sentence or a small paragraph long)
* **filename**: The filename of the blog post (without the extension)

All values are strings despite the topics, which are a list of strings for each blog entry.

Please note that this information must be given in each entry&#39;s meta-data.


### php Index Browser

A very simple (and probably very naive) php page for listing entries, topics, an topic entries is included and can be found at  [***&lt;GRESIBLOS&gt;*/tools/index.php**](https://github.com/dkrajzew/gresiblos/blob/main/tools/index.php).
