#!/usr/bin/env python
"""
.. py:currentmodule:: format.test_RegionType
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Test for module `RegionType`.
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
import mcxray.format.RegionType as RegionType

# Globals and constants variables.

class TestRegionType(unittest.TestCase):
    """
    TestCase class for the module `RegionType`.
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

    def test_Constants(self):
        """
        Tests for method `Constants`.
        """

        self.assertEqual("BOX", RegionType.REGION_TYPE_BOX)
        self.assertEqual("CYLINDER", RegionType.REGION_TYPE_CYLINDER)
        self.assertEqual("SPHERE", RegionType.REGION_TYPE_SPHERE)

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from tests.testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__)
