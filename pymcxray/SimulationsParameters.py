#!/usr/bin/env python
"""
.. py:currentmodule:: SimulationsParameters
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Simulations parameters
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2012 Hendrix Demers"
__license__ = ""

# Standard library modules.
import logging
import csv

# Third party modules.

# Local modules.
import pymcxray.multipleloop as multipleloop

# Project modules

# Globals and constants variables.
PARAMETER_INCIDENT_ENERGY_keV = "incidentEnergy"
PARAMETER_NUMBER_ELECTRONS = "numberElectrons"
PARAMETER_NUMBER_XRAYS = "numberXrays"

PARAMETER_REPETITION = "Repetition"

PARAMETER_SPHERE_DIAMETER_nm = "sphereDiameter"
PARAMETER_SPHERE_DEPTH_FRACTION_RADIUS = "sphereDepthFractionRadius"
PARAMETER_BOX_SIDE_nm = "boxSide"
PARAMETER_BOX_WIDTH_nm = "boxWidth"
PARAMETER_BOX_DEPTH_nm = "boxDepth"
PARAMETER_FILM_THICKNESS_nm = "filmThickness"

PARAMETER_MEAN_NUMBER_COLLISIONS = "meanNumberCollisions"

PARAMETER_SPECIMEN = "specimen"
PARAMETER_SAMPLE_NAME = "sampleName"
PARAMETER_ELASTIC_CROSS_SECTION_SCALING_FACTOR = "elasticCrossSectionScalingFactor"
PARAMETER_ENERGY_LOSS_SCALING_FACTOR = "energyLossScalingFactor"

PARAMETER_TIME_s = "time"
PARAMETER_CURRENT_nA = "current"
PARAMETER_ATOMIC_NUMBER = "atomicNumber"
PARAMETER_BEAM_DIAMETER_nm = "beamDiameter"
PARAMETER_BEAM_TILT_deg = "beamTilt"
PARAMETER_BEAM_POSITION_nm = "beamPosition"

PARAMETER_DETECTOR_DISTANCE_cm = "detectorDistance"
PARAMETER_DETECTOR_RADIUS_cm = "detectorRadius"
PARAMETER_DETECTOR_THICKNESS_cm = "detectorThickness"
PARAMETER_DETECTOR_NOISE_eV = "detectorNoise"
PARAMETER_DETECTOR_CHANNEL_WIDTH_eV = "detectorChannelWidth"
PARAMETER_TOA_deg = "detectorTOA"
PARAMETER_DETECTOR_AZIMUTHAL_ANGLE_deg = "azimuthalAngle_deg"
PARAMETER_NUMBER_WINDOWS = "numberBackgroundWindows"

PARAMETER_NUMBER_LAYERS_X = "numberLayersX"
PARAMETER_NUMBER_LAYERS_Y = "numberLayersY"
PARAMETER_NUMBER_LAYERS_Z = "numberLayersZ"

PARAMETER_WEIGHT_FRACTION = "weightFraction"
PARAMETER_WEIGHT_FRACTIONS = "weightFractions"
PARAMETER_ATOMIC_FRACTION = "atomicFraction"
PARAMETER_ATOMIC_FRACTIONs = "atomicFractions"
PARAMETER_ELEMENTS = "elements"
PARAMETER_USER_MASS_DENSITY = "userMassDensity"

PARAMETER_TRACER_ATOMIC_NUMBER = "tracerAtomicNumber"
PARAMETER_TRACER_THICKNESS_nm = "tracerThickness"
PARAMETER_TRACER_LINE = "tracerLine"

PARAMETER_MODEL_SAMPLE_ENERGY_LOSS = "modelSampleEnergyLoss"
PARAMETER_MODEL_XRAY_CHARACTERISTIC = "modelXrayCharacteristic"
PARAMETER_MODEL_XRAY_BREMSSTRAHLUNG = "modelXrayBremsstrahlung"
PARAMETER_MODEL_ATOM_CROSS_SECTION = "modelAtomCrossSection"
PARAMETER_MODEL_ATOM_COLLISION = "modelAtomCollision"
PARAMETER_MODEL_ATOM_MAC = "modelAtomMac"

class SimulationsParameters(dict):
    def __init__(self):
        self._variedParameters = {}
        self._fixedParameters = {}
        self._computedParameters = set()

    def addVaried(self, parameterKey, values):
        if parameterKey not in self._variedParameters:
            self._variedParameters[parameterKey] = []

        self._variedParameters[parameterKey].extend(values)

        self._removeDuplicated(self._variedParameters[parameterKey])

    def _removeDuplicated(self, parameters):
        numberBefore = len(parameters)

        try:
            parameters = list(set(parameters))
        except TypeError:
            pass

        numberAfter = len(parameters)
        numberDuplicated = numberBefore - numberAfter
        if numberDuplicated > 0:
            logging.info("Removed %i duplicated items", numberDuplicated)

    def addFixed(self, parameterKey, value):
        self._fixedParameters[parameterKey] = value

    def addCompute(self, parameterKey):
        self._computedParameters.add(parameterKey)

    def getAllSimulationParameters(self):
        parametersList = {}
        parametersList.update(self._variedParameters)
        parametersList.update(self._fixedParameters)

        allValues, names, dummyVaried = multipleloop.combine(parametersList)

        experiments = []

        for values in allValues:
            experiment = dict(zip(names, values))

            for parameterKey in self._computedParameters:
                if parameterKey == PARAMETER_NUMBER_XRAYS:
                    value = self.computeNumberXrays(experiment)
                    experiment[PARAMETER_NUMBER_XRAYS] = value

            experiments.append(experiment)

        return experiments

    def computeNumberXrays(self, experiment):
        reader = csv.reader(open(self.computeNumberXraysFilepath, 'r'))

        next(reader)

        for row in reader:
            if float(row[0]) == float(experiment[PARAMETER_INCIDENT_ENERGY_keV]) and float(row[1]) == float(experiment[PARAMETER_SPHERE_DIAMETER_nm]):
                counts_1_sAsr = float(row[2])
                break
        else:
            logging.warning("counts_1_sAsr not found for these conditions.")
            return 0

        current_A = experiment[PARAMETER_CURRENT_nA]*1.0e-9
        time_s = experiment[PARAMETER_TIME_s]
        solidAngle_sr =  0.0351945099176

        numberXrays = int(counts_1_sAsr*current_A*time_s*solidAngle_sr)
        return numberXrays

    def getVariedParameterLabels(self):
        return sorted(self._variedParameters.keys())

    @property
    def computeNumberXraysFilepath(self):
        return self._computeNumberXraysFilepath
    @computeNumberXraysFilepath.setter
    def computeNumberXraysFilepath(self, filepath):
        self._computeNumberXraysFilepath = filepath

    @property
    def fixedParameters(self):
        return self._fixedParameters

    @property
    def variedParameters(self):
        return self._variedParameters

class SimulationsParametersFixed(object):
    def __init__(self):
        self._experiments = []

    def addExperiment(self, experiment):
        self._experiments.append(experiment)

    def getAllSimulationParameters(self):
        return self._experiments
