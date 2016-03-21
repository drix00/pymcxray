#!/usr/bin/env python
"""
.. py:currentmodule:: analyzeNumberBackgroundWindows
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Analyze the number of background windows on the x-ray spectrum.
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
import os.path

# Third party modules.
import matplotlib.pyplot as plt
import numpy as np

# Local modules.
import pymcxray.FileFormat.ExportedSpectrum as ExportedSpectrum

# Project modules

# Globals and constants variables.


class AnalyzeNumberBackgroundWindows(object):
    def __init__(self):
        self._dataPath = r"J:\hdemers\work\results\simulations\McXRay\TestNumberBackgroundWindows"

        self._results = {}

    def readData(self):
        numberWindowsList = [64, 128, 256, 512, 1024]

        for numberWindows in numberWindowsList:
            filename = "bulkC_E20keV_w%iBW.txt" % (numberWindows)
            filepath = os.path.join(self._dataPath, filename)

            exportedSpectrum = ExportedSpectrum.ExportedSpectrum()
            exportedSpectrum.read(filepath)
            results = exportedSpectrum.getData()
            self._results[numberWindows] = results

    def plotData(self):
        plt.figure()

        numberWindowsList = [64, 128, 256, 512, 1024]

        for numberWindows in numberWindowsList:
            x, y = self._results[numberWindows]
            y = np.array(y)
            y *= (20.0/numberWindows)

            label = "%i" % (numberWindows)
            plt.semilogy(x, y, label=label)

        plt.xlabel("Energy (keV)")
        plt.ylabel("Counts")
        plt.legend(loc='best')

    def plotDifference(self):
        pass

def run():
    analyze = AnalyzeNumberBackgroundWindows()

    analyze.readData()
    analyze.plotData()
    analyze.plotDifference()

    plt.show()

if __name__ == '__main__': #pragma: no cover
    run()