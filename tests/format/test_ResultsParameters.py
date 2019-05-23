#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.format.test_ResultsParameters

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for module :py:mod:`mcxray.format.ResultsParameters`.
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
import mcxray.format.ResultsParameters as ResultsParameters
import tests.format.testUtilities as testUtilities
import mcxray.format.version as version

# Globals and constants variables.


class TestResultsParameters(unittest.TestCase):
    """
    TestCase class for the module :py:mod:`mcxray.format.ResultsParameters`.
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
        raise unittest.SkipTest("Test test_read not implemented")

        for title in testUtilities.getSimulationTitles():
            resultsParameters = ResultsParameters.ResultsParameters()

            filepath = os.path.abspath(os.path.join(self.testDataPath, "{}/{}.rp".format(title, title)))
            resultsParameters.read(filepath)

            resultsParametersRef = get_simulation_parameters_reference(title)
            self.assertEquals(resultsParametersRef.isComputeXrayCharacteristic,
                              resultsParameters.isComputeXrayCharacteristic)
            self.assertEquals(resultsParametersRef.isComputeXrayBremsstrahlung,
                              resultsParameters.isComputeXrayBremsstrahlung)
            self.assertEquals(resultsParametersRef.isComputeXrayPhirhoz, resultsParameters.isComputeXrayPhirhoz)

        self.fail("Test if the testcase is working.")

    def test_read_1_4_1(self):
        """
        Tests for method `read`.
        """

        resultsParameters = ResultsParameters.ResultsParameters()

        title = "AlMgBulk5keV_version_1_4_1"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.rp".format(title)))
        resultsParameters.read(filepath)

        self.assertEquals(version.VERSION_1_4_1.major, resultsParameters.version.major)
        self.assertEquals(version.VERSION_1_4_1.minor, resultsParameters.version.minor)
        self.assertEquals(version.VERSION_1_4_1.revision, resultsParameters.version.revision)
        self.assertEquals(version.VERSION_1_4_1, resultsParameters.version)

        resultsParametersRef = get_simulation_parameters_reference(title)
        self.assertEquals(resultsParametersRef.version.major, resultsParameters.version.major)
        self.assertEquals(resultsParametersRef.version.minor, resultsParameters.version.minor)
        self.assertEquals(resultsParametersRef.version.revision, resultsParameters.version.revision)
        self.assertEquals(resultsParametersRef.version, resultsParameters.version)

        self.assertEquals(resultsParametersRef.isComputeXrayCharacteristic,
                          resultsParameters.isComputeXrayCharacteristic)
        self.assertEquals(resultsParametersRef.isComputeXrayBremsstrahlung,
                          resultsParameters.isComputeXrayBremsstrahlung)
        self.assertEquals(resultsParametersRef.isComputeXrayPhirhoz, resultsParameters.isComputeXrayPhirhoz)

        # self.fail("Test if the testcase is working.")

    def test_read_1_4_3(self):
        """
        Tests for method `read`.
        """

        resultsParameters = ResultsParameters.ResultsParameters()

        title = "AlMgBulk5keV_version_1_4_3"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.rp".format(title)))
        resultsParameters.read(filepath)

        self.assertEquals(version.VERSION_1_4_3.major, resultsParameters.version.major)
        self.assertEquals(version.VERSION_1_4_3.minor, resultsParameters.version.minor)
        self.assertEquals(version.VERSION_1_4_3.revision, resultsParameters.version.revision)
        self.assertEquals(version.VERSION_1_4_3, resultsParameters.version)

        resultsParametersRef = get_simulation_parameters_reference(title)
        self.assertEquals(resultsParametersRef.version.major, resultsParameters.version.major)
        self.assertEquals(resultsParametersRef.version.minor, resultsParameters.version.minor)
        self.assertEquals(resultsParametersRef.version.revision, resultsParameters.version.revision)
        self.assertEquals(resultsParametersRef.version, resultsParameters.version)

        self.assertEquals(resultsParametersRef.isComputeXrayCharacteristic,
                          resultsParameters.isComputeXrayCharacteristic)
        self.assertEquals(resultsParametersRef.isComputeXrayBremsstrahlung,
                          resultsParameters.isComputeXrayBremsstrahlung)
        self.assertEquals(resultsParametersRef.isComputeXrayPhirhoz, resultsParameters.isComputeXrayPhirhoz)
        self.assertEquals(resultsParametersRef.isComputeXraySimulatedSpectrum,
                          resultsParameters.isComputeXraySimulatedSpectrum)

        # self.fail("Test if the testcase is working.")

    def test_write(self):
        """
        Tests for method `write`.
        """
        raise unittest.SkipTest("Test test_write not implemented")

        self.maxDiff = None

        for title in testUtilities.getSimulationTitles():
            resultsParametersRef = get_simulation_parameters_reference(title)

            filepathReference = os.path.abspath(os.path.join(self.testDataPath, "{}/{}.rp".format(title, title)))

            filepath = os.path.join(self.tempDataPath, "{}.rp".format(title))
            # resultsParameters = ResultsParameters.ResultsParameters()
            resultsParameters = resultsParametersRef

            resultsParameters.write(filepath)

            self.assertEquals(resultsParametersRef.isComputeXrayCharacteristic,
                              resultsParameters.isComputeXrayCharacteristic)
            self.assertEquals(resultsParametersRef.isComputeXrayBremsstrahlung,
                              resultsParameters.isComputeXrayBremsstrahlung)
            self.assertEquals(resultsParametersRef.isComputeXrayPhirhoz, resultsParameters.isComputeXrayPhirhoz)

            linesRef = open(filepathReference, 'r').readlines()
            lines = open(filepath, 'r').readlines()

            self.assertListEqual(linesRef, lines)

        self.fail("Test if the testcase is working.")

    def test_write_1_4_1(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        title = "AlMgBulk5keV_version_1_4_1"
        resultsParametersRef = get_simulation_parameters_reference(title)

        filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.rp".format(title)))

        filepath = os.path.join(self.tempDataPath, "{}.rp".format(title))
        resultsParameters = resultsParametersRef
        resultsParameters.version = version.VERSION_1_4_1

        resultsParameters.write(filepath)

        self.assertEquals(resultsParametersRef.isComputeXrayCharacteristic,
                          resultsParameters.isComputeXrayCharacteristic)
        self.assertEquals(resultsParametersRef.isComputeXrayBremsstrahlung,
                          resultsParameters.isComputeXrayBremsstrahlung)
        self.assertEquals(resultsParametersRef.isComputeXrayPhirhoz, resultsParameters.isComputeXrayPhirhoz)

        self.assertEquals(resultsParametersRef.version.major, resultsParameters.version.major)
        self.assertEquals(resultsParametersRef.version.minor, resultsParameters.version.minor)
        self.assertEquals(resultsParametersRef.version.revision, resultsParameters.version.revision)
        self.assertEquals(resultsParametersRef.version, resultsParameters.version)

        linesRef = open(filepathReference, 'r').readlines()
        lines = open(filepath, 'r').readlines()

        self.assertListEqual(linesRef, lines)

        # self.fail("Test if the testcase is working.")

    def test_write_1_4_3(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        title = "AlMgBulk5keV_version_1_4_3"
        resultsParametersRef = get_simulation_parameters_reference(title)

        filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.rp".format(title)))

        filepath = os.path.join(self.tempDataPath, "{}.rp".format(title))
        resultsParameters = resultsParametersRef
        resultsParameters.version = version.VERSION_1_4_3

        resultsParameters.write(filepath)

        self.assertEquals(resultsParametersRef.isComputeXrayCharacteristic,
                          resultsParameters.isComputeXrayCharacteristic)
        self.assertEquals(resultsParametersRef.isComputeXrayBremsstrahlung,
                          resultsParameters.isComputeXrayBremsstrahlung)
        self.assertEquals(resultsParametersRef.isComputeXrayPhirhoz, resultsParameters.isComputeXrayPhirhoz)
        self.assertEquals(resultsParametersRef.isComputeXraySimulatedSpectrum,
                          resultsParameters.isComputeXraySimulatedSpectrum)

        self.assertEquals(resultsParametersRef.version.major, resultsParameters.version.major)
        self.assertEquals(resultsParametersRef.version.minor, resultsParameters.version.minor)
        self.assertEquals(resultsParametersRef.version.revision, resultsParameters.version.revision)
        self.assertEquals(resultsParametersRef.version, resultsParameters.version)

        linesRef = open(filepathReference, 'r').readlines()
        lines = open(filepath, 'r').readlines()

        self.assertListEqual(linesRef, lines)

        # self.fail("Test if the testcase is working.")


def get_simulation_parameters_reference(title):
    resultsParameters = ResultsParameters.ResultsParameters()

    if title == "AlMgBulk5keV_version_1_2_1":
        resultsParameters.version = version.Version(1, 2, 1)
        resultsParameters.isComputeXrayCharacteristic = None
        resultsParameters.isComputeXrayBremsstrahlung = None
        resultsParameters.isComputeXrayPhirhoz = None
    elif title == "AlMgBulk5keV_version_1_4_1":
        resultsParameters.version = version.Version(1, 4, 1)
        resultsParameters.isComputeXrayCharacteristic = True
        resultsParameters.isComputeXrayBremsstrahlung = True
        resultsParameters.isComputeXrayPhirhoz = True
    elif title == "AlMgBulk5keV_version_1_4_3":
        resultsParameters.version = version.Version(1, 4, 3)
        resultsParameters.isComputeXrayCharacteristic = True
        resultsParameters.isComputeXrayBremsstrahlung = False
        resultsParameters.isComputeXrayPhirhoz = False
        resultsParameters.isComputeXraySimulatedSpectrum = False

    return resultsParameters
