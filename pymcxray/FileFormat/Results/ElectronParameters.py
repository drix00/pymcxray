#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.ElectronParameters
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

MCXRay electron parameters results file.
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
KEY_ELECTRON_PARAMETERS = "Electrons Parameters and Results"

KEY_NUMBER_SIMULATED_ELECTRONS = "Total simulated electrons"
KEY_MEAN_NUMBER_COLLISIONS_PER_ELECTRON = "Mean number of collisions per e"
KEY_MEAN_DISTANCE_BETWEEN_COLLISIONS_A = "Mean distance between collisions"
KEY_MEAN_POLAR_ANGLE_COLLISIONS_deg = "Mean polar angle of collision"
KEY_MEAN_AZIMUTHAL_ANGLE_COLLISIONS_deg = "Mean azimuthal angle of collision"
KEY_BACKSCATTERING_RATIO = "Backscattering ratio"
KEY_INTERNAL_RATIO = "Internal ratio"
KEY_THROUGH_RATIO = "Through ratio"
KEY_SKIRT_RATIO = "Skirt ratio"
KEY_E_RATIO = "E_Ratio"

class ElectronParameters(object):
    def __init__(self):
        self._parameters = {}

    def _createKeys(self):
        keys = []

        keys.append(KEY_NUMBER_SIMULATED_ELECTRONS)
        keys.append(KEY_MEAN_NUMBER_COLLISIONS_PER_ELECTRON)
        keys.append(KEY_MEAN_DISTANCE_BETWEEN_COLLISIONS_A)
        keys.append(KEY_MEAN_POLAR_ANGLE_COLLISIONS_deg)
        keys.append(KEY_MEAN_AZIMUTHAL_ANGLE_COLLISIONS_deg)
        keys.append(KEY_BACKSCATTERING_RATIO)
        keys.append(KEY_INTERNAL_RATIO)
        keys.append(KEY_THROUGH_RATIO)
        keys.append(KEY_SKIRT_RATIO)
        keys.append(KEY_E_RATIO)

        return keys

    def _createExtractMdethodList(self):
        extractMethodList = {}

        extractMethodList[KEY_NUMBER_SIMULATED_ELECTRONS] = int
        extractMethodList[KEY_MEAN_NUMBER_COLLISIONS_PER_ELECTRON] = float
        extractMethodList[KEY_MEAN_DISTANCE_BETWEEN_COLLISIONS_A] = self._extractFloatValue
        extractMethodList[KEY_MEAN_POLAR_ANGLE_COLLISIONS_deg] = self._extractFloatValue
        extractMethodList[KEY_MEAN_AZIMUTHAL_ANGLE_COLLISIONS_deg] = self._extractFloatValue
        extractMethodList[KEY_BACKSCATTERING_RATIO] = float
        extractMethodList[KEY_INTERNAL_RATIO] = float
        extractMethodList[KEY_THROUGH_RATIO] = float
        extractMethodList[KEY_SKIRT_RATIO] = float
        extractMethodList[KEY_E_RATIO] = float

        return extractMethodList

    def _extractFloatValue(self, valueText):
        if '(' in valueText:
            endIndex = valueText.find('(')
            return float(valueText[:endIndex])
        else:
            return float(valueText)

    def readFromLines(self, lines):
        # Skip header line.
        indexLine = 0
        for line in lines:
            indexLine += 1
            if line.strip().startswith(KEY_ELECTRON_PARAMETERS):
                break
        else:
            message = "Cannot find the section header in the liens: %s" % (KEY_ELECTRON_PARAMETERS)
            raise ValueError(message)

        extractMethodList = self._createExtractMdethodList()
        for key in self._createKeys():
            line = lines[indexLine]
            indexLine += 1

            label, value = line.split('=')

            if label.strip() == key:
                self._parameters[key] = extractMethodList[key](value)

        return indexLine

    @property
    def numberSimulatedElectrons(self):
        return self._parameters[KEY_NUMBER_SIMULATED_ELECTRONS]
    @numberSimulatedElectrons.setter
    def numberSimulatedElectrons(self, numberSimulatedElectrons):
        self._parameters[KEY_NUMBER_SIMULATED_ELECTRONS] = numberSimulatedElectrons

    @property
    def meanNumberCollisionPerElectrons(self):
        return self._parameters[KEY_MEAN_NUMBER_COLLISIONS_PER_ELECTRON]
    @meanNumberCollisionPerElectrons.setter
    def meanNumberCollisionPerElectrons(self, meanNumberCollisionPerElectrons):
        self._parameters[KEY_MEAN_NUMBER_COLLISIONS_PER_ELECTRON] = meanNumberCollisionPerElectrons

    @property
    def meanDistanceBetweenCollisions_A(self):
        return self._parameters[KEY_MEAN_DISTANCE_BETWEEN_COLLISIONS_A]
    @meanDistanceBetweenCollisions_A.setter
    def meanDistanceBetweenCollisions_A(self, meanDistanceBetweenCollisions_A):
        self._parameters[KEY_MEAN_DISTANCE_BETWEEN_COLLISIONS_A] = meanDistanceBetweenCollisions_A

    @property
    def meanPolarAngleCollision_deg(self):
        return self._parameters[KEY_MEAN_POLAR_ANGLE_COLLISIONS_deg]
    @meanPolarAngleCollision_deg.setter
    def meanPolarAngleCollision_deg(self, meanPolarAngleCollision_deg):
        self._parameters[KEY_MEAN_POLAR_ANGLE_COLLISIONS_deg] = meanPolarAngleCollision_deg

    @property
    def meanAzimuthalAngleCollision_deg(self):
        return self._parameters[KEY_MEAN_AZIMUTHAL_ANGLE_COLLISIONS_deg]
    @meanAzimuthalAngleCollision_deg.setter
    def meanAzimuthalAngleCollision_deg(self, meanAzimuthalAngleCollision_deg):
        self._parameters[KEY_MEAN_AZIMUTHAL_ANGLE_COLLISIONS_deg] = meanAzimuthalAngleCollision_deg

    @property
    def backscatteredRatio(self):
        return self._parameters[KEY_BACKSCATTERING_RATIO]
    @backscatteredRatio.setter
    def backscatteredRatio(self, backscatteredRatio):
        self._parameters[KEY_BACKSCATTERING_RATIO] = backscatteredRatio

    @property
    def internalRatio(self):
        return self._parameters[KEY_INTERNAL_RATIO]
    @internalRatio.setter
    def internalRatio(self, internalRatio):
        self._parameters[KEY_INTERNAL_RATIO] = internalRatio

    @property
    def throughRatio(self):
        return self._parameters[KEY_THROUGH_RATIO]
    @throughRatio.setter
    def throughRatio(self, throughRatio):
        self._parameters[KEY_THROUGH_RATIO] = throughRatio

    @property
    def skirtRatio(self):
        return self._parameters[KEY_SKIRT_RATIO]
    @skirtRatio.setter
    def skirtRatio(self, skirtRatio):
        self._parameters[KEY_SKIRT_RATIO] = skirtRatio

    @property
    def eRatio(self):
        return self._parameters[KEY_E_RATIO]
    @eRatio.setter
    def eRatio(self, eRatio):
        self._parameters[KEY_E_RATIO] = eRatio
