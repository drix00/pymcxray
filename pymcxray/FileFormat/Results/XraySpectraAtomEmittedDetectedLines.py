#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.XraySpectraAtomEmittedDetectedLines
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Read MCXRay XraySpectraAtomEmittedDetectedLines file.
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
ENERGIES_keV = "Energy (keV)"

class XraySpectraAtomEmittedDetectedLines(BaseResults.BaseResults):
    def __init__(self):
        super(XraySpectraAtomEmittedDetectedLines, self).__init__()

        self.fieldNames = []
        self.energies_keV = []
        self.characteristics = {}

    def read(self, regionID):
        suffix = "_SpectraAtomEmittedDetectedLines_Region%i.csv" % (regionID)
        filename = self.basename + suffix
        filepath = os.path.join(self.path, filename)

        with open(filepath, 'r') as csvFile:
            reader = csv.DictReader(csvFile)

            fieldnames = reader.fieldnames
            assert fieldnames[0] == ENERGIES_keV
            self.fieldNames = fieldnames

            for row in reader:
                self.energies_keV.append(float(row[ENERGIES_keV]))

                for elementSymbol in self.fieldNames[1:]:
                    self.characteristics.setdefault(elementSymbol.strip(), []).append(float(row[elementSymbol]))

    @property
    def fieldNames(self):
        return self._fieldNames
    @fieldNames.setter
    def fieldNames(self, fieldNames):
        self._fieldNames = fieldNames

    @property
    def energies_keV(self):
        return self._energies_keV
    @energies_keV.setter
    def energies_keV(self, energies_keV):
        self._energies_keV = energies_keV

    @property
    def characteristics(self):
        return self._characteristics
    @characteristics.setter
    def characteristics(self, characteristics):
        self._characteristics = characteristics
