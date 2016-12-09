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
import numpy as np

# Local modules.

# Project modules
import pymcxray.FileFormat.Results.BaseResults as BaseResults

# Globals and constants variables.
INDEX_REGION = "Region"
ATOM_SYMBOL = " Symbol"
SUBSHELL_K = " Shell K"
SUBSHELL_L = " Shell L"
SUBSHELL_M = " Shell M"

HDF5_PHIRHOZ_GENERATED_CHARACTERISTIC_THIN_FILM = "PhirhozGeneratedCharacteristicThinFilm"
HDF5_REGION_IDS = "Region IDs"
HDF5_SUBSHELLS = "Subshells"
HDF5_SUBSHELL_K = "K"
HDF5_SUBSHELL_L = "L"
HDF5_SUBSHELL_M = "M"

# SimulationMCXrayPhirhozTestCases_Cu_E500d0keV_N100000e_PhirhozGeneratedCharacteristicThinFilm.csv
class PhirhozGeneratedCharacteristicThinFilm(BaseResults.BaseResults):
    def __init__(self):
        super(PhirhozGeneratedCharacteristicThinFilm, self).__init__()

        self.intensities = []
        self.symbols = set()
        self.regions = set()

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
                        if key is ATOM_SYMBOL:
                            self.symbols.add(intensity[key])
                        if key is INDEX_REGION:
                            self.regions.add(int(intensity[key]))
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

    def get_symbols(self):
        return self.symbols

    def get_subshells(self):
        return [HDF5_SUBSHELL_K, HDF5_SUBSHELL_L, HDF5_SUBSHELL_M]

    def write_hdf5(self, hdf5_group):
        hdf5_group = hdf5_group.require_group(HDF5_PHIRHOZ_GENERATED_CHARACTERISTIC_THIN_FILM)

        symbols = self.get_symbols()

        shape = (self.numberRegions, 3)

        data = np.array(sorted(list(self.regions)))
        region_ids = hdf5_group.create_dataset(HDF5_REGION_IDS, dtype='i4', data=data)
        data = np.array(sorted(self.get_subshells()), dtype='S4')
        subshells = hdf5_group.create_dataset(HDF5_SUBSHELLS, dtype='S4', data=data)

        for symbol in symbols:
            intensity = np.zeros(shape)
            for region_id in range(self.numberRegions):
                for subshell_id, subshell in enumerate(self.get_subshells()):
                    intensity[region_id, subshell_id] = self.getIntensity(region_id, symbol, subshell)

            dataset = hdf5_group.create_dataset(symbol, data=intensity)
            dataset.dims.create_scale(region_ids, 'Region ID')
            dataset.dims.create_scale(subshells, 'Subshell')
            dataset.dims[0].attach_scale(region_ids)
            dataset.dims[1].attach_scale(subshells)

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
        return len(self.regions)
