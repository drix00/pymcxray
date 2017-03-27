#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.exported.test_XrayIntensityXY
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module XrayIntensityXY.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2014 Hendrix Demers"
__license__ = ""

# Standard library modules.
import unittest
import logging
import os.path

# Third party modules.

# Local modules.

# Project modules
import pymcxray.FileFormat.Results.exported.XrayIntensityXY as XrayIntensityXY

# Globals and constants variables.

class TestXrayIntensityXY(unittest.TestCase):
    """
    TestCase class for the module `XrayIntensityXY`.
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

    def testOpenFile(self):
        """
        Test if the test data file can be open.
        """

        path = "../../test_data"
        filename = "AlMgBulk5keVB_Generated.txt"

        filepath = os.path.join(path, filename)

        xrayIntensityXY = XrayIntensityXY.XrayIntensityXY()

        xrayIntensityXY.readData(filepath)

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from pymcxray.Testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__)
