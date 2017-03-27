#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.test_ResultsParameters
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for module `ResultsParameters`.
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
from nose.plugins.skip import SkipTest

# Local modules.

# Project modules
import pymcxray.FileFormat.ResultsParameters as ResultsParameters
import pymcxray.FileFormat.testUtilities as testUtilities
import pymcxray.FileFormat.Version as Version

# Globals and constants variables.

class TestResultsParameters(unittest.TestCase):
    """
    TestCase class for the module `ResultsParameters`.
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

    def test_read(self):
        """
        Tests for method `read`.
        """
        raise SkipTest

        for title in testUtilities.getSimulationTitles():
            resultsParameters = ResultsParameters.ResultsParameters()

            filepath = os.path.abspath(os.path.join(self.testDataPath, "%s/%s.rp" % (title, title)))
            resultsParameters.read(filepath)

            resultsParametersRef = self.getSimulationParametersReference(title)
            self.assertEquals(resultsParametersRef.isComputeXrayCharacteristic, resultsParameters.isComputeXrayCharacteristic)
            self.assertEquals(resultsParametersRef.isComputeXrayBremsstrahlung, resultsParameters.isComputeXrayBremsstrahlung)
            self.assertEquals(resultsParametersRef.isComputeXrayPhirhoz, resultsParameters.isComputeXrayPhirhoz)

        self.fail("Test if the testcase is working.")

    def test_read_1_4_1(self):
        """
        Tests for method `read`.
        """

        resultsParameters = ResultsParameters.ResultsParameters()

        title = "AlMgBulk5keV_version_1_4_1"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.rp" % (title)))
        resultsParameters.read(filepath)

        self.assertEquals(Version.VERSION_1_4_1.major, resultsParameters.version.major)
        self.assertEquals(Version.VERSION_1_4_1.minor, resultsParameters.version.minor)
        self.assertEquals(Version.VERSION_1_4_1.revision, resultsParameters.version.revision)
        self.assertEquals(Version.VERSION_1_4_1, resultsParameters.version)

        resultsParametersRef = self.getSimulationParametersReference(title)
        self.assertEquals(resultsParametersRef.version.major, resultsParameters.version.major)
        self.assertEquals(resultsParametersRef.version.minor, resultsParameters.version.minor)
        self.assertEquals(resultsParametersRef.version.revision, resultsParameters.version.revision)
        self.assertEquals(resultsParametersRef.version, resultsParameters.version)

        self.assertEquals(resultsParametersRef.isComputeXrayCharacteristic, resultsParameters.isComputeXrayCharacteristic)
        self.assertEquals(resultsParametersRef.isComputeXrayBremsstrahlung, resultsParameters.isComputeXrayBremsstrahlung)
        self.assertEquals(resultsParametersRef.isComputeXrayPhirhoz, resultsParameters.isComputeXrayPhirhoz)

        #self.fail("Test if the testcase is working.")

    def test_read_1_4_3(self):
        """
        Tests for method `read`.
        """

        resultsParameters = ResultsParameters.ResultsParameters()

        title = "AlMgBulk5keV_version_1_4_3"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.rp" % (title)))
        resultsParameters.read(filepath)

        self.assertEquals(Version.VERSION_1_4_3.major, resultsParameters.version.major)
        self.assertEquals(Version.VERSION_1_4_3.minor, resultsParameters.version.minor)
        self.assertEquals(Version.VERSION_1_4_3.revision, resultsParameters.version.revision)
        self.assertEquals(Version.VERSION_1_4_3, resultsParameters.version)

        resultsParametersRef = self.getSimulationParametersReference(title)
        self.assertEquals(resultsParametersRef.version.major, resultsParameters.version.major)
        self.assertEquals(resultsParametersRef.version.minor, resultsParameters.version.minor)
        self.assertEquals(resultsParametersRef.version.revision, resultsParameters.version.revision)
        self.assertEquals(resultsParametersRef.version, resultsParameters.version)

        self.assertEquals(resultsParametersRef.isComputeXrayCharacteristic, resultsParameters.isComputeXrayCharacteristic)
        self.assertEquals(resultsParametersRef.isComputeXrayBremsstrahlung, resultsParameters.isComputeXrayBremsstrahlung)
        self.assertEquals(resultsParametersRef.isComputeXrayPhirhoz, resultsParameters.isComputeXrayPhirhoz)
        self.assertEquals(resultsParametersRef.isComputeXraySimulatedSpectrum, resultsParameters.isComputeXraySimulatedSpectrum)

        #self.fail("Test if the testcase is working.")

    def getSimulationParametersReference(self, title):
        resultsParameters = ResultsParameters.ResultsParameters()

        if title == "AlMgBulk5keV_version_1_2_1":
            resultsParameters.version = Version.Version(1, 2, 1)
            resultsParameters.isComputeXrayCharacteristic = None
            resultsParameters.isComputeXrayBremsstrahlung = None
            resultsParameters.isComputeXrayPhirhoz = None
        elif title == "AlMgBulk5keV_version_1_4_1":
            resultsParameters.version = Version.Version(1, 4, 1)
            resultsParameters.isComputeXrayCharacteristic = True
            resultsParameters.isComputeXrayBremsstrahlung = True
            resultsParameters.isComputeXrayPhirhoz = True
        elif title == "AlMgBulk5keV_version_1_4_3":
            resultsParameters.version = Version.Version(1, 4, 3)
            resultsParameters.isComputeXrayCharacteristic = True
            resultsParameters.isComputeXrayBremsstrahlung = False
            resultsParameters.isComputeXrayPhirhoz = False
            resultsParameters.isComputeXraySimulatedSpectrum = False

        return resultsParameters

    def test_write(self):
        """
        Tests for method `write`.
        """
        raise SkipTest

        self.maxDiff = None

        for title in testUtilities.getSimulationTitles():
            resultsParametersRef = self.getSimulationParametersReference(title)

            filepathReference = os.path.abspath(os.path.join(self.testDataPath, "%s/%s.rp" % (title, title)))

            filepath = os.path.join(self.tempDataPath, "%s.rp" % (title))
            resultsParameters = ResultsParameters.ResultsParameters()
            resultsParameters = resultsParametersRef

            resultsParameters.write(filepath)

            self.assertEquals(resultsParametersRef.isComputeXrayCharacteristic, resultsParameters.isComputeXrayCharacteristic)
            self.assertEquals(resultsParametersRef.isComputeXrayBremsstrahlung, resultsParameters.isComputeXrayBremsstrahlung)
            self.assertEquals(resultsParametersRef.isComputeXrayPhirhoz, resultsParameters.isComputeXrayPhirhoz)

            linesRef = open(filepathReference, 'r').readlines()
            lines = open(filepath, 'r').readlines()

            self.assertListEqual(linesRef, lines)

        self.fail("Test if the testcase is working.")

    def test_write_1_4_1(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        title = "AlMgBulk5keV_version_1_4_1"
        resultsParametersRef = self.getSimulationParametersReference(title)

        filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.rp" % (title)))

        filepath = os.path.join(self.tempDataPath, "%s.rp" % (title))
        resultsParameters = resultsParametersRef
        resultsParameters.version = Version.VERSION_1_4_1

        resultsParameters.write(filepath)

        self.assertEquals(resultsParametersRef.isComputeXrayCharacteristic, resultsParameters.isComputeXrayCharacteristic)
        self.assertEquals(resultsParametersRef.isComputeXrayBremsstrahlung, resultsParameters.isComputeXrayBremsstrahlung)
        self.assertEquals(resultsParametersRef.isComputeXrayPhirhoz, resultsParameters.isComputeXrayPhirhoz)

        self.assertEquals(resultsParametersRef.version.major, resultsParameters.version.major)
        self.assertEquals(resultsParametersRef.version.minor, resultsParameters.version.minor)
        self.assertEquals(resultsParametersRef.version.revision, resultsParameters.version.revision)
        self.assertEquals(resultsParametersRef.version, resultsParameters.version)

        linesRef = open(filepathReference, 'r').readlines()
        lines = open(filepath, 'r').readlines()

        self.assertListEqual(linesRef, lines)

        #self.fail("Test if the testcase is working.")

    def test_write_1_4_3(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        title = "AlMgBulk5keV_version_1_4_3"
        resultsParametersRef = self.getSimulationParametersReference(title)

        filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.rp" % (title)))

        filepath = os.path.join(self.tempDataPath, "%s.rp" % (title))
        resultsParameters = resultsParametersRef
        resultsParameters.version = Version.VERSION_1_4_3

        resultsParameters.write(filepath)

        self.assertEquals(resultsParametersRef.isComputeXrayCharacteristic, resultsParameters.isComputeXrayCharacteristic)
        self.assertEquals(resultsParametersRef.isComputeXrayBremsstrahlung, resultsParameters.isComputeXrayBremsstrahlung)
        self.assertEquals(resultsParametersRef.isComputeXrayPhirhoz, resultsParameters.isComputeXrayPhirhoz)
        self.assertEquals(resultsParametersRef.isComputeXraySimulatedSpectrum, resultsParameters.isComputeXraySimulatedSpectrum)

        self.assertEquals(resultsParametersRef.version.major, resultsParameters.version.major)
        self.assertEquals(resultsParametersRef.version.minor, resultsParameters.version.minor)
        self.assertEquals(resultsParametersRef.version.revision, resultsParameters.version.revision)
        self.assertEquals(resultsParametersRef.version, resultsParameters.version)

        linesRef = open(filepathReference, 'r').readlines()
        lines = open(filepath, 'r').readlines()

        self.assertListEqual(linesRef, lines)

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    import nose
    nose.runmodule()
