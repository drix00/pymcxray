#!/usr/bin/env python
"""
.. py:currentmodule:: BatchFileConsole
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

MCXRay console batch file creator.

"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2012 Hendrix Demers"
__license__ = ""

# Standard library modules.
import os
import logging
import math
import random

# Third party modules.

# Local modules.

# Project modules

# Globals and constants variables.

class BatchFileConsole(object):
    def __init__(self, name, programName, numberFiles=1):
        self._name = name
        self._programName = programName
        self._numberFiles = numberFiles

        self._extension = ".bat"
        self._simulationFilenames = []


    def addSimulationName(self, simulationFilename):
        self._simulationFilenames.append(simulationFilename)

    def write(self, path):
        self.removePreviousFiles(path)

        if len(self._simulationFilenames) == 0:
            return
        random.shuffle(self._simulationFilenames)

        if self._numberFiles > 1:
            indexStep = int(math.ceil(float(len(self._simulationFilenames))/float(self._numberFiles)))

            indexFilenames = 0
            for indexFile in range(self._numberFiles):
                filename = self._name + "_%i" % (indexFile+1) + self._extension
                filepath = os.path.join(path, filename)

                logging.info("Write batch file: %s", filepath)
                batchFile = open(filepath, 'w')

                for simulationFilename in self._simulationFilenames[indexFilenames:indexFilenames+indexStep]:
                    line = "%s %s\n" % (self._programName, simulationFilename)
                    batchFile.write(line)

                indexFilenames += indexStep

                batchFile.close()
        else:
            filename = self._name + self._extension
            filepath = os.path.join(path, filename)

            logging.info("Write batch file: %s", filepath)
            batchFile = open(filepath, 'w')

            for simulationFilename in self._simulationFilenames:
                line = "%s %s\n" % (self._programName, simulationFilename)
                batchFile.write(line)

            batchFile.close()

    def removePreviousFiles(self, path):
        for filename in os.listdir(path):
            if filename.startswith(self._name) and filename.endswith(self._extension):
                filepath = os.path.join(path, filename)
                logging.info("Remove previous file: %s", filepath)
                os.remove(filepath)
