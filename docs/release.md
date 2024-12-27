Release Steps
=============

* check the [ChangeLog](https://github.com/dkrajzew/gresiblos/blob/master/docs/mkdocs/changes.md)
* patch the release number and the copyright information in
    * the [README.md](https://github.com/dkrajzew/gresiblos/blob/master/README.md) file
    * the [setup.py](https://github.com/dkrajzew/gresiblos/blob/master/setup.py) file
    * the [install.md](https://github.com/dkrajzew/gresiblos/blob/master/docs/mkdocs/install.md) file
    * the scripts and tests
* run the tests (run tests/run_tests.bat)
* commit changes
* build the pydoc documentation, copy it to the web pages
* build the github release (tag: ___&lt;VERSION&gt;___, name: __gresiblos-_&lt;VERSION&gt;___)
* build the PyPI release
	* ```python -m build```
	* ```python -m twine upload --repository pypi dist/*```

