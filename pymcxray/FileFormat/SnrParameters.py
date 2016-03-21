#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Snr
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

MCXRay Snr input file.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2012 Hendrix Demers"
__license__ = ""

# Standard library modules.

# Third party modules.

# Local modules.

# Project modules

# Globals and constants variables.
SNR_SPECTRA_TYPE_FULL = 0
SNR_SPECTRA_TYPE_EDS = 1
SNR_SPECTRA_TYPE_NBR = 2

KEY_SNR_TYPE = "SNRType"
KEY_ENERGY_START_keV = "EnergyStart"
KEY_ENERGY_END_keV = "EnergyEnd"
KEY_NUMBER_ENERGY_STEPS = "EnergyStepNbr"
KEY_BACKGROUND_ENERGY_WINDOWS_SIZE = "BackEnergyWinSiz"
KEY_SPECTRUM_ENERGY_WINDOWS_SIZE = "SpectraEnergyWinSiz"

class SnrParameters(object):
    def __init__(self):
        self._keys = self._createKeys()

        self._parameters = {}

        self.defaultValues()

    def _createKeys(self):
        keys = []

        keys.append(KEY_SNR_TYPE)
        keys.append(KEY_ENERGY_START_keV)
        keys.append(KEY_ENERGY_END_keV)
        keys.append(KEY_NUMBER_ENERGY_STEPS)
        keys.append(KEY_BACKGROUND_ENERGY_WINDOWS_SIZE)
        keys.append(KEY_SPECTRUM_ENERGY_WINDOWS_SIZE)

        return keys

    def defaultValues(self):
        self.snrType = SNR_SPECTRA_TYPE_FULL
        self.energyStart_keV = 1.0
        self.energyEnd_keV = 20.0
        self.numberEnergySteps = 100.0
        self.backgroundEnergyWindowsSize = 5.0e-3
        self.spectrumEnergyWindowsSize = 40.0

    def _createExtractMethod(self):
        extractMethods = {}

        extractMethods[KEY_SNR_TYPE] = int
        extractMethods[KEY_ENERGY_START_keV] = float
        extractMethods[KEY_ENERGY_END_keV] = float
        extractMethods[KEY_NUMBER_ENERGY_STEPS] = int
        extractMethods[KEY_BACKGROUND_ENERGY_WINDOWS_SIZE] = float
        extractMethods[KEY_SPECTRUM_ENERGY_WINDOWS_SIZE] = float

        return extractMethods

    def read(self, filepath):
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

        formats = self._createFormats()

        for key in self._createKeys():
            valueFormat = formats[key]
            value = valueFormat % (self._parameters[key])
            if "e-" in value:
                value = value.replace('e-', 'e-0')
            if "e+" in value:
                value = value.replace('e+', 'e+0')

            line = "%s=%s\n" % (key, value)
            outputFile.write(line)

    def _writeHeader(self, outputFile):
        headerLines = ["********************************************************************************",
                       "***                       SNR SIMULATION PARAMETERS",
                       "***",
                       "***    SNRType             = Type of SNR computations performed",
                       "***    EnergyStart         = Starting energy value",
                       "***    EnergyEnd           = Ending energy value",
                       "***    EnergyStepNbr       = Energy number of step",
                       "***    BackEnergyWinSiz    = Size of background energy windows",
                       "***    SpectraEnergyWinSiz = Size of spectra energy window",
                       "***",
                       "********************************************************************************"]

        for line in headerLines:
            outputFile.write(line+'\n')

    def _createFormats(self):
        formats = {}

        formats[KEY_SNR_TYPE] = "%i"
        formats[KEY_ENERGY_START_keV] = "%.6e"
        formats[KEY_ENERGY_END_keV] = "%.6e"
        formats[KEY_NUMBER_ENERGY_STEPS] = "%i"
        formats[KEY_BACKGROUND_ENERGY_WINDOWS_SIZE] = "%.6e"
        formats[KEY_SPECTRUM_ENERGY_WINDOWS_SIZE] = "%.6e"

        return formats

    @property
    def snrType(self):
        return self._parameters[KEY_SNR_TYPE]
    @snrType.setter
    def snrType(self, snrType):
        self._parameters[KEY_SNR_TYPE] = snrType

    @property
    def energyStart_keV(self):
        return self._parameters[KEY_ENERGY_START_keV]
    @energyStart_keV.setter
    def energyStart_keV(self, energyStart_keV):
        self._parameters[KEY_ENERGY_START_keV] = energyStart_keV

    @property
    def energyEnd_keV(self):
        return self._parameters[KEY_ENERGY_END_keV]
    @energyEnd_keV.setter
    def energyEnd_keV(self, energyEnd_keV):
        self._parameters[KEY_ENERGY_END_keV] = energyEnd_keV

    @property
    def numberEnergySteps(self):
        return self._parameters[KEY_NUMBER_ENERGY_STEPS]
    @numberEnergySteps.setter
    def numberEnergySteps(self, numberEnergySteps):
        self._parameters[KEY_NUMBER_ENERGY_STEPS] = numberEnergySteps

    @property
    def backgroundEnergyWindowsSize(self):
        return self._parameters[KEY_BACKGROUND_ENERGY_WINDOWS_SIZE]
    @backgroundEnergyWindowsSize.setter
    def backgroundEnergyWindowsSize(self, backgroundEnergyWindowsSize):
        self._parameters[KEY_BACKGROUND_ENERGY_WINDOWS_SIZE] = backgroundEnergyWindowsSize

    @property
    def spectrumEnergyWindowsSize(self):
        return self._parameters[KEY_SPECTRUM_ENERGY_WINDOWS_SIZE]
    @spectrumEnergyWindowsSize.setter
    def spectrumEnergyWindowsSize(self, spectrumEnergyWindowsSize):
        self._parameters[KEY_SPECTRUM_ENERGY_WINDOWS_SIZE] = spectrumEnergyWindowsSize
