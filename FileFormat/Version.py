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
        line = "%s=%s\r\n" % (self.key, self.toString())
        outputFile.write(line)

    def readFromFile(self, filepath):
        lines = open(filepath, 'rb').readlines()

        for line in lines:
            line = line.strip()

            if line.startswith(self.key):
                items = line.split('=')
                self.fromString(str(items[-1]))
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

VERSION_1_1_1 = Version(1, 1, 1);

VERSION_1_2_0 = Version(1, 2, 0);

VERSION_1_2_1 = Version(1, 2, 1);

BEFORE_VERSION = VERSION_1_1_1;
CURRENT_VERSION = VERSION_1_2_1;


if __name__ == '__main__': #pragma: no cover
    import DrixUtilities.Runner as Runner
    Runner.Runner().run(runFunction=None)
