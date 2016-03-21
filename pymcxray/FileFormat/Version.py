#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Version
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

MCXray version information.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2012 Hendrix Demers"
__license__ = ""

# Standard library modules.
import copy

# Third party modules.

# Local modules.

# Project modules

# Globals and constants variables.

class Version(object):
    key = "Version"

    def __init__(self, major, minor, revision):
        self.major = major
        self.minor = minor
        self.revision = revision

    def toString(self):
        text = "%s.%s.%s" % (self.major, self.minor, self.revision)
        return text

    def fromString(self, versionString):
        items = versionString.split('.')
        self.major = items[0]
        self.minor = items[1]
        self.revision = items[2]

    def writeLine(self, outputFile):
        line = "%s=%s\n" % (self.key, self.toString())
        outputFile.write(line)

    def readFromFile(self, filepath):
        lines = open(filepath, 'r').readlines()

        for line in lines:
            line = line.strip()

            if line.startswith(self.key):
                items = line.split('=')
                self.fromString((items[-1]))
                return
        else:
            self.major = 1
            self.minor = 1
            self.revision = 1

    def __eq__(self, other):
        if self.major == other.major and self.minor == other.minor and self.revision == other.revision:
            return True
        else:
            return False

    def __lt__(self, other):
        if self == other:
            return False

        if self.major < other.major:
            return True
        elif self.major > other.major:
            return False

        if self.minor < other.minor:
            return True
        elif self.minor > other.minor:
            return False

        if self.revision < other.revision:
            return True
        elif self.revision > other.revision:
            return False

    def __ge__(self, other):
        if self == other:
            return True
        if self < other:
            return False
        else:
            return True

    @property
    def major(self):
        return self._major
    @major.setter
    def major(self, major):
        self._major = int(major)

    @property
    def minor(self):
        return self._minor
    @minor.setter
    def minor(self, minor):
        self._minor = int(minor)

    @property
    def revision(self):
        return self._revision
    @revision.setter
    def revision(self, revision):
        self._revision = int(revision)

VERSION_1_1_1 = Version(1, 1, 1)

VERSION_1_2_0 = Version(1, 2, 0)

VERSION_1_2_1 = Version(1, 2, 1)

VERSION_1_2_2 = Version(1, 2, 2)

VERSION_1_2_3 = Version(1, 2, 3)

VERSION_1_2_4 = Version(1, 2, 4)

VERSION_1_2_5 = Version(1, 2, 5)

VERSION_1_3_0 = Version(1, 3, 0)

VERSION_1_4_0 = Version(1, 4, 0)

VERSION_1_4_1 = Version(1, 4, 1)

VERSION_1_4_2 = Version(1, 4, 2)

VERSION_1_4_3 = Version(1, 4, 3)

VERSION_1_4_4 = Version(1, 4, 4)

VERSION_1_4_5 = Version(1, 4, 5)

VERSION_1_4_6 = Version(1, 4, 6)

VERSION_1_5_0 = Version(1, 5, 0)

VERSION_1_5_1 = Version(1, 5, 1)

VERSION_1_5_2 = Version(1, 5, 2)

BEFORE_VERSION = copy.deepcopy(VERSION_1_1_1)
CURRENT_VERSION = copy.deepcopy(VERSION_1_5_2)
