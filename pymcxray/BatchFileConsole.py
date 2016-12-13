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
from pymcxray.mcxray import ANALYZE_TYPE_READ_RESULTS

# Globals and constants variables.
READ_RESULT_AFTER_N_SIMULATIONS = 10

class BatchFileConsole(object):
    def __init__(self, name, programName, numberFiles=1, script_file_path=None):
        self._name = name
        self._programName = programName
        self._numberFiles = numberFiles
        self.script_file_path = script_file_path

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
            number_simulations = len(self._simulationFilenames)
            indexStep = int(math.ceil(float(number_simulations)/float(self._numberFiles)))

            indexFilenames = 0
            for indexFile in range(self._numberFiles):
                if indexFilenames < number_simulations:
                    filename = self._name + "_%i" % (indexFile+1) + self._extension
                    filepath = os.path.join(path, filename)

                    logging.info("Write batch file: %s", filepath)
                    batchFile = open(filepath, 'w')

                    for index_local_batch, simulationFilename in enumerate(self._simulationFilenames[indexFilenames:indexFilenames+indexStep]):
                        line = "%s %s\n" % (self._programName, simulationFilename)
                        batchFile.write(line)
                        if self.script_file_path is not None and index_local_batch%10 == 0:
                            line_read_data = "py -3 %s %s\n" % (self.script_file_path, ANALYZE_TYPE_READ_RESULTS)
                            batchFile.write(line_read_data)

                    indexFilenames += indexStep

                    if self.script_file_path is not None:
                        line_read_data = "py -3 %s %s\n" % (self.script_file_path, ANALYZE_TYPE_READ_RESULTS)
                        batchFile.write(line_read_data)
                    batchFile.close()
        else:
            filename = self._name + self._extension
            filepath = os.path.join(path, filename)

            logging.info("Write batch file: %s", filepath)
            batchFile = open(filepath, 'w')

            for index_local_batch, simulationFilename in enumerate(self._simulationFilenames):
                line = "%s %s\n" % (self._programName, simulationFilename)
                batchFile.write(line)
                if self.script_file_path is not None and index_local_batch != 0 and index_local_batch%READ_RESULT_AFTER_N_SIMULATIONS == 0:
                    line_read_data = "py -3 %s %s\n" % (self.script_file_path, ANALYZE_TYPE_READ_RESULTS)
                    batchFile.write(line_read_data)

            if self.script_file_path is not None:
                line_read_data = "py -3 %s %s\n" % (self.script_file_path, ANALYZE_TYPE_READ_RESULTS)
                batchFile.write(line_read_data)
            batchFile.close()

    def removePreviousFiles(self, path):
        for filename in os.listdir(path):
            if filename.startswith(self._name) and filename.endswith(self._extension):
                filepath = os.path.join(path, filename)
                logging.info("Remove previous file: %s", filepath)
                os.remove(filepath)
