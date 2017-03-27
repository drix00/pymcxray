#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.test_XraySpectraAtomEmittedDetectedLines
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module `XraySpectraAtomEmittedDetectedLines`.
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
import pymcxray.FileFormat.Results.XraySpectraAtomEmittedDetectedLines as XraySpectraAtomEmittedDetectedLines

# Globals and constants variables.

class TestXraySpectraAtomEmittedDetectedLines(unittest.TestCase):
    """
    TestCase class for the module `XraySpectraAtomEmittedDetectedLines`.
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
        #SimulationsAuNPonCExperimental_Au_d61A_C_E5d0keV_N10000e_N1000X_SpectraAtomEmittedDetectedLines_Region1.csv

        spectrumFile = XraySpectraAtomEmittedDetectedLines.XraySpectraAtomEmittedDetectedLines()
        spectrumFile.path = get_current_module_path(__file__, "../../../test_data/results")
        spectrumFile.basename = "SimulationsAuNPonCExperimental_Au_d61A_C_E5d0keV_N10000e_N1000X"

        regionID = 1
        spectrumFile.read(regionID)

        self.assertEquals(0.0025, spectrumFile.energies_keV[0])
        self.assertEquals(4.9975, spectrumFile.energies_keV[-1])
        self.assertEquals(1000, len(spectrumFile.energies_keV))
        self.assertEquals(1, len(spectrumFile.characteristics))
        self.assertEquals(1000, len(spectrumFile.characteristics['Au']))

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from pymcxray.Testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__, withCoverage=True)
