#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
# ===========================================================================
"""gresiblos - Setup module."""
# ===========================================================================
__author__     = "Daniel Krajzewicz"
__copyright__  = "Copyright 2014-2024, Daniel Krajzewicz"
__credits__    = ["Daniel Krajzewicz"]
__license__    = "GPLv3"
__version__    = "0.2.0"
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
    version="0.2.0",
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
    license='GPLv3',
    # add modules
    packages=setuptools.find_packages(),
    data_files=[
        ('', ['data/entry1.txt', 'data/entry2.txt', 'data/template.html',
            'tests/cfg1.cfg', 'tests/cfg2.cfg', 
            'tests/my-first-blog-entry.html', 'tests/my-second-blog-entry.html']),
    ],
    entry_points = {
        'console_scripts': [
            'gresiblos = gresiblos:main'
        ]
    },
    # see https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
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

