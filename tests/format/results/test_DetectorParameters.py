#!/usr/bin/env python
"""
.. py:currentmodule:: format.results.test_DetectorParameters
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for module `DetectorParameters`.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2012 Hendrix Demers"
__license__ = ""

# Subversion informations for the file.
__svnRevision__ = "$Revision$"
__svnDate__ = "$Date$"
__svnId__ = "$Id$"

# Standard library modules.
import unittest
import logging

# Third party modules.

# Local modules.

# Project modules
import mcxray.format.results.DetectorParameters as DetectorParameters

# Globals and constants variables.

class TestDetectorParameters(unittest.TestCase):
    """
    TestCase class for the module `DetectorParameters`.
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

        #self.fail("Test if the testcase is working.")
        self.assertTrue(True)

    def test_readFromLines(self):
        """
        Tests for method `readFromLines`.
        """

        lines, detectorParametersRef = self._getLinesAndReference()

        detectorParameters = DetectorParameters.DetectorParameters()
        detectorParameters.readFromLines(lines)

        self.assertEqual(detectorParametersRef.crystalName, detectorParameters.crystalName)
        self.assertAlmostEqual(detectorParametersRef.crystalDensity_g_cm3, detectorParameters.crystalDensity_g_cm3)
        self.assertAlmostEqual(detectorParametersRef.crystalThickness_cm, detectorParameters.crystalThickness_cm)
        self.assertAlmostEqual(detectorParametersRef.crystalRadius_cm, detectorParameters.crystalRadius_cm)
        self.assertAlmostEqual(detectorParametersRef.beamDetectorDistance_cm, detectorParameters.beamDetectorDistance_cm)
        self.assertAlmostEqual(detectorParametersRef.deadLayerThickness_A, detectorParameters.deadLayerThickness_A)
        self.assertAlmostEqual(detectorParametersRef.diffusionLength_A, detectorParameters.diffusionLength_A)
        self.assertAlmostEqual(detectorParametersRef.surfaceQualityFactor, detectorParameters.surfaceQualityFactor)
        self.assertAlmostEqual(detectorParametersRef.noiseEdsDetector_eV, detectorParameters.noiseEdsDetector_eV)
        self.assertAlmostEqual(detectorParametersRef.thicknessBeWindow_um, detectorParameters.thicknessBeWindow_um)
        self.assertAlmostEqual(detectorParametersRef.thicknessAlWindow_um, detectorParameters.thicknessAlWindow_um)
        self.assertAlmostEqual(detectorParametersRef.thicknessTiWindow_um, detectorParameters.thicknessTiWindow_um)
        self.assertAlmostEqual(detectorParametersRef.thicknessOil_um, detectorParameters.thicknessOil_um)
        self.assertAlmostEqual(detectorParametersRef.thicknessH2O_um, detectorParameters.thicknessH2O_um)
        self.assertAlmostEqual(detectorParametersRef.thicknessMoxtek_um, detectorParameters.thicknessMoxtek_um)
        self.assertAlmostEqual(detectorParametersRef.thicknessAir_um, detectorParameters.thicknessAir_um)
        self.assertAlmostEqual(detectorParametersRef.angleBetweenDetectorSpecimenNormal_deg, detectorParameters.angleBetweenDetectorSpecimenNormal_deg)
        self.assertAlmostEqual(detectorParametersRef.angleBetweenDetectorXAxis_deg, detectorParameters.angleBetweenDetectorXAxis_deg)
        self.assertAlmostEqual(detectorParametersRef.takeoffAngleNormalIncidence_deg, detectorParameters.takeoffAngleNormalIncidence_deg)
        self.assertAlmostEqual(detectorParametersRef.takeoffAngleEffective_deg, detectorParameters.takeoffAngleEffective_deg)
        self.assertAlmostEqual(detectorParametersRef.solidAngle_deg, detectorParameters.solidAngle_deg)

        #self.fail("Test if the testcase is working.")

    def _getLinesAndReference(self):
        lines = """Detector Parameters:
   Detector crystal is          Silicium
   Crystal density            = 2.330000 (g/cm3)
   Crystal thichness          = 30000000.000000 (cm)
   Crystal radius             = 300000000.000000 (cm)
   Distance beam-detector     = 400000000.000000 (cm)
   Dead layer                 = 200.000000 (A)
   Diffusion length           = 0.500000 (A)
   Surface quality factor     = 1.000000
   Noise at EDS detector      = 50.000000 (eV)
   Thickness of Be window     = 0.000000 (um)
   Thickness of Al window     = 0.000000 (um)
   Thickness of Ti window     = 0.000000 (um)
   Thickness of Oil           = 0.000000 (um)
   Thickness of H2O           = 0.000000 (um)
   Thickness of Moxtek        = 0.300000 (um)
   Thickness of air path      = 0.000000 (cm)
   Angle between detector axis and specimen normal    = 50.000000 (deg)
   Angle between detector and x axis on the X-Y plane = 90.000000 (deg)
   Take Off Angle at Normal Incidence                 = 40.000000 (deg)
   Effective Take Off Angle                           = 40.000000 (deg)
   Solid angle of the detector                        = 0.001400 (deg)
   """.splitlines()

        detectorParametersRef = DetectorParameters.DetectorParameters()
        detectorParametersRef.crystalName = "Silicium"
        detectorParametersRef.crystalDensity_g_cm3 = 2.33
        detectorParametersRef.crystalThickness_cm = 30000000.0
        detectorParametersRef.crystalRadius_cm = 300000000.0
        detectorParametersRef.beamDetectorDistance_cm = 400000000.0
        detectorParametersRef.deadLayerThickness_A = 200.0
        detectorParametersRef.diffusionLength_A = 0.5
        detectorParametersRef.surfaceQualityFactor = 1.0
        detectorParametersRef.noiseEdsDetector_eV = 50.0
        detectorParametersRef.thicknessBeWindow_um = 0.0
        detectorParametersRef.thicknessAlWindow_um = 0.0
        detectorParametersRef.thicknessTiWindow_um = 0.0
        detectorParametersRef.thicknessOil_um = 0.0
        detectorParametersRef.thicknessH2O_um = 0.0
        detectorParametersRef.thicknessMoxtek_um = 0.3
        detectorParametersRef.thicknessAir_um = 0.0
        detectorParametersRef.angleBetweenDetectorSpecimenNormal_deg = 50.0
        detectorParametersRef.angleBetweenDetectorXAxis_deg = 90.0
        detectorParametersRef.takeoffAngleNormalIncidence_deg = 40.0
        detectorParametersRef.takeoffAngleEffective_deg = 40.0
        detectorParametersRef.solidAngle_deg = 0.0014

        return lines, detectorParametersRef

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from tests.testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__)
