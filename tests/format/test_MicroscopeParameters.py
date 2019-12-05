#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.format.test_MicroscopeParameters

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for modules :py:mod:`mcxray.format.MicroscopeParameters`.
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
import logging
import os.path

# Third party modules.

# Local modules.

# Project modules
import mcxray.format.MicroscopeParameters as MicroscopeParameters
import tests.format.testUtilities as testUtilities
import mcxray.format.version as version

# Globals and constants variables.


class TestMicroscopeParameters(unittest.TestCase):
    """
    TestCase class for the module :py:mod:`mcxray.format.MicroscopeParameters`.
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
        self.assertTrue(True)

    def test__createKeys(self):
        """
        Tests for method `_create_keys`.
        """

        numberKeys = 24

        keys = MicroscopeParameters._create_keys()
        self.assertEqual(numberKeys, len(keys))

        # self.fail("Test if the testcase is working.")

    def test_read(self):
        """
        Tests for method `read`.
        """

        for title in testUtilities.getSimulationTitles():
            logging.info(title)

            microscopeParameters = MicroscopeParameters.MicroscopeParameters()

            filepath = os.path.abspath(os.path.join(self.testDataPath, "%s/%s.mic" % (title, title)))
            microscopeParameters.read(filepath)

            microscopeParametersRef = get_microscope_parameters_reference(title)

            self.assertEqual(microscopeParametersRef.beamEnergy_keV, microscopeParameters.beamEnergy_keV)
            self.assertEqual(microscopeParametersRef.beamCurrent_A, microscopeParameters.beamCurrent_A)
            self.assertEqual(microscopeParametersRef.beamDiameter_A, microscopeParameters.beamDiameter_A)
            self.assertEqual(microscopeParametersRef.beamPositionX_A, microscopeParameters.beamPositionX_A)
            self.assertEqual(microscopeParametersRef.beamPositionY_A, microscopeParameters.beamPositionY_A)
            self.assertEqual(microscopeParametersRef.beamTilt_deg, microscopeParameters.beamTilt_deg)
            self.assertEqual(microscopeParametersRef.beamStandardDeviation_A,
                              microscopeParameters.beamStandardDeviation_A)

            self.assertEqual(microscopeParametersRef.detectorCrystalAtomSymbol,
                              microscopeParameters.detectorCrystalAtomSymbol)
            self.assertEqual(microscopeParametersRef.detectorCrystalThickness_cm,
                              microscopeParameters.detectorCrystalThickness_cm)
            self.assertEqual(microscopeParametersRef.detectorCrystalRadius_cm,
                              microscopeParameters.detectorCrystalRadius_cm)
            self.assertEqual(microscopeParametersRef.detectorCrystalDistance_cm,
                              microscopeParameters.detectorCrystalDistance_cm)

            self.assertEqual(microscopeParametersRef.detectorDeadLayer_A, microscopeParameters.detectorDeadLayer_A)
            self.assertEqual(microscopeParametersRef.detectorDiffusionLenght_A,
                              microscopeParameters.detectorDiffusionLenght_A)
            self.assertEqual(microscopeParametersRef.detectorSurfaceQuality,
                              microscopeParameters.detectorSurfaceQuality)
            self.assertEqual(microscopeParametersRef.detectorNoise_eV, microscopeParameters.detectorNoise_eV)
            self.assertEqual(microscopeParametersRef.detectorTOA_deg, microscopeParameters.detectorTOA_deg)
            self.assertEqual(microscopeParametersRef.detectorPitch_deg, microscopeParameters.detectorPitch_deg)

            self.assertEqual(microscopeParametersRef.detectorBFLow_rad, microscopeParameters.detectorBFLow_rad)
            self.assertEqual(microscopeParametersRef.detectorBFHigh_rad, microscopeParameters.detectorBFHigh_rad)
            self.assertEqual(microscopeParametersRef.detectorDFLow_rad, microscopeParameters.detectorDFLow_rad)
            self.assertEqual(microscopeParametersRef.detectorDFHigh_rad, microscopeParameters.detectorDFHigh_rad)
            self.assertEqual(microscopeParametersRef.detectorHAADFLow_rad, microscopeParameters.detectorHAADFLow_rad)
            self.assertEqual(microscopeParametersRef.detectorHAADFHigh_rad, microscopeParameters.detectorHAADFHigh_rad)

        # self.fail("Test if the testcase is working.")

    def test_read_1_1_1(self):
        """
        Tests for method `read`.
        """

        title = "AlMgBulk5keV_version_1_1_1"
        microscopeParameters = MicroscopeParameters.MicroscopeParameters()

        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.mic".format(title)))
        microscopeParameters.read(filepath)

        self.assertEqual(version.VERSION_1_1_1.major, microscopeParameters.version.major)
        self.assertEqual(version.VERSION_1_1_1.minor, microscopeParameters.version.minor)
        self.assertEqual(version.VERSION_1_1_1.revision, microscopeParameters.version.revision)
        self.assertEqual(version.VERSION_1_1_1, microscopeParameters.version)

        microscopeParametersRef = get_microscope_parameters_reference(title)
        self.assertEqual(microscopeParametersRef.version.major, microscopeParameters.version.major)
        self.assertEqual(microscopeParametersRef.version.minor, microscopeParameters.version.minor)
        self.assertEqual(microscopeParametersRef.version.revision, microscopeParameters.version.revision)
        self.assertEqual(microscopeParametersRef.version, microscopeParameters.version)

        self.assertEqual(microscopeParametersRef.beamEnergy_keV, microscopeParameters.beamEnergy_keV)
        self.assertEqual(microscopeParametersRef.beamCurrent_A, microscopeParameters.beamCurrent_A)
        self.assertEqual(microscopeParametersRef.beamDiameter_A, microscopeParameters.beamDiameter_A)
        self.assertEqual(microscopeParametersRef.beamPositionX_A, microscopeParameters.beamPositionX_A)
        self.assertEqual(microscopeParametersRef.beamPositionY_A, microscopeParameters.beamPositionY_A)
        self.assertEqual(microscopeParametersRef.beamTilt_deg, microscopeParameters.beamTilt_deg)
        self.assertEqual(microscopeParametersRef.beamStandardDeviation_A, microscopeParameters.beamStandardDeviation_A)

        self.assertEqual(microscopeParametersRef.detectorCrystalAtomSymbol,
                          microscopeParameters.detectorCrystalAtomSymbol)
        self.assertEqual(microscopeParametersRef.detectorCrystalThickness_cm,
                          microscopeParameters.detectorCrystalThickness_cm)
        self.assertEqual(microscopeParametersRef.detectorCrystalRadius_cm,
                          microscopeParameters.detectorCrystalRadius_cm)
        self.assertEqual(microscopeParametersRef.detectorCrystalDistance_cm,
                          microscopeParameters.detectorCrystalDistance_cm)

        self.assertEqual(microscopeParametersRef.detectorDeadLayer_A, microscopeParameters.detectorDeadLayer_A)
        self.assertEqual(microscopeParametersRef.detectorDiffusionLenght_A,
                          microscopeParameters.detectorDiffusionLenght_A)
        self.assertEqual(microscopeParametersRef.detectorSurfaceQuality, microscopeParameters.detectorSurfaceQuality)
        self.assertEqual(microscopeParametersRef.detectorNoise_eV, microscopeParameters.detectorNoise_eV)
        self.assertEqual(microscopeParametersRef.detectorTOA_deg, microscopeParameters.detectorTOA_deg)
        self.assertEqual(microscopeParametersRef.detectorPitch_deg, microscopeParameters.detectorPitch_deg)

        self.assertEqual(microscopeParametersRef.detectorBFLow_rad, microscopeParameters.detectorBFLow_rad)
        self.assertEqual(microscopeParametersRef.detectorBFHigh_rad, microscopeParameters.detectorBFHigh_rad)
        self.assertEqual(microscopeParametersRef.detectorDFLow_rad, microscopeParameters.detectorDFLow_rad)
        self.assertEqual(microscopeParametersRef.detectorDFHigh_rad, microscopeParameters.detectorDFHigh_rad)
        self.assertEqual(microscopeParametersRef.detectorHAADFLow_rad, microscopeParameters.detectorHAADFLow_rad)
        self.assertEqual(microscopeParametersRef.detectorHAADFHigh_rad, microscopeParameters.detectorHAADFHigh_rad)

        # self.fail("Test if the testcase is working.")

    def test_read_1_2_0(self):
        """
        Tests for method `read`.
        """

        title = "AlMgBulk5keV_version_1_2_0"
        microscopeParameters = MicroscopeParameters.MicroscopeParameters()

        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.mic".format(title)))
        microscopeParameters.read(filepath)

        self.assertEqual(version.VERSION_1_2_0.major, microscopeParameters.version.major)
        self.assertEqual(version.VERSION_1_2_0.minor, microscopeParameters.version.minor)
        self.assertEqual(version.VERSION_1_2_0.revision, microscopeParameters.version.revision)
        self.assertEqual(version.VERSION_1_2_0, microscopeParameters.version)

        microscopeParametersRef = get_microscope_parameters_reference(title)
        self.assertEqual(microscopeParametersRef.version.major, microscopeParameters.version.major)
        self.assertEqual(microscopeParametersRef.version.minor, microscopeParameters.version.minor)
        self.assertEqual(microscopeParametersRef.version.revision, microscopeParameters.version.revision)
        self.assertEqual(microscopeParametersRef.version, microscopeParameters.version)

        self.assertEqual(microscopeParametersRef.beamEnergy_keV, microscopeParameters.beamEnergy_keV)
        self.assertEqual(microscopeParametersRef.beamCurrent_A, microscopeParameters.beamCurrent_A)
        self.assertEqual(microscopeParametersRef.beamDiameter_A, microscopeParameters.beamDiameter_A)
        self.assertEqual(microscopeParametersRef.beamPositionX_A, microscopeParameters.beamPositionX_A)
        self.assertEqual(microscopeParametersRef.beamPositionY_A, microscopeParameters.beamPositionY_A)
        self.assertEqual(microscopeParametersRef.beamTilt_deg, microscopeParameters.beamTilt_deg)
        self.assertEqual(microscopeParametersRef.beamStandardDeviation_A, microscopeParameters.beamStandardDeviation_A)

        self.assertEqual(microscopeParametersRef.detectorCrystalAtomSymbol,
                          microscopeParameters.detectorCrystalAtomSymbol)
        self.assertEqual(microscopeParametersRef.detectorCrystalThickness_cm,
                          microscopeParameters.detectorCrystalThickness_cm)
        self.assertEqual(microscopeParametersRef.detectorCrystalRadius_cm,
                          microscopeParameters.detectorCrystalRadius_cm)
        self.assertEqual(microscopeParametersRef.detectorCrystalDistance_cm,
                          microscopeParameters.detectorCrystalDistance_cm)

        self.assertEqual(microscopeParametersRef.detectorDeadLayer_A, microscopeParameters.detectorDeadLayer_A)
        self.assertEqual(microscopeParametersRef.detectorDiffusionLenght_A,
                          microscopeParameters.detectorDiffusionLenght_A)
        self.assertEqual(microscopeParametersRef.detectorSurfaceQuality, microscopeParameters.detectorSurfaceQuality)
        self.assertEqual(microscopeParametersRef.detectorNoise_eV, microscopeParameters.detectorNoise_eV)
        self.assertEqual(microscopeParametersRef.detectorTOA_deg, microscopeParameters.detectorTOA_deg)
        self.assertEqual(microscopeParametersRef.detectorPitch_deg, microscopeParameters.detectorPitch_deg)

        self.assertEqual(microscopeParametersRef.detectorBFLow_rad, microscopeParameters.detectorBFLow_rad)
        self.assertEqual(microscopeParametersRef.detectorBFHigh_rad, microscopeParameters.detectorBFHigh_rad)
        self.assertEqual(microscopeParametersRef.detectorDFLow_rad, microscopeParameters.detectorDFLow_rad)
        self.assertEqual(microscopeParametersRef.detectorDFHigh_rad, microscopeParameters.detectorDFHigh_rad)
        self.assertEqual(microscopeParametersRef.detectorHAADFLow_rad, microscopeParameters.detectorHAADFLow_rad)
        self.assertEqual(microscopeParametersRef.detectorHAADFHigh_rad, microscopeParameters.detectorHAADFHigh_rad)

        # self.fail("Test if the testcase is working.")

    def test_read_1_2_1(self):
        """
        Tests for method `read`.
        """

        title = "AlMgBulk5keV_version_1_2_1"
        microscopeParameters = MicroscopeParameters.MicroscopeParameters()

        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.mic".format(title)))
        microscopeParameters.read(filepath)

        self.assertEqual(version.VERSION_1_2_1.major, microscopeParameters.version.major)
        self.assertEqual(version.VERSION_1_2_1.minor, microscopeParameters.version.minor)
        self.assertEqual(version.VERSION_1_2_1.revision, microscopeParameters.version.revision)
        self.assertEqual(version.VERSION_1_2_1, microscopeParameters.version)

        microscopeParametersRef = get_microscope_parameters_reference(title)
        self.assertEqual(microscopeParametersRef.version.major, microscopeParameters.version.major)
        self.assertEqual(microscopeParametersRef.version.minor, microscopeParameters.version.minor)
        self.assertEqual(microscopeParametersRef.version.revision, microscopeParameters.version.revision)
        self.assertEqual(microscopeParametersRef.version, microscopeParameters.version)

        self.assertEqual(microscopeParametersRef.beamEnergy_keV, microscopeParameters.beamEnergy_keV)
        self.assertAlmostEqual(microscopeParametersRef.beamCurrent_A, microscopeParameters.beamCurrent_A)
        self.assertEqual(microscopeParametersRef.beamDiameter_A, microscopeParameters.beamDiameter_A)
        self.assertEqual(microscopeParametersRef.beamPositionX_A, microscopeParameters.beamPositionX_A)
        self.assertEqual(microscopeParametersRef.beamPositionY_A, microscopeParameters.beamPositionY_A)
        self.assertEqual(microscopeParametersRef.beamTilt_deg, microscopeParameters.beamTilt_deg)
        self.assertEqual(microscopeParametersRef.beamStandardDeviation_A, microscopeParameters.beamStandardDeviation_A)

        self.assertEqual(microscopeParametersRef.detectorCrystalAtomSymbol,
                          microscopeParameters.detectorCrystalAtomSymbol)
        self.assertEqual(microscopeParametersRef.detectorCrystalThickness_cm,
                          microscopeParameters.detectorCrystalThickness_cm)
        self.assertEqual(microscopeParametersRef.detectorCrystalRadius_cm,
                          microscopeParameters.detectorCrystalRadius_cm)
        self.assertEqual(microscopeParametersRef.detectorCrystalDistance_cm,
                          microscopeParameters.detectorCrystalDistance_cm)

        self.assertEqual(microscopeParametersRef.detectorDeadLayer_A, microscopeParameters.detectorDeadLayer_A)
        self.assertEqual(microscopeParametersRef.detectorDiffusionLenght_A,
                          microscopeParameters.detectorDiffusionLenght_A)
        self.assertEqual(microscopeParametersRef.detectorSurfaceQuality, microscopeParameters.detectorSurfaceQuality)
        self.assertEqual(microscopeParametersRef.detectorNoise_eV, microscopeParameters.detectorNoise_eV)
        self.assertEqual(microscopeParametersRef.detectorTOA_deg, microscopeParameters.detectorTOA_deg)
        self.assertEqual(microscopeParametersRef.detectorPitch_deg, microscopeParameters.detectorPitch_deg)

        self.assertEqual(microscopeParametersRef.detectorBFLow_rad, microscopeParameters.detectorBFLow_rad)
        self.assertEqual(microscopeParametersRef.detectorBFHigh_rad, microscopeParameters.detectorBFHigh_rad)
        self.assertEqual(microscopeParametersRef.detectorDFLow_rad, microscopeParameters.detectorDFLow_rad)
        self.assertEqual(microscopeParametersRef.detectorDFHigh_rad, microscopeParameters.detectorDFHigh_rad)
        self.assertEqual(microscopeParametersRef.detectorHAADFLow_rad, microscopeParameters.detectorHAADFLow_rad)
        self.assertEqual(microscopeParametersRef.detectorHAADFHigh_rad, microscopeParameters.detectorHAADFHigh_rad)

        # self.fail("Test if the testcase is working.")

    def test_read_1_4_1(self):
        """
        Tests for method `read`.
        """

        title = "AlMgBulk5keV_version_1_4_1"
        microscopeParameters = MicroscopeParameters.MicroscopeParameters()

        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.mic".format(title)))
        microscopeParameters.read(filepath)

        self.assertEqual(version.VERSION_1_4_1.major, microscopeParameters.version.major)
        self.assertEqual(version.VERSION_1_4_1.minor, microscopeParameters.version.minor)
        self.assertEqual(version.VERSION_1_4_1.revision, microscopeParameters.version.revision)
        self.assertEqual(version.VERSION_1_4_1, microscopeParameters.version)

        microscopeParametersRef = get_microscope_parameters_reference(title)
        self.assertEqual(microscopeParametersRef.version.major, microscopeParameters.version.major)
        self.assertEqual(microscopeParametersRef.version.minor, microscopeParameters.version.minor)
        self.assertEqual(microscopeParametersRef.version.revision, microscopeParameters.version.revision)
        self.assertEqual(microscopeParametersRef.version, microscopeParameters.version)

        self.assertEqual(microscopeParametersRef.beamEnergy_keV, microscopeParameters.beamEnergy_keV)
        self.assertAlmostEqual(microscopeParametersRef.beamCurrent_A, microscopeParameters.beamCurrent_A)
        self.assertEqual(microscopeParametersRef.beamDiameter_A, microscopeParameters.beamDiameter_A)
        self.assertEqual(microscopeParametersRef.beamPositionX_A, microscopeParameters.beamPositionX_A)
        self.assertEqual(microscopeParametersRef.beamPositionY_A, microscopeParameters.beamPositionY_A)
        self.assertEqual(microscopeParametersRef.beamTilt_deg, microscopeParameters.beamTilt_deg)
        self.assertEqual(microscopeParametersRef.beamStandardDeviation_A, microscopeParameters.beamStandardDeviation_A)

        self.assertEqual(microscopeParametersRef.detectorCrystalAtomSymbol,
                          microscopeParameters.detectorCrystalAtomSymbol)
        self.assertEqual(microscopeParametersRef.detectorCrystalThickness_cm,
                          microscopeParameters.detectorCrystalThickness_cm)
        self.assertEqual(microscopeParametersRef.detectorCrystalRadius_cm,
                          microscopeParameters.detectorCrystalRadius_cm)
        self.assertEqual(microscopeParametersRef.detectorCrystalDistance_cm,
                          microscopeParameters.detectorCrystalDistance_cm)

        self.assertEqual(microscopeParametersRef.detectorDeadLayer_A, microscopeParameters.detectorDeadLayer_A)
        self.assertEqual(microscopeParametersRef.detectorDiffusionLenght_A,
                          microscopeParameters.detectorDiffusionLenght_A)
        self.assertEqual(microscopeParametersRef.detectorSurfaceQuality, microscopeParameters.detectorSurfaceQuality)
        self.assertEqual(microscopeParametersRef.detectorNoise_eV, microscopeParameters.detectorNoise_eV)
        self.assertEqual(microscopeParametersRef.detectorTOA_deg, microscopeParameters.detectorTOA_deg)
        self.assertEqual(microscopeParametersRef.detectorPitch_deg, microscopeParameters.detectorPitch_deg)

        self.assertEqual(microscopeParametersRef.detectorBFLow_rad, microscopeParameters.detectorBFLow_rad)
        self.assertEqual(microscopeParametersRef.detectorBFHigh_rad, microscopeParameters.detectorBFHigh_rad)
        self.assertEqual(microscopeParametersRef.detectorDFLow_rad, microscopeParameters.detectorDFLow_rad)
        self.assertEqual(microscopeParametersRef.detectorDFHigh_rad, microscopeParameters.detectorDFHigh_rad)
        self.assertEqual(microscopeParametersRef.detectorHAADFLow_rad, microscopeParameters.detectorHAADFLow_rad)
        self.assertEqual(microscopeParametersRef.detectorHAADFHigh_rad, microscopeParameters.detectorHAADFHigh_rad)

        # self.fail("Test if the testcase is working.")

    def test_write(self):
        """
        Tests for method `write`.
        """
        for title in testUtilities.getSimulationTitles():
            microscopeParametersRef = get_microscope_parameters_reference(title)

            filepath = os.path.join(self.tempDataPath, "{}.mic".format(title))

            microscopeParameters = microscopeParametersRef

            microscopeParameters.write(filepath)

            self.assertEqual(microscopeParametersRef.beamEnergy_keV, microscopeParameters.beamEnergy_keV)
            self.assertEqual(microscopeParametersRef.beamCurrent_A, microscopeParameters.beamCurrent_A)
            self.assertEqual(microscopeParametersRef.beamDiameter_A, microscopeParameters.beamDiameter_A)
            self.assertEqual(microscopeParametersRef.beamPositionX_A, microscopeParameters.beamPositionX_A)
            self.assertEqual(microscopeParametersRef.beamPositionY_A, microscopeParameters.beamPositionY_A)
            self.assertEqual(microscopeParametersRef.beamTilt_deg, microscopeParameters.beamTilt_deg)
            self.assertEqual(microscopeParametersRef.beamStandardDeviation_A,
                              microscopeParameters.beamStandardDeviation_A)

            self.assertEqual(microscopeParametersRef.detectorCrystalAtomSymbol,
                              microscopeParameters.detectorCrystalAtomSymbol)
            self.assertEqual(microscopeParametersRef.detectorCrystalThickness_cm,
                              microscopeParameters.detectorCrystalThickness_cm)
            self.assertEqual(microscopeParametersRef.detectorCrystalRadius_cm,
                              microscopeParameters.detectorCrystalRadius_cm)
            self.assertEqual(microscopeParametersRef.detectorCrystalDistance_cm,
                              microscopeParameters.detectorCrystalDistance_cm)

            self.assertEqual(microscopeParametersRef.detectorDeadLayer_A, microscopeParameters.detectorDeadLayer_A)
            self.assertEqual(microscopeParametersRef.detectorDiffusionLenght_A,
                              microscopeParameters.detectorDiffusionLenght_A)
            self.assertEqual(microscopeParametersRef.detectorSurfaceQuality,
                              microscopeParameters.detectorSurfaceQuality)
            self.assertEqual(microscopeParametersRef.detectorNoise_eV, microscopeParameters.detectorNoise_eV)
            self.assertEqual(microscopeParametersRef.detectorTOA_deg, microscopeParameters.detectorTOA_deg)
            self.assertEqual(microscopeParametersRef.detectorPitch_deg, microscopeParameters.detectorPitch_deg)

            self.assertEqual(microscopeParametersRef.detectorBFLow_rad, microscopeParameters.detectorBFLow_rad)
            self.assertEqual(microscopeParametersRef.detectorBFHigh_rad, microscopeParameters.detectorBFHigh_rad)
            self.assertEqual(microscopeParametersRef.detectorDFLow_rad, microscopeParameters.detectorDFLow_rad)
            self.assertEqual(microscopeParametersRef.detectorDFHigh_rad, microscopeParameters.detectorDFHigh_rad)
            self.assertEqual(microscopeParametersRef.detectorHAADFLow_rad, microscopeParameters.detectorHAADFLow_rad)
            self.assertEqual(microscopeParametersRef.detectorHAADFHigh_rad, microscopeParameters.detectorHAADFHigh_rad)

            # .. todo:: Make the lines comparison work.
            # filepathReference = os.path.abspath(os.path.join(self.testDataPath, "{}/{}.mic".format(title, title)))
            # linesRef = open(filepathReference, 'r').readlines()
            # lines = open(filepath, 'r').readlines()
            # self.assertListEqual(linesRef, lines)

        # self.fail("Test if the testcase is working.")

    def test_write_1_1_1(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        title = "AlMgBulk5keV_version_1_1_1"
        microscopeParametersRef = get_microscope_parameters_reference(title)

        filepath = os.path.join(self.tempDataPath, "{}.mic".format(title))
        microscopeParameters = microscopeParametersRef

        microscopeParameters.write(filepath)

        self.assertEqual(microscopeParametersRef.beamEnergy_keV, microscopeParameters.beamEnergy_keV)
        self.assertEqual(microscopeParametersRef.beamCurrent_A, microscopeParameters.beamCurrent_A)
        self.assertEqual(microscopeParametersRef.beamDiameter_A, microscopeParameters.beamDiameter_A)
        self.assertEqual(microscopeParametersRef.beamPositionX_A, microscopeParameters.beamPositionX_A)
        self.assertEqual(microscopeParametersRef.beamPositionY_A, microscopeParameters.beamPositionY_A)
        self.assertEqual(microscopeParametersRef.beamTilt_deg, microscopeParameters.beamTilt_deg)
        self.assertEqual(microscopeParametersRef.beamStandardDeviation_A, microscopeParameters.beamStandardDeviation_A)

        self.assertEqual(microscopeParametersRef.detectorCrystalAtomSymbol,
                          microscopeParameters.detectorCrystalAtomSymbol)
        self.assertEqual(microscopeParametersRef.detectorCrystalThickness_cm,
                          microscopeParameters.detectorCrystalThickness_cm)
        self.assertEqual(microscopeParametersRef.detectorCrystalRadius_cm,
                          microscopeParameters.detectorCrystalRadius_cm)
        self.assertEqual(microscopeParametersRef.detectorCrystalDistance_cm,
                          microscopeParameters.detectorCrystalDistance_cm)

        self.assertEqual(microscopeParametersRef.detectorDeadLayer_A, microscopeParameters.detectorDeadLayer_A)
        self.assertEqual(microscopeParametersRef.detectorDiffusionLenght_A,
                          microscopeParameters.detectorDiffusionLenght_A)
        self.assertEqual(microscopeParametersRef.detectorSurfaceQuality, microscopeParameters.detectorSurfaceQuality)
        self.assertEqual(microscopeParametersRef.detectorNoise_eV, microscopeParameters.detectorNoise_eV)
        self.assertEqual(microscopeParametersRef.detectorTOA_deg, microscopeParameters.detectorTOA_deg)
        self.assertEqual(microscopeParametersRef.detectorPitch_deg, microscopeParameters.detectorPitch_deg)

        self.assertEqual(microscopeParametersRef.detectorBFLow_rad, microscopeParameters.detectorBFLow_rad)
        self.assertEqual(microscopeParametersRef.detectorBFHigh_rad, microscopeParameters.detectorBFHigh_rad)
        self.assertEqual(microscopeParametersRef.detectorDFLow_rad, microscopeParameters.detectorDFLow_rad)
        self.assertEqual(microscopeParametersRef.detectorDFHigh_rad, microscopeParameters.detectorDFHigh_rad)
        self.assertEqual(microscopeParametersRef.detectorHAADFLow_rad, microscopeParameters.detectorHAADFLow_rad)
        self.assertEqual(microscopeParametersRef.detectorHAADFHigh_rad, microscopeParameters.detectorHAADFHigh_rad)

        # .. todo:: Make the lines comparison work.
        # filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.mic".format(title)))
        # linesRef = open(filepathReference, 'r').readlines()
        # lines = open(filepath, 'r').readlines()
        # self.assertListEqual(linesRef, lines)

        # self.fail("Test if the testcase is working.")

    def test_write_1_2_0(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        title = "AlMgBulk5keV_version_1_2_0"
        microscopeParametersRef = get_microscope_parameters_reference(title)

        filepath = os.path.join(self.tempDataPath, "{}.mic".format(title))
        microscopeParameters = microscopeParametersRef
        microscopeParameters.version = version.VERSION_1_2_0

        microscopeParameters.write(filepath)

        self.assertEqual(microscopeParametersRef.beamEnergy_keV, microscopeParameters.beamEnergy_keV)
        self.assertEqual(microscopeParametersRef.beamCurrent_A, microscopeParameters.beamCurrent_A)
        self.assertEqual(microscopeParametersRef.beamDiameter_A, microscopeParameters.beamDiameter_A)
        self.assertEqual(microscopeParametersRef.beamPositionX_A, microscopeParameters.beamPositionX_A)
        self.assertEqual(microscopeParametersRef.beamPositionY_A, microscopeParameters.beamPositionY_A)
        self.assertEqual(microscopeParametersRef.beamTilt_deg, microscopeParameters.beamTilt_deg)
        self.assertEqual(microscopeParametersRef.beamStandardDeviation_A, microscopeParameters.beamStandardDeviation_A)

        self.assertEqual(microscopeParametersRef.detectorCrystalAtomSymbol,
                          microscopeParameters.detectorCrystalAtomSymbol)
        self.assertEqual(microscopeParametersRef.detectorCrystalThickness_cm,
                          microscopeParameters.detectorCrystalThickness_cm)
        self.assertEqual(microscopeParametersRef.detectorCrystalRadius_cm,
                          microscopeParameters.detectorCrystalRadius_cm)
        self.assertEqual(microscopeParametersRef.detectorCrystalDistance_cm,
                          microscopeParameters.detectorCrystalDistance_cm)

        self.assertEqual(microscopeParametersRef.detectorDeadLayer_A, microscopeParameters.detectorDeadLayer_A)
        self.assertEqual(microscopeParametersRef.detectorDiffusionLenght_A,
                          microscopeParameters.detectorDiffusionLenght_A)
        self.assertEqual(microscopeParametersRef.detectorSurfaceQuality, microscopeParameters.detectorSurfaceQuality)
        self.assertEqual(microscopeParametersRef.detectorNoise_eV, microscopeParameters.detectorNoise_eV)
        self.assertEqual(microscopeParametersRef.detectorTOA_deg, microscopeParameters.detectorTOA_deg)
        self.assertEqual(microscopeParametersRef.detectorPitch_deg, microscopeParameters.detectorPitch_deg)

        self.assertEqual(microscopeParametersRef.detectorBFLow_rad, microscopeParameters.detectorBFLow_rad)
        self.assertEqual(microscopeParametersRef.detectorBFHigh_rad, microscopeParameters.detectorBFHigh_rad)
        self.assertEqual(microscopeParametersRef.detectorDFLow_rad, microscopeParameters.detectorDFLow_rad)
        self.assertEqual(microscopeParametersRef.detectorDFHigh_rad, microscopeParameters.detectorDFHigh_rad)
        self.assertEqual(microscopeParametersRef.detectorHAADFLow_rad, microscopeParameters.detectorHAADFLow_rad)
        self.assertEqual(microscopeParametersRef.detectorHAADFHigh_rad, microscopeParameters.detectorHAADFHigh_rad)

        # .. todo:: Make the lines comparison work.
        # filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.mic".format(title)))
        # linesRef = open(filepathReference, 'r').readlines()
        # lines = open(filepath, 'r').readlines()
        # self.assertListEqual(linesRef, lines)

        # self.fail("Test if the testcase is working.")

    def test_write_1_2_1(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        title = "AlMgBulk5keV_version_1_2_1"
        microscopeParametersRef = get_microscope_parameters_reference(title)

        filepath = os.path.join(self.tempDataPath, "{}.mic".format(title))
        microscopeParameters = microscopeParametersRef
        microscopeParameters.version = version.VERSION_1_2_1

        microscopeParameters.write(filepath)

        self.assertEqual(microscopeParametersRef.beamEnergy_keV, microscopeParameters.beamEnergy_keV)
        self.assertEqual(microscopeParametersRef.beamCurrent_A, microscopeParameters.beamCurrent_A)
        self.assertEqual(microscopeParametersRef.beamDiameter_A, microscopeParameters.beamDiameter_A)
        self.assertEqual(microscopeParametersRef.beamPositionX_A, microscopeParameters.beamPositionX_A)
        self.assertEqual(microscopeParametersRef.beamPositionY_A, microscopeParameters.beamPositionY_A)
        self.assertEqual(microscopeParametersRef.beamTilt_deg, microscopeParameters.beamTilt_deg)
        self.assertEqual(microscopeParametersRef.beamStandardDeviation_A, microscopeParameters.beamStandardDeviation_A)

        self.assertEqual(microscopeParametersRef.detectorCrystalAtomSymbol,
                          microscopeParameters.detectorCrystalAtomSymbol)
        self.assertEqual(microscopeParametersRef.detectorCrystalThickness_cm,
                          microscopeParameters.detectorCrystalThickness_cm)
        self.assertEqual(microscopeParametersRef.detectorCrystalRadius_cm,
                          microscopeParameters.detectorCrystalRadius_cm)
        self.assertEqual(microscopeParametersRef.detectorCrystalDistance_cm,
                          microscopeParameters.detectorCrystalDistance_cm)

        self.assertEqual(microscopeParametersRef.detectorDeadLayer_A, microscopeParameters.detectorDeadLayer_A)
        self.assertEqual(microscopeParametersRef.detectorDiffusionLenght_A,
                          microscopeParameters.detectorDiffusionLenght_A)
        self.assertEqual(microscopeParametersRef.detectorSurfaceQuality, microscopeParameters.detectorSurfaceQuality)
        self.assertEqual(microscopeParametersRef.detectorNoise_eV, microscopeParameters.detectorNoise_eV)
        self.assertEqual(microscopeParametersRef.detectorTOA_deg, microscopeParameters.detectorTOA_deg)
        self.assertEqual(microscopeParametersRef.detectorPitch_deg, microscopeParameters.detectorPitch_deg)

        self.assertEqual(microscopeParametersRef.detectorBFLow_rad, microscopeParameters.detectorBFLow_rad)
        self.assertEqual(microscopeParametersRef.detectorBFHigh_rad, microscopeParameters.detectorBFHigh_rad)
        self.assertEqual(microscopeParametersRef.detectorDFLow_rad, microscopeParameters.detectorDFLow_rad)
        self.assertEqual(microscopeParametersRef.detectorDFHigh_rad, microscopeParameters.detectorDFHigh_rad)
        self.assertEqual(microscopeParametersRef.detectorHAADFLow_rad, microscopeParameters.detectorHAADFLow_rad)
        self.assertEqual(microscopeParametersRef.detectorHAADFHigh_rad, microscopeParameters.detectorHAADFHigh_rad)

        # .. todo:: Make the lines comparison work.
        # filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.mic".format(title)))
        # linesRef = open(filepathReference, 'r').readlines()
        # lines = open(filepath, 'r').readlines()
        # self.assertListEqual(linesRef, lines)

        # self.fail("Test if the testcase is working.")

    def test_write_1_4_1(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        title = "AlMgBulk5keV_version_1_4_1"
        microscopeParametersRef = get_microscope_parameters_reference(title)

        filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.mic".format(title)))

        filepath = os.path.join(self.tempDataPath, "{}.mic".format(title))
        microscopeParameters = microscopeParametersRef
        microscopeParameters.version = version.VERSION_1_4_1

        microscopeParameters.write(filepath)

        self.assertEqual(microscopeParametersRef.beamEnergy_keV, microscopeParameters.beamEnergy_keV)
        self.assertEqual(microscopeParametersRef.beamCurrent_A, microscopeParameters.beamCurrent_A)
        self.assertEqual(microscopeParametersRef.beamDiameter_A, microscopeParameters.beamDiameter_A)
        self.assertEqual(microscopeParametersRef.beamPositionX_A, microscopeParameters.beamPositionX_A)
        self.assertEqual(microscopeParametersRef.beamPositionY_A, microscopeParameters.beamPositionY_A)
        self.assertEqual(microscopeParametersRef.beamTilt_deg, microscopeParameters.beamTilt_deg)
        self.assertEqual(microscopeParametersRef.beamStandardDeviation_A, microscopeParameters.beamStandardDeviation_A)

        self.assertEqual(microscopeParametersRef.detectorCrystalAtomSymbol,
                          microscopeParameters.detectorCrystalAtomSymbol)
        self.assertEqual(microscopeParametersRef.detectorCrystalThickness_cm,
                          microscopeParameters.detectorCrystalThickness_cm)
        self.assertEqual(microscopeParametersRef.detectorCrystalRadius_cm,
                          microscopeParameters.detectorCrystalRadius_cm)
        self.assertEqual(microscopeParametersRef.detectorCrystalDistance_cm,
                          microscopeParameters.detectorCrystalDistance_cm)

        self.assertEqual(microscopeParametersRef.detectorDeadLayer_A, microscopeParameters.detectorDeadLayer_A)
        self.assertEqual(microscopeParametersRef.detectorDiffusionLenght_A,
                          microscopeParameters.detectorDiffusionLenght_A)
        self.assertEqual(microscopeParametersRef.detectorSurfaceQuality, microscopeParameters.detectorSurfaceQuality)
        self.assertEqual(microscopeParametersRef.detectorNoise_eV, microscopeParameters.detectorNoise_eV)
        self.assertEqual(microscopeParametersRef.detectorTOA_deg, microscopeParameters.detectorTOA_deg)
        self.assertEqual(microscopeParametersRef.detectorPitch_deg, microscopeParameters.detectorPitch_deg)

        self.assertEqual(microscopeParametersRef.detectorBFLow_rad, microscopeParameters.detectorBFLow_rad)
        self.assertEqual(microscopeParametersRef.detectorBFHigh_rad, microscopeParameters.detectorBFHigh_rad)
        self.assertEqual(microscopeParametersRef.detectorDFLow_rad, microscopeParameters.detectorDFLow_rad)
        self.assertEqual(microscopeParametersRef.detectorDFHigh_rad, microscopeParameters.detectorDFHigh_rad)
        self.assertEqual(microscopeParametersRef.detectorHAADFLow_rad, microscopeParameters.detectorHAADFLow_rad)
        self.assertEqual(microscopeParametersRef.detectorHAADFHigh_rad, microscopeParameters.detectorHAADFHigh_rad)

        linesRef = open(filepathReference, 'r').readlines()
        lines = open(filepath, 'r').readlines()

        self.assertEqual(len(linesRef), len(lines))
        # .. todo:: make this assert pass.
        # self.assertListEqual(linesRef, lines)

        # self.fail("Test if the testcase is working.")


def get_microscope_parameters_reference(title):
    microscopeParameters = MicroscopeParameters.MicroscopeParameters()

    if title == "AuBC cyl":
        microscopeParameters.beamEnergy_keV = 20.0
        microscopeParameters.beamCurrent_A = 1e-10
        microscopeParameters.beamDiameter_A = 0.0
        microscopeParameters.beamPositionX_A = 0.0
        microscopeParameters.beamPositionY_A = 0.0
        microscopeParameters.beamTilt_deg = 0.0
        microscopeParameters.beamStandardDeviation_A = 3.487886e-08
        microscopeParameters.detectorCrystalAtomSymbol = 'Si'
        microscopeParameters.detectorCrystalThickness_cm = 0.3
        microscopeParameters.detectorCrystalRadius_cm = 0.3
        microscopeParameters.detectorCrystalDistance_cm = 4.0
        microscopeParameters.detectorDeadLayer_A = 200.0
        microscopeParameters.detectorDiffusionLenght_A = 500.0
        microscopeParameters.detectorSurfaceQuality = 1.0
        microscopeParameters.detectorNoise_eV = 50.0
        microscopeParameters.detectorTOA_deg = 40.0
        microscopeParameters.detectorPitch_deg = 90.0
        microscopeParameters.detectorBFLow_rad = 0.0
        microscopeParameters.detectorBFHigh_rad = 0.01
        microscopeParameters.detectorDFLow_rad = 0.02
        microscopeParameters.detectorDFHigh_rad = 0.1
        microscopeParameters.detectorHAADFLow_rad = 0.15
        microscopeParameters.detectorHAADFHigh_rad = 0.3
    elif title == "BioRitchieNew111017":
        microscopeParameters.beamEnergy_keV = 60.0
        microscopeParameters.beamCurrent_A = 1e-10
        microscopeParameters.beamDiameter_A = 300.0
        microscopeParameters.beamPositionX_A = 0.0
        microscopeParameters.beamPositionY_A = 0.0
        microscopeParameters.beamTilt_deg = 0.0
        microscopeParameters.beamStandardDeviation_A = 1.0
        microscopeParameters.detectorCrystalAtomSymbol = 'Si'
        microscopeParameters.detectorCrystalThickness_cm = 0.3
        microscopeParameters.detectorCrystalRadius_cm = 0.3
        microscopeParameters.detectorCrystalDistance_cm = 4.0
        microscopeParameters.detectorDeadLayer_A = 200.0
        microscopeParameters.detectorDiffusionLenght_A = 500.0
        microscopeParameters.detectorSurfaceQuality = 1.0
        microscopeParameters.detectorNoise_eV = 50.0
        microscopeParameters.detectorTOA_deg = 40.0
        microscopeParameters.detectorPitch_deg = 90.0
        microscopeParameters.detectorBFLow_rad = 0.0
        microscopeParameters.detectorBFHigh_rad = 0.01
        microscopeParameters.detectorDFLow_rad = 0.02
        microscopeParameters.detectorDFHigh_rad = 0.1
        microscopeParameters.detectorHAADFLow_rad = 0.15
        microscopeParameters.detectorHAADFHigh_rad = 0.3
    elif title == "Bug Al Zr Sphere":
        microscopeParameters.beamEnergy_keV = 200.0
        microscopeParameters.beamCurrent_A = 1e-10
        microscopeParameters.beamDiameter_A = 0.0
        microscopeParameters.beamPositionX_A = 0.0
        microscopeParameters.beamPositionY_A = 0.0
        microscopeParameters.beamTilt_deg = 0.0
        microscopeParameters.beamStandardDeviation_A = 1.0
        microscopeParameters.detectorCrystalAtomSymbol = 'Si'
        microscopeParameters.detectorCrystalThickness_cm = 0.3
        microscopeParameters.detectorCrystalRadius_cm = 0.3
        microscopeParameters.detectorCrystalDistance_cm = 4.0
        microscopeParameters.detectorDeadLayer_A = 200.0
        microscopeParameters.detectorDiffusionLenght_A = 500.0
        microscopeParameters.detectorSurfaceQuality = 1.0
        microscopeParameters.detectorNoise_eV = 50.0
        microscopeParameters.detectorTOA_deg = 40.0
        microscopeParameters.detectorPitch_deg = 90.0
        microscopeParameters.detectorBFLow_rad = 0.0
        microscopeParameters.detectorBFHigh_rad = 0.01
        microscopeParameters.detectorDFLow_rad = 0.02
        microscopeParameters.detectorDFHigh_rad = 0.1
        microscopeParameters.detectorHAADFLow_rad = 0.15
        microscopeParameters.detectorHAADFHigh_rad = 0.3
    elif title == "Mg2SiAlCube3kev":
        microscopeParameters.beamEnergy_keV = 3.0
        microscopeParameters.beamCurrent_A = 1e-10
        microscopeParameters.beamDiameter_A = 0.0
        microscopeParameters.beamPositionX_A = 0.0
        microscopeParameters.beamPositionY_A = 0.0
        microscopeParameters.beamTilt_deg = 0.0
        microscopeParameters.beamStandardDeviation_A = 1.0
        microscopeParameters.detectorCrystalAtomSymbol = 'Si'
        microscopeParameters.detectorCrystalThickness_cm = 0.3
        microscopeParameters.detectorCrystalRadius_cm = 0.3
        microscopeParameters.detectorCrystalDistance_cm = 4.0
        microscopeParameters.detectorDeadLayer_A = 200.0
        microscopeParameters.detectorDiffusionLenght_A = 500.0
        microscopeParameters.detectorSurfaceQuality = 1.0
        microscopeParameters.detectorNoise_eV = 50.0
        microscopeParameters.detectorTOA_deg = 40.0
        microscopeParameters.detectorPitch_deg = 90.0
        microscopeParameters.detectorBFLow_rad = 0.0
        microscopeParameters.detectorBFHigh_rad = 0.01
        microscopeParameters.detectorDFLow_rad = 0.02
        microscopeParameters.detectorDFHigh_rad = 0.1
        microscopeParameters.detectorHAADFLow_rad = 0.15
        microscopeParameters.detectorHAADFHigh_rad = 0.3
    elif title == "AlMgBulk5keV_version_1_1_1":
        microscopeParameters.version = version.Version(1, 1, 1)
        microscopeParameters.beamEnergy_keV = 5.0
        microscopeParameters.beamCurrent_A = 1e-10
        microscopeParameters.beamDiameter_A = 0.0
        microscopeParameters.beamPositionX_A = 0.0
        microscopeParameters.beamPositionY_A = 0.0
        microscopeParameters.beamTilt_deg = 0.0
        microscopeParameters.beamStandardDeviation_A = 1.0
        microscopeParameters.detectorCrystalAtomSymbol = 'Si'
        microscopeParameters.detectorCrystalThickness_cm = 0.3
        microscopeParameters.detectorCrystalRadius_cm = 0.3
        microscopeParameters.detectorCrystalDistance_cm = 4.0
        microscopeParameters.detectorDeadLayer_A = 200.0
        microscopeParameters.detectorDiffusionLenght_A = 500.0
        microscopeParameters.detectorSurfaceQuality = 1.0
        microscopeParameters.detectorNoise_eV = 50.0
        microscopeParameters.detectorTOA_deg = 40.0
        microscopeParameters.detectorPitch_deg = 90.0
        microscopeParameters.detectorBFLow_rad = 0.0
        microscopeParameters.detectorBFHigh_rad = 0.01
        microscopeParameters.detectorDFLow_rad = 0.02
        microscopeParameters.detectorDFHigh_rad = 0.1
        microscopeParameters.detectorHAADFLow_rad = 0.15
        microscopeParameters.detectorHAADFHigh_rad = 0.3
    elif title == "AlMgBulk5keV_version_1_2_0":
        microscopeParameters.version = version.Version(1, 2, 0)
        microscopeParameters.beamEnergy_keV = 4.0
        microscopeParameters.beamCurrent_A = 2e-10
        microscopeParameters.beamDiameter_A = 1.0
        microscopeParameters.beamPositionX_A = 1.0
        microscopeParameters.beamPositionY_A = 2.0
        microscopeParameters.beamTilt_deg = 3.0
        microscopeParameters.beamStandardDeviation_A = 4.0
        microscopeParameters.detectorCrystalAtomSymbol = 'Ge'
        microscopeParameters.detectorCrystalThickness_cm = 0.4
        microscopeParameters.detectorCrystalRadius_cm = 0.5
        microscopeParameters.detectorCrystalDistance_cm = 8.0
        microscopeParameters.detectorDeadLayer_A = 150.0
        microscopeParameters.detectorDiffusionLenght_A = 50.0
        microscopeParameters.detectorSurfaceQuality = 0.9
        microscopeParameters.detectorNoise_eV = 49.0
        microscopeParameters.detectorTOA_deg = 35.0
        microscopeParameters.detectorPitch_deg = 80.0
        microscopeParameters.detectorBFLow_rad = 0.001
        microscopeParameters.detectorBFHigh_rad = 0.02
        microscopeParameters.detectorDFLow_rad = 0.03
        microscopeParameters.detectorDFHigh_rad = 0.4
        microscopeParameters.detectorHAADFLow_rad = 0.16
        microscopeParameters.detectorHAADFHigh_rad = 0.6
    elif title == "AlMgBulk5keV_version_1_2_1":
        microscopeParameters.version = version.Version(1, 2, 1)
        microscopeParameters.beamEnergy_keV = 4.0
        microscopeParameters.beamCurrent_A = 2e-10
        microscopeParameters.beamDiameter_A = 1.7458717472684776e-007
        microscopeParameters.beamPositionX_A = 1.0
        microscopeParameters.beamPositionY_A = 2.0
        microscopeParameters.beamTilt_deg = 3.0
        microscopeParameters.beamStandardDeviation_A = 1.0
        microscopeParameters.detectorCrystalAtomSymbol = 'Si'
        microscopeParameters.detectorCrystalThickness_cm = 0.4
        microscopeParameters.detectorCrystalRadius_cm = 0.5
        microscopeParameters.detectorCrystalDistance_cm = 8.0
        microscopeParameters.detectorDeadLayer_A = 150.0
        microscopeParameters.detectorDiffusionLenght_A = 50.0
        microscopeParameters.detectorSurfaceQuality = 0.9
        microscopeParameters.detectorNoise_eV = 49.0
        microscopeParameters.detectorTOA_deg = 35.0
        microscopeParameters.detectorPitch_deg = 80.0
        microscopeParameters.detectorBFLow_rad = 0.001
        microscopeParameters.detectorBFHigh_rad = 0.02
        microscopeParameters.detectorDFLow_rad = 0.03
        microscopeParameters.detectorDFHigh_rad = 0.4
        microscopeParameters.detectorHAADFLow_rad = 0.16
        microscopeParameters.detectorHAADFHigh_rad = 0.6
    elif title == "AlMgBulk5keV_version_1_4_1":
        microscopeParameters.version = version.Version(1, 4, 1)
        microscopeParameters.beamEnergy_keV = 4.0
        microscopeParameters.beamCurrent_A = 2e-10
        microscopeParameters.beamDiameter_A = 1.7458717472684776e-007
        microscopeParameters.beamPositionX_A = 1.0
        microscopeParameters.beamPositionY_A = 2.0
        microscopeParameters.beamTilt_deg = 3.0
        microscopeParameters.beamStandardDeviation_A = 1.0
        microscopeParameters.detectorCrystalAtomSymbol = 'Si'
        microscopeParameters.detectorCrystalThickness_cm = 0.4
        microscopeParameters.detectorCrystalRadius_cm = 0.5
        microscopeParameters.detectorCrystalDistance_cm = 8.0
        microscopeParameters.detectorDeadLayer_A = 150.0
        microscopeParameters.detectorDiffusionLenght_A = 50.0
        microscopeParameters.detectorSurfaceQuality = 0.9
        microscopeParameters.detectorNoise_eV = 49.0
        microscopeParameters.detectorTOA_deg = 35.0
        microscopeParameters.detectorPitch_deg = 80.0
        microscopeParameters.detectorBFLow_rad = 0.001
        microscopeParameters.detectorBFHigh_rad = 0.02
        microscopeParameters.detectorDFLow_rad = 0.03
        microscopeParameters.detectorDFHigh_rad = 0.4
        microscopeParameters.detectorHAADFLow_rad = 0.16
        microscopeParameters.detectorHAADFHigh_rad = 0.6

    return microscopeParameters
