#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.SimulationParameters
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

MCXRay simulation parameters input file.
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
import pymcxray.FileFormat.MCXRayModel as MCXRayModel
import pymcxray.FileFormat.Version as Version

# Globals and constants variables.
KEY_BASE_FILENAME = "BaseFileName"
KEY_NUMBER_ELECTRONS = "ElectronNbr"
KEY_NUMBER_PHOTONS = "PhotonNbr"
KEY_NUMBER_WINDOWS = "WindowNbr"
KEY_NUMBER_FILMS_X = "FilmNbrX"
KEY_NUMBER_FILMS_Y = "FilmNbrY"
KEY_NUMBER_FILMS_Z = "FilmNbrZ"
KEY_NUMBER_CHANNELS = "SpectraChannel"
KEY_ENERGY_CHANNEL_WIDTH = "EnergyChannelWidth"
KEY_SPECTRA_INTERPOLATION_MODEL = "SpectraInterpolation"
KEY_VOXEL_SIMPLIFICATION = "VoxelSimplification"
KEY_ELASTIC_CROSS_SECTION_SCALING_FACTOR = "ElasticCrossSectionScalingFactor"
KEY_ENERGY_LOSS_SCALING_FACTOR = "EnergyLossScalingFactor"

class SimulationParameters(object):
    def __init__(self):
        self.version = copy.deepcopy(Version.CURRENT_VERSION)

        self._keys = self._createKeys()

        self._parameters = {}

        self.defaultValues()

    def _createKeys(self):
        keys = []

        keys.append(KEY_BASE_FILENAME)
        keys.append(KEY_NUMBER_ELECTRONS)
        keys.append(KEY_NUMBER_PHOTONS)
        keys.append(KEY_NUMBER_WINDOWS)
        keys.append(KEY_NUMBER_FILMS_X)
        keys.append(KEY_NUMBER_FILMS_Y)
        keys.append(KEY_NUMBER_FILMS_Z)
        if self.version == Version.BEFORE_VERSION:
            keys.append(KEY_NUMBER_CHANNELS)
        else:
            keys.append(KEY_ENERGY_CHANNEL_WIDTH)
        keys.append(KEY_SPECTRA_INTERPOLATION_MODEL)
        keys.append(KEY_VOXEL_SIMPLIFICATION)
        if self.version >= Version.VERSION_1_4_4:
            keys.append(KEY_ELASTIC_CROSS_SECTION_SCALING_FACTOR)
            keys.append(KEY_ENERGY_LOSS_SCALING_FACTOR)

        return keys

    def defaultValues(self):
        baseFilenameRef = r"Results\McXRay"
        self.baseFilename = baseFilenameRef
        self.numberElectrons = 1000
        self.numberPhotons = 10000
        self.numberWindows = 64
        self.numberFilmsX = 128
        self.numberFilmsY = 128
        self.numberFilmsZ = 128
        self.numberChannels = 1024
        self.energyChannelWidth_eV = 5.0
        self.spectrumInterpolationModel = MCXRayModel.SpectrumInterpolationModel.TYPE_LINEAR_DOUBLE
        self.voxelSimplification = None
        self.elasticCrossSectionScalingFactor = 1.0
        self.energyLossScalingFactor = 1.0

    def _createExtractMethod(self):
        extractMethods = {}

        extractMethods[KEY_BASE_FILENAME] = str
        extractMethods[KEY_NUMBER_ELECTRONS] = int
        extractMethods[KEY_NUMBER_PHOTONS] = int
        extractMethods[KEY_NUMBER_WINDOWS] = int
        extractMethods[KEY_NUMBER_FILMS_X] = int
        extractMethods[KEY_NUMBER_FILMS_Y] = int
        extractMethods[KEY_NUMBER_FILMS_Z] = int
        extractMethods[KEY_NUMBER_CHANNELS] = int
        extractMethods[KEY_ENERGY_CHANNEL_WIDTH] = float
        extractMethods[KEY_SPECTRA_INTERPOLATION_MODEL] = self._extractSpectrumInterpolationModel
        extractMethods[KEY_VOXEL_SIMPLIFICATION] = bool
        extractMethods[KEY_ELASTIC_CROSS_SECTION_SCALING_FACTOR] = float
        extractMethods[KEY_ENERGY_LOSS_SCALING_FACTOR] = float

        return extractMethods

    def _createFormatMethod(self):
        fromatMethods = {}

        fromatMethods[KEY_BASE_FILENAME] = "%s"
        fromatMethods[KEY_NUMBER_ELECTRONS] = "%i"
        fromatMethods[KEY_NUMBER_PHOTONS] = "%i"
        fromatMethods[KEY_NUMBER_WINDOWS] = "%i"
        fromatMethods[KEY_NUMBER_FILMS_X] = "%i"
        fromatMethods[KEY_NUMBER_FILMS_Y] = "%i"
        fromatMethods[KEY_NUMBER_FILMS_Z] = "%i"
        fromatMethods[KEY_NUMBER_CHANNELS] = "%i"
        fromatMethods[KEY_ENERGY_CHANNEL_WIDTH] = "%s"
        fromatMethods[KEY_SPECTRA_INTERPOLATION_MODEL] = "%s"
        fromatMethods[KEY_VOXEL_SIMPLIFICATION] = "%s"
        fromatMethods[KEY_ELASTIC_CROSS_SECTION_SCALING_FACTOR] = "%.5f"
        fromatMethods[KEY_ENERGY_LOSS_SCALING_FACTOR] = "%.5f"

        return fromatMethods

    def _extractSpectrumInterpolationModel(self, text):
        model = MCXRayModel.SpectrumInterpolationModel(int(text))
        return model

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

        formatMethods = self._createFormatMethod()
        keys = self._createKeys()
        for key in keys:
            if key == KEY_SPECTRA_INTERPOLATION_MODEL:
                value = formatMethods[key] % (self._parameters[key].getModel())
            else:
                value = formatMethods[key] % (self._parameters[key])
            if value is not None and value != "None":
                line = "%s=%s\n" % (key, value)
                outputFile.write(line)

    def _writeHeader(self, outputFile):
        if self._parameters[KEY_VOXEL_SIMPLIFICATION] is not None:
            headerLines = [ "********************************************************************************",
                            "***                           SIMULATION PARAMETERS",
                            "***",
                            "***    BaseFileName         = All output files will be named using this term",
                            "***    ElectronNbr          = Total number of electrons to simulate",
                            "***    PhotonNbr            = Total number of photons to simulate in EDS",
                            "***    WindowNbr            = Number of energy windows in PhiRo computations",
                            "***    FilmNbrX             = Number of X layers in PhiRo computations",
                            "***    FilmNbrY             = Number of Y layers in PhiRo computations",
                            "***    FilmNbrZ             = Number of Z layers in PhiRo computations",
                            "***    SpectraChannel       = Number of channels in spectraa",
                            "***    SpectraInterpolation = Interpolation type for spectras",
                            "***    VoxelSimplification  = Use only middle voxel of trajectories to store energy",
                            "***",
                            "********************************************************************************"]
        elif self.version == Version.BEFORE_VERSION:
            headerLines = [ "********************************************************************************",
                            "***                           SIMULATION PARAMETERS",
                            "***",
                            "***    BaseFileName         = All output files will be named using this term",
                            "***    ElectronNbr          = Total number of electrons to simulate",
                            "***    PhotonNbr            = Total number of photons to simulate in EDS",
                            "***    WindowNbr            = Number of energy windows in PhiRo computations",
                            "***    FilmNbrX             = Number of X layers in PhiRo computations",
                            "***    FilmNbrY             = Number of Y layers in PhiRo computations",
                            "***    FilmNbrZ             = Number of Z layers in PhiRo computations",
                            "***    SpectraChannel       = Number of channels in spectraa",
                            "***    SpectraInterpolation = Interpolation type for spectras",
                            "***",
                            "********************************************************************************"]
        elif self.version >= Version.VERSION_1_4_4:
            headerLines = [ "********************************************************************************",
                            "***                           SIMULATION PARAMETERS",
                            "***",
                            "***    BaseFileName         = All output files will be named using this term",
                            "***    ElectronNbr          = Total number of electrons to simulate",
                            "***    PhotonNbr            = Total number of photons to simulate in EDS",
                            "***    WindowNbr            = Number of energy windows in Spectrum computations",
                            "***    FilmNbrX             = Number of X layers in Spectrum computations",
                            "***    FilmNbrY             = Number of Y layers in Spectrum computations",
                            "***    FilmNbrZ             = Number of Z layers in Spectrum computations",
                            "***    EnergyChannelWidth in eV",
                            "***    SpectraInterpolation = Interpolation type for spectra",
                            "***    ElasticCrossSectionScalingFactor",
                            "***    EnergyLossScalingFactor",
                            "***",
                            "********************************************************************************"]
        else:
            headerLines = [ "********************************************************************************",
                            "***                           SIMULATION PARAMETERS",
                            "***",
                            "***    BaseFileName         = All output files will be named using this term",
                            "***    ElectronNbr          = Total number of electrons to simulate",
                            "***    PhotonNbr            = Total number of photons to simulate in EDS",
                            "***    WindowNbr            = Number of energy windows in Spectrum computations",
                            "***    FilmNbrX             = Number of X layers in Spectrum computations",
                            "***    FilmNbrY             = Number of Y layers in Spectrum computations",
                            "***    FilmNbrZ             = Number of Z layers in Spectrum computations",
                            "***    EnergyChannelWidth in eV",
                            "***    SpectraInterpolation = Interpolation type for spectra",
                            "***",
                            "********************************************************************************"]

        for line in headerLines:
            outputFile.write(line+'\n')

    @property
    def version(self):
        return self._version
    @version.setter
    def version(self, version):
        self._version = version

    @property
    def baseFilename(self):
        return self._parameters[KEY_BASE_FILENAME]
    @baseFilename.setter
    def baseFilename(self, baseFilename):
        self._parameters[KEY_BASE_FILENAME] = baseFilename

    @property
    def numberElectrons(self):
        return self._parameters[KEY_NUMBER_ELECTRONS]
    @numberElectrons.setter
    def numberElectrons(self, numberElectrons):
        self._parameters[KEY_NUMBER_ELECTRONS] = numberElectrons

    @property
    def numberPhotons(self):
        return self._parameters[KEY_NUMBER_PHOTONS]
    @numberPhotons.setter
    def numberPhotons(self, numberPhotons):
        self._parameters[KEY_NUMBER_PHOTONS] = numberPhotons

    @property
    def numberWindows(self):
        return self._parameters[KEY_NUMBER_WINDOWS]
    @numberWindows.setter
    def numberWindows(self, numberWindows):
        self._parameters[KEY_NUMBER_WINDOWS] = numberWindows

    @property
    def numberFilmsX(self):
        return self._parameters[KEY_NUMBER_FILMS_X]
    @numberFilmsX.setter
    def numberFilmsX(self, numberFilmsX):
        self._parameters[KEY_NUMBER_FILMS_X] = numberFilmsX

    @property
    def numberFilmsY(self):
        return self._parameters[KEY_NUMBER_FILMS_Y]
    @numberFilmsY.setter
    def numberFilmsY(self, numberFilmsY):
        self._parameters[KEY_NUMBER_FILMS_Y] = numberFilmsY

    @property
    def numberFilmsZ(self):
        return self._parameters[KEY_NUMBER_FILMS_Z]
    @numberFilmsZ.setter
    def numberFilmsZ(self, numberFilmsZ):
        self._parameters[KEY_NUMBER_FILMS_Z] = numberFilmsZ

    @property
    def numberChannels(self):
        return self._parameters[KEY_NUMBER_CHANNELS]
    @numberChannels.setter
    def numberChannels(self, numberChannels):
        self._parameters[KEY_NUMBER_CHANNELS] = numberChannels

    @property
    def energyChannelWidth_eV(self):
        return self._parameters[KEY_ENERGY_CHANNEL_WIDTH]
    @energyChannelWidth_eV.setter
    def energyChannelWidth_eV(self, energyChannelWidth_eV):
        self._parameters[KEY_ENERGY_CHANNEL_WIDTH] = energyChannelWidth_eV

    @property
    def spectrumInterpolationModel(self):
        return self._parameters[KEY_SPECTRA_INTERPOLATION_MODEL].getModel()
    @spectrumInterpolationModel.setter
    def spectrumInterpolationModel(self, spectrumInterpolationModel):
        self._parameters[KEY_SPECTRA_INTERPOLATION_MODEL] = MCXRayModel.SpectrumInterpolationModel(spectrumInterpolationModel)

    @property
    def voxelSimplification(self):
        return self._parameters.get(KEY_VOXEL_SIMPLIFICATION, None)
    @voxelSimplification.setter
    def voxelSimplification(self, voxelSimplification):
        self._parameters[KEY_VOXEL_SIMPLIFICATION] = voxelSimplification

    @property
    def elasticCrossSectionScalingFactor(self):
        return self._parameters[KEY_ELASTIC_CROSS_SECTION_SCALING_FACTOR]
    @elasticCrossSectionScalingFactor.setter
    def elasticCrossSectionScalingFactor(self, elasticCrossSectionScalingFactor):
        self._parameters[KEY_ELASTIC_CROSS_SECTION_SCALING_FACTOR] = elasticCrossSectionScalingFactor

    @property
    def energyLossScalingFactor(self):
        return self._parameters[KEY_ENERGY_LOSS_SCALING_FACTOR]
    @energyLossScalingFactor.setter
    def energyLossScalingFactor(self, energyLossScalingFactor):
        self._parameters[KEY_ENERGY_LOSS_SCALING_FACTOR] = energyLossScalingFactor
