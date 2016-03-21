#!/usr/bin/env python
"""
.. py:currentmodule:: test_AtomData
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module `AtomData`.
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
import pymcxray.AtomData as AtomData

# Globals and constants variables.

class TestAtomData(unittest.TestCase):
    """
    TestCase class for the module `AtomData`.
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

    def testConstants(self):
        """
        First test to check if the testcase is working with the testing framework.
        """

        self.assertEquals(AtomData._NUMBER_SHELLS, len(AtomData.ATOM_SHELL_NAMES))
        self.assertEquals(AtomData._NUMBER_LINES, len(AtomData.ATOM_LINE_NAMES))

        self.assertEquals(AtomData._NUMBER_ATOMS, len(AtomData.ATOM_NAMES))
        self.assertEquals(AtomData._NUMBER_ATOMS, len(AtomData.ATOM_SYMBOLS))
        self.assertEquals(AtomData._NUMBER_ATOMS, len(AtomData.ATOM_WEIGHTS))
        self.assertEquals(AtomData._NUMBER_ATOMS, len(AtomData.ATOM_MASS_DENSITY_g_cm3))
        self.assertEquals(AtomData._NUMBER_ATOMS, len(AtomData.ATOM_ION_ENERGY_SHELL_K_keV))
        self.assertEquals(AtomData._NUMBER_ATOMS, len(AtomData.ATOM_ION_ENERGY_SHELL_L3_keV))
        self.assertEquals(AtomData._NUMBER_ATOMS, len(AtomData.ATOM_ION_ENERGY_SHELL_M5_keV))

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from pymcxray.Testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__)
