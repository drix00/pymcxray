#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.Phirhoz
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

MCXRay phirhoz result file.
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
KEY_SHELL = "shell"
KEY_INTENSITY = "Intensity"
KEY_DEPTHS_A = "depths_A"
KEY_VALUES = "values"

class Phirhoz(object):
    def __init__(self, symbol, shell):
        self._parameters = {}

        self.symbol = symbol
        self.shell = shell
        self._label = "%s [Shell %s]," % (symbol, shell)

    def readFromLines(self, lines):
        indexLine = 0

        for line in lines[indexLine:]:
            indexLine += 1

            if line.startswith(self._label):
                items = line.split('=')
                self.intensity = float(items[-1])
                break

        self.depths_A = []
        self.values = []
        for _index in range(len(lines[indexLine:])):
            line = lines[indexLine]
            indexLine += 1
            try:
                items = line.split()

                depth_A = float(items[0])
                value = float(items[1])

                self.depths_A.append(depth_A)
                self.values.append(value)
            except:
                break

        return indexLine

    @property
    def symbol(self):
        return self._parameters[KEY_SYMBOL]
    @symbol.setter
    def symbol(self, symbol):
        self._parameters[KEY_SYMBOL] = symbol

    @property
    def shell(self):
        return self._parameters[KEY_SHELL]
    @shell.setter
    def shell(self, shell):
        self._parameters[KEY_SHELL] = shell

    @property
    def intensity(self):
        return self._parameters[KEY_INTENSITY]
    @intensity.setter
    def intensity(self, intensity):
        self._parameters[KEY_INTENSITY] = intensity

    @property
    def depths_A(self):
        return self._parameters[KEY_DEPTHS_A]
    @depths_A.setter
    def depths_A(self, depths_A):
        self._parameters[KEY_DEPTHS_A] = depths_A

    @property
    def values(self):
        return self._parameters[KEY_VALUES]
    @values.setter
    def values(self, values):
        self._parameters[KEY_VALUES] = values
