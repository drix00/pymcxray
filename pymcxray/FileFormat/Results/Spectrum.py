#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.Spectrum
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

MCXRay spectrum result file.
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

SPECTRUM_ENERGIES_keV = "Energies (keV)"
SPECTRUM_INTENSITIES = "Intensities"
SPECTRUM_INTENSITIES_BACKGROUND = "Background Intensities"
SPECTRUM_INTENSITIES_CHARACTERISTIC = "Characteristic Intensities"

class Spectrum(object):
    def __init__(self):
        self._keys = self._createKeys()

        self._values = {}

    def _createKeys(self):
        keys = []

        keys.append(SPECTRUM_ENERGIES_keV)
        keys.append(SPECTRUM_INTENSITIES)
        keys.append(SPECTRUM_INTENSITIES_BACKGROUND)
        keys.append(SPECTRUM_INTENSITIES_CHARACTERISTIC)

        return keys

    @property
    def energies_keV(self):
        return self._values[SPECTRUM_ENERGIES_keV]
    @energies_keV.setter
    def energies_keV(self, energies_keV):
        self._values[SPECTRUM_ENERGIES_keV] = energies_keV

    @property
    def intensities(self):
        return self._values[SPECTRUM_INTENSITIES]
    @intensities.setter
    def intensities(self, intensities):
        self._values[SPECTRUM_INTENSITIES] = intensities

    @property
    def backgroundIntensities(self):
        return self._values[SPECTRUM_INTENSITIES_BACKGROUND]
    @backgroundIntensities.setter
    def backgroundIntensities(self, backgroundIntensities):
        self._values[SPECTRUM_INTENSITIES_BACKGROUND] = backgroundIntensities

    @property
    def characteristicIntensities(self):
        return self._values[SPECTRUM_INTENSITIES_CHARACTERISTIC]
    @characteristicIntensities.setter
    def characteristicIntensities(self, characteristicIntensities):
        self._values[SPECTRUM_INTENSITIES_CHARACTERISTIC] = characteristicIntensities
