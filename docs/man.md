# Man page

__gresiblos__ &#8212; a simple private blogging system.

## Synopsis

```shell
gresiblos [-t TEMPLATE] [-e EXTENSION]
          [-s STATE] [-d DESTINATION] [--index-output INDEX_OUTPUT]
          [--chrono-output CHRONO_OUTPUT] [--alpha-output ALPHA_OUTPUT]
          [--markdown] [--degrotesque] [--topic-format TOPIC_FORMAT]
          [--index-indent INDEX_INDENT] [--date-format DATE_FORMAT]
          input

gresiblos -c FILE

gresiblos [-c FILE] [-t TEMPLATE] [-e EXTENSION]
          [-s STATE] [-d DESTINATION] [--index-output INDEX_OUTPUT]
          [--chrono-output CHRONO_OUTPUT] [--alpha-output ALPHA_OUTPUT]
          [--markdown] [--degrotesque] [--topic-format TOPIC_FORMAT]
          [--index-indent INDEX_INDENT] [--date-format DATE_FORMAT]
          [input]
          
gresiblos --help

gresiblos --version
```

## Description

__gresiblos__ is implemented in [Python](https://www.python.org/). It is started on the command line.

__gresiblos__ reads one or multiple text files and embeds them into a template. The entry/entries to process are a mandatory argument. Multiple entries can be given divided by a &#8216;,&#8217;. Wildcards are accepted as well, so giving ```./entries/*.txt``` will process all files with the extension .txt within the folder ```entries```.

The template file to use is defined using the option **--template *&lt;TEMPLATE&gt;*** / **-t *&lt;TEMPLATE&gt;***. If not given the default template is used.

Generated pages are saved as .html-files per default. You may change it (e.g. to php) using the option **--extension *&lt;EXTENSION&gt;*** / **-e *&lt;EXTENSION&gt;***.

The entries may include the meta-information ```state```. You may filter entries to process by setting the option **--state *&lt;STATE&gt;*** / **-s *&lt;STATE&gt;*** to the one that shall be processed.

The path to store the generated pages into can be defined using the option **--destination *&lt;PATH&gt;*** / **-d *&lt;PATH&gt;***. The default is ```./```.

Besides the generated entries, **gresiblos** may generate a json-index file that lists the entries with some meta-information. The option **--index-output *&lt;FILE&gt;*** will generate the index and save it under the given file name. The index is usually stored as plain json in a single line. For a prettier output, the indentation can be changed using the option **--index-indent *&lt;INT&gt;***.

In addition, files containing the list of converted files can be generated. The lists are embedded into the content section of the template file. Use the option **--chrono-output *&lt;FILE&gt;*** to generate a file with the entries sorted in chronological order and/or the option **--alpha-output *&lt;FILE&gt;*** with the entries sorted alphabetically.

To convert contents from markdown to HTML before embedding them, use the option **--markdown**. When set, the content, the title, and the abstract will be converted. Use the option **--degrotesque** to apply the [degrotesque](https://github.com/dkrajzew/degrotesque) type setter on the contents before embedding them. Please note that you need to install markdown and/or degrotesque by yourself.

When embedding the meta-information of single blog entries into the template, the topics are split and rendered individually before being embedded. To allow for using them as links, the rendering format can be set using the option **--topic-format *&lt;TOPIC_FORMAT&gt;***. Please note that this string should include something like &#8220;\[\[:topic:\]\]&#8221;, what is replaced by the topic itself. The date meta information is assumed to be in ISO-format (e.g. ```2025-01-08 19:26:00```), but may be adapted using the option __--date-format *&lt;DATE_FORMAT&gt;*__.

__gresiblos__ generates an RSS 2.0 feed if the option **--rss-output *&lt;FILE&gt;*** is set and writes it into ***&lt;FILE&gt;***. It generates an Atom feed if the option **--atom-output *&lt;FILE&gt;*** is set and writes it into ***&lt;FILE&gt;***.

Further options should be set when generating feeds for supplying needed information. **--feed-title *&lt;STRING&gt;*** sets the title of the feed, **--feed-site *&lt;STRING&gt;*** the URL of the feed (without the file name which is generated from ), **--feed-description *&lt;STRING&gt;*** sets the feed description, **--feed-editor-email *&lt;STRING&gt;*** sets the editor's e-mail address and **--feed-editor-name *&lt;STRING&gt;*** the editor's name. **--feed-language *&lt;STRING&gt;*** sets the feed's language, **--feed-copyright *&lt;STRING&gt;*** sets the copyright information about the feed, and **--feed-utz *&lt;STRING&gt;*** sets the feed's time zone. The defined language must match the ISO 639 specification.

The options can be stored in a configuration file which can be passed to __gresiblos__ using the option **--config *&lt;CONFIGURATION&gt;*** / **-c *&lt;CONFIGURATION&gt;***. Options given on the command line will overwrite the options set in the configuration file.


## Arguments and options

__gresiblos__ requires one parameter:

* **input**: The files (entries) to read, separated by &#8216;,&#8217;; accepts wildcards as well


__gresiblos__ can be started with the following options:

* **--config *&lt;CFG_FILE&gt;*** / **-c *&lt;CFG_FILE&gt;***: Reads the named configuration file
* **--destination *&lt;PATH&gt;*** / **-d *&lt;PATH&gt;***: The path to store the generated file(s) into
* **--template *&lt;TEMPLATE_FILE&gt;*** / **-t *&lt;TEMPLATE_FILE&gt;***: Defines the template file to use
* **--extension *&lt;EXTENSION&gt;*** / **-e *&lt;EXTENSION&gt;***: The extension of the built file(s)
* **--state *&lt;STATE&gt;*** / **-s *&lt;STATE&gt;***: The state the entries must have for being processed
* **--index-output *&lt;FILE&gt;***: Writes the index to the named file
* **--chrono-output *&lt;FILE&gt;***: Writes the named file with entries in chronological order
* **--alpha-output *&lt;FILE&gt;***: Writes the named file with entries in alphabetical order
* **--markdown**: If set, markdown is applied on the contents
* **--degrotesque**: If set, degrotesque is applied on the contents, the abstract, and the title
* **--topic-format *&lt;TOPIC_FORMAT&gt;***: Defines how each of the topics is rendered
* **--index-indent *&lt;INT&gt;***: Defines the indent used for the index file
* **--date-format *&lt;DATE_FORMAT&gt;***: Defines the time format used
* **--rss-output *&lt;FILE&gt;***: Writes an RSS 2.0 feed to the named file
* **--atom-output *&lt;FILE&gt;***: Writes an Atom feed to the named file
* **--feed-title *&lt;STRING&gt;***:Title to use for the feed
* **--feed-site *&lt;STRING&gt;***: Base URL used to prefix entry filenames in the feed
* **--feed-description *&lt;STRING&gt;***: The feed description
* **--feed-editor-email *&lt;STRING&gt;***: The email of the feed editor
* **--feed-editor-name *&lt;STRING&gt;***: The name of the feed editor
* **--feed-language *&lt;STRING&gt;***: The language of the feed
* **--feed-copyright *&lt;STRING&gt;***: The copyright information about the feed
* **--feed-utz *&lt;STRING&gt;***: The feed's time zone
* **--help** / **-h**: Show a help message
* **--version**: Show the version information


## Examples

```shell
gresiblos ./entries/*
```

Generates pages using the default template ```./data/template.html``` and the blog entries located in ```entries``` and writes them to ```./gresiblos_out```.


```shell
gresiblos ./entries/* -d ./my_blog/
```

Generates pages using the default template ```./data/template.html``` and the blog entries located in ```entries``` and writes them to ```./my_blog```.


```shell
gresiblos --template mytemplate.html --state release ./entries/*
```

Generates pages using the template ```mytemplate.html``` and the blog entries located in ```entries``` and writes them to ```./gresiblos_out```. Processes only entries with state=release.


```shell
gresiblos ./entries/* --rss-output atom.xml --rss-output atom.xml
```

Generates pages using the default template ```./data/template.html``` and the blog entries located in ```entries``` and writes them to ```./gresiblos_out```. Generates an RSS 2.0 and an Atom feed containing the read items. Please note that the options starting with --feed should be set for obtaining complete and valid feeds.


```shell
gresiblos -c my_blog.cfg
```

Reads settings from the configuration file ```my_blog.cfg``` and processes as defined therein.


## Files

__gresiblos__ comes with a default template.

As well, __gresiblos__ uses templates for generating the feeds. For both, RSS and Atom, files that contain the feed's head and tail, as well as files for the entries are used, respectively.

All files are located in the folder ```./data/``` which is located in the same folder as ```./gresiblos.py/```.

## Diagnostics

__gresiblos__ uses the following exit codes:

* **0**: no issues / finished successfully
* **1**: at least two of the read entries have the same output name
* **2**: one of the set options is not valid
* **3**: the given template is broken; check whether all opening / closing tags match

## Bugs and caveats

* When setting __--date-format *&lt;DATE_FORMAT&gt;*__, all entries must use this date format.

## See also

* https://github.com/dkrajzew/gresiblos
* http://www.krajzewicz.de/blog


 