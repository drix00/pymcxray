#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.SpectrumEDS
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Read MCXRay EDS spectrm from results file.
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
import logging

# Third party modules.

# Local modules.

# Project modules

# Globals and constants variables.
KEY_CHANNEL = "channel"
KEY_ENERGY_keV = "Eref"
KEY_COUNTS = "Iref"

class SpectrumEDS(object):
    def __init__(self, lines=None):
        self._parameters = {}

        self.channels = []
        self.enegies_keV = []
        self.countsList = []

        if lines is not None:
            self.readLines(lines)

    def readLines(self, lines):
        for line in lines:
            try:
                items = line.split(',')

                for item in items:
                    key, value = item.split('=')
                    key = key.strip()

                    if key == KEY_CHANNEL:
                        self.channels.append(int(value))
                    elif key == KEY_ENERGY_keV:
                        self.enegies_keV.append(float(value))
                    elif key == KEY_COUNTS:
                        self.countsList.append(float(value))
            except ValueError as message:
                logging.info(message)

    @property
    def channels(self):
        return self._parameters[KEY_CHANNEL]
    @channels.setter
    def channels(self, channels):
        self._parameters[KEY_CHANNEL] = channels

    @property
    def enegies_keV(self):
        return self._parameters[KEY_ENERGY_keV]
    @enegies_keV.setter
    def enegies_keV(self, enegies_keV):
        self._parameters[KEY_ENERGY_keV] = enegies_keV

    @property
    def countsList(self):
        return self._parameters[KEY_COUNTS]
    @countsList.setter
    def countsList(self, countsList):
        self._parameters[KEY_COUNTS] = countsList
