#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.test_PhirhozRegion
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module `PhirhozRegion`.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2012 Hendrix Demers"
__license__ = ""

# Subversion informations for the file.
__svnRevision__ = "$Revision$"
__svnDate__ = "$Date$"
__svnId__ = "$Id$"

# Standard library modules.
import unittest
import logging
import os.path

# Third party modules.

# Local modules.

# Project modules
import pymcxray.FileFormat.Results.PhirhozRegion as PhirhozRegion

# Globals and constants variables.

class TestPhirhozRegion(unittest.TestCase):
    """
    TestCase class for the module `PhirhozRegion`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

        self.testDataPath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../test_data"))

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

    def test_readFromLines(self):
        """
        Tests for method `readFromLines`.
        """

        lines, phirhozRegionRef = getLinesAndReference(self.testDataPath)

        phirhozRegion = PhirhozRegion.PhirhozRegion(64, 128)
        phirhozRegion.readFromLines(lines)

        self.assertEquals(phirhozRegionRef.regionID, phirhozRegion.regionID)

        #self.fail("Test if the testcase is working.")

def getLinesAndReference(path):
    filepath = os.path.join(path, "version1.1/autoSavedFiles/phirhozGenerated_region0.txt")
    lines = open(filepath, 'r').readlines()

    phirhozRegionRef = PhirhozRegion.PhirhozRegion(64, 128)
    phirhozRegionRef.regionID = 0

    return lines, phirhozRegionRef

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from pymcxray.Testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__)
