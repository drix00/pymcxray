#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.test_XraySimulatedSpectraSpecimen
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>


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
import pymcxray.FileFormat.Results.XraySimulatedSpectraSpecimen as XraySimulatedSpectraSpecimen

# Globals and constants variables.

class TestXraySimulatedSpectraSpecimen(unittest.TestCase):
    """
    TestCase class for the module `XraySimulatedSpectraSpecimen`.
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

        spectrumFile = XraySimulatedSpectraSpecimen.XraySimulatedSpectraSpecimen()
        spectrumFile.path = get_current_module_path(__file__, "../../../test_data/results")
        spectrumFile.basename = "testC_10e_10kp"

        spectrumFile.read()

        self.assertEquals(1024, len(spectrumFile.energies_keV))
        self.assertEquals(1024, len(spectrumFile.totals))

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from pymcxray.Testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__)
