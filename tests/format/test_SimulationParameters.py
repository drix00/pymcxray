#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.format.test_SimulationParameters

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for module :py:mod:`mcxray.format.SimulationParameters`.
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
import copy

# Third party modules.

# Local modules.

# Project modules
import mcxray.format.SimulationParameters as SimulationParameters
import tests.format.testUtilities as testUtilities
import mcxray.format.version as version

# Globals and constants variables.


class TestSimulationParameters(unittest.TestCase):
    """
    TestCase class for the module :py:mod:`mcxray.format.SimulationParameters`.
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

        for title in testUtilities.getSimulationTitles():
            simulationParameters = SimulationParameters.SimulationParameters()

            filepath = os.path.abspath(os.path.join(self.testDataPath, "{}/{}.par".format(title, title)))
            simulationParameters.read(filepath)

            simulationParametersRef = get_simulation_parameters_reference(title)
            self.assertEquals(simulationParametersRef.baseFilename, simulationParameters.baseFilename)
            self.assertEquals(simulationParametersRef.numberElectrons, simulationParameters.numberElectrons)
            self.assertEquals(simulationParametersRef.numberPhotons, simulationParameters.numberPhotons)
            self.assertEquals(simulationParametersRef.numberWindows, simulationParameters.numberWindows)
            self.assertEquals(simulationParametersRef.numberFilmsX, simulationParameters.numberFilmsX)
            self.assertEquals(simulationParametersRef.numberFilmsY, simulationParameters.numberFilmsY)
            self.assertEquals(simulationParametersRef.numberFilmsZ, simulationParameters.numberFilmsZ)
            self.assertEquals(simulationParametersRef.numberChannels, simulationParameters.numberChannels)
            self.assertEquals(simulationParametersRef.energyChannelWidth_eV, simulationParameters.energyChannelWidth_eV)
            self.assertEquals(simulationParametersRef.spectrumInterpolationModel,
                              simulationParameters.spectrumInterpolationModel)
            self.assertEquals(simulationParametersRef.voxelSimplification, simulationParameters.voxelSimplification,
                              title)

        # self.fail("Test if the testcase is working.")

    def test_read_1_1_1(self):
        """
        Tests for method `read`.
        """

        simulationParameters = SimulationParameters.SimulationParameters()

        title = "AlMgBulk5keV_version_1_1_1"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.par".format(title)))
        simulationParameters.read(filepath)

        self.assertEquals(version.VERSION_1_1_1.major, simulationParameters.version.major)
        self.assertEquals(version.VERSION_1_1_1.minor, simulationParameters.version.minor)
        self.assertEquals(version.VERSION_1_1_1.revision, simulationParameters.version.revision)
        self.assertEquals(version.VERSION_1_1_1, simulationParameters.version)

        simulationParametersRef = get_simulation_parameters_reference(title)
        self.assertEquals(simulationParametersRef.version.major, simulationParameters.version.major)
        self.assertEquals(simulationParametersRef.version.minor, simulationParameters.version.minor)
        self.assertEquals(simulationParametersRef.version.revision, simulationParameters.version.revision)
        self.assertEquals(simulationParametersRef.version, simulationParameters.version)

        self.assertEquals(simulationParametersRef.baseFilename, simulationParameters.baseFilename)
        self.assertEquals(simulationParametersRef.numberElectrons, simulationParameters.numberElectrons)
        self.assertEquals(simulationParametersRef.numberPhotons, simulationParameters.numberPhotons)
        self.assertEquals(simulationParametersRef.numberWindows, simulationParameters.numberWindows)
        self.assertEquals(simulationParametersRef.numberFilmsX, simulationParameters.numberFilmsX)
        self.assertEquals(simulationParametersRef.numberFilmsY, simulationParameters.numberFilmsY)
        self.assertEquals(simulationParametersRef.numberFilmsZ, simulationParameters.numberFilmsZ)
        self.assertEquals(simulationParametersRef.numberChannels, simulationParameters.numberChannels)
        self.assertEquals(simulationParametersRef.energyChannelWidth_eV, simulationParameters.energyChannelWidth_eV)
        self.assertEquals(simulationParametersRef.spectrumInterpolationModel,
                          simulationParameters.spectrumInterpolationModel)
        self.assertEquals(simulationParametersRef.voxelSimplification, simulationParameters.voxelSimplification, title)

        # self.fail("Test if the testcase is working.")

    def test_read_1_2_0(self):
        """
        Tests for method `read`.
        """

        simulationParameters = SimulationParameters.SimulationParameters()

        title = "AlMgBulk5keV_version_1_2_0"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.par".format(title)))
        simulationParameters.read(filepath)

        self.assertEquals(version.VERSION_1_2_0.major, simulationParameters.version.major)
        self.assertEquals(version.VERSION_1_2_0.minor, simulationParameters.version.minor)
        self.assertEquals(version.VERSION_1_2_0.revision, simulationParameters.version.revision)
        self.assertEquals(version.VERSION_1_2_0, simulationParameters.version)

        simulationParametersRef = get_simulation_parameters_reference(title)
        self.assertEquals(simulationParametersRef.version.major, simulationParameters.version.major)
        self.assertEquals(simulationParametersRef.version.minor, simulationParameters.version.minor)
        self.assertEquals(simulationParametersRef.version.revision, simulationParameters.version.revision)
        self.assertEquals(simulationParametersRef.version, simulationParameters.version)

        self.assertEquals(simulationParametersRef.baseFilename, simulationParameters.baseFilename)
        self.assertEquals(simulationParametersRef.numberElectrons, simulationParameters.numberElectrons)
        self.assertEquals(simulationParametersRef.numberPhotons, simulationParameters.numberPhotons)
        self.assertEquals(simulationParametersRef.numberWindows, simulationParameters.numberWindows)
        self.assertEquals(simulationParametersRef.numberFilmsX, simulationParameters.numberFilmsX)
        self.assertEquals(simulationParametersRef.numberFilmsY, simulationParameters.numberFilmsY)
        self.assertEquals(simulationParametersRef.numberFilmsZ, simulationParameters.numberFilmsZ)
        self.assertEquals(simulationParametersRef.numberChannels, simulationParameters.numberChannels)
        self.assertEquals(simulationParametersRef.energyChannelWidth_eV, simulationParameters.energyChannelWidth_eV)
        self.assertEquals(simulationParametersRef.spectrumInterpolationModel,
                          simulationParameters.spectrumInterpolationModel)
        self.assertEquals(simulationParametersRef.voxelSimplification, simulationParameters.voxelSimplification, title)

        # self.fail("Test if the testcase is working.")

    def test_read_1_2_1(self):
        """
        Tests for method `read`.
        """

        simulationParameters = SimulationParameters.SimulationParameters()

        title = "AlMgBulk5keV_version_1_2_1"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.par".format(title)))
        simulationParameters.read(filepath)

        self.assertEquals(version.VERSION_1_2_1.major, simulationParameters.version.major)
        self.assertEquals(version.VERSION_1_2_1.minor, simulationParameters.version.minor)
        self.assertEquals(version.VERSION_1_2_1.revision, simulationParameters.version.revision)
        self.assertEquals(version.VERSION_1_2_1, simulationParameters.version)

        simulationParametersRef = get_simulation_parameters_reference(title)
        self.assertEquals(simulationParametersRef.version.major, simulationParameters.version.major)
        self.assertEquals(simulationParametersRef.version.minor, simulationParameters.version.minor)
        self.assertEquals(simulationParametersRef.version.revision, simulationParameters.version.revision)
        self.assertEquals(simulationParametersRef.version, simulationParameters.version)

        self.assertEquals(simulationParametersRef.baseFilename, simulationParameters.baseFilename)
        self.assertEquals(simulationParametersRef.numberElectrons, simulationParameters.numberElectrons)
        self.assertEquals(simulationParametersRef.numberPhotons, simulationParameters.numberPhotons)
        self.assertEquals(simulationParametersRef.numberWindows, simulationParameters.numberWindows)
        self.assertEquals(simulationParametersRef.numberFilmsX, simulationParameters.numberFilmsX)
        self.assertEquals(simulationParametersRef.numberFilmsY, simulationParameters.numberFilmsY)
        self.assertEquals(simulationParametersRef.numberFilmsZ, simulationParameters.numberFilmsZ)
        self.assertEquals(simulationParametersRef.numberChannels, simulationParameters.numberChannels)
        self.assertEquals(simulationParametersRef.energyChannelWidth_eV, simulationParameters.energyChannelWidth_eV)
        self.assertEquals(simulationParametersRef.spectrumInterpolationModel,
                          simulationParameters.spectrumInterpolationModel)
        self.assertEquals(simulationParametersRef.voxelSimplification, simulationParameters.voxelSimplification, title)

        # self.fail("Test if the testcase is working.")

    def test_read_1_4_1(self):
        """
        Tests for method `read`.
        """

        simulationParameters = SimulationParameters.SimulationParameters()

        title = "AlMgBulk5keV_version_1_4_1"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.par".format(title)))
        simulationParameters.read(filepath)

        self.assertEquals(version.VERSION_1_4_1.major, simulationParameters.version.major)
        self.assertEquals(version.VERSION_1_4_1.minor, simulationParameters.version.minor)
        self.assertEquals(version.VERSION_1_4_1.revision, simulationParameters.version.revision)
        self.assertEquals(version.VERSION_1_4_1, simulationParameters.version)

        simulationParametersRef = get_simulation_parameters_reference(title)
        self.assertEquals(simulationParametersRef.version.major, simulationParameters.version.major)
        self.assertEquals(simulationParametersRef.version.minor, simulationParameters.version.minor)
        self.assertEquals(simulationParametersRef.version.revision, simulationParameters.version.revision)
        self.assertEquals(simulationParametersRef.version, simulationParameters.version)

        self.assertEquals(simulationParametersRef.baseFilename, simulationParameters.baseFilename)
        self.assertEquals(simulationParametersRef.numberElectrons, simulationParameters.numberElectrons)
        self.assertEquals(simulationParametersRef.numberPhotons, simulationParameters.numberPhotons)
        self.assertEquals(simulationParametersRef.numberWindows, simulationParameters.numberWindows)
        self.assertEquals(simulationParametersRef.numberFilmsX, simulationParameters.numberFilmsX)
        self.assertEquals(simulationParametersRef.numberFilmsY, simulationParameters.numberFilmsY)
        self.assertEquals(simulationParametersRef.numberFilmsZ, simulationParameters.numberFilmsZ)
        self.assertEquals(simulationParametersRef.numberChannels, simulationParameters.numberChannels)
        self.assertEquals(simulationParametersRef.energyChannelWidth_eV, simulationParameters.energyChannelWidth_eV)
        self.assertEquals(simulationParametersRef.spectrumInterpolationModel,
                          simulationParameters.spectrumInterpolationModel)
        self.assertEquals(simulationParametersRef.voxelSimplification, simulationParameters.voxelSimplification, title)

        # self.fail("Test if the testcase is working.")

    def test_read_1_4_4(self):
        """
        Tests for method `read`.
        """

        simulationParameters = SimulationParameters.SimulationParameters()

        title = "AlMgBulk5keV_version_1_4_4"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.par".format(title)))
        simulationParameters.read(filepath)

        self.assertEquals(version.VERSION_1_4_4.major, simulationParameters.version.major)
        self.assertEquals(version.VERSION_1_4_4.minor, simulationParameters.version.minor)
        self.assertEquals(version.VERSION_1_4_4.revision, simulationParameters.version.revision)
        self.assertEquals(version.VERSION_1_4_4, simulationParameters.version)

        simulationParametersRef = get_simulation_parameters_reference(title)
        self.assertEquals(simulationParametersRef.version.major, simulationParameters.version.major)
        self.assertEquals(simulationParametersRef.version.minor, simulationParameters.version.minor)
        self.assertEquals(simulationParametersRef.version.revision, simulationParameters.version.revision)
        self.assertEquals(simulationParametersRef.version, simulationParameters.version)

        self.assertEquals(simulationParametersRef.baseFilename, simulationParameters.baseFilename)
        self.assertEquals(simulationParametersRef.numberElectrons, simulationParameters.numberElectrons)
        self.assertEquals(simulationParametersRef.numberPhotons, simulationParameters.numberPhotons)
        self.assertEquals(simulationParametersRef.numberWindows, simulationParameters.numberWindows)
        self.assertEquals(simulationParametersRef.numberFilmsX, simulationParameters.numberFilmsX)
        self.assertEquals(simulationParametersRef.numberFilmsY, simulationParameters.numberFilmsY)
        self.assertEquals(simulationParametersRef.numberFilmsZ, simulationParameters.numberFilmsZ)
        self.assertEquals(simulationParametersRef.numberChannels, simulationParameters.numberChannels)
        self.assertEquals(simulationParametersRef.energyChannelWidth_eV, simulationParameters.energyChannelWidth_eV)
        self.assertEquals(simulationParametersRef.spectrumInterpolationModel,
                          simulationParameters.spectrumInterpolationModel)
        self.assertEquals(simulationParametersRef.voxelSimplification, simulationParameters.voxelSimplification, title)
        self.assertEquals(simulationParametersRef.elasticCrossSectionScalingFactor,
                          simulationParameters.elasticCrossSectionScalingFactor)
        self.assertEquals(simulationParametersRef.energyLossScalingFactor, simulationParameters.energyLossScalingFactor)

        # self.fail("Test if the testcase is working.")

    def test__createKeys(self):
        """
        Tests for method `_createKeys`.
        """

        simulationParameters = SimulationParameters.SimulationParameters()

        simulationParameters.version = copy.deepcopy(version.VERSION_1_4_3)
        numberKeys = 10
        keys = simulationParameters._createKeys()
        self.assertEquals(numberKeys, len(keys))

        simulationParameters.version = copy.deepcopy(version.VERSION_1_4_4)
        numberKeys = 12
        keys = simulationParameters._createKeys()
        self.assertEquals(numberKeys, len(keys))

        # self.fail("Test if the testcase is working.")

    def test_write(self):
        """
        Tests for method `write`.
        """
        raise unittest.SkipTest("Test test_write not implemented")

        self.maxDiff = None

        for title in testUtilities.getSimulationTitles():
            simulationParametersRef = get_simulation_parameters_reference(title)

            filepathReference = os.path.abspath(os.path.join(self.testDataPath, "%s/%s.par" % (title, title)))

            filepath = os.path.join(self.tempDataPath, "{}.par".format(title))
            simulationParameters = SimulationParameters.SimulationParameters()
            simulationParameters = simulationParametersRef

            simulationParameters.write(filepath)

            self.assertEquals(simulationParametersRef.baseFilename, simulationParameters.baseFilename)
            self.assertEquals(simulationParametersRef.numberElectrons, simulationParameters.numberElectrons)
            self.assertEquals(simulationParametersRef.numberPhotons, simulationParameters.numberPhotons)
            self.assertEquals(simulationParametersRef.numberWindows, simulationParameters.numberWindows)
            self.assertEquals(simulationParametersRef.numberFilmsX, simulationParameters.numberFilmsX)
            self.assertEquals(simulationParametersRef.numberFilmsY, simulationParameters.numberFilmsY)
            self.assertEquals(simulationParametersRef.numberFilmsZ, simulationParameters.numberFilmsZ)
            self.assertEquals(simulationParametersRef.numberChannels, simulationParameters.numberChannels)
            self.assertEquals(simulationParametersRef.energyChannelWidth_eV, simulationParameters.energyChannelWidth_eV)
            self.assertEquals(simulationParametersRef.spectrumInterpolationModel,
                              simulationParameters.spectrumInterpolationModel)
            self.assertEquals(simulationParametersRef.voxelSimplification, simulationParameters.voxelSimplification,
                              title)

            linesRef = open(filepathReference, 'r').readlines()
            lines = open(filepath, 'r').readlines()

            self.assertListEqual(linesRef, lines)

        # self.fail("Test if the testcase is working.")

    def test_write_1_1_1(self):
        """
        Tests for method `write`.
        """
        raise unittest.SkipTest("Test test_write_1_1_1 not implemented")

        self.maxDiff = None

        title = "AlMgBulk5keV_version_1_1_1"
        simulationParametersRef = get_simulation_parameters_reference(title)

        filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.par".format(title)))

        filepath = os.path.join(self.tempDataPath, "{}.par".format(title))
        simulationParameters = simulationParametersRef

        simulationParameters.write(filepath)

        self.assertEquals(simulationParametersRef.baseFilename, simulationParameters.baseFilename)
        self.assertEquals(simulationParametersRef.numberElectrons, simulationParameters.numberElectrons)
        self.assertEquals(simulationParametersRef.numberPhotons, simulationParameters.numberPhotons)
        self.assertEquals(simulationParametersRef.numberWindows, simulationParameters.numberWindows)
        self.assertEquals(simulationParametersRef.numberFilmsX, simulationParameters.numberFilmsX)
        self.assertEquals(simulationParametersRef.numberFilmsY, simulationParameters.numberFilmsY)
        self.assertEquals(simulationParametersRef.numberFilmsZ, simulationParameters.numberFilmsZ)
        self.assertEquals(simulationParametersRef.numberChannels, simulationParameters.numberChannels)
        self.assertEquals(simulationParametersRef.energyChannelWidth_eV, simulationParameters.energyChannelWidth_eV)
        self.assertEquals(simulationParametersRef.spectrumInterpolationModel,
                          simulationParameters.spectrumInterpolationModel)
        self.assertEquals(simulationParametersRef.voxelSimplification, simulationParameters.voxelSimplification, title)

        self.assertEquals(simulationParametersRef.version.major, simulationParameters.version.major)
        self.assertEquals(simulationParametersRef.version.minor, simulationParameters.version.minor)
        self.assertEquals(simulationParametersRef.version.revision, simulationParameters.version.revision)
        self.assertEquals(simulationParametersRef.version, simulationParameters.version)

        linesRef = open(filepathReference, 'r').readlines()
        lines = open(filepath, 'r').readlines()

        self.assertListEqual(linesRef, lines)

        self.fail("Test if the testcase is working.")

    def test_write_1_2_0(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        title = "AlMgBulk5keV_version_1_2_0"
        simulationParametersRef = get_simulation_parameters_reference(title)

        filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.par".format(title)))

        filepath = os.path.join(self.tempDataPath, "{}.par".format(title))
        simulationParameters = simulationParametersRef
        simulationParameters.version = copy.deepcopy(version.VERSION_1_2_0)
        simulationParameters.write(filepath)

        self.assertEquals(simulationParametersRef.baseFilename, simulationParameters.baseFilename)
        self.assertEquals(simulationParametersRef.numberElectrons, simulationParameters.numberElectrons)
        self.assertEquals(simulationParametersRef.numberPhotons, simulationParameters.numberPhotons)
        self.assertEquals(simulationParametersRef.numberWindows, simulationParameters.numberWindows)
        self.assertEquals(simulationParametersRef.numberFilmsX, simulationParameters.numberFilmsX)
        self.assertEquals(simulationParametersRef.numberFilmsY, simulationParameters.numberFilmsY)
        self.assertEquals(simulationParametersRef.numberFilmsZ, simulationParameters.numberFilmsZ)
        self.assertEquals(simulationParametersRef.numberChannels, simulationParameters.numberChannels)
        self.assertEquals(simulationParametersRef.energyChannelWidth_eV, simulationParameters.energyChannelWidth_eV)
        self.assertEquals(simulationParametersRef.spectrumInterpolationModel,
                          simulationParameters.spectrumInterpolationModel)
        self.assertEquals(simulationParametersRef.voxelSimplification, simulationParameters.voxelSimplification, title)

        self.assertEquals(simulationParametersRef.version.major, simulationParameters.version.major)
        self.assertEquals(simulationParametersRef.version.minor, simulationParameters.version.minor)
        self.assertEquals(simulationParametersRef.version.revision, simulationParameters.version.revision)
        self.assertEquals(simulationParametersRef.version, simulationParameters.version)

        linesRef = open(filepathReference, 'r').readlines()
        lines = open(filepath, 'r').readlines()

        self.assertListEqual(linesRef, lines)

        # self.fail("Test if the testcase is working.")

    def test_write_1_2_1(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        title = "AlMgBulk5keV_version_1_2_1"
        simulationParametersRef = get_simulation_parameters_reference(title)

        filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.par".format(title)))

        filepath = os.path.join(self.tempDataPath, "{}.par".format(title))
        simulationParameters = simulationParametersRef
        simulationParameters.version = copy.deepcopy(version.VERSION_1_2_1)

        simulationParameters.write(filepath)

        self.assertEquals(simulationParametersRef.baseFilename, simulationParameters.baseFilename)
        self.assertEquals(simulationParametersRef.numberElectrons, simulationParameters.numberElectrons)
        self.assertEquals(simulationParametersRef.numberPhotons, simulationParameters.numberPhotons)
        self.assertEquals(simulationParametersRef.numberWindows, simulationParameters.numberWindows)
        self.assertEquals(simulationParametersRef.numberFilmsX, simulationParameters.numberFilmsX)
        self.assertEquals(simulationParametersRef.numberFilmsY, simulationParameters.numberFilmsY)
        self.assertEquals(simulationParametersRef.numberFilmsZ, simulationParameters.numberFilmsZ)
        self.assertEquals(simulationParametersRef.numberChannels, simulationParameters.numberChannels)
        self.assertEquals(simulationParametersRef.energyChannelWidth_eV, simulationParameters.energyChannelWidth_eV)
        self.assertEquals(simulationParametersRef.spectrumInterpolationModel,
                          simulationParameters.spectrumInterpolationModel)
        self.assertEquals(simulationParametersRef.voxelSimplification, simulationParameters.voxelSimplification, title)

        self.assertEquals(simulationParametersRef.version.major, simulationParameters.version.major)
        self.assertEquals(simulationParametersRef.version.minor, simulationParameters.version.minor)
        self.assertEquals(simulationParametersRef.version.revision, simulationParameters.version.revision)
        self.assertEquals(simulationParametersRef.version, simulationParameters.version)

        linesRef = open(filepathReference, 'r').readlines()
        lines = open(filepath, 'r').readlines()

        self.assertListEqual(linesRef, lines)

        # self.fail("Test if the testcase is working.")

    def test_write_1_4_1(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        title = "AlMgBulk5keV_version_1_4_1"
        simulationParametersRef = get_simulation_parameters_reference(title)

        filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.par".format(title)))

        filepath = os.path.join(self.tempDataPath, "{}.par".format(title))
        simulationParameters = simulationParametersRef
        simulationParameters.version = copy.deepcopy(version.VERSION_1_4_1)

        simulationParameters.write(filepath)

        self.assertEquals(simulationParametersRef.baseFilename, simulationParameters.baseFilename)
        self.assertEquals(simulationParametersRef.numberElectrons, simulationParameters.numberElectrons)
        self.assertEquals(simulationParametersRef.numberPhotons, simulationParameters.numberPhotons)
        self.assertEquals(simulationParametersRef.numberWindows, simulationParameters.numberWindows)
        self.assertEquals(simulationParametersRef.numberFilmsX, simulationParameters.numberFilmsX)
        self.assertEquals(simulationParametersRef.numberFilmsY, simulationParameters.numberFilmsY)
        self.assertEquals(simulationParametersRef.numberFilmsZ, simulationParameters.numberFilmsZ)
        self.assertEquals(simulationParametersRef.numberChannels, simulationParameters.numberChannels)
        self.assertEquals(simulationParametersRef.energyChannelWidth_eV, simulationParameters.energyChannelWidth_eV)
        self.assertEquals(simulationParametersRef.spectrumInterpolationModel,
                          simulationParameters.spectrumInterpolationModel)
        self.assertEquals(simulationParametersRef.voxelSimplification, simulationParameters.voxelSimplification, title)

        self.assertEquals(simulationParametersRef.version.major, simulationParameters.version.major)
        self.assertEquals(simulationParametersRef.version.minor, simulationParameters.version.minor)
        self.assertEquals(simulationParametersRef.version.revision, simulationParameters.version.revision)
        self.assertEquals(simulationParametersRef.version, simulationParameters.version)

        linesRef = open(filepathReference, 'r').readlines()
        lines = open(filepath, 'r').readlines()

        self.assertListEqual(linesRef, lines)

        # self.fail("Test if the testcase is working.")

    def test_write_1_4_4(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        title = "AlMgBulk5keV_version_1_4_4"
        simulationParametersRef = get_simulation_parameters_reference(title)

        filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.par".format(title)))

        filepath = os.path.join(self.tempDataPath, "{}.par".format(title))
        simulationParameters = simulationParametersRef
        simulationParameters.version = copy.deepcopy(version.VERSION_1_4_4)

        simulationParameters.write(filepath)

        self.assertEquals(simulationParametersRef.baseFilename, simulationParameters.baseFilename)
        self.assertEquals(simulationParametersRef.numberElectrons, simulationParameters.numberElectrons)
        self.assertEquals(simulationParametersRef.numberPhotons, simulationParameters.numberPhotons)
        self.assertEquals(simulationParametersRef.numberWindows, simulationParameters.numberWindows)
        self.assertEquals(simulationParametersRef.numberFilmsX, simulationParameters.numberFilmsX)
        self.assertEquals(simulationParametersRef.numberFilmsY, simulationParameters.numberFilmsY)
        self.assertEquals(simulationParametersRef.numberFilmsZ, simulationParameters.numberFilmsZ)
        self.assertEquals(simulationParametersRef.numberChannels, simulationParameters.numberChannels)
        self.assertEquals(simulationParametersRef.energyChannelWidth_eV, simulationParameters.energyChannelWidth_eV)
        self.assertEquals(simulationParametersRef.spectrumInterpolationModel,
                          simulationParameters.spectrumInterpolationModel)
        self.assertEquals(simulationParametersRef.voxelSimplification, simulationParameters.voxelSimplification, title)
        self.assertEquals(simulationParametersRef.elasticCrossSectionScalingFactor,
                          simulationParameters.elasticCrossSectionScalingFactor)
        self.assertEquals(simulationParametersRef.energyLossScalingFactor, simulationParameters.energyLossScalingFactor)

        self.assertEquals(simulationParametersRef.version.major, simulationParameters.version.major)
        self.assertEquals(simulationParametersRef.version.minor, simulationParameters.version.minor)
        self.assertEquals(simulationParametersRef.version.revision, simulationParameters.version.revision)
        self.assertEquals(simulationParametersRef.version, simulationParameters.version)

        linesRef = open(filepathReference, 'r').readlines()
        lines = open(filepath, 'r').readlines()

        self.assertListEqual(linesRef, lines)

        # self.fail("Test if the testcase is working.")


def get_simulation_parameters_reference(title):
    simulationParameters = SimulationParameters.SimulationParameters()

    if title == "AuBC cyl":
        baseFilenameRef = r"Results\{} Low Count".format(title)
        simulationParameters.baseFilename = baseFilenameRef
        simulationParameters.numberElectrons = 20
        simulationParameters.numberPhotons = 500
        simulationParameters.numberWindows = 32
        simulationParameters.numberFilmsX = 64
        simulationParameters.numberFilmsY = 64
        simulationParameters.numberFilmsZ = 64
        simulationParameters.numberChannels = 1024
        simulationParameters.spectrumInterpolationModel = 2
        simulationParameters.voxelSimplification = None
    elif title == "BioRitchieNew111017":
        baseFilenameRef = r"Results\Ritchie60"
        simulationParameters.baseFilename = baseFilenameRef
        simulationParameters.numberElectrons = 50
        simulationParameters.numberPhotons = 10000
        simulationParameters.numberWindows = 64
        simulationParameters.numberFilmsX = 128
        simulationParameters.numberFilmsY = 128
        simulationParameters.numberFilmsZ = 128
        simulationParameters.numberChannels = 1024
        simulationParameters.spectrumInterpolationModel = 2
        simulationParameters.voxelSimplification = 1
    elif title == "Bug Al Zr Sphere":
        baseFilenameRef = r"Results\McXRay"
        simulationParameters.baseFilename = baseFilenameRef
        simulationParameters.numberElectrons = 1000
        simulationParameters.numberPhotons = 10000
        simulationParameters.numberWindows = 64
        simulationParameters.numberFilmsX = 128
        simulationParameters.numberFilmsY = 128
        simulationParameters.numberFilmsZ = 128
        simulationParameters.numberChannels = 1024
        simulationParameters.spectrumInterpolationModel = 2
        simulationParameters.voxelSimplification = None
    elif title == "Mg2SiAlCube3kev":
        baseFilenameRef = r"Results\{}".format(title)
        simulationParameters.baseFilename = baseFilenameRef
        simulationParameters.numberElectrons = 30
        simulationParameters.numberPhotons = 1000
        simulationParameters.numberWindows = 32
        simulationParameters.numberFilmsX = 64
        simulationParameters.numberFilmsY = 64
        simulationParameters.numberFilmsZ = 64
        simulationParameters.numberChannels = 1024
        simulationParameters.spectrumInterpolationModel = 2
        simulationParameters.voxelSimplification = None
    elif title == "AlMgBulk5keV_version_1_1_1":
        baseFilenameRef = r"Results\{}".format("AlMgBulk5keV")
        simulationParameters.baseFilename = baseFilenameRef
        simulationParameters.version = version.Version(1, 1, 1)
        simulationParameters.numberElectrons = 1000
        simulationParameters.numberPhotons = 127678
        simulationParameters.numberWindows = 64
        simulationParameters.numberFilmsX = 128
        simulationParameters.numberFilmsY = 128
        simulationParameters.numberFilmsZ = 128
        simulationParameters.numberChannels = 1024
        simulationParameters.spectrumInterpolationModel = 2
        simulationParameters.voxelSimplification = None
    elif title == "AlMgBulk5keV_version_1_2_0":
        baseFilenameRef = r"Results\{}".format("AlMgBulk5keV_1_2_0")
        simulationParameters.baseFilename = baseFilenameRef
        simulationParameters.version = version.Version(1, 2, 0)
        simulationParameters.numberElectrons = 10000
        simulationParameters.numberPhotons = 1000
        simulationParameters.numberWindows = 128
        simulationParameters.numberFilmsX = 64
        simulationParameters.numberFilmsY = 66
        simulationParameters.numberFilmsZ = 70
        simulationParameters.energyChannelWidth_eV = 5
        simulationParameters.spectrumInterpolationModel = 1
        simulationParameters.voxelSimplification = None
    elif title == "AlMgBulk5keV_version_1_2_1":
        baseFilenameRef = r"Results\{}".format("AlMgBulk5keV_1_2_1")
        simulationParameters.baseFilename = baseFilenameRef
        simulationParameters.version = version.Version(1, 2, 1)
        simulationParameters.numberElectrons = 10000
        simulationParameters.numberPhotons = 1000
        simulationParameters.numberWindows = 128
        simulationParameters.numberFilmsX = 64
        simulationParameters.numberFilmsY = 66
        simulationParameters.numberFilmsZ = 70
        simulationParameters.energyChannelWidth_eV = 5
        simulationParameters.spectrumInterpolationModel = 1
        simulationParameters.voxelSimplification = None
    elif title == "AlMgBulk5keV_version_1_4_1":
        baseFilenameRef = r"Results\{}".format("AlMgBulk5keV_1_4_1")
        simulationParameters.baseFilename = baseFilenameRef
        simulationParameters.version = version.Version(1, 4, 1)
        simulationParameters.numberElectrons = 10000
        simulationParameters.numberPhotons = 1000
        simulationParameters.numberWindows = 128
        simulationParameters.numberFilmsX = 64
        simulationParameters.numberFilmsY = 66
        simulationParameters.numberFilmsZ = 70
        simulationParameters.energyChannelWidth_eV = 5
        simulationParameters.spectrumInterpolationModel = 1
        simulationParameters.voxelSimplification = None
    elif title == "AlMgBulk5keV_version_1_4_4":
        baseFilenameRef = r"Results\{}".format("AlMgBulk5keV_1_4_4")
        simulationParameters.baseFilename = baseFilenameRef
        simulationParameters.version = version.Version(1, 4, 4)
        simulationParameters.numberElectrons = 10000
        simulationParameters.numberPhotons = 1000
        simulationParameters.numberWindows = 128
        simulationParameters.numberFilmsX = 64
        simulationParameters.numberFilmsY = 66
        simulationParameters.numberFilmsZ = 70
        simulationParameters.energyChannelWidth_eV = 5
        simulationParameters.spectrumInterpolationModel = 1
        simulationParameters.voxelSimplification = None
        simulationParameters.elasticCrossSectionScalingFactor = 1.3
        simulationParameters.energyLossScalingFactor = 0.7

    return simulationParameters
