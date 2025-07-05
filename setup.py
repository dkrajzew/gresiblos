#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
# ===========================================================================
"""gresiblos - Setup module."""
# ===========================================================================
__author__     = "Daniel Krajzewicz"
__copyright__  = "Copyright 2014-2025, Daniel Krajzewicz"
__credits__    = ["Daniel Krajzewicz"]
__license__    = "BSD"
__version__    = "0.8.0"
__maintainer__ = "Daniel Krajzewicz"
__email__      = "daniel@krajzewicz.de"
__status__     = "Development"
# ===========================================================================
# - https://github.com/dkrajzew/gresiblos
# - http://www.krajzewicz.de/docs/gresiblos/index.html
# - http://www.krajzewicz.de
# ===========================================================================


# --- imports ---------------------------------------------------------------
import setuptools


# --- definitions -----------------------------------------------------------
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gresiblos",
    version="0.8.0",
    author="dkrajzew",
    author_email="d.krajzewicz@gmail.com",
    description="A simple private blogging system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://gresiblos.readthedocs.org/',
    download_url='http://pypi.python.org/pypi/gresiblos',
    project_urls={
        'Documentation': 'https://gresiblos.readthedocs.io/',
        'Source': 'https://github.com/dkrajzew/gresiblos',
        'Tracker': 'https://github.com/dkrajzew/gresiblos/issues',
        'Discussions': 'https://github.com/dkrajzew/gresiblos/discussions',
    },
    license='BSD-3-Clause',
    packages = ["", "data", "tools"],
    package_dir = { "": "gresiblos", "data": "gresiblos/data", "tools": "gresiblos/tools" },
    package_data={"": ["data/*", "tools/*"]},
    entry_points = {
        "console_scripts": [
            "gresiblos = gresiblos:script_run"
        ]
    },
    # see https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Telecommunications Industry",
        "Intended Audience :: Other Audience",
        "Topic :: Communications",
        "Topic :: Documentation",
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Text Processing"
    ],
    python_requires='>=3, <4',
)

