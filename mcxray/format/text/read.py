#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: mcxray.format.text.read

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Read mcxray input output text files.
"""

###############################################################################
# Copyright 2018 Hendrix Demers
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

# Third party modules.

# Local modules.

# Project modules.
from mcxray.format.simulation import Simulation
from mcxray.format.text import extract_basename
import mcxray.format.text.version
from mcxray.format.version import Version

# Globals and constants variables.


def read_text_input(file_path):
    """
    Read simulation input from a text file.

    :param file_path: path of the text file.
    :return: :py:class:`Simulation` object.
    """
    simulation = Simulation()

    basename = extract_basename(file_path)
    simulation.name = basename

    version = Version(0, 0, 0)
    mcxray.format.text.version.read_from_file(version, file_path)
    simulation.version = version

    return simulation


def read_text_output(path, basename):
    """
    Read simulation output from a text file.

    :param path: path of the text files
    :param basename:
    :return: :py:class:`Simulation` object.
    """
    simulation = Simulation()

    simulation.name = basename
    simulation.version = mcxray.format.text.version.read_from_output_file(path, basename)
    return simulation
