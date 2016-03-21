#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.test_FileReaderWriterTools
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module `FileReaderWriterTools`.
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
import pymcxray.FileFormat.FileReaderWriterTools as FileReaderWriterTools

# Globals and constants variables.

class TestFileReaderWriterTools(unittest.TestCase):
    """
    TestCase class for the module `FileReaderWriterTools`.
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

    def test__reduceAfterDot(self):
        """
        Tests for method `reduceAfterDot`.
        """

        value = 23.0
        valueStr = FileReaderWriterTools.reduceAfterDot(value)
        self.assertEquals("23", valueStr)

        value = 67.80
        valueStr = FileReaderWriterTools.reduceAfterDot(value)
        self.assertEquals("67.8", valueStr)

        value = 2.34000
        valueStr = FileReaderWriterTools.reduceAfterDot(value)
        self.assertEquals("2.34", valueStr)

        value = 2.070
        valueStr = FileReaderWriterTools.reduceAfterDot(value)
        self.assertEquals("2.07", valueStr)

        value = 0.070
        valueStr = FileReaderWriterTools.reduceAfterDot(value)
        self.assertEquals("0.07", valueStr)

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from pymcxray.Testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__)
