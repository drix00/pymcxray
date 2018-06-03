#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: mcxray.format.hdf5.read

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Read mcxray input output HDF5 files.
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
import h5py

# Local modules.

# Project modules.
from mcxray.format.simulation import Simulation
from mcxray.format.text import extract_basename
import mcxray.format.hdf5.version

# Globals and constants variables.

GROUP_SIMULATION = "Simulation"

ATTRIBUTE_NAME = "name"


def read_hdf5_input(file_path):
    """
    Read simulation input from a hdf5 file.

    :param file_path: file path of the hdf5 file.
    :return: :py:`Simulation` object.
    """
    simulation = Simulation()

    with h5py.File(file_path, 'r', driver='core') as hdf5_file:
        simulation.name = extract_basename(file_path)

        simulation_group = hdf5_file[GROUP_SIMULATION]

        if ATTRIBUTE_NAME in simulation_group.attrs:
            simulation.name = simulation_group.attrs[ATTRIBUTE_NAME]
        simulation.version = mcxray.format.hdf5.version.read_from_file(simulation_group)

    return simulation


def read_hdf5_output(file_path):
    """
    Read simulation output from a hdf5 file.

    :param file_path: file path of the hdf5 file.
    :return: :py:`Simulation` object.
    """
    simulation = Simulation()

    with h5py.File(file_path, 'r', driver='core') as hdf5_file:
        simulation.name = extract_basename(file_path)

        simulation_group = hdf5_file[GROUP_SIMULATION]

        if ATTRIBUTE_NAME in simulation_group.attrs:
            simulation.name = simulation_group.attrs[ATTRIBUTE_NAME]
        simulation.version = mcxray.format.hdf5.version.read_from_file(simulation_group)

    return simulation


def write_hdf5_input(simulation, file_path):
    """
    Write simulation input into a hdf5 file.

    :param simulation:
    :param file_path:
    """

    with h5py.File(file_path, 'w', driver='core') as hdf5_file:
        simulation_group = hdf5_file.require_group(GROUP_SIMULATION)

        simulation_group.attrs[ATTRIBUTE_NAME] = simulation.name
        mcxray.format.hdf5.version.write_file(simulation_group, simulation.version)


def write_hdf5_output(simulation, file_path):
    """
    Write simulation output into a hdf5 file.

    :param simulation:
    :param file_path:
    """

    with h5py.File(file_path, 'w', driver='core') as hdf5_file:
        simulation_group = hdf5_file.require_group(GROUP_SIMULATION)

        simulation_group.attrs[ATTRIBUTE_NAME] = simulation.name
        mcxray.format.hdf5.version.write_file(simulation_group, simulation.version)
