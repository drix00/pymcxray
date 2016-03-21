#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.SimulationParameters
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

MCXRay simulation parameters results file.
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

# Globals and constants variables.
KEY_SIMULATION_PARAMETERS = "Simulation Parameters"
KEY_NUMBER_ELECTRONS = "Total simulated electrons"
KEY_NUMBER_PHOTONS = "Total simulated photons in EDS"
KEY_NUMBER_WINDOWS = "Number of energy windows"
KEY_NUMBER_FILMS_X = "Number of layers in PhiRoX"
KEY_NUMBER_FILMS_Y = "Number of layers in PhiRoY"
KEY_NUMBER_FILMS_Z = "Number of layers in PhiRoZ"
KEY_NUMBER_CHANNELS = "Number of channels in spectras"
KEY_SPECTRA_INTERPOLATION_MODEL = "Spectras interpolation type"
KEY_EDS_MAXIMUM_ENERGY_keV = "EDS spectras maximum energy"
KEY_GENERALIZED_WALK = "Generalized Walk"
KEY_USE_LIVE_TIME_s = "Use Live Time"
KEY_MAXIMUM_LIVE_TIME_s = "Live Time Max"

class SimulationParameters(object):
    def __init__(self):
        self._parameters = {}

    def _createKeys(self):
        keys = []

        keys.append(KEY_NUMBER_ELECTRONS)
        keys.append(KEY_NUMBER_PHOTONS)
        keys.append(KEY_NUMBER_WINDOWS)
        keys.append(KEY_NUMBER_FILMS_X)
        keys.append(KEY_NUMBER_FILMS_Y)
        keys.append(KEY_NUMBER_FILMS_Z)
        keys.append(KEY_NUMBER_CHANNELS)
        keys.append(KEY_SPECTRA_INTERPOLATION_MODEL)
        keys.append(KEY_EDS_MAXIMUM_ENERGY_keV)
        keys.append(KEY_GENERALIZED_WALK)
        keys.append(KEY_USE_LIVE_TIME_s)
        keys.append(KEY_MAXIMUM_LIVE_TIME_s)

        return keys

    def _createExtractMdethodList(self):
        extractMethodList = {}

        extractMethodList[KEY_NUMBER_ELECTRONS] = int
        extractMethodList[KEY_NUMBER_PHOTONS] = int
        extractMethodList[KEY_NUMBER_WINDOWS] = int
        extractMethodList[KEY_NUMBER_FILMS_X] = int
        extractMethodList[KEY_NUMBER_FILMS_Y] = int
        extractMethodList[KEY_NUMBER_FILMS_Z] = int
        extractMethodList[KEY_NUMBER_CHANNELS] = int
        extractMethodList[KEY_SPECTRA_INTERPOLATION_MODEL] = int
        extractMethodList[KEY_EDS_MAXIMUM_ENERGY_keV] = float
        extractMethodList[KEY_GENERALIZED_WALK] = int
        extractMethodList[KEY_USE_LIVE_TIME_s] = float
        extractMethodList[KEY_MAXIMUM_LIVE_TIME_s] = float

        return extractMethodList

    def readFromLines(self, lines):
        # Skip header line.
        indexLine = 0
        for line in lines:
            indexLine += 1
            if line.strip().startswith(KEY_SIMULATION_PARAMETERS):
                break
        else:
            message = "Cannot find the section header in the liens: %s" % (KEY_SIMULATION_PARAMETERS)
            raise ValueError(message)

        extractMethodList = self._createExtractMdethodList()
        for key in self._createKeys():
            line = lines[indexLine]
            indexLine += 1

            label, value = line.split('=')

            if label.strip() == key:
                self._parameters[key] = extractMethodList[key](value)

        return indexLine

    @property
    def numberElectrons(self):
        return self._parameters[KEY_NUMBER_ELECTRONS]
    @numberElectrons.setter
    def numberElectrons(self, numberElectrons):
        self._parameters[KEY_NUMBER_ELECTRONS] = numberElectrons

    @property
    def numberPhotons(self):
        return self._parameters[KEY_NUMBER_PHOTONS]
    @numberPhotons.setter
    def numberPhotons(self, numberPhotons):
        self._parameters[KEY_NUMBER_PHOTONS] = numberPhotons

    @property
    def numberEnergyWindows(self):
        return self._parameters[KEY_NUMBER_WINDOWS]
    @numberEnergyWindows.setter
    def numberEnergyWindows(self, numberEnergyWindows):
        self._parameters[KEY_NUMBER_WINDOWS] = numberEnergyWindows

    @property
    def numberLayersX(self):
        return self._parameters[KEY_NUMBER_FILMS_X]
    @numberLayersX.setter
    def numberLayersX(self, numberLayersX):
        self._parameters[KEY_NUMBER_FILMS_X] = numberLayersX

    @property
    def numberLayersY(self):
        return self._parameters[KEY_NUMBER_FILMS_Y]
    @numberLayersY.setter
    def numberLayersY(self, numberLayersY):
        self._parameters[KEY_NUMBER_FILMS_Y] = numberLayersY

    @property
    def numberLayersZ(self):
        return self._parameters[KEY_NUMBER_FILMS_Z]
    @numberLayersZ.setter
    def numberLayersZ(self, numberLayersZ):
        self._parameters[KEY_NUMBER_FILMS_Z] = numberLayersZ

    @property
    def numberChannels(self):
        return self._parameters[KEY_NUMBER_CHANNELS]
    @numberChannels.setter
    def numberChannels(self, numberChannels):
        self._parameters[KEY_NUMBER_CHANNELS] = numberChannels

    @property
    def interpolationType(self):
        return self._parameters[KEY_SPECTRA_INTERPOLATION_MODEL]
    @interpolationType.setter
    def interpolationType(self, interpolationType):
        self._parameters[KEY_SPECTRA_INTERPOLATION_MODEL] = interpolationType

    @property
    def edsMaximumEnergy_keV(self):
        return self._parameters[KEY_EDS_MAXIMUM_ENERGY_keV]
    @edsMaximumEnergy_keV.setter
    def edsMaximumEnergy_keV(self, edsMaximumEnergy_keV):
        self._parameters[KEY_EDS_MAXIMUM_ENERGY_keV] = edsMaximumEnergy_keV

    @property
    def generalizedWalk(self):
        return self._parameters[KEY_GENERALIZED_WALK]
    @generalizedWalk.setter
    def generalizedWalk(self, generalizedWalk):
        self._parameters[KEY_GENERALIZED_WALK] = generalizedWalk

    @property
    def useLiveTime_s(self):
        return self._parameters[KEY_USE_LIVE_TIME_s]
    @useLiveTime_s.setter
    def useLiveTime_s(self, useLiveTime_s):
        self._parameters[KEY_USE_LIVE_TIME_s] = useLiveTime_s

    @property
    def maximumLiveTime_s(self):
        return self._parameters[KEY_MAXIMUM_LIVE_TIME_s]
    @maximumLiveTime_s.setter
    def maximumLiveTime_s(self, maximumLiveTime_s):
        self._parameters[KEY_MAXIMUM_LIVE_TIME_s] = maximumLiveTime_s
