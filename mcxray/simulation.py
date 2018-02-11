#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: mcxray.simulation

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Simulation data structure for mcxray Monte Carlo simulation program.
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
from mcxray.format.text import extract_basename

# Globals and constants variables.


class Simulation(object):
    def __init__(self):
        self.name = ""

    def __eq__(self, other):
        return self.name == other.name


def read_text_input(file_path):
    simulation = Simulation()

    basename = extract_basename(file_path)
    simulation.name = basename

    return simulation


def read_text_output(path, basename):
    simulation = Simulation()

    simulation.name = basename

    return simulation


def convert_text_input_to_hdf5(text_file_path, hdf5_file_path=None):
    simulation = Simulation()
    return simulation


def convert_text_output_to_hdf5(text_file_path, hdf5_file_path=None):
    simulation = Simulation()
    return simulation


def read_hdf5_input(file_path):
    simulation = Simulation()

    basename = extract_basename(file_path)
    simulation.name = basename

    return simulation


def read_hdf5_output(file_path):
    simulation = Simulation()

    basename = extract_basename(file_path)
    simulation.name = basename

    return simulation
