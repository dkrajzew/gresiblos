#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
# ===========================================================================
"""gresiblos - Setup module."""
# ===========================================================================
__author__     = "Daniel Krajzewicz"
__copyright__  = "Copyright 2014-2024, Daniel Krajzewicz"
__credits__    = ["Daniel Krajzewicz"]
__license__    = "BSD"
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
    description="A BibTex parser and converter",
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
    license='BSD',
    # add modules
    packages=setuptools.find_packages(),
    package_data={'': ["tex.db"]},
    entry_points = {
        'console_scripts': [
            'gresiblos = gresiblos:main'
        ]
    },
    # see https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Telecommunications Industry",
        "Topic :: Documentation",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Localization",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Other/Nonlisted Topic",
        "Topic :: Artistic Software"
    ],
    python_requires='>=3, <4',
)

