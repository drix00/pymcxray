#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.test_RegionDimensions
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for module `RegionDimensions`.
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
import pymcxray.FileFormat.RegionDimensions as RegionDimensions
import pymcxray.FileFormat.RegionType as RegionType

# Globals and constants variables.

class TestRegionDimensions(unittest.TestCase):
    """
    TestCase class for the module `RegionDimensions`.
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

    def test_createRegionDimensions(self):
        """
        Tests for method `createRegionDimensions`.
        """

        classList = {}
        classList[RegionType.REGION_TYPE_BOX] = RegionDimensions.RegionDimensionsBox
        classList[RegionType.REGION_TYPE_CYLINDER] = RegionDimensions.RegionDimensionsCylinder
        classList[RegionType.REGION_TYPE_SPHERE] = RegionDimensions.RegionDimensionsSphere

        for regionType in classList:
            classRef = classList[regionType]
            regionDimension = RegionDimensions.createRegionDimensions(regionType)
            self.assertIsInstance(regionDimension, classRef)

        #self.fail("Test if the testcase is working.")

    def test_RegionDimensionsBox_extractFromLineOldVersion(self):
        """
        Tests for class `RegionDimensionsBox`.
        """

        regionDimensions = RegionDimensions.RegionDimensionsBox()

        numberParameters = 6
        self.assertEquals(numberParameters, len(regionDimensions._keys))

        line = "0.000000 10000000000.000000 -10000000000.000000 10000000000.000000 0.000000 20000000000.000000"
        regionDimensions.extractFromLineOldVersion(line)

        self.assertEquals(0.0, regionDimensions.minimumX)
        self.assertEquals(10000000000.0, regionDimensions.maximumX)
        self.assertEquals(-10000000000.0, regionDimensions.minimumY)
        self.assertEquals(10000000000.0, regionDimensions.maximumY)
        self.assertEquals(0.0, regionDimensions.minimumZ)
        self.assertEquals(20000000000.0, regionDimensions.maximumZ)

        #self.fail("Test if the testcase is working.")

    def test_RegionDimensionsCylinder_extractFromLineOldVersion(self):
        """
        Tests for class `RegionDimensionsCylinder`.
        """

        regionDimensions = RegionDimensions.RegionDimensionsCylinder()

        numberParameters = 8
        self.assertEquals(numberParameters, len(regionDimensions._keys))

        line = "-500.000000 -500.000000 300.000000 0.000000 1.000000 0.350000 1000.000000 300.000000"
        regionDimensions.extractFromLineOldVersion(line)

        self.assertEquals(-500.0, regionDimensions.positionX)
        self.assertEquals(-500.0, regionDimensions.positionY)
        self.assertEquals(300.0, regionDimensions.positionZ)
        self.assertEquals(0.0, regionDimensions.directionX)
        self.assertEquals(1.0, regionDimensions.directionY)
        self.assertEquals(0.35, regionDimensions.directionZ)
        self.assertEquals(1000.0, regionDimensions.length)
        self.assertEquals(300.0, regionDimensions.radius)

        #self.fail("Test if the testcase is working.")

    def test_RegionDimensionsSphere_extractFromLineOldVersion(self):
        """
        Tests for class `RegionDimensionsSphere`.
        """

        regionDimensions = RegionDimensions.RegionDimensionsSphere()

        numberParameters = 4
        self.assertEquals(numberParameters, len(regionDimensions._keys))

        line = "500.000000 500.000000 300.000000 300.000000"
        regionDimensions.extractFromLineOldVersion(line)

        self.assertEquals(500.0, regionDimensions.positionX)
        self.assertEquals(500.0, regionDimensions.positionY)
        self.assertEquals(300.0, regionDimensions.positionZ)
        self.assertEquals(300.0, regionDimensions.radius)

        #self.fail("Test if the testcase is working.")

    def test_RegionDimensionsBox_extractFromLinesWithKey(self):
        """
        Tests for class `RegionDimensionsBox`.
        """

        regionDimensions = RegionDimensions.RegionDimensionsBox()

        numberParameters = 6
        self.assertEquals(numberParameters, len(regionDimensions._keys))

        line = "RegionParameters=0.000000 10000000000.000000 -10000000000.000000 10000000000.000000 0.000000 20000000000.000000"
        regionDimensions.extractFromLinesWithKey(line)

        self.assertEquals(0.0, regionDimensions.minimumX)
        self.assertEquals(10000000000.0, regionDimensions.maximumX)
        self.assertEquals(-10000000000.0, regionDimensions.minimumY)
        self.assertEquals(10000000000.0, regionDimensions.maximumY)
        self.assertEquals(0.0, regionDimensions.minimumZ)
        self.assertEquals(20000000000.0, regionDimensions.maximumZ)

        #self.fail("Test if the testcase is working.")

    def test_RegionDimensionsCylinder_extractFromLinesWithKey(self):
        """
        Tests for class `RegionDimensionsCylinder`.
        """

        regionDimensions = RegionDimensions.RegionDimensionsCylinder()

        numberParameters = 8
        self.assertEquals(numberParameters, len(regionDimensions._keys))

        line = "RegionParameters=-500.000000 -500.000000 300.000000 0.000000 1.000000 0.350000 1000.000000 300.000000"
        regionDimensions.extractFromLinesWithKey(line)

        self.assertEquals(-500.0, regionDimensions.positionX)
        self.assertEquals(-500.0, regionDimensions.positionY)
        self.assertEquals(300.0, regionDimensions.positionZ)
        self.assertEquals(0.0, regionDimensions.directionX)
        self.assertEquals(1.0, regionDimensions.directionY)
        self.assertEquals(0.35, regionDimensions.directionZ)
        self.assertEquals(1000.0, regionDimensions.length)
        self.assertEquals(300.0, regionDimensions.radius)

        #self.fail("Test if the testcase is working.")

    def test_RegionDimensionsSphere_extractFromLinesWithKey(self):
        """
        Tests for class `RegionDimensionsSphere`.
        """

        regionDimensions = RegionDimensions.RegionDimensionsSphere()

        numberParameters = 4
        self.assertEquals(numberParameters, len(regionDimensions._keys))

        line = "RegionParameters=500.000000 500.000000 300.000000 300.000000"
        regionDimensions.extractFromLinesWithKey(line)

        self.assertEquals(500.0, regionDimensions.positionX)
        self.assertEquals(500.0, regionDimensions.positionY)
        self.assertEquals(300.0, regionDimensions.positionZ)
        self.assertEquals(300.0, regionDimensions.radius)

        #self.fail("Test if the testcase is working.")

    def test_RegionDimensionsBox_createLineOldVersion(self):
        """
        Tests for class `RegionDimensionsBox`.
        """

        lineRef = "0.000000 10000000000.000000 -10000000000.000000 10000000000.000000 0.000000 20000000000.000000"

        regionDimensions = RegionDimensions.RegionDimensionsBox()
        regionDimensions.minimumX = 0.0
        regionDimensions.maximumX = 10000000000.0
        regionDimensions.minimumY = -10000000000.0
        regionDimensions.maximumY = 10000000000.0
        regionDimensions.minimumZ = 0.0
        regionDimensions.maximumZ = 20000000000.0

        line = regionDimensions.createLineOldVersion()
        self.assertEquals(lineRef, line)

        #self.fail("Test if the testcase is working.")

    def test_RegionDimensionsCylinder_createLineOldVersion(self):
        """
        Tests for class `RegionDimensionsCylinder`.
        """

        lineRef = "-500.000000 -500.000000 300.000000 0.000000 1.000000 0.350000 1000.000000 300.000000"

        regionDimensions = RegionDimensions.RegionDimensionsCylinder()
        regionDimensions.positionX = -500.0
        regionDimensions.positionY = -500.0
        regionDimensions.positionZ = 300.0
        regionDimensions.directionX = 0.0
        regionDimensions.directionY = 1.0
        regionDimensions.directionZ = 0.35
        regionDimensions.length = 1000.0
        regionDimensions.radius = 300.0

        line = regionDimensions.createLineOldVersion()
        self.assertEquals(lineRef, line)

        #self.fail("Test if the testcase is working.")

    def test_RegionDimensionsSphere_createLineOldVersion(self):
        """
        Tests for class `RegionDimensionsSphere`.
        """

        lineRef = "500.000000 500.000000 300.000000 300.000000"

        regionDimensions = RegionDimensions.RegionDimensionsSphere()
        regionDimensions.positionX = 500.0
        regionDimensions.positionY = 500.0
        regionDimensions.positionZ = 300.0
        regionDimensions.radius = 300.0

        line = regionDimensions.createLineOldVersion()
        self.assertEquals(lineRef, line)

        #self.fail("Test if the testcase is working.")

    def test_RegionDimensionsBox_createLineWithKey(self):
        """
        Tests for class `RegionDimensionsBox`.
        """

        lineRef = "RegionParameters=0.000000 10000000000.000000 -10000000000.000000 10000000000.000000 0.000000 20000000000.000000"

        regionDimensions = RegionDimensions.RegionDimensionsBox()
        regionDimensions.minimumX = 0.0
        regionDimensions.maximumX = 10000000000.0
        regionDimensions.minimumY = -10000000000.0
        regionDimensions.maximumY = 10000000000.0
        regionDimensions.minimumZ = 0.0
        regionDimensions.maximumZ = 20000000000.0

        line = regionDimensions.createLineWithKey()
        self.assertEquals(lineRef, line)

        #self.fail("Test if the testcase is working.")

    def test_RegionDimensionsCylinder_createLineWithKey(self):
        """
        Tests for class `RegionDimensionsCylinder`.
        """

        lineRef = "RegionParameters=-500.000000 -500.000000 300.000000 0.000000 1.000000 0.350000 1000.000000 300.000000"

        regionDimensions = RegionDimensions.RegionDimensionsCylinder()
        regionDimensions.positionX = -500.0
        regionDimensions.positionY = -500.0
        regionDimensions.positionZ = 300.0
        regionDimensions.directionX = 0.0
        regionDimensions.directionY = 1.0
        regionDimensions.directionZ = 0.35
        regionDimensions.length = 1000.0
        regionDimensions.radius = 300.0

        line = regionDimensions.createLineWithKey()
        self.assertEquals(lineRef, line)

        #self.fail("Test if the testcase is working.")

    def test_RegionDimensionsSphere_createLineWithKey(self):
        """
        Tests for class `RegionDimensionsSphere`.
        """

        lineRef = "RegionParameters=500.000000 500.000000 300.000000 300.000000"

        regionDimensions = RegionDimensions.RegionDimensionsSphere()
        regionDimensions.positionX = 500.0
        regionDimensions.positionY = 500.0
        regionDimensions.positionZ = 300.0
        regionDimensions.radius = 300.0

        line = regionDimensions.createLineWithKey()
        self.assertEquals(lineRef, line)

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from pymcxray.Testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__)
