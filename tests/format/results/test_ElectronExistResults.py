#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.format.results.test_ElectronExistResults

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`mcxray.format.results.ElectronExistResults`.
"""

###############################################################################
# Copyright 2019 Hendrix Demers
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
import os.path

# Third party modules.

# Local modules.

# Project modules
import mcxray.format.results.ElectronExistResults as ElectronExistResults

# Globals and constants variables.


class TestElectronExistResults(unittest.TestCase):
    """
    TestCase class for the module :py:mod:`mcxray.format.results.ElectronExistResults`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

        # SimulationBseReciprocity_Ag_E1d0keV_N10000e_dB1d0nm_tB15d0deg_ElectronExitResults.csv
        self.testDataPath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../test_data"))

        basename = "SimulationBseReciprocity_Ag_E1d0keV_N10000e_dB1d0nm_tB15d0deg"
        self.results = ElectronExistResults.ElectronExistResults(path=os.path.join(self.testDataPath, "results"),
                                                                 basename=basename)

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
        self.assertTrue(True)

    def test_dataFileExist(self):
        """
        First test to check if the testcase is working with the testing framework.
        """

        results = ElectronExistResults.ElectronExistResults()
        results.path = os.path.join(self.testDataPath, "results")
        results.basename = "SimulationBseReciprocity_Ag_E1d0keV_N10000e_dB1d0nm_tB15d0deg"

        self.assertTrue(os.path.isfile(results.filepath))

        self.assertTrue(os.path.isfile(self.results.filepath))

        # self.fail("Test if the testcase is working.")
        self.assertTrue(True)

    def test_read(self):
        """
        Tests for method `read`.
        """

        self.assertEqual(0, self.results.numberData)
        self.results.read()
        self.assertEqual(4036, self.results.numberData)

        # self.fail("Test if the testcase is working.")

    def test_energyDistribution(self):
        """
        Tests for method `energyDistribution`.

        .. todo:: Replace scipy.stats.histogram with numpy method.
        """
        energies_keV, histogram = self.results.getEnergyDistribution()

        self.assertEqual(10, len(energies_keV))
        self.assertEqual(10, len(histogram))

        self.assertAlmostEqual(0.0505063517, energies_keV[0])
        self.assertAlmostEqual(0.15039168310000001, energies_keV[1])
        self.assertAlmostEqual(0.94947433429999994, energies_keV[-1])

        self.assertEqual(123, histogram[0])
        self.assertEqual(897, histogram[-1])

        energies_keV, histogram = self.results.getEnergyDistribution(numberBins=20)

        self.assertEqual(20, len(energies_keV))
        self.assertEqual(20, len(histogram))

        self.assertAlmostEqual(0.025535018850000001, energies_keV[0])
        self.assertAlmostEqual(0.075477684550000007, energies_keV[1])
        self.assertAlmostEqual(0.97444566715000003, energies_keV[-1])

        self.assertEqual(67, histogram[0])
        self.assertEqual(461, histogram[-1])

        # self.fail("Test if the testcase is working.")