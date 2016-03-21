#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.test_BaseResults
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module `BaseResults`.
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

# Project modules
import pymcxray.FileFormat.Results.BaseResults as BaseResults

# Globals and constants variables.

class TestBaseResults(unittest.TestCase):
    """
    TestCase class for the module `BaseResults`.
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

    def test_init(self):
        """
        Tests for method `init`.
        """

        baseResults = BaseResults.BaseResults()

        self.assertEquals("", baseResults.path)
        self.assertEquals("MCXRay", baseResults.basename)

        #self.fail("Test if the testcase is working.")

    def test_path(self):
        """
        Tests for method `path`.
        """

        pathRef = r"J:\hdemers\work\mcgill2012\results\simulations\McXRay\SimulationsFRatioAlCu\MCXRay_v1_2_1\simulations\Results"

        baseResults = BaseResults.BaseResults()
        self.assertEquals("", baseResults.path)

        baseResults.path = pathRef
        self.assertEquals(pathRef, baseResults.path)

        BaseResults.BaseResults(path=pathRef)
        self.assertEquals(pathRef, baseResults.path)

        BaseResults.BaseResults(pathRef)
        self.assertEquals(pathRef, baseResults.path)

        #self.fail("Test if the testcase is working.")

    def test_basename(self):
        """
        Tests for method `basename`.
        """

        basenameRef = "SimulationsFRatio_Al0d100000Cu0d900000_E10d0keV"

        baseResults = BaseResults.BaseResults()
        self.assertEquals("MCXRay", baseResults.basename)

        baseResults.basename = basenameRef
        self.assertEquals(basenameRef, baseResults.basename)

        baseResults = BaseResults.BaseResults(basename=basenameRef)
        self.assertEquals(basenameRef, baseResults.basename)

        baseResults = BaseResults.BaseResults(basenameRef)
        self.assertNotEquals(basenameRef, baseResults.basename)
        self.assertEquals(basenameRef, baseResults.path)

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from pymcxray.Testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__)
