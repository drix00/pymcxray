#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.ModelParameters
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

MCXRay model parameters from results file.
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
import pymcxray.FileFormat.MCXRayModel as MCXRayModel

# Globals and constants variables.
KEY_MODEL_PARAMETERS = "Model Parameters"

KEY_ATOM_ENERGY_LOSS_MODEL = "Atom Energy Loss"
KEY_ATOM_MEAN_IONIZATION_POTENTIAL_MODEL = "Atom Mean Ionization Potential"
KEY_ATOM_SCREENING_MODEL = "Atom Screening"
KEY_ATOM_CROSS_SECTION_MODEL = "Atom Cross Section"
KEY_ATOM_CROSS_SECTION_SCREENING_MODEL = "Atom Screening"
KEY_ATOM_COLLISION_MODEL = "Atom Collision"
KEY_ATOM_COLLISION_SCREENING_MODEL = "Atom Screening"
KEY_ATOM_ELECTRON_RANGE_MODEL = "Atom Electron Range"
KEY_SAMPLE_ENERGY_LOSS_MODEL = "Region Energy Loss"
KEY_XRAY_CS_CHARACTERISTIC_MODEL = "XRay Characteristic Cross Section"
KEY_XRAY_CS_BREMSSTRAHLUNG_MODEL = "XRay Bremsstrahlung Cross Section"

class ModelParameters(object):
    def __init__(self):
        self._parameters = {}

    def _createKeys(self):
        keys = []

        keys.append(KEY_ATOM_ENERGY_LOSS_MODEL)
        keys.append(KEY_ATOM_MEAN_IONIZATION_POTENTIAL_MODEL)
        keys.append(KEY_ATOM_SCREENING_MODEL)
        keys.append(KEY_ATOM_CROSS_SECTION_MODEL)
        keys.append(KEY_ATOM_CROSS_SECTION_SCREENING_MODEL)
        keys.append(KEY_ATOM_COLLISION_MODEL)
        keys.append(KEY_ATOM_COLLISION_SCREENING_MODEL)
        keys.append(KEY_ATOM_ELECTRON_RANGE_MODEL)
        keys.append(KEY_SAMPLE_ENERGY_LOSS_MODEL)
        keys.append(KEY_XRAY_CS_CHARACTERISTIC_MODEL)
        keys.append(KEY_XRAY_CS_BREMSSTRAHLUNG_MODEL)

        return keys

    def _createModelList(self):
        modelList = {}

        modelList[KEY_ATOM_ENERGY_LOSS_MODEL] = MCXRayModel.AtomEnergyLossModel()
        modelList[KEY_ATOM_MEAN_IONIZATION_POTENTIAL_MODEL] = MCXRayModel.AtomMeanIonizationPotentialModel()
        modelList[KEY_ATOM_SCREENING_MODEL] = MCXRayModel.AtomScreeningModel()
        modelList[KEY_ATOM_CROSS_SECTION_MODEL] = MCXRayModel.AtomCrossSectionModel()
        modelList[KEY_ATOM_CROSS_SECTION_SCREENING_MODEL] = MCXRayModel.AtomCrossSectionScreeningModel()
        modelList[KEY_ATOM_COLLISION_MODEL] = MCXRayModel.AtomCollisionModel()
        modelList[KEY_ATOM_COLLISION_SCREENING_MODEL] = MCXRayModel.AtomCollisionScreeningModel()
        modelList[KEY_ATOM_ELECTRON_RANGE_MODEL] = MCXRayModel.AtomElectronRangeModel()
        modelList[KEY_SAMPLE_ENERGY_LOSS_MODEL] = MCXRayModel.SampleEnergyLossModel()
        modelList[KEY_XRAY_CS_CHARACTERISTIC_MODEL] = MCXRayModel.XRayCSCharacteristicModel()
        modelList[KEY_XRAY_CS_BREMSSTRAHLUNG_MODEL] = MCXRayModel.XRayCSBremsstrahlungModel()

        return modelList

    def readFromLines(self, lines):
        # Skip header line.
        indexLine = 0
        for line in lines:
            indexLine += 1
            if line.strip().startswith(KEY_MODEL_PARAMETERS):
                break
        else:
            message = "Cannot find the section header in the liens: %s" % (KEY_MODEL_PARAMETERS)
            raise ValueError(message)

        modelList = self._createModelList()
        for key in self._createKeys():
            line = lines[indexLine]
            indexLine += 1

            label, value = line.split(':')

            if label.strip() == key:
                modelList[key].setModelFromString(value)
                self._parameters[key] = modelList[key].getModel()

        return indexLine

    @property
    def atomEnergyLossModel(self):
        return self._parameters[KEY_ATOM_ENERGY_LOSS_MODEL]
    @atomEnergyLossModel.setter
    def atomEnergyLossModel(self, atomEnergyLossModel):
        self._parameters[KEY_ATOM_ENERGY_LOSS_MODEL] = atomEnergyLossModel

    @property
    def atomMeanIonizationPotentialModel(self):
        return self._parameters[KEY_ATOM_MEAN_IONIZATION_POTENTIAL_MODEL]
    @atomMeanIonizationPotentialModel.setter
    def atomMeanIonizationPotentialModel(self, atomMeanIonizationPotentialModel):
        self._parameters[KEY_ATOM_MEAN_IONIZATION_POTENTIAL_MODEL] = atomMeanIonizationPotentialModel

    @property
    def atomScreeningModel(self):
        return self._parameters[KEY_ATOM_SCREENING_MODEL]
    @atomScreeningModel.setter
    def atomScreeningModel(self, atomScreeningModel):
        self._parameters[KEY_ATOM_SCREENING_MODEL] = atomScreeningModel

    @property
    def atomCrossSectionModel(self):
        return self._parameters[KEY_ATOM_CROSS_SECTION_MODEL]
    @atomCrossSectionModel.setter
    def atomCrossSectionModel(self, atomCrossSectionModel):
        self._parameters[KEY_ATOM_CROSS_SECTION_MODEL] = atomCrossSectionModel

    @property
    def atomCrossSectionScreeningModel(self):
        return self._parameters[KEY_ATOM_CROSS_SECTION_SCREENING_MODEL]
    @atomCrossSectionScreeningModel.setter
    def atomCrossSectionScreeningModel(self, atomCrossSectionScreeningModel):
        self._parameters[KEY_ATOM_CROSS_SECTION_SCREENING_MODEL] = atomCrossSectionScreeningModel

    @property
    def atomCollisionModel(self):
        return self._parameters[KEY_ATOM_COLLISION_MODEL]
    @atomCollisionModel.setter
    def atomCollisionModel(self, atomCollisionModel):
        self._parameters[KEY_ATOM_COLLISION_MODEL] = atomCollisionModel

    @property
    def atomCollisionScreeningModel(self):
        return self._parameters[KEY_ATOM_COLLISION_SCREENING_MODEL]
    @atomCollisionScreeningModel.setter
    def atomCollisionScreeningModel(self, atomCollisionScreeningModel):
        self._parameters[KEY_ATOM_COLLISION_SCREENING_MODEL] = atomCollisionScreeningModel

    @property
    def atomElectronRangeModel(self):
        return self._parameters[KEY_ATOM_ELECTRON_RANGE_MODEL]
    @atomElectronRangeModel.setter
    def atomElectronRangeModel(self, atomElectronRangeModel):
        self._parameters[KEY_ATOM_ELECTRON_RANGE_MODEL] = atomElectronRangeModel

    @property
    def regionEnergyLossModel(self):
        return self._parameters[KEY_SAMPLE_ENERGY_LOSS_MODEL]
    @regionEnergyLossModel.setter
    def regionEnergyLossModel(self, regionEnergyLossModel):
        self._parameters[KEY_SAMPLE_ENERGY_LOSS_MODEL] = regionEnergyLossModel

    @property
    def characterisitcCrossSectionModel(self):
        return self._parameters[KEY_XRAY_CS_CHARACTERISTIC_MODEL]
    @characterisitcCrossSectionModel.setter
    def characterisitcCrossSectionModel(self, characterisitcCrossSectionModel):
        self._parameters[KEY_XRAY_CS_CHARACTERISTIC_MODEL] = characterisitcCrossSectionModel

    @property
    def bremsstrahlungCrossSectionModel(self):
        return self._parameters[KEY_XRAY_CS_BREMSSTRAHLUNG_MODEL]
    @bremsstrahlungCrossSectionModel.setter
    def bremsstrahlungCrossSectionModel(self, bremsstrahlungCrossSectionModel):
        self._parameters[KEY_XRAY_CS_BREMSSTRAHLUNG_MODEL] = bremsstrahlungCrossSectionModel
