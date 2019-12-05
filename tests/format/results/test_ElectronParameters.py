#!/usr/bin/env python
"""
.. py:currentmodule:: format.results.test_ElectronParameters
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for module `ElectronParameters`.
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
import mcxray.format.results.ElectronParameters as ElectronParameters

# Globals and constants variables.

class TestElectronParameters(unittest.TestCase):
    """
    TestCase class for the module `ElectronParameters`.
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

        lines, electronParametersRef = getLinesAndReference()

        electronParameters = ElectronParameters.ElectronParameters()
        electronParameters.readFromLines(lines)

        self.assertEqual(electronParametersRef.numberSimulatedElectrons, electronParameters.numberSimulatedElectrons)
        self.assertEqual(electronParametersRef.meanNumberCollisionPerElectrons, electronParameters.meanNumberCollisionPerElectrons)
        self.assertEqual(electronParametersRef.meanDistanceBetweenCollisions_A, electronParameters.meanDistanceBetweenCollisions_A)
        self.assertEqual(electronParametersRef.meanPolarAngleCollision_deg, electronParameters.meanPolarAngleCollision_deg)
        self.assertEqual(electronParametersRef.meanAzimuthalAngleCollision_deg, electronParameters.meanAzimuthalAngleCollision_deg)
        self.assertEqual(electronParametersRef.backscatteredRatio, electronParameters.backscatteredRatio)
        self.assertEqual(electronParametersRef.internalRatio, electronParameters.internalRatio)
        self.assertEqual(electronParametersRef.throughRatio, electronParameters.throughRatio)
        self.assertEqual(electronParametersRef.skirtRatio, electronParameters.skirtRatio)
        self.assertEqual(electronParametersRef.eRatio, electronParameters.eRatio)

        #self.fail("Test if the testcase is working.")

def getLinesAndReference():
    lines = """Electrons Parameters and Results:
   Total simulated electrons         = 10000
   Mean number of collisions per e   = 935.058100
   Mean distance between collisions  = 17.399915 (A)
   Mean polar angle of collision     = 6.241020 (deg)
   Mean azimuthal angle of collision = 180.012217 (deg)
   Backscattering ratio              = 0.432500
   Internal ratio                    = 0.567400
   Through ratio                     = 0.000000
   Skirt ratio                       = 0.000000
   E_Ratio                           = 0.661328
""".splitlines()

    electronParametersRef = ElectronParameters.ElectronParameters()
    electronParametersRef.numberSimulatedElectrons = 10000
    electronParametersRef.meanNumberCollisionPerElectrons = 935.058100
    electronParametersRef.meanDistanceBetweenCollisions_A = 17.399915
    electronParametersRef.meanPolarAngleCollision_deg = 6.241020
    electronParametersRef.meanAzimuthalAngleCollision_deg = 180.012217
    electronParametersRef.backscatteredRatio = 0.432500
    electronParametersRef.internalRatio = 0.567400
    electronParametersRef.throughRatio = 0.0
    electronParametersRef.skirtRatio = 0.0
    electronParametersRef.eRatio = 0.661328

    return lines, electronParametersRef

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from tests.testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__)
