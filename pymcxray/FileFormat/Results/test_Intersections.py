#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.test_Intersections
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for module `Intersections`.
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
import pymcxray.FileFormat.Results.Intersections as Intersections

# Globals and constants variables.

class TestIntersections(unittest.TestCase):
    """
    TestCase class for the module `Intersections`.
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

    def test_extractFromLines(self):
        """
        Tests for method `extractFromLines`.
        """

        lines = \
"""--- Volume 0 --- has no exclusion
0 BOX
-10000000000.000000 10000000000.000000 -10000000000.000000 10000000000.000000 0.000000 20000000000.000000

""".splitlines()
        print(lines)

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from pymcxray.Testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__)
