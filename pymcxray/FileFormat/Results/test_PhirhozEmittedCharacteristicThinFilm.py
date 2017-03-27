#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.test_PhirhozEmittedCharacteristicThinFilm
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for module `PhirhozEmittedCharacteristicThinFilm`.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2014 Hendrix Demers"
__license__ = ""

# Standard library modules.
import unittest
import logging

# Third party modules.

# Local modules.
from pymcxray import get_current_module_path

# Project modules
import pymcxray.FileFormat.Results.PhirhozEmittedCharacteristicThinFilm as PhirhozEmittedCharacteristicThinFilm

# Globals and constants variables.

class TestPhirhozEmittedCharacteristicThinFilm(unittest.TestCase):
    """
    TestCase class for the module `PhirhozEmittedCharacteristicThinFilm`.
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

        phirhozThinFilm = PhirhozEmittedCharacteristicThinFilm.PhirhozEmittedCharacteristicThinFilm()
        phirhozThinFilm.path = get_current_module_path(__file__, "../../../test_data/results")
        phirhozThinFilm.basename = "SimulationMCXrayPhirhozTestCases_Cu_E500d0keV_N100000e"

        phirhozThinFilm.read()

        self.assertEquals(1, phirhozThinFilm.numberRegions)

        intensity  = phirhozThinFilm.intensities[0]

        self.assertEquals("0", intensity[PhirhozEmittedCharacteristicThinFilm.INDEX_REGION])
        self.assertEquals("Cu", intensity[PhirhozEmittedCharacteristicThinFilm.ATOM_SYMBOL])
        self.assertEquals("0.00194507", intensity[PhirhozEmittedCharacteristicThinFilm.LINE_KA1])
        self.assertEquals("0.00179503", intensity[PhirhozEmittedCharacteristicThinFilm.LINE_KA2])
        self.assertEquals("0.0337762", intensity[PhirhozEmittedCharacteristicThinFilm.LINE_KB1])
        self.assertEquals("0", intensity[PhirhozEmittedCharacteristicThinFilm.LINE_KB2])
        self.assertEquals("8.20759e-158", intensity[PhirhozEmittedCharacteristicThinFilm.LINE_LA])
        self.assertEquals("0", intensity[PhirhozEmittedCharacteristicThinFilm.LINE_LB1])
        self.assertEquals("0", intensity[PhirhozEmittedCharacteristicThinFilm.LINE_LB2])
        self.assertEquals("0", intensity[PhirhozEmittedCharacteristicThinFilm.LINE_LG])
        self.assertEquals("0", intensity[PhirhozEmittedCharacteristicThinFilm.LINE_MA])

        #self.fail("Test if the testcase is working.")

    def test_getIntensity(self):
        """
        Tests for method `getIntensity`.
        """

        phirhozThinFilm = PhirhozEmittedCharacteristicThinFilm.PhirhozEmittedCharacteristicThinFilm()
        phirhozThinFilm.path = get_current_module_path(__file__, "../../../test_data/results")
        phirhozThinFilm.basename = "SimulationMCXrayPhirhozTestCases_Cu_E500d0keV_N100000e"

        phirhozThinFilm.read()

        self.assertEquals(1, phirhozThinFilm.numberRegions)

        regionID = 0
        atomicSymbol = "Cu"
        intensity = phirhozThinFilm.getIntensity(regionID, atomicSymbol, PhirhozEmittedCharacteristicThinFilm.LINE_KA1)
        self.assertAlmostEquals(0.00194507, intensity, 6)
        intensity = phirhozThinFilm.getIntensity(regionID, atomicSymbol, PhirhozEmittedCharacteristicThinFilm.LINE_KA2)
        self.assertAlmostEquals(0.00179503, intensity, 6)
        intensity = phirhozThinFilm.getIntensity(regionID, atomicSymbol, PhirhozEmittedCharacteristicThinFilm.LINE_KB1)
        self.assertAlmostEquals(0.0337762, intensity, 6)
        intensity = phirhozThinFilm.getIntensity(regionID, atomicSymbol, PhirhozEmittedCharacteristicThinFilm.LINE_KB2)
        self.assertAlmostEquals(0.0, intensity, 6)
        intensity = phirhozThinFilm.getIntensity(regionID, atomicSymbol, PhirhozEmittedCharacteristicThinFilm.LINE_LA)
        self.assertAlmostEquals(8.20759E-158, intensity, 6)
        intensity = phirhozThinFilm.getIntensity(regionID, atomicSymbol, PhirhozEmittedCharacteristicThinFilm.LINE_LB1)
        self.assertAlmostEquals(0.0, intensity, 6)
        intensity = phirhozThinFilm.getIntensity(regionID, atomicSymbol, PhirhozEmittedCharacteristicThinFilm.LINE_LB2)
        self.assertAlmostEquals(0.0, intensity, 6)
        intensity = phirhozThinFilm.getIntensity(regionID, atomicSymbol, PhirhozEmittedCharacteristicThinFilm.LINE_LG)
        self.assertAlmostEquals(0.0, intensity, 6)
        intensity = phirhozThinFilm.getIntensity(regionID, atomicSymbol, PhirhozEmittedCharacteristicThinFilm.LINE_MA)
        self.assertAlmostEquals(0.0, intensity, 6)

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from pymcxray.Testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__)
