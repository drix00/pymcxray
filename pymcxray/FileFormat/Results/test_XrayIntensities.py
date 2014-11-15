#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.test_XrayIntensities
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module `XrayIntensities`.
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
import pyHendrixDemersTools.Files as Files

# Project modules
import XrayIntensities

# Globals and constants variables.

class TestXrayIntensities(unittest.TestCase):
    """
    TestCase class for the module `XrayIntensities`.
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

        intensitiesFile = XrayIntensities.XrayIntensities()
        intensitiesFile.path = Files.getCurrentModulePath(__file__, "../../testData/results")
        intensitiesFile.basename = "SimulationsFRatio_Al0d200000Cu0d800000_E5d0keV"

        intensitiesFile.read()

        self.assertEquals(5, intensitiesFile.numberIntensities)

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from pyHendrixDemersTools.Testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__)
