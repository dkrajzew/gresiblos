# Usage - Feeds

__gresiblos__ can generate __Atom__ and __RSS 2.0__ feeds listing the read entries.

An __Atom__ feed is generated using:

```shell
> gresiblos blog/*.txt --atom-output <FILE_NAME>
```

Where __&lt;FILE_NAME&gt;__ is the name of the file the __Atom__ feed will be written to.


An __RSS 2.0__ feed is generated using:

```shell
> gresiblos blog/*.txt --rss-output <FILE_NAME>
```

Where __&lt;FILE_NAME&gt;__ is the name of the file the __RSS 2.0__ feed will be written to.

You can write both in one batch:

```shell
> gresiblos blog/*.txt --atom-output <FILE_NAME1> --rss-output <FILE_NAME2>
```

**Yet, several important information about the feeds will be missing.** Some things have to be set on the command line additionally. A complete call that yields in valid __Atom__ and __RSS 2.0__ should have the following feed information set:

```shell
> gresiblos blog/*.txt --atom-output <FILE_NAME1> --rss-output <FILE_NAME2>
    --feed_title "Collected Notes"
    --feed_site http://john.doe.org
    --feed_description "Notes collected in the past time"
    --feed_editor_email john@doe.org
    --feed_editor_name "John Doe"
    --feed_copyright "(c) John Doe 2026"
```

You may want to use a configuration file:

```shell
gresiblos blog/*.txt -c blog.cfg
```

The accrding configuration file ```blog.cfg``` would look like this:

```cfg
[gresiblos]
input=blog/*.txt
atom_output=<FILE_NAME1>
rss_output=<FILE_NAME2>
feed_title=Collected Notes
feed_site=<URL>
feed_description=Notes collected in the past time
feed_editor_email=<EMAIL>
feed_editor_name=<NAME>
feed_copyright=<COPYRIGHT>
```

The values are inserted into the respective feeds as given in the next table.

| option                | Atom | RSS 2.0 |
| ---                   | ---   | --- |
| --feed-title          | &lt;title type="html"&gt;_[[:feed_title:]]_&lt;/title&gt; | &lt;title&gt;*[[:feed_title:]]*&lt;/title&gt; |
| --feed-site           | <ul><li>&lt;link&gt;_[[:feed_site:]]_&lt;/link&gt;</li><li>&lt;atom:link href="*[[:feed_site:]]*_rss.xml" rel="self" type="application/rss+xml"/&gt;</li></ul> | <ul><li>&lt;link href="_[[:feed_site:]]_"/&gt;</li><li>&lt;link rel="self" href="_[[:feed_site:]]_"/&gt;</li><li>&lt;link rel="alternate" type="text/html" hreflang="_[[:feed_language_short:]]_" href="_[[:feed_site:]]_"/&gt;</li><li>&lt;id&gt;_[[:feed_site:]]_&lt;/id&gt;</li></ul> |
| --feed-description    | &lt;description&gt;_[[:feed_description:]]_&lt;/description&gt; | |
| --feed-editor-email   | &lt;managingEditor&gt;_[[:feed_editor_email:]]_ (_[[:feed_editor_name:]]_)&lt;/managingEditor&gt; | &lt;author&gt;&lt;name&gt;_[[:feed_editor_name:]]_&lt;/name&gt;&lt;email&gt;_[[:feed_editor_email:]]_&lt;/email&gt;&lt;/author&gt; |
| --feed-editor-name    |  &lt;managingEditor&gt;_[[:feed_editor_email:]]_ (_[[:feed_editor_name:]]_)&lt;/managingEditor&gt; | &lt;author&gt;&lt;name&gt;_[[:feed_editor_name:]]_&lt;/name&gt;&lt;email&gt;_[[:feed_editor_email:]]_&lt;/email&gt;&lt;/author&gt; |
| --feed-copyright      |  &lt;copyright&gt;_[[:feed_copyright:]]_&lt;/copyright&gt; | &lt;rights&gt;_[[:feed_copyright:]]_&lt;/rights&gt; |
| --feed-language       |  &lt;language&gt;*[[:feed_language:]]*&lt;/language&gt; | &lt;link rel="alternate" type="text/html" hreflang="*[[:feed_language_short:]]*" href="*[[:feed_site:]]*"/&gt; |
| --feed-utz            | | |


The generated __Atom__ feed looks like this:


The generated __RSS 2.0__ feed looks like this:


