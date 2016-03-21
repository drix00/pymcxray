#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.DetectorParameters
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

MCXRay detector parameters from results file.
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
KEY_DETECTOR_PARAMETERS = "Detector Parameters"

KEY_CRYSTAL_NAME = "Detector crystal"
KEY_CRYSTAL_DENSITY_g_cm3 = "Crystal density"
KEY_CRYSTAL_THICKNESS_cm = "Crystal thichness"
KEY_CRYSTAL_RADIUS_cm = "Crystal radius"
KEY_BEAM_DETECTOR_DISTANCE_cm = "Distance beam-detector"
KEY_DEAD_LAYER_THICKNESS_A = "Dead layer"
KEY_DIFFUSION_LENGTH_A = "Diffusion length"
KEY_SURFACE_QUALITY_FACTOR = "Surface quality factor"
KEY_NOISE_EDS_DETECTOR_eV = "Noise at EDS detector"
KEY_THICKNESS_BE_WINDOW_um = "Thickness of Be window"
KEY_THICKNESS_AL_WINDOW_um = "Thickness of Al window"
KEY_THICKNESS_TI_WINDOW_um = "Thickness of Ti window"
KEY_THICKNESS_OIL_um = "Thickness of Oil"
KEY_THICKNESS_H2O_um = "Thickness of H2O"
KEY_THICKNESS_MOXTEK_um = "Thickness of Moxtek"
KEY_THICKNESS_AIR_um = "Thickness of air path"
KEY_ANGLE_BETWEEN_DETECTOR_SPECIMEN_NORMAL_deg = "Angle between detector axis and specimen normal"
KEY_ANGLE_BETWEEN_DETECTORX_AXIS_deg = "Angle between detector and x axis on the X-Y plane"
KEY_TAKEOFF_ANGLE_NORMAL_INCIDENCE_deg = "Take Off Angle at Normal Incidence"
KEY_TAKEOFF_ANGLE_EFFECTIVE_deg = "Effective Take Off Angle"
KEY_SOLID_ANGLE_deg = "Solid angle of the detector"

class DetectorParameters(object):
    def __init__(self):
        self._parameters = {}

    def _createKeys(self):
        keys = []

        keys.append(KEY_CRYSTAL_NAME)
        keys.append(KEY_CRYSTAL_DENSITY_g_cm3)
        keys.append(KEY_CRYSTAL_THICKNESS_cm)
        keys.append(KEY_CRYSTAL_RADIUS_cm)
        keys.append(KEY_BEAM_DETECTOR_DISTANCE_cm)
        keys.append(KEY_DEAD_LAYER_THICKNESS_A)
        keys.append(KEY_DIFFUSION_LENGTH_A)
        keys.append(KEY_SURFACE_QUALITY_FACTOR)
        keys.append(KEY_NOISE_EDS_DETECTOR_eV)
        keys.append(KEY_THICKNESS_BE_WINDOW_um)
        keys.append(KEY_THICKNESS_AL_WINDOW_um)
        keys.append(KEY_THICKNESS_TI_WINDOW_um)
        keys.append(KEY_THICKNESS_OIL_um)
        keys.append(KEY_THICKNESS_H2O_um)
        keys.append(KEY_THICKNESS_MOXTEK_um)
        keys.append(KEY_THICKNESS_AIR_um)
        keys.append(KEY_ANGLE_BETWEEN_DETECTOR_SPECIMEN_NORMAL_deg)
        keys.append(KEY_ANGLE_BETWEEN_DETECTORX_AXIS_deg)
        keys.append(KEY_TAKEOFF_ANGLE_NORMAL_INCIDENCE_deg)
        keys.append(KEY_TAKEOFF_ANGLE_EFFECTIVE_deg)
        keys.append(KEY_SOLID_ANGLE_deg)

        return keys

    def readFromLines(self, lines):
        # Skip header line.
        indexLine = 0
        for line in lines:
            indexLine += 1
            if line.strip().startswith(KEY_DETECTOR_PARAMETERS):
                break
        else:
            message = "Cannot find the section header in the liens: %s" % (KEY_DETECTOR_PARAMETERS)
            raise ValueError(message)

        for key in self._createKeys():
            line = lines[indexLine]
            indexLine += 1

            if key == KEY_CRYSTAL_NAME:
                label, value = line.split('is')
                if label.strip() == key:
                    self._parameters[key] = str(value).strip()
                    continue

            label, value = line.split('=')
            if label.strip() == key:
                self._parameters[key] = self._extractValue(value)

        return indexLine

    def _extractValue(self, valueText):
        if '(' in valueText:
            endIndex = valueText.find('(')
            return float(valueText[:endIndex])
        else:
            return float(valueText)

    @property
    def crystalName(self):
        return self._parameters[KEY_CRYSTAL_NAME]
    @crystalName.setter
    def crystalName(self, crystalName):
        self._parameters[KEY_CRYSTAL_NAME] = crystalName

    @property
    def crystalDensity_g_cm3(self):
        return self._parameters[KEY_CRYSTAL_DENSITY_g_cm3]
    @crystalDensity_g_cm3.setter
    def crystalDensity_g_cm3(self, crystalDensity_g_cm3):
        self._parameters[KEY_CRYSTAL_DENSITY_g_cm3] = crystalDensity_g_cm3

    @property
    def crystalThickness_cm(self):
        return self._parameters[KEY_CRYSTAL_THICKNESS_cm]
    @crystalThickness_cm.setter
    def crystalThickness_cm(self, crystalThickness_cm):
        self._parameters[KEY_CRYSTAL_THICKNESS_cm] = crystalThickness_cm

    @property
    def crystalRadius_cm(self):
        return self._parameters[KEY_CRYSTAL_RADIUS_cm]
    @crystalRadius_cm.setter
    def crystalRadius_cm(self, crystalRadius_cm):
        self._parameters[KEY_CRYSTAL_RADIUS_cm] = crystalRadius_cm

    @property
    def beamDetectorDistance_cm(self):
        return self._parameters[KEY_BEAM_DETECTOR_DISTANCE_cm]
    @beamDetectorDistance_cm.setter
    def beamDetectorDistance_cm(self, beamDetectorDistance_cm):
        self._parameters[KEY_BEAM_DETECTOR_DISTANCE_cm] = beamDetectorDistance_cm

    @property
    def deadLayerThickness_A(self):
        return self._parameters[KEY_DEAD_LAYER_THICKNESS_A]
    @deadLayerThickness_A.setter
    def deadLayerThickness_A(self, deadLayerThickness_A):
        self._parameters[KEY_DEAD_LAYER_THICKNESS_A] = deadLayerThickness_A

    @property
    def diffusionLength_A(self):
        return self._parameters[KEY_DIFFUSION_LENGTH_A]
    @diffusionLength_A.setter
    def diffusionLength_A(self, diffusionLength_A):
        self._parameters[KEY_DIFFUSION_LENGTH_A] = diffusionLength_A

    @property
    def surfaceQualityFactor(self):
        return self._parameters[KEY_SURFACE_QUALITY_FACTOR]
    @surfaceQualityFactor.setter
    def surfaceQualityFactor(self, surfaceQualityFactor):
        self._parameters[KEY_SURFACE_QUALITY_FACTOR] = surfaceQualityFactor

    @property
    def noiseEdsDetector_eV(self):
        return self._parameters[KEY_NOISE_EDS_DETECTOR_eV]
    @noiseEdsDetector_eV.setter
    def noiseEdsDetector_eV(self, noiseEdsDetector_eV):
        self._parameters[KEY_NOISE_EDS_DETECTOR_eV] = noiseEdsDetector_eV

    @property
    def thicknessBeWindow_um(self):
        return self._parameters[KEY_THICKNESS_BE_WINDOW_um]
    @thicknessBeWindow_um.setter
    def thicknessBeWindow_um(self, thicknessBeWindow_um):
        self._parameters[KEY_THICKNESS_BE_WINDOW_um] = thicknessBeWindow_um

    @property
    def thicknessAlWindow_um(self):
        return self._parameters[KEY_THICKNESS_AL_WINDOW_um]
    @thicknessAlWindow_um.setter
    def thicknessAlWindow_um(self, thicknessAlWindow_um):
        self._parameters[KEY_THICKNESS_AL_WINDOW_um] = thicknessAlWindow_um

    @property
    def thicknessTiWindow_um(self):
        return self._parameters[KEY_THICKNESS_TI_WINDOW_um]
    @thicknessTiWindow_um.setter
    def thicknessTiWindow_um(self, thicknessTiWindow_um):
        self._parameters[KEY_THICKNESS_TI_WINDOW_um] = thicknessTiWindow_um

    @property
    def thicknessOil_um(self):
        return self._parameters[KEY_THICKNESS_OIL_um]
    @thicknessOil_um.setter
    def thicknessOil_um(self, thicknessOil_um):
        self._parameters[KEY_THICKNESS_OIL_um] = thicknessOil_um

    @property
    def thicknessH2O_um(self):
        return self._parameters[KEY_THICKNESS_H2O_um]
    @thicknessH2O_um.setter
    def thicknessH2O_um(self, thicknessH2O_um):
        self._parameters[KEY_THICKNESS_H2O_um] = thicknessH2O_um

    @property
    def thicknessMoxtek_um(self):
        return self._parameters[KEY_THICKNESS_MOXTEK_um]
    @thicknessMoxtek_um.setter
    def thicknessMoxtek_um(self, thicknessMoxtek_um):
        self._parameters[KEY_THICKNESS_MOXTEK_um] = thicknessMoxtek_um

    @property
    def thicknessAir_um(self):
        return self._parameters[KEY_THICKNESS_AIR_um]
    @thicknessAir_um.setter
    def thicknessAir_um(self, thicknessAir_um):
        self._parameters[KEY_THICKNESS_AIR_um] = thicknessAir_um

    @property
    def angleBetweenDetectorSpecimenNormal_deg(self):
        return self._parameters[KEY_ANGLE_BETWEEN_DETECTOR_SPECIMEN_NORMAL_deg]
    @angleBetweenDetectorSpecimenNormal_deg.setter
    def angleBetweenDetectorSpecimenNormal_deg(self, angleBetweenDetectorSpecimenNormal_deg):
        self._parameters[KEY_ANGLE_BETWEEN_DETECTOR_SPECIMEN_NORMAL_deg] = angleBetweenDetectorSpecimenNormal_deg

    @property
    def angleBetweenDetectorXAxis_deg(self):
        return self._parameters[KEY_ANGLE_BETWEEN_DETECTORX_AXIS_deg]
    @angleBetweenDetectorXAxis_deg.setter
    def angleBetweenDetectorXAxis_deg(self, angleBetweenDetectorXAxis_deg):
        self._parameters[KEY_ANGLE_BETWEEN_DETECTORX_AXIS_deg] = angleBetweenDetectorXAxis_deg

    @property
    def takeoffAngleNormalIncidence_deg(self):
        return self._parameters[KEY_TAKEOFF_ANGLE_NORMAL_INCIDENCE_deg]
    @takeoffAngleNormalIncidence_deg.setter
    def takeoffAngleNormalIncidence_deg(self, takeoffAngleNormalIncidence_deg):
        self._parameters[KEY_TAKEOFF_ANGLE_NORMAL_INCIDENCE_deg] = takeoffAngleNormalIncidence_deg

    @property
    def takeoffAngleEffective_deg(self):
        return self._parameters[KEY_TAKEOFF_ANGLE_EFFECTIVE_deg]
    @takeoffAngleEffective_deg.setter
    def takeoffAngleEffective_deg(self, takeoffAngleEffective_deg):
        self._parameters[KEY_TAKEOFF_ANGLE_EFFECTIVE_deg] = takeoffAngleEffective_deg

    @property
    def solidAngle_deg(self):
        return self._parameters[KEY_SOLID_ANGLE_deg]
    @solidAngle_deg.setter
    def solidAngle_deg(self, solidAngle_deg):
        self._parameters[KEY_SOLID_ANGLE_deg] = solidAngle_deg
