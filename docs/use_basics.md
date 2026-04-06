# Usage &#8212; Basics

## Prerequisites

You may find information about how to install gresiblos at the [Download and Installation](./install.md) page.

__gresiblos__ is implemented in [Python](https://www.python.org/). It is started on the command line.


## Basics

Assume you would have some text files with notes stored in a folder named &ldquo;blog&rdquo;. You can use __gresiblos__ to turn them into a set of HTML pages with the following call:

```shell
gresiblos blog/*.txt --to-html
```

The contents of the text files will be first annotated with some basic HTML tags - links will be embedded in ```<a>```-elements, and each line will be embedded into a paragraph (```<p>```) tag. The result is then embedded into the default template and written to the destination folder **./gresiblos_out**.

The generated files will be named as your text files, though Python&apos;s ```urllib.parse.quote``` is applied to encode characters that are not compliant for being a part of an URL assuming the files will be uploaded to a server. Some further information is extracted from the files: the __date__ using the file&apos;s change date, and the __title__ using the file&apos;s file name.

In case your entries are stored as [markdown](https://python-markdown.github.io/) files, you may install [markdown](https://python-markdown.github.io/) additionally and start __gresiblos__ with the **--markdown** option instead of using **--to-html**.

At subsequent pages, you will find some information about how the [entries](./use_entries.md) and the [template](./use_templates.md) can be enriched for obtaining full-fledged blog pages and about generating [lists and indices](./use_lists.md) or [feeds](./use_feeds.md) to browse your blog.

