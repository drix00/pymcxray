#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.ElectronResults
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Read ElectronResults MCXRay results file.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2012 Hendrix Demers"
__license__ = ""

# Standard library modules.
import os.path

# Third party modules.

# Local modules.

# Project modules
import pymcxray.FileFormat.Results.BaseResults as BaseResults

# Globals and constants variables.
NUMBER_SIMULATED_ELECTRONS = "Total simulated electrons"
NUMBER_INTERNAL_ELECTRONS = "Number of internal electrons"
NUMBER_BACKSCATTERED_ELECTRONS = "Number of backscattered electrons"
NUMBER_TRANSMITTED_ELECTRONS = "Number of transmitted electrons"
NUMBER_SKIRTED_ELECTRONS = "Number of skirted electrons"
NUMBER_ELECTRON_COLLISIONS = "Number of electron collisions"
FRACTION_INTERNAL_ELECTRONS = "Internal coefficient"
FRACTION_BACKSCATTERED_ELECTRONS = "Backscattering coefficient"
FRACTION_TRANSMITTED_ELECTRONS = "Transmitted coefficient"
FRACTION_SKIRTED_ELECTRONS = "Skirted coefficient"

HDF5_ELECTRON_RESULTS = "ElectronResults"

class ElectronResults(BaseResults.BaseResults):
    def __init__(self):
        super(ElectronResults, self).__init__()

        self._values = {}

    def read(self):
        suffix = "_ElectronResults.dat"
        filename = self.basename + suffix
        filepath = os.path.join(self.path, filename)

        with open(filepath, 'r') as inputFile:
            lines = inputFile.readlines()

            for line in lines:
                items = line.split('=')
                if len(items) == 2:
                    for fieldName in self.fieldNames:
                        if fieldName in items[0]:
                            self._values[fieldName] = items[-1]

    def write_hdf5(self, hdf5_group):
        hdf5_group = hdf5_group.require_group(HDF5_ELECTRON_RESULTS)

        for field_name in self.fieldNames:
            hdf5_group.attrs[field_name] = self._values[field_name].strip()

    @property
    def fieldNames(self):
        fieldNames = []

        fieldNames.append(NUMBER_SIMULATED_ELECTRONS)
        fieldNames.append(NUMBER_INTERNAL_ELECTRONS)
        fieldNames.append(NUMBER_BACKSCATTERED_ELECTRONS)
        fieldNames.append(NUMBER_TRANSMITTED_ELECTRONS)
        fieldNames.append(NUMBER_SKIRTED_ELECTRONS)
        fieldNames.append(NUMBER_ELECTRON_COLLISIONS)
        fieldNames.append(FRACTION_INTERNAL_ELECTRONS)
        fieldNames.append(FRACTION_BACKSCATTERED_ELECTRONS)
        fieldNames.append(FRACTION_TRANSMITTED_ELECTRONS)
        fieldNames.append(FRACTION_SKIRTED_ELECTRONS)

        return fieldNames

    @property
    def numberSimulatedElectrons(self):
        return int(self._values[NUMBER_SIMULATED_ELECTRONS])
    @numberSimulatedElectrons.setter
    def numberSimulatedElectrons(self, numberSimulatedElectrons):
        self._values[NUMBER_SIMULATED_ELECTRONS] = int(numberSimulatedElectrons)

    @property
    def numberInternalElectrons(self):
        return int(self._values[NUMBER_INTERNAL_ELECTRONS])
    @numberInternalElectrons.setter
    def numberInternalElectrons(self, numberInternalElectrons):
        self._values[NUMBER_INTERNAL_ELECTRONS] = int(numberInternalElectrons)

    @property
    def numberBackscatteredElectrons(self):
        return int(self._values[NUMBER_BACKSCATTERED_ELECTRONS])
    @numberBackscatteredElectrons.setter
    def numberBackscatteredElectrons(self, numberBackscatteredElectrons):
        self._values[NUMBER_BACKSCATTERED_ELECTRONS] = int(numberBackscatteredElectrons)

    @property
    def numberTransmittedElectrons(self):
        return int(self._values[NUMBER_TRANSMITTED_ELECTRONS])
    @numberTransmittedElectrons.setter
    def numberTransmittedElectrons(self, numberTransmittedElectrons):
        self._values[NUMBER_TRANSMITTED_ELECTRONS] = int(numberTransmittedElectrons)

    @property
    def numberSkirtedElectrons(self):
        return int(self._values[NUMBER_SKIRTED_ELECTRONS])
    @numberSkirtedElectrons.setter
    def numberSkirtedElectrons(self, numberSkirtedElectrons):
        self._values[NUMBER_SKIRTED_ELECTRONS] = int(numberSkirtedElectrons)

    @property
    def numberElectronCollisions(self):
        return int(self._values[NUMBER_ELECTRON_COLLISIONS])
    @numberElectronCollisions.setter
    def numberElectronCollisions(self, numberElectronCollisions):
        self._values[NUMBER_ELECTRON_COLLISIONS] = int(numberElectronCollisions)

    @property
    def fractionInternalElectrons(self):
        return float(self._values[FRACTION_INTERNAL_ELECTRONS])
    @fractionInternalElectrons.setter
    def fractionInternalElectrons(self, fractionInternalElectrons):
        self._values[FRACTION_INTERNAL_ELECTRONS] = float(fractionInternalElectrons)

    @property
    def fractionBackscatteredElectrons(self):
        return float(self._values[FRACTION_BACKSCATTERED_ELECTRONS])
    @fractionBackscatteredElectrons.setter
    def fractionBackscatteredElectrons(self, fractionBackscatteredElectrons):
        self._values[FRACTION_BACKSCATTERED_ELECTRONS] = float(fractionBackscatteredElectrons)

    @property
    def fractionTransmittedElectrons(self):
        return float(self._values[FRACTION_TRANSMITTED_ELECTRONS])
    @fractionTransmittedElectrons.setter
    def fractionTransmittedElectrons(self, fractionTransmittedElectrons):
        self._values[FRACTION_TRANSMITTED_ELECTRONS] = float(fractionTransmittedElectrons)

    @property
    def fractionSkirtedElectrons(self):
        return float(self._values[FRACTION_SKIRTED_ELECTRONS])
    @fractionSkirtedElectrons.setter
    def fractionSkirtedElectrons(self, fractionSkirtedElectrons):
        self._values[FRACTION_SKIRTED_ELECTRONS] = float(fractionSkirtedElectrons)
