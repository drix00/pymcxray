#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.test_PhirhozEmittedCharacteristic
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module `PhirhozEmittedCharacteristic`.
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
import pymcxray.FileFormat.Results.PhirhozEmittedCharacteristic as PhirhozEmittedCharacteristic

# Globals and constants variables.

class TestPhirhozEmittedCharacteristic(unittest.TestCase):
    """
    TestCase class for the module `PhirhozEmittedCharacteristic`.
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
        #PhirhozMCXRay_Ag_E5d0keV_N10000e_tB0d0deg_TOA45d0deg_PhirhozEmittedCharacteristic_Region0.csv

        spectrumFile = PhirhozEmittedCharacteristic.PhirhozEmittedCharacteristic()
        spectrumFile.path = get_current_module_path(__file__, "../../../test_data/results")
        spectrumFile.basename = "PhirhozMCXRay_Ag_E5d0keV_N10000e_tB0d0deg_TOA45d0deg"

        regionID = 0
        spectrumFile.read(regionID)

        self.assertEquals(5, len(spectrumFile.fieldNames))
        self.assertEquals(128, len(spectrumFile.depth_A))
        self.assertEquals(4, len(spectrumFile.phirhozs))
        self.assertEquals(128, len(spectrumFile.phirhozs[("Ag", "La")]))

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from pymcxray.Testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__)
