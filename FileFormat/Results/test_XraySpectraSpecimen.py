#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.test_XraySpectraSpecimen
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
import DrixUtilities.Files as Files

# Project modules
import XraySpectraSpecimen

# Globals and constants variables.

class TestXraySpectraSpecimen(unittest.TestCase):
    """
    TestCase class for the module `XraySpectraSpecimen`.
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

        spectrumFile = XraySpectraSpecimen.XraySpectraSpecimen()
        spectrumFile.path = Files.getCurrentModulePath(__file__, "../../testData/results")
        spectrumFile.basename = "ExperimentalSpectraMCXRay_Au100T250000A_E200d0keV_N1000e_N21000000X_t600s_w20eV_N64W"

        spectrumFile.read()

        self.assertEquals(40000, len(spectrumFile.energies_keV))
        self.assertEquals(40000, len(spectrumFile.totals))
        self.assertEquals(40000, len(spectrumFile.characteristics))
        self.assertEquals(40000, len(spectrumFile.backgrounds))

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from DrixUtilities.Testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__)