#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.XraySpectraSpecimenEmittedDetected
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Read XraySpectraSpecimenEmittedDetected MCXRay results file.
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
ENERGIES_keV = "Energy (keV)"
SPECTRUM_TOTAL = "Spectra Total"
SPECTRUM_LINES = "Spectra Lines"
SPECTRUM_BREMSSTRAHLUNG = "Spectra Bremsstrahlung"

HDF5_XRAY_SPECTRA_SPECIMEN_EMITTED_DETECTED = "XraySpectraSpecimenEmittedDetected"
HDF5_ENERGIES_keV = ENERGIES_keV
HDF5_TOTAL = SPECTRUM_TOTAL
HDF5_CHARACTERISTIC = SPECTRUM_LINES
HDF5_BREMSSTRAHLUNG = SPECTRUM_BREMSSTRAHLUNG

class XraySpectraSpecimenEmittedDetected(BaseResults.BaseResults):
    def __init__(self):
        super(XraySpectraSpecimenEmittedDetected, self).__init__()

        self.energies_keV = []
        self.totals = []
        self.characteristics = []
        self.backgrounds = []

    def read(self):
        suffix = "_SpectraSpecimenEmittedDetected.csv"
        filename = self.basename + suffix
        filepath = os.path.join(self.path, filename)

        self._read(filepath)
        #self._read_fast(filepath)

    def _read(self, file_path):
        with open(file_path, 'r') as csvFile:
            reader = csv.DictReader(csvFile, self.fieldNames)
            # Skip header row
            next(reader)

            for row in reader:
                self.energies_keV.append(float(row[ENERGIES_keV]))
                self.totals.append(float(row[SPECTRUM_TOTAL]))
                self.characteristics.append(float(row[SPECTRUM_LINES]))
                self.backgrounds.append(float(row[SPECTRUM_BREMSSTRAHLUNG]))

    def _read(self, file_path):
        with open(file_path, 'r') as csvFile:
            reader = csv.reader(csvFile, self.fieldNames)
            # Skip header row
            next(reader)

            for items in reader:
                self.energies_keV.append(float(items[0]))
                self.totals.append(float(items[1]))
                self.characteristics.append(float(items[2]))
                self.backgrounds.append(float(items[3]))

    def _read_fast(self, file_path):
        with open(file_path, 'r') as data_file:
            data = np.loadtxt(data_file, dtype=float, delimiter =',', skiprows=1)
            self.energies_keV = data[:,0].tolist()
            self.totals = data[:,1].tolist()
            self.characteristics = data[:,2].tolist()
            self.backgrounds = data[:,3].tolist()

    def write_hdf5(self, hdf5_group):
        hdf5_group = hdf5_group.require_group(HDF5_XRAY_SPECTRA_SPECIMEN_EMITTED_DETECTED)

        hdf5_group.create_dataset(HDF5_ENERGIES_keV, data=self.energies_keV)
        hdf5_group.create_dataset(HDF5_TOTAL, data=self.totals)
        hdf5_group.create_dataset(HDF5_CHARACTERISTIC, data=self.characteristics)
        hdf5_group.create_dataset(HDF5_BREMSSTRAHLUNG, data=self.backgrounds)

    @property
    def fieldNames(self):
        fieldNames = []
        fieldNames.append(ENERGIES_keV)
        fieldNames.append(SPECTRUM_TOTAL)
        fieldNames.append(SPECTRUM_LINES)
        fieldNames.append(SPECTRUM_BREMSSTRAHLUNG)

        return fieldNames

    @property
    def energies_keV(self):
        return self._energies_keV
    @energies_keV.setter
    def energies_keV(self, energies_keV):
        self._energies_keV = energies_keV

    @property
    def totals(self):
        return self._totals
    @totals.setter
    def totals(self, totals):
        self._totals = totals

    @property
    def characteristics(self):
        return self._characteristics
    @characteristics.setter
    def characteristics(self, characteristics):
        self._characteristics = characteristics

    @property
    def backgrounds(self):
        return self._backgrounds
    @backgrounds.setter
    def backgrounds(self, backgrounds):
        self._backgrounds = backgrounds
