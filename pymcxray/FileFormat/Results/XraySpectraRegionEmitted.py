#!/usr/bin/env python
"""
.. py:currentmodule:: pymcxray.FileFormat.Results.XraySpectraRegionEmitted
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Read XraySpectraRegionEmitted mcxray result file.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = "0.1"
__date__ = "Feb 12, 2015"
__copyright__ = "Copyright (c) 2015 Hendrix Demers"
__license__ = "GPL 3"

# Standard library modules.
import os.path
import csv

# Third party modules.

# Local modules.

# Project modules
import pymcxray.FileFormat.Results.BaseResults as BaseResults

# Globals and constants variables.
FIELD_ENERGY = "Energy (keV)"
FIELD_TOTAL = " Spectrum Total"
FIELD_CHARACTERISTIC = " Spectrum Lines"
FIELD_BREMSSTRAHLUNG = " Spectrum Bremsstrahlung"

class XraySpectraRegionEmitted(BaseResults.BaseResults):
    def __init__(self):
        super(XraySpectraRegionEmitted, self).__init__()

        self.fieldnames = None

    def read(self, regionID=0):
        self.energies_keV = []
        self.total_1_ekeVsr = []
        self.characteristic_1_ekeVsr = []
        self.bremsstrahlung_1_ekeVsr = []

        suffix = "_SpectraPerElectron_1_srkeV_Region_%i.csv" % (regionID)
        filename = self.basename + suffix
        filepath = os.path.join(self.path, filename)

        if not os.path.isfile(filepath):
            raise ValueError

        self._read_fast(filepath)

    def _read(self, filepath):
        with open(filepath, 'r') as csvFile:
            reader = csv.DictReader(csvFile)

            fieldnames = reader.fieldnames
            assert fieldnames[0] == FIELD_ENERGY
            assert fieldnames[1] == FIELD_TOTAL
            assert fieldnames[2] == FIELD_CHARACTERISTIC
            assert fieldnames[3] == FIELD_BREMSSTRAHLUNG

            self.fieldnames = fieldnames

            for row in reader:
                self.energies_keV.append(float(row[FIELD_ENERGY]))
                self.total_1_ekeVsr.append(float(row[FIELD_TOTAL]))
                self.characteristic_1_ekeVsr.append(float(row[FIELD_CHARACTERISTIC]))
                self.bremsstrahlung_1_ekeVsr.append(float(row[FIELD_BREMSSTRAHLUNG]))

    def _read_fast(self, filepath):
        with open(filepath, 'r') as csvFile:
            reader = csv.reader(csvFile)
            next(reader)

            for items in reader:
                self.energies_keV.append(float(items[0]))
                self.total_1_ekeVsr.append(float(items[1]))
                self.characteristic_1_ekeVsr.append(float(items[2]))
                self.bremsstrahlung_1_ekeVsr.append(float(items[3]))

    def _indice(self, energy_keV):
        energy_keV = float(energy_keV)
        delta_eV = self.energies_keV[0]
        for index, E_keV in enumerate(self.energies_keV):
#            if E_keV - delta_eV <= energy_keV < E_keV + delta_eV:
            if energy_keV > E_keV + delta_eV:
                continue
            else:
                return index

        raise IndexError

    def totalValue_1_ekeVsr(self, energy_keV):
            index = self._indice(energy_keV)
            return self._total_1_ekeVsr[index]

    def characteristicValue_1_ekeVsr(self, energy_keV):
            index = self._indice(energy_keV)
            return self.characteristic_1_ekeVsr[index]

    def bremsstrahlungValue_1_ekeVsr(self, energy_keV):
            index = self._indice(energy_keV)
            return self.bremsstrahlung_1_ekeVsr[index]

    @property
    def fieldnames(self):
        return self._fieldnames
    @fieldnames.setter
    def fieldnames(self, fieldnames):
        self._fieldnames = fieldnames

    @property
    def energies_keV(self):
        return self._energies_keV
    @energies_keV.setter
    def energies_keV(self, energies_keV):
        self._energies_keV = energies_keV

    @property
    def total_1_ekeVsr(self):
        return self._total_1_ekeVsr
    @total_1_ekeVsr.setter
    def total_1_ekeVsr(self, total_1_ekeVsr):
        self._total_1_ekeVsr = total_1_ekeVsr

    @property
    def characteristic_1_ekeVsr(self):
        return self._characteristic_1_ekeVsr
    @characteristic_1_ekeVsr.setter
    def characteristic_1_ekeVsr(self, characteristic_1_ekeVsr):
        self._characteristic_1_ekeVsr= characteristic_1_ekeVsr

    @property
    def bremsstrahlung_1_ekeVsr(self):
        return self._bremsstrahlung_1_ekeVsr
    @bremsstrahlung_1_ekeVsr.setter
    def bremsstrahlung_1_ekeVsr(self, bremsstrahlung_1_ekeVsr):
        self._bremsstrahlung_1_ekeVsr = bremsstrahlung_1_ekeVsr

def run():
    pass

if __name__ == '__main__':  #pragma: no cover
    run()