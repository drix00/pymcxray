#!/usr/bin/env python
"""
.. py:currentmodule:: format.results.test_PhirhozElement
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module `PhirhozElement`.
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

# Third party modules.

# Local modules.

# Project modules
import mcxray.format.results.PhirhozElement as PhirhozElement

# Globals and constants variables.

class TestPhirhozElement(unittest.TestCase):
    """
    TestCase class for the module `PhirhozElement`.
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
        self.assertTrue(True)

    def test_readFromLine(self):
        """
        Tests for method `readFromLines`.
        """

        line, phirhozElementRef = getLineAndReference()

        phirhozElement = PhirhozElement.PhirhozElement()
        phirhozElement.readFromLine(line)

        self.assertEqual(phirhozElementRef.symbol, phirhozElement.symbol)
        self.assertEqual(phirhozElementRef.weightFraction, phirhozElement.weightFraction)
        self.assertEqual(phirhozElementRef.isIonizationShell_K, phirhozElement.isIonizationShell_K)
        self.assertEqual(phirhozElementRef.isIonizationShell_L, phirhozElement.isIonizationShell_L)
        self.assertEqual(phirhozElementRef.isIonizationShell_M, phirhozElement.isIonizationShell_M)

        #self.fail("Test if the testcase is working.")

def getLineAndReference():
    line = "Au, 100.0000000 %   Ionization shells 0 1 1"

    phirhozElementRef = PhirhozElement.PhirhozElement()
    phirhozElementRef.symbol = 'Au'
    phirhozElementRef.weightFraction = 1.0
    phirhozElementRef.isIonizationShell_K = False
    phirhozElementRef.isIonizationShell_L = True
    phirhozElementRef.isIonizationShell_M = True

    return line, phirhozElementRef

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from tests.testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__, withCoverage=False)
