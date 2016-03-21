#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.ResultsParameters
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

MCXRay ResultsParameters input file.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2012 Hendrix Demers"
__license__ = ""

# Standard library modules.
import copy

# Third party modules.

# Local modules.

# Project modules
import pymcxray.FileFormat.Version as Version

# Globals and constants variables.
KEY_COMPUTE_XRAY_CHARACTERISTIC = "ComputeXrayCharacteristic"
KEY_COMPUTE_XRAY_BREMSSTRAHLUNG = "ComputeXrayBremsstrahlung"
KEY_COMPUTE_XRAY_PHIRHOZ = "ComputeXrayPhirhoz"
KEY_COMPUTE_XRAY_SIMULATED_SPECTRUM = "ComputeXraySimulatedSpectrum"

class ResultsParameters(object):
    def __init__(self):
        self.version = copy.deepcopy(Version.CURRENT_VERSION)

        self._keys = self._createKeys()

        self._parameters = {}

        self.defaultValues()

    def _createKeys(self):
        keys = []

        keys.append(KEY_COMPUTE_XRAY_CHARACTERISTIC)
        keys.append(KEY_COMPUTE_XRAY_BREMSSTRAHLUNG)
        keys.append(KEY_COMPUTE_XRAY_PHIRHOZ)
        keys.append(KEY_COMPUTE_XRAY_SIMULATED_SPECTRUM)

        return keys

    def defaultValues(self):
        self.isComputeXrayCharacteristic = True
        self.isComputeXrayBremsstrahlung = True
        self.isComputeXrayPhirhoz = True
        self.isComputeXraySimulatedSpectrum = False

    def _createExtractMethod(self):
        extractMethods = {}

        extractMethods[KEY_COMPUTE_XRAY_CHARACTERISTIC] = self._extractBool
        extractMethods[KEY_COMPUTE_XRAY_BREMSSTRAHLUNG] = self._extractBool
        extractMethods[KEY_COMPUTE_XRAY_PHIRHOZ] = self._extractBool
        extractMethods[KEY_COMPUTE_XRAY_SIMULATED_SPECTRUM] = self._extractBool

        return extractMethods

    def _extractBool(self, itemStr):
        return bool(int(itemStr))

    def read(self, filepath):
        self.version.readFromFile(filepath)

        lines = open(filepath, 'r').readlines()

        extractMethods = self._createExtractMethod()

        for line in lines:
            line = line.strip()

            for key in self._keys:
                if line.startswith(key):
                    items = line.split('=')
                    self._parameters[key] = extractMethods[key](items[-1])

    def write(self, filepath):
        outputFile = open(filepath, 'w')

        self._writeHeader(outputFile)

        self.version.writeLine(outputFile)

        keys = self._createKeys()
        if self.version < Version.VERSION_1_4_3:
            keys.remove(KEY_COMPUTE_XRAY_SIMULATED_SPECTRUM)

        for key in keys:
            value = self._parameters[key]
            if value is not None:
                line = "%s=%i\n" % (key, int(value))
                outputFile.write(line)

    def _writeHeader(self, outputFile):
        headerLines = [ "********************************************************************************",
                       "***                           Results Parameters",
                       "***",
                       "***",
                       "********************************************************************************"]


        for line in headerLines:
            outputFile.write(line+'\n')

    @property
    def version(self):
        return self._version
    @version.setter
    def version(self, version):
        self._version = version

    @property
    def isComputeXrayCharacteristic(self):
        return bool(self._parameters[KEY_COMPUTE_XRAY_CHARACTERISTIC])
    @isComputeXrayCharacteristic.setter
    def isComputeXrayCharacteristic(self, isComputeXrayCharacteristic):
        self._parameters[KEY_COMPUTE_XRAY_CHARACTERISTIC] = bool(isComputeXrayCharacteristic)

    @property
    def isComputeXrayBremsstrahlung(self):
        return bool(self._parameters[KEY_COMPUTE_XRAY_BREMSSTRAHLUNG])
    @isComputeXrayBremsstrahlung.setter
    def isComputeXrayBremsstrahlung(self, isComputeXrayBremsstrahlung):
        self._parameters[KEY_COMPUTE_XRAY_BREMSSTRAHLUNG] = bool(isComputeXrayBremsstrahlung)

    @property
    def isComputeXrayPhirhoz(self):
        return bool(self._parameters[KEY_COMPUTE_XRAY_PHIRHOZ])
    @isComputeXrayPhirhoz.setter
    def isComputeXrayPhirhoz(self, isComputeXrayPhirhoz):
        self._parameters[KEY_COMPUTE_XRAY_PHIRHOZ] = bool(isComputeXrayPhirhoz)

    @property
    def isComputeXraySimulatedSpectrum(self):
        return bool(self._parameters[KEY_COMPUTE_XRAY_SIMULATED_SPECTRUM])
    @isComputeXraySimulatedSpectrum.setter
    def isComputeXraySimulatedSpectrum(self, isComputeXraySimulatedSpectrum):
        self._parameters[KEY_COMPUTE_XRAY_SIMULATED_SPECTRUM] = bool(isComputeXraySimulatedSpectrum)
