#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.test_ElectronExistResults
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module `ElectronExistResults`.
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
import os.path

# Third party modules.

# Local modules.

# Project modules
import ElectronExistResults

# Globals and constants variables.

class TestElectronExistResults(unittest.TestCase):
    """
    TestCase class for the module `ElectronExistResults`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

        #SimulationBseReciprocity_Ag_E1d0keV_N10000e_dB1d0nm_tB15d0deg_ElectronExitResults.csv
        self.testDataPath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../testData"))

        self.results = ElectronExistResults.ElectronExistResults(path=os.path.join(self.testDataPath, "results"), basename="SimulationBseReciprocity_Ag_E1d0keV_N10000e_dB1d0nm_tB15d0deg")

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

    def test_dataFileExist(self):
        """
        First test to check if the testcase is working with the testing framework.
        """

        results = ElectronExistResults.ElectronExistResults()
        results.path = os.path.join(self.testDataPath, "results")
        results.basename = "SimulationBseReciprocity_Ag_E1d0keV_N10000e_dB1d0nm_tB15d0deg"

        self.assertTrue(os.path.isfile(results.filepath))


        self.assertTrue(os.path.isfile(self.results.filepath))

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_read(self):
        """
        Tests for method `read`.
        """

        self.assertEquals(0, self.results.numberData)
        self.results.read()
        self.assertEquals(4036, self.results.numberData)

        #self.fail("Test if the testcase is working.")

    def test_energyDistribution(self):
        """
        Tests for method `energyDistribution`.
        """
        energies_keV, histogram = self.results.getEnergyDistribution()

        self.assertEquals(10, len(energies_keV))
        self.assertEquals(10, len(histogram))

        self.assertEquals(0.00056368600000000074, energies_keV[0])
        self.assertEquals(0.99941699999999978, energies_keV[-1])

        self.assertEquals(71.0, histogram[0])
        self.assertEquals(502, histogram[-1])

        energies_keV, histogram = self.results.getEnergyDistribution(numberBins=20)

        self.assertEquals(20, len(energies_keV))
        self.assertEquals(20, len(histogram))

        self.assertEquals(0.8, energies_keV[0])
        self.assertEquals(0.9, energies_keV[-1])

        self.assertEquals(71.0, histogram[0])
        self.assertEquals(502, histogram[-1])

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from DrixUtilities.Testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__)