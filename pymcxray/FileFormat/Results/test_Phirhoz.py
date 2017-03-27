#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.test_Phirhoz
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module `Phirhoz`.
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
import pymcxray.FileFormat.Results.Phirhoz as Phirhoz
from pymcxray.FileFormat.Results.PhirhozRegion import SHELL_L

# Globals and constants variables.

class TestPhirhoz(unittest.TestCase):
    """
    TestCase class for the module `Phirhoz`.
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

        lines, phirhozRef = getLinesAndReference(self.testDataPath)

        phirhoz = Phirhoz.Phirhoz('Au', SHELL_L)
        phirhoz.readFromLines(lines)

        self.assertEquals(phirhozRef.symbol, phirhoz.symbol)
        self.assertEquals(phirhozRef.shell, phirhoz.shell)
        self.assertEquals(phirhozRef.intensity, phirhoz.intensity)

        self.assertEquals(128, len(phirhoz.depths_A))
        self.assertEquals(128, len(phirhoz.values))

        self.assertEquals(0.0, phirhoz.depths_A[0])
        self.assertEquals(86531.709610, phirhoz.depths_A[-1])

        self.assertEquals(1.961092, phirhoz.values[0])
        self.assertEquals(0.0, phirhoz.values[-1])

        #self.fail("Test if the testcase is working.")

def getLinesAndReference(path):
    filepath = os.path.join(path, "version1.1/autoSavedFiles/phirhozGenerated_elementShell.txt")
    lines = open(filepath, 'r').readlines()

    phirhozRef = Phirhoz.Phirhoz('Au', SHELL_L)
    phirhozRef.intensity = 1.366974e+007

    return lines, phirhozRef


if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from pymcxray.Testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__)
