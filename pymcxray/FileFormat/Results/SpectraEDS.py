#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.SpectraEDS
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Read MCXRay spectra EDS results file.
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
import pymcxray.FileFormat.Results.SpectrumEDS as SpectrumEDS
import pymcxray.FileFormat.Results.MicroscopeParameters as MicroscopeParameters

# Globals and constants variables.
TEST_INPUT_SECTION_START = "TEST INPUT - START"
TEST_INPUT_SECTION_STOP = "TEST INPUT - STOP"
PARTIAL_SPECTRA_REFERENCE_SECTION_START = "PARTIAL SPECTRA REFERENCE - START"
PARTIAL_SPECTRA_REFERENCE_SECTION_STOP = "PARTIAL SPECTRA REFERENCE - STOP"
PARTIAL_SPECTRA_REFERENCE_SECTION_ORIGINAL = "Original:"
PARTIAL_SPECTRA_REFERENCE_SECTION_ORIGINAL_1024 = "Original dans 1024:"
PARTIAL_SPECTRA_REFERENCE_SECTION_INTERPOLATED = "Interpolated:"

REGION_SPECTRA_SECTION_START = "Region ID"
KEY_REGION_ID = REGION_SPECTRA_SECTION_START
KEY_NUMBER_ELEMENTS = "Number of elements in region"
KEY_ELEMENT_WEIGHT_FRACTION = "Weight fraction of"
KEY_ELEMENTS = "elements"

KEY_CHARACTERISTIC_PROBABILITY = "Characteristic probability (P_Net)"
KEY_NUMBER_SIMULATED_PHOTONS = "Number of simulated photon in region"
KEY_NUMBER_CHARACTERISTIC_PEAKS = "Number of characteristic peaks in region"

SECTION_ICC_FROM_XRAY_SPECTRA = "ICC From X-Ray Spectra"
SECTION_ICC_FROM_ELECTRON_TRAJECTORIES = "ICC From Electron Trajectories"
SECTION_EIDEAL_EDETECTED_RATIO  = "Eideal Edetected Ratio"

SECTION_I_OUT_CHANNEL = "I_Out[channel]"
SECTION_E_NET_PEAK_CHANNEL = "E_Net[peak][channel]"

SECTION_P_CHARACTERISTIC_CHAR = "P_I (char)"
SECTION_P_BACKGROUND = "P_B (cont)"
SECTION_CONTINUUM_CUMULATIVE_EQUIPROBABLE_CHANNELS = "P_B_pm_avg (cont)"

class SpectraEDS(object):
    def __init__(self):
        self._parameters = {}

    def readFilepath(self, filepath):
        inputFile = open(filepath, 'r')

        self.readFileObject(inputFile)

    def readFileObject(self, inputFile):
        lineIndex = 0
        lines = inputFile.readlines()
        lines =[line.strip() for line in lines]

        if self._isTestInputSection(lines):
            lineIndex += self.readTestInputSection(lines)

        if self._isPartialSpectraReferenceSection(lines):
            lineIndex += self.readPartialSpectraReferenceSection(lines)

        if self._isRegionSpectraSection(lines):
            lineIndex += self.readRegionSpectraSection(lines[lineIndex:])

    def _isTestInputSection(self, lines):
        return self._isSection(lines, TEST_INPUT_SECTION_START, TEST_INPUT_SECTION_STOP)

    def _isPartialSpectraReferenceSection(self, lines):
        return self._isSection(lines, PARTIAL_SPECTRA_REFERENCE_SECTION_START, PARTIAL_SPECTRA_REFERENCE_SECTION_STOP)

    def _isRegionSpectraSection(self, lines):
        for line in lines:
            if line.startswith(REGION_SPECTRA_SECTION_START):
                return True
        else:
            return False

    def _isSection(self, lines, lineStart, lineStop):
        if lineStart in lines and lineStop in lines:
            return True
        else:
            return False

    def readTestInputSection(self, lines):
        raise NotImplementedError()

    def readPartialSpectraReferenceSection(self, lines):
        indexLineStart = lines.index(PARTIAL_SPECTRA_REFERENCE_SECTION_ORIGINAL)
        indexLineStop = lines.index(PARTIAL_SPECTRA_REFERENCE_SECTION_ORIGINAL_1024)
        self.originalSpectrumEDS = SpectrumEDS.SpectrumEDS(lines[indexLineStart+1:indexLineStop])

        indexLineStart = lines.index(PARTIAL_SPECTRA_REFERENCE_SECTION_ORIGINAL_1024)
        indexLineStop = lines.index(PARTIAL_SPECTRA_REFERENCE_SECTION_INTERPOLATED)
        self.original1024SpectrumEDS = SpectrumEDS.SpectrumEDS(lines[indexLineStart+1:indexLineStop])

        indexLineStart = lines.index(PARTIAL_SPECTRA_REFERENCE_SECTION_INTERPOLATED)
        indexLineStop = lines.index(PARTIAL_SPECTRA_REFERENCE_SECTION_STOP)
        self.interpolatedSpectrumEDS = SpectrumEDS.SpectrumEDS(lines[indexLineStart+1:indexLineStop])

        indexLine = lines.index(PARTIAL_SPECTRA_REFERENCE_SECTION_STOP)-1
        line = lines[indexLine]
        self.totalCountsOriginal, self.totalCountsInterpolated, self.totalCountsSynthetic = self._extractTotalCounts(line)

        indexLineStart = lines.index(PARTIAL_SPECTRA_REFERENCE_SECTION_START)
        indexLineStop = lines.index(PARTIAL_SPECTRA_REFERENCE_SECTION_STOP)
        return indexLineStop - indexLineStart

    def _extractTotalCounts(self, line):
        totalCountsOriginal = 0.0
        totalCountsInterpolated = 0.0
        totalCountsSynthetic = 0.0

        items = line.split(',')

        for item in items:
            key, value = item.split('=')
            key = key.strip()

            if key == "Counts original":
                totalCountsOriginal = float(value)
            elif key == "Counts original inter":
                totalCountsInterpolated = float(value)
            elif key == "Counts syn":
                totalCountsSynthetic = float(value)

        return totalCountsOriginal, totalCountsInterpolated, totalCountsSynthetic

    def readRegionSpectraSection(self, lines):
        indexLine = 0
        for line in lines:
            if line.startswith(REGION_SPECTRA_SECTION_START):
                break
            indexLine += 1
        else:
            raise ValueError()

        line = lines[indexLine]
        key, value = line.split('=')
        key = key.strip()
        self._parameters[key] = int(value)
        indexLine += 1

        line = lines[indexLine]
        key, value = line.split('=')
        key = key.strip()
        self._parameters[key] = int(value)
        indexLine += 1

        self._parameters[KEY_ELEMENTS] = {}
        for _index in range(self.numberElements):
            line = lines[indexLine]
            symbol, value = line.split('=')
            symbol = symbol.replace(KEY_ELEMENT_WEIGHT_FRACTION, '').strip()
            self._parameters[KEY_ELEMENTS][symbol] = float(value)
            indexLine += 1

        # Skip empty line
        indexLine += 1

        self.microscope = MicroscopeParameters.MicroscopeParameters()
        indexLine += self.microscope.readFromLines(lines[indexLine:])

        # Skip empty line
        indexLine += 1

        line = lines[indexLine]
        key, value = line.split('=')
        key = key.strip()
        self._parameters[key] = float(value)
        indexLine += 1

        line = lines[indexLine]
        key, value = line.split('=')
        key = key.strip()
        self._parameters[key] = int(value)
        indexLine += 1

        line = lines[indexLine]
        key, value = line.split('=')
        key = key.strip()
        self._parameters[key] = int(value)
        indexLine += 1

        # todo: extract values from lines.
        indexLine = lines.index(SECTION_ICC_FROM_XRAY_SPECTRA) + 1
        for line in lines[indexLine:]:
            line = line.strip()
            if line.startswith('Peak'):
                pass
            else:
                break

        # todo: extract values from lines.
        indexLine = lines.index(SECTION_ICC_FROM_ELECTRON_TRAJECTORIES) + 1
        for line in lines[indexLine:]:
            line = line.strip()
            if line.startswith('Peak'):
                pass
            else:
                break

        # todo: extract values from lines.
        indexLine = lines.index(SECTION_EIDEAL_EDETECTED_RATIO) + 1
        for line in lines[indexLine:]:
            line = line.strip()
            if line.startswith('Peak'):
                pass
            else:
                break

        self.iOutSpectrumEDS = SpectrumEDS.SpectrumEDS()
        indexLine = lines.index(SECTION_I_OUT_CHANNEL) + 1
        for line in lines[indexLine:]:
            line = line.strip()
            if line.startswith('Channel'):
                # Channel    0 [0.00000e+000 KeV] = 0.000000
                channelText, value = line.split('=')
                items = channelText.split()
                channel = int(items[1])
                energy_keV = float(items[2][1:])
                counts = float(value)

                self.iOutSpectrumEDS.channels.append(channel)
                self.iOutSpectrumEDS.enegies_keV.append(energy_keV)
                self.iOutSpectrumEDS.countsList.append(counts)
            else:
                break

        numberChannelEds = len(self.iOutSpectrumEDS.channels)

        self.eNetSpectrumEDS = {}
        for indexPeak in range(self.numberCharateristicPeaks):
            self.eNetSpectrumEDS[indexPeak] = SpectrumEDS.SpectrumEDS()
        indexLine = lines.index(SECTION_E_NET_PEAK_CHANNEL) + 1
        for line in lines[indexLine:]:
            line = line.strip()
            if line.startswith('Channel'):
                # Channel    0 [0.00000e+000 KeV]:   0.000e+000 0.000e+000 0.000e+000 0.000e+000 0.000e+000
                channelText, values = line.split(':')
                items = channelText.split()
                channel = int(items[1])
                energy_keV = float(items[2][1:])

                values = values.split()
                for indexPeak in range(len(values)):
                    counts = float(values[indexPeak])
                    self.eNetSpectrumEDS[indexPeak].channels.append(channel)
                    self.eNetSpectrumEDS[indexPeak].enegies_keV.append(energy_keV)
                    self.eNetSpectrumEDS[indexPeak].countsList.append(counts)
            else:
                break

        self.pCharacteristic = []
        numberLines = self.numberCharateristicPeaks
        sectionName = "%s(%i)" % (SECTION_P_CHARACTERISTIC_CHAR, numberLines)
        indexLine = lines.index(sectionName) + 1
        for line in lines[indexLine:indexLine+numberLines]:
            line = line.strip()
            key, value = line.split()
            self.pCharacteristic.append(float(value))

        self.pBackground = []
        numberLines = numberChannelEds
        sectionName = "%s(%i)" % (SECTION_P_BACKGROUND, numberLines)
        indexLine = lines.index(sectionName) + 1
        for line in lines[indexLine:indexLine+numberLines]:
            line = line.strip()
            key, value = line.split()
            self.pBackground.append(float(value))

        self.continuumCumulativeEquiprobableChannels = []
        numberLines = numberChannelEds
        sectionName = "%s(%i)" % (SECTION_CONTINUUM_CUMULATIVE_EQUIPROBABLE_CHANNELS, numberLines)
        indexLine = lines.index(sectionName) + 1
        for line in lines[indexLine:indexLine+numberLines]:
            line = line.strip()
            key, value = line.split()
            self.continuumCumulativeEquiprobableChannels.append(float(value))

        indexLine += numberLines

        return indexLine

    @property
    def regionID(self):
        return self._parameters[KEY_REGION_ID]
    @regionID.setter
    def regionID(self, regionID):
        self._parameters[KEY_REGION_ID] = regionID

    @property
    def numberElements(self):
        return self._parameters[KEY_NUMBER_ELEMENTS]
    @numberElements.setter
    def numberElements(self, numberElements):
        self._parameters[KEY_NUMBER_ELEMENTS] = numberElements

    @property
    def elements(self):
        return self._parameters[KEY_ELEMENTS]
    @elements.setter
    def elements(self, elements):
        self._parameters[KEY_ELEMENTS] = elements

    @property
    def characteristicProbability(self):
        return self._parameters[KEY_CHARACTERISTIC_PROBABILITY]
    @characteristicProbability.setter
    def characteristicProbability(self, characteristicProbability):
        self._parameters[KEY_CHARACTERISTIC_PROBABILITY] = characteristicProbability

    @property
    def numberSimulatedPhotons(self):
        return self._parameters[KEY_NUMBER_SIMULATED_PHOTONS]
    @numberSimulatedPhotons.setter
    def numberSimulatedPhotons(self, numberSimulatedPhotons):
        self._parameters[KEY_NUMBER_SIMULATED_PHOTONS] = numberSimulatedPhotons

    @property
    def numberCharateristicPeaks(self):
        return self._parameters[KEY_NUMBER_CHARACTERISTIC_PEAKS]
    @numberCharateristicPeaks.setter
    def numberCharateristicPeaks(self, numberCharateristicPeaks):
        self._parameters[KEY_NUMBER_CHARACTERISTIC_PEAKS] = numberCharateristicPeaks

def runExample():
    import os.path
    import matplotlib.pyplot as plt
    import logging

    testDataPath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../test_data"))

    _spectraEdsRegion1Filepath = os.path.join(testDataPath, "version1.1/autoSavedFiles/DetectionLimits_N1000x_C_r10A_z11A_Au_E30d0keVEDSRegion1.txt")

    spectraEDSregion0 = SpectraEDS()
    spectraEdsRegion0Filepath = os.path.join(testDataPath, "version1.1/autoSavedFiles/DetectionLimits_N1000x_C_r10A_z11A_Au_E30d0keVEDSRegion0.txt")
    spectraEDSregion0.readFilepath(spectraEdsRegion0Filepath)

    plt.figure()

    _x = spectraEDSregion0.originalSpectrumEDS.channels
    x = spectraEDSregion0.originalSpectrumEDS.enegies_keV
    y = spectraEDSregion0.originalSpectrumEDS.countsList
    plt.plot(x, y, label="Original")

    x = spectraEDSregion0.original1024SpectrumEDS.channels
    x = spectraEDSregion0.original1024SpectrumEDS.enegies_keV
    y = spectraEDSregion0.original1024SpectrumEDS.countsList
    plt.plot(x, y, label="Original1024")

    x = spectraEDSregion0.interpolatedSpectrumEDS.channels
    x = spectraEDSregion0.interpolatedSpectrumEDS.enegies_keV
    y = spectraEDSregion0.interpolatedSpectrumEDS.countsList
    plt.plot(x, y, label="Interpolated")

    plt.legend(loc='best')

    logging.info("Total counts original    : %i", spectraEDSregion0.totalCountsOriginal)
    logging.info("Total counts interpolated: %i", spectraEDSregion0.totalCountsInterpolated)
    logging.info("Total counts synthetic   : %i", spectraEDSregion0.totalCountsSynthetic)

    plt.figure()

    x = spectraEDSregion0.iOutSpectrumEDS.channels
    x = spectraEDSregion0.iOutSpectrumEDS.enegies_keV
    y = spectraEDSregion0.iOutSpectrumEDS.countsList
    plt.plot(x, y, label="i out")

    for indexPeak in spectraEDSregion0.eNetSpectrumEDS:
        x = spectraEDSregion0.eNetSpectrumEDS[indexPeak].channels
        x = spectraEDSregion0.eNetSpectrumEDS[indexPeak].enegies_keV
        y = spectraEDSregion0.eNetSpectrumEDS[indexPeak].countsList
        label = str(indexPeak)
        plt.plot(x, y, label=label)

    plt.legend(loc='best')


    plt.figure()

    x = range(len(spectraEDSregion0.pCharacteristic))
    y = spectraEDSregion0.pCharacteristic
    plt.plot(x, y, label="p Char")

    x = range(len(spectraEDSregion0.pBackground))
    y = spectraEDSregion0.pBackground
    plt.plot(x, y, label="p Back")

    x = range(len(spectraEDSregion0.continuumCumulativeEquiprobableChannels))
    y = spectraEDSregion0.continuumCumulativeEquiprobableChannels
    plt.plot(x, y, label="p Back Equi")

    plt.legend()

    plt.show()

if __name__ == '__main__': #pragma: no cover
    runExample()
