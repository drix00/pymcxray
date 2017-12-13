#!/usr/bin/env python
"""
.. py:currentmodule:: BatchFileConsole
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

MCXRay console batch file creator.

"""

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
        """
        The batch file is responsible to create the simulation structure with a copy of mcxray program.

        One important parameter to set is the `numberFiles`, this is the number of batch files generated
        and that can be run in parallel. For maximum efficiency it should be set as the number of logical processors minus 1 or 2.
        For example, on a computer with 12 logical processors, the `numberFiles` should be set at 10.

        :param str name: Basename used for the batch files
        :param str programName: Name of the executable to add in the batch file
        :param int numberFiles: Number of batch files to generate and possibly to run in parallel
        """
        self._name = name
        self._programName = programName
        self._numberFiles = numberFiles

        self._extension = ".bat"
        self._simulationFilenames = []


    def addSimulationName(self, simulationFilename):
        """
        Add a simulation in the simulation list.

        :param str simulationFilename: File path of the simulation added
        """
        self._simulationFilenames.append(simulationFilename)

    def write(self, path):
        """
        Write the batch files for all simulations in the simulation list.

        :param str path: Path where the batch files are written.
        """
        self._remove_previous_files(path)

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

    def _remove_previous_files(self, path):
        for filename in os.listdir(path):
            if filename.startswith(self._name) and filename.endswith(self._extension):
                filepath = os.path.join(path, filename)
                logging.info("Remove previous file: %s", filepath)
                os.remove(filepath)
