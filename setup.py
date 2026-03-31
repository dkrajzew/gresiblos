#!/usr/bin/env python
"""gresiblos - Setup module."""
# ===========================================================================
# - https://github.com/dkrajzew/gresiblos
# - http://gresiblos.readthedocs.org/
# - http://www.krajzewicz.de/docs/gresiblos/index.html
# - http://www.krajzewicz.de
# - contact me: daniel@krajzewicz.de
# ===========================================================================


# --- imports ---------------------------------------------------------------
import setuptools
import gresiblos

# --- definitions -----------------------------------------------------------
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gresiblos",
    version=gresiblos.__version__,
    author=gresiblos.__author__,
    author_email=gresiblos.__email__,
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
    license='GPL-3.0',
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

