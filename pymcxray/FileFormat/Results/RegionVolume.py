#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.RegionVolume
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

MCXRay result file region volume.
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
KEY_REGION_ID = "Volume ID"

class RegionVolume(object):
    def __init__(self):
        self._parameters = {}

    def _createKeys(self):
        keys = []

        keys.append(KEY_REGION_ID)

        return keys

    def readFromLines(self, lines):
        indexLine = 0

        for key in self._createKeys():
            line = lines[indexLine]
            indexLine += 1

            label, value = line.split('=')

            if label.strip() == key:
                self._parameters[key] = value

        return indexLine

    @property
    def regionID(self):
        return self._parameters[KEY_REGION_ID]
    @regionID.setter
    def regionID(self, regionID):
        self._parameters[KEY_REGION_ID] = regionID
