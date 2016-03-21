#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.BeamParameters
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

MCXRay beam parameters from results file.
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
KEY_BEAM_PARAMETERS = "Beam Parameters"

KEY_INCIDENT_ENERGY_keV = "Electron incident energy"
KEY_CURRENT_A = "Beam Current"
KEY_ACQUISITION_TIME_s = "Acquisition Time"
KEY_DIAMETER_90_A = "Diameter with 90% of the electrons"
KEY_TILT_ANGLE_deg = "Tilt angle"
KEY_GAUSSIAN_MEAN = "Gaussian Mean"
KEY_GAUSSIAN_SIGMA = "Gaussian Sigma"

class BeamParameters(object):
    def __init__(self):
        self._parameters = {}

    def _createKeys(self):
        keys = []

        keys.append(KEY_INCIDENT_ENERGY_keV)
        keys.append(KEY_CURRENT_A)
        keys.append(KEY_ACQUISITION_TIME_s)
        keys.append(KEY_DIAMETER_90_A)
        keys.append(KEY_TILT_ANGLE_deg)
        keys.append(KEY_GAUSSIAN_MEAN)
        keys.append(KEY_GAUSSIAN_SIGMA)

        return keys

    def readFromLines(self, lines):
        # Skip header line.
        indexLine = 0
        for line in lines:
            indexLine += 1
            if line.strip().startswith(KEY_BEAM_PARAMETERS):
                break
        else:
            message = "Cannot find the section header in the liens: %s" % (KEY_BEAM_PARAMETERS)
            raise ValueError(message)

        for key in self._createKeys():
            line = lines[indexLine]
            indexLine += 1

            label, value = line.split('=')

            if label.strip() == key:
                self._parameters[key] = self._extractValue(value)

        # Skip comment lines.
        indexLine += 3

        return indexLine

    def _extractValue(self, valueText):
        if '(' in valueText:
            endIndex = valueText.find('(')
            return float(valueText[:endIndex])
        else:
            return float(valueText)

    @property
    def incidentEnergy_keV(self):
        return self._parameters[KEY_INCIDENT_ENERGY_keV]
    @incidentEnergy_keV.setter
    def incidentEnergy_keV(self, incidentEnergy_keV):
        self._parameters[KEY_INCIDENT_ENERGY_keV] = incidentEnergy_keV

    @property
    def current_A(self):
        return self._parameters[KEY_CURRENT_A]
    @current_A.setter
    def current_A(self, current_A):
        self._parameters[KEY_CURRENT_A] = current_A

    @property
    def acquisitionTime_s(self):
        return self._parameters[KEY_ACQUISITION_TIME_s]
    @acquisitionTime_s.setter
    def acquisitionTime_s(self, acquisitionTime_s):
        self._parameters[KEY_ACQUISITION_TIME_s] = acquisitionTime_s

    @property
    def diameter90_A(self):
        return self._parameters[KEY_DIAMETER_90_A]
    @diameter90_A.setter
    def diameter90_A(self, diameter90_A):
        self._parameters[KEY_DIAMETER_90_A] = diameter90_A

    @property
    def tiltAngle_deg(self):
        return self._parameters[KEY_TILT_ANGLE_deg]
    @tiltAngle_deg.setter
    def tiltAngle_deg(self, tiltAngle_deg):
        self._parameters[KEY_TILT_ANGLE_deg] = tiltAngle_deg

    @property
    def gaussianMean(self):
        return self._parameters[KEY_GAUSSIAN_MEAN]
    @gaussianMean.setter
    def gaussianMean(self, gaussianMean):
        self._parameters[KEY_GAUSSIAN_MEAN] = gaussianMean

    @property
    def gaussianSigma(self):
        return self._parameters[KEY_GAUSSIAN_SIGMA]
    @gaussianSigma.setter
    def gaussianSigma(self, gaussianSigma):
        self._parameters[KEY_GAUSSIAN_SIGMA] = gaussianSigma
