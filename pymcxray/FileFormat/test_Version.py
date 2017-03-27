#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.test_Version
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for module `Version`.
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
import os.path

# Third party modules.

# Local modules.

# Project modules
import pymcxray.FileFormat.Version as Version
import pymcxray.FileFormat.testUtilities as testUtilities

# Globals and constants variables.

class TestVersion(unittest.TestCase):
    """
    TestCase class for the module `Version`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

        self.testDataPath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../test_data"))
        self.tempDataPath = testUtilities.createTempDataPath(self.testDataPath)

    def tearDown(self):
        """
        Teardown method.
        """

        unittest.TestCase.tearDown(self)

        testUtilities.removeTempDataPath(self.tempDataPath)

    def testSkeleton(self):
        """
        First test to check if the testcase is working with the testing framework.
        """

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_toString(self):
        """
        Tests for method `toString`.
        """

        version =  Version.Version(1, 2, 3)
        stringRef = "1.2.3"
        versionString = version.toString()
        self.assertEquals(stringRef, versionString)

        #self.fail("Test if the testcase is working.")

    def test_fromString(self):
        """
        Tests for method `fromString`.
        """

        version =  Version.Version(1, 2, 3)
        stringRef = "4.5.6"
        version.fromString(stringRef)
        versionString = version.toString()
        self.assertEquals(stringRef, versionString)

        self.assertEquals(4, version.major)
        self.assertEquals(5, version.minor)
        self.assertEquals(6, version.revision)

        #self.fail("Test if the testcase is working.")

    def test_readFromFile(self):
        """
        Tests for method `readFromFile`.
        """

        title = "AlMgBulk5keV_version_1_4_1"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.sim" % (title)))

        version =  Version.Version(0, 0, 0)
        version.readFromFile(filepath)

        stringRef = "1.4.1"
        versionString = version.toString()
        self.assertEquals(stringRef, versionString)

        self.assertEquals(1, version.major)
        self.assertEquals(4, version.minor)
        self.assertEquals(1, version.revision)

        #self.fail("Test if the testcase is working.")

    def test_readFromFile_BadFile(self):
        """
        Tests for method `readFromFile`.
        """

        title = "AlMgBulk5keV_version_1_1_1"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.snp" % (title)))

        version =  Version.Version(0, 0, 0)
        version.readFromFile(filepath)

        stringRef = "1.1.1"
        versionString = version.toString()
        self.assertEquals(stringRef, versionString)
        self.assertEquals(1, version.major)
        self.assertEquals(1, version.minor)
        self.assertEquals(1, version.revision)

        #self.fail("Test if the testcase is working.")

    def test_VersionConstants(self):
        """
        Tests for method `VersionConstants`.
        """

        stringRef = "1.1.1"
        versionString = Version.VERSION_1_1_1.toString()
        self.assertEquals(stringRef, versionString)
        self.assertEquals(1, Version.VERSION_1_1_1.major)
        self.assertEquals(1, Version.VERSION_1_1_1.minor)
        self.assertEquals(1, Version.VERSION_1_1_1.revision)

        stringRef = "1.2.0"
        versionString = Version.VERSION_1_2_0.toString()
        self.assertEquals(stringRef, versionString)
        self.assertEquals(1, Version.VERSION_1_2_0.major)
        self.assertEquals(2, Version.VERSION_1_2_0.minor)
        self.assertEquals(0, Version.VERSION_1_2_0.revision)

        stringRef = "1.2.1"
        versionString = Version.VERSION_1_2_1.toString()
        self.assertEquals(stringRef, versionString)
        self.assertEquals(1, Version.VERSION_1_2_1.major)
        self.assertEquals(2, Version.VERSION_1_2_1.minor)
        self.assertEquals(1, Version.VERSION_1_2_1.revision)

        stringRef = "1.2.2"
        versionString = Version.VERSION_1_2_2.toString()
        self.assertEquals(stringRef, versionString)
        self.assertEquals(1, Version.VERSION_1_2_2.major)
        self.assertEquals(2, Version.VERSION_1_2_2.minor)
        self.assertEquals(2, Version.VERSION_1_2_2.revision)

        stringRef = "1.2.3"
        versionString = Version.VERSION_1_2_3.toString()
        self.assertEquals(stringRef, versionString)
        self.assertEquals(1, Version.VERSION_1_2_3.major)
        self.assertEquals(2, Version.VERSION_1_2_3.minor)
        self.assertEquals(3, Version.VERSION_1_2_3.revision)

        stringRef = "1.2.4"
        versionString = Version.VERSION_1_2_4.toString()
        self.assertEquals(stringRef, versionString)
        self.assertEquals(1, Version.VERSION_1_2_4.major)
        self.assertEquals(2, Version.VERSION_1_2_4.minor)
        self.assertEquals(4, Version.VERSION_1_2_4.revision)

        stringRef = "1.2.5"
        versionString = Version.VERSION_1_2_5.toString()
        self.assertEquals(stringRef, versionString)
        self.assertEquals(1, Version.VERSION_1_2_5.major)
        self.assertEquals(2, Version.VERSION_1_2_5.minor)
        self.assertEquals(5, Version.VERSION_1_2_5.revision)

        stringRef = "1.3.0"
        versionString = Version.VERSION_1_3_0.toString()
        self.assertEquals(stringRef, versionString)
        self.assertEquals(1, Version.VERSION_1_3_0.major)
        self.assertEquals(3, Version.VERSION_1_3_0.minor)
        self.assertEquals(0, Version.VERSION_1_3_0.revision)

        stringRef = "1.4.0"
        versionString = Version.VERSION_1_4_0.toString()
        self.assertEquals(stringRef, versionString)
        self.assertEquals(1, Version.VERSION_1_4_0.major)
        self.assertEquals(4, Version.VERSION_1_4_0.minor)
        self.assertEquals(0, Version.VERSION_1_4_0.revision)

        stringRef = "1.4.1"
        versionString = Version.VERSION_1_4_1.toString()
        self.assertEquals(stringRef, versionString)
        self.assertEquals(1, Version.VERSION_1_4_1.major)
        self.assertEquals(4, Version.VERSION_1_4_1.minor)
        self.assertEquals(1, Version.VERSION_1_4_1.revision)

        stringRef = "1.4.2"
        versionString = Version.VERSION_1_4_2.toString()
        self.assertEquals(stringRef, versionString)
        self.assertEquals(1, Version.VERSION_1_4_2.major)
        self.assertEquals(4, Version.VERSION_1_4_2.minor)
        self.assertEquals(2, Version.VERSION_1_4_2.revision)

        stringRef = "1.1.1"
        versionString = Version.BEFORE_VERSION.toString()
        self.assertEquals(stringRef, versionString)
        self.assertEquals(1, Version.BEFORE_VERSION.major)
        self.assertEquals(1, Version.BEFORE_VERSION.minor)
        self.assertEquals(1, Version.BEFORE_VERSION.revision)

        self.assertEquals(Version.VERSION_1_1_1, Version.BEFORE_VERSION)
        self.assertNotEquals(Version.VERSION_1_1_1, Version.CURRENT_VERSION)

        stringRef = "1.5.2"
        versionString = Version.CURRENT_VERSION.toString()
        self.assertEquals(stringRef, versionString)
        self.assertEquals(1, Version.CURRENT_VERSION.major)
        self.assertEquals(5, Version.CURRENT_VERSION.minor)
        self.assertEquals(2, Version.CURRENT_VERSION.revision)

        self.assertEquals(Version.VERSION_1_5_2, Version.CURRENT_VERSION)
        self.assertNotEquals(Version.VERSION_1_5_2, Version.BEFORE_VERSION)
        self.assertFalse(Version.VERSION_1_5_2 == Version.BEFORE_VERSION)

        #self.fail("Test if the testcase is working.")

    def test_writeLine(self):
        """
        Tests for method `writeLine`.
        """

        title = "AlMgBulk5keV_version_3_4_5"
        filepath = os.path.join(self.tempDataPath, "%s.sim" % (title))
        logging.info(filepath)
        version = Version.Version(3, 4, 5)
        outputFile = open(filepath, 'w')
        version.writeLine(outputFile)
        outputFile.close()

        version =  Version.Version(0, 0, 0)
        version.readFromFile(filepath)

        stringRef = "3.4.5"
        versionString = version.toString()
        self.assertEquals(stringRef, versionString)

        self.assertEquals(3, version.major)
        self.assertEquals(4, version.minor)
        self.assertEquals(5, version.revision)

        #self.fail("Test if the testcase is working.")

    def test_comparison(self):
        """
        Test comparison operation on Version class.
        """
        self.assertTrue(Version.VERSION_1_2_0 == Version.VERSION_1_2_0)
        self.assertFalse(Version.VERSION_1_2_0 == Version.VERSION_1_1_1)
        self.assertFalse(Version.VERSION_1_2_0 == Version.VERSION_1_2_1)

        self.assertFalse(Version.VERSION_1_2_0 != Version.VERSION_1_2_0)
        self.assertTrue(Version.VERSION_1_2_0 != Version.VERSION_1_1_1)
        self.assertTrue(Version.VERSION_1_2_0 != Version.VERSION_1_2_1)

        self.assertTrue(Version.VERSION_1_2_0 > Version.VERSION_1_1_1)
        self.assertTrue(Version.VERSION_1_2_0 < Version.VERSION_1_2_1)
        self.assertTrue(Version.VERSION_1_1_1 < Version.VERSION_1_2_0)
        self.assertTrue(Version.VERSION_1_2_1 > Version.VERSION_1_2_0)

        self.assertTrue(Version.VERSION_1_2_0 >= Version.VERSION_1_1_1)
        self.assertTrue(Version.VERSION_1_2_0 <= Version.VERSION_1_2_1)
        self.assertTrue(Version.VERSION_1_1_1 <= Version.VERSION_1_2_0)
        self.assertTrue(Version.VERSION_1_2_1 >= Version.VERSION_1_2_0)

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    import nose
    nose.runmodule()
