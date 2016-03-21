#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.test_Region
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for module `Region`.
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
import pymcxray.FileFormat.Region as Region
import pymcxray.FileFormat.RegionType as RegionType
import pymcxray.FileFormat.Element as Element
import pymcxray.FileFormat.RegionDimensions as RegionDimensions

# Globals and constants variables.

class TestRegion(unittest.TestCase):
    """
    TestCase class for the module `moduleName`.
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

    def test_extractFromLinesWithoutVersion(self):
        """
        Tests for method `read`.
        """
        regionTypes = [RegionType.REGION_TYPE_BOX, RegionType.REGION_TYPE_CYLINDER, RegionType.REGION_TYPE_SPHERE]

        for userMassDensity in [True, False]:
            logging.info("userMassDensity: %s", userMassDensity)
            for regionType in regionTypes:
                logging.info("regionType: %s", regionType)
                region = Region.Region()

                lines, regionRef = self.getTestRegionLinesWithoutVersion(regionType, userMassDensity)
                region.extractFromLinesWithoutVersion(lines)

                self.assertEquals(regionRef.numberElements, region.numberElements)

                elementsRef = regionRef.elements
                elements = region.elements

                for elementRef, element in zip(elementsRef, elements):
                    self.assertEquals(elementRef.atomicNumber, element.atomicNumber)
                    self.assertEquals(elementRef.massFraction, element.massFraction)

                self.assertEquals(regionRef.regionMassDensity_g_cm3, region.regionMassDensity_g_cm3)
                self.assertEquals(regionRef.regionType, region.regionType)

                self.assertDictEqual(regionRef.regionDimensions._parameters, region.regionDimensions._parameters)

        #self.fail("Test if the testcase is working.")

    def test_extractFromLinesWithVersion(self):
        """
        Tests for method `read`.
        """
        regionTypes = [RegionType.REGION_TYPE_BOX, RegionType.REGION_TYPE_CYLINDER, RegionType.REGION_TYPE_SPHERE]

        for userMassDensity in [True, False]:
            logging.info("userMassDensity: %s", userMassDensity)
            for regionType in regionTypes:
                logging.info("regionType: %s", regionType)
                region = Region.Region()

                lines, regionRef = self.getTestRegionLinesWithVersion(regionType, userMassDensity)
                region.extractFromLinesWithVersion(lines)

                self.assertEquals(regionRef.numberElements, region.numberElements)

                elementsRef = regionRef.elements
                elements = region.elements

                for elementRef, element in zip(elementsRef, elements):
                    self.assertEquals(elementRef.atomicNumber, element.atomicNumber)
                    self.assertEquals(elementRef.massFraction, element.massFraction)

                self.assertEquals(regionRef.regionMassDensity_g_cm3, region.regionMassDensity_g_cm3)
                self.assertEquals(regionRef.regionType, region.regionType)

                self.assertDictEqual(regionRef.regionDimensions._parameters, region.regionDimensions._parameters)

        #self.fail("Test if the testcase is working.")

    def test_createLinesWithoutVersion(self):
        """
        Tests for method `createLinesWithoutVersion`.
        """
        regionTypes = [RegionType.REGION_TYPE_BOX, RegionType.REGION_TYPE_CYLINDER, RegionType.REGION_TYPE_SPHERE]

        for userMassDensity in [True, False]:
            logging.info("userMassDensity: %s", userMassDensity)
            for regionType in regionTypes:
                logging.info("regionType: %s", regionType)
                linesRef, regionRef = self.getTestRegionLinesWithoutVersion(regionType, userMassDensity)

                lines = regionRef.createLinesWithoutVersion()

                self.assertEquals(len(linesRef), len(lines))
                self.assertListEqual(linesRef, lines)

        #self.fail("Test if the testcase is working.")

    def test_createLinesWithVersion(self):
        """
        Tests for method `createLinesWithVersion`.
        """
        regionTypes = [RegionType.REGION_TYPE_BOX, RegionType.REGION_TYPE_CYLINDER, RegionType.REGION_TYPE_SPHERE]

        for userMassDensity in [True, False]:
            logging.info("userMassDensity: %s", userMassDensity)
            for regionType in regionTypes:
                logging.info("regionType: %s", regionType)
                linesRef, regionRef = self.getTestRegionLinesWithVersion(regionType, userMassDensity)

                lines = regionRef.createLinesWithVersion()

                self.assertEquals(len(linesRef), len(lines))
                self.assertListEqual(linesRef, lines)

        #self.fail("Test if the testcase is working.")

    def getTestRegionLinesWithoutVersion(self, title, userMassDensity=True):
        region = Region.Region()

        if not userMassDensity:
            if title == RegionType.REGION_TYPE_BOX:
                lines = \
"""1
79 1.000000000000000
BOX
0.000000 10000000000.000000 -10000000000.000000 10000000000.000000 0.000000 20000000000.000000
""".splitlines()
                region.numberElements = 1
                element = Element.Element()
                element.atomicNumber = 79
                element.massFraction = 1.0
                region.elements.append(element)
                #region.regionMassDensity_g_cm3
                region.regionType = RegionType.REGION_TYPE_BOX
                regionDimensions = RegionDimensions.createRegionDimensions(region.regionType)
                regionDimensions.minimumX = 0.0
                regionDimensions.maximumX = 10000000000.0
                regionDimensions.minimumY = -10000000000.0
                regionDimensions.maximumY = 10000000000.0
                regionDimensions.minimumZ = 0.0
                regionDimensions.maximumZ = 20000000000.0
                region.regionDimensions = regionDimensions
                return lines, region

            if title == RegionType.REGION_TYPE_CYLINDER:
                lines = \
"""1
5 1.000000000000000
CYLINDER
-500.000000 -500.000000 300.000000 0.000000 1.000000 0.350000 1000.000000 300.000000
""".splitlines()
                region.numberElements = 1
                element = Element.Element()
                element.atomicNumber = 5
                element.massFraction = 1.0
                region.elements.append(element)
                #region.regionMassDensity_g_cm3
                region.regionType = RegionType.REGION_TYPE_CYLINDER
                regionDimensions = RegionDimensions.createRegionDimensions(region.regionType)
                regionDimensions.positionX = -500.0
                regionDimensions.positionY = -500.0
                regionDimensions.positionZ = 300.0
                regionDimensions.directionX = 0.0
                regionDimensions.directionY = 1.0
                regionDimensions.directionZ = 0.35
                regionDimensions.length = 1000.0
                regionDimensions.radius = 300.0
                region.regionDimensions = regionDimensions
                return lines, region

            if title == RegionType.REGION_TYPE_SPHERE:
                lines = \
"""1
5 1.000000000000000
SPHERE
500.000000 500.000000 300.000000 300.000000
""".splitlines()
                region.numberElements = 1
                element = Element.Element()
                element.atomicNumber = 5
                element.massFraction = 1.0
                region.elements.append(element)
                #region.regionMassDensity_g_cm3
                region.regionType = RegionType.REGION_TYPE_SPHERE
                regionDimensions = RegionDimensions.createRegionDimensions(region.regionType)
                regionDimensions.positionX = 500.0
                regionDimensions.positionY = 500.0
                regionDimensions.positionZ = 300.0
                regionDimensions.radius = 300.0
                region.regionDimensions = regionDimensions
                return lines, region

        if userMassDensity:
            if title == RegionType.REGION_TYPE_BOX:
                lines = \
"""3
6 0.700000000000000
8 0.280000000000000
17 0.020000000000000
1.140000000000000
BOX
-10000000000.000000 10000000000.000000 -10000000000.000000 10000000000.000000 0.000000 20000000000.000000
""".splitlines()
                region.numberElements = 3
                element = Element.Element()
                element.atomicNumber = 6
                element.massFraction = 0.7
                region.elements.append(element)
                element = Element.Element()
                element.atomicNumber = 8
                element.massFraction = 0.28
                region.elements.append(element)
                element = Element.Element()
                element.atomicNumber = 17
                element.massFraction = 0.02
                region.elements.append(element)
                region.regionMassDensity_g_cm3 = 1.14
                region.regionType = RegionType.REGION_TYPE_BOX
                regionDimensions = RegionDimensions.createRegionDimensions(region.regionType)
                regionDimensions.minimumX = -10000000000.0
                regionDimensions.maximumX = 10000000000.0
                regionDimensions.minimumY = -10000000000.0
                regionDimensions.maximumY = 10000000000.0
                regionDimensions.minimumZ = 0.0
                regionDimensions.maximumZ = 20000000000.0
                region.regionDimensions = regionDimensions
                return lines, region

            if title == RegionType.REGION_TYPE_CYLINDER:
                lines = \
"""2
8 0.530000000000000
14 0.470000000000000
2.200000000000000
CYLINDER
-20000.000000 0.000000 30000.000000 1.000000 0.000000 0.000000 40000.000000 30000.000000
""".splitlines()
                region.numberElements = 2
                element = Element.Element()
                element.atomicNumber = 8
                element.massFraction = 0.53
                region.elements.append(element)
                element = Element.Element()
                element.atomicNumber = 14
                element.massFraction = 0.47
                region.elements.append(element)
                region.regionMassDensity_g_cm3 = 2.2
                region.regionType = RegionType.REGION_TYPE_CYLINDER
                regionDimensions = RegionDimensions.createRegionDimensions(region.regionType)
                regionDimensions.positionX = -20000.0
                regionDimensions.positionY = 0.0
                regionDimensions.positionZ = 30000.0
                regionDimensions.directionX = 1.0
                regionDimensions.directionY = 0.0
                regionDimensions.directionZ = 0.0
                regionDimensions.length = 40000.0
                regionDimensions.radius = 30000.0
                region.regionDimensions = regionDimensions
                return lines, region

            if title == RegionType.REGION_TYPE_SPHERE:
                lines = \
"""7
1 0.071000000000000
6 0.414000000000000
7 0.168000000000000
8 0.285000000000000
15 0.036000000000000
16 0.006000000000000
76 0.020000000000000
1.320000000000000
SPHERE
12000.000000 10000.000000 10000.000000 8000.000000
""".splitlines()
                region.numberElements = 7
                element = Element.Element()
                element.atomicNumber = 1
                element.massFraction = 0.071
                region.elements.append(element)
                element = Element.Element()
                element.atomicNumber = 6
                element.massFraction = 0.414
                region.elements.append(element)
                element = Element.Element()
                element.atomicNumber = 7
                element.massFraction = 0.168
                region.elements.append(element)
                element = Element.Element()
                element.atomicNumber = 8
                element.massFraction = 0.285
                region.elements.append(element)
                element = Element.Element()
                element.atomicNumber = 15
                element.massFraction = 0.036
                region.elements.append(element)
                element = Element.Element()
                element.atomicNumber = 16
                element.massFraction = 0.006
                region.elements.append(element)
                element = Element.Element()
                element.atomicNumber = 76
                element.massFraction = 0.02
                region.elements.append(element)
                region.regionMassDensity_g_cm3 = 1.32
                region.regionType = RegionType.REGION_TYPE_SPHERE
                regionDimensions = RegionDimensions.createRegionDimensions(region.regionType)
                regionDimensions.positionX = 12000.0
                regionDimensions.positionY = 10000.0
                regionDimensions.positionZ = 10000.0
                regionDimensions.radius = 8000.0
                region.regionDimensions = regionDimensions
                return lines, region

    def getTestRegionLinesWithVersion(self, title, userMassDensity=True):
        region = Region.Region()

        if not userMassDensity:
            if title == RegionType.REGION_TYPE_BOX:
                lines = \
"""NumberElements=2
AtomicNumber=14
WeightFraction=0.400000000000000
AtomicNumber=15
WeightFraction=0.600000000000000
UserDefinedMassDensity=0
RegionType=BOX
RegionParameters=-2000000000.000000 6000000000.000000 -4000000000.000000 5000000000.000000 0.800000 70000.000000
""".splitlines()
                region.numberElements = 2
                element = Element.Element(14, 0.4)
                region.elements.append(element)
                element = Element.Element(15, 0.6)
                region.elements.append(element)
                region.regionType = RegionType.REGION_TYPE_BOX
                parameters = [-2000000000.0, 6000000000.0, -4000000000.0, 5000000000.0, 0.8, 70000.0]
                region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
                return lines, region

            if title == RegionType.REGION_TYPE_CYLINDER:
                lines = \
"""NumberElements=1
AtomicNumber=7
WeightFraction=1.000000000000000
UserDefinedMassDensity=0
RegionType=CYLINDER
RegionParameters=0.400000 -8000.000000 0.900000 0.100000 0.600000 -0.800000 50000.000000 700.000000
""".splitlines()
                region.numberElements = 1
                element = Element.Element(7)
                region.elements.append(element)
                region.regionType = RegionType.REGION_TYPE_CYLINDER
                parameters = [0.4, -8000.0, 0.9, 0.1, 0.6, -0.8, 50000.0, 700.0]
                region.regionDimensions = RegionDimensions.RegionDimensionsCylinder(parameters)
                return lines, region

            if title == RegionType.REGION_TYPE_SPHERE:
                lines = \
"""NumberElements=1
AtomicNumber=56
WeightFraction=1.000000000000000
UserDefinedMassDensity=0
RegionType=SPHERE
RegionParameters=0.500000 0.600000 102.000000 101.000000
""".splitlines()
                region.numberElements = 1
                element = Element.Element(56)
                region.elements.append(element)
                region.regionType = RegionType.REGION_TYPE_SPHERE
                parameters = [0.5, 0.6, 102.0, 101.0]
                region.regionDimensions = RegionDimensions.RegionDimensionsSphere(parameters)
                return lines, region

        if userMassDensity:
            if title == RegionType.REGION_TYPE_BOX:
                lines = \
"""NumberElements=2
AtomicNumber=14
WeightFraction=0.400000000000000
AtomicNumber=15
WeightFraction=0.600000000000000
UserDefinedMassDensity=23
RegionType=BOX
RegionParameters=-2000000000.000000 6000000000.000000 -4000000000.000000 5000000000.000000 0.800000 70000.000000
""".splitlines()
                region.numberElements = 2
                element = Element.Element(14, 0.4)
                region.elements.append(element)
                element = Element.Element(15, 0.6)
                region.elements.append(element)
                region.regionMassDensity_g_cm3 = 23.0
                region.regionType = RegionType.REGION_TYPE_BOX
                parameters = [-2000000000.0, 6000000000.0, -4000000000.0, 5000000000.0, 0.8, 70000.0]
                region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
                return lines, region

            if title == RegionType.REGION_TYPE_CYLINDER:
                lines = \
"""NumberElements=1
AtomicNumber=7
WeightFraction=1.000000000000000
UserDefinedMassDensity=2.22
RegionType=CYLINDER
RegionParameters=0.400000 -8000.000000 0.900000 0.100000 0.600000 -0.800000 50000.000000 700.000000
""".splitlines()
                region.numberElements = 1
                element = Element.Element(7)
                region.elements.append(element)
                region.regionMassDensity_g_cm3 = 2.22
                region.regionType = RegionType.REGION_TYPE_CYLINDER
                parameters = [0.4, -8000.0, 0.9, 0.1, 0.6, -0.8, 50000.0, 700.0]
                region.regionDimensions = RegionDimensions.RegionDimensionsCylinder(parameters)
                return lines, region

            if title == RegionType.REGION_TYPE_SPHERE:
                lines = \
"""NumberElements=1
AtomicNumber=56
WeightFraction=1.000000000000000
UserDefinedMassDensity=67.8
RegionType=SPHERE
RegionParameters=0.500000 0.600000 102.000000 101.000000
""".splitlines()
                region.numberElements = 1
                element = Element.Element(56)
                region.elements.append(element)
                region.regionMassDensity_g_cm3 = 67.8
                region.regionType = RegionType.REGION_TYPE_SPHERE
                parameters = [0.5, 0.6, 102.0, 101.0]
                region.regionDimensions = RegionDimensions.RegionDimensionsSphere(parameters)
                return lines, region

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from pymcxray.Testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__, withCoverage=True)
