#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Models
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

MCXRay models file.
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
import pymcxray.FileFormat.MCXRayModel as MCXRayModel

# Project modules
import pymcxray.FileFormat.Version as Version

# Globals and constants variables.

KEY_ATOM_MEAN_IONIZATION_POTENTIAL_MODEL = "AtomMeanIonizationPotentialModel"
KEY_ATOM_ENERGY_LOSS_MODEL = "AtomEnergyLossModel"
KEY_ATOM_SCREENING_MODEL = "AtomScreeningModel"
KEY_ATOM_CROSS_SECTION_MODEL = "AtomCrossSectionModel"
ATOM_CROSS_SECTION_MODEL_BROWNING = 0
ATOM_CROSS_SECTION_MODEL_GAUVIN_DROUIN = 1
KEY_ATOM_CROSS_SECTION_SCREENING_MODEL = "AtomCrossSectionScreeningModel"
KEY_ATOM_COLLISION_MODEL = "AtomCollisionModel"
ATOM_COLLISION_MODEL_RUTHERFORD = 0
ATOM_COLLISION_MODEL_BROWNING = 1
ATOM_COLLISION_MODEL_GAUVIN = 2
KEY_ATOM_COLLISION_SCREENING_MODEL = "AtomCollisionScreeningModel"
KEY_ATOM_ELECTRON_RANGE_MODEL = "AtomElectronRangeModel"
KEY_XRAY_CS_CHARACTERISTIC_MODEL = "XRayCSCharacteristicModel"
XRAY_CS_CHARACTERISTIC_MODEL_CASNATI = 0
XRAY_CS_CHARACTERISTIC_MODEL_BOTE = 1 
KEY_XRAY_CS_BREMSSTRAHLUNG_MODEL = "XRayCSBremsstrahlungModel"
XRAY_CS_BREMSSTRAHLUNG_MODEL_BETHE_HEITLER = 0
XRAY_CS_BREMSSTRAHLUNG_MODEL_KIRPATRICK_WIEDMAN = 1
XRAY_CS_BREMSSTRAHLUNG_MODEL_DING = 2
KEY_SAMPLE_ENERGY_LOSS_MODEL = "SampleEnergyLossModel"
SAMPLE_ENERGY_LOSS_MODEL_BETHE_JOY_LUO = 0
SAMPLE_ENERGY_LOSS_MODEL_BETHE = 1
SAMPLE_ENERGY_LOSS_MODEL_BETHE_RELATIVISTIC = 2
SAMPLE_ENERGY_LOSS_MODEL_JOY_LUO_GAUVIN = 3
SAMPLE_ENERGY_LOSS_MODEL_JOY_LUO_MONSEL = 4
KEY_REGION_ENERGY_LOSS_MODEL = "RegionEnergyLossModel"
KEY_MASS_ABSORPTION_COEFFICIENT_MODEL = "XRayMassAbsorptionCoefficientMode"
MASS_ABSORPTION_COEFFICIENT_MODEL_HENKE = 0
MASS_ABSORPTION_COEFFICIENT_MODEL_HEINRICH_DATA = 1
MASS_ABSORPTION_COEFFICIENT_MODEL_HEINRICH_PARAMETERS = 2
MASS_ABSORPTION_COEFFICIENT_MODEL_CHANTLER = 3


class Models(object):
    def __init__(self):
        self.version = copy.deepcopy(Version.CURRENT_VERSION)

        self._keys = self._createKeys()

        self._modelList = self._createModelList()

    def _createKeys(self):
        keys = []

        keys.append(KEY_ATOM_MEAN_IONIZATION_POTENTIAL_MODEL)
        keys.append(KEY_ATOM_ENERGY_LOSS_MODEL)
        keys.append(KEY_ATOM_SCREENING_MODEL)
        keys.append(KEY_ATOM_CROSS_SECTION_MODEL)
        keys.append(KEY_ATOM_CROSS_SECTION_SCREENING_MODEL)
        keys.append(KEY_ATOM_COLLISION_MODEL)
        keys.append(KEY_ATOM_COLLISION_SCREENING_MODEL)
        keys.append(KEY_ATOM_ELECTRON_RANGE_MODEL)
        keys.append(KEY_XRAY_CS_CHARACTERISTIC_MODEL)
        keys.append(KEY_XRAY_CS_BREMSSTRAHLUNG_MODEL)
        keys.append(KEY_SAMPLE_ENERGY_LOSS_MODEL)
        keys.append(KEY_REGION_ENERGY_LOSS_MODEL)
        keys.append(KEY_MASS_ABSORPTION_COEFFICIENT_MODEL)

        return keys

    def _createModelList(self):
        modelList = {}

        modelList[KEY_ATOM_MEAN_IONIZATION_POTENTIAL_MODEL] = MCXRayModel.AtomMeanIonizationPotentialModel()
        modelList[KEY_ATOM_ENERGY_LOSS_MODEL] = MCXRayModel.AtomEnergyLossModel()
        modelList[KEY_ATOM_SCREENING_MODEL] = MCXRayModel.AtomScreeningModel()
        modelList[KEY_ATOM_CROSS_SECTION_MODEL] = MCXRayModel.AtomCrossSectionModel()
        modelList[KEY_ATOM_CROSS_SECTION_SCREENING_MODEL] = MCXRayModel.AtomCrossSectionScreeningModel()
        modelList[KEY_ATOM_COLLISION_MODEL] = MCXRayModel.AtomCollisionModel()
        modelList[KEY_ATOM_COLLISION_SCREENING_MODEL] = MCXRayModel.AtomCollisionScreeningModel()
        modelList[KEY_ATOM_ELECTRON_RANGE_MODEL] = MCXRayModel.AtomElectronRangeModel()
        modelList[KEY_XRAY_CS_CHARACTERISTIC_MODEL] = MCXRayModel.XRayCSCharacteristicModel()
        modelList[KEY_XRAY_CS_BREMSSTRAHLUNG_MODEL] = MCXRayModel.XRayCSBremsstrahlungModel()
        modelList[KEY_SAMPLE_ENERGY_LOSS_MODEL] = MCXRayModel.SampleEnergyLossModel()
        modelList[KEY_REGION_ENERGY_LOSS_MODEL] = MCXRayModel.RegionEnergyLossModel()
        modelList[KEY_MASS_ABSORPTION_COEFFICIENT_MODEL] = MCXRayModel.MassAbsorptionCoefficientModel()

        return modelList

    def read(self, filepath):
        self.version.readFromFile(filepath)

        lines = open(filepath, 'r').readlines()

        for line in lines:
            line = line.strip()

            for key in self._keys:
                if line.startswith(key):
                    items = line.split('=')
                    self._modelList[key].setModel(int(items[-1]))

    def getModelList(self):
        return self._modelList

    def write(self, filepath):
        outputFile = open(filepath, 'w')

        self._writeHeader(outputFile)

        self.version.writeLine(outputFile)

        keys = self._createKeys()

        if self.version >= Version.VERSION_1_4_1:
            keys.remove(KEY_SAMPLE_ENERGY_LOSS_MODEL)
        else:
            keys.remove(KEY_REGION_ENERGY_LOSS_MODEL)
            keys.remove(KEY_MASS_ABSORPTION_COEFFICIENT_MODEL)

        for key in keys:
            line = "%s=%s\n" % (key, self._modelList[key].getModel())
            outputFile.write(line)

    def _writeHeader(self, outputFile):
        headerLines = []
        headerLines.append("********************************************************************************")
        headerLines.append("***                               PHYSICAL MODEL")
        headerLines.append("***")
        headerLines.append("***    AtomMeanIonizationPotentialModel    = 0 Joy & Luo")
        headerLines.append("***    AtomEnergyLossModel                 = 0 Bethe")
        headerLines.append("***    AtomScreeningModel                  = 0 Henoc & Maurice")
        headerLines.append("***    AtomCrossSectionModel               = 0 Browning")
        headerLines.append("***                                          1 Gauvin & Drouin")
        headerLines.append("***    AtomCrossSectionScreeningModel      = 0 Henoc & Maurice")
        headerLines.append("***    AtomCollisionModel                  = 0 Rutherford")
        headerLines.append("***                                          1 Browning")
        headerLines.append("***                                          2 Gauvin")
        headerLines.append("***    AtomCollisionScreeningModel         = 0 Henoc & Maurice")
        headerLines.append("***    AtomElectronRangeModel              = 0 Kanaya & Okayama")
        if self.version >= Version.VERSION_1_2_2:
            headerLines.append("***    XRayCSCharacteristicModel           = 0 Casnati")
        else:
            headerLines.append("***    XRayCSCharacteristicModel           = 0 Castani")
        headerLines.append("***    XRayCSBremsstrahlungModel           = 0 Bethe & Heitler")
        headerLines.append("***                                          1 Kirkpatrick & Wiedman")
        headerLines.append("***                                          2 Ding")
        headerLines.append("***                                          3 Gauvin")
        if self.version >= Version.VERSION_1_4_1:
            headerLines.append("***    RegionEnergyLossModel               = 0 Bethe & Joy & Luo")
            headerLines.append("***                                          1 Bethe")
            headerLines.append("***                                          2 Bethe Relativistic")
            headerLines.append("***                                          3 Joy & Luo & Gauvin")
            headerLines.append("***                                          4 Joy & Luo & Monsel")
            headerLines.append("***    MAC                                 = 0 Henke")
            headerLines.append("***                                          1 Heinrich Data (1966)")
            headerLines.append("***                                          2 Heinrich Parameters (1987)")
            headerLines.append("***                                          3 Chantler (2005)")
        else:
            headerLines.append("***    SampleEnergyLossModel               = 0 Bethe & Joy & Luo")
        headerLines.append("***")
        headerLines.append("********************************************************************************")

        for line in headerLines:
            outputFile.write(line+'\n')

    @property
    def version(self):
        return self._version
    @version.setter
    def version(self, version):
        self._version = version

    @property
    def modelSampleEnergyLoss(self):
        return self._modelList[KEY_REGION_ENERGY_LOSS_MODEL].getModel()
    @modelSampleEnergyLoss.setter
    def modelSampleEnergyLoss(self, modelSampleEnergyLoss):
        self._modelList[KEY_REGION_ENERGY_LOSS_MODEL].setModel(modelSampleEnergyLoss)

    @property
    def modelXrayCharacteristic(self):
        return self._modelList[KEY_XRAY_CS_CHARACTERISTIC_MODEL].getModel()
    @modelXrayCharacteristic.setter
    def modelXrayCharacteristic(self, modelXrayCharacteristic):
        self._modelList[KEY_XRAY_CS_CHARACTERISTIC_MODEL].setModel(modelXrayCharacteristic)

    @property
    def modelXrayBremsstrahlung(self):
        return self._modelList[KEY_XRAY_CS_BREMSSTRAHLUNG_MODEL].getModel()
    @modelXrayBremsstrahlung.setter
    def modelXrayBremsstrahlung(self, modelXrayBremsstrahlung):
        self._modelList[KEY_XRAY_CS_BREMSSTRAHLUNG_MODEL].setModel(modelXrayBremsstrahlung)

    @property
    def modelAtomCrossSection(self):
        return self._modelList[KEY_ATOM_CROSS_SECTION_MODEL].getModel()
    @modelAtomCrossSection.setter
    def modelAtomCrossSection(self, modelAtomCrossSection):
        self._modelList[KEY_ATOM_CROSS_SECTION_MODEL].setModel(modelAtomCrossSection)

    @property
    def modelAtomCollision(self):
        return self._modelList[KEY_ATOM_COLLISION_MODEL].getModel()
    @modelAtomCollision.setter
    def modelAtomCollision(self, modelAtomCollision):
        self._modelList[KEY_ATOM_COLLISION_MODEL].setModel(modelAtomCollision)

    @property
    def modelAtomMac(self):
        return self._modelList[KEY_MASS_ABSORPTION_COEFFICIENT_MODEL].getModel()
    @modelAtomMac.setter
    def modelAtomMac(self, modelAtomMac):
        self._modelList[KEY_MASS_ABSORPTION_COEFFICIENT_MODEL].setModel(modelAtomMac)
