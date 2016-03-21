#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.test_BeamParameters
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for module `BeamParameters`.
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
import pymcxray.FileFormat.Results.BeamParameters as BeamParameters

# Globals and constants variables.

class TestBeamParameters(unittest.TestCase):
    """
    TestCase class for the module `BeamParameters`.
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
        self.assert_(True)

    def test_readFromLines(self):
        """
        Tests for method `readFromLines`.
        """

        lines, beamParametersRef = self._getLinesAndReference()

        beamParameters = BeamParameters.BeamParameters()
        beamParameters.readFromLines(lines)

        self.assertAlmostEquals(beamParametersRef.incidentEnergy_keV, beamParameters.incidentEnergy_keV)
        self.assertAlmostEquals(beamParametersRef.current_A, beamParameters.current_A)
        self.assertAlmostEquals(beamParametersRef.acquisitionTime_s, beamParameters.acquisitionTime_s)
        self.assertAlmostEquals(beamParametersRef.diameter90_A, beamParameters.diameter90_A)
        self.assertAlmostEquals(beamParametersRef.tiltAngle_deg, beamParameters.tiltAngle_deg)
        self.assertAlmostEquals(beamParametersRef.gaussianMean, beamParameters.gaussianMean)
        self.assertAlmostEquals(beamParametersRef.gaussianSigma, beamParameters.gaussianSigma)

        #self.fail("Test if the testcase is working.")

    def _getLinesAndReference(self):
        lines = """Beam Parameters:
   Electron incident energy           = 30.000000 (KeV)
   Beam Current                       = 1.000000e-010 (A)
   Acquisition Time                   = 100.000000 (s)
   Diameter with 90% of the electrons = 0.000000 (A)
   Tilt angle                         = 0.000000 (deg)
   Gaussian Mean                      = 0.000000
   Gaussian Sigma                     = 0.000000
   The negative Z axis is the e Beam axis
   A positive tilt angle gives a negative projection on X Axis
   The Y axis is the rotation axis
   """.splitlines()

        beamParametersRef = BeamParameters.BeamParameters()
        beamParametersRef.incidentEnergy_keV = 30.0
        beamParametersRef.current_A = 1.0e-10
        beamParametersRef.acquisitionTime_s = 100.0
        beamParametersRef.diameter90_A = 0.0
        beamParametersRef.tiltAngle_deg = 0.0
        beamParametersRef.gaussianMean = 0.0
        beamParametersRef.gaussianSigma = 0.0

        return lines, beamParametersRef

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from pymcxray.Testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__)
