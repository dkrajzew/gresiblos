# Running on the Command Line

## Synopsis

```shell
gresiblos [-h] [-c FILE] [--version] [-t TEMPLATE] [-e EXTENSION]
          [-s STATE] [-d DESTINATION] [--topic-format TOPIC_FORMAT]
          input

```

## Description

__gresiblos__ is implemented in [Python](https://www.python.org/). It is started on the command line.

__gresiblos__ reads one or multiple blog entry files and embeds them into a template. The template file to use is defined using the option **--template *&lt;TEMPLATE&gt;*** / **-t *&lt;TEMPLATE&gt;***.

Generated pages are daved as .html-files per default. You may change it (e.g. to php) using the option **--extension *&lt;EXTENSION&gt;*** / **-e *&lt;EXTENSION&gt;***.

The path to store the generated pages into can be defined using the option **--destination *&lt;PATH&gt;*** / **-d *&lt;PATH&gt;***. The default is ```./```. The index will be stored in this folder as well.

The entries include the meta-information ```state```. You may filter entries to process by setting the option **--state *&lt;STATE&gt;*** / **-s *&lt;STATE&gt;*** to the one that shall be processed.

When embedding the meta-information of single blog entries into the template, the topics are split and rendered individually before being embedded. To allow for using them as links, the rendering format can be set using the option **--topic-format *&lt;TOPIC_FORMAT&gt;***. Please note that this string should include something like &#8220;\[\[:topic:\]\]&#8221;, what is replaced by the topic itself. The date meta information is assumed to be in ISO-format (e.g. ```2025-01-08 19:26:00```), but may be adapted using the option __--date-format *&lt;DATE_FORMAT&gt;*__.

The index is usually stored as plain json in a single line. For a prettier output, the identation can be changed using the option **--index-indent *&lt;INT&gt;***.

The entry/entries to process are given as the last parameter. Multiple entries can be given divided by a &#8216;,&#8217;. Wildcards are accepted as well, so giving ```./entries/*.txt``` will process all files with the extension .txt within the folder ```entries```.

The options can be stored in a configuration file which can be passed to __gresiblos__ using the option **--config *&lt;CONFIGURATION&gt;*** / **-c *&lt;CONFIGURATION&gt;***. Options given on the command line will overwrite the options set in the configuration file.


## Examples

```shell
python gresiblos ./entries/*
```

Generates pages using the default template ```./data/template.html``` and the blog entries located in ```entries``` and writes them to ```./```.

```shell
python gresiblos --template mytemplate.html --state release ./entries/*
```

Generates pages using the template ```mytemplate.html``` and the blog entries located in ```entries``` and writes them to ```./```. Processes only entries with state=release.


## Command line arguments

The script can be started on the command line with the following options:

* **--config *&lt;CFG_FILE&gt;*** / **-c *&lt;CFG_FILE&gt;***: Reads the named configuration file
* **--template *&lt;TEMPLATE_FILE&gt;*** / **-t *&lt;TEMPLATE_FILE&gt;***: Uses the named template file
* **--extension *&lt;EXTENSION&gt;*** / **-e *&lt;EXTENSION&gt;***: The extension to use for the generated files
* **--state *&lt;STATE&gt;*** / **-s *&lt;STATE&gt;***: The state the entries must have for being processed
* **--destination *&lt;PATH&gt;*** / **-d *&lt;PATH&gt;***: The path to save the generated file(s) into
* **--topic-format *&lt;TOPIC_FORMAT&gt;***: Defines how each of the topics is rendered
* **--index-indent *&lt;INT&gt;***: Defines the indent used for the index file
* **--date-format *&lt;DATE_FORMAT&gt;***: Defines the time format used
* **--help** / **-h**: Show a help message
* **--version**: Show the version information

__gresiblos__ requires one parameter:

* **input**: The files (entries) to read, separated by &#8216;,&#8217;; accepts wildcards as well

