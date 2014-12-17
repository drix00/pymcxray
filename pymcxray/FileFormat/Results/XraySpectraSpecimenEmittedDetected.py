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

# Local modules.

# Project modules
import pymcxray.FileFormat.Results.BaseResults as BaseResults

# Globals and constants variables.
ENERGIES_keV = "Energy (keV)"
SPECTRUM_TOTAL = "Spectra Total"
SPECTRUM_LINES = "Spectra Lines"
SPECTRUM_BREMSSTRAHLUNG = "Spectra Bremsstrahlung"

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

        with open(filepath, 'r') as csvFile:
            reader = csv.DictReader(csvFile, self.fieldNames)
            # Skip header row
            next(reader)

            for row in reader:
                self.energies_keV.append(float(row[ENERGIES_keV]))
                self.totals.append(float(row[SPECTRUM_TOTAL]))
                self.characteristics.append(float(row[SPECTRUM_LINES]))
                self.backgrounds.append(float(row[SPECTRUM_BREMSSTRAHLUNG]))

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

if __name__ == '__main__': #pragma: no cover
    import pyHendrixDemersTools.Runner as Runner
    Runner.Runner().run(runFunction=None)
