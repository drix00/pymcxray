#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.RegionParameters
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

MCXRay region parameters result file.
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
REGION_PARAMETERS_REGION_ID = "regionID"
REGION_PARAMETERS_NUMBER_ELEMENTS = "numberElements"
REGION_PARAMETERS_ELEMENTS = "Elements"
REGION_PARAMETERS_LAYER_THICKNESS_A = "layerThickness"

class RegionParameters(object):
    def __init__(self):
        self._keys = self._createKeys()

        self._parameters = {}

    def _createKeys(self):
        keys = []

        keys.append(REGION_PARAMETERS_REGION_ID)
        keys.append(REGION_PARAMETERS_NUMBER_ELEMENTS)
        keys.append(REGION_PARAMETERS_ELEMENTS)
        keys.append(REGION_PARAMETERS_LAYER_THICKNESS_A)

        return keys

    @property
    def regionID(self):
        return self._parameters[REGION_PARAMETERS_REGION_ID]
    @regionID.setter
    def regionID(self, regionID):
        self._parameters[REGION_PARAMETERS_REGION_ID] = regionID

    @property
    def numberElements(self):
        return self._parameters[REGION_PARAMETERS_NUMBER_ELEMENTS]
    @numberElements.setter
    def numberElements(self, numberElements):
        self._parameters[REGION_PARAMETERS_NUMBER_ELEMENTS] = numberElements

    @property
    def elements(self):
        return self._parameters[REGION_PARAMETERS_ELEMENTS]
    @elements.setter
    def elements(self, elements):
        self._parameters[REGION_PARAMETERS_ELEMENTS] = elements

    @property
    def layerThickness_A(self):
        return self._parameters[REGION_PARAMETERS_LAYER_THICKNESS_A]
    @layerThickness_A.setter
    def layerThickness_A(self, layerThickness_A):
        self._parameters[REGION_PARAMETERS_LAYER_THICKNESS_A] = layerThickness_A
