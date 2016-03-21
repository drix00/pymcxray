#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.PhirhozGenerated
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

MCXRay phirhoz generated result file.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2012 Hendrix Demers"
__license__ = ""

# Subversion informations for the file.
__svnRevision__ = "$Revision$"
__svnDate__ = "$Date$"
__svnId__ = "$Id$"

# Standard library modules.

# Third party modules.

# Local modules.

# Project modules
import pymcxray.FileFormat.Results.ModelParameters as ModelParameters
import pymcxray.FileFormat.Results.SimulationParameters as SimulationParameters
import pymcxray.FileFormat.Results.MicroscopeParameters as MicroscopeParameters
import pymcxray.FileFormat.Results.ElectronParameters as ElectronParameters
import pymcxray.FileFormat.Results.PhirhozRegion as PhirhozRegion

# Globals and constants variables.

KEY_PHIRHOZ_GENERATED = "phirhozGenerated"

KEY_NUMBER_REGIONS = "Number of Regions"

KEY_PHIRHOZ_CHARACTERISTIC = "Characteristic"

class PhirhozGenerated(object):
    def __init__(self):
        self._parameters = {}

    def read(self, filepath):
        lines = open(filepath, 'r').readlines()

        lineIndex = 0

        lineIndex += self.readSolidSimulationModels(lines[lineIndex:])
        lineIndex += self.readSimulationParameters(lines[lineIndex:])
        lineIndex += self.readMicroscope(lines[lineIndex:])
        lineIndex += self.readElectron(lines[lineIndex:])

        lineIndex += self.readRegions(lines[lineIndex:])

    def readSolidSimulationModels(self, lines):
        self.modelParameters = ModelParameters.ModelParameters()
        lineIndex = self.modelParameters.readFromLines(lines)

        return lineIndex

    def readSimulationParameters(self, lines):
        self.simulationParameters = SimulationParameters.SimulationParameters()
        lineIndex = self.simulationParameters.readFromLines(lines)

        return lineIndex

    def readMicroscope(self, lines):
        self.microscopeParameters = MicroscopeParameters.MicroscopeParameters()
        lineIndex = self.microscopeParameters.readFromLines(lines)

        return lineIndex

    def readElectron(self, lines):
        self.electronParameters = ElectronParameters.ElectronParameters()
        lineIndex = self.electronParameters.readFromLines(lines)

        return lineIndex

    def readRegions(self, lines):
        indexLine = 0
        for line in lines:
            indexLine += 1
            if line.strip().startswith(KEY_NUMBER_REGIONS):
                indexNumberRegions = len(KEY_NUMBER_REGIONS)
                self.numberRegions = int(line[indexNumberRegions:])
                break
        else:
            message = "Cannot find the section header in the liens: %s" % (KEY_NUMBER_REGIONS)
            raise ValueError(message)

        self._regions = {}

        for _indexRegion in range(self.numberRegions):
            region = PhirhozRegion.PhirhozRegion(self.simulationParameters.numberEnergyWindows, self.simulationParameters.numberLayersZ)
            indexLine += region.readFromLines(lines[indexLine:])

            self._regions[region.regionID] = region

        assert len(self._regions) == self.numberRegions

        return indexLine

    def getCharacteristicPhiRhoZ(self, regionID):
        return self._regions[regionID].characteristicPhirhoz

    @property
    def modelParameters(self):
        return self._parameters[ModelParameters.KEY_MODEL_PARAMETERS]
    @modelParameters.setter
    def modelParameters(self, modelParameters):
        self._parameters[ModelParameters.KEY_MODEL_PARAMETERS] = modelParameters

    @property
    def simulationParameters(self):
        return self._parameters[SimulationParameters.KEY_SIMULATION_PARAMETERS]
    @simulationParameters.setter
    def simulationParameters(self, simulationParameters):
        self._parameters[SimulationParameters.KEY_SIMULATION_PARAMETERS] = simulationParameters

    @property
    def microscopeParameters(self):
        return self._parameters[MicroscopeParameters.KEY_MICROSCOPE_PARAMETERS]
    @microscopeParameters.setter
    def microscopeParameters(self, microscopeParameters):
        self._parameters[MicroscopeParameters.KEY_MICROSCOPE_PARAMETERS] = microscopeParameters

    @property
    def electronParameters(self):
        return self._parameters[ElectronParameters.KEY_ELECTRON_PARAMETERS]
    @electronParameters.setter
    def electronParameters(self, electronParameters):
        self._parameters[ElectronParameters.KEY_ELECTRON_PARAMETERS] = electronParameters

    @property
    def numberRegions(self):
        return self._parameters[KEY_NUMBER_REGIONS]
    @numberRegions.setter
    def numberRegions(self, numberRegions):
        self._parameters[KEY_NUMBER_REGIONS] = numberRegions
