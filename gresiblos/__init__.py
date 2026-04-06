#!/usr/bin/env python
"""Package initialization for gresiblos - greyrat's simple blog system."""
# ===========================================================================
# - https://github.com/dkrajzew/gresiblos
# - http://gresiblos.readthedocs.org/
# - http://www.krajzewicz.de/docs/gresiblos/index.html
# - http://www.krajzewicz.de
# - contact me: daniel@krajzewicz.de
# ===========================================================================


# --- imports ---------------------------------------------------------------
from .gresiblos import __author__
from .gresiblos import __copyright__
from .gresiblos import __credits__
from .gresiblos import __license__
from .gresiblos import __version__
from .gresiblos import __maintainer__
from .gresiblos import __email__
from .gresiblos import __status__
from .gresiblos import Template
from .gresiblos import Entry
from .gresiblos import PlainStorage
from .gresiblos import load_template
from .gresiblos import write_list
from .gresiblos import write_feed
from .gresiblos import get_args
from .gresiblos import collect_files_sorted
from .gresiblos import main
from .gresiblos import script_run


# --- definitions -----------------------------------------------------------
__all__ = [
    "__author__",
    "__copyright__",
    "__credits__",
    "__license__",
    "__version__",
    "__maintainer__",
    "__email__",
    "__status__",
    "Template",
    "Entry",
    "PlainStorage",
    "load_template",
    "write_list",
    "write_feed",
    "get_args",
    "collect_files_sorted",
    "main",
    "script_run"
]
