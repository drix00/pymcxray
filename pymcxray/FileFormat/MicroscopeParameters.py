#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.MicroscopeParameters
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

MCXRay microscope parameters input file.
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
import copy

# Third party modules.

# Local modules.

# Project modules
import pymcxray.FileFormat.Version as Version
from pymcxray.FileFormat.FileReaderWriterTools import reduceAfterDot

# Globals and constants variables.
KEY_BEAM_ENERGY_keV = "BeamEnergy"
KEY_BEAM_CURRENT_A = "BeamCurrent"
KEY_BEAM_TIME_s = "AcquisitionTime"
KEY_BEAM_DIAMETER_A = "BeamDiameter"
KEY_BEAM_POSITION_X_A = "BeamPosX"
KEY_BEAM_POSITION_Y_A = "BeamPosY"
KEY_BEAM_TILT_deg = "BeamTilt"
KEY_BEAM_STANDARD_DEVIATION_A = "BeamStandardDeviation"
KEY_DETECTOR_CRYSTAL_ATOM = "DetectorCrystalAtom"
KEY_DETECTOR_CRYSTAL_THICKNESS_cm = "DetectorCrystalThickness"
KEY_DETECTOR_CRYSTAL_RADIUS_cm = "DetectorCrystalRadius"
KEY_DETECTOR_CRYSTAL_DISTANCE_cm = "DetectorCrystalDistance"
KEY_DETECTOR_DEAD_LAYER_A = "DetectorDeadLayer"
KEY_DETECTOR_DIFFUSION_LENGHT_A = "DetectorDiffusionLenght"
KEY_DETECTOR_SURFACE_QUALITY = "DetectorSurfaceQuality"
KEY_DETECTOR_NOISE_eV = "DetectorNoise"
KEY_DETECTOR_TOA_deg = "DetectorTOA"
KEY_DETECTOR_CHANNEL_WIDTH_eV = "DetectorChannelWidth"
KEY_DETECTOR_PITCH_deg = "DetectorPitch"
KEY_DETECTOR_BF_LOW_rad = "DetectorBFLow"
KEY_DETECTOR_BF_HIGH_RAD = "DetectorBFHigh"
KEY_DETECTOR_DF_LOW_rad = "DetectorDFLow"
KEY_DETECTOR_DF_HIGH_rad = "DetectorDFHigh"
KEY_DETECTOR_HAADF_LOW_rad = "DetectorHAADFLow"
KEY_DETECTOR_HAADF_HIGH_rad = "DetectorHAADFHigh"

class MicroscopeParameters(object):
    def __init__(self):
        self.version = copy.deepcopy(Version.CURRENT_VERSION)

        self._keys = self._createKeys()

        self._parameters = {}

        self.defaultValues()

    def _createKeys(self):
        keys = []

        keys.append(KEY_BEAM_ENERGY_keV)
        keys.append(KEY_BEAM_CURRENT_A)
        keys.append(KEY_BEAM_TIME_s)
        keys.append(KEY_BEAM_DIAMETER_A)
        keys.append(KEY_BEAM_POSITION_X_A)
        keys.append(KEY_BEAM_POSITION_Y_A)
        keys.append(KEY_BEAM_TILT_deg)
        keys.append(KEY_BEAM_STANDARD_DEVIATION_A)
        keys.append(KEY_DETECTOR_CRYSTAL_ATOM)
        keys.append(KEY_DETECTOR_CRYSTAL_THICKNESS_cm)
        keys.append(KEY_DETECTOR_CRYSTAL_RADIUS_cm)
        keys.append(KEY_DETECTOR_CRYSTAL_DISTANCE_cm)
        keys.append(KEY_DETECTOR_DEAD_LAYER_A)
        keys.append(KEY_DETECTOR_DIFFUSION_LENGHT_A)
        keys.append(KEY_DETECTOR_SURFACE_QUALITY)
        keys.append(KEY_DETECTOR_NOISE_eV)
        keys.append(KEY_DETECTOR_TOA_deg)
        #keys.append(KEY_DETECTOR_CHANNEL_WIDTH_eV)
        keys.append(KEY_DETECTOR_PITCH_deg)
        keys.append(KEY_DETECTOR_BF_LOW_rad)
        keys.append(KEY_DETECTOR_BF_HIGH_RAD)
        keys.append(KEY_DETECTOR_DF_LOW_rad)
        keys.append(KEY_DETECTOR_DF_HIGH_rad)
        keys.append(KEY_DETECTOR_HAADF_LOW_rad)
        keys.append(KEY_DETECTOR_HAADF_HIGH_rad)

        return keys

    def defaultValues(self):
        self.beamEnergy_keV = 20.0
        self.beamCurrent_A = 1e-10
        self.time_s = 100.0
        self.beamDiameter_A = 10.0
        self.beamPositionX_A = 0.0
        self.beamPositionY_A = 0.0
        self.beamTilt_deg = 0.0
        self.beamStandardDeviation_A = 3.03030303030303
        self.detectorCrystalAtomSymbol = 'Si'
        self.detectorCrystalThickness_cm = 0.3
        self.detectorCrystalRadius_cm = 0.3
        self.detectorCrystalDistance_cm = 4.0
        self.detectorDeadLayer_A = 200.0
        self.detectorDiffusionLenght_A = 0.5
        self.detectorSurfaceQuality = 1.0
        self.detectorNoise_eV = 50.0
        self.detectorTOA_deg = 40.0
        self.detectorPitch_deg = 90.0
        self.detectorBFLow_rad = 0.0
        self.detectorBFHigh_rad = 0.01
        self.detectorDFLow_rad = 0.02
        self.detectorDFHigh_rad = 0.1
        self.detectorHAADFLow_rad = 0.15
        self.detectorHAADFHigh_rad = 0.3
        self.detectorChannelWidth_eV = 5.0

    def _createExtractMethod(self):
        extractMethods = {}

        extractMethods[KEY_BEAM_ENERGY_keV] = float
        extractMethods[KEY_BEAM_CURRENT_A] = float
        extractMethods[KEY_BEAM_TIME_s] = float
        extractMethods[KEY_BEAM_DIAMETER_A] = float
        extractMethods[KEY_BEAM_POSITION_X_A] = float
        extractMethods[KEY_BEAM_POSITION_Y_A] = float
        extractMethods[KEY_BEAM_TILT_deg] = float
        extractMethods[KEY_BEAM_STANDARD_DEVIATION_A] = float
        extractMethods[KEY_DETECTOR_CRYSTAL_ATOM] = str
        extractMethods[KEY_DETECTOR_CRYSTAL_THICKNESS_cm] = float
        extractMethods[KEY_DETECTOR_CRYSTAL_RADIUS_cm] = float
        extractMethods[KEY_DETECTOR_CRYSTAL_DISTANCE_cm] = float
        extractMethods[KEY_DETECTOR_DEAD_LAYER_A] = float
        extractMethods[KEY_DETECTOR_DIFFUSION_LENGHT_A] = float
        extractMethods[KEY_DETECTOR_SURFACE_QUALITY] = float
        extractMethods[KEY_DETECTOR_NOISE_eV] = float
        extractMethods[KEY_DETECTOR_TOA_deg] = float
        extractMethods[KEY_DETECTOR_CHANNEL_WIDTH_eV] = float
        extractMethods[KEY_DETECTOR_PITCH_deg] = float
        extractMethods[KEY_DETECTOR_BF_LOW_rad] = float
        extractMethods[KEY_DETECTOR_BF_HIGH_RAD] = float
        extractMethods[KEY_DETECTOR_DF_LOW_rad] = float
        extractMethods[KEY_DETECTOR_DF_HIGH_rad] = float
        extractMethods[KEY_DETECTOR_HAADF_LOW_rad] = float
        extractMethods[KEY_DETECTOR_HAADF_HIGH_rad] = float

        return extractMethods

    def read(self, filepath):
        self.version.readFromFile(filepath)

        lines = open(filepath, 'r').readlines()

        extractMethods = self._createExtractMethod()

        for line in lines:
            line = line.strip()

            for key in self._keys:
                if line.startswith(key):
                    items = line.split('=')
                    self._parameters[key] = extractMethods[key](items[-1])

    def write(self, filepath):
        outputFile = open(filepath, 'w')

        self._writeHeader(outputFile)

        self.version.writeLine(outputFile)

        formats = self._createFormats()

        for key in self._createKeys():
            value = formats[key](self._parameters[key])
            if "e-" in value:
                value = value.replace('e-', 'e-0')
            if "e+" in value:
                value = value.replace('e+', 'e+0')

            line = "%s=%s\n" % (key, value)
            outputFile.write(line)

    def _writeHeader(self, outputFile):
        headerLines = [ "********************************************************************************",
                        "***                                MICROSCOPE",
                        "***",
                        "***    BeamEnergy                  = Tension of the collimated electrons",
                        "***    BeamCurrent                 = Current of the electron beam",
                        "***    BeamDiameter                = Diameter at 90% of the electron beam",
                        "***    BeamPosX                    = Position in X of the electron beam",
                        "***    BeamPosY                    = Position in Y of the electron beam",
                        "***    BeamTilt                    = Theta angle of the electron beam (deg)",
                        "***    BeamStandardDeviation       = Standard deviation of the Gaussian distribution of the electrons in the beam",
                        "***    DetectorCrystalAtom         = Atomic symbol, name or number of the detector crystal",
                        "***    DetectorCrystalThickness    = Thickness of the detector crystal",
                        "***    DetectorCrystalRadius       = Radius of the detector crystal",
                        "***    DetectorCrystalDistance     = Distance of the detector crystal to the sample",
                        "***    DetectorDeadLayer           = Thickness of the detector dead layer",
                        "***    DetectorDiffusionLenght     = Diffusion lenght of the detector",
                        "***    DetectorSurfaceQuality      = Surface quality of the detector",
                        "***    DetectorNoise               = Noise at EDS",
                        "***    DetectorTOA                 = Take off angle of the detector (deg)",
                        "***    DetectorPitch               = Phi angle of the detector (deg)",
                        "***    DetectorBFLow               = Bright Field low angle (rad)",
                        "***    DetectorBFHigh              = Bright Field high angle (rad)",
                        "***    DetectorDFLow               = Dark Field low angle (rad)",
                        "***    DetectorDFHigh              = Dark Field high angle (rad)",
                        "***    DetectorHAADFLow            = High Angle Annular Dark Field low angle (rad)",
                        "***    DetectorHAADFHigh           = High Angle Annular Dark Field high angle (rad)",
                        "***",
                        "********************************************************************************"]

        for line in headerLines:
            outputFile.write(line+'\n')

    def _createFormats(self):
        formats = {}

        formats[KEY_BEAM_ENERGY_keV] = lambda value: "%.6f" % (value)
        formats[KEY_BEAM_CURRENT_A] = lambda value: "%.16g" % (value)
        formats[KEY_BEAM_TIME_s] = lambda value: "%.16g" % (value)
        formats[KEY_BEAM_DIAMETER_A] = lambda value: "%.16g" % (value)
        formats[KEY_BEAM_POSITION_X_A] = lambda value: reduceAfterDot("%.6f" % (value))
        formats[KEY_BEAM_POSITION_Y_A] = lambda value: reduceAfterDot("%.6f" % (value))
        formats[KEY_BEAM_TILT_deg] = lambda value: "%.6f" % (value)
        formats[KEY_BEAM_STANDARD_DEVIATION_A] = lambda value: reduceAfterDot("%.6g" % (value))
        formats[KEY_DETECTOR_CRYSTAL_ATOM] = lambda value: "%s" % (value)
        formats[KEY_DETECTOR_CRYSTAL_THICKNESS_cm] = lambda value: "%.6f" % (value)
        formats[KEY_DETECTOR_CRYSTAL_RADIUS_cm] = lambda value: reduceAfterDot("%.6f" % (value))
        formats[KEY_DETECTOR_CRYSTAL_DISTANCE_cm] = lambda value: reduceAfterDot("%.6f" % (value))
        formats[KEY_DETECTOR_DEAD_LAYER_A] = lambda value: reduceAfterDot("%.6f" % (value))
        formats[KEY_DETECTOR_DIFFUSION_LENGHT_A] = lambda value: reduceAfterDot("%.6f" % (value))
        formats[KEY_DETECTOR_SURFACE_QUALITY] = lambda value: "%.6f" % (value)
        formats[KEY_DETECTOR_NOISE_eV] = lambda value: reduceAfterDot("%.6f" % (value))
        formats[KEY_DETECTOR_TOA_deg] = lambda value: "%.6f" % (value)
        formats[KEY_DETECTOR_CHANNEL_WIDTH_eV] = lambda value: "%.6f" % (value)
        formats[KEY_DETECTOR_PITCH_deg] = lambda value: "%.6f" % (value)
        formats[KEY_DETECTOR_BF_LOW_rad] = lambda value: "%.6f" % (value)
        formats[KEY_DETECTOR_BF_HIGH_RAD] = lambda value: "%.6f" % (value)
        formats[KEY_DETECTOR_DF_LOW_rad] = lambda value: "%.6f" % (value)
        formats[KEY_DETECTOR_DF_HIGH_rad] = lambda value: "%.6f" % (value)
        formats[KEY_DETECTOR_HAADF_LOW_rad] = lambda value: "%.6f" % (value)
        formats[KEY_DETECTOR_HAADF_HIGH_rad] = lambda value: "%.6f" % (value)

        return formats

    @property
    def version(self):
        return self._version
    @version.setter
    def version(self, version):
        self._version = version

    @property
    def beamEnergy_keV(self):
        return self._parameters[KEY_BEAM_ENERGY_keV]
    @beamEnergy_keV.setter
    def beamEnergy_keV(self, beamEnergy_keV):
        self._parameters[KEY_BEAM_ENERGY_keV] = beamEnergy_keV

    @property
    def beamCurrent_A(self):
        return self._parameters[KEY_BEAM_CURRENT_A]
    @beamCurrent_A.setter
    def beamCurrent_A(self, beamCurrent_A):
        self._parameters[KEY_BEAM_CURRENT_A] = beamCurrent_A

    @property
    def time_s(self):
        return self._parameters[KEY_BEAM_TIME_s]
    @time_s.setter
    def time_s(self, time_s):
        self._parameters[KEY_BEAM_TIME_s] = time_s

    @property
    def beamDiameter_A(self):
        return self._parameters[KEY_BEAM_DIAMETER_A]
    @beamDiameter_A.setter
    def beamDiameter_A(self, beamDiameter_A):
        self._parameters[KEY_BEAM_DIAMETER_A] = beamDiameter_A

    @property
    def beamPositionX_A(self):
        return self._parameters[KEY_BEAM_POSITION_X_A]
    @beamPositionX_A.setter
    def beamPositionX_A(self, beamPositionX_A):
        self._parameters[KEY_BEAM_POSITION_X_A] = beamPositionX_A

    @property
    def beamPositionY_A(self):
        return self._parameters[KEY_BEAM_POSITION_Y_A]
    @beamPositionY_A.setter
    def beamPositionY_A(self, beamPositionY_A):
        self._parameters[KEY_BEAM_POSITION_Y_A] = beamPositionY_A

    @property
    def beamTilt_deg(self):
        return self._parameters[KEY_BEAM_TILT_deg]
    @beamTilt_deg.setter
    def beamTilt_deg(self, beamTilt_deg):
        self._parameters[KEY_BEAM_TILT_deg] = beamTilt_deg

    @property
    def beamStandardDeviation_A(self):
        return self._parameters[KEY_BEAM_STANDARD_DEVIATION_A]
    @beamStandardDeviation_A.setter
    def beamStandardDeviation_A(self, beamStandardDeviation_A):
        self._parameters[KEY_BEAM_STANDARD_DEVIATION_A] = beamStandardDeviation_A

    @property
    def detectorCrystalAtomSymbol(self):
        return self._parameters[KEY_DETECTOR_CRYSTAL_ATOM]
    @detectorCrystalAtomSymbol.setter
    def detectorCrystalAtomSymbol(self, detectorCrystalAtomSymbol):
        self._parameters[KEY_DETECTOR_CRYSTAL_ATOM] = detectorCrystalAtomSymbol

    @property
    def detectorCrystalThickness_cm(self):
        return self._parameters[KEY_DETECTOR_CRYSTAL_THICKNESS_cm]
    @detectorCrystalThickness_cm.setter
    def detectorCrystalThickness_cm(self, detectorCrystalThickness_cm):
        self._parameters[KEY_DETECTOR_CRYSTAL_THICKNESS_cm] = detectorCrystalThickness_cm

    @property
    def detectorCrystalRadius_cm(self):
        return self._parameters[KEY_DETECTOR_CRYSTAL_RADIUS_cm]
    @detectorCrystalRadius_cm.setter
    def detectorCrystalRadius_cm(self, detectorCrystalRadius_cm):
        self._parameters[KEY_DETECTOR_CRYSTAL_RADIUS_cm] = detectorCrystalRadius_cm

    @property
    def detectorCrystalDistance_cm(self):
        return self._parameters[KEY_DETECTOR_CRYSTAL_DISTANCE_cm]
    @detectorCrystalDistance_cm.setter
    def detectorCrystalDistance_cm(self, detectorCrystalDistance_cm):
        self._parameters[KEY_DETECTOR_CRYSTAL_DISTANCE_cm] = detectorCrystalDistance_cm

    @property
    def detectorDeadLayer_A(self):
        return self._parameters[KEY_DETECTOR_DEAD_LAYER_A]
    @detectorDeadLayer_A.setter
    def detectorDeadLayer_A(self, detectorDeadLayer_A):
        self._parameters[KEY_DETECTOR_DEAD_LAYER_A] = detectorDeadLayer_A

    @property
    def detectorDiffusionLenght_A(self):
        return self._parameters[KEY_DETECTOR_DIFFUSION_LENGHT_A]
    @detectorDiffusionLenght_A.setter
    def detectorDiffusionLenght_A(self, detectorDiffusionLenght_A):
        self._parameters[KEY_DETECTOR_DIFFUSION_LENGHT_A] = detectorDiffusionLenght_A

    @property
    def detectorSurfaceQuality(self):
        return self._parameters[KEY_DETECTOR_SURFACE_QUALITY]
    @detectorSurfaceQuality.setter
    def detectorSurfaceQuality(self, detectorSurfaceQuality):
        self._parameters[KEY_DETECTOR_SURFACE_QUALITY] = detectorSurfaceQuality

    @property
    def detectorNoise_eV(self):
        return self._parameters[KEY_DETECTOR_NOISE_eV]
    @detectorNoise_eV.setter
    def detectorNoise_eV(self, detectorNoise_eV):
        self._parameters[KEY_DETECTOR_NOISE_eV] = detectorNoise_eV

    @property
    def detectorTOA_deg(self):
        return self._parameters[KEY_DETECTOR_TOA_deg]
    @detectorTOA_deg.setter
    def detectorTOA_deg(self, detectorTOA_deg):
        self._parameters[KEY_DETECTOR_TOA_deg] = detectorTOA_deg

    @property
    def detectorAzimuthalAngle_deg(self):
        return self._parameters[KEY_DETECTOR_PITCH_deg]
    @detectorAzimuthalAngle_deg.setter
    def detectorAzimuthalAngle_deg(self, detectorAzimuthalAngle_deg):
        self._parameters[KEY_DETECTOR_PITCH_deg] = detectorAzimuthalAngle_deg

    @property
    def detectorChannelWidth_eV(self):
        return self._parameters[KEY_DETECTOR_CHANNEL_WIDTH_eV]
    @detectorChannelWidth_eV.setter
    def detectorChannelWidth_eV(self, detectorChannelWidth_eV):
        self._parameters[KEY_DETECTOR_CHANNEL_WIDTH_eV] = detectorChannelWidth_eV

    @property
    def detectorPitch_deg(self):
        return self._parameters[KEY_DETECTOR_PITCH_deg]
    @detectorPitch_deg.setter
    def detectorPitch_deg(self, detectorPitch_deg):
        self._parameters[KEY_DETECTOR_PITCH_deg] = detectorPitch_deg

    @property
    def detectorBFLow_rad(self):
        return self._parameters[KEY_DETECTOR_BF_LOW_rad]
    @detectorBFLow_rad.setter
    def detectorBFLow_rad(self, detectorBFLow_rad):
        self._parameters[KEY_DETECTOR_BF_LOW_rad] = detectorBFLow_rad

    @property
    def detectorBFHigh_rad(self):
        return self._parameters[KEY_DETECTOR_BF_HIGH_RAD]
    @detectorBFHigh_rad.setter
    def detectorBFHigh_rad(self, detectorBFHigh_rad):
        self._parameters[KEY_DETECTOR_BF_HIGH_RAD] = detectorBFHigh_rad

    @property
    def detectorDFLow_rad(self):
        return self._parameters[KEY_DETECTOR_DF_LOW_rad]
    @detectorDFLow_rad.setter
    def detectorDFLow_rad(self, detectorDFLow_rad):
        self._parameters[KEY_DETECTOR_DF_LOW_rad] = detectorDFLow_rad

    @property
    def detectorDFHigh_rad(self):
        return self._parameters[KEY_DETECTOR_DF_HIGH_rad]
    @detectorDFHigh_rad.setter
    def detectorDFHigh_rad(self, detectorDFHigh_rad):
        self._parameters[KEY_DETECTOR_DF_HIGH_rad] = detectorDFHigh_rad

    @property
    def detectorHAADFLow_rad(self):
        return self._parameters[KEY_DETECTOR_HAADF_LOW_rad]
    @detectorHAADFLow_rad.setter
    def detectorHAADFLow_rad(self, detectorHAADFLow_rad):
        self._parameters[KEY_DETECTOR_HAADF_LOW_rad] = detectorHAADFLow_rad

    @property
    def detectorHAADFHigh_rad(self):
        return self._parameters[KEY_DETECTOR_HAADF_HIGH_rad]
    @detectorHAADFHigh_rad.setter
    def detectorHAADFHigh_rad(self, detectorHAADFHigh_rad):
        self._parameters[KEY_DETECTOR_HAADF_HIGH_rad] = detectorHAADFHigh_rad
