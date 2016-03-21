#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2011 Hendrix Demers"
__license__ = ""

# Standard library modules.
import logging
import os.path

# Third party modules.
import numpy as np

# Local modules.

# Project modules
import pymcxray.serialization._Serialization as _Serialization

# Globals and constants variables.

class SerializationNumpy(_Serialization._Serialization):
    def load(self):
        filepath = self.getFilepath()
        if self._verbose:
            logging.debug("Reading serialization file: %s.", filepath)

        serializedData = np.zeros((1), dtype=float)

        if os.path.isfile(filepath):
            serializedData = np.fromfile(filepath)

        return serializedData

    def save(self, serializedData):
        filepath = self.getFilepath()
        if self._verbose:
            logging.debug("Writing serialization file %s.", filepath)

        serializedData.tofile(filepath)

    def _getSerializationExtension(self):
        return "_numpy.dat"
