# ChangeLog for gresiblos


## gresiblos-0.10.0 (06.05.2026)

* changed the license from BSD to GPL-3.0
* added file output for rss/atom feeds instead of using a php-script
    * use **--rss-output** and **--atom-output** to respectively generate RSS 2.0 and Atom feeds
    * according options had to be added (**--feed-title**, **--feed-site**, **--feed-description**, **--feed-editor-email**, **--feed-editor-name**, **--feed-language**, **--feed-copyright**, **--feed-utz**)
    * removed the ```feed.php``` script
* added an option **--to-html** that embeds links in ```<a>``` tags and text paragraphs in ```<p>``` tags for converting text files to basic HTML files
* much debugging and code cleaning
* API / breaking changes
    * the list of items is now a JSON list, no longer a dict
    * the template has been updated
* updated index.php
    * removed cross site scripting vulnerability
* extended the documentation &#8212; split the user manual into parts

## gresiblos-0.8.0 (05.07.2025)

* improved installation (can be now included as a module and executed on the command line after being installed with pip
* the default template is now included in the package
* some linting
* corrected documentation


## gresiblos-0.6.0 (30.03.2025)

* changed the license from GPLv3 to BSD
* improving the documentation
* changes:
    * **important**: the replacement pattern for values within the template changed from __%*&lt;FIELD_NAME&gt;*%__ to __\[\[:*&lt;FIELD_NAME&gt;*:\]\]__
    * topics are stored as list in the index file
    * the filenames in the index now include the extension
    * the **state** attribute was removed from the index file
    * replaced option **--have-php-index** by the option **--topic-format *&lt;FORMAT&gt;*** which directly defines how each of a blog entries topics shall be rendered when embedding it into the template
    * removed options **--default-author *&lt;NAME&gt;***, **--default-copyright-date *&lt;DATE&gt;***, **--default-state *&lt;STATE&gt;*** and introduced replacements with defaults instead
* new
    * the indentation level of the index file can now be set using the option **--index-indent *&lt;INT&gt;***
    * you may use a different format for the date in your entries than the ISO-format by defining it using **--date-format *&lt;DATE_FORMAT&gt;***
    * added the possibility to skip document parts using the begin/end tags __\[\[:?*&lt;FIELD_NAME&gt;*:\]\]__ and __\[\[:*&lt;FIELD_NAME&gt;*?:\]\]__ if __*&lt;FIELD_NAME&gt;*__ is not set


## gresiblos-0.4.2 (29.12.2024)

* fixing tests&#8230;


## gresiblos-0.4.0 (29.12.2024)

* support for entry index (using json and php)
    * generates a json-file with entries
    * added a php-file which lists entries or topics
    * added a php-file which generates an rss or an atom feed
* updated the documentation
* fixing packaging


## gresiblos-0.2.0 (27.12.2024)

* Initial version
    * processes entries and saves them



