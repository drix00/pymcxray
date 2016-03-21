#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.RegionDimensions
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

MCXRay region dimensions input file.
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
import pymcxray.FileFormat.RegionType as RegionType

# Globals and constants variables.
REGION_DIMENSION_MINIMUM_X = "minimumX"
REGION_DIMENSION_MAXIMUM_X = "maximumX"
REGION_DIMENSION_MINIMUM_Y = "minimumY"
REGION_DIMENSION_MAXIMUM_Y = "maximumY"
REGION_DIMENSION_MINIMUM_Z = "minimumZ"
REGION_DIMENSION_MAXIMUM_Z = "maximumZ"

REGION_DIMENSION_POSITION_X = "positionX"
REGION_DIMENSION_POSITION_Y = "positionY"
REGION_DIMENSION_POSITION_Z = "positionZ"
REGION_DIMENSION_DIRECTION_X = "directionX"
REGION_DIMENSION_DIRECTION_Y = "directionY"
REGION_DIMENSION_DIRECTION_Z = "directionZ"
REGION_DIMENSION_LENGTH = "length"
REGION_DIMENSION_RADIUS = "radius"

KEY_REGION_PARAMETERS = "RegionParameters"

class RegionDimensions(object):
    def __init__(self, parameters=None):
        self._keys = self._createKeys()

        self._parameters = {}

        if parameters is not None:
            assert len(parameters) == len(self._keys)

            for key, parameter in zip(self._keys, parameters):
                self._parameters[key] = parameter

    def extractFromLineOldVersion(self, line):
        items = line.split()
        for key, item in zip(self._keys, items):
            self._parameters[key] = float(item)

    def extractFromLinesWithKey(self, line):
        key = KEY_REGION_PARAMETERS
        line = line.strip()
        if line.startswith(key):
            items = line.split('=')
            self.extractFromLineOldVersion(items[-1])

    def _createKeys(self): # pragma: no cover
        raise NotImplementedError

    def getLineFormat(self): # pragma: no cover
        raise NotImplementedError

    def createLineOldVersion(self):
        items = []
        for key in self._keys:
            items.append(self._parameters[key])

        line = self.getLineFormat() % tuple(items)
        return line

    def createLineWithKey(self):
        key = KEY_REGION_PARAMETERS
        value = self.createLineOldVersion()
        line = "%s=%s" % (key, value)

        return line

    def __eq__(self, other):
        if len(self._parameters) == len(other._parameters) and self._parameters == other._parameters:
            return True
        else:
            return False

class RegionDimensionsBox(RegionDimensions):
    def _createKeys(self):
        keys = []

        keys.append(REGION_DIMENSION_MINIMUM_X)
        keys.append(REGION_DIMENSION_MAXIMUM_X)
        keys.append(REGION_DIMENSION_MINIMUM_Y)
        keys.append(REGION_DIMENSION_MAXIMUM_Y)
        keys.append(REGION_DIMENSION_MINIMUM_Z)
        keys.append(REGION_DIMENSION_MAXIMUM_Z)

        return keys

    def getLineFormat(self):
        lineFormat = "%.6f %.6f %.6f %.6f %.6f %.6f"
        return lineFormat

    @property
    def minimumX(self):
        return self._parameters[REGION_DIMENSION_MINIMUM_X]
    @minimumX.setter
    def minimumX(self, minimumX):
        self._parameters[REGION_DIMENSION_MINIMUM_X] = minimumX

    @property
    def maximumX(self):
        return self._parameters[REGION_DIMENSION_MAXIMUM_X]
    @maximumX.setter
    def maximumX(self, maximumX):
        self._parameters[REGION_DIMENSION_MAXIMUM_X] = maximumX

    @property
    def minimumY(self):
        return self._parameters[REGION_DIMENSION_MINIMUM_Y]
    @minimumY.setter
    def minimumY(self, minimumY):
        self._parameters[REGION_DIMENSION_MINIMUM_Y] = minimumY

    @property
    def maximumY(self):
        return self._parameters[REGION_DIMENSION_MAXIMUM_Y]
    @maximumY.setter
    def maximumY(self, maximumY):
        self._parameters[REGION_DIMENSION_MAXIMUM_Y] = maximumY

    @property
    def minimumZ(self):
        return self._parameters[REGION_DIMENSION_MINIMUM_Z]
    @minimumZ.setter
    def minimumZ(self, minimumZ):
        self._parameters[REGION_DIMENSION_MINIMUM_Z] = minimumZ

    @property
    def maximumZ(self):
        return self._parameters[REGION_DIMENSION_MAXIMUM_Z]
    @maximumZ.setter
    def maximumZ(self, maximumZ):
        self._parameters[REGION_DIMENSION_MAXIMUM_Z] = maximumZ

class RegionDimensionsSphere(RegionDimensions):
    def _createKeys(self):
        keys = []

        keys.append(REGION_DIMENSION_POSITION_X)
        keys.append(REGION_DIMENSION_POSITION_Y)
        keys.append(REGION_DIMENSION_POSITION_Z)
        keys.append(REGION_DIMENSION_RADIUS)

        return keys

    def getLineFormat(self):
        lineFormat = "%.6f %.6f %.6f %.6f"
        return lineFormat

    @property
    def positionX(self):
        return self._parameters[REGION_DIMENSION_POSITION_X]
    @positionX.setter
    def positionX(self, positionX):
        self._parameters[REGION_DIMENSION_POSITION_X] = positionX

    @property
    def positionY(self):
        return self._parameters[REGION_DIMENSION_POSITION_Y]
    @positionY.setter
    def positionY(self, positionY):
        self._parameters[REGION_DIMENSION_POSITION_Y] = positionY

    @property
    def positionZ(self):
        return self._parameters[REGION_DIMENSION_POSITION_Z]
    @positionZ.setter
    def positionZ(self, positionZ):
        self._parameters[REGION_DIMENSION_POSITION_Z] = positionZ

    @property
    def radius(self):
        return self._parameters[REGION_DIMENSION_RADIUS]
    @radius.setter
    def radius(self, radius):
        self._parameters[REGION_DIMENSION_RADIUS] = radius

class RegionDimensionsCylinder(RegionDimensionsSphere):
    def _createKeys(self):
        keys = []

        keys.append(REGION_DIMENSION_POSITION_X)
        keys.append(REGION_DIMENSION_POSITION_Y)
        keys.append(REGION_DIMENSION_POSITION_Z)
        keys.append(REGION_DIMENSION_DIRECTION_X)
        keys.append(REGION_DIMENSION_DIRECTION_Y)
        keys.append(REGION_DIMENSION_DIRECTION_Z)
        keys.append(REGION_DIMENSION_LENGTH)
        keys.append(REGION_DIMENSION_RADIUS)

        return keys

    def getLineFormat(self):
        lineFormat = "%.6f %.6f %.6f %.6f %.6f %.6f %.6f %.6f"
        return lineFormat

    @property
    def directionX(self):
        return self._parameters[REGION_DIMENSION_DIRECTION_X]
    @directionX.setter
    def directionX(self, directionX):
        self._parameters[REGION_DIMENSION_DIRECTION_X] = directionX

    @property
    def directionY(self):
        return self._parameters[REGION_DIMENSION_DIRECTION_Y]
    @directionY.setter
    def directionY(self, directionY):
        self._parameters[REGION_DIMENSION_DIRECTION_Y] = directionY

    @property
    def directionZ(self):
        return self._parameters[REGION_DIMENSION_DIRECTION_Z]
    @directionZ.setter
    def directionZ(self, directionZ):
        self._parameters[REGION_DIMENSION_DIRECTION_Z] = directionZ

    @property
    def length(self):
        return self._parameters[REGION_DIMENSION_LENGTH]
    @length.setter
    def length(self, length):
        self._parameters[REGION_DIMENSION_LENGTH] = length

def createRegionDimensions(regionType):
    if regionType == RegionType.REGION_TYPE_BOX:
        return RegionDimensionsBox()
    elif regionType == RegionType.REGION_TYPE_CYLINDER:
        return RegionDimensionsCylinder()
    elif regionType == RegionType.REGION_TYPE_SPHERE:
        return RegionDimensionsSphere()
