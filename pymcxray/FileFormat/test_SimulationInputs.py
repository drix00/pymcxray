#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.test_SimulationInputs
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Test the module `SimulationInputs`.
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
import os.path
import copy

# Third party modules.
from nose.plugins.skip import SkipTest

# Local modules.

# Project modules
import pymcxray.FileFormat.SimulationInputs as SimulationInputs
import pymcxray.FileFormat.testUtilities as testUtilities
import pymcxray.FileFormat.Version as Version

# Globals and constants variables.

class TestSimulationInputs(unittest.TestCase):
    """
    TestCase class for the module `moduleName`.
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

        simulationInputs = SimulationInputs.SimulationInputs()

        for title in testUtilities.getSimulationTitles():
            filepath = os.path.abspath(os.path.join(self.testDataPath, "%s/%s.sim" % (title, title)))
            simulationInputs.read(filepath)

            self.assertEquals(title, simulationInputs.title)

            self.assertEquals("%s.sam" % (title), simulationInputs.specimenFilename)
            self.assertEquals("%s.mdl" % (title), simulationInputs.modelFilename)
            self.assertEquals("%s.mic" % (title), simulationInputs.microsopeFilename)
            self.assertEquals("%s.par" % (title), simulationInputs.simulationParametersFilename)

        #self.fail("Test if the testcase is working.")

    def test_read_1_1_1(self):
        """
        Tests for method `read`.
        """

        simulationInputs = SimulationInputs.SimulationInputs()

        title = "AlMgBulk5keV_version_1_1_1"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.sim" % (title)))
        simulationInputs.read(filepath)

        self.assertEquals(title, simulationInputs.title)

        self.assertEquals(Version.VERSION_1_1_1.major, simulationInputs.version.major)
        self.assertEquals(Version.VERSION_1_1_1.minor, simulationInputs.version.minor)
        self.assertEquals(Version.VERSION_1_1_1.revision, simulationInputs.version.revision)
        self.assertEquals(Version.VERSION_1_1_1, simulationInputs.version)

        self.assertEquals("%s.sam" % (title), simulationInputs.specimenFilename)
        self.assertEquals("%s.mdl" % (title), simulationInputs.modelFilename)
        self.assertEquals("%s.mic" % (title), simulationInputs.microsopeFilename)
        self.assertEquals("%s.par" % (title), simulationInputs.simulationParametersFilename)

        #self.fail("Test if the testcase is working.")

    def test_read_1_2_0(self):
        """
        Tests for method `read`.
        """

        simulationInputs = SimulationInputs.SimulationInputs()

        title = "AlMgBulk5keV_version_1_2_0"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.sim" % (title)))
        simulationInputs.read(filepath)

        self.assertEquals(title, simulationInputs.title)

        self.assertEquals(Version.VERSION_1_2_0.major, simulationInputs.version.major)
        self.assertEquals(Version.VERSION_1_2_0.minor, simulationInputs.version.minor)
        self.assertEquals(Version.VERSION_1_2_0.revision, simulationInputs.version.revision)
        self.assertEquals(Version.VERSION_1_2_0, simulationInputs.version)

        self.assertEquals("%s.sam" % (title), simulationInputs.specimenFilename)
        self.assertEquals("%s.mdl" % (title), simulationInputs.modelFilename)
        self.assertEquals("%s.mic" % (title), simulationInputs.microsopeFilename)
        self.assertEquals("%s.par" % (title), simulationInputs.simulationParametersFilename)

        #self.fail("Test if the testcase is working.")

    def test_read_1_2_1(self):
        """
        Tests for method `read`.
        """

        simulationInputs = SimulationInputs.SimulationInputs()

        title = "AlMgBulk5keV_version_1_2_1"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.sim" % (title)))
        simulationInputs.read(filepath)

        self.assertEquals(title, simulationInputs.title)

        self.assertEquals(Version.VERSION_1_2_1.major, simulationInputs.version.major)
        self.assertEquals(Version.VERSION_1_2_1.minor, simulationInputs.version.minor)
        self.assertEquals(Version.VERSION_1_2_1.revision, simulationInputs.version.revision)
        self.assertEquals(Version.VERSION_1_2_1, simulationInputs.version)

        self.assertEquals("%s.sam" % (title), simulationInputs.specimenFilename)
        self.assertEquals("%s.mdl" % (title), simulationInputs.modelFilename)
        self.assertEquals("%s.mic" % (title), simulationInputs.microsopeFilename)
        self.assertEquals("%s.par" % (title), simulationInputs.simulationParametersFilename)
        self.assertEquals("%s.mpp" % (title), simulationInputs.mapFilename)

        #self.fail("Test if the testcase is working.")

    def test_read_1_4_1(self):
        """
        Tests for method `read`.
        """

        simulationInputs = SimulationInputs.SimulationInputs()

        title = "AlMgBulk5keV_version_1_4_1"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.sim" % (title)))
        simulationInputs.read(filepath)

        self.assertEquals(title, simulationInputs.title)

        self.assertEquals(Version.VERSION_1_4_1.major, simulationInputs.version.major)
        self.assertEquals(Version.VERSION_1_4_1.minor, simulationInputs.version.minor)
        self.assertEquals(Version.VERSION_1_4_1.revision, simulationInputs.version.revision)
        self.assertEquals(Version.VERSION_1_4_1, simulationInputs.version)

        self.assertEquals("%s.sam" % (title), simulationInputs.specimenFilename)
        self.assertEquals("%s.mdl" % (title), simulationInputs.modelFilename)
        self.assertEquals("%s.mic" % (title), simulationInputs.microsopeFilename)
        self.assertEquals("%s.par" % (title), simulationInputs.simulationParametersFilename)
        self.assertEquals("%s.mpp" % (title), simulationInputs.mapFilename)
        self.assertEquals("%s.rp" % (title), simulationInputs.resultParametersFilename)

        #self.fail("Test if the testcase is working.")

    def test__createKeys(self):
        """
        Tests for method `_createKeys`.
        """

        numberKeys = 6

        keys = SimulationInputs.SimulationInputs()._createKeys()
        self.assertEquals(numberKeys, len(keys))

        #self.fail("Test if the testcase is working.")

    def test_write(self):
        """
        Tests for method `write`.
        """
        raise SkipTest

        self.maxDiff = None

        # todo: make test pass using testUtilities.getSimulationTitles().
        for title in ["BioRitchieNew111017"]:
            filepathReference = os.path.abspath(os.path.join(self.testDataPath, "%s/%s.sim" % (title, title)))

            filepath = os.path.join(self.tempDataPath, "%s.sim" % (title))
            simulationInputs = SimulationInputs.SimulationInputs()
            simulationInputs.write(filepath)

            self.assertEquals("%s.sam" % (title), simulationInputs.specimenFilename)
            self.assertEquals("%s.mdl" % (title), simulationInputs.modelFilename)
            self.assertEquals("%s.mic" % (title), simulationInputs.microsopeFilename)
            self.assertEquals("%s.par" % (title), simulationInputs.simulationParametersFilename)

            linesRef = open(filepathReference, 'r').readlines()
            lines = open(filepath, 'r').readlines()

            self.assertListEqual(linesRef, lines)

        #self.fail("Test if the testcase is working.")

    def test_write_1_1_1(self):
        """
        Tests for method `write`.
        """
        raise SkipTest

        self.maxDiff = None

        simulationInputsRef = SimulationInputs.SimulationInputs()
        simulationInputsRef.version = copy.deepcopy(Version.VERSION_1_1_1)

        title = "AlMgBulk5keV_version_1_1_1"
        filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.sim" % (title)))
        simulationInputsRef.read(filepathReference)

        self.assertEquals(title, simulationInputsRef.title)

        filepath = os.path.join(self.tempDataPath, "%s.sim" % (title))
        simulationInputs = SimulationInputs.SimulationInputs()
        simulationInputs.version = copy.deepcopy(Version.VERSION_1_1_1)
        simulationInputs.write(filepath)

        self.assertEquals("%s.sam" % (title), simulationInputs.specimenFilename)
        self.assertEquals("%s.mdl" % (title), simulationInputs.modelFilename)
        self.assertEquals("%s.mic" % (title), simulationInputs.microsopeFilename)
        self.assertEquals("%s.par" % (title), simulationInputs.simulationParametersFilename)

        self.assertEquals(simulationInputsRef.version.major, simulationInputs.version.major)
        self.assertEquals(simulationInputsRef.version.minor, simulationInputs.version.minor)
        self.assertEquals(simulationInputsRef.version.revision, simulationInputs.version.revision)
        self.assertEquals(simulationInputsRef.version, simulationInputs.version)

        linesRef = open(filepathReference, 'r').readlines()
        lines = open(filepath, 'r').readlines()

        self.assertListEqual(linesRef, lines)

        self.fail("Test if the testcase is working.")

    def test_write_1_2_0(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        simulationInputsRef = SimulationInputs.SimulationInputs()
        simulationInputsRef.version = copy.deepcopy(Version.VERSION_1_2_0)

        title = "AlMgBulk5keV_version_1_2_0"
        filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.sim" % (title)))
        simulationInputsRef.read(filepathReference)

        self.assertEquals(title, simulationInputsRef.title)

        filepath = os.path.join(self.tempDataPath, "%s.sim" % (title))
        simulationInputs = SimulationInputs.SimulationInputs()
        simulationInputs.version = copy.deepcopy(Version.VERSION_1_2_0)
        simulationInputs.write(filepath)

        self.assertEquals("%s.sam" % (title), simulationInputs.specimenFilename)
        self.assertEquals("%s.mdl" % (title), simulationInputs.modelFilename)
        self.assertEquals("%s.mic" % (title), simulationInputs.microsopeFilename)
        self.assertEquals("%s.par" % (title), simulationInputs.simulationParametersFilename)

        self.assertEquals(simulationInputsRef.version.major, simulationInputs.version.major)
        self.assertEquals(simulationInputsRef.version.minor, simulationInputs.version.minor)
        self.assertEquals(simulationInputsRef.version.revision, simulationInputs.version.revision)
        self.assertEquals(simulationInputsRef.version, simulationInputs.version)

        linesRef = open(filepathReference, 'r').readlines()
        lines = open(filepath, 'r').readlines()

        self.assertListEqual(linesRef, lines)

        #self.fail("Test if the testcase is working.")

    def test_write_1_2_1(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        simulationInputsRef = SimulationInputs.SimulationInputs()
        simulationInputsRef.version = copy.deepcopy(Version.VERSION_1_2_1)

        title = "AlMgBulk5keV_version_1_2_1"
        filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.sim" % (title)))
        simulationInputsRef.read(filepathReference)

        self.assertEquals(title, simulationInputsRef.title)

        filepath = os.path.join(self.tempDataPath, "%s.sim" % (title))
        simulationInputs = SimulationInputs.SimulationInputs()
        simulationInputs.version = copy.deepcopy(Version.VERSION_1_2_1)
        simulationInputs.write(filepath)

        self.assertEquals("%s.sam" % (title), simulationInputs.specimenFilename)
        self.assertEquals("%s.mdl" % (title), simulationInputs.modelFilename)
        self.assertEquals("%s.mic" % (title), simulationInputs.microsopeFilename)
        self.assertEquals("%s.par" % (title), simulationInputs.simulationParametersFilename)

        self.assertEquals(simulationInputsRef.version.major, simulationInputs.version.major)
        self.assertEquals(simulationInputsRef.version.minor, simulationInputs.version.minor)
        self.assertEquals(simulationInputsRef.version.revision, simulationInputs.version.revision)
        self.assertEquals(simulationInputsRef.version, simulationInputs.version)

        linesRef = open(filepathReference, 'r').readlines()
        lines = open(filepath, 'r').readlines()

        self.assertListEqual(linesRef, lines)

        #self.fail("Test if the testcase is working.")

    def test_write_1_4_1(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        simulationInputsRef = SimulationInputs.SimulationInputs()
        simulationInputsRef.version = copy.deepcopy(Version.VERSION_1_4_1)

        title = "AlMgBulk5keV_version_1_4_1"
        filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.sim" % (title)))
        simulationInputsRef.read(filepathReference)

        self.assertEquals(title, simulationInputsRef.title)

        filepath = os.path.join(self.tempDataPath, "%s.sim" % (title))
        simulationInputs = SimulationInputs.SimulationInputs()
        simulationInputs.version = Version.Version(1, 4, 1)
        simulationInputs.write(filepath)

        self.assertEquals("%s.sam" % (title), simulationInputs.specimenFilename)
        self.assertEquals("%s.mdl" % (title), simulationInputs.modelFilename)
        self.assertEquals("%s.mic" % (title), simulationInputs.microsopeFilename)
        self.assertEquals("%s.par" % (title), simulationInputs.simulationParametersFilename)
        self.assertEquals("%s.mpp" % (title), simulationInputs.mapFilename)
        self.assertEquals("%s.rp" % (title), simulationInputs.resultParametersFilename)

        self.assertEquals(simulationInputsRef.version.major, simulationInputs.version.major)
        self.assertEquals(simulationInputsRef.version.minor, simulationInputs.version.minor)
        self.assertEquals(simulationInputsRef.version.revision, simulationInputs.version.revision)
        self.assertEquals(simulationInputsRef.version, simulationInputs.version)

        linesRef = open(filepathReference, 'r').readlines()
        lines = open(filepath, 'r').readlines()

        self.assertListEqual(linesRef, lines)

        #self.fail("Test if the testcase is working.")

    def test__extractTitleFromFilepath(self):
        """
        Tests for method `_extractTitleFromFilepath`.
        """

        simulationInputs = SimulationInputs.SimulationInputs()

        for titleRef in testUtilities.getSimulationTitles():
            filepath = os.path.abspath(os.path.join(self.testDataPath, "%s/%s.sim" % (titleRef, titleRef)))
            title = simulationInputs._extractTitleFromFilepath(filepath)

            self.assertEquals(titleRef, title)

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    import nose
    nose.runmodule()
