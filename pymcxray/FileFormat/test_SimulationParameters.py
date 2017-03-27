#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.test_SimulationParameters
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for module `SimulationParameters`.
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
import pymcxray.FileFormat.SimulationParameters as SimulationParameters
import pymcxray.FileFormat.testUtilities as testUtilities
import pymcxray.FileFormat.Version as Version

# Globals and constants variables.

class TestSimulationParameters(unittest.TestCase):
    """
    TestCase class for the module `SimulationParameters`.
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

        for title in testUtilities.getSimulationTitles():
            simulationParameters = SimulationParameters.SimulationParameters()

            filepath = os.path.abspath(os.path.join(self.testDataPath, "%s/%s.par" % (title, title)))
            simulationParameters.read(filepath)

            simulationParametersRef = self.getSimulationParametersReference(title)
            self.assertEquals(simulationParametersRef.baseFilename, simulationParameters.baseFilename)
            self.assertEquals(simulationParametersRef.numberElectrons, simulationParameters.numberElectrons)
            self.assertEquals(simulationParametersRef.numberPhotons, simulationParameters.numberPhotons)
            self.assertEquals(simulationParametersRef.numberWindows, simulationParameters.numberWindows)
            self.assertEquals(simulationParametersRef.numberFilmsX, simulationParameters.numberFilmsX)
            self.assertEquals(simulationParametersRef.numberFilmsY, simulationParameters.numberFilmsY)
            self.assertEquals(simulationParametersRef.numberFilmsZ, simulationParameters.numberFilmsZ)
            self.assertEquals(simulationParametersRef.numberChannels, simulationParameters.numberChannels)
            self.assertEquals(simulationParametersRef.energyChannelWidth_eV, simulationParameters.energyChannelWidth_eV)
            self.assertEquals(simulationParametersRef.spectrumInterpolationModel, simulationParameters.spectrumInterpolationModel)
            self.assertEquals(simulationParametersRef.voxelSimplification, simulationParameters.voxelSimplification, title)

        #self.fail("Test if the testcase is working.")

    def test_read_1_1_1(self):
        """
        Tests for method `read`.
        """

        simulationParameters = SimulationParameters.SimulationParameters()

        title = "AlMgBulk5keV_version_1_1_1"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.par" % (title)))
        simulationParameters.read(filepath)

        self.assertEquals(Version.VERSION_1_1_1.major, simulationParameters.version.major)
        self.assertEquals(Version.VERSION_1_1_1.minor, simulationParameters.version.minor)
        self.assertEquals(Version.VERSION_1_1_1.revision, simulationParameters.version.revision)
        self.assertEquals(Version.VERSION_1_1_1, simulationParameters.version)

        simulationParametersRef = self.getSimulationParametersReference(title)
        self.assertEquals(simulationParametersRef.version.major, simulationParameters.version.major)
        self.assertEquals(simulationParametersRef.version.minor, simulationParameters.version.minor)
        self.assertEquals(simulationParametersRef.version.revision, simulationParameters.version.revision)
        self.assertEquals(simulationParametersRef.version, simulationParameters.version)

        self.assertEquals(simulationParametersRef.baseFilename, simulationParameters.baseFilename)
        self.assertEquals(simulationParametersRef.numberElectrons, simulationParameters.numberElectrons)
        self.assertEquals(simulationParametersRef.numberPhotons, simulationParameters.numberPhotons)
        self.assertEquals(simulationParametersRef.numberWindows, simulationParameters.numberWindows)
        self.assertEquals(simulationParametersRef.numberFilmsX, simulationParameters.numberFilmsX)
        self.assertEquals(simulationParametersRef.numberFilmsY, simulationParameters.numberFilmsY)
        self.assertEquals(simulationParametersRef.numberFilmsZ, simulationParameters.numberFilmsZ)
        self.assertEquals(simulationParametersRef.numberChannels, simulationParameters.numberChannels)
        self.assertEquals(simulationParametersRef.energyChannelWidth_eV, simulationParameters.energyChannelWidth_eV)
        self.assertEquals(simulationParametersRef.spectrumInterpolationModel, simulationParameters.spectrumInterpolationModel)
        self.assertEquals(simulationParametersRef.voxelSimplification, simulationParameters.voxelSimplification, title)

        #self.fail("Test if the testcase is working.")

    def test_read_1_2_0(self):
        """
        Tests for method `read`.
        """

        simulationParameters = SimulationParameters.SimulationParameters()

        title = "AlMgBulk5keV_version_1_2_0"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.par" % (title)))
        simulationParameters.read(filepath)

        self.assertEquals(Version.VERSION_1_2_0.major, simulationParameters.version.major)
        self.assertEquals(Version.VERSION_1_2_0.minor, simulationParameters.version.minor)
        self.assertEquals(Version.VERSION_1_2_0.revision, simulationParameters.version.revision)
        self.assertEquals(Version.VERSION_1_2_0, simulationParameters.version)

        simulationParametersRef = self.getSimulationParametersReference(title)
        self.assertEquals(simulationParametersRef.version.major, simulationParameters.version.major)
        self.assertEquals(simulationParametersRef.version.minor, simulationParameters.version.minor)
        self.assertEquals(simulationParametersRef.version.revision, simulationParameters.version.revision)
        self.assertEquals(simulationParametersRef.version, simulationParameters.version)

        self.assertEquals(simulationParametersRef.baseFilename, simulationParameters.baseFilename)
        self.assertEquals(simulationParametersRef.numberElectrons, simulationParameters.numberElectrons)
        self.assertEquals(simulationParametersRef.numberPhotons, simulationParameters.numberPhotons)
        self.assertEquals(simulationParametersRef.numberWindows, simulationParameters.numberWindows)
        self.assertEquals(simulationParametersRef.numberFilmsX, simulationParameters.numberFilmsX)
        self.assertEquals(simulationParametersRef.numberFilmsY, simulationParameters.numberFilmsY)
        self.assertEquals(simulationParametersRef.numberFilmsZ, simulationParameters.numberFilmsZ)
        self.assertEquals(simulationParametersRef.numberChannels, simulationParameters.numberChannels)
        self.assertEquals(simulationParametersRef.energyChannelWidth_eV, simulationParameters.energyChannelWidth_eV)
        self.assertEquals(simulationParametersRef.spectrumInterpolationModel, simulationParameters.spectrumInterpolationModel)
        self.assertEquals(simulationParametersRef.voxelSimplification, simulationParameters.voxelSimplification, title)

        #self.fail("Test if the testcase is working.")

    def test_read_1_2_1(self):
        """
        Tests for method `read`.
        """

        simulationParameters = SimulationParameters.SimulationParameters()

        title = "AlMgBulk5keV_version_1_2_1"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.par" % (title)))
        simulationParameters.read(filepath)

        self.assertEquals(Version.VERSION_1_2_1.major, simulationParameters.version.major)
        self.assertEquals(Version.VERSION_1_2_1.minor, simulationParameters.version.minor)
        self.assertEquals(Version.VERSION_1_2_1.revision, simulationParameters.version.revision)
        self.assertEquals(Version.VERSION_1_2_1, simulationParameters.version)

        simulationParametersRef = self.getSimulationParametersReference(title)
        self.assertEquals(simulationParametersRef.version.major, simulationParameters.version.major)
        self.assertEquals(simulationParametersRef.version.minor, simulationParameters.version.minor)
        self.assertEquals(simulationParametersRef.version.revision, simulationParameters.version.revision)
        self.assertEquals(simulationParametersRef.version, simulationParameters.version)

        self.assertEquals(simulationParametersRef.baseFilename, simulationParameters.baseFilename)
        self.assertEquals(simulationParametersRef.numberElectrons, simulationParameters.numberElectrons)
        self.assertEquals(simulationParametersRef.numberPhotons, simulationParameters.numberPhotons)
        self.assertEquals(simulationParametersRef.numberWindows, simulationParameters.numberWindows)
        self.assertEquals(simulationParametersRef.numberFilmsX, simulationParameters.numberFilmsX)
        self.assertEquals(simulationParametersRef.numberFilmsY, simulationParameters.numberFilmsY)
        self.assertEquals(simulationParametersRef.numberFilmsZ, simulationParameters.numberFilmsZ)
        self.assertEquals(simulationParametersRef.numberChannels, simulationParameters.numberChannels)
        self.assertEquals(simulationParametersRef.energyChannelWidth_eV, simulationParameters.energyChannelWidth_eV)
        self.assertEquals(simulationParametersRef.spectrumInterpolationModel, simulationParameters.spectrumInterpolationModel)
        self.assertEquals(simulationParametersRef.voxelSimplification, simulationParameters.voxelSimplification, title)

        #self.fail("Test if the testcase is working.")

    def test_read_1_4_1(self):
        """
        Tests for method `read`.
        """

        simulationParameters = SimulationParameters.SimulationParameters()

        title = "AlMgBulk5keV_version_1_4_1"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.par" % (title)))
        simulationParameters.read(filepath)

        self.assertEquals(Version.VERSION_1_4_1.major, simulationParameters.version.major)
        self.assertEquals(Version.VERSION_1_4_1.minor, simulationParameters.version.minor)
        self.assertEquals(Version.VERSION_1_4_1.revision, simulationParameters.version.revision)
        self.assertEquals(Version.VERSION_1_4_1, simulationParameters.version)

        simulationParametersRef = self.getSimulationParametersReference(title)
        self.assertEquals(simulationParametersRef.version.major, simulationParameters.version.major)
        self.assertEquals(simulationParametersRef.version.minor, simulationParameters.version.minor)
        self.assertEquals(simulationParametersRef.version.revision, simulationParameters.version.revision)
        self.assertEquals(simulationParametersRef.version, simulationParameters.version)

        self.assertEquals(simulationParametersRef.baseFilename, simulationParameters.baseFilename)
        self.assertEquals(simulationParametersRef.numberElectrons, simulationParameters.numberElectrons)
        self.assertEquals(simulationParametersRef.numberPhotons, simulationParameters.numberPhotons)
        self.assertEquals(simulationParametersRef.numberWindows, simulationParameters.numberWindows)
        self.assertEquals(simulationParametersRef.numberFilmsX, simulationParameters.numberFilmsX)
        self.assertEquals(simulationParametersRef.numberFilmsY, simulationParameters.numberFilmsY)
        self.assertEquals(simulationParametersRef.numberFilmsZ, simulationParameters.numberFilmsZ)
        self.assertEquals(simulationParametersRef.numberChannels, simulationParameters.numberChannels)
        self.assertEquals(simulationParametersRef.energyChannelWidth_eV, simulationParameters.energyChannelWidth_eV)
        self.assertEquals(simulationParametersRef.spectrumInterpolationModel, simulationParameters.spectrumInterpolationModel)
        self.assertEquals(simulationParametersRef.voxelSimplification, simulationParameters.voxelSimplification, title)

        #self.fail("Test if the testcase is working.")

    def test_read_1_4_4(self):
        """
        Tests for method `read`.
        """

        simulationParameters = SimulationParameters.SimulationParameters()

        title = "AlMgBulk5keV_version_1_4_4"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.par" % (title)))
        simulationParameters.read(filepath)

        self.assertEquals(Version.VERSION_1_4_4.major, simulationParameters.version.major)
        self.assertEquals(Version.VERSION_1_4_4.minor, simulationParameters.version.minor)
        self.assertEquals(Version.VERSION_1_4_4.revision, simulationParameters.version.revision)
        self.assertEquals(Version.VERSION_1_4_4, simulationParameters.version)

        simulationParametersRef = self.getSimulationParametersReference(title)
        self.assertEquals(simulationParametersRef.version.major, simulationParameters.version.major)
        self.assertEquals(simulationParametersRef.version.minor, simulationParameters.version.minor)
        self.assertEquals(simulationParametersRef.version.revision, simulationParameters.version.revision)
        self.assertEquals(simulationParametersRef.version, simulationParameters.version)

        self.assertEquals(simulationParametersRef.baseFilename, simulationParameters.baseFilename)
        self.assertEquals(simulationParametersRef.numberElectrons, simulationParameters.numberElectrons)
        self.assertEquals(simulationParametersRef.numberPhotons, simulationParameters.numberPhotons)
        self.assertEquals(simulationParametersRef.numberWindows, simulationParameters.numberWindows)
        self.assertEquals(simulationParametersRef.numberFilmsX, simulationParameters.numberFilmsX)
        self.assertEquals(simulationParametersRef.numberFilmsY, simulationParameters.numberFilmsY)
        self.assertEquals(simulationParametersRef.numberFilmsZ, simulationParameters.numberFilmsZ)
        self.assertEquals(simulationParametersRef.numberChannels, simulationParameters.numberChannels)
        self.assertEquals(simulationParametersRef.energyChannelWidth_eV, simulationParameters.energyChannelWidth_eV)
        self.assertEquals(simulationParametersRef.spectrumInterpolationModel, simulationParameters.spectrumInterpolationModel)
        self.assertEquals(simulationParametersRef.voxelSimplification, simulationParameters.voxelSimplification, title)
        self.assertEquals(simulationParametersRef.elasticCrossSectionScalingFactor, simulationParameters.elasticCrossSectionScalingFactor)
        self.assertEquals(simulationParametersRef.energyLossScalingFactor, simulationParameters.energyLossScalingFactor)

        #self.fail("Test if the testcase is working.")

    def getSimulationParametersReference(self, title):
        simulationParameters = SimulationParameters.SimulationParameters()

        if title == "AuBC cyl":
            baseFilenameRef = r"Results\%s Low Count" % (title)
            simulationParameters.baseFilename = baseFilenameRef
            simulationParameters.numberElectrons = 20
            simulationParameters.numberPhotons = 500
            simulationParameters.numberWindows = 32
            simulationParameters.numberFilmsX = 64
            simulationParameters.numberFilmsY = 64
            simulationParameters.numberFilmsZ = 64
            simulationParameters.numberChannels = 1024
            simulationParameters.spectrumInterpolationModel = 2
            simulationParameters.voxelSimplification = None
        elif title == "BioRitchieNew111017":
            baseFilenameRef = r"Results\Ritchie60"
            simulationParameters.baseFilename = baseFilenameRef
            simulationParameters.numberElectrons = 50
            simulationParameters.numberPhotons = 10000
            simulationParameters.numberWindows = 64
            simulationParameters.numberFilmsX = 128
            simulationParameters.numberFilmsY = 128
            simulationParameters.numberFilmsZ = 128
            simulationParameters.numberChannels = 1024
            simulationParameters.spectrumInterpolationModel = 2
            simulationParameters.voxelSimplification = 1
        elif title == "Bug Al Zr Sphere":
            baseFilenameRef = r"Results\McXRay"
            simulationParameters.baseFilename = baseFilenameRef
            simulationParameters.numberElectrons = 1000
            simulationParameters.numberPhotons = 10000
            simulationParameters.numberWindows = 64
            simulationParameters.numberFilmsX = 128
            simulationParameters.numberFilmsY = 128
            simulationParameters.numberFilmsZ = 128
            simulationParameters.numberChannels = 1024
            simulationParameters.spectrumInterpolationModel = 2
            simulationParameters.voxelSimplification = None
        elif title == "Mg2SiAlCube3kev":
            baseFilenameRef = r"Results\%s" % (title)
            simulationParameters.baseFilename = baseFilenameRef
            simulationParameters.numberElectrons = 30
            simulationParameters.numberPhotons = 1000
            simulationParameters.numberWindows = 32
            simulationParameters.numberFilmsX = 64
            simulationParameters.numberFilmsY = 64
            simulationParameters.numberFilmsZ = 64
            simulationParameters.numberChannels = 1024
            simulationParameters.spectrumInterpolationModel = 2
            simulationParameters.voxelSimplification = None
        elif title == "AlMgBulk5keV_version_1_1_1":
            baseFilenameRef = r"Results\%s" % ("AlMgBulk5keV")
            simulationParameters.baseFilename = baseFilenameRef
            simulationParameters.version = Version.Version(1, 1, 1)
            simulationParameters.numberElectrons = 1000
            simulationParameters.numberPhotons = 127678
            simulationParameters.numberWindows = 64
            simulationParameters.numberFilmsX = 128
            simulationParameters.numberFilmsY = 128
            simulationParameters.numberFilmsZ = 128
            simulationParameters.numberChannels = 1024
            simulationParameters.spectrumInterpolationModel = 2
            simulationParameters.voxelSimplification = None
        elif title == "AlMgBulk5keV_version_1_2_0":
            baseFilenameRef = r"Results\%s" % ("AlMgBulk5keV_1_2_0")
            simulationParameters.baseFilename = baseFilenameRef
            simulationParameters.version = Version.Version(1, 2, 0)
            simulationParameters.numberElectrons = 10000
            simulationParameters.numberPhotons = 1000
            simulationParameters.numberWindows = 128
            simulationParameters.numberFilmsX = 64
            simulationParameters.numberFilmsY = 66
            simulationParameters.numberFilmsZ = 70
            simulationParameters.energyChannelWidth_eV = 5
            simulationParameters.spectrumInterpolationModel = 1
            simulationParameters.voxelSimplification = None
        elif title == "AlMgBulk5keV_version_1_2_1":
            baseFilenameRef = r"Results\%s" % ("AlMgBulk5keV_1_2_1")
            simulationParameters.baseFilename = baseFilenameRef
            simulationParameters.version = Version.Version(1, 2, 1)
            simulationParameters.numberElectrons = 10000
            simulationParameters.numberPhotons = 1000
            simulationParameters.numberWindows = 128
            simulationParameters.numberFilmsX = 64
            simulationParameters.numberFilmsY = 66
            simulationParameters.numberFilmsZ = 70
            simulationParameters.energyChannelWidth_eV = 5
            simulationParameters.spectrumInterpolationModel = 1
            simulationParameters.voxelSimplification = None
        elif title == "AlMgBulk5keV_version_1_4_1":
            baseFilenameRef = r"Results\%s" % ("AlMgBulk5keV_1_4_1")
            simulationParameters.baseFilename = baseFilenameRef
            simulationParameters.version = Version.Version(1, 4, 1)
            simulationParameters.numberElectrons = 10000
            simulationParameters.numberPhotons = 1000
            simulationParameters.numberWindows = 128
            simulationParameters.numberFilmsX = 64
            simulationParameters.numberFilmsY = 66
            simulationParameters.numberFilmsZ = 70
            simulationParameters.energyChannelWidth_eV = 5
            simulationParameters.spectrumInterpolationModel = 1
            simulationParameters.voxelSimplification = None
        elif title == "AlMgBulk5keV_version_1_4_4":
            baseFilenameRef = r"Results\%s" % ("AlMgBulk5keV_1_4_4")
            simulationParameters.baseFilename = baseFilenameRef
            simulationParameters.version = Version.Version(1, 4, 4)
            simulationParameters.numberElectrons = 10000
            simulationParameters.numberPhotons = 1000
            simulationParameters.numberWindows = 128
            simulationParameters.numberFilmsX = 64
            simulationParameters.numberFilmsY = 66
            simulationParameters.numberFilmsZ = 70
            simulationParameters.energyChannelWidth_eV = 5
            simulationParameters.spectrumInterpolationModel = 1
            simulationParameters.voxelSimplification = None
            simulationParameters.elasticCrossSectionScalingFactor = 1.3
            simulationParameters.energyLossScalingFactor = 0.7

        return simulationParameters

    def test__createKeys(self):
        """
        Tests for method `_createKeys`.
        """

        simulationParameters = SimulationParameters.SimulationParameters()

        simulationParameters.version = copy.deepcopy(Version.VERSION_1_4_3)
        numberKeys = 10
        keys = simulationParameters._createKeys()
        self.assertEquals(numberKeys, len(keys))

        simulationParameters.version = copy.deepcopy(Version.VERSION_1_4_4)
        numberKeys = 12
        keys = simulationParameters._createKeys()
        self.assertEquals(numberKeys, len(keys))

        #self.fail("Test if the testcase is working.")

    def test_write(self):
        """
        Tests for method `write`.
        """
        raise SkipTest

        self.maxDiff = None

        for title in testUtilities.getSimulationTitles():
            simulationParametersRef = self.getSimulationParametersReference(title)

            filepathReference = os.path.abspath(os.path.join(self.testDataPath, "%s/%s.par" % (title, title)))

            filepath = os.path.join(self.tempDataPath, "%s.par" % (title))
            simulationParameters = SimulationParameters.SimulationParameters()
            simulationParameters = simulationParametersRef

            simulationParameters.write(filepath)

            self.assertEquals(simulationParametersRef.baseFilename, simulationParameters.baseFilename)
            self.assertEquals(simulationParametersRef.numberElectrons, simulationParameters.numberElectrons)
            self.assertEquals(simulationParametersRef.numberPhotons, simulationParameters.numberPhotons)
            self.assertEquals(simulationParametersRef.numberWindows, simulationParameters.numberWindows)
            self.assertEquals(simulationParametersRef.numberFilmsX, simulationParameters.numberFilmsX)
            self.assertEquals(simulationParametersRef.numberFilmsY, simulationParameters.numberFilmsY)
            self.assertEquals(simulationParametersRef.numberFilmsZ, simulationParameters.numberFilmsZ)
            self.assertEquals(simulationParametersRef.numberChannels, simulationParameters.numberChannels)
            self.assertEquals(simulationParametersRef.energyChannelWidth_eV, simulationParameters.energyChannelWidth_eV)
            self.assertEquals(simulationParametersRef.spectrumInterpolationModel, simulationParameters.spectrumInterpolationModel)
            self.assertEquals(simulationParametersRef.voxelSimplification, simulationParameters.voxelSimplification, title)

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

        title = "AlMgBulk5keV_version_1_1_1"
        simulationParametersRef = self.getSimulationParametersReference(title)

        filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.par" % (title)))

        filepath = os.path.join(self.tempDataPath, "%s.par" % (title))
        simulationParameters = simulationParametersRef

        simulationParameters.write(filepath)

        self.assertEquals(simulationParametersRef.baseFilename, simulationParameters.baseFilename)
        self.assertEquals(simulationParametersRef.numberElectrons, simulationParameters.numberElectrons)
        self.assertEquals(simulationParametersRef.numberPhotons, simulationParameters.numberPhotons)
        self.assertEquals(simulationParametersRef.numberWindows, simulationParameters.numberWindows)
        self.assertEquals(simulationParametersRef.numberFilmsX, simulationParameters.numberFilmsX)
        self.assertEquals(simulationParametersRef.numberFilmsY, simulationParameters.numberFilmsY)
        self.assertEquals(simulationParametersRef.numberFilmsZ, simulationParameters.numberFilmsZ)
        self.assertEquals(simulationParametersRef.numberChannels, simulationParameters.numberChannels)
        self.assertEquals(simulationParametersRef.energyChannelWidth_eV, simulationParameters.energyChannelWidth_eV)
        self.assertEquals(simulationParametersRef.spectrumInterpolationModel, simulationParameters.spectrumInterpolationModel)
        self.assertEquals(simulationParametersRef.voxelSimplification, simulationParameters.voxelSimplification, title)

        self.assertEquals(simulationParametersRef.version.major, simulationParameters.version.major)
        self.assertEquals(simulationParametersRef.version.minor, simulationParameters.version.minor)
        self.assertEquals(simulationParametersRef.version.revision, simulationParameters.version.revision)
        self.assertEquals(simulationParametersRef.version, simulationParameters.version)

        linesRef = open(filepathReference, 'r').readlines()
        lines = open(filepath, 'r').readlines()

        self.assertListEqual(linesRef, lines)

        self.fail("Test if the testcase is working.")

    def test_write_1_2_0(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        title = "AlMgBulk5keV_version_1_2_0"
        simulationParametersRef = self.getSimulationParametersReference(title)

        filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.par" % (title)))

        filepath = os.path.join(self.tempDataPath, "%s.par" % (title))
        simulationParameters = simulationParametersRef
        simulationParameters.version = copy.deepcopy(Version.VERSION_1_2_0)
        simulationParameters.write(filepath)

        self.assertEquals(simulationParametersRef.baseFilename, simulationParameters.baseFilename)
        self.assertEquals(simulationParametersRef.numberElectrons, simulationParameters.numberElectrons)
        self.assertEquals(simulationParametersRef.numberPhotons, simulationParameters.numberPhotons)
        self.assertEquals(simulationParametersRef.numberWindows, simulationParameters.numberWindows)
        self.assertEquals(simulationParametersRef.numberFilmsX, simulationParameters.numberFilmsX)
        self.assertEquals(simulationParametersRef.numberFilmsY, simulationParameters.numberFilmsY)
        self.assertEquals(simulationParametersRef.numberFilmsZ, simulationParameters.numberFilmsZ)
        self.assertEquals(simulationParametersRef.numberChannels, simulationParameters.numberChannels)
        self.assertEquals(simulationParametersRef.energyChannelWidth_eV, simulationParameters.energyChannelWidth_eV)
        self.assertEquals(simulationParametersRef.spectrumInterpolationModel, simulationParameters.spectrumInterpolationModel)
        self.assertEquals(simulationParametersRef.voxelSimplification, simulationParameters.voxelSimplification, title)

        self.assertEquals(simulationParametersRef.version.major, simulationParameters.version.major)
        self.assertEquals(simulationParametersRef.version.minor, simulationParameters.version.minor)
        self.assertEquals(simulationParametersRef.version.revision, simulationParameters.version.revision)
        self.assertEquals(simulationParametersRef.version, simulationParameters.version)

        linesRef = open(filepathReference, 'r').readlines()
        lines = open(filepath, 'r').readlines()

        self.assertListEqual(linesRef, lines)

        #self.fail("Test if the testcase is working.")

    def test_write_1_2_1(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        title = "AlMgBulk5keV_version_1_2_1"
        simulationParametersRef = self.getSimulationParametersReference(title)

        filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.par" % (title)))

        filepath = os.path.join(self.tempDataPath, "%s.par" % (title))
        simulationParameters = simulationParametersRef
        simulationParameters.version = copy.deepcopy(Version.VERSION_1_2_1)

        simulationParameters.write(filepath)

        self.assertEquals(simulationParametersRef.baseFilename, simulationParameters.baseFilename)
        self.assertEquals(simulationParametersRef.numberElectrons, simulationParameters.numberElectrons)
        self.assertEquals(simulationParametersRef.numberPhotons, simulationParameters.numberPhotons)
        self.assertEquals(simulationParametersRef.numberWindows, simulationParameters.numberWindows)
        self.assertEquals(simulationParametersRef.numberFilmsX, simulationParameters.numberFilmsX)
        self.assertEquals(simulationParametersRef.numberFilmsY, simulationParameters.numberFilmsY)
        self.assertEquals(simulationParametersRef.numberFilmsZ, simulationParameters.numberFilmsZ)
        self.assertEquals(simulationParametersRef.numberChannels, simulationParameters.numberChannels)
        self.assertEquals(simulationParametersRef.energyChannelWidth_eV, simulationParameters.energyChannelWidth_eV)
        self.assertEquals(simulationParametersRef.spectrumInterpolationModel, simulationParameters.spectrumInterpolationModel)
        self.assertEquals(simulationParametersRef.voxelSimplification, simulationParameters.voxelSimplification, title)

        self.assertEquals(simulationParametersRef.version.major, simulationParameters.version.major)
        self.assertEquals(simulationParametersRef.version.minor, simulationParameters.version.minor)
        self.assertEquals(simulationParametersRef.version.revision, simulationParameters.version.revision)
        self.assertEquals(simulationParametersRef.version, simulationParameters.version)

        linesRef = open(filepathReference, 'r').readlines()
        lines = open(filepath, 'r').readlines()

        self.assertListEqual(linesRef, lines)

        #self.fail("Test if the testcase is working.")

    def test_write_1_4_1(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        title = "AlMgBulk5keV_version_1_4_1"
        simulationParametersRef = self.getSimulationParametersReference(title)

        filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.par" % (title)))

        filepath = os.path.join(self.tempDataPath, "%s.par" % (title))
        simulationParameters = simulationParametersRef
        simulationParameters.version = copy.deepcopy(Version.VERSION_1_4_1)

        simulationParameters.write(filepath)

        self.assertEquals(simulationParametersRef.baseFilename, simulationParameters.baseFilename)
        self.assertEquals(simulationParametersRef.numberElectrons, simulationParameters.numberElectrons)
        self.assertEquals(simulationParametersRef.numberPhotons, simulationParameters.numberPhotons)
        self.assertEquals(simulationParametersRef.numberWindows, simulationParameters.numberWindows)
        self.assertEquals(simulationParametersRef.numberFilmsX, simulationParameters.numberFilmsX)
        self.assertEquals(simulationParametersRef.numberFilmsY, simulationParameters.numberFilmsY)
        self.assertEquals(simulationParametersRef.numberFilmsZ, simulationParameters.numberFilmsZ)
        self.assertEquals(simulationParametersRef.numberChannels, simulationParameters.numberChannels)
        self.assertEquals(simulationParametersRef.energyChannelWidth_eV, simulationParameters.energyChannelWidth_eV)
        self.assertEquals(simulationParametersRef.spectrumInterpolationModel, simulationParameters.spectrumInterpolationModel)
        self.assertEquals(simulationParametersRef.voxelSimplification, simulationParameters.voxelSimplification, title)

        self.assertEquals(simulationParametersRef.version.major, simulationParameters.version.major)
        self.assertEquals(simulationParametersRef.version.minor, simulationParameters.version.minor)
        self.assertEquals(simulationParametersRef.version.revision, simulationParameters.version.revision)
        self.assertEquals(simulationParametersRef.version, simulationParameters.version)

        linesRef = open(filepathReference, 'r').readlines()
        lines = open(filepath, 'r').readlines()

        self.assertListEqual(linesRef, lines)

        #self.fail("Test if the testcase is working.")

    def test_write_1_4_4(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        title = "AlMgBulk5keV_version_1_4_4"
        simulationParametersRef = self.getSimulationParametersReference(title)

        filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.par" % (title)))

        filepath = os.path.join(self.tempDataPath, "%s.par" % (title))
        simulationParameters = simulationParametersRef
        simulationParameters.version = copy.deepcopy(Version.VERSION_1_4_4)

        simulationParameters.write(filepath)

        self.assertEquals(simulationParametersRef.baseFilename, simulationParameters.baseFilename)
        self.assertEquals(simulationParametersRef.numberElectrons, simulationParameters.numberElectrons)
        self.assertEquals(simulationParametersRef.numberPhotons, simulationParameters.numberPhotons)
        self.assertEquals(simulationParametersRef.numberWindows, simulationParameters.numberWindows)
        self.assertEquals(simulationParametersRef.numberFilmsX, simulationParameters.numberFilmsX)
        self.assertEquals(simulationParametersRef.numberFilmsY, simulationParameters.numberFilmsY)
        self.assertEquals(simulationParametersRef.numberFilmsZ, simulationParameters.numberFilmsZ)
        self.assertEquals(simulationParametersRef.numberChannels, simulationParameters.numberChannels)
        self.assertEquals(simulationParametersRef.energyChannelWidth_eV, simulationParameters.energyChannelWidth_eV)
        self.assertEquals(simulationParametersRef.spectrumInterpolationModel, simulationParameters.spectrumInterpolationModel)
        self.assertEquals(simulationParametersRef.voxelSimplification, simulationParameters.voxelSimplification, title)
        self.assertEquals(simulationParametersRef.elasticCrossSectionScalingFactor, simulationParameters.elasticCrossSectionScalingFactor)
        self.assertEquals(simulationParametersRef.energyLossScalingFactor, simulationParameters.energyLossScalingFactor)

        self.assertEquals(simulationParametersRef.version.major, simulationParameters.version.major)
        self.assertEquals(simulationParametersRef.version.minor, simulationParameters.version.minor)
        self.assertEquals(simulationParametersRef.version.revision, simulationParameters.version.revision)
        self.assertEquals(simulationParametersRef.version, simulationParameters.version)

        linesRef = open(filepathReference, 'r').readlines()
        lines = open(filepath, 'r').readlines()

        self.assertListEqual(linesRef, lines)

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    import nose
    nose.runmodule()
