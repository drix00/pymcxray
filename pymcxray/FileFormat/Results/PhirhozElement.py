#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.PhirhozElement
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

MCXRay result file phirhoz element.
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
KEY_SYMBOL = "symbol"
KEY_WEIGHT_FRACTION = "weightFraction"
KEY_IONIZATION_SHELL_K = "isIonizationShell_K"
KEY_IONIZATION_SHELL_L = "isIonizationShell_L"
KEY_IONIZATION_SHELL_M = "isIonizationShell_M"

class PhirhozElement(object):
    def __init__(self):
        self._parameters = {}

    def _createKeys(self):
        keys = []

        keys.append(KEY_SYMBOL)
        keys.append(KEY_WEIGHT_FRACTION)
        keys.append(KEY_IONIZATION_SHELL_K)
        keys.append(KEY_IONIZATION_SHELL_L)
        keys.append(KEY_IONIZATION_SHELL_M)

        return keys

    def readFromLine(self, line):
        # Au, 100.0000000 %   Ionization shells 0 1 1
        items = line.split()
        self.symbol = str(items[0]).replace(',', '')
        self.weightFraction = float(items[1])/100.0

        self.isIonizationShell_K = bool(int(items[-3]))
        self.isIonizationShell_L = bool(int(items[-2]))
        self.isIonizationShell_M = bool(int(items[-1]))

    @property
    def symbol(self):
        return self._parameters[KEY_SYMBOL]
    @symbol.setter
    def symbol(self, symbol):
        self._parameters[KEY_SYMBOL] = symbol

    @property
    def weightFraction(self):
        return self._parameters[KEY_WEIGHT_FRACTION]
    @weightFraction.setter
    def weightFraction(self, weightFraction):
        self._parameters[KEY_WEIGHT_FRACTION] = weightFraction

    @property
    def isIonizationShell_K(self):
        return self._parameters[KEY_IONIZATION_SHELL_K]
    @isIonizationShell_K.setter
    def isIonizationShell_K(self, isIonizationShell_K):
        self._parameters[KEY_IONIZATION_SHELL_K] = isIonizationShell_K

    @property
    def isIonizationShell_L(self):
        return self._parameters[KEY_IONIZATION_SHELL_L]
    @isIonizationShell_L.setter
    def isIonizationShell_L(self, isIonizationShell_L):
        self._parameters[KEY_IONIZATION_SHELL_L] = isIonizationShell_L

    @property
    def isIonizationShell_M(self):
        return self._parameters[KEY_IONIZATION_SHELL_M]
    @isIonizationShell_M.setter
    def isIonizationShell_M(self, isIonizationShell_M):
        self._parameters[KEY_IONIZATION_SHELL_M] = isIonizationShell_M
