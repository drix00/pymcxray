#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.XrayIntensities
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Xray intensities result file from MCXRay.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2012 Hendrix Demers"
__license__ = ""

# Standard library modules.
import os.path
import csv

# Third party modules.

# Local modules.

# Project modules
import pymcxray.FileFormat.Results.BaseResults as BaseResults

# Globals and constants variables.
INDEX_REGION = "Index Region"
INDEX_ATOM = "Index Atom"
ATOMIC_NUMBER = "Atomic number"
LINE = "Line"
LINE_ENERGY_KEV = "Line energy (keV)"
INTENSITY_GENERATED = "Intensity Generated (photons/e/sr)"
INTENSITY_GENERATED_DETECTED = "Intensity Generated Detected (photons)"
INTENSITY_EMITTED = "Intensity Emitted (photons/e/sr)"
INTENSITY_EMITTED_DETECTED = "Intensity Emitted Detected (photons)"

class XrayIntensities(BaseResults.BaseResults):
    def __init__(self):
        super(XrayIntensities, self).__init__()

        self.intensities = []

    def read(self):
        suffix = "_XrayIntensities.csv"
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

    def getDetectedIntensity(self, atomicNumber, xrayLine):
        return self.getIntensityEmittedDetected(atomicNumber, xrayLine)

    def getIntensityEmitted(self, atomicNumber, xrayLine, total=False):
        if total:
            data = 0.0
        else:
            data = {}

        for intensity in self.intensities:
            indexRegion = intensity[INDEX_REGION]

            if not xrayLine.startswith("Line"):
                xrayLineLabel = "Line %s" % (xrayLine)
            else:
                xrayLineLabel = xrayLine
            if intensity[ATOMIC_NUMBER] == str(atomicNumber) and intensity[LINE].startswith(xrayLineLabel):
                if not total and indexRegion not in data:
                    data[indexRegion] = 0.0

                if total:
                    data += float(intensity[INTENSITY_EMITTED])
                else:
                    data[indexRegion] += float(intensity[INTENSITY_EMITTED])

        return data

    def getIntensityEmittedDetected(self, atomicNumber, xrayLine):
        data = {}

        for intensity in self.intensities:
            indexRegion = intensity[INDEX_REGION]

            xrayLineLabel = "Line %s" % (xrayLine)
            if intensity[ATOMIC_NUMBER] == str(atomicNumber) and intensity[LINE].startswith(xrayLineLabel):
                if indexRegion not in data:
                    data[indexRegion] = 0.0

                data[indexRegion] += float(intensity[INTENSITY_EMITTED_DETECTED])

        return data

    def getIntensityGenerated(self, atomicNumber, xraySubshell, total=False):
        if total:
            data = 0.0
        else:
            data = {}

        for intensity in self.intensities:
            indexRegion = intensity[INDEX_REGION]

            if xraySubshell == "K":
                xrayLine = "Ka1"
            elif xraySubshell == "L":
                xrayLine = "Ka1"
            elif xraySubshell == "M":
                xrayLine = "Ma"
            xrayLineLabel = "Line %s" % (xrayLine)
            if intensity[ATOMIC_NUMBER] == str(atomicNumber) and intensity[LINE].startswith(xrayLineLabel):
                if not total and indexRegion not in data:
                    data[indexRegion] = 0.0

                if total:
                    data += float(intensity[INTENSITY_GENERATED])
                else:
                    data[indexRegion] += float(intensity[INTENSITY_GENERATED])

        return data

    def getIntensityGeneratedDetected(self, atomicNumber, xraySubshell):
        data = {}

        for intensity in self.intensities:
            indexRegion = intensity[INDEX_REGION]

            if xraySubshell == "K":
                xrayLine = "Ka1"
            elif xraySubshell == "L":
                xrayLine = "Ka1"
            elif xraySubshell == "M":
                xrayLine = "Ma"
            xrayLineLabel = "Line %s" % (xrayLine)
            if intensity[ATOMIC_NUMBER] == str(atomicNumber) and intensity[LINE].startswith(xrayLineLabel):
                if indexRegion not in data:
                    data[indexRegion] = 0.0

                data[indexRegion] += float(intensity[INTENSITY_GENERATED_DETECTED])

        return data

    def getAtomicNumberLineEnergySets(self):
        atomicNumberLineSets = set()

        for intensity in self.intensities:
            atomicNumber = intensity[ATOMIC_NUMBER]
            line = intensity[LINE]
            energy_keV = intensity[LINE_ENERGY_KEV]

            atomicNumberLineSets.add((atomicNumber, line, energy_keV))

        return atomicNumberLineSets

    @property
    def fieldNames(self):
        fieldNames = []
        fieldNames.append(INDEX_REGION)
        fieldNames.append(INDEX_ATOM)
        fieldNames.append(ATOMIC_NUMBER)
        fieldNames.append(LINE)
        fieldNames.append(LINE_ENERGY_KEV)
        fieldNames.append(INTENSITY_GENERATED)
        fieldNames.append(INTENSITY_GENERATED_DETECTED)
        fieldNames.append(INTENSITY_EMITTED)
        fieldNames.append(INTENSITY_EMITTED_DETECTED)

        return fieldNames

    @property
    def intensities(self):
        return self._intensities
    @intensities.setter
    def intensities(self, intensities):
        self._intensities = intensities

    @property
    def numberIntensities(self):
        return len(self.intensities)

if __name__ == '__main__': #pragma: no cover
    import pyHendrixDemersTools.Runner as Runner
    Runner.Runner().run(runFunction=None)
