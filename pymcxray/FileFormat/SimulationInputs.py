#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.SimulationInputs
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

MCXRay simulation inputs file.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2012 Hendrix Demers"
__license__ = ""

# Standard library modules.
import os.path
import copy

# Third party modules.

# Local modules.

# Project modules
import pymcxray.FileFormat.Version as Version

# Globals and constants variables.

KEY_SPECIMEN = "specimen"
KEY_MODEL = "model"
KEY_MICROSCOPE = "microscope"
KEY_PARAMETERS = "parameters"
KEY_MAP = "map"
KEY_SNR = "snr"
KEY_RESULTS = "results"

class SimulationInputs(object):
    def __init__(self):
        self._keys = self._createKeys()
        self._filenames = {}

        self._title = ""

        self.version = copy.deepcopy(Version.CURRENT_VERSION)

    def _createKeys(self):
        keys = []

        keys.append(KEY_SPECIMEN)
        keys.append(KEY_MODEL)
        keys.append(KEY_MICROSCOPE)
        keys.append(KEY_PARAMETERS)
        keys.append(KEY_MAP)
        keys.append(KEY_RESULTS)
        #keys.append(KEY_SNR)

        return keys

    def read(self, filepath):
        self.version.readFromFile(filepath)

        self._title = self._extractTitleFromFilepath(filepath)

        lines = open(filepath, 'r').readlines()

        for line in lines:
            line = line.strip()

            for key in self._keys:
                if line.startswith(key):
                    items = line.split('=')
                    self._filenames[key] = str(items[-1])

    def write(self, filepath):
        title = self._extractTitleFromFilepath(filepath)

        outputFile = open(filepath, 'w')

        self.version.writeLine(outputFile)

        keys = self._createKeys()
        if self.version < Version.VERSION_1_4_0:
            keys.remove(KEY_RESULTS)

        for key in keys:
            if key not in self._filenames:
                extension = self.getExtension(key)
                filename = "%s.%s" % (title, extension)
                self._filenames[key] = filename

            if self._filenames[key] is not None:
                line = "%s=%s\n" % (key, self._filenames[key])
                outputFile.write(line)

    def _extractTitleFromFilepath(self, filepath):
        filename = os.path.basename(filepath)
        title, _extension = os.path.splitext(filename)

        return title

    def getExtension(self, key):
        if key == KEY_SPECIMEN:
            return "sam"
        elif key == KEY_MODEL:
            return "mdl"
        elif key == KEY_MICROSCOPE:
            return "mic"
        elif key == KEY_PARAMETERS:
            return "par"
        elif key == KEY_MAP:
            return "mpp"
        elif key == KEY_RESULTS:
            return "rp"
        elif key == KEY_SNR:
            return "snp"

    @property
    def version(self):
        return self._version
    @version.setter
    def version(self, version):
        self._version = version

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        self._title = title

    @property
    def specimenFilename(self):
        return self._filenames[KEY_SPECIMEN]
    @specimenFilename.setter
    def specimenFilename(self, specimenFilename):
        self._filenames[KEY_SPECIMEN] = specimenFilename

    @property
    def modelFilename(self):
        return self._filenames[KEY_MODEL]
    @modelFilename.setter
    def modelFilename(self, modelFilename):
        self._filenames[KEY_MODEL] = modelFilename

    @property
    def microsopeFilename(self):
        return self._filenames[KEY_MICROSCOPE]
    @microsopeFilename.setter
    def microsopeFilename(self, microsopeFilename):
        self._filenames[KEY_MICROSCOPE] = microsopeFilename

    @property
    def simulationParametersFilename(self):
        return self._filenames[KEY_PARAMETERS]
    @simulationParametersFilename.setter
    def simulationParametersFilename(self, simulationParametersFilename):
        self._filenames[KEY_PARAMETERS] = simulationParametersFilename

    @property
    def mapFilename(self):
        return self._filenames[KEY_MAP]
    @mapFilename.setter
    def mapFilename(self, mapFilename):
        self._filenames[KEY_MAP] = mapFilename

    @property
    def snrFilename(self):
        return self._filenames[KEY_SNR]
    @snrFilename.setter
    def snrFilename(self, snrFilename):
        self._filenames[KEY_SNR] = snrFilename

    @property
    def resultParametersFilename(self):
        return self._filenames[KEY_RESULTS]
    @resultParametersFilename.setter
    def resultParametersFilename(self, resultParametersFilename):
        self._filenames[KEY_RESULTS] = resultParametersFilename
