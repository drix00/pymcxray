#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.test_PhirhozGeneratedCharacteristicThinFilm
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for module `PhirhozGeneratedCharacteristicThinFilm`.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2014 Hendrix Demers"
__license__ = ""##

# Standard library modules.
import unittest
import logging

# Third party modules.

# Local modules.
from pymcxray import get_current_module_path

# Project modules
import pymcxray.FileFormat.Results.PhirhozGeneratedCharacteristicThinFilm as PhirhozGeneratedCharacteristicThinFilm

# Globals and constants variables.

class TestPhirhozGeneratedCharacteristicThinFilm(unittest.TestCase):
    """
    TestCase class for the module `PhirhozGeneratedCharacteristicThinFilm`.
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

    def test_read(self):
        """
        Tests for method `read`.
        """

        phirhozThinFilm = PhirhozGeneratedCharacteristicThinFilm.PhirhozGeneratedCharacteristicThinFilm()
        phirhozThinFilm.path = get_current_module_path(__file__, "../../../test_data/results")
        phirhozThinFilm.basename = "SimulationMCXrayPhirhozTestCases_Cu_E500d0keV_N100000e"

        phirhozThinFilm.read()

        self.assertEquals(1, phirhozThinFilm.numberRegions)

        intensity  = phirhozThinFilm.intensities[0]

        self.assertEquals("0", intensity[PhirhozGeneratedCharacteristicThinFilm.INDEX_REGION])
        self.assertEquals("Cu", intensity[PhirhozGeneratedCharacteristicThinFilm.ATOM_SYMBOL])
        self.assertEquals("390.159", intensity[PhirhozGeneratedCharacteristicThinFilm.SUBSHELL_K])
        self.assertEquals("13367.3", intensity[PhirhozGeneratedCharacteristicThinFilm.SUBSHELL_L])
        self.assertEquals("0", intensity[PhirhozGeneratedCharacteristicThinFilm.SUBSHELL_M])

        #self.fail("Test if the testcase is working.")

    def test_getIntensity(self):
        """
        Tests for method `getIntensity`.
        """

        phirhozThinFilm = PhirhozGeneratedCharacteristicThinFilm.PhirhozGeneratedCharacteristicThinFilm()
        phirhozThinFilm.path = get_current_module_path(__file__, "../../../test_data/results")
        phirhozThinFilm.basename = "SimulationMCXrayPhirhozTestCases_Cu_E500d0keV_N100000e"

        phirhozThinFilm.read()

        self.assertEquals(1, phirhozThinFilm.numberRegions)

        regionID = 0
        atomicSymbol = "Cu"
        intensity = phirhozThinFilm.getIntensity(regionID, atomicSymbol, PhirhozGeneratedCharacteristicThinFilm.SUBSHELL_K)
        self.assertAlmostEquals(390.159, intensity, 6)
        intensity = phirhozThinFilm.getIntensity(regionID, atomicSymbol, PhirhozGeneratedCharacteristicThinFilm.SUBSHELL_L)
        self.assertAlmostEquals(13367.3, intensity, 6)
        intensity = phirhozThinFilm.getIntensity(regionID, atomicSymbol, PhirhozGeneratedCharacteristicThinFilm.SUBSHELL_M)
        self.assertAlmostEquals(0.0, intensity, 6)

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from pymcxray.Testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__)
