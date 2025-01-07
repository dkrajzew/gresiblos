# ChangeLog for gresiblos

## gresiblos-0.6.0 (to come)
* improving the documentation
* changes:
    * **important**: the replacement pattern for values within the template changed from __%*&lt;FIELD_NAME&gt;*%__ to __\[\[:*&lt;FIELD_NAME&gt;*:\]\]__
    * topics are stored as list in the index file
    * the filenames in the index now include the extension
    * the **state** attribute was removed from the index file
    * replaced option **--have-php-index** by the option **--topic-format *&lt;FORMAT&gt;*** which directly defines how each of a blog entries topics shall be rendered when embedding it into the template
    * removed options **--default-author *&lt;NAME&gt;***, **--default-copyright-date *&lt;DATE&gt;***, **--default-state *&lt;STATE&gt;*** and introduced replacements with defaults instead
* new
    * the identation level of the index file can now be set using the option **--index-indent *&lt;INT&gt;***


## gresiblos-0.4.2 (29.12.2024)
* fixing tests...

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
    


