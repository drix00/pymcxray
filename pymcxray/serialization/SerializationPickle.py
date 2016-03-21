#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2007 Hendrix Demers"
__license__ = ""

# Standard library modules.
import pickle
import logging

# Third party modules.

# Local modules.
import pymcxray.serialization._Serialization as _Serialization

# Globals and constants variables.

class SerializationPickle(_Serialization._Serialization):
    KEY_FILE_VERSION = "fileVersion"
    KEY_SERIALIZED_DATA = "serializedData"

    def load(self):
        filepath = self.getFilepath()
        if self._verbose:
            logging.debug("Reading serialization file: %s.", filepath)

        dataFile = open(filepath, "rb")
        data = pickle.load(dataFile)

        if isinstance(data, dict) and SerializationPickle.KEY_FILE_VERSION in data:
            self._fileVersion = data[SerializationPickle.KEY_FILE_VERSION]
            serializedData = data[SerializationPickle.KEY_SERIALIZED_DATA]
        else:
            self._fileVersion = None
            serializedData = data

        dataFile.close()
        del data

        return serializedData

    def save(self, serializedData):
        filepath = self.getFilepath()
        if self._verbose:
            logging.debug("Writing serialization file %s.", filepath)

        if self._currentVersion is not None:
            data = {}
            data[SerializationPickle.KEY_FILE_VERSION] = self._currentVersion
            data[SerializationPickle.KEY_SERIALIZED_DATA] = serializedData

        dataFile = open(filepath, "wb")
        pickle.dump(data, dataFile, protocol=2)
        dataFile.close()
        del data
