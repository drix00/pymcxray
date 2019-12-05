#!/usr/bin/env python
"""
.. py:currentmodule:: format.results.test_PhirhozGeneratedCharacteristicThinFilm
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
from mcxray import get_current_module_path

# Project modules
import mcxray.format.results.PhirhozGeneratedCharacteristicThinFilm as PhirhozGeneratedCharacteristicThinFilm

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
        self.assertTrue(True)

    def test_read(self):
        """
        Tests for method `read`.
        """

        phirhozThinFilm = PhirhozGeneratedCharacteristicThinFilm.PhirhozGeneratedCharacteristicThinFilm()
        phirhozThinFilm.path = get_current_module_path(__file__, "../../../test_data/results")
        phirhozThinFilm.basename = "SimulationMCXrayPhirhozTestCases_Cu_E500d0keV_N100000e"

        phirhozThinFilm.read()

        self.assertEqual(1, phirhozThinFilm.numberRegions)

        intensity  = phirhozThinFilm.intensities[0]

        self.assertEqual("0", intensity[PhirhozGeneratedCharacteristicThinFilm.INDEX_REGION])
        self.assertEqual("Cu", intensity[PhirhozGeneratedCharacteristicThinFilm.ATOM_SYMBOL])
        self.assertEqual("390.159", intensity[PhirhozGeneratedCharacteristicThinFilm.SUBSHELL_K])
        self.assertEqual("13367.3", intensity[PhirhozGeneratedCharacteristicThinFilm.SUBSHELL_L])
        self.assertEqual("0", intensity[PhirhozGeneratedCharacteristicThinFilm.SUBSHELL_M])

        #self.fail("Test if the testcase is working.")

    def test_getIntensity(self):
        """
        Tests for method `getIntensity`.
        """

        phirhozThinFilm = PhirhozGeneratedCharacteristicThinFilm.PhirhozGeneratedCharacteristicThinFilm()
        phirhozThinFilm.path = get_current_module_path(__file__, "../../../test_data/results")
        phirhozThinFilm.basename = "SimulationMCXrayPhirhozTestCases_Cu_E500d0keV_N100000e"

        phirhozThinFilm.read()

        self.assertEqual(1, phirhozThinFilm.numberRegions)

        regionID = 0
        atomicSymbol = "Cu"
        intensity = phirhozThinFilm.getIntensity(regionID, atomicSymbol, PhirhozGeneratedCharacteristicThinFilm.SUBSHELL_K)
        self.assertAlmostEqual(390.159, intensity, 6)
        intensity = phirhozThinFilm.getIntensity(regionID, atomicSymbol, PhirhozGeneratedCharacteristicThinFilm.SUBSHELL_L)
        self.assertAlmostEqual(13367.3, intensity, 6)
        intensity = phirhozThinFilm.getIntensity(regionID, atomicSymbol, PhirhozGeneratedCharacteristicThinFilm.SUBSHELL_M)
        self.assertAlmostEqual(0.0, intensity, 6)

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from mcxray.Testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__)
