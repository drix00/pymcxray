#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: mcxray.format.io

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Read input and output mcxray files.
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
import mcxray.format.text.read
import mcxray.format.hdf5.read

# Globals and constants variables.


def read_text_input(file_path):
    """
    Read simulation input from a text file.

    :param file_path: path of the text file.
    :return: :py:`Simulation` object.
    """
    simulation = mcxray.format.text.read.read_text_input(file_path)

    return simulation


def read_text_output(path, basename):
    """
    Read simulation output from a text file.

    :param path: path of the text files
    :param basename:
    :return: :py:`Simulation` object.
    """
    simulation = mcxray.format.text.read.read_text_output(path, basename)

    return simulation


def convert_text_input_to_hdf5(text_file_path, hdf5_file_path=None):
    """
    Convert a text input files into a hdf5.

    .. todo:: Implement this method.

    :param text_file_path:
    :param hdf5_file_path:
    :return: :py:`Simulation` object.
    """
    simulation = read_text_input(text_file_path)

    return simulation


def convert_text_output_to_hdf5(text_file_path, hdf5_file_path=None):
    """
    Convert a text output files into a hdf5.

    .. todo:: Implement this method.

    :param text_file_path:
    :param hdf5_file_path:
    :return: :py:`Simulation` object.
    """
    simulation = read_text_output(text_file_path)

    return simulation


def read_hdf5_input(file_path):
    """
    Read simulation input from a hdf5 file.

    :param file_path:
    :return: :py:`Simulation` object.
    """
    simulation = mcxray.format.hdf5.read.read_hdf5_input(file_path)

    return simulation


def read_hdf5_output(file_path):
    """
    Read simulation output from a hdf5 file.

    :param file_path:
    :return: :py:`Simulation` object.
    """
    simulation = mcxray.format.hdf5.read.read_hdf5_output(file_path)

    return simulation
