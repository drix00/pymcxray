#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.XraySimulatedSpectraRegion
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

description
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
CHANNEL_NUMBER = "Channel index"
ENERGIES_REFERENCE_keV = "Channel reference energy (keV)"
ENERGIES_SIMULATED_keV = "Channel synthetic energy (keV)"
SIMULATED_INTENSITY = "Simulated intensity"
DETECTED_INTENSITY = "Detected intensity"
E_NET_PEAK_I = "E_Net peak %i"
PEAK_TO_BACKGROUND = "P_B (continuum)"
PEAK_TO_BACKGROUND_AVERAGE ="P_B_pm_avg (continuum)"

class XraySimulatedSpectraRegion(BaseResults.BaseResults):
    def __init__(self):
        super(XraySimulatedSpectraRegion, self).__init__()

        self.channelNumbers = []
        self.energiesReference_keV = []
        self.energies_keV = []
        self.simulatedIntensities = []
        self.detectedIntensities = []
        self.eNetPeak = {}
        self.peakToBackgrpound = []
        self.peakToBackgrpoundAverage = []

    def read(self, regionID=0):
        suffix = "_SimulatedSpectraRegion_%i.csv" % (regionID)
        filename = self.basename + suffix
        filepath = os.path.join(self.path, filename)

        with open(filepath, 'r') as csvFile:
            reader = csv.DictReader(csvFile)
            _fieldNames = reader.fieldnames

            # Skip header row

            for row in reader:
                self.channelNumbers.append(float(row[CHANNEL_NUMBER]))
                self.energiesReference_keV.append(float(row[ENERGIES_REFERENCE_keV]))
                self.energies_keV.append(float(row[ENERGIES_SIMULATED_keV]))
                self.simulatedIntensities.append(float(row[SIMULATED_INTENSITY]))
                self.detectedIntensities.append(float(row[DETECTED_INTENSITY]))

                indexPeak = 0
                key = E_NET_PEAK_I % (indexPeak)
                while key in row.keys():
                    self.eNetPeak.setdefault(indexPeak, []).append(float(row[key]))
                    indexPeak += 1
                    key = E_NET_PEAK_I % (indexPeak)

                self.peakToBackgrpound.append(float(row[PEAK_TO_BACKGROUND]))
                self.peakToBackgrpoundAverage.append(float(row[PEAK_TO_BACKGROUND_AVERAGE]))

    @property
    def fieldNames(self):
        fieldNames = []
        fieldNames.append(SIMULATED_INTENSITY)
        fieldNames.append(DETECTED_INTENSITY)

        return fieldNames

    @property
    def channelNumbers(self):
        return self._channelNumbers
    @channelNumbers.setter
    def channelNumbers(self, channelNumbers):
        self._channelNumbers = channelNumbers

    @property
    def energiesReference_keV(self):
        return self._energiesReference_keV
    @energiesReference_keV.setter
    def energiesReference_keV(self, energiesReference_keV):
        self._energiesReference_keV = energiesReference_keV

    @property
    def energies_keV(self):
        return self._energies_keV
    @energies_keV.setter
    def energies_keV(self, energies_keV):
        self._energies_keV = energies_keV

    @property
    def simulatedIntensities(self):
        return self._simulatedIntensities
    @simulatedIntensities.setter
    def simulatedIntensities(self, simulatedIntensities):
        self._simulatedIntensities = simulatedIntensities

    @property
    def detectedIntensities(self):
        return self._detectedIntensities
    @detectedIntensities.setter
    def detectedIntensities(self, detectedIntensities):
        self._detectedIntensities = detectedIntensities

    @property
    def eNetPeak(self):
        return self._eNetPeak
    @eNetPeak.setter
    def eNetPeak(self, eNetPeak):
        self._eNetPeak = eNetPeak

    @property
    def peakToBackgrpound(self):
        return self._peakToBackgrpound
    @peakToBackgrpound.setter
    def peakToBackgrpound(self, peakToBackgrpound):
        self._peakToBackgrpound = peakToBackgrpound

    @property
    def peakToBackgrpoundAverage(self):
        return self._peakToBackgrpoundAverage
    @peakToBackgrpoundAverage.setter
    def peakToBackgrpoundAverage(self, peakToBackgrpoundAverage):
        self._peakToBackgrpoundAverage = peakToBackgrpoundAverage
