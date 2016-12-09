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
import numpy as np

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

HDF5_PHIRHOZ_GENERATED_CHARACTERISTIC_THIN_FILM = "PhirhozGeneratedCharacteristicThinFilm"
HDF5_REGION_IDS = "Region IDs"
HDF5_XRAY_LINES = "X-ray lines"

class XrayIntensities(BaseResults.BaseResults):
    def __init__(self):
        super(XrayIntensities, self).__init__()

        self.intensities = []
        self.atomic_numbers = set()
        self.xray_lines = set()
        self.regions = set()

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
                        if key is ATOMIC_NUMBER:
                            self.atomic_numbers.add(int(intensity[key]))
                        if key is LINE:
                            line = str(intensity[key])
                            line = line[5:]
                            self.xray_lines.add(line)
                        if key is INDEX_REGION:
                            self.regions.add(int(intensity[key]))
                    except AttributeError:
                        pass

                self._intensities.append(intensity)

    def getDetectedIntensity(self, atomicNumber, xrayLine):
        return self.getIntensityEmittedDetected(atomicNumber, xrayLine)

    def getIntensityEmitted(self, atomicNumber, xrayLine, total=True):
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

    def getIntensityEmittedDetected(self, atomicNumber, xrayLine, total=True):
        if total:
            data = 0.0
        else:
            data = {}

        for intensity in self.intensities:
            indexRegion = intensity[INDEX_REGION]

            xrayLineLabel = "Line %s" % (xrayLine)
            if intensity[ATOMIC_NUMBER] == str(atomicNumber) and intensity[LINE].startswith(xrayLineLabel):
                if not total and indexRegion not in data:
                    data[indexRegion] = 0.0

                if total:
                    data += float(intensity[INTENSITY_EMITTED_DETECTED])
                else:
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

    def getIntensity(self, data_type, region_id, atomic_number, xray_line):
        xray_line = "Line " + xray_line

        if data_type == LINE_ENERGY_KEV:
            for atomicNumber, line, energy_keV in self.getAtomicNumberLineEnergySets():
                if atomicNumber == atomic_number and line == xray_line:
                    return energy_keV
            return 0.0
        elif data_type == INTENSITY_GENERATED:
            return 0.0
        elif data_type == INTENSITY_GENERATED_DETECTED:
            return 0.0
        elif data_type == INTENSITY_EMITTED:
            return 0.0
        elif data_type == INTENSITY_EMITTED_DETECTED:
            return 0.0
        else:
            return 0.0

    def write_hdf5(self, hdf5_group):
        hdf5_group = hdf5_group.require_group(HDF5_PHIRHOZ_GENERATED_CHARACTERISTIC_THIN_FILM)

        data = np.array(sorted(list(self.regions)))
        region_ids = hdf5_group.create_dataset(HDF5_REGION_IDS, dtype='i4', data=data)
        xray_lines = np.array(sorted(self.xray_lines()), dtype='S4')
        subshells = hdf5_group.create_dataset(HDF5_XRAY_LINES, dtype='S4', data=data)

        shape = (self.numberRegions, len(data))

        for atomic_number in sorted(self.atomic_numbers):
            hdf5_group_element = hdf5_group.require_group(atomic_number)

            data_types = [LINE_ENERGY_KEV, INTENSITY_GENERATED, INTENSITY_GENERATED_DETECTED, INTENSITY_EMITTED, INTENSITY_EMITTED_DETECTED]
            for data_type in data_types:
                intensity = np.zeros(shape)
                for region_id in range(self.numberRegions):
                    for xray_lines_id, xray_line in enumerate(xray_lines):
                        intensity[region_id, xray_lines_id] = self.getIntensity(data_type, region_id, atomic_number, xray_line)

                dataset = hdf5_group.create_dataset(data_type, data=intensity)
                dataset.dims.create_scale(region_ids, 'Region ID')
                dataset.dims.create_scale(subshells, 'Subshell')
                dataset.dims[0].attach_scale(region_ids)
                dataset.dims[1].attach_scale(subshells)

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
