#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.format.simulation

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`mcxray.format.simulation`.
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
import unittest

# Third party modules.

# Local modules.

# Project modules.

# Globals and constants variables.
from mcxray.format.simulation import Simulation
from mcxray.format.version import VERSION_1_6_7, VERSION_1_7_1, VERSION_2_0_0, VERSION_2_2_0


class TestSimulation(unittest.TestCase):
    """
    TestCase class for the module :py:mod:`mcxray.format.simulation`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

    def tearDown(self):
        """
        Teardown method.
        """

        unittest.TestCase.tearDown(self)

    def testSkeleton(self):
        """
        First test to check if the testcase is working with the testing framework.
        """

        # self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_equality(self):
        """
        Test equality of simulation reference objects.
        """

        self.assertEqual(get_simulation_text_input_ref(), get_simulation_text_input_ref())
        self.assertNotEqual(get_simulation_text_input_ref(), get_simulation_text_output_ref())
        self.assertNotEqual(get_simulation_text_input_ref(), get_simulation_hdf5_input_ref())
        self.assertNotEqual(get_simulation_text_input_ref(), get_simulation_hdf5_output_ref())

        self.assertNotEqual(get_simulation_text_output_ref(), get_simulation_text_input_ref())
        self.assertEqual(get_simulation_text_output_ref(), get_simulation_text_output_ref())
        self.assertNotEqual(get_simulation_text_output_ref(), get_simulation_hdf5_input_ref())
        self.assertNotEqual(get_simulation_text_output_ref(), get_simulation_hdf5_output_ref())

        self.assertNotEqual(get_simulation_hdf5_input_ref(), get_simulation_text_input_ref())
        self.assertNotEqual(get_simulation_hdf5_input_ref(), get_simulation_text_output_ref())
        self.assertEqual(get_simulation_hdf5_input_ref(), get_simulation_hdf5_input_ref())
        self.assertNotEqual(get_simulation_hdf5_input_ref(), get_simulation_hdf5_output_ref())

        self.assertNotEqual(get_simulation_hdf5_output_ref(), get_simulation_text_input_ref())
        self.assertNotEqual(get_simulation_hdf5_output_ref(), get_simulation_text_output_ref())
        self.assertNotEqual(get_simulation_hdf5_output_ref(), get_simulation_hdf5_input_ref())
        self.assertEqual(get_simulation_hdf5_output_ref(), get_simulation_hdf5_output_ref())

        # self.fail("Test if the testcase is working.")
        self.assert_(True)


def get_simulation_text_input_ref():
    simulation = Simulation()

    simulation.name = "CuFeGrainBoundary20kV_5um"
    simulation.version = VERSION_1_6_7

    return simulation


def get_simulation_text_output_ref():
    simulation = Simulation()

    simulation.name = "CuFeGrainBoundary20kV"
    simulation.version = VERSION_1_7_1

    return simulation


def get_simulation_hdf5_input_ref():
    simulation = Simulation()

    simulation.name = "CuFeGrainBoundary20kV_5um"
    simulation.version = VERSION_2_0_0

    return simulation


def get_simulation_hdf5_output_ref():
    simulation = Simulation()

    simulation.name = "CuFeGrainBoundary20kV_5um_results"
    simulation.version = VERSION_2_2_0

    return simulation
