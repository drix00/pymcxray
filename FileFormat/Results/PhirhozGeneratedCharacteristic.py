#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.PhirhozGeneratedCharacteristic
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Read PhirhozGeneratedCharacteristic file from MCXRay program.
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
FIELD_DEPTH_A = "Depth (A)"

class PhirhozGeneratedCharacteristic(BaseResults.BaseResults):
    def __init__(self):
        super(PhirhozGeneratedCharacteristic, self).__init__()

        self.fieldNames = []
        self.depth_A = []
        self.phirhozs = {}

    def read(self, regionID=0):
        suffix = "_PhirhozGeneratedCharacteristic_Region%i.csv" % (regionID)
        filename = self.basename + suffix
        filepath = os.path.join(self.path, filename)

        with open(filepath, 'rb') as csvFile:
            reader = csv.DictReader(csvFile)

            fieldnames = reader.fieldnames
            assert fieldnames[0] == FIELD_DEPTH_A
            self.fieldNames = fieldnames

            for row in reader:
                self.depth_A.append(float(row[FIELD_DEPTH_A]))

                for elementSymbolLine in self.fieldNames[1:]:
                    symbol, xrayLine = elementSymbolLine.split()
                    self.phirhozs.setdefault((symbol.strip(), xrayLine.strip()), []).append(float(row[elementSymbolLine]))

    @property
    def fieldNames(self):
        return self._fieldNames
    @fieldNames.setter
    def fieldNames(self, fieldNames):
        self._fieldNames = fieldNames

    @property
    def depth_A(self):
        return self._depth_A
    @depth_A.setter
    def depth_A(self, depth_A):
        self._depth_A = depth_A

    @property
    def phirhozs(self):
        return self._phirhozs
    @phirhozs.setter
    def phirhozs(self, phirhozs):
        self._phirhozs = phirhozs

if __name__ == '__main__': #pragma: no cover
    import DrixUtilities.Runner as Runner
    Runner.Runner().run(runFunction=None)
