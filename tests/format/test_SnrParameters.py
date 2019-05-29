#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.format.test_SnrParameters

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module `SnrParameters`.
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
import mcxray.format.SnrParameters as SnrParameters
import tests.format.testUtilities as testUtilities

# Globals and constants variables.


class TestSnrParameters(unittest.TestCase):
    """
    TestCase class for the module `SnrParameters`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

        self.testDataPath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../test_data"))
        self.tempDataPath = testUtilities.createTempDataPath(self.testDataPath)

    def tearDown(self):
        """
        Teardown method.
        """

        unittest.TestCase.tearDown(self)

        testUtilities.removeTempDataPath(self.tempDataPath)

    def testSkeleton(self):
        """
        First test to check if the testcase is working with the testing framework.
        """

        # self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_read(self):
        """
        Tests for method `read`.
        """

        for title in ["BioRitchieNew111017"]:
            snrParameters = SnrParameters.SnrParameters()

            filepath = os.path.abspath(os.path.join(self.testDataPath, "%s/%s.snp" % (title, title)))
            snrParameters.read(filepath)

            snrParametersRef = get_snr_parameters_reference(title)
            self.assertEquals(snrParametersRef.snrType, snrParameters.snrType)
            self.assertEquals(snrParametersRef.energyStart_keV, snrParameters.energyStart_keV)
            self.assertEquals(snrParametersRef.energyEnd_keV, snrParameters.energyEnd_keV)
            self.assertEquals(snrParametersRef.numberEnergySteps, snrParameters.numberEnergySteps)
            self.assertEquals(snrParametersRef.backgroundEnergyWindowsSize, snrParameters.backgroundEnergyWindowsSize)
            self.assertEquals(snrParametersRef.spectrumEnergyWindowsSize, snrParameters.spectrumEnergyWindowsSize)

        # self.fail("Test if the testcase is working.")

    def test__createKeys(self):
        """
        Tests for method `_create_keys`.
        """

        numberKeys = 6

        keys = SnrParameters.SnrParameters()._createKeys()
        self.assertEquals(numberKeys, len(keys))

        # self.fail("Test if the testcase is working.")

    def test_write(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        for title in ["BioRitchieNew111017"]:
            snrParametersRef = get_snr_parameters_reference(title)

            filepathReference = os.path.abspath(os.path.join(self.testDataPath, "%s/%s.snp" % (title, title)))

            filepath = os.path.join(self.tempDataPath, "{}.snp".format(title))
            snrParameters = snrParametersRef

            snrParameters.write(filepath)

            self.assertEquals(snrParametersRef.snrType, snrParameters.snrType)
            self.assertEquals(snrParametersRef.energyStart_keV, snrParameters.energyStart_keV)
            self.assertEquals(snrParametersRef.energyEnd_keV, snrParameters.energyEnd_keV)
            self.assertEquals(snrParametersRef.numberEnergySteps, snrParameters.numberEnergySteps)
            self.assertEquals(snrParametersRef.backgroundEnergyWindowsSize, snrParameters.backgroundEnergyWindowsSize)
            self.assertEquals(snrParametersRef.spectrumEnergyWindowsSize, snrParameters.spectrumEnergyWindowsSize)

            linesRef = open(filepathReference, 'r').readlines()
            lines = open(filepath, 'r').readlines()

            self.assertListEqual(linesRef, lines)

        # self.fail("Test if the testcase is working.")


def get_snr_parameters_reference(title):
    snrParameters = SnrParameters.SnrParameters()

    if title == "BioRitchieNew111017":
        snrParameters.snrType = 0
        snrParameters.energyStart_keV = 1.0
        snrParameters.energyEnd_keV = 20.0
        snrParameters.numberEnergySteps = 100
        snrParameters.backgroundEnergyWindowsSize = 5.0e-3
        snrParameters.spectrumEnergyWindowsSize = 40.0

    return snrParameters
