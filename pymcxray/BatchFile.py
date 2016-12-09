#!/usr/bin/env python
"""
.. py:currentmodule:: BatchFile
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

MCXRay batch file creator.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2012 Hendrix Demers"
__license__ = ""

# Subversion informations for the file.
__svnRevision__ = "$Revision$"
__svnDate__ = "$Date$"
__svnId__ = "$Id$"

# Standard library modules.
import os
import logging
import math

# Third party modules.

# Local modules.

# Project modules

# Globals and constants variables.

class BatchFile(object):
    def __init__(self, name, numberFiles=1):
        self._name = name
        self._numberFiles = numberFiles

        self._extension = ".bfs"
        self._simulationFilenames = []


    def addSimulationName(self, simulationFilename):
        self._simulationFilenames.append(simulationFilename)

    def write(self, path):
        self.removePreviousFiles(path)

        if len(self._simulationFilenames) == 0:
            return

        if self._numberFiles > 1:
            indexStep = int(math.ceil(float(len(self._simulationFilenames))/float(self._numberFiles)))

            indexFilenames = 0
            for indexFile in range(self._numberFiles):
                filename = self._name + "_%i" % (indexFile+1) + self._extension
                filepath = os.path.join(path, filename)
                
                logging.info("Write batch file: %s", filepath)
                batchFile = open(filepath, 'w')

                for simulationFilename in self._simulationFilenames[indexFilenames:indexFilenames+indexStep]:
                    line = simulationFilename + "\n"
                    batchFile.write(line)

                indexFilenames += indexStep

                batchFile.close()
        else:
            filename = self._name + self._extension
            filepath = os.path.join(path, filename)

            logging.info("Write batch file: %s", filepath)
            batchFile = open(filepath, 'w')

            for simulationFilename in self._simulationFilenames:
                line = simulationFilename + "\n"
                batchFile.write(line)

            batchFile.close()

    def removePreviousFiles(self, path):
        for filename in os.listdir(path):
            if filename.startswith(self._name) and filename.endswith(self._extension):
                filepath = os.path.join(path, filename)
                logging.info("Remove previous file: %s", filepath)
                os.remove(filepath)
