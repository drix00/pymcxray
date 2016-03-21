#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.PhirhozRegion
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

MCXRay phirhoz results file for a region.
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
import pymcxray.FileFormat.Results.RegionVolume as RegionVolume
import pymcxray.FileFormat.Results.PhirhozElement as PhirhozElement
import pymcxray.FileFormat.Results.Phirhoz as Phirhoz

# Globals and constants variables.

KEY_REGION = "Region"
KEY_PHIRHOZ_DISTISTRIBUTION = "Phi_DistX"
KEY_ELEMENTS = "elements"
KEY_PHIRHOZ_BACKGROUND = "Background"
KEY_PHIRHOZ_BACKGROUND_SUMMARY = "Background Summary"

KEY_REGION_ID = "Region"

SHELL_K = "K"
SHELL_L = "L"
SHELL_M = "M"

class PhirhozRegion(object):
    def __init__(self, numberEnergyWindows, numberLayersZ):
        self._parameters = {}

        self._numberEnergyWindows = numberEnergyWindows
        self._numberLayersZ = numberLayersZ

    def readFromLines(self, lines):
        indexLine = 0

        for line in lines[indexLine:]:
            indexLine += 1

            if line.startswith(KEY_REGION):
                items = line.split()
                self.regionID = int(items[1])
                break

        indexLine += self.readRegionVolume(lines[indexLine:])
        indexLine += self.readPhirhozDistributions(lines[indexLine:])
        indexLine += self.readElements(lines[indexLine:])

        indexLine += self.readBackgroundPhirhozs(lines[indexLine:])
        indexLine += self.readCharacteristicPhirhozs(lines[indexLine:])

        return indexLine

    def readRegionVolume(self, lines):
        lineIndex = 0

        regionVolume = RegionVolume.RegionVolume()
        # todo read region volume info.
        lineIndex += 8
        return lineIndex

    def readPhirhozDistributions(self, lines):
        indexLine = 0
        for line in lines:
            indexLine += 1
            if line.strip().startswith(KEY_PHIRHOZ_DISTISTRIBUTION):
                break
        else:
            message = "Cannot find the section header in the liens: %s" % (KEY_PHIRHOZ_DISTISTRIBUTION)
            raise ValueError(message)

        # todo read phirhoz distribution.
        indexLine += 2

        return indexLine

    def readElements(self, lines):
        indexLine = 0

        self.elements = []
        for line in lines:
            indexLine += 1
            if line.strip().endswith(KEY_ELEMENTS):
                items = line.split()
                self.numberElements = int(items[0])
                break
        else:
            message = "Cannot find the section header in the liens: %s" % (KEY_ELEMENTS)
            raise ValueError(message)

        for indexElements in range(self.numberElements):
            line = lines[indexLine]
            indexLine += 1

            element = PhirhozElement.PhirhozElement()
            element.readFromLine(line)
            self.elements.append(element)

        assert len(self.elements) == self.numberElements

        return indexLine

    def readBackgroundPhirhozs(self, lines):
        indexLine = 0
        for indexWindows in range(self._numberEnergyWindows):
            for line in lines[indexLine:]:
                indexLine += 1
                if line.strip().startswith(KEY_PHIRHOZ_BACKGROUND):
                    items = line.split('=')
                    intensity = float(items[-1])
                    indexStart = line.find('[')
                    indexEnd = line.find(']')

                    items = line[indexStart+1:indexEnd].split(',')
                    energyWindowLow = float(items[0])
                    energyWindowHigh = float(items[1])
                    break
            else:
                message = "Cannot find the section header in the liens: %s" % (KEY_PHIRHOZ_BACKGROUND)
                raise ValueError(message)

        for indexDepth in range(self._numberLayersZ):
            line = lines[indexLine]
            indexLine += 1
            items = line.split()
            depth_A = float(items[0])
            phirhoz = float(items[1])

        # Read summary
        for line in lines[indexLine:]:
            indexLine += 1
            if line.strip().startswith(KEY_PHIRHOZ_BACKGROUND_SUMMARY):
                break
        else:
            message = "Cannot find the section header in the liens: %s" % (KEY_PHIRHOZ_BACKGROUND_SUMMARY)
            raise ValueError(message)

        for indexWindows in range(self._numberEnergyWindows):
            line  = lines[indexLine]
            indexLine += 1

        return indexLine

    def readCharacteristicPhirhozs(self, lines):
        indexLine = 0

        self.characteristicPhirhoz = {}
        for element in self.elements:
            self.characteristicPhirhoz.setdefault(element.symbol, {})

            if element.isIonizationShell_K:
                phirhoz = Phirhoz.Phirhoz(element.symbol, SHELL_K)
                indexLine += phirhoz.readFromLines(lines[indexLine:])
                self.characteristicPhirhoz[element.symbol][SHELL_K] = phirhoz

            if element.isIonizationShell_L:
                phirhoz = Phirhoz.Phirhoz(element.symbol, SHELL_L)
                indexLine += phirhoz.readFromLines(lines[indexLine:])
                self.characteristicPhirhoz[element.symbol][SHELL_L] = phirhoz

            if element.isIonizationShell_M:
                phirhoz = Phirhoz.Phirhoz(element.symbol, SHELL_M)
                indexLine += phirhoz.readFromLines(lines[indexLine:])
                self.characteristicPhirhoz[element.symbol][SHELL_M] = phirhoz

        return indexLine

    @property
    def regionID(self):
        return self._parameters[KEY_REGION_ID]
    @regionID.setter
    def regionID(self, regionID):
        self._parameters[KEY_REGION_ID] = regionID
