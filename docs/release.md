Release Steps
=============

* check the [ChangeLog](https://github.com/dkrajzew/gresiblos/blob/master/docs/mkdocs/changes.md)
* patch the release number and the copyright information in
    * the [README.md](https://github.com/dkrajzew/gresiblos/blob/master/README.md) file
    * the [setup.py](https://github.com/dkrajzew/gresiblos/blob/master/setup.py) file
    * the [install.md](https://github.com/dkrajzew/gresiblos/blob/master/docs/mkdocs/install.md) file
    * the scripts and tests
* run the tests (run tests/run_tests.bat)
* build the pydoc documentation, copy it to the web pages
* commit changes
* build and upload the documentation
    * use the script "___&lt;GRESIBLOS&gt;_\docs\build_docs.bat__"
    * copy it to the web pages
* build the github release (tag: ___&lt;VERSION&gt;___, name: __gresiblos-_&lt;VERSION&gt;___)
* build the PyPI release using the script "___&lt;GRESIBLOS&gt;_\docs\build_release.bat__"

