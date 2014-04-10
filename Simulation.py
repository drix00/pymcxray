#!/usr/bin/env python
"""
.. py:currentmodule:: Simulation
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

MCXRay simulation parameters.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2012 Hendrix Demers"
__license__ = ""

# Standard library modules.
import logging
import os.path

# Third party modules.
import numpy as np

# Local modules.
from DatabasesTools.ElementProperties import getAtomicMass_g_mol

# Project modules
import pymcxray.AtomData as AtomData
import pymcxray.FileFormat.SimulationInputs as SimulationInputs
import pymcxray.FileFormat.Specimen as Specimen
import pymcxray.FileFormat.Region as Region
import pymcxray.FileFormat.RegionType as RegionType
import pymcxray.FileFormat.RegionDimensions as RegionDimensions
import pymcxray.FileFormat.Element as Element
import pymcxray.FileFormat.Models as Models
import pymcxray.FileFormat.MicroscopeParameters as MicroscopeParameters
import pymcxray.FileFormat.SimulationParameters as SimulationParameters
import pymcxray.FileFormat.ResultsParameters as ResultsParameters

from pymcxray.SimulationsParameters import PARAMETER_INCIDENT_ENERGY_keV, PARAMETER_NUMBER_ELECTRONS, \
PARAMETER_NUMBER_XRAYS, PARAMETER_TIME_s, PARAMETER_CURRENT_nA, PARAMETER_BEAM_DIAMETER_nm, PARAMETER_BEAM_TILT_deg, PARAMETER_BEAM_POSITION_nm, \
PARAMETER_DETECTOR_DISTANCE_cm, PARAMETER_DETECTOR_RADIUS_cm, PARAMETER_DETECTOR_THICKNESS_cm, \
PARAMETER_DETECTOR_NOISE_eV, PARAMETER_DETECTOR_CHANNEL_WIDTH_eV, PARAMETER_TOA_deg, PARAMETER_DETECTOR_AZIMUTHAL_ANGLE_deg, PARAMETER_NUMBER_WINDOWS, \
PARAMETER_ELASTIC_CROSS_SECTION_SCALING_FACTOR, PARAMETER_ENERGY_LOSS_SCALING_FACTOR, PARAMETER_REPETITION


# Globals and constants variables.

def createPureBulkSample(atomicNumber):
    specimen = Specimen.Specimen()

    specimen.name = AtomData.getAtomSymbol(atomicNumber)

    specimen.numberRegions = 1
    region = Region.Region()
    region.numberElements = 1
    element = Element.Element(atomicNumber)
    region.elements.append(element)
    region.regionType = RegionType.REGION_TYPE_BOX
    parameters = [-10000000000.0, 10000000000.0, -10000000000.0, 10000000000.0, 0.0, 20000000000.0]
    region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
    specimen.regions.append(region)

    return specimen

def createAlloyBulkSample(elements, sampleName=None):
    specimen = Specimen.Specimen()

    specimen.numberRegions = 1
    region = Region.Region()
    region.numberElements = len(elements)
    name = ""

    for atomicNumber, weightFraction in elements:
        name += "%s%0.6f" % (AtomData.getAtomSymbol(atomicNumber), weightFraction)
        element = Element.Element(atomicNumber, massFraction=weightFraction)
        region.elements.append(element)

    if sampleName is None:
        specimen.name = name
    else:
        specimen.name = sampleName

    region.regionType = RegionType.REGION_TYPE_BOX
    parameters = [-10000000000.0, 10000000000.0, -10000000000.0, 10000000000.0, 0.0, 20000000000.0]
    region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
    specimen.regions.append(region)

    return specimen

def createAlloyThinFilm(elements, filmThickness_nm):
    specimen = Specimen.Specimen()

    specimen.numberRegions = 1
    region = Region.Region()
    region.numberElements = len(elements)
    name = ""

    for atomicNumber, weightFraction in elements:
        name += "%s%i" % (AtomData.getAtomSymbol(atomicNumber), weightFraction*100)
        element = Element.Element(atomicNumber, massFraction=weightFraction)
        region.elements.append(element)

    filmThickness_A = filmThickness_nm*10.0
    name += "T%iA" % (filmThickness_A)

    specimen.name = name
    region.regionType = RegionType.REGION_TYPE_BOX
    parameters = [-10000000000.0, 10000000000.0, -10000000000.0, 10000000000.0, 0.0, filmThickness_A]
    region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
    specimen.regions.append(region)

    return specimen

def createFilmOverSubstrate(atomicNumberFilm, atomicNumberSubstrate,
                            filmThickness_nm=10.0):
    specimen = Specimen.Specimen()

    symbolFilm = AtomData.getAtomSymbol(atomicNumberFilm)
    symbolSubstrate = AtomData.getAtomSymbol(atomicNumberSubstrate)
    name = "%s_T%inm_%s" % (symbolFilm, filmThickness_nm, symbolSubstrate)
    specimen.name = name

    specimen.numberRegions = 2
    region = Region.Region()
    region.numberElements = 1
    element = Element.Element(atomicNumberSubstrate)
    region.elements.append(element)
    region.regionType = RegionType.REGION_TYPE_BOX
    parameters = [-10000000000.0, 10000000000.0, -10000000000.0, 10000000000.0, 0.0, 20000000000.0]
    region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
    specimen.regions.append(region)

    region = Region.Region()
    region.numberElements = 1
    element = Element.Element(atomicNumberFilm)
    region.elements.append(element)
    region.regionType = RegionType.REGION_TYPE_BOX
    filmThickness_A = filmThickness_nm*1.0e1
    parameters = [-10000000000.0, 10000000000.0, -10000000000.0, 10000000000.0, 0.0, filmThickness_A]
    region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
    specimen.regions.append(region)

    return specimen

def createFilmInSubstrate(atomicNumberFilm, atomicNumberSubstrate,
                            filmThickness_nm, filmTopPositionZ_nm):
    specimen = Specimen.Specimen()

    symbolFilm = AtomData.getAtomSymbol(atomicNumberFilm)
    symbolSubstrate = AtomData.getAtomSymbol(atomicNumberSubstrate)
    name = "%s_T%inm_Z%inm_%s" % (symbolFilm, filmThickness_nm, filmTopPositionZ_nm, symbolSubstrate)
    specimen.name = name

    specimen.numberRegions = 2

    region = Region.Region()
    region.numberElements = 1
    element = Element.Element(atomicNumberSubstrate)
    region.elements.append(element)
    region.regionType = RegionType.REGION_TYPE_BOX
    parameters = [-10000000000.0, 10000000000.0, -10000000000.0, 10000000000.0, 0.0, 20000000000.0]
    region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
    specimen.regions.append(region)

    region = Region.Region()
    region.numberElements = 1
    element = Element.Element(atomicNumberFilm)
    region.elements.append(element)
    region.regionType = RegionType.REGION_TYPE_BOX
    filmThickness_A = filmThickness_nm*1.0e1
    filmTopPositionZ_A = filmTopPositionZ_nm*1.0e1
    parameters = [-10000000000.0, 10000000000.0, -10000000000.0, 10000000000.0, filmTopPositionZ_A, filmTopPositionZ_A+filmThickness_A]
    region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
    specimen.regions.append(region)

    return specimen

def createPhirhozSpecimens(atomicNumberTracer, atomicNumberMatrix, tracerThickness_nm, maximumThickness_nm):
    specimens = []

    # Create thin film unsuported.
    elements = [(atomicNumberTracer, 1.0)]
    filmThickness_nm = tracerThickness_nm
    specimen = createAlloyThinFilm(elements, filmThickness_nm)
    specimen.name += "_IsolatedLayer"
    specimens.append(specimen)

    for tracerTopPositionZ_nm in np.arange(0.0, maximumThickness_nm+tracerThickness_nm, tracerThickness_nm):
        specimen = createFilmInSubstrate(atomicNumberTracer, atomicNumberMatrix, tracerThickness_nm, tracerTopPositionZ_nm)
        specimens.append(specimen)

    return specimens

def createParticleInSubstrate(atomicNumberParticle, atomicNumberSubstrate, particleRadius_nm, particlePositionZ_nm=None):
    if particlePositionZ_nm is None:
        particlePositionZ_nm = particleRadius_nm + 0.1

    specimen = Specimen.Specimen()

    symbolParticle = AtomData.getAtomSymbol(atomicNumberParticle)
    symbolSubstrate = AtomData.getAtomSymbol(atomicNumberSubstrate)
    name = "%s_r%iA_z%iA_%s" % (symbolParticle, int(particleRadius_nm*10), int(particlePositionZ_nm*10), symbolSubstrate)
    specimen.name = name

    specimen.numberRegions = 2
    region = Region.Region()
    region.numberElements = 1
    element = Element.Element(atomicNumberSubstrate)
    region.elements.append(element)
    region.regionType = RegionType.REGION_TYPE_BOX
    parameters = [-10000000000.0, 10000000000.0, -10000000000.0, 10000000000.0, 0.0, 20000000000.0]
    region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
    specimen.regions.append(region)

    region = Region.Region()
    region.numberElements = 1
    element = Element.Element(atomicNumberParticle)
    region.elements.append(element)
    region.regionType = RegionType.REGION_TYPE_SPHERE

    particlePositionX_A = 0.0
    particlePositionY_A = 0.0
    particlePositionZ_A = particlePositionZ_nm*10.0
    particleRadius_A = particleRadius_nm*10.0

    parameters = [particlePositionX_A, particlePositionY_A, particlePositionZ_A, particleRadius_A]
    region.regionDimensions = RegionDimensions.RegionDimensionsSphere(parameters)
    specimen.regions.append(region)

    return specimen

def createParticleOnSubstrate(atomicNumberParticle, atomicNumberSubstrate, particleDiameter_nm):
    particleDiameter_A = particleDiameter_nm*10.0
    specimen = Specimen.Specimen()

    symbolParticle = AtomData.getAtomSymbol(atomicNumberParticle)
    symbolSubstrate = AtomData.getAtomSymbol(atomicNumberSubstrate)
    name = "%s_d%iA_%s" % (symbolParticle, int(particleDiameter_A), symbolSubstrate)
    specimen.name = name

    specimen.numberRegions = 3

    region = Region.Region()
    region.numberElements = 0
    region.regionType = RegionType.REGION_TYPE_BOX
    parameters = [-10000000000.0, 10000000000.0, -10000000000.0, 10000000000.0, 0.0, particleDiameter_A]
    region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
    specimen.regions.append(region)

    region = Region.Region()
    region.numberElements = 1
    element = Element.Element(atomicNumberParticle)
    region.elements.append(element)
    region.regionType = RegionType.REGION_TYPE_SPHERE

    particleRadius_A = particleDiameter_A/2.0
    particlePositionX_A = 0.0
    particlePositionY_A = 0.0
    particlePositionZ_A = particleRadius_A

    parameters = [particlePositionX_A, particlePositionY_A, particlePositionZ_A, particleRadius_A]
    region.regionDimensions = RegionDimensions.RegionDimensionsSphere(parameters)
    specimen.regions.append(region)

    region = Region.Region()
    region.numberElements = 1
    element = Element.Element(atomicNumberSubstrate)
    region.elements.append(element)
    region.regionType = RegionType.REGION_TYPE_BOX
    parameters = [-10000000000.0, 10000000000.0, -10000000000.0, 10000000000.0, particleDiameter_A, 20000000000.0]
    region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
    specimen.regions.append(region)

    return specimen

def createParticleOnFilm(atomicNumberParticle, atomicNumberSubstrate, particleDiameter_nm, filmThiskness_nm):
    particleDiameter_A = particleDiameter_nm*10.0
    filmThiskness_A = filmThiskness_nm*10.0
    specimen = Specimen.Specimen()

    symbolParticle = AtomData.getAtomSymbol(atomicNumberParticle)
    symbolSubstrate = AtomData.getAtomSymbol(atomicNumberSubstrate)
    name = "%s_d%iA_%s" % (symbolParticle, int(particleDiameter_A), symbolSubstrate)
    specimen.name = name

    specimen.numberRegions = 3

    region = Region.Region()
    region.numberElements = 0
    region.regionType = RegionType.REGION_TYPE_BOX
    parameters = [-10000000000.0, 10000000000.0, -10000000000.0, 10000000000.0, 0.0, particleDiameter_A]
    region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
    specimen.regions.append(region)

    region = Region.Region()
    region.numberElements = 1
    element = Element.Element(atomicNumberParticle)
    region.elements.append(element)
    region.regionType = RegionType.REGION_TYPE_SPHERE

    particleRadius_A = particleDiameter_A/2.0
    particlePositionX_A = 0.0
    particlePositionY_A = 0.0
    particlePositionZ_A = particleRadius_A

    parameters = [particlePositionX_A, particlePositionY_A, particlePositionZ_A, particleRadius_A]
    region.regionDimensions = RegionDimensions.RegionDimensionsSphere(parameters)
    specimen.regions.append(region)

    region = Region.Region()
    region.numberElements = 1
    element = Element.Element(atomicNumberSubstrate)
    region.elements.append(element)
    region.regionType = RegionType.REGION_TYPE_BOX
    parameters = [-10000000000.0, 10000000000.0, -10000000000.0, 10000000000.0, particleDiameter_A, filmThiskness_A]
    region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
    specimen.regions.append(region)

    return specimen

def createAlloyParticleInSubstrate(elementsParticle, atomicNumberSubstrate, particleRadius_nm, particlePositionZ_nm=None):
    if particlePositionZ_nm is None:
        particlePositionZ_nm = particleRadius_nm + 0.1

    if particlePositionZ_nm == particleRadius_nm:
        particlePositionZ_nm += 0.1

    specimen = Specimen.Specimen()

    nameParticle = ""
    for atomicNumber, weightFraction in elementsParticle:
        nameParticle += "%s%i" % (AtomData.getAtomSymbol(atomicNumber), weightFraction*100)

    symbolSubstrate = AtomData.getAtomSymbol(atomicNumberSubstrate)
    name = "%s_r%.1fA_z%.1fA_%s" % (nameParticle, particleRadius_nm*10.0, particlePositionZ_nm*10.0, symbolSubstrate)
    specimen.name = name

    specimen.numberRegions = 2
    region = Region.Region()
    region.numberElements = 1
    element = Element.Element(atomicNumberSubstrate)
    region.elements.append(element)
    region.regionType = RegionType.REGION_TYPE_BOX
    parameters = [-10000000000.0, 10000000000.0, -10000000000.0, 10000000000.0, 0.0, 20000000000.0]
    region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
    specimen.regions.append(region)

    region = Region.Region()
    region.numberElements = len(elementsParticle)
    for atomicNumber, weightFraction in elementsParticle:
        element = Element.Element(atomicNumber, massFraction=weightFraction)
        region.elements.append(element)
    region.regionType = RegionType.REGION_TYPE_SPHERE

    particlePositionX_A = 0.0
    particlePositionY_A = 0.0
    particlePositionZ_A = particlePositionZ_nm*10.0
    particleRadius_A = particleRadius_nm*10.0

    parameters = [particlePositionX_A, particlePositionY_A, particlePositionZ_A, particleRadius_A]
    region.regionDimensions = RegionDimensions.RegionDimensionsSphere(parameters)
    specimen.regions.append(region)

    return specimen

def createAlloyParticleInThinFilm(elementsParticle, atomicNumberSubstrate, particleRadius_nm, filmThickness_nm,
                                  particlePositionZ_nm=None):
    if particlePositionZ_nm is None:
        particlePositionZ_nm = particleRadius_nm + 0.1

    specimen = Specimen.Specimen()

    nameParticle = ""
    for atomicNumber, weightFraction in elementsParticle:
        nameParticle += "%s%i" % (AtomData.getAtomSymbol(atomicNumber), weightFraction*100)

    symbolSubstrate = AtomData.getAtomSymbol(atomicNumberSubstrate)
    name = "%s_r%iA_z%iA_%s" % (nameParticle, int(particleRadius_nm*10), int(particlePositionZ_nm*10), symbolSubstrate)
    filmThickness_A = filmThickness_nm*10.0
    name += "T%iA" % (filmThickness_A)
    specimen.name = name

    specimen.numberRegions = 2
    region = Region.Region()
    region.numberElements = 1
    element = Element.Element(atomicNumberSubstrate)
    region.elements.append(element)
    region.regionType = RegionType.REGION_TYPE_BOX
    parameters = [-10000000000.0, 10000000000.0, -10000000000.0, 10000000000.0, 0.0, filmThickness_A]
    region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
    specimen.regions.append(region)

    region = Region.Region()
    region.numberElements = len(elementsParticle)
    for atomicNumber, weightFraction in elementsParticle:
        element = Element.Element(atomicNumber, massFraction=weightFraction)
        region.elements.append(element)
    region.regionType = RegionType.REGION_TYPE_SPHERE

    particlePositionX_A = 0.0
    particlePositionY_A = 0.0
    particlePositionZ_A = particlePositionZ_nm*10.0
    particleRadius_A = particleRadius_nm*10.0

    if filmThickness_A <= 2.0*particleRadius_A:
        particleRadius_A -= 0.1
        particlePositionZ_A += 0.1

    parameters = [particlePositionX_A, particlePositionY_A, particlePositionZ_A, particleRadius_A]
    region.regionDimensions = RegionDimensions.RegionDimensionsSphere(parameters)
    specimen.regions.append(region)

    return specimen

def createAlloyBoxInSubstrate(elementsParticle, elementsSubstrate, boxParameters_nm):
    if isinstance(elementsSubstrate, int):
        elementsSubstrate = [(elementsSubstrate, 1.0)]

    specimen = Specimen.Specimen()

    nameParticle = ""
    for atomicNumber, weightFraction in elementsParticle:
        nameParticle += "%s%i" % (AtomData.getAtomSymbol(atomicNumber), weightFraction*100)

    substrateName = ""
    for atomicNumber, weightFraction in elementsParticle:
        substrateName += "%s%i" % (AtomData.getAtomSymbol(atomicNumber), weightFraction*100)

    name = "%s_%s" % (nameParticle, substrateName)
    specimen.name = name

    specimen.numberRegions = 2
    region = Region.Region()
    region.numberElements = len(elementsSubstrate)
    for atomicNumber, weightFraction in elementsSubstrate:
        element = Element.Element(atomicNumber, massFraction=weightFraction)
        region.elements.append(element)
    region.regionType = RegionType.REGION_TYPE_BOX
    parameters = [-10000000000.0, 10000000000.0, -10000000000.0, 10000000000.0, 0.0, 20000000000.0]
    region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
    specimen.regions.append(region)

    region = Region.Region()
    region.numberElements = len(elementsParticle)
    for atomicNumber, weightFraction in elementsParticle:
        element = Element.Element(atomicNumber, massFraction=weightFraction)
        region.elements.append(element)
    region.regionType = RegionType.REGION_TYPE_BOX
    parameters_A = [value_nm*10.0 for value_nm in boxParameters_nm]
    region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters_A)
    specimen.regions.append(region)

    return specimen

def createAlloyBoxInThinFilm(elementsParticle, atomicNumberSubstrate, boxParameters_nm, filmThickness_nm):
    specimen = Specimen.Specimen()

    nameParticle = ""
    for atomicNumber, weightFraction in elementsParticle:
        nameParticle += "%s%i" % (AtomData.getAtomSymbol(atomicNumber), weightFraction*100)

    symbolSubstrate = AtomData.getAtomSymbol(atomicNumberSubstrate)
    name = "%s_%s" % (nameParticle, symbolSubstrate)
    filmThickness_A = filmThickness_nm*10.0
    name += "T%iA" % (filmThickness_A)
    specimen.name = name

    specimen.numberRegions = 2
    region = Region.Region()
    region.numberElements = 1
    element = Element.Element(atomicNumberSubstrate)
    region.elements.append(element)
    region.regionType = RegionType.REGION_TYPE_BOX
    parameters = [-10000000000.0, 10000000000.0, -10000000000.0, 10000000000.0, 0.0, filmThickness_A]
    region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
    specimen.regions.append(region)

    region = Region.Region()
    region.numberElements = len(elementsParticle)
    for atomicNumber, weightFraction in elementsParticle:
        element = Element.Element(atomicNumber, massFraction=weightFraction)
        region.elements.append(element)
    region.regionType = RegionType.REGION_TYPE_BOX
    parameters_A = [value_nm*10.0 for value_nm in boxParameters_nm]
    region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters_A)
    specimen.regions.append(region)

    return specimen

def createAlloyBoxInVaccuum(elements, boxParameters_nm):
    specimen = Specimen.Specimen()

    nameParticle = ""
    for atomicNumber, weightFraction in elements:
        nameParticle += "%s%i" % (AtomData.getAtomSymbol(atomicNumber), weightFraction*100)

    specimen.numberRegions = 2
    region = Region.Region()
    region.numberElements = 0
    region.regionType = RegionType.REGION_TYPE_BOX
    parameters = [-10000000000.0, 10000000000.0, -10000000000.0, 10000000000.0, 0.0, 20000000000.0]
    region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
    specimen.regions.append(region)

    region = Region.Region()
    region.numberElements = len(elements)
    for atomicNumber, weightFraction in elements:
        element = Element.Element(atomicNumber, massFraction=weightFraction)
        region.elements.append(element)
    region.regionType = RegionType.REGION_TYPE_BOX
    parameters_A = [value_nm*10.0 for value_nm in boxParameters_nm]
    region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters_A)
    specimen.regions.append(region)

    return specimen

def createAlloyMultiVerticalLayer(elementsLayers, layerWidths_nm):
    assert(len(elementsLayers) == len(layerWidths_nm))

    specimen = Specimen.Specimen()

    specimen.name = ""
    for elementsLayer in elementsLayers:
        name = ""
        for atomicNumber, _weightFraction in elementsLayer:
            name += "%s" % (AtomData.getAtomSymbol(atomicNumber))

        specimen.name += "%s_" % (name)
    specimen.name = specimen.name[:-1]

    specimen.numberRegions = len(elementsLayers)

    # First region substrate
    region = Region.Region()
    elementsLayer, layerWidth_nm = (elementsLayers[0], layerWidths_nm[0])

    region.numberElements = len(elementsLayer)
    for atomicNumber, weightFraction in elementsLayer:
        element = Element.Element(atomicNumber, massFraction=weightFraction)
        region.elements.append(element)

    layerWidth_A = layerWidth_nm*10.0
    previousWidth_A = layerWidth_A

    region.regionType = RegionType.REGION_TYPE_BOX
    parameters = [-10000000000.0, 10000000000.0, -10000000000.0, 10000000000.0, 0.0, 20000000000.0]
    region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
    specimen.regions.append(region)

    # Other regions starting after the first layer width.
    for elementsLayer, layerWidth_nm in zip(elementsLayers[1:-1], layerWidths_nm[1:-1]):
        layerWidth_A = layerWidth_nm*10.0

        region = Region.Region()
        region.numberElements = len(elementsLayer)
        for atomicNumber, weightFraction in elementsLayer:
            element = Element.Element(atomicNumber, massFraction=weightFraction)
            region.elements.append(element)

        region.regionType = RegionType.REGION_TYPE_BOX
        parameters = [previousWidth_A+1, previousWidth_A+layerWidth_A-1, -10000000000.0, 10000000000.0, 0.0+1, 20000000000.0]
        region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
        specimen.regions.append(region)

        previousWidth_A += layerWidth_A

    # Last region
    region = Region.Region()
    elementsLayer, layerWidth_nm = (elementsLayers[-1], layerWidths_nm[-1])

    region.numberElements = len(elementsLayer)
    for atomicNumber, weightFraction in elementsLayer:
        element = Element.Element(atomicNumber, massFraction=weightFraction)
        region.elements.append(element)

    region.regionType = RegionType.REGION_TYPE_BOX
    parameters = [previousWidth_A+1, 10000000000.0, -10000000000.0, 10000000000.0, 0.0+1, 20000000000.0]
    region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
    specimen.regions.append(region)

    return specimen

def computeWeightFraction(atomicNumberRef, atomicWeights):
    nominator = atomicWeights[atomicNumberRef] * getAtomicMass_g_mol(atomicNumberRef)
    denominator = 0.0
    for atomicNumber in atomicWeights:
        denominator += atomicWeights[atomicNumber] * getAtomicMass_g_mol(atomicNumber)

    weightFraction = nominator/denominator
    return weightFraction

class Simulation(object):
    def __init__(self, overwrite=True):
        self._simulationInputs = SimulationInputs.SimulationInputs()
        self._specimen = Specimen.Specimen()
        self._models = Models.Models()
        self._microscopeParameters = MicroscopeParameters.MicroscopeParameters()
        self._simulationParameters = SimulationParameters.SimulationParameters()
        self._resultParameters = ResultsParameters.ResultsParameters()

        self._overwrite = overwrite

        self._useOldVersion = False

        self._parameters = {}

    def createSimulationFiles(self, path, simulationPath):
        nameWithoutDot = self.name.replace('.', 'd')
        baseFilenameRef = r"Results\%s" % (nameWithoutDot)
        self._simulationParameters.baseFilename = baseFilenameRef

        self._simulationInputs.specimenFilename = self.name + ".sam"
        self._simulationInputs.modelFilename = self.name + ".mdl"
        self._simulationInputs.microsopeFilename = self.name + ".mic"
        self._simulationInputs.simulationParametersFilename = self.name + ".par"
        self._simulationInputs.mapFilename = None
        self._simulationInputs.resultParametersFilename = self.name + ".rp"
        self._simulationInputs.snrFilename = None

        self._path = path

        if self._overwrite or not self.isDone(simulationPath):
            self._createSimulationInputsFile()
            self._createSpecimenInputFile()
            self._createModelsInputFile()
            self._createMicroscopeInputFile()
            self._createSimulationParametersInputFile()
            self._createResultParametersInputFile()
        elif self.isDone(simulationPath):
            self.removeInputsFiles()

    def _createSimulationInputsFile(self):
        simulationInputsFilepath = os.path.join(self._path, self.filename)

        self._simulationInputs.write(simulationInputsFilepath)

    def removeInputsFiles(self):
        filepaths = []

        filepath = os.path.join(self._path, self.name + ".sim")
        filepaths.append(filepath)
        filepath = os.path.join(self._path, self._simulationInputs.specimenFilename)
        filepaths.append(filepath)
        filepath = os.path.join(self._path, self._simulationInputs.modelFilename)
        filepaths.append(filepath)
        filepath = os.path.join(self._path, self._simulationInputs.microsopeFilename)
        filepaths.append(filepath)
        filepath = os.path.join(self._path, self._simulationInputs.simulationParametersFilename)
        filepaths.append(filepath)
        filepath = os.path.join(self._path, self._simulationInputs.resultParametersFilename)
        filepaths.append(filepath)

        for filepath in filepaths:
            if os.path.exists(filepath):
                os.remove(filepath)

    def _createSpecimenInputFile(self):
        filepath = os.path.join(self._path, self._simulationInputs.specimenFilename)
        self._specimen.write(filepath)

    def _createModelsInputFile(self):
        filepath = os.path.join(self._path, self._simulationInputs.modelFilename)
        self._models.write(filepath)

    def _createMicroscopeInputFile(self):
        filepath = os.path.join(self._path, self._simulationInputs.microsopeFilename)
        self._microscopeParameters.write(filepath)

    def _createSimulationParametersInputFile(self):
        filepath = os.path.join(self._path, self._simulationInputs.simulationParametersFilename)
        self._simulationParameters.write(filepath)

    def _createResultParametersInputFile(self):
        filepath = os.path.join(self._path, self._simulationInputs.resultParametersFilename)
        self._resultParameters.write(filepath)

    def isDone(self, simulationPath):
        _isDone = True
        for suffix in self.getFilenameSuffixes():
            filepath = os.path.join(simulationPath, self._simulationParameters.baseFilename + suffix)
            if not os.path.isfile(filepath):
                _isDone = False
                logging.debug("Missing file: %s", self._simulationParameters.baseFilename + suffix)

        return _isDone

    def getFilenameSuffixes(self):
        filenameSuffixes = """_ElectronResults.dat
_ElectronTrajectoriesResults.csv
_ElectronTrajectoriesResultsInfo.dat
_InternalDump.dat
_MacBremsstrahlung.csv
_MacCharacteristic.csv
_NumberVacancies.csv
_Options.txt
_PartialSpectraInterpolatedRegion_0.csv
_PartialSpectraOriginalRegion_0.csv
_PhirhozEmittedBremsstrahlung_Region0.csv
_PhirhozEmittedBremsstrahlungThinFilm.csv
_PhirhozEmittedCharacteristic_Region0.csv
_PhirhozEmittedCharacteristicThinFilm.csv
_PhirhozEmittedInfo.dat
_PhirhozGeneratedBremsstrahlung_Region0.csv
_PhirhozGeneratedBremsstrahlungThinFilm.csv
_PhirhozGeneratedCharacteristic_Region0.csv
_PhirhozGeneratedCharacteristicThinFilm.csv
_PhirhozGeneratedInfo.dat
_ProgramVersion.dat
_SimulatedSpectraCharacteristicRegion_0.csv
_SimulatedSpectraRegion_0.csv
_SimulatedSpectraRegionInfo_0.dat
_SimulatedSpectraSpecimen.csv
_SpectraAtomDetectedLines_Region0.csv
_SpectraAtomEmittedDetectedLines_Region0.csv
_SpectraAtomInfo_Region0_Aluminium.dat
_SpectraAtomInfo_Region0_Copper.dat
_SpectraAtomPerElectronLines_1_srkeV_Region0.csv
_SpectraDetectedRegion_0.csv
_SpectraEmittedDetectedRegion_0.csv
_SpectraPerElectron_1_srkeV_Region_0.csv
_SpectraRegionInfo_0.dat
_SpectraSpecimen.csv
_SpectraSpecimenEmittedDetected.csv
_SpectraSpecimenInfo.dat
_XrayIntensities.csv
_XrayIntensitiesBremstrahlungAfterInterpolation_Region0.csv
_XrayIntensitiesBremstrahlungBeforeInterpolation_Region0.csv
_XrayIntensitiesFromPhirhoz.csv""".splitlines()

        filenameSuffixes = """_ElectronResults.dat
_ElectronTrajectoriesResults.csv
_ElectronTrajectoriesResultsInfo.dat
_InternalDump.dat
_MacBremsstrahlung.csv
_MacCharacteristic.csv
_NumberVacancies.csv
_Options.txt
_PhirhozEmittedBremsstrahlungThinFilm.csv
_PhirhozEmittedCharacteristicThinFilm.csv
_PhirhozEmittedInfo.dat
_PhirhozGeneratedBremsstrahlungThinFilm.csv
_PhirhozGeneratedCharacteristicThinFilm.csv
_PhirhozGeneratedInfo.dat
_ProgramVersion.dat
_SimulatedSpectraSpecimen.csv
_SpectraSpecimen.csv
_SpectraSpecimenEmittedDetected.csv
_SpectraSpecimenInfo.dat
_XrayIntensities.csv
_XrayIntensitiesFromPhirhoz.csv""".splitlines()

        return filenameSuffixes

    def getProgramVersionFilepath(self, simulationPath):
        filepath = os.path.join(simulationPath, self._simulationParameters.baseFilename + "_ProgramVersion.dat")
        return filepath

    def setParameters(self, parameters):
        self._parameters = parameters

        if PARAMETER_INCIDENT_ENERGY_keV in parameters:
            self.energy_keV = parameters[PARAMETER_INCIDENT_ENERGY_keV]
        if PARAMETER_NUMBER_ELECTRONS in parameters:
            self.numberElectrons = parameters[PARAMETER_NUMBER_ELECTRONS]
        if PARAMETER_NUMBER_XRAYS in parameters:
            self.numberPhotons = parameters[PARAMETER_NUMBER_XRAYS]
        if PARAMETER_BEAM_DIAMETER_nm in parameters:
            self.beamDiameter_nm = parameters[PARAMETER_BEAM_DIAMETER_nm]
        if PARAMETER_BEAM_TILT_deg in parameters:
            self.beamTilt_deg = parameters[PARAMETER_BEAM_TILT_deg]
        if PARAMETER_BEAM_POSITION_nm in parameters:
            self.beamPosition_nm = parameters[PARAMETER_BEAM_POSITION_nm]

        if PARAMETER_DETECTOR_DISTANCE_cm in parameters:
            self.detectorCrystalDistance_cm = parameters[PARAMETER_DETECTOR_DISTANCE_cm]
        if PARAMETER_DETECTOR_RADIUS_cm in parameters:
            self.detectorCrystalRadius_cm = parameters[PARAMETER_DETECTOR_RADIUS_cm]
        if PARAMETER_DETECTOR_THICKNESS_cm in parameters:
            self.detectorCrystalThickness_cm = parameters[PARAMETER_DETECTOR_THICKNESS_cm]
        if PARAMETER_DETECTOR_NOISE_eV in parameters:
            self.detectorNoise_eV = parameters[PARAMETER_DETECTOR_NOISE_eV]
        if PARAMETER_DETECTOR_CHANNEL_WIDTH_eV in parameters:
            self.detectorChannelWidth_eV = parameters[PARAMETER_DETECTOR_CHANNEL_WIDTH_eV]
        if PARAMETER_TOA_deg in parameters:
            self.takeOffAngle_deg = parameters[PARAMETER_TOA_deg]
        if PARAMETER_DETECTOR_AZIMUTHAL_ANGLE_deg in parameters:
            self.detectorAzimuthalAngle_deg = parameters[PARAMETER_DETECTOR_AZIMUTHAL_ANGLE_deg]
        if PARAMETER_NUMBER_WINDOWS in parameters:
            self.numberContinuumWindows = parameters[PARAMETER_NUMBER_WINDOWS]
        if PARAMETER_ELASTIC_CROSS_SECTION_SCALING_FACTOR in parameters:
            self.elasticCrossSectionScalingFactor = parameters[PARAMETER_ELASTIC_CROSS_SECTION_SCALING_FACTOR]
        if PARAMETER_ENERGY_LOSS_SCALING_FACTOR in parameters:
            self.energyLossScalingFactor = parameters[PARAMETER_ENERGY_LOSS_SCALING_FACTOR]

    def getParameters(self):
        return self._parameters

    def generateBaseFilename(self):
        nameWithoutDot = self.name.replace('.', 'd')
        baseFilenameRef = r"Results\%s" % (nameWithoutDot)
        self._simulationParameters.baseFilename = baseFilenameRef

    @property
    def energy_keV(self):
        return self._microscopeParameters.beamEnergy_keV
    @energy_keV.setter
    def energy_keV(self, energy_keV):
        self._microscopeParameters.beamEnergy_keV = energy_keV

    @property
    def detectorNoise_eV(self):
        return self._microscopeParameters.detectorNoise_eV
    @detectorNoise_eV.setter
    def detectorNoise_eV(self, detectorNoise_eV):
        self._microscopeParameters.detectorNoise_eV = detectorNoise_eV

    @property
    def detectorCrystalDistance_cm(self):
        return self._microscopeParameters.detectorCrystalDistance_cm
    @detectorCrystalDistance_cm.setter
    def detectorCrystalDistance_cm(self, detectorCrystalDistance_cm):
        self._microscopeParameters.detectorCrystalDistance_cm = detectorCrystalDistance_cm

    @property
    def detectorCrystalRadius_cm(self):
        return self._microscopeParameters.detectorCrystalRadius_cm
    @detectorCrystalRadius_cm.setter
    def detectorCrystalRadius_cm(self, detectorCrystalRadius_cm):
        self._microscopeParameters.detectorCrystalRadius_cm = detectorCrystalRadius_cm

    @property
    def detectorCrystalThickness_cm(self):
        return self._microscopeParameters.detectorCrystalThickness_cm
    @detectorCrystalThickness_cm.setter
    def detectorCrystalThickness_cm(self, detectorCrystalThickness_cm):
        self._microscopeParameters.detectorCrystalThickness_cm = detectorCrystalThickness_cm

    @property
    def detectorChannelWidth_eV(self):
        return self._simulationParameters.energyChannelWidth_eV
    @detectorChannelWidth_eV.setter
    def detectorChannelWidth_eV(self, detectorChannelWidth_eV):
        self._simulationParameters.energyChannelWidth_eV = detectorChannelWidth_eV

    @property
    def takeOffAngle_deg(self):
        return self._microscopeParameters.detectorTOA_deg
    @takeOffAngle_deg.setter
    def takeOffAngle_deg(self, takeOffAngle_deg):
        self._microscopeParameters.detectorTOA_deg = takeOffAngle_deg

    @property
    def detectorAzimuthalAngle_deg(self):
        return self._microscopeParameters.detectorAzimuthalAngle_deg
    @detectorAzimuthalAngle_deg.setter
    def detectorAzimuthalAngle_deg(self, detectorAzimuthalAngle_deg):
        self._microscopeParameters.detectorAzimuthalAngle_deg = detectorAzimuthalAngle_deg

    @property
    def numberContinuumWindows(self):
        return self._simulationParameters.numberWindows
    @numberContinuumWindows.setter
    def numberContinuumWindows(self, numberContinuumWindows):
        self._simulationParameters.numberWindows = numberContinuumWindows

    @property
    def solidAngle_sr(self):
        d_cm = self._microscopeParameters.detectorCrystalDistance_cm
        r_cm = self._microscopeParameters.detectorCrystalRadius_cm

        value = 4.0 * np.pi * (1.0 - d_cm/np.sqrt(d_cm*d_cm + r_cm*r_cm))
        return value

    @property
    def current_A(self):
        return self._microscopeParameters.beamCurrent_A
    @current_A.setter
    def current_A(self, current_A):
        self._microscopeParameters.beamCurrent_A = current_A

    @property
    def beamDiameter_nm(self):
        return self._microscopeParameters.beamDiameter_A/10.0
    @beamDiameter_nm.setter
    def beamDiameter_nm(self, beamDiameter_nm):
        self._microscopeParameters.beamDiameter_A = beamDiameter_nm*10.0

    @property
    def beamPosition_nm(self):
        beamPositionX_nm = self._microscopeParameters.beamPositionX_A/10.0
        beamPositionY_nm = self._microscopeParameters.beamPositionY_A/10.0
        return (beamPositionX_nm, beamPositionY_nm)

    @beamPosition_nm.setter
    def beamPosition_nm(self, beamPosition_nm):
        self._microscopeParameters.beamPositionX_A = beamPosition_nm[0]*10.0
        self._microscopeParameters.beamPositionY_A = beamPosition_nm[1]*10.0

    @property
    def time_s(self):
        return self._microscopeParameters.time_s
    @time_s.setter
    def time_s(self, time_s):
        self._microscopeParameters.time_s = time_s

    @property
    def basename(self):
        return self._basename
    @basename.setter
    def basename(self, basename):
        self._basename = basename

    @property
    def name(self):
        name = "%s_%s" % (self.basename, self._specimen.name)

        if PARAMETER_INCIDENT_ENERGY_keV in self._parameters:
            name += "_E%.1fkeV" % (self._parameters[PARAMETER_INCIDENT_ENERGY_keV])

        if PARAMETER_NUMBER_ELECTRONS in self._parameters:
            name += "_N%ie" % (self._parameters[PARAMETER_NUMBER_ELECTRONS])

        if PARAMETER_NUMBER_XRAYS in self._parameters:
            name += "_N%iX" % (self._parameters[PARAMETER_NUMBER_XRAYS])

        if PARAMETER_REPETITION in self._parameters:
            name += "_R%0i" % (self._parameters[PARAMETER_REPETITION])

        if PARAMETER_BEAM_DIAMETER_nm in self._parameters:
            name += "_dB%.1fnm" % (self._parameters[PARAMETER_BEAM_DIAMETER_nm])

        if PARAMETER_BEAM_TILT_deg in self._parameters:
            name += "_tB%.1fdeg" % (self._parameters[PARAMETER_BEAM_TILT_deg])

        if PARAMETER_BEAM_POSITION_nm in self._parameters:
            name += "_PX%.1fPY%.1fnm" % (self._parameters[PARAMETER_BEAM_POSITION_nm])

        if PARAMETER_TIME_s in self._parameters:
            name += "_t%is" % (self._parameters[PARAMETER_TIME_s])

        if PARAMETER_CURRENT_nA in self._parameters:
            name += "_I%inA" % (self._parameters[PARAMETER_CURRENT_nA])

        if PARAMETER_DETECTOR_DISTANCE_cm in self._parameters:
            name += "_dX%.2fcm" % (self._parameters[PARAMETER_DETECTOR_DISTANCE_cm])
        if PARAMETER_DETECTOR_RADIUS_cm in self._parameters:
            name += "_rDX%.2fcm" % (self._parameters[PARAMETER_DETECTOR_RADIUS_cm])
        if PARAMETER_DETECTOR_THICKNESS_cm in self._parameters:
            name += "_TDX%.2fcm" % (self._parameters[PARAMETER_DETECTOR_THICKNESS_cm])
        if PARAMETER_DETECTOR_NOISE_eV in self._parameters:
            name += "_N%.1feV" % (self._parameters[PARAMETER_DETECTOR_NOISE_eV])
        if PARAMETER_DETECTOR_CHANNEL_WIDTH_eV in self._parameters:
            name += "_w%ieV" % (self._parameters[PARAMETER_DETECTOR_CHANNEL_WIDTH_eV])
        if PARAMETER_TOA_deg in self._parameters:
            name += "_TOA%.1fdeg" % (self._parameters[PARAMETER_TOA_deg])
        if PARAMETER_DETECTOR_AZIMUTHAL_ANGLE_deg in self._parameters:
            name += "_AA%.1fdeg" % (self._parameters[PARAMETER_DETECTOR_AZIMUTHAL_ANGLE_deg])
        if PARAMETER_NUMBER_WINDOWS in self._parameters:
            name += "_N%iW" % (self._parameters[PARAMETER_NUMBER_WINDOWS])

        if PARAMETER_ELASTIC_CROSS_SECTION_SCALING_FACTOR in self._parameters:
            name += "_ECSF%f" % (self._parameters[PARAMETER_ELASTIC_CROSS_SECTION_SCALING_FACTOR])

        if PARAMETER_ENERGY_LOSS_SCALING_FACTOR in self._parameters:
            name += "_ELF%f" % (self._parameters[PARAMETER_ENERGY_LOSS_SCALING_FACTOR])

        if self._useOldVersion:
            name += "_E%.1fkeV" % (self.energy_keV)

        logging.debug(name)

        return name

    @property
    def filename(self):
        return self.name + ".sim"

    @property
    def resultsBasename(self):
        return self._simulationParameters.baseFilename

    @property
    def numberElectrons(self):
        return self._simulationParameters.numberElectrons
    @numberElectrons.setter
    def numberElectrons(self, numberElectrons):
        self._simulationParameters.numberElectrons = numberElectrons

    @property
    def numberPhotons(self):
        return self._simulationParameters.numberPhotons
    @numberPhotons.setter
    def numberPhotons(self, numberPhotons):
        self._simulationParameters.numberPhotons = numberPhotons

    @property
    def bremsstrahlungModel(self):
        return self._models.bremsstrahlungModel
    @bremsstrahlungModel.setter
    def bremsstrahlungModel(self, bremsstrahlungModel):
        self._models.bremsstrahlungModel = bremsstrahlungModel

    @property
    def numberEnergyWindows(self):
        return self._simulationParameters.numberWindows
    @numberEnergyWindows.setter
    def numberEnergyWindows(self, numberEnergyWindows):
        self._simulationParameters.numberWindows = numberEnergyWindows

    @property
    def spectrumInterpolationModel(self):
        return self._simulationParameters.spectrumInterpolationModel
    @spectrumInterpolationModel.setter
    def spectrumInterpolationModel(self, spectrumInterpolationModel):
        self._simulationParameters.spectrumInterpolationModel = spectrumInterpolationModel

    @property
    def elasticCrossSectionScalingFactor(self):
        return self._simulationParameters.elasticCrossSectionScalingFactor
    @elasticCrossSectionScalingFactor.setter
    def elasticCrossSectionScalingFactor(self, elasticCrossSectionScalingFactor):
        self._simulationParameters.elasticCrossSectionScalingFactor = elasticCrossSectionScalingFactor

    @property
    def energyLossScalingFactor(self):
        return self._simulationParameters.energyLossScalingFactor
    @energyLossScalingFactor.setter
    def energyLossScalingFactor(self, energyLossScalingFactor):
        self._simulationParameters.energyLossScalingFactor = energyLossScalingFactor

if __name__ == '__main__': #pragma: no cover
    import DrixUtilities.Runner as Runner
    Runner.Runner().run(runFunction=None)