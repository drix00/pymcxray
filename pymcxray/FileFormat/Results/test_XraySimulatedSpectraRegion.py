#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.test_XraySimulatedSpectraRegion
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

description
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
import pymcxray.FileFormat.Results.XraySimulatedSpectraRegion as XraySimulatedSpectraRegion

# Globals and constants variables.

class TestXraySimulatedSpectraRegion(unittest.TestCase):
    """
    TestCase class for the module `moduleName`.
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

        spectrumFile = XraySimulatedSpectraRegion.XraySimulatedSpectraRegion()
        spectrumFile.path = get_current_module_path(__file__, "../../../test_data/results")
        spectrumFile.basename = "testC_10e_10kp"

        spectrumFile.read()

        self.assertEquals(1024, len(spectrumFile.channelNumbers))
        self.assertEquals(1024, len(spectrumFile.energiesReference_keV))
        self.assertEquals(1024, len(spectrumFile.energies_keV))
        self.assertEquals(1024, len(spectrumFile.simulatedIntensities))
        self.assertEquals(1024, len(spectrumFile.detectedIntensities))
        self.assertEquals(1024, len(spectrumFile.eNetPeak[0]))
        self.assertEquals(1024, len(spectrumFile.peakToBackgrpound))
        self.assertEquals(1024, len(spectrumFile.peakToBackgrpoundAverage))

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from pymcxray.Testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__, withCoverage=False)
