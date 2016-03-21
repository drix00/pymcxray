#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.test_Tags
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the modules `Tags`.
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
import pymcxray.FileFormat.Results.Tags as Tags

# Globals and constants variables.

class TestTags(unittest.TestCase):
    """
    TestCase class for the module `Tags`.
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

    def test_findTag(self):
        """
        Tests for method `findTag`.
        """

        lines = self.getLines()

        tag = "##### Geometry Setup Start #####"
        index = Tags.findTag(tag, lines)
        self.assertEquals(0, index)

        tag = "--- Volume"
        index = Tags.findTag(tag, lines)
        self.assertEquals(3, index)

        tag = "##### Geometry Setup End #####"
        index = Tags.findTag(tag, lines)
        self.assertEquals(8, index)

        tag = "##### Energy Update Start #####"
        index = Tags.findTag(tag, lines)
        self.assertEquals(10, index)

        tag = "##### Energy Update End #####"
        index = Tags.findTag(tag, lines)
        self.assertEquals(23, index)

        #self.fail("Test if the testcase is working.")

    def getLines(self):
        lines = \
"""##### Geometry Setup Start #####


--- Volume 0 --- has no exclusion
0 BOX
-10000000000.000000 10000000000.000000 -10000000000.000000 10000000000.000000 0.000000 20000000000.000000


##### Geometry Setup End #####

##### Energy Update Start #####

Voxel total            = 446915
Voxel failed precision = 0

Coordinate faults      = 0
   faults X neg = 0    min coord index = 0
   faults X pos = 0    max coord index = 0
   faults Y neg = 0    min coord index = 0
   faults Y pos = 0    max coord index = 0
   faults Z neg = 0    min coord index = 0
   faults Z pos = 0    max coord index = 0

##### Energy Update End #####
""".splitlines()

        return lines

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from pymcxray.Testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__)
