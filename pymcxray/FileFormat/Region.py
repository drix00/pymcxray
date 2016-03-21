#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Region
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

MCXRay region input file.
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

# Third party modules.

# Local modules.

# Project modules
import pymcxray.FileFormat.Element as Element
import pymcxray.FileFormat.RegionDimensions as RegionDimensions
import pymcxray.FileFormat.RegionType as RegionType
import pymcxray.FileFormat.FileReaderWriterTools as FileReaderWriterTools

# Globals and constants variables.
KEY_NUMBER_ELEMENTS = "NumberElements"
KEY_USER_DEFINED_MASS_DENSITY = "UserDefinedMassDensity"
KEY_REGIONS_TYPE = "RegionType"

class Region(object):
    def __init__(self):
        self._parameters = {}

        self.clear()

    def clear(self):
        self.numberElements = 0
        self.elements = []
        self.regionMassDensity_g_cm3 = None
        self.regionType = None
        self.regionDimensions = None

    def _createKeys(self):
        keys = []

        keys.append(KEY_NUMBER_ELEMENTS)
        keys.append(KEY_USER_DEFINED_MASS_DENSITY)
        keys.append(KEY_REGIONS_TYPE)

        return keys

    def _createExtractMethods(self):
        extractMethods = {}

        extractMethods[KEY_NUMBER_ELEMENTS] = int
        extractMethods[KEY_USER_DEFINED_MASS_DENSITY] = float
        extractMethods[KEY_REGIONS_TYPE] = str

        return extractMethods

    def extractFromLinesWithoutVersion(self, lines):
        self.clear()

        indexLine = 0
        self.numberElements = int(lines[indexLine])
        indexLine += 1

        for _indexElement in range(self.numberElements):
            element = Element.Element()
            element.extractFromLineOldVersion(lines[indexLine])
            self.elements.append(element)
            indexLine += 1

        # Test if the region mass density is defined by the user in the file.
        try:
            regionMassDensity_g_cm3 = float(lines[indexLine])
            self.regionMassDensity_g_cm3 = regionMassDensity_g_cm3
            indexLine += 1
        except ValueError:
            pass

        self.regionType = self._extractRegionType(lines[indexLine])
        indexLine += 1

        self.regionDimensions = RegionDimensions.createRegionDimensions(self.regionType)
        self.regionDimensions.extractFromLineOldVersion(lines[indexLine])
        indexLine += 1

        return indexLine

    def extractFromLinesWithVersion(self, lines):
        extractMethods = self._createExtractMethods()

        indexLine = 0
        key = KEY_NUMBER_ELEMENTS
        line = lines[indexLine]
        if line.startswith(key):
            items = line.split('=')
            self.numberElements = extractMethods[key](items[-1])
            indexLine += 1

        for _indexElement in range(self.numberElements):
            element = Element.Element()
            indexLine +=element.extractFromLinesWithKey(lines[indexLine:])
            self.elements.append(element)

        key = KEY_USER_DEFINED_MASS_DENSITY
        line = lines[indexLine]
        if line.startswith(key):
            items = line.split('=')
            regionMassDensity_g_cm3 = extractMethods[key](items[-1])
            if regionMassDensity_g_cm3 > 0.0:
                self.regionMassDensity_g_cm3 = regionMassDensity_g_cm3
            indexLine += 1

        self.regionType = self._extractRegionTypeWithKey(lines[indexLine])
        indexLine += 1

        self.regionDimensions = RegionDimensions.createRegionDimensions(self.regionType)
        self.regionDimensions.extractFromLinesWithKey(lines[indexLine])
        indexLine += 1

        return indexLine


    def _extractRegionType(self, line):
        line = line.strip()
        if line == RegionType.REGION_TYPE_BOX:
            return RegionType.REGION_TYPE_BOX
        elif line == RegionType.REGION_TYPE_CYLINDER:
            return RegionType.REGION_TYPE_CYLINDER
        elif line == RegionType.REGION_TYPE_SPHERE:
            return RegionType.REGION_TYPE_SPHERE

    def _extractRegionTypeWithKey(self, line):
        key = KEY_REGIONS_TYPE
        line = line.strip()
        if line.startswith(key):
            items = line.split('=')
            regionType = str(items[-1]).strip()

            if regionType == RegionType.REGION_TYPE_BOX:
                return RegionType.REGION_TYPE_BOX
            elif regionType == RegionType.REGION_TYPE_CYLINDER:
                return RegionType.REGION_TYPE_CYLINDER
            elif regionType == RegionType.REGION_TYPE_SPHERE:
                return RegionType.REGION_TYPE_SPHERE

    def createLinesWithoutVersion(self):
        assert self.numberElements == len(self.elements)

        lines = []

        line = "%i" % (self.numberElements)
        lines.append(line)

        for element in self.elements:
            line = element.createLineOldVersion()
            lines.append(line)

        if self.regionMassDensity_g_cm3 is not None:
            line = "%.15f" % (self.regionMassDensity_g_cm3)
            lines.append(line)

        line = "%s" % (self.regionType)
        lines.append(line)

        line = self.regionDimensions.createLineOldVersion()
        lines.append(line)

        return lines

    def createLinesWithVersion(self):
        assert self.numberElements == len(self.elements)

        lines = []

        key = KEY_NUMBER_ELEMENTS
        value = self.numberElements
        line = "%s=%s" % (key, value)
        lines.append(line)

        for element in self.elements:
            elementLines = element.createLinesWithKey()
            for line in elementLines:
                lines.append(line)

        key = KEY_USER_DEFINED_MASS_DENSITY
        if self.regionMassDensity_g_cm3 is not None:
            value = self.regionMassDensity_g_cm3
        else:
            value = 0.0
        value = FileReaderWriterTools.reduceAfterDot(value)
        line = "%s=%s" % (key, value)
        lines.append(line)

        key = KEY_REGIONS_TYPE
        value = self.regionType
        line = "%s=%s" % (key, value)
        lines.append(line)

        line = self.regionDimensions.createLineWithKey()
        lines.append(line)

        return lines
