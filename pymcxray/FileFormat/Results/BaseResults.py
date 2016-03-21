#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.BaseResults
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

BaseResults
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2012 Hendrix Demers"
__license__ = ""

# Standard library modules.
import os.path

# Third party modules.

# Local modules.

# Project modules

# Globals and constants variables.

class BaseResults(object):
    def __init__(self, path="", basename="MCXRay"):
        self.path = path
        self.basename = basename

    def _createFilename(self):
        raise NotImplementedError()

    @property
    def path(self):
        return self._path
    @path.setter
    def path(self, path):
        self._path = path

    @property
    def basename(self):
        return self._basename
    @basename.setter
    def basename(self, basename):
        self._basename = basename

    @property
    def filepath(self):
        filename = self._createFilename()
        filepath = os.path.join(self.path, filename)
        return filepath
