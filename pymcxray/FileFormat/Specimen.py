#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Specimen
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

MCXRay specimen input file.
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
import copy

# Third party modules.

# Local modules.
import pymcxray.FileFormat.Region as Region
import pymcxray.FileFormat.Version as Version

# Project modules

# Globals and constants variables.
KEY_NAME = "Name"
KEY_NUMBER_REGIONS = "NumberRegions"
KEY_REGIONS = "Regions"

class Specimen(object):
    def __init__(self):
        self.version = copy.deepcopy(Version.CURRENT_VERSION)

        self._keys = self._createKeys()

        self._parameters = {}

        self.clear()

    def _createKeys(self):
        keys = []

        keys.append(KEY_NUMBER_REGIONS)
        #keys.append(KEY_REGIONS)

        return keys

    def clear(self):
        self.numberRegions = 0
        self.regions = []
        self._shortHeader = False

    def _createExtractMethods(self):
        extractMethods = {}

        extractMethods[KEY_NUMBER_REGIONS] = int

        return extractMethods

    def read(self, filepath):
        self.clear()

        self.version.readFromFile(filepath)

        if self.version == Version.BEFORE_VERSION:
            self._readOldVersion(filepath)
        else:
            self._readWithVersion(filepath)

    def _readWithVersion(self, filepath):
        lines = open(filepath, 'r').readlines()

        indexLine = 0
        for line in lines:
            indexLine += 1

            line = line.strip()

            key = KEY_NUMBER_REGIONS
            if line.startswith(key):
                items = line.split('=')
                self.numberRegions = int(items[-1])
                break

        for _indexRegion in range(self.numberRegions):
            while lines[indexLine].strip() == "":
                indexLine += 1

            region = Region.Region()
            self.regions.append(region)
            indexLine += region.extractFromLinesWithVersion(lines[indexLine:])

    def _readOldVersion(self, filepath):
        lines = open(filepath, 'r').readlines()

        extractMethods = self._createExtractMethods()

        indexLine = 0
        while indexLine < len(lines):
            line = lines[indexLine]
            line = line.strip()

            indexLine += 1
            if not line.startswith("***") and len(line) != 0:
                self.numberRegions = extractMethods[KEY_NUMBER_REGIONS](line)

                for _indexRegion in range(self.numberRegions):
                    # Skip blank line.
                    indexLine += 1
                    region = Region.Region()
                    self.regions.append(region)
                    indexLine += region.extractFromLinesWithoutVersion(lines[indexLine:])

    def write(self, filepath):
        assert self.numberRegions == len(self.regions)

        outputFile = open(filepath, 'w')

        self._writeHeader(outputFile)

        self.version.writeLine(outputFile)

        key = KEY_NUMBER_REGIONS
        value = self.numberRegions
        line = "%s=%s\n" % (key, value)
        outputFile.write(line)
        outputFile.write("\n")

        for region in self.regions:
            lines = region.createLinesWithVersion()
            for line in lines:
                outputFile.write(line+"\n")

            outputFile.write("\n")

    def _writeHeader(self, outputFile):
        if self._shortHeader:
            headerLines = \
"""********************************************************************************
""".splitlines()
        elif self.version == Version.BEFORE_VERSION:
            headerLines = \
"""********************************************************************************
***                                  SPECIMEN
***
***    First Entry is:
***        number of region (integer)
***
***    then region by region:
***        number of elements in region
***        first element atomic number (integer)   mass concentration (double)
***        ...
***        last element atomic number (integer)    mass concentration (double)
***        user's elements mass density if any (double)
***        region volume type: BOX, SPHERE or CYLINDER
***        region extents (all doubles):
***            BOX:      minX maxX minY maxY minZ maxZ
***            SPHERE:   posX posY posZ radius
***            CYLINDER: posX posY posZ dirX dirY dirZ lenght radius
***                      the position is the center of the base of the cylinder
***
********************************************************************************
""".splitlines()
        else:
            headerLines = \
"""********************************************************************************
***                                  SPECIMEN
***
***    First Entry is:
***        number of region (integer)
***
***    then region by region:
***        number of elements in region
***        first element atomic number (integer)   mass concentration (double)
***        ...
***        last element atomic number (integer)    mass concentration (double)
***        user's elements mass density if larger than 0.0 (double)
***        region volume type: BOX, SPHERE or CYLINDER
***        region extents (all doubles):
***            BOX:      minX maxX minY maxY minZ maxZ
***            SPHERE:   posX posY posZ radius
***            CYLINDER: posX posY posZ dirX dirY dirZ lenght radius
***                      the position is the center of the base of the cylinder
***
********************************************************************************
""".splitlines()

        for line in headerLines:
            outputFile.write(line+'\n')

    @property
    def version(self):
        return self._version
    @version.setter
    def version(self, version):
        self._version = version

    @property
    def name(self):
        return self._parameters[KEY_NAME]
    @name.setter
    def name(self, name):
        self._parameters[KEY_NAME] = name

    @property
    def numberRegions(self):
        return self._parameters[KEY_NUMBER_REGIONS]
    @numberRegions.setter
    def numberRegions(self, numberRegions):
        self._parameters[KEY_NUMBER_REGIONS] = numberRegions

    @property
    def regions(self):
        return self._parameters[KEY_REGIONS]
    @regions.setter
    def regions(self, regions):
        self._parameters[KEY_REGIONS] = regions
