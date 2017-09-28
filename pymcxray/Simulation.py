#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pymcxray.Simulation

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

MCXRay simulation parameters.
"""

###############################################################################
# Copyright 2017 Hendrix Demers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
###############################################################################

# Standard library modules.
import logging
import os.path
from itertools import combinations_with_replacement, product, combinations

# Third party modules.
import numpy as np

# Local modules.
from pymcxray.ElementProperties import getAtomicMass_g_mol

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
    PARAMETER_NUMBER_XRAYS, PARAMETER_TIME_s, PARAMETER_CURRENT_nA, PARAMETER_BEAM_DIAMETER_nm, \
    PARAMETER_BEAM_TILT_deg, PARAMETER_BEAM_POSITION_nm, PARAMETER_DETECTOR_DISTANCE_cm, \
    PARAMETER_DETECTOR_RADIUS_cm, PARAMETER_DETECTOR_THICKNESS_cm, PARAMETER_DETECTOR_NOISE_eV, \
    PARAMETER_DETECTOR_CHANNEL_WIDTH_eV, PARAMETER_TOA_deg, PARAMETER_DETECTOR_AZIMUTHAL_ANGLE_deg, \
    PARAMETER_NUMBER_WINDOWS, PARAMETER_ELASTIC_CROSS_SECTION_SCALING_FACTOR, PARAMETER_ENERGY_LOSS_SCALING_FACTOR, \
    PARAMETER_REPETITION, PARAMETER_MODEL_SAMPLE_ENERGY_LOSS, PARAMETER_MODEL_XRAY_CHARACTERISTIC, \
    PARAMETER_MODEL_XRAY_BREMSSTRAHLUNG, PARAMETER_MODEL_ATOM_CROSS_SECTION, PARAMETER_MODEL_ATOM_COLLISION, \
    PARAMETER_MODEL_ATOM_MAC, PARAMETER_NUMBER_LAYERS_X, PARAMETER_NUMBER_LAYERS_Y, PARAMETER_NUMBER_LAYERS_Z

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
        name += "%s%0.6f" % (AtomData.getAtomSymbol(atomicNumber), weightFraction)
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


def createAlloyThinFilm2(elements, filmThickness_nm):
    specimen = Specimen.Specimen()

    specimen.numberRegions = 2

    # Region 0
    region = Region.Region()
    region.numberElements = 0
    region.regionType = RegionType.REGION_TYPE_BOX
    parameters = [-10000000000.0, 10000000000.0, -10000000000.0, 10000000000.0, 0.0, 20000000000.0]
    region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
    specimen.regions.append(region)

    # Region 1
    region = Region.Region()
    region.numberElements = len(elements)
    name = ""

    for atomicNumber, weightFraction in elements:
        name += "%s%0.6f" % (AtomData.getAtomSymbol(atomicNumber), weightFraction)
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


def createAlloyFilmOverSubstrate(film_elements, substrate_elements, film_thickness_nm=10.0,
                                 film_mass_density_g_cm3=None, substrate_mass_density_g_cm3=None):
    specimen = Specimen.Specimen()

    name = ""

    specimen.numberRegions = 2

    region = Region.Region()
    region.numberElements = len(substrate_elements)
    for atomicNumber, weightFraction in substrate_elements:
        name += "%s%i" % (AtomData.getAtomSymbol(atomicNumber), weightFraction*100)
        element = Element.Element(atomicNumber, massFraction=weightFraction)
        region.elements.append(element)
    region.regionType = RegionType.REGION_TYPE_BOX
    parameters = [-10000000000.0, 10000000000.0, -10000000000.0, 10000000000.0, 0.0, 20000000000.0]
    region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
    region.regionMassDensity_g_cm3 = substrate_mass_density_g_cm3
    specimen.regions.append(region)

    region = Region.Region()
    region.numberElements = len(film_elements)
    for atomicNumber, weightFraction in film_elements:
        name += "%s%i" % (AtomData.getAtomSymbol(atomicNumber), weightFraction*100)
        element = Element.Element(atomicNumber, massFraction=weightFraction)
        region.elements.append(element)
    region.regionType = RegionType.REGION_TYPE_BOX
    film_thickness_A = film_thickness_nm*1.0e1
    parameters = [-10000000000.0, 10000000000.0, -10000000000.0, 10000000000.0, 0.0, film_thickness_A]
    region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
    region.regionMassDensity_g_cm3 = film_mass_density_g_cm3
    specimen.regions.append(region)

    name += "_T%.1fnm" % (film_thickness_nm)

    specimen.name = name

    return specimen


class Layer(object):
    def __init__(self, elements, thickness_nm, mass_density_g_cm3=None):
        self.elements = elements
        self.thickness_nm = thickness_nm
        self.mass_density_g_cm3 = mass_density_g_cm3


def create_multi_horizontal_layer(substrate_elements, layers, substrate_mass_density_g_cm3=None):
    """
    Create a horizontal multi layer sample.

    The substrate is the first region created. The other region are each of the element in the `layers`.

    :param substrate_elements: list of atomic number and weight fraction pair for the composition of the substrate
    :param layers:
    :param substrate_mass_density_g_cm3:
    :return:
    """
    specimen = Specimen.Specimen()
    specimen.numberRegions = 1 + len(layers)

    name = ""

    # Create first region as the substrate.
    region = Region.Region()
    region.numberElements = len(substrate_elements)
    for atomicNumber, weightFraction in substrate_elements:
        name += "%s%i" % (AtomData.getAtomSymbol(atomicNumber), weightFraction*100)
        element = Element.Element(atomicNumber, massFraction=weightFraction)
        region.elements.append(element)
    region.regionType = RegionType.REGION_TYPE_BOX
    parameters = [-10000000000.0, 10000000000.0, -10000000000.0, 10000000000.0, 0.0, 20000000000.0]
    region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
    region.regionMassDensity_g_cm3 = substrate_mass_density_g_cm3
    specimen.regions.append(region)

    # Loop over each layer.
    previous_layer_thickness_A = 0.0
    for layer in layers:
        region = Region.Region()

        region.numberElements = len(layer.elements)
        for atomicNumber, weightFraction in layer.elements:
            name += "_%s%i" % (AtomData.getAtomSymbol(atomicNumber), weightFraction*100)
            element = Element.Element(atomicNumber, massFraction=weightFraction)
            region.elements.append(element)
        region.regionType = RegionType.REGION_TYPE_BOX
        layer_thickness_A = layer.thickness_nm*1.0e1
        parameters = [-10000000000.0, 10000000000.0, -10000000000.0, 10000000000.0, previous_layer_thickness_A, previous_layer_thickness_A + layer_thickness_A]
        region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
        region.regionMassDensity_g_cm3 = layer.mass_density_g_cm3
        specimen.regions.append(region)

        name += "_T{:.1f}nm".format(layer_thickness_A)
        previous_layer_thickness_A = layer_thickness_A

    specimen.name = name

    return specimen


def createBoxFeatureInSubstrate(feature_elements, substrate_elements, depth_nm, width_nm):
    depth_A = depth_nm*1.0e1
    width_A = width_nm*1.0e1

    specimen = Specimen.Specimen()

    name = ""

    specimen.numberRegions = 2

    region = Region.Region()
    region.numberElements = len(substrate_elements)
    for atomicNumber, weightFraction in substrate_elements:
        name += "%s%i" % (AtomData.getAtomSymbol(atomicNumber), weightFraction*100)
        element = Element.Element(atomicNumber, massFraction=weightFraction)
        region.elements.append(element)
    region.regionType = RegionType.REGION_TYPE_BOX
    parameters = [-10000000000.0, 10000000000.0, -10000000000.0, 10000000000.0, 0.0, 20000000000.0]
    region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
    specimen.regions.append(region)

    region = Region.Region()
    region.numberElements = len(feature_elements)
    for atomicNumber, weightFraction in feature_elements:
        name += "%s%i" % (AtomData.getAtomSymbol(atomicNumber), weightFraction*100)
        element = Element.Element(atomicNumber, massFraction=weightFraction)
        region.elements.append(element)
    region.regionType = RegionType.REGION_TYPE_BOX
    parameters = [-width_A/2.0, width_A/2.0, -width_A/2.0, width_A/2.0, 0.0, depth_A]
    region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
    specimen.regions.append(region)

    name += "_D%inm" % (depth_nm)
    name += "_W%inm" % (width_nm)

    specimen.name = name

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
    parameters = [-10000000000.0, 10000000000.0, -10000000000.0, 10000000000.0, 0.0, 20000000000.0]
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
    particlePositionZ_A = particleRadius_A + 1.0

    parameters = [particlePositionX_A, particlePositionY_A, particlePositionZ_A, particleRadius_A]
    region.regionDimensions = RegionDimensions.RegionDimensionsSphere(parameters)
    specimen.regions.append(region)

    region = Region.Region()
    region.numberElements = 1
    element = Element.Element(atomicNumberSubstrate)
    region.elements.append(element)
    region.regionType = RegionType.REGION_TYPE_BOX
    parameters = [-10000000000.0, 10000000000.0, -10000000000.0, 10000000000.0, particlePositionZ_A + 1.0, 20000000000.0]
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
    parameters = [-10000000000.0, 10000000000.0, -10000000000.0, 10000000000.0, 0.0, particleDiameter_A+filmThiskness_A + 100.0]
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

    parameters = [particlePositionX_A, particlePositionY_A, particlePositionZ_A+0.1, particleRadius_A]
    region.regionDimensions = RegionDimensions.RegionDimensionsSphere(parameters)
    specimen.regions.append(region)

    region = Region.Region()
    region.numberElements = 1
    element = Element.Element(atomicNumberSubstrate)
    region.elements.append(element)
    region.regionType = RegionType.REGION_TYPE_BOX
    parameters = [-10000000000.0, 10000000000.0, -10000000000.0, 10000000000.0, particleDiameter_A+0.2, particleDiameter_A+0.2+filmThiskness_A]
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


def create_cnt_sample(body_elements, cnt_length_nm=1000.0, cnt_outside_diameter_nm=100.0, cnt_inside_diameter_nm=50.0, particle_diameter_nm=5.0):
    specimen = Specimen.Specimen()

    cnt_length_A = cnt_length_nm * 10.0
    cnt_outside_diameter_A = cnt_outside_diameter_nm * 10.0
    cnt_inside_diameter_A = cnt_inside_diameter_nm *10.0
    particle_diameter_A = particle_diameter_nm * 10.0
    length_A = cnt_length_A

    name = "cnt_B_"
    for atomic_number, weight_fraction in body_elements:
        name += "{:s}{:03d}".format(AtomData.getAtomSymbol(atomic_number), int(weight_fraction*100))
    specimen.name = name

    specimen.numberRegions = 3

    # region 0
    region = Region.Region()
    region.numberElements = 0
    region.regionType = RegionType.REGION_TYPE_BOX
    parameters = [-10000000000.0, 10000000000.0, -10000000000.0, 10000000000.0, 0.0, cnt_outside_diameter_A+particle_diameter_A + 10000.0]
    region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
    specimen.regions.append(region)

    # Outside body
    region = Region.Region()
    region.numberElements = len(body_elements)
    for atomic_number, weight_fraction in body_elements:
        element = Element.Element(atomic_number, massFraction=weight_fraction)
        region.elements.append(element)
    region.regionType = RegionType.REGION_TYPE_CYLINDER
    position_center_X_A = 0.0
    position_center_Y_A = -length_A / 2.0
    position_center_Z_A = cnt_outside_diameter_A / 2.0 + particle_diameter_A
    direction_X = 0.0
    direction_Y = 1.0
    direction_Z = 0.0
    radius_A = cnt_outside_diameter_A/2.0
    parameters = [position_center_X_A, position_center_Y_A, position_center_Z_A,
                  direction_X, direction_Y, direction_Z,
                  length_A, radius_A]
    region.regionDimensions = RegionDimensions.RegionDimensionsCylinder(parameters)
    specimen.regions.append(region)

    # Inside
    region = Region.Region()
    region.numberElements = 0
    region.regionType = RegionType.REGION_TYPE_CYLINDER
    position_center_X_A = 0.0
    position_center_Y_A = -length_A /2.0
    position_center_Z_A = cnt_outside_diameter_A/2.0 + particle_diameter_A
    direction_X = 0.0
    direction_Y = 1.0
    direction_Z = 0.0
    length_A = cnt_length_A
    radius_A = cnt_inside_diameter_A/2.0
    parameters = [position_center_X_A, position_center_Y_A, position_center_Z_A,
                  direction_X, direction_Y, direction_Z,
                  length_A, radius_A]
    region.regionDimensions = RegionDimensions.RegionDimensionsCylinder(parameters)
    specimen.regions.append(region)

    return specimen


def computeWeightFraction(atomicNumberRef, atomicWeights):
    nominator = atomicWeights[atomicNumberRef] * getAtomicMass_g_mol(atomicNumberRef)
    denominator = 0.0
    for atomicNumber in atomicWeights:
        denominator += atomicWeights[atomicNumber] * getAtomicMass_g_mol(atomicNumber)

    weightFraction = nominator/denominator
    return weightFraction


def create_weight_fractions(weight_fraction_step, number_elements):
    weight_fractions = np.arange(0.0, 1.0+weight_fraction_step, weight_fraction_step)
    if number_elements == 1:
        return weight_fractions.tolist()

    items = product(weight_fractions.tolist(), repeat=number_elements)

    weight_fractions_data = []
    for item in items:
        if 1.0-weight_fraction_step/2.0 <= sum(item) <= 1.0+weight_fraction_step/2.0:
            weight_fractions_data.append(tuple(item))

    return list(weight_fractions_data)


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

        self.format_digit = {}

    def createSimulationFiles(self, path, simulationPath, hdf5_group):
        nameWithoutDot = self.name.replace('.', 'd')
        baseFilenameRef = "Results/%s" % (nameWithoutDot)
        self._simulationParameters.baseFilename = os.path.normpath(baseFilenameRef)

        self._simulationInputs.specimenFilename = self.name + ".sam"
        self._simulationInputs.modelFilename = self.name + ".mdl"
        self._simulationInputs.microsopeFilename = self.name + ".mic"
        self._simulationInputs.simulationParametersFilename = self.name + ".par"
        self._simulationInputs.mapFilename = None
        self._simulationInputs.resultParametersFilename = self.name + ".rp"
        self._simulationInputs.snrFilename = None

        self._path = path

        if self._overwrite or not self.isDone(simulationPath, hdf5_group):
            self._createSimulationInputsFile()
            self._createSpecimenInputFile()
            self._createModelsInputFile()
            self._createMicroscopeInputFile()
            self._createSimulationParametersInputFile()
            self._createResultParametersInputFile()
        elif self.isDone(simulationPath, hdf5_group):
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

    def isDone(self, simulationPath, hdf5_group=None):
        _isDone = True
        for suffix in self.getFilenameSuffixes():
            filepath = os.path.join(simulationPath, self._simulationParameters.baseFilename + suffix)
            if not os.path.isfile(filepath):
                _isDone = False
                logging.debug("Missing file: %s", self._simulationParameters.baseFilename + suffix)
                break

        if hdf5_group is not None and not _isDone:
            group_name = self.name
            if group_name in hdf5_group:
                _isDone = True
        return _isDone

    def getFilenameSuffixes(self):
#         filenameSuffixes = """_ElectronResults.dat
# _ElectronTrajectoriesResults.csv
# _ElectronTrajectoriesResultsInfo.dat
# _InternalDump.dat
# _MacBremsstrahlung.csv
# _MacCharacteristic.csv
# _NumberVacancies.csv
# _Options.txt
# _PartialSpectraInterpolatedRegion_0.csv
# _PartialSpectraOriginalRegion_0.csv
# _PhirhozEmittedBremsstrahlung_Region0.csv
# _PhirhozEmittedBremsstrahlungThinFilm.csv
# _PhirhozEmittedCharacteristic_Region0.csv
# _PhirhozEmittedCharacteristicThinFilm.csv
# _PhirhozEmittedInfo.dat
# _PhirhozGeneratedBremsstrahlung_Region0.csv
# _PhirhozGeneratedBremsstrahlungThinFilm.csv
# _PhirhozGeneratedCharacteristic_Region0.csv
# _PhirhozGeneratedCharacteristicThinFilm.csv
# _PhirhozGeneratedInfo.dat
# _ProgramVersion.dat
# _SimulatedSpectraCharacteristicRegion_0.csv
# _SimulatedSpectraRegion_0.csv
# _SimulatedSpectraRegionInfo_0.dat
# _SimulatedSpectraSpecimen.csv
# _SpectraAtomDetectedLines_Region0.csv
# _SpectraAtomEmittedDetectedLines_Region0.csv
# _SpectraAtomInfo_Region0_Aluminium.dat
# _SpectraAtomInfo_Region0_Copper.dat
# _SpectraAtomPerElectronLines_1_srkeV_Region0.csv
# _SpectraDetectedRegion_0.csv
# _SpectraEmittedDetectedRegion_0.csv
# _SpectraPerElectron_1_srkeV_Region_0.csv
# _SpectraRegionInfo_0.dat
# _SpectraSpecimen.csv
# _SpectraSpecimenEmittedDetected.csv
# _SpectraSpecimenInfo.dat
# _XrayIntensities.csv
# _XrayIntensitiesBremstrahlungAfterInterpolation_Region0.csv
# _XrayIntensitiesBremstrahlungBeforeInterpolation_Region0.csv
# _XrayIntensitiesFromPhirhoz.csv""".splitlines()

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
        if PARAMETER_NUMBER_LAYERS_X in parameters:
            self.numberLayersX = parameters[PARAMETER_NUMBER_LAYERS_X]
        if PARAMETER_NUMBER_LAYERS_Y in parameters:
            self.numberLayersY = parameters[PARAMETER_NUMBER_LAYERS_Y]
        if PARAMETER_NUMBER_LAYERS_Z in parameters:
            self.numberLayersZ = parameters[PARAMETER_NUMBER_LAYERS_Z]
        if PARAMETER_ELASTIC_CROSS_SECTION_SCALING_FACTOR in parameters:
            self.elasticCrossSectionScalingFactor = parameters[PARAMETER_ELASTIC_CROSS_SECTION_SCALING_FACTOR]
        if PARAMETER_ENERGY_LOSS_SCALING_FACTOR in parameters:
            self.energyLossScalingFactor = parameters[PARAMETER_ENERGY_LOSS_SCALING_FACTOR]

        if PARAMETER_MODEL_SAMPLE_ENERGY_LOSS in parameters:
            self._models.modelSampleEnergyLoss = parameters[PARAMETER_MODEL_SAMPLE_ENERGY_LOSS]
        if PARAMETER_MODEL_XRAY_CHARACTERISTIC in parameters:
            self._models.modelXrayCharacteristic = parameters[PARAMETER_MODEL_XRAY_CHARACTERISTIC]
        if PARAMETER_MODEL_XRAY_BREMSSTRAHLUNG in parameters:
            self._models.modelXrayBremsstrahlung = parameters[PARAMETER_MODEL_XRAY_BREMSSTRAHLUNG]
        if PARAMETER_MODEL_ATOM_CROSS_SECTION in parameters:
            self._models.modelAtomCrossSection = parameters[PARAMETER_MODEL_ATOM_CROSS_SECTION]
        if PARAMETER_MODEL_ATOM_COLLISION in parameters:
            self._models.modelAtomCollision = parameters[PARAMETER_MODEL_ATOM_COLLISION]
        if PARAMETER_MODEL_ATOM_MAC in parameters:
            self._models.modelAtomMac = parameters[PARAMETER_MODEL_ATOM_MAC]


    def getParameters(self):
        return self._parameters

    def generateBaseFilename(self):
        nameWithoutDot = self.name.replace('.', 'd')
        baseFilenameRef = "Results/%s" % (nameWithoutDot)
        self._simulationParameters.baseFilename = os.path.normpath(baseFilenameRef)

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
    def numberLayersX(self):
        return self._simulationParameters.numberFilmsX
    @numberLayersX.setter
    def numberLayersX(self, number_layers_x):
        self._simulationParameters.numberFilmsX = number_layers_x

    @property
    def numberLayersY(self):
        return self._simulationParameters.numberFilmsY
    @numberLayersY.setter
    def numberLayersY(self, number_layers_y):
        self._simulationParameters.numberFilmsY = number_layers_y

    @property
    def numberLayersZ(self):
        return self._simulationParameters.numberFilmsZ
    @numberLayersZ.setter
    def numberLayersZ(self, number_layers_z):
        self._simulationParameters.numberFilmsZ = number_layers_z

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
    def beamTilt_deg(self):
        return self._microscopeParameters.beamTilt_deg
    @beamTilt_deg.setter
    def beamTilt_deg(self, beamTilt_deg):
        self._microscopeParameters.beamTilt_deg = beamTilt_deg

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
            if PARAMETER_INCIDENT_ENERGY_keV in self.format_digit:
                name += "_E{:.{}f}keV".format(self._parameters[PARAMETER_INCIDENT_ENERGY_keV], self.format_digit[PARAMETER_INCIDENT_ENERGY_keV])
            else:
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
        if PARAMETER_NUMBER_LAYERS_X in self._parameters:
            name += "_N%iLX" % (self._parameters[PARAMETER_NUMBER_LAYERS_X])
        if PARAMETER_NUMBER_LAYERS_Y in self._parameters:
            name += "_N%iLY" % (self._parameters[PARAMETER_NUMBER_LAYERS_Y])
        if PARAMETER_NUMBER_LAYERS_Z in self._parameters:
            name += "_N%iLZ" % (self._parameters[PARAMETER_NUMBER_LAYERS_Z])

        if PARAMETER_ELASTIC_CROSS_SECTION_SCALING_FACTOR in self._parameters:
            name += "_ECSF%f" % (self._parameters[PARAMETER_ELASTIC_CROSS_SECTION_SCALING_FACTOR])

        if PARAMETER_ENERGY_LOSS_SCALING_FACTOR in self._parameters:
            name += "_ELF%f" % (self._parameters[PARAMETER_ENERGY_LOSS_SCALING_FACTOR])

        if PARAMETER_MODEL_SAMPLE_ENERGY_LOSS in self._parameters:
            name += "_MSEL%i" % (self._parameters[PARAMETER_MODEL_SAMPLE_ENERGY_LOSS])
        if PARAMETER_MODEL_XRAY_CHARACTERISTIC in self._parameters:
            name += "_MXC%i" % (self._parameters[PARAMETER_MODEL_XRAY_CHARACTERISTIC])
        if PARAMETER_MODEL_XRAY_BREMSSTRAHLUNG in self._parameters:
            name += "_MXB%i" % (self._parameters[PARAMETER_MODEL_XRAY_BREMSSTRAHLUNG])
        if PARAMETER_MODEL_ATOM_CROSS_SECTION in self._parameters:
            name += "_MACS%i" % (self._parameters[PARAMETER_MODEL_ATOM_CROSS_SECTION])
        if PARAMETER_MODEL_ATOM_COLLISION in self._parameters:
            name += "_MAC%i" % (self._parameters[PARAMETER_MODEL_ATOM_COLLISION])
        if PARAMETER_MODEL_ATOM_MAC in self._parameters:
            name += "_MAM%i" % (self._parameters[PARAMETER_MODEL_ATOM_MAC])

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
    def modelXrayBremsstrahlung(self):
        return self._models.modelXrayBremsstrahlung
    @modelXrayBremsstrahlung.setter
    def modelXrayBremsstrahlung(self, modelXrayBremsstrahlung):
        self._models.modelXrayBremsstrahlung = modelXrayBremsstrahlung

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
