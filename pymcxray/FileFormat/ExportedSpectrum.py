#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.ExportedSpectrum
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Read and write exported spectrum from McXRay.
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

class ExportedSpectrum(object):
    def __init__(self):
        self._spectrumType = None
        self._energies_keV = []
        self._intensities = []

    def read(self, filepath):
        lines = open(filepath, 'r').readlines()

        header = lines[0].strip()
        self._spectrumType = header

        for line in lines[1:]:
            items = line.split()
            if len(items) >= 2:
                energy_keV = float(items[0])
                intensity = float(items[1])

                self._energies_keV.append(energy_keV)
                self._intensities.append(intensity)

    def getSpectrumType(self):
        return self._spectrumType

    def getData(self):
        return self._energies_keV, self._intensities
