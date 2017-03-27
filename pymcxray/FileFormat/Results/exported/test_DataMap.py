#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.exported.test_DataMap
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module `DataMap`.
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
import pymcxray.FileFormat.Results.exported.DataMap as DataMap

# Globals and constants variables.

class TestDataMap(unittest.TestCase):
    """
    TestCase class for the module `DataMap`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

        self.filepath = get_current_module_path(__file__, "../../../../test_data/exportedFiles/CNTsFePt_30keV_100e_100pixels_BF.txt")

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
        dataMap = DataMap.DataMap(self.filepath)

        self.assertEquals(self.filepath, dataMap._filepath)

        #self.fail("Test if the testcase is working.")

    def test_read(self):
        """
        Tests for method `read`.
        """

        dataMap = DataMap.DataMap(self.filepath)
        dataMap.read()

        self.assertEquals("Bright Field Image", dataMap.imageName)
        self.assertEquals((100, 100), dataMap.size)

        self.assertEquals(34.0, dataMap.pixels[50][50])

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from pymcxray.Testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__, withCoverage=False)
