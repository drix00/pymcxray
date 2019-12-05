#!/usr/bin/env python
"""
.. py:currentmodule:: format.results.test_ElectronResults
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module `XraySpectraSpecimen`.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2012 Hendrix Demers"
__license__ = ""

# Standard library modules.
import unittest
import logging

# Third party modules.

# Local modules.
from mcxray import get_current_module_path

# Project modules
import mcxray.format.results.ElectronResults as ElectronResults

# Globals and constants variables.

class TestElectronResults(unittest.TestCase):
    """
    TestCase class for the module `ElectronResults`.
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

        electronResults = ElectronResults.ElectronResults()
        electronResults.path = get_current_module_path(__file__, "../../../test_data/results")
        electronResults.basename = "SimulationKalefEzra1982_Al100T10000A_E300d0keV_N100000e"

        electronResults.read()

        self.assertEqual(100000, electronResults.numberSimulatedElectrons)
        self.assertEqual(0, electronResults.numberInternalElectrons)
        self.assertEqual(43, electronResults.numberBackscatteredElectrons)
        self.assertEqual(99956, electronResults.numberTransmittedElectrons)
        self.assertEqual(0, electronResults.numberSkirtedElectrons)
        self.assertEqual(458571, electronResults.numberElectronCollisions)
        self.assertEqual(0, electronResults.fractionInternalElectrons)
        self.assertEqual(0.00043, electronResults.fractionBackscatteredElectrons)
        self.assertEqual(0.99956, electronResults.fractionTransmittedElectrons)
        self.assertEqual(0, electronResults.fractionSkirtedElectrons)
        #self.assertEqual(1.00306e+009, electronResults.totalElectronPathLength_A)
        #self.assertEqual(10000, electronResults.maximumPositionZ_A)
        #self.assertEqual(4.58571, electronResults.meanNumberCollisionsPerElectron)
        #self.assertEqual(1795.76, electronResults.meanDistanceBetweenCollision_A)
        #self.assertEqual(402906, electronResults.totalCollisionPolarAngle_deg)
        #self.assertEqual(8.25569e+007, electronResults.totalCollisionAzimuthalAngle_deg)
        #self.assertEqual(0.878612, electronResults.meanCollisionPolarAngle_deg)
        #self.assertEqual(180.031, electronResults.meanCollisionAzimuthalAngle_deg)
        #self.assertEqual(0.0015828, electronResults.absorbedEnergyRatioPerElectron)

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from tests.testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__)
