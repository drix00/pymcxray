#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.test_PhirhozGeneratedCharacteristic
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module `PhirhozGeneratedCharacteristic`.
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
from pymcxray import get_current_module_path

# Project modules
import pymcxray.FileFormat.Results.PhirhozGeneratedCharacteristic as PhirhozGeneratedCharacteristic

# Globals and constants variables.

class TestPhirhozGeneratedCharacteristic(unittest.TestCase):
    """
    TestCase class for the module `PhirhozGeneratedCharacteristic`.
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
        #PhirhozMCXRay_Ag_E5d0keV_N10000e_tB0d0deg_TOA45d0deg_PhirhozGeneratedCharacteristic_Region0.csv

        spectrumFile = PhirhozGeneratedCharacteristic.PhirhozGeneratedCharacteristic()
        spectrumFile.path = get_current_module_path(__file__, "../../../test_data/results")
        spectrumFile.basename = "PhirhozMCXRay_Ag_E5d0keV_N10000e_tB0d0deg_TOA45d0deg"

        regionID = 0
        spectrumFile.read(regionID)

        self.assertEquals(2, len(spectrumFile.fieldNames))
        self.assertEquals(128, len(spectrumFile.depth_A))
        self.assertEquals(1, len(spectrumFile.phirhozs))
        self.assertEquals(128, len(spectrumFile.phirhozs[("Ag", "L")]))

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from pymcxray.Testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__)
