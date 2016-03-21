#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.PhirhozEmittedCharacteristicThinFilm
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Read mcxray phirhoz thin film emitted results.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2014 Hendrix Demers"
__license__ = ""

# Standard library modules.
import os.path
import csv

# Third party modules.

# Local modules.

# Project modules
import pymcxray.FileFormat.Results.BaseResults as BaseResults

# Globals and constants variables.
INDEX_REGION = "Region"
ATOM_SYMBOL = " Symbol"
LINE_KA1 = " Line Ka1"
LINE_KA2 = " Line Ka2"
LINE_KB1 = " Line Kb1"
LINE_KB2 = " Line Kb2"
LINE_LA = " Line La"
LINE_LB1 = " Line Lb1"
LINE_LB2 = " Line Lb2"
LINE_LG = " Line Lg"
LINE_MA = " Line Ma"

# SimulationMCXrayPhirhozTestCases_Cu_E500d0keV_N100000e_PhirhozEmittedCharacteristicThinFilm.csv
class PhirhozEmittedCharacteristicThinFilm(BaseResults.BaseResults):
    def __init__(self):
        super(PhirhozEmittedCharacteristicThinFilm, self).__init__()

        self.intensities = []

    def read(self):
        suffix = "_PhirhozEmittedCharacteristicThinFilm.csv"
        filename = self.basename + suffix
        filepath = os.path.join(self.path, filename)

        with open(filepath, 'r') as csvFile:
            reader = csv.DictReader(csvFile, self.fieldNames)
            # Skip header row
            next(reader)

            for intensityRow in reader:
                intensity = intensityRow
                for key in intensity:
                    try:
                        intensity[key] = intensity[key].strip()
                    except AttributeError:
                        pass

                self._intensities.append(intensity)

    def getIntensity(self, regionID, atomicSymbol, xrayLine):
        intensity = 0.0

        for data in self.intensities:
            if data[INDEX_REGION] == str(regionID) and data[ATOM_SYMBOL] == atomicSymbol:
                if not xrayLine.startswith(" Line"):
                    subshellLabel = " Line %s" % xrayLine
                else:
                    subshellLabel = xrayLine
                intensity = float(data[subshellLabel])
                break

        return intensity

    @property
    def fieldNames(self):
        fieldNames = []
        fieldNames.append(INDEX_REGION)
        fieldNames.append(ATOM_SYMBOL)
        fieldNames.append(LINE_KA1)
        fieldNames.append(LINE_KA2)
        fieldNames.append(LINE_KB1)
        fieldNames.append(LINE_KB2)
        fieldNames.append(LINE_LA)
        fieldNames.append(LINE_LB1)
        fieldNames.append(LINE_LB2)
        fieldNames.append(LINE_LG)
        fieldNames.append(LINE_MA)

        return fieldNames

    @property
    def intensities(self):
        return self._intensities
    @intensities.setter
    def intensities(self, intensities):
        self._intensities = intensities

    @property
    def numberRegions(self):
        return len(self.intensities)
