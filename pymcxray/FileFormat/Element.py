#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Element
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

MCXRay element input file.
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

KEY_ATOMIC_NUMBERS = "AtomicNumber"
KEY_NAME = "Name"
KEY_MASS_FRACTION = "WeightFraction"

class Element(object):
    def __init__(self, atomicNumber=0, massFraction=1.0):
        self._parameters = {}

        self.atomicNumber = atomicNumber
        self.massFraction = massFraction

    def extractFromLineOldVersion(self, line):
        items = line.split()

        self.atomicNumber = int(items[0])
        self.massFraction = float(items[1])

    def extractFromLinesWithKey(self, lines):
        indexLine = 0
        key = KEY_ATOMIC_NUMBERS
        line = lines[indexLine]
        line = line.strip()
        if line.startswith(key):
            items = line.split('=')
            self.atomicNumber = int(items[-1])
            indexLine += 1

        key = KEY_MASS_FRACTION
        line = lines[indexLine]
        line = line.strip()
        if line.startswith(key):
            items = line.split('=')
            self.massFraction = float(items[-1])
            indexLine += 1

        return indexLine

    def createLineOldVersion(self):
        line = "%i %.15f" % (self.atomicNumber, self.massFraction)

        return line

    def createLinesWithKey(self):
        lines = []

        line = "%s=%s" % (KEY_ATOMIC_NUMBERS, self.atomicNumber)
        lines.append(line)

        line = "%s=%.15f" % (KEY_MASS_FRACTION, self.massFraction)
        lines.append(line)

        return lines

    @property
    def atomicNumber(self):
        return self._parameters[KEY_ATOMIC_NUMBERS]
    @atomicNumber.setter
    def atomicNumber(self, atomicNumber):
        self._parameters[KEY_ATOMIC_NUMBERS] = atomicNumber

    @property
    def name(self):
        return self._parameters[KEY_NAME]
    @name.setter
    def name(self, name):
        self._parameters[KEY_NAME] = name

    @property
    def massFraction(self):
        return self._parameters[KEY_MASS_FRACTION]
    @massFraction.setter
    def massFraction(self, massFraction):
        self._parameters[KEY_MASS_FRACTION] = massFraction
