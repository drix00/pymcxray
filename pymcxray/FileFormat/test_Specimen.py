#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.test_Specimen
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for module `Specimen`.
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
import pymcxray.FileFormat.Specimen as Specimen
import pymcxray.FileFormat.testUtilities as testUtilities
import pymcxray.FileFormat.Region as Region
import pymcxray.FileFormat.Element as Element
import pymcxray.FileFormat.RegionType as RegionType
import pymcxray.FileFormat.RegionDimensions as RegionDimensions
import pymcxray.FileFormat.Version as Version

# Globals and constants variables.

class TestSpecimen(unittest.TestCase):
    """
    TestCase class for the module `Specimen`.
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
            logging.info(title)

            specimen = Specimen.Specimen()

            filepath = os.path.abspath(os.path.join(self.testDataPath, "%s/%s.sam" % (title, title)))
            specimen.read(filepath)

            self.assertEquals(Version.VERSION_1_1_1.major, specimen.version.major)
            self.assertEquals(Version.VERSION_1_1_1.minor, specimen.version.minor)
            self.assertEquals(Version.VERSION_1_1_1.revision, specimen.version.revision)
            self.assertEquals(Version.VERSION_1_1_1, specimen.version)

            specimenRef = self.getSpecimenReference(title)

            self.assertEquals(specimenRef.version.major, specimen.version.major)
            self.assertEquals(specimenRef.version.minor, specimen.version.minor, title)
            self.assertEquals(specimenRef.version.revision, specimen.version.revision)
            self.assertEquals(specimenRef.version, specimen.version)

            self.assertEquals(specimenRef.numberRegions, specimen.numberRegions)

        #self.fail("Test if the testcase is working.")

    def test_read_1_1_1(self):
        """
        Tests for method `read`.
        """

        specimen = Specimen.Specimen()

        title = "AlMgBulk5keV_version_1_1_1"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.sam" % (title)))
        specimen.read(filepath)

        self.assertEquals(Version.VERSION_1_1_1.major, specimen.version.major)
        self.assertEquals(Version.VERSION_1_1_1.minor, specimen.version.minor)
        self.assertEquals(Version.VERSION_1_1_1.revision, specimen.version.revision)
        self.assertEquals(Version.VERSION_1_1_1, specimen.version)

        specimenRef = self.getSpecimenReference(title)
        self.assertEquals(specimenRef.version.major, specimen.version.major)
        self.assertEquals(specimenRef.version.minor, specimen.version.minor)
        self.assertEquals(specimenRef.version.revision, specimen.version.revision)
        self.assertEquals(specimenRef.version, specimen.version)

        self.assertEquals(specimenRef.numberRegions, specimen.numberRegions)

        indexRegion = 0
        region = specimen.regions[indexRegion]
        regionRef = specimenRef.regions[indexRegion]
        self.assertEquals(regionRef.numberElements, region.numberElements)
        self.assertEquals(regionRef.regionMassDensity_g_cm3, region.regionMassDensity_g_cm3)
        self.assertEquals(regionRef.regionType, region.regionType)
        self.assertEquals(regionRef.regionDimensions, region.regionDimensions)
        indexElement = 0
        element = region.elements[indexElement]
        elementRef = regionRef.elements[indexElement]
        self.assertEquals(elementRef.atomicNumber, element.atomicNumber)
        self.assertEquals(elementRef.massFraction, element.massFraction)
        indexElement = 1
        element = region.elements[indexElement]
        elementRef = regionRef.elements[indexElement]
        self.assertEquals(elementRef.atomicNumber, element.atomicNumber)
        self.assertEquals(elementRef.massFraction, element.massFraction)

        indexRegion = 1
        region = specimen.regions[indexRegion]
        regionRef = specimenRef.regions[indexRegion]
        self.assertEquals(regionRef.numberElements, region.numberElements)
        self.assertEquals(regionRef.regionMassDensity_g_cm3, region.regionMassDensity_g_cm3)
        self.assertEquals(regionRef.regionType, region.regionType)
        self.assertEquals(regionRef.regionDimensions, region.regionDimensions)
        indexElement = 0
        element = region.elements[indexElement]
        elementRef = regionRef.elements[indexElement]
        self.assertEquals(elementRef.atomicNumber, element.atomicNumber)
        self.assertEquals(elementRef.massFraction, element.massFraction)

        indexRegion = 2
        region = specimen.regions[indexRegion]
        regionRef = specimenRef.regions[indexRegion]
        self.assertEquals(regionRef.numberElements, region.numberElements)
        self.assertEquals(regionRef.regionMassDensity_g_cm3, region.regionMassDensity_g_cm3)
        self.assertEquals(regionRef.regionType, region.regionType)
        self.assertEquals(regionRef.regionDimensions, region.regionDimensions)
        indexElement = 0
        element = region.elements[indexElement]
        elementRef = regionRef.elements[indexElement]
        self.assertEquals(elementRef.atomicNumber, element.atomicNumber)
        self.assertEquals(elementRef.massFraction, element.massFraction)

        #self.fail("Test if the testcase is working.")

    def test_read_1_2_0(self):
        """
        Tests for method `read`.
        """

        specimen = Specimen.Specimen()

        title = "AlMgBulk5keV_version_1_2_0"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.sam" % (title)))
        specimen.read(filepath)

        self.assertEquals(Version.VERSION_1_2_0.major, specimen.version.major)
        self.assertEquals(Version.VERSION_1_2_0.minor, specimen.version.minor)
        self.assertEquals(Version.VERSION_1_2_0.revision, specimen.version.revision)
        self.assertEquals(Version.VERSION_1_2_0, specimen.version)

        specimenRef = self.getSpecimenReference(title)
        self.assertEquals(specimenRef.version.major, specimen.version.major)
        self.assertEquals(specimenRef.version.minor, specimen.version.minor)
        self.assertEquals(specimenRef.version.revision, specimen.version.revision)
        self.assertEquals(specimenRef.version, specimen.version)

        self.assertEquals(specimenRef.numberRegions, specimen.numberRegions)

        indexRegion = 0
        region = specimen.regions[indexRegion]
        regionRef = specimenRef.regions[indexRegion]
        self.assertEquals(regionRef.numberElements, region.numberElements)
        self.assertEquals(regionRef.regionMassDensity_g_cm3, region.regionMassDensity_g_cm3)
        self.assertEquals(regionRef.regionType, region.regionType)
        self.assertEquals(regionRef.regionDimensions, region.regionDimensions)
        indexElement = 0
        element = region.elements[indexElement]
        elementRef = regionRef.elements[indexElement]
        self.assertEquals(elementRef.atomicNumber, element.atomicNumber)
        self.assertEquals(elementRef.massFraction, element.massFraction)
        indexElement = 1
        element = region.elements[indexElement]
        elementRef = regionRef.elements[indexElement]
        self.assertEquals(elementRef.atomicNumber, element.atomicNumber)
        self.assertEquals(elementRef.massFraction, element.massFraction)

        indexRegion = 1
        region = specimen.regions[indexRegion]
        regionRef = specimenRef.regions[indexRegion]
        self.assertEquals(regionRef.numberElements, region.numberElements)
        self.assertEquals(regionRef.regionMassDensity_g_cm3, region.regionMassDensity_g_cm3)
        self.assertEquals(regionRef.regionType, region.regionType)
        self.assertEquals(regionRef.regionDimensions, region.regionDimensions)
        indexElement = 0
        element = region.elements[indexElement]
        elementRef = regionRef.elements[indexElement]
        self.assertEquals(elementRef.atomicNumber, element.atomicNumber)
        self.assertEquals(elementRef.massFraction, element.massFraction)

        indexRegion = 2
        region = specimen.regions[indexRegion]
        regionRef = specimenRef.regions[indexRegion]
        self.assertEquals(regionRef.numberElements, region.numberElements)
        self.assertEquals(regionRef.regionMassDensity_g_cm3, region.regionMassDensity_g_cm3)
        self.assertEquals(regionRef.regionType, region.regionType)
        self.assertEquals(regionRef.regionDimensions, region.regionDimensions)
        indexElement = 0
        element = region.elements[indexElement]
        elementRef = regionRef.elements[indexElement]
        self.assertEquals(elementRef.atomicNumber, element.atomicNumber)
        self.assertEquals(elementRef.massFraction, element.massFraction)

        #self.fail("Test if the testcase is working.")

    def test_read_1_2_1(self):
        """
        Tests for method `read`.
        """

        specimen = Specimen.Specimen()

        title = "AlMgBulk5keV_version_1_2_1"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.sam" % (title)))
        specimen.read(filepath)

        self.assertEquals(Version.VERSION_1_2_1.major, specimen.version.major)
        self.assertEquals(Version.VERSION_1_2_1.minor, specimen.version.minor)
        self.assertEquals(Version.VERSION_1_2_1.revision, specimen.version.revision)
        self.assertEquals(Version.VERSION_1_2_1, specimen.version)

        specimenRef = self.getSpecimenReference(title)
        self.assertEquals(specimenRef.version.major, specimen.version.major)
        self.assertEquals(specimenRef.version.minor, specimen.version.minor)
        self.assertEquals(specimenRef.version.revision, specimen.version.revision)
        self.assertEquals(specimenRef.version, specimen.version)

        self.assertEquals(specimenRef.numberRegions, specimen.numberRegions)

        indexRegion = 0
        region = specimen.regions[indexRegion]
        regionRef = specimenRef.regions[indexRegion]
        self.assertEquals(regionRef.numberElements, region.numberElements)
        self.assertEquals(regionRef.regionMassDensity_g_cm3, region.regionMassDensity_g_cm3)
        self.assertEquals(regionRef.regionType, region.regionType)
        self.assertEquals(regionRef.regionDimensions, region.regionDimensions)
        indexElement = 0
        element = region.elements[indexElement]
        elementRef = regionRef.elements[indexElement]
        self.assertEquals(elementRef.atomicNumber, element.atomicNumber)
        self.assertEquals(elementRef.massFraction, element.massFraction)
        indexElement = 1
        element = region.elements[indexElement]
        elementRef = regionRef.elements[indexElement]
        self.assertEquals(elementRef.atomicNumber, element.atomicNumber)
        self.assertEquals(elementRef.massFraction, element.massFraction)

        indexRegion = 1
        region = specimen.regions[indexRegion]
        regionRef = specimenRef.regions[indexRegion]
        self.assertEquals(regionRef.numberElements, region.numberElements)
        self.assertEquals(regionRef.regionMassDensity_g_cm3, region.regionMassDensity_g_cm3)
        self.assertEquals(regionRef.regionType, region.regionType)
        self.assertEquals(regionRef.regionDimensions, region.regionDimensions)
        indexElement = 0
        element = region.elements[indexElement]
        elementRef = regionRef.elements[indexElement]
        self.assertEquals(elementRef.atomicNumber, element.atomicNumber)
        self.assertEquals(elementRef.massFraction, element.massFraction)

        indexRegion = 2
        region = specimen.regions[indexRegion]
        regionRef = specimenRef.regions[indexRegion]
        self.assertEquals(regionRef.numberElements, region.numberElements)
        self.assertEquals(regionRef.regionMassDensity_g_cm3, region.regionMassDensity_g_cm3)
        self.assertEquals(regionRef.regionType, region.regionType)
        self.assertEquals(regionRef.regionDimensions, region.regionDimensions)
        indexElement = 0
        element = region.elements[indexElement]
        elementRef = regionRef.elements[indexElement]
        self.assertEquals(elementRef.atomicNumber, element.atomicNumber)
        self.assertEquals(elementRef.massFraction, element.massFraction)

        #self.fail("Test if the testcase is working.")

    def test_read_1_4_1(self):
        """
        Tests for method `read`.
        """

        specimen = Specimen.Specimen()

        title = "AlMgBulk5keV_version_1_4_1"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.sam" % (title)))
        specimen.read(filepath)

        self.assertEquals(Version.VERSION_1_4_1.major, specimen.version.major)
        self.assertEquals(Version.VERSION_1_4_1.minor, specimen.version.minor)
        self.assertEquals(Version.VERSION_1_4_1.revision, specimen.version.revision)
        self.assertEquals(Version.VERSION_1_4_1, specimen.version)

        specimenRef = self.getSpecimenReference(title)
        self.assertEquals(specimenRef.version.major, specimen.version.major)
        self.assertEquals(specimenRef.version.minor, specimen.version.minor)
        self.assertEquals(specimenRef.version.revision, specimen.version.revision)
        self.assertEquals(specimenRef.version, specimen.version)

        self.assertEquals(specimenRef.numberRegions, specimen.numberRegions)

        indexRegion = 0
        region = specimen.regions[indexRegion]
        regionRef = specimenRef.regions[indexRegion]
        self.assertEquals(regionRef.numberElements, region.numberElements)
        self.assertEquals(regionRef.regionMassDensity_g_cm3, region.regionMassDensity_g_cm3)
        self.assertEquals(regionRef.regionType, region.regionType)
        self.assertEquals(regionRef.regionDimensions, region.regionDimensions)
        indexElement = 0
        element = region.elements[indexElement]
        elementRef = regionRef.elements[indexElement]
        self.assertEquals(elementRef.atomicNumber, element.atomicNumber)
        self.assertEquals(elementRef.massFraction, element.massFraction)
        indexElement = 1
        element = region.elements[indexElement]
        elementRef = regionRef.elements[indexElement]
        self.assertEquals(elementRef.atomicNumber, element.atomicNumber)
        self.assertEquals(elementRef.massFraction, element.massFraction)

        indexRegion = 1
        region = specimen.regions[indexRegion]
        regionRef = specimenRef.regions[indexRegion]
        self.assertEquals(regionRef.numberElements, region.numberElements)
        self.assertEquals(regionRef.regionMassDensity_g_cm3, region.regionMassDensity_g_cm3)
        self.assertEquals(regionRef.regionType, region.regionType)
        self.assertEquals(regionRef.regionDimensions, region.regionDimensions)
        indexElement = 0
        element = region.elements[indexElement]
        elementRef = regionRef.elements[indexElement]
        self.assertEquals(elementRef.atomicNumber, element.atomicNumber)
        self.assertEquals(elementRef.massFraction, element.massFraction)

        indexRegion = 2
        region = specimen.regions[indexRegion]
        regionRef = specimenRef.regions[indexRegion]
        self.assertEquals(regionRef.numberElements, region.numberElements)
        self.assertEquals(regionRef.regionMassDensity_g_cm3, region.regionMassDensity_g_cm3)
        self.assertEquals(regionRef.regionType, region.regionType)
        self.assertEquals(regionRef.regionDimensions, region.regionDimensions)
        indexElement = 0
        element = region.elements[indexElement]
        elementRef = regionRef.elements[indexElement]
        self.assertEquals(elementRef.atomicNumber, element.atomicNumber)
        self.assertEquals(elementRef.massFraction, element.massFraction)

        #self.fail("Test if the testcase is working.")

    def test_write(self):
        """
        Tests for method `write`.
        """
        raise SkipTest

        self.maxDiff = None

        for title in testUtilities.getSimulationTitles():
            logging.info(title)

            specimenRef = self.getSpecimenReference(title)
            filepathReference = os.path.abspath(os.path.join(self.testDataPath, "%s/%s.sam" % (title, title)))

            filepath = os.path.join(self.tempDataPath, "%s.sam" % (title))

            specimen = Specimen.Specimen()
            specimen = specimenRef

            specimen.write(filepath)

            linesRef = open(filepathReference, 'r').readlines()
            lines = open(filepath, 'r').readlines()

            for index in range(len(linesRef)):
                lineRef = linesRef[index]
                line = lines[index]
                message = "%i:\n%s\n%s" % (index, lineRef, line)
                self.assertEquals(lineRef, line, message)

            self.assertListEqual(linesRef, lines)

        #self.fail("Test if the testcase is working.")

    def test_write_1_1_1(self):
        """
        Tests for method `write`.
        """
        raise SkipTest

        self.maxDiff = None

        title = "AlMgBulk5keV_version_1_1_1"

        specimenRef = self.getSpecimenReference(title)
        filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.sam" % (title)))

        filepath = os.path.join(self.tempDataPath, "%s.sam" % (title))

        specimen = specimenRef

        specimen.write(filepath)

        linesRef = open(filepathReference, 'r').readlines()
        lines = open(filepath, 'r').readlines()

        for index in range(len(linesRef)):
            lineRef = linesRef[index]
            line = lines[index]
            message = "%i:\n%s\n%s" % (index, lineRef, line)
            self.assertEquals(lineRef, line, message)

        self.assertListEqual(linesRef, lines)

        self.fail("Test if the testcase is working.")

    def test_write_1_2_0(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        title = "AlMgBulk5keV_version_1_2_0"

        specimenRef = self.getSpecimenReference(title)
        filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.sam" % (title)))

        filepath = os.path.join(self.tempDataPath, "%s.sam" % (title))

        specimen = specimenRef
        specimen.version = copy.deepcopy(Version.VERSION_1_2_0)
        specimen.write(filepath)

        linesRef = open(filepathReference, 'r').readlines()
        lines = open(filepath, 'r').readlines()

        for index in range(len(linesRef)):
            lineRef = linesRef[index]
            line = lines[index]
            message = "%i:\n%s\n%s" % (index, lineRef, line)
            self.assertEquals(lineRef, line, message)

        self.assertListEqual(linesRef, lines)

        #self.fail("Test if the testcase is working.")

    def test_write_1_2_1(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        title = "AlMgBulk5keV_version_1_2_1"

        specimenRef = self.getSpecimenReference(title)
        filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.sam" % (title)))

        filepath = os.path.join(self.tempDataPath, "%s.sam" % (title))

        specimen = specimenRef
        specimen.version = copy.deepcopy(Version.VERSION_1_2_1)
        specimen.write(filepath)

        linesRef = open(filepathReference, 'r').readlines()
        lines = open(filepath, 'r').readlines()

        for index in range(len(linesRef)):
            lineRef = linesRef[index]
            line = lines[index]
            message = "%i:\n%s\n%s" % (index, lineRef, line)
            self.assertEquals(lineRef, line, message)

        self.assertListEqual(linesRef, lines)

        #self.fail("Test if the testcase is working.")

    def test_write_1_4_1(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        title = "AlMgBulk5keV_version_1_4_1"

        specimenRef = self.getSpecimenReference(title)
        filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.sam" % (title)))

        filepath = os.path.join(self.tempDataPath, "%s.sam" % (title))

        specimen = specimenRef

        specimen.write(filepath)

        linesRef = open(filepathReference, 'r').readlines()
        lines = open(filepath, 'r').readlines()

        for index in range(len(linesRef)):
            lineRef = linesRef[index]
            line = lines[index]
            message = "%i:\n%s\n%s" % (index, lineRef, line)
            self.assertEquals(lineRef, line, message)

        self.assertListEqual(linesRef, lines)

        #self.fail("Test if the testcase is working.")

    def getSpecimenReference(self, title):
        specimen = Specimen.Specimen()

        if title == "AuBC cyl":
            specimen.numberRegions = 4
            specimen.version = Version.Version(1, 1, 1)

            region = Region.Region()
            region.numberElements = 1
            element = Element.Element(6)
            region.elements.append(element)
            region.regionType = RegionType.REGION_TYPE_BOX
            parameters = [-10000000000.0, 10000000000.0, -10000000000.0, 10000000000.0, 0.0, 20000000000.0]
            region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
            specimen.regions.append(region)

            region = Region.Region()
            region.numberElements = 1
            element = Element.Element(79)
            region.elements.append(element)
            region.regionType = RegionType.REGION_TYPE_BOX
            parameters = [0.0, 10000000000.0, -10000000000.0, 10000000000.0, 0.0, 20000000000.0]
            region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
            specimen.regions.append(region)

            region = Region.Region()
            region.numberElements = 1
            element = Element.Element(5)
            region.elements.append(element)
            region.regionType = RegionType.REGION_TYPE_CYLINDER
            parameters = [-500.0, -500.0, 300.0, 0.0, 1.0, 0.35, 1000.0, 300.0]
            region.regionDimensions = RegionDimensions.RegionDimensionsCylinder(parameters)
            specimen.regions.append(region)

            region = Region.Region()
            region.numberElements = 1
            element = Element.Element(5)
            region.elements.append(element)
            region.regionType = RegionType.REGION_TYPE_CYLINDER
            parameters = [500.0, 500.0, 300.0, 0.0, -1.0, 0.35, 1000.0, 300.0]
            region.regionDimensions = RegionDimensions.RegionDimensionsCylinder(parameters)
            specimen.regions.append(region)

        elif title == "BioRitchieNew111017":
            specimen.numberRegions = 7
            specimen.version = Version.Version(1, 1, 1)

            region = Region.Region()
            region.numberElements = 3
            element = Element.Element(6, 0.7)
            region.elements.append(element)
            element = Element.Element(8, 0.28)
            region.elements.append(element)
            element = Element.Element(17, 0.02)
            region.elements.append(element)
            region.regionMassDensity_g_cm3 = 1.14
            region.regionType = RegionType.REGION_TYPE_BOX
            parameters = [-10000000000.0, 10000000000.0, -10000000000.0, 10000000000.0, 0.0, 20000000000.0]
            region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
            specimen.regions.append(region)

            region = Region.Region()
            region.numberElements = 2
            element = Element.Element(8, 0.53)
            region.elements.append(element)
            element = Element.Element(14, 0.47)
            region.elements.append(element)
            region.regionMassDensity_g_cm3 = 2.2
            region.regionType = RegionType.REGION_TYPE_CYLINDER
            parameters = [-20000.0, 0.0, 30000.0, 1.0, 0.0, 0.0, 40000.0, 30000.0]
            region.regionDimensions = RegionDimensions.RegionDimensionsCylinder(parameters)
            specimen.regions.append(region)

            region = Region.Region()
            region.numberElements = 3
            element = Element.Element(6, 0.7)
            region.elements.append(element)
            element = Element.Element(8, 0.28)
            region.elements.append(element)
            element = Element.Element(17, 0.02)
            region.elements.append(element)
            region.regionMassDensity_g_cm3 = 1.14
            region.regionType = RegionType.REGION_TYPE_CYLINDER
            parameters = [-20000.0, 0.0, 30000.0, 1.0, 0.0, 0.0, 40000.0, 29500.0]
            region.regionDimensions = RegionDimensions.RegionDimensionsCylinder(parameters)
            specimen.regions.append(region)

            region = Region.Region()
            region.numberElements = 7
            region.elements.append(Element.Element(1, 0.071))
            region.elements.append(Element.Element(6, 0.414))
            region.elements.append(Element.Element(7, 0.168))
            region.elements.append(Element.Element(8, 0.285))
            region.elements.append(Element.Element(15, 0.036))
            region.elements.append(Element.Element(16, 0.006))
            region.elements.append(Element.Element(76, 0.02))
            region.regionMassDensity_g_cm3 = 1.32
            region.regionType = RegionType.REGION_TYPE_SPHERE
            parameters = [12000.0, 10000.0, 10000.0, 8000.0]
            region.regionDimensions = RegionDimensions.RegionDimensionsSphere(parameters)
            specimen.regions.append(region)

            region = Region.Region()
            region.numberElements = 9
            region.elements.append(Element.Element(1, 0.11))
            region.elements.append(Element.Element(6, 0.49))
            region.elements.append(Element.Element(7, 0.12))
            region.elements.append(Element.Element(8, 0.25))
            region.elements.append(Element.Element(12, 0.003))
            region.elements.append(Element.Element(15, 0.003))
            region.elements.append(Element.Element(16, 0.003))
            region.elements.append(Element.Element(25, 0.001))
            region.elements.append(Element.Element(76, 0.02))
            region.regionMassDensity_g_cm3 = 1.24
            region.regionType = RegionType.REGION_TYPE_SPHERE
            parameters = [-10000.0, 0.0, 20000.0, 15000.0]
            region.regionDimensions = RegionDimensions.RegionDimensionsSphere(parameters)
            specimen.regions.append(region)

            region = Region.Region()
            region.numberElements = 9
            region.elements.append(Element.Element(1, 0.11))
            region.elements.append(Element.Element(6, 0.49))
            region.elements.append(Element.Element(7, 0.12))
            region.elements.append(Element.Element(8, 0.25))
            region.elements.append(Element.Element(12, 0.003))
            region.elements.append(Element.Element(15, 0.003))
            region.elements.append(Element.Element(16, 0.003))
            region.elements.append(Element.Element(25, 0.001))
            region.elements.append(Element.Element(76, 0.02))
            region.regionMassDensity_g_cm3 = 1.24
            region.regionType = RegionType.REGION_TYPE_SPHERE
            parameters = [10000.0, -5000.0, 25000.0, 6000.0]
            region.regionDimensions = RegionDimensions.RegionDimensionsSphere(parameters)
            specimen.regions.append(region)

            region = Region.Region()
            region.numberElements = 7
            region.elements.append(Element.Element(1, 0.077))
            region.elements.append(Element.Element(6, 0.497))
            region.elements.append(Element.Element(7, 0.11))
            region.elements.append(Element.Element(8, 0.259))
            region.elements.append(Element.Element(15, 0.031))
            region.elements.append(Element.Element(16, 0.006))
            region.elements.append(Element.Element(76, 0.02))
            region.regionMassDensity_g_cm3 = 1.18
            region.regionType = RegionType.REGION_TYPE_SPHERE
            parameters = [-23000.0, 4000.0, 33500.0, 2000.0]
            region.regionDimensions = RegionDimensions.RegionDimensionsSphere(parameters)
            specimen.regions.append(region)

            specimen._shortHeader = True

        elif title == "Bug Al Zr Sphere":
            specimen.numberRegions = 2
            specimen.version = Version.Version(1, 1, 1)

            region = Region.Region()
            region.numberElements = 1
            element = Element.Element(13)
            region.elements.append(element)
            region.regionType = RegionType.REGION_TYPE_BOX
            parameters = [-10000000000.0, 10000000000.0, -10000000000.0, 10000000000.0, 0.0, 1000.0]
            region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
            specimen.regions.append(region)

            region = Region.Region()
            region.numberElements = 1
            element = Element.Element(40)
            region.elements.append(element)
            region.regionType = RegionType.REGION_TYPE_SPHERE
            parameters = [0.0, 0.0, 500.0, 499.9]
            region.regionDimensions = RegionDimensions.RegionDimensionsSphere(parameters)
            specimen.regions.append(region)

        elif title == "Mg2SiAlCube3kev":
            specimen.numberRegions = 2
            specimen.version = Version.Version(1, 1, 1)

            region = Region.Region()
            region.numberElements = 2
            element = Element.Element(12, 0.5)
            region.elements.append(element)
            element = Element.Element(13, 0.5)
            region.elements.append(element)
            region.regionType = RegionType.REGION_TYPE_BOX
            parameters = [-10000000000.0, 10000000000.0, -10000000000.0, 10000000000.0, 0.0, 20000000000.0]
            region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
            specimen.regions.append(region)

            region = Region.Region()
            region.numberElements = 1
            element = Element.Element(6)
            region.elements.append(element)
            region.regionType = RegionType.REGION_TYPE_BOX
            parameters = (-10.0, 10.0, -10.0, 10.0, 0.0, 20.0)
            region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
            specimen.regions.append(region)

        elif title == "AlMgBulk5keV_version_1_1_1":
            specimen.numberRegions = 3
            specimen.version = Version.Version(1, 1, 1)

            region = Region.Region()
            region.numberElements = 2
            element = Element.Element(12, 0.5)
            region.elements.append(element)
            element = Element.Element(13, 0.5)
            region.elements.append(element)
            region.regionType = RegionType.REGION_TYPE_BOX
            parameters = [-10000000000.0, 10000000000.0, -10000000000.0, 10000000000.0, 0.0, 20000000000.0]
            region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
            specimen.regions.append(region)

            region = Region.Region()
            region.numberElements = 1
            element = Element.Element(6)
            region.elements.append(element)
            region.regionType = RegionType.REGION_TYPE_CYLINDER
            parameters = [0.0, -5000.0, 0.0, 0.0, 1.0, -0.7, 10000.0, 100.0]
            region.regionDimensions = RegionDimensions.RegionDimensionsCylinder(parameters)
            specimen.regions.append(region)

            region = Region.Region()
            region.numberElements = 1
            element = Element.Element(79)
            region.elements.append(element)
            region.regionType = RegionType.REGION_TYPE_SPHERE
            parameters = [0.0, 0.0, 101.0, 100.0]
            region.regionDimensions = RegionDimensions.RegionDimensionsSphere(parameters)
            specimen.regions.append(region)

        elif title == "AlMgBulk5keV_version_1_2_0":
            specimen.numberRegions = 3
            specimen.version = Version.Version(1, 2, 0)

            region = Region.Region()
            region.numberElements = 2
            element = Element.Element(14, 0.4)
            region.elements.append(element)
            element = Element.Element(15, 0.6)
            region.elements.append(element)
            region.regionMassDensity_g_cm3 = 23.0
            region.regionType = RegionType.REGION_TYPE_BOX
            parameters = [-2000000000.0, 6000000000.0, -4000000000.0, 5000000000.0, 0.8, 70000.0]
            region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
            specimen.regions.append(region)

            region = Region.Region()
            region.numberElements = 1
            element = Element.Element(7)
            region.elements.append(element)
            region.regionType = RegionType.REGION_TYPE_CYLINDER
            parameters = [0.4, -8000.0, 0.9, 0.1, 0.6, -0.8, 50000.0, 700.0]
            region.regionDimensions = RegionDimensions.RegionDimensionsCylinder(parameters)
            specimen.regions.append(region)

            region = Region.Region()
            region.numberElements = 1
            element = Element.Element(56)
            region.elements.append(element)
            region.regionType = RegionType.REGION_TYPE_SPHERE
            parameters = [0.5, 0.6, 102.0, 101.0]
            region.regionDimensions = RegionDimensions.RegionDimensionsSphere(parameters)
            specimen.regions.append(region)

        elif title == "AlMgBulk5keV_version_1_2_1":
            specimen.numberRegions = 3
            specimen.version = Version.Version(1, 2, 1)

            region = Region.Region()
            region.numberElements = 2
            element = Element.Element(14, 0.4)
            region.elements.append(element)
            element = Element.Element(15, 0.6)
            region.elements.append(element)
            region.regionMassDensity_g_cm3 = 23.0
            region.regionType = RegionType.REGION_TYPE_BOX
            parameters = [-2000000000.0, 6000000000.0, -4000000000.0, 5000000000.0, 0.8, 70000.0]
            region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
            specimen.regions.append(region)

            region = Region.Region()
            region.numberElements = 1
            element = Element.Element(7)
            region.elements.append(element)
            region.regionType = RegionType.REGION_TYPE_CYLINDER
            parameters = [0.4, -8000.0, 0.9, 0.1, 0.6, -0.8, 50000.0, 700.0]
            region.regionDimensions = RegionDimensions.RegionDimensionsCylinder(parameters)
            specimen.regions.append(region)

            region = Region.Region()
            region.numberElements = 1
            element = Element.Element(56)
            region.elements.append(element)
            region.regionType = RegionType.REGION_TYPE_SPHERE
            parameters = [0.5, 0.6, 102.0, 101.0]
            region.regionDimensions = RegionDimensions.RegionDimensionsSphere(parameters)
            specimen.regions.append(region)

        elif title == "AlMgBulk5keV_version_1_4_1":
            specimen.numberRegions = 3
            specimen.version = Version.Version(1, 4, 1)

            region = Region.Region()
            region.numberElements = 2
            element = Element.Element(14, 0.4)
            region.elements.append(element)
            element = Element.Element(15, 0.6)
            region.elements.append(element)
            region.regionMassDensity_g_cm3 = 23.0
            region.regionType = RegionType.REGION_TYPE_BOX
            parameters = [-2000000000.0, 6000000000.0, -4000000000.0, 5000000000.0, 0.8, 70000.0]
            region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
            specimen.regions.append(region)

            region = Region.Region()
            region.numberElements = 1
            element = Element.Element(7)
            region.elements.append(element)
            region.regionType = RegionType.REGION_TYPE_CYLINDER
            parameters = [0.4, -8000.0, 0.9, 0.1, 0.6, -0.8, 50000.0, 700.0]
            region.regionDimensions = RegionDimensions.RegionDimensionsCylinder(parameters)
            specimen.regions.append(region)

            region = Region.Region()
            region.numberElements = 1
            element = Element.Element(56)
            region.elements.append(element)
            region.regionType = RegionType.REGION_TYPE_SPHERE
            parameters = [0.5, 0.6, 102.0, 101.0]
            region.regionDimensions = RegionDimensions.RegionDimensionsSphere(parameters)
            specimen.regions.append(region)

        return specimen

if __name__ == '__main__':  #pragma: no cover
    import nose
    nose.runmodule()
