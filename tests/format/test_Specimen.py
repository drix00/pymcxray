#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.format.test_Specimen

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for module :py:mod:`mcxray.format.Specimen`.
"""

###############################################################################
# Copyright 2019 Hendrix Demers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
###############################################################################

# Standard library modules.
import unittest
import logging
import os.path
import copy

# Third party modules.

# Local modules.

# Project modules
import mcxray.format.Specimen as Specimen
import tests.format.testUtilities as testUtilities
import mcxray.format.Region as Region
import mcxray.format.Element as Element
import mcxray.format.RegionType as RegionType
import mcxray.format.RegionDimensions as RegionDimensions
import mcxray.format.version as version

# Globals and constants variables.


class TestSpecimen(unittest.TestCase):
    """
    TestCase class for the module :py:mod:`mcxray.format.Specimen`.
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

        # self.fail("Test if the testcase is working.")
        self.assertTrue(True)

    def test_read(self):
        """
        Tests for method `read`.
        """

        for title in testUtilities.getSimulationTitles():
            logging.info(title)

            specimen = Specimen.Specimen()

            filepath = os.path.abspath(os.path.join(self.testDataPath, "%s/%s.sam" % (title, title)))
            specimen.read(filepath)

            self.assertEqual(version.VERSION_1_1_1.major, specimen.version.major)
            self.assertEqual(version.VERSION_1_1_1.minor, specimen.version.minor)
            self.assertEqual(version.VERSION_1_1_1.revision, specimen.version.revision)
            self.assertEqual(version.VERSION_1_1_1, specimen.version)

            specimen_ref = get_specimen_reference(title)

            self.assertEqual(specimen_ref.version.major, specimen.version.major)
            self.assertEqual(specimen_ref.version.minor, specimen.version.minor, title)
            self.assertEqual(specimen_ref.version.revision, specimen.version.revision)
            self.assertEqual(specimen_ref.version, specimen.version)

            self.assertEqual(specimen_ref.numberRegions, specimen.numberRegions)

        # self.fail("Test if the testcase is working.")

    def test_read_1_1_1(self):
        """
        Tests for method `read`.
        """

        specimen = Specimen.Specimen()

        title = "AlMgBulk5keV_version_1_1_1"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.sam".format(title)))
        specimen.read(filepath)

        self.assertEqual(version.VERSION_1_1_1.major, specimen.version.major)
        self.assertEqual(version.VERSION_1_1_1.minor, specimen.version.minor)
        self.assertEqual(version.VERSION_1_1_1.revision, specimen.version.revision)
        self.assertEqual(version.VERSION_1_1_1, specimen.version)

        specimen_ref = get_specimen_reference(title)
        self.assertEqual(specimen_ref.version.major, specimen.version.major)
        self.assertEqual(specimen_ref.version.minor, specimen.version.minor)
        self.assertEqual(specimen_ref.version.revision, specimen.version.revision)
        self.assertEqual(specimen_ref.version, specimen.version)

        self.assertEqual(specimen_ref.numberRegions, specimen.numberRegions)

        index_region = 0
        region = specimen.regions[index_region]
        region_ref = specimen_ref.regions[index_region]
        self.assertEqual(region_ref.numberElements, region.numberElements)
        self.assertEqual(region_ref.regionMassDensity_g_cm3, region.regionMassDensity_g_cm3)
        self.assertEqual(region_ref.regionType, region.regionType)
        self.assertEqual(region_ref.regionDimensions, region.regionDimensions)
        index_element = 0
        element = region.elements[index_element]
        element_ref = region_ref.elements[index_element]
        self.assertEqual(element_ref.atomicNumber, element.atomicNumber)
        self.assertEqual(element_ref.massFraction, element.massFraction)
        index_element = 1
        element = region.elements[index_element]
        element_ref = region_ref.elements[index_element]
        self.assertEqual(element_ref.atomicNumber, element.atomicNumber)
        self.assertEqual(element_ref.massFraction, element.massFraction)

        index_region = 1
        region = specimen.regions[index_region]
        region_ref = specimen_ref.regions[index_region]
        self.assertEqual(region_ref.numberElements, region.numberElements)
        self.assertEqual(region_ref.regionMassDensity_g_cm3, region.regionMassDensity_g_cm3)
        self.assertEqual(region_ref.regionType, region.regionType)
        self.assertEqual(region_ref.regionDimensions, region.regionDimensions)
        index_element = 0
        element = region.elements[index_element]
        element_ref = region_ref.elements[index_element]
        self.assertEqual(element_ref.atomicNumber, element.atomicNumber)
        self.assertEqual(element_ref.massFraction, element.massFraction)

        index_region = 2
        region = specimen.regions[index_region]
        region_ref = specimen_ref.regions[index_region]
        self.assertEqual(region_ref.numberElements, region.numberElements)
        self.assertEqual(region_ref.regionMassDensity_g_cm3, region.regionMassDensity_g_cm3)
        self.assertEqual(region_ref.regionType, region.regionType)
        self.assertEqual(region_ref.regionDimensions, region.regionDimensions)
        index_element = 0
        element = region.elements[index_element]
        element_ref = region_ref.elements[index_element]
        self.assertEqual(element_ref.atomicNumber, element.atomicNumber)
        self.assertEqual(element_ref.massFraction, element.massFraction)

        # self.fail("Test if the testcase is working.")

    def test_read_1_2_0(self):
        """
        Tests for method `read`.
        """

        specimen = Specimen.Specimen()

        title = "AlMgBulk5keV_version_1_2_0"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.sam".format(title)))
        specimen.read(filepath)

        self.assertEqual(version.VERSION_1_2_0.major, specimen.version.major)
        self.assertEqual(version.VERSION_1_2_0.minor, specimen.version.minor)
        self.assertEqual(version.VERSION_1_2_0.revision, specimen.version.revision)
        self.assertEqual(version.VERSION_1_2_0, specimen.version)

        specimenRef = get_specimen_reference(title)
        self.assertEqual(specimenRef.version.major, specimen.version.major)
        self.assertEqual(specimenRef.version.minor, specimen.version.minor)
        self.assertEqual(specimenRef.version.revision, specimen.version.revision)
        self.assertEqual(specimenRef.version, specimen.version)

        self.assertEqual(specimenRef.numberRegions, specimen.numberRegions)

        indexRegion = 0
        region = specimen.regions[indexRegion]
        regionRef = specimenRef.regions[indexRegion]
        self.assertEqual(regionRef.numberElements, region.numberElements)
        self.assertEqual(regionRef.regionMassDensity_g_cm3, region.regionMassDensity_g_cm3)
        self.assertEqual(regionRef.regionType, region.regionType)
        self.assertEqual(regionRef.regionDimensions, region.regionDimensions)
        indexElement = 0
        element = region.elements[indexElement]
        elementRef = regionRef.elements[indexElement]
        self.assertEqual(elementRef.atomicNumber, element.atomicNumber)
        self.assertEqual(elementRef.massFraction, element.massFraction)
        indexElement = 1
        element = region.elements[indexElement]
        elementRef = regionRef.elements[indexElement]
        self.assertEqual(elementRef.atomicNumber, element.atomicNumber)
        self.assertEqual(elementRef.massFraction, element.massFraction)

        indexRegion = 1
        region = specimen.regions[indexRegion]
        regionRef = specimenRef.regions[indexRegion]
        self.assertEqual(regionRef.numberElements, region.numberElements)
        self.assertEqual(regionRef.regionMassDensity_g_cm3, region.regionMassDensity_g_cm3)
        self.assertEqual(regionRef.regionType, region.regionType)
        self.assertEqual(regionRef.regionDimensions, region.regionDimensions)
        indexElement = 0
        element = region.elements[indexElement]
        elementRef = regionRef.elements[indexElement]
        self.assertEqual(elementRef.atomicNumber, element.atomicNumber)
        self.assertEqual(elementRef.massFraction, element.massFraction)

        indexRegion = 2
        region = specimen.regions[indexRegion]
        regionRef = specimenRef.regions[indexRegion]
        self.assertEqual(regionRef.numberElements, region.numberElements)
        self.assertEqual(regionRef.regionMassDensity_g_cm3, region.regionMassDensity_g_cm3)
        self.assertEqual(regionRef.regionType, region.regionType)
        self.assertEqual(regionRef.regionDimensions, region.regionDimensions)
        indexElement = 0
        element = region.elements[indexElement]
        elementRef = regionRef.elements[indexElement]
        self.assertEqual(elementRef.atomicNumber, element.atomicNumber)
        self.assertEqual(elementRef.massFraction, element.massFraction)

        # self.fail("Test if the testcase is working.")

    def test_read_1_2_1(self):
        """
        Tests for method `read`.
        """

        specimen = Specimen.Specimen()

        title = "AlMgBulk5keV_version_1_2_1"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.sam".format(title)))
        specimen.read(filepath)

        self.assertEqual(version.VERSION_1_2_1.major, specimen.version.major)
        self.assertEqual(version.VERSION_1_2_1.minor, specimen.version.minor)
        self.assertEqual(version.VERSION_1_2_1.revision, specimen.version.revision)
        self.assertEqual(version.VERSION_1_2_1, specimen.version)

        specimenRef = get_specimen_reference(title)
        self.assertEqual(specimenRef.version.major, specimen.version.major)
        self.assertEqual(specimenRef.version.minor, specimen.version.minor)
        self.assertEqual(specimenRef.version.revision, specimen.version.revision)
        self.assertEqual(specimenRef.version, specimen.version)

        self.assertEqual(specimenRef.numberRegions, specimen.numberRegions)

        indexRegion = 0
        region = specimen.regions[indexRegion]
        regionRef = specimenRef.regions[indexRegion]
        self.assertEqual(regionRef.numberElements, region.numberElements)
        self.assertEqual(regionRef.regionMassDensity_g_cm3, region.regionMassDensity_g_cm3)
        self.assertEqual(regionRef.regionType, region.regionType)
        self.assertEqual(regionRef.regionDimensions, region.regionDimensions)
        indexElement = 0
        element = region.elements[indexElement]
        elementRef = regionRef.elements[indexElement]
        self.assertEqual(elementRef.atomicNumber, element.atomicNumber)
        self.assertEqual(elementRef.massFraction, element.massFraction)
        indexElement = 1
        element = region.elements[indexElement]
        elementRef = regionRef.elements[indexElement]
        self.assertEqual(elementRef.atomicNumber, element.atomicNumber)
        self.assertEqual(elementRef.massFraction, element.massFraction)

        indexRegion = 1
        region = specimen.regions[indexRegion]
        regionRef = specimenRef.regions[indexRegion]
        self.assertEqual(regionRef.numberElements, region.numberElements)
        self.assertEqual(regionRef.regionMassDensity_g_cm3, region.regionMassDensity_g_cm3)
        self.assertEqual(regionRef.regionType, region.regionType)
        self.assertEqual(regionRef.regionDimensions, region.regionDimensions)
        indexElement = 0
        element = region.elements[indexElement]
        elementRef = regionRef.elements[indexElement]
        self.assertEqual(elementRef.atomicNumber, element.atomicNumber)
        self.assertEqual(elementRef.massFraction, element.massFraction)

        indexRegion = 2
        region = specimen.regions[indexRegion]
        regionRef = specimenRef.regions[indexRegion]
        self.assertEqual(regionRef.numberElements, region.numberElements)
        self.assertEqual(regionRef.regionMassDensity_g_cm3, region.regionMassDensity_g_cm3)
        self.assertEqual(regionRef.regionType, region.regionType)
        self.assertEqual(regionRef.regionDimensions, region.regionDimensions)
        indexElement = 0
        element = region.elements[indexElement]
        elementRef = regionRef.elements[indexElement]
        self.assertEqual(elementRef.atomicNumber, element.atomicNumber)
        self.assertEqual(elementRef.massFraction, element.massFraction)

        # self.fail("Test if the testcase is working.")

    def test_read_1_4_1(self):
        """
        Tests for method `read`.
        """

        specimen = Specimen.Specimen()

        title = "AlMgBulk5keV_version_1_4_1"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.sam".format(title)))
        specimen.read(filepath)

        self.assertEqual(version.VERSION_1_4_1.major, specimen.version.major)
        self.assertEqual(version.VERSION_1_4_1.minor, specimen.version.minor)
        self.assertEqual(version.VERSION_1_4_1.revision, specimen.version.revision)
        self.assertEqual(version.VERSION_1_4_1, specimen.version)

        specimenRef = get_specimen_reference(title)
        self.assertEqual(specimenRef.version.major, specimen.version.major)
        self.assertEqual(specimenRef.version.minor, specimen.version.minor)
        self.assertEqual(specimenRef.version.revision, specimen.version.revision)
        self.assertEqual(specimenRef.version, specimen.version)

        self.assertEqual(specimenRef.numberRegions, specimen.numberRegions)

        indexRegion = 0
        region = specimen.regions[indexRegion]
        regionRef = specimenRef.regions[indexRegion]
        self.assertEqual(regionRef.numberElements, region.numberElements)
        self.assertEqual(regionRef.regionMassDensity_g_cm3, region.regionMassDensity_g_cm3)
        self.assertEqual(regionRef.regionType, region.regionType)
        self.assertEqual(regionRef.regionDimensions, region.regionDimensions)
        indexElement = 0
        element = region.elements[indexElement]
        elementRef = regionRef.elements[indexElement]
        self.assertEqual(elementRef.atomicNumber, element.atomicNumber)
        self.assertEqual(elementRef.massFraction, element.massFraction)
        indexElement = 1
        element = region.elements[indexElement]
        elementRef = regionRef.elements[indexElement]
        self.assertEqual(elementRef.atomicNumber, element.atomicNumber)
        self.assertEqual(elementRef.massFraction, element.massFraction)

        indexRegion = 1
        region = specimen.regions[indexRegion]
        regionRef = specimenRef.regions[indexRegion]
        self.assertEqual(regionRef.numberElements, region.numberElements)
        self.assertEqual(regionRef.regionMassDensity_g_cm3, region.regionMassDensity_g_cm3)
        self.assertEqual(regionRef.regionType, region.regionType)
        self.assertEqual(regionRef.regionDimensions, region.regionDimensions)
        indexElement = 0
        element = region.elements[indexElement]
        elementRef = regionRef.elements[indexElement]
        self.assertEqual(elementRef.atomicNumber, element.atomicNumber)
        self.assertEqual(elementRef.massFraction, element.massFraction)

        indexRegion = 2
        region = specimen.regions[indexRegion]
        regionRef = specimenRef.regions[indexRegion]
        self.assertEqual(regionRef.numberElements, region.numberElements)
        self.assertEqual(regionRef.regionMassDensity_g_cm3, region.regionMassDensity_g_cm3)
        self.assertEqual(regionRef.regionType, region.regionType)
        self.assertEqual(regionRef.regionDimensions, region.regionDimensions)
        indexElement = 0
        element = region.elements[indexElement]
        elementRef = regionRef.elements[indexElement]
        self.assertEqual(elementRef.atomicNumber, element.atomicNumber)
        self.assertEqual(elementRef.massFraction, element.massFraction)

        # self.fail("Test if the testcase is working.")

    def test_write(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        for title in testUtilities.getSimulationTitles():
            logging.info(title)

            specimenRef = get_specimen_reference(title)

            filepath = os.path.join(self.tempDataPath, "{}.sam".format(title))

            specimen = specimenRef

            specimen.write(filepath)

            # .. todo:: Make the lines comparison work.
            # filepathReference = os.path.abspath(os.path.join(self.testDataPath, "%s/%s.sam" % (title, title)))
            # linesRef = open(filepathReference, 'r').readlines()
            # lines = open(filepath, 'r').readlines()
            # self.assertListEqual(linesRef, lines)

        # self.fail("Test if the testcase is working.")

    def test_write_1_1_1(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        title = "AlMgBulk5keV_version_1_1_1"

        specimenRef = get_specimen_reference(title)

        filepath = os.path.join(self.tempDataPath, "{}.sam".format(title))

        specimen = specimenRef

        specimen.write(filepath)

        # .. todo:: Make the lines comparison work.
        # filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.sam".format(title)))
        # linesRef = open(filepathReference, 'r').readlines()
        # lines = open(filepath, 'r').readlines()
        # self.assertListEqual(linesRef, lines)

        # self.fail("Test if the testcase is working.")

    def test_write_1_2_0(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        title = "AlMgBulk5keV_version_1_2_0"

        specimenRef = get_specimen_reference(title)
        filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.sam".format(title)))

        filepath = os.path.join(self.tempDataPath, "{}.sam".format(title))

        specimen = specimenRef
        specimen.version = copy.deepcopy(version.VERSION_1_2_0)
        specimen.write(filepath)

        linesRef = open(filepathReference, 'r').readlines()
        lines = open(filepath, 'r').readlines()

        for index in range(len(linesRef)):
            lineRef = linesRef[index]
            line = lines[index]
            message = "%i:\n%s\n%s" % (index, lineRef, line)
            self.assertEqual(lineRef, line, message)

        self.assertListEqual(linesRef, lines)

        # self.fail("Test if the testcase is working.")

    def test_write_1_2_1(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        title = "AlMgBulk5keV_version_1_2_1"

        specimenRef = get_specimen_reference(title)
        filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.sam".format(title)))

        filepath = os.path.join(self.tempDataPath, "{}.sam".format(title))

        specimen = specimenRef
        specimen.version = copy.deepcopy(version.VERSION_1_2_1)
        specimen.write(filepath)

        linesRef = open(filepathReference, 'r').readlines()
        lines = open(filepath, 'r').readlines()

        for index in range(len(linesRef)):
            lineRef = linesRef[index]
            line = lines[index]
            message = "%i:\n%s\n%s" % (index, lineRef, line)
            self.assertEqual(lineRef, line, message)

        self.assertListEqual(linesRef, lines)

        # self.fail("Test if the testcase is working.")

    def test_write_1_4_1(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        title = "AlMgBulk5keV_version_1_4_1"

        specimenRef = get_specimen_reference(title)
        filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.sam".format(title)))

        filepath = os.path.join(self.tempDataPath, "{}.sam".format(title))

        specimen = specimenRef

        specimen.write(filepath)

        linesRef = open(filepathReference, 'r').readlines()
        lines = open(filepath, 'r').readlines()

        for index in range(len(linesRef)):
            lineRef = linesRef[index]
            line = lines[index]
            message = "%i:\n%s\n%s" % (index, lineRef, line)
            self.assertEqual(lineRef, line, message)

        self.assertListEqual(linesRef, lines)

        # self.fail("Test if the testcase is working.")


def get_specimen_reference(title):
    specimen = Specimen.Specimen()

    if title == "AuBC cyl":
        specimen.numberRegions = 4
        specimen.version = version.Version(1, 1, 1)

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
        specimen.version = version.Version(1, 1, 1)

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
        specimen.version = version.Version(1, 1, 1)

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
        specimen.version = version.Version(1, 1, 1)

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
        specimen.version = version.Version(1, 1, 1)

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
        specimen.version = version.Version(1, 2, 0)

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
        specimen.version = version.Version(1, 2, 1)

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
        specimen.version = version.Version(1, 4, 1)

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