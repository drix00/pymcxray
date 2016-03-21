#!/usr/bin/env python
"""
.. py:currentmodule:: DebugSimulatedSpectrum
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Debug the simulated spectrum implementation in mcxray.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2012 Hendrix Demers"
__license__ = ""

# Standard library modules.

# Third party modules.
import matplotlib.pyplot as plt

# Local modules.

# Project modules
import pymcxray.FileFormat.Results.XraySpectraSpecimen as XraySpectraSpecimen
import pymcxray.FileFormat.Results.XraySimulatedSpectraSpecimen as XraySimulatedSpectraSpecimen
import pymcxray.FileFormat.Results.XraySimulatedSpectraRegion as XraySimulatedSpectraRegion

# Globals and constants variables.

class DebugSimulatedSpectrum(object):
    def __init__(self):
        self._resultsPath = r"J:\hdemers\work\codings\MCXRay\mcxray-110218-hd\Dev\bin\Results"
        self._basename = "testC_10e_10kp"

    def runSpecimen(self):
        spectraSpecimen = XraySpectraSpecimen.XraySpectraSpecimen()
        spectraSpecimen.path = self._resultsPath
        spectraSpecimen.basename = self._basename
        spectraSpecimen.read()

        simulatedSpectraSpecimen = XraySimulatedSpectraSpecimen.XraySimulatedSpectraSpecimen()
        simulatedSpectraSpecimen.path = self._resultsPath
        simulatedSpectraSpecimen.basename = self._basename
        simulatedSpectraSpecimen.read()

        plt.figure()

        plt.semilogy(spectraSpecimen.energies_keV, spectraSpecimen.totals, label="Synthetic")
        plt.semilogy(simulatedSpectraSpecimen.energies_keV, simulatedSpectraSpecimen.totals, label="Simulated Specimen")

        plt.legend(loc='best')

    def runRegion(self):
        simulatedSpectraRegion = XraySimulatedSpectraRegion.XraySimulatedSpectraRegion()
        simulatedSpectraRegion.path = self._resultsPath
        simulatedSpectraRegion.basename = self._basename
        simulatedSpectraRegion.read()

        plt.figure()

        plt.semilogy(simulatedSpectraRegion.energies_keV, simulatedSpectraRegion.simulatedIntensities, label="Simulated")
        plt.semilogy(simulatedSpectraRegion.energies_keV, simulatedSpectraRegion.detectedIntensities, label="Detected")

        plt.legend(loc='best')

        plt.figure()

        plt.semilogy(simulatedSpectraRegion.channelNumbers, simulatedSpectraRegion.energiesReference_keV, label="Reference")
        plt.semilogy(simulatedSpectraRegion.channelNumbers, simulatedSpectraRegion.energies_keV, label="Simulated")

        plt.legend(loc='best')

        plt.figure()

        for peakNumber in simulatedSpectraRegion.eNetPeak:
            plt.semilogy(simulatedSpectraRegion.channelNumbers, simulatedSpectraRegion.eNetPeak[peakNumber], label=peakNumber)

        plt.legend(loc='best')

        plt.figure()

        plt.semilogy(simulatedSpectraRegion.energies_keV, simulatedSpectraRegion.peakToBackgrpound, label="P/B")
        plt.semilogy(simulatedSpectraRegion.energies_keV, simulatedSpectraRegion.peakToBackgrpoundAverage, label="P/B average")

        plt.legend(loc='best')

def run():
    debug = DebugSimulatedSpectrum()
    debug.runSpecimen()
    debug.runRegion()

    plt.show()

if __name__ == '__main__': #pragma: no cover
    run()
