#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.test_XraySpectraSpecimenEmittedDetected
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module `XraySpectraSpecimenEmittedDetected`.
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
import DrixUtilities.Files as Files

# Project modules
import XraySpectraSpecimenEmittedDetected

# Globals and constants variables.
#SimulationsAuNPonC_Au_d100A_C_E10d0keV_N10000e_N1000000X_SpectraSpecimenEmittedDetected.csv

class TestXraySpectraSpecimenEmittedDetected(unittest.TestCase):
    """
    TestCase class for the module `XraySpectraSpecimenEmittedDetected`.
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

        spectrumFile = XraySpectraSpecimenEmittedDetected.XraySpectraSpecimenEmittedDetected()
        spectrumFile.path = Files.getCurrentModulePath(__file__, "../../testData/results")
        spectrumFile.basename = "SimulationsAuNPonC_Au_d100A_C_E10d0keV_N10000e_N1000000X"

        spectrumFile.read()

        self.assertEquals(2000, len(spectrumFile.energies_keV))
        self.assertEquals(2000, len(spectrumFile.totals))
        self.assertEquals(2000, len(spectrumFile.characteristics))
        self.assertEquals(2000, len(spectrumFile.backgrounds))

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from DrixUtilities.Testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__)
