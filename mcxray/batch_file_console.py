#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: mcxray.batch_file_console
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

MCXRay console batch file creator.
"""

###############################################################################
# Copyright 2024 Hendrix Demers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
###############################################################################

# Standard library modules.
import os
import logging
import math
import random

# Third party modules.

# Local modules.

# Project modules.

# Globals and constants variables.


class BatchFileConsole:
    def __init__(self, name, program_name, number_files=1):
        """
        The batch file is responsible to create the simulation structure with a copy of mcxray program.

        One important parameter to set is the `number_files`, this is the number of batch files generated
        and that can be run in parallel. For maximum efficiency it should be set as the number of
        logical processors minus 1 or 2.
        For example, on a computer with 12 logical processors, the `numberFiles` should be set at 10.

        :param str name: Basename used for the batch files
        :param str program_name: Name of the executable to add in the batch file
        :param int number_files: Number of batch files to generate and possibly to run in parallel
        """
        self._name = name
        self._program_name = program_name
        self._number_files = number_files

        self._extension = ".bat"
        self._simulation_filenames = []

    def add_simulation_name(self, simulation_filename):
        """
        Add a simulation in the simulation list.

        :param str simulation_filename: File path of the simulation added
        """
        self._simulation_filenames.append(simulation_filename)

    def write(self, path):
        """
        Write the batch files for all simulations in the simulation list.

        :param str path: Path where the batch files are written.
        """
        self._remove_previous_files(path)

        if len(self._simulation_filenames) == 0:
            return

        random.shuffle(self._simulation_filenames)

        if self._number_files > 1:
            number_simulations = len(self._simulation_filenames)
            index_step = int(math.ceil(float(number_simulations) / float(self._number_files)))

            index_filenames = 0
            for index_file in range(self._number_files):
                if index_filenames < number_simulations:
                    filename = self._name + "_%i" % (index_file+1) + self._extension
                    filepath = os.path.join(path, filename)

                    logging.info("Write batch file: %s", filepath)
                    batch_file = open(filepath, 'w')

                    for simulation_filename in self._simulation_filenames[index_filenames:index_filenames + index_step]:
                        line = "%s %s\n" % (self._program_name, simulation_filename)
                        batch_file.write(line)

                    index_filenames += index_step

                    batch_file.close()
        else:
            filename = self._name + self._extension
            filepath = os.path.join(path, filename)

            logging.info("Write batch file: %s", filepath)
            batch_file = open(filepath, 'w')

            for simulation_filename in self._simulation_filenames:
                line = "%s %s\n" % (self._program_name, simulation_filename)
                batch_file.write(line)

            batch_file.close()

    def _remove_previous_files(self, path):
        for filename in os.listdir(path):
            if filename.startswith(self._name) and filename.endswith(self._extension):
                filepath = os.path.join(path, filename)
                logging.info("Remove previous file: %s", filepath)
                os.remove(filepath)
