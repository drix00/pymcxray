#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.PhirhozEmittedCharacteristic
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Read PhirhozEmittedCharacteristic file from MCXRay.
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

HDF5_PHIRHOZ_EMITTED_CHARACTERISTIC = "PhirhozEmittedCharacteristic"
HDF5_DEPTH_nm = "Depth (nm)"

class PhirhozEmittedCharacteristic(BaseResults.BaseResults):
    def __init__(self):
        super(PhirhozEmittedCharacteristic, self).__init__()

        self.fieldNames = []
        self.depth_A = []
        self.phirhozs = {}

    def read(self, regionID=0):
        suffix = "_PhirhozEmittedCharacteristic_Region%i.csv" % (regionID)
        filename = self.basename + suffix
        filepath = os.path.join(self.path, filename)

        with open(filepath, 'r') as csvFile:
            reader = csv.DictReader(csvFile)

            fieldnames = reader.fieldnames
            assert fieldnames[0] == FIELD_DEPTH_A
            self.fieldNames = fieldnames

            for row in reader:
                self.depth_A.append(float(row[FIELD_DEPTH_A]))

                for elementSymbolLine in self.fieldNames[1:]:
                    symbol, _line, xrayLine = elementSymbolLine.split()
                    self.phirhozs.setdefault((symbol.strip(), xrayLine.strip()), []).append(float(row[elementSymbolLine]))

    def write_hdf5(self, hdf5_group):
        hdf5_group = hdf5_group.require_group(HDF5_PHIRHOZ_EMITTED_CHARACTERISTIC)
        
        hdf5_group.create_dataset(HDF5_DEPTH_nm, data=self.depth_nm)
        
        for phirhoz_name in self.phirhozs:
            symbol, xray_line = phirhoz_name
            group = hdf5_group.require_group(symbol)
            group.create_dataset(xray_line, data=self.phirhozs[phirhoz_name])
            
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
    def depth_nm(self):
        depths_nm = [depth_A*0.1 for depth_A in self._depth_A]
        return depths_nm

    @property
    def phirhozs(self):
        return self._phirhozs
    @phirhozs.setter
    def phirhozs(self, phirhozs):
        self._phirhozs = phirhozs
