#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.PhirhozGeneratedCharacteristicThinFilm
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Read mcxray phirhoz thin film generated results.
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
SUBSHELL_K = " Shell K"
SUBSHELL_L = " Shell L"
SUBSHELL_M = " Shell M"

# SimulationMCXrayPhirhozTestCases_Cu_E500d0keV_N100000e_PhirhozGeneratedCharacteristicThinFilm.csv
class PhirhozGeneratedCharacteristicThinFilm(BaseResults.BaseResults):
    def __init__(self):
        super(PhirhozGeneratedCharacteristicThinFilm, self).__init__()

        self.intensities = []

    def read(self):
        suffix = "_PhirhozGeneratedCharacteristicThinFilm.csv"
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
                if not xrayLine.startswith(" Shell"):
                    subshellLabel = " Shell %s" % xrayLine
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
        fieldNames.append(SUBSHELL_K)
        fieldNames.append(SUBSHELL_L)
        fieldNames.append(SUBSHELL_M)

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

if __name__ == '__main__': #pragma: no cover
    import pyHendrixDemersTools.Runner as Runner
    Runner.Runner().run(runFunction=None)
