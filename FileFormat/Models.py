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

# Third party modules.

# Local modules.
import MCXRayModel

# Project modules
import Version

# Globals and constants variables.

KEY_ATOM_MEAN_IONIZATION_POTENTIAL_MODEL = "AtomMeanIonizationPotentialModel"
KEY_ATOM_ENERGY_LOSS_MODEL = "AtomEnergyLossModel"
KEY_ATOM_SCREENING_MODEL = "AtomScreeningModel"
KEY_ATOM_CROSS_SECTION_MODEL = "AtomCrossSectionModel"
KEY_ATOM_CROSS_SECTION_SCREENING_MODEL = "AtomCrossSectionScreeningModel"
KEY_ATOM_COLLISION_MODEL = "AtomCollisionModel"
KEY_ATOM_COLLISION_SCREENING_MODEL = "AtomCollisionScreeningModel"
KEY_ATOM_ELECTRON_RANGE_MODEL = "AtomElectronRangeModel"
KEY_XRAY_CS_CHARACTERISTIC_MODEL = "XRayCSCharacteristicModel"
KEY_XRAY_CS_BREMSSTRAHLUNG_MODEL = "XRayCSBremsstrahlungModel"
KEY_SAMPLE_ENERGY_LOSS_MODEL = "SampleEnergyLossModel"


class Models(object):
    def __init__(self):
        self.version = Version.CURRENT_VERSION

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

        return modelList

    def read(self, filepath):
        self.version.readFromFile(filepath)

        lines = open(filepath, 'rb').readlines()

        for line in lines:
            line = line.strip()

            for key in self._keys:
                if line.startswith(key):
                    items = line.split('=')
                    self._modelList[key].setModel(int(items[-1]))

    def getModelList(self):
        return self._modelList

    def write(self, filepath):
        outputFile = open(filepath, 'wb')

        self._writeHeader(outputFile)

        self.version.writeLine(outputFile)

        for key in self._createKeys():
            line = "%s=%s\r\n" % (key, self._modelList[key].getModel())
            outputFile.write(line)

    def _writeHeader(self, outputFile):
        headerLines = [ "********************************************************************************",
                        "***                               PHYSICAL MODEL",
                        "***",
                        "***    AtomMeanIonizationPotentialModel    = 0 Joy & Luo",
                        "***    AtomEnergyLossModel                 = 0 Bethe",
                        "***    AtomScreeningModel                  = 0 Henoc & Maurice",
                        "***    AtomCrossSectionModel               = 0 Browning",
                        "***                                          1 Gauvin & Drouin",
                        "***    AtomCrossSectionScreeningModel      = 0 Henoc & Maurice",
                        "***    AtomCollisionModel                  = 0 Rutherford",
                        "***                                          1 Browning",
                        "***                                          2 Gauvin",
                        "***    AtomCollisionScreeningModel         = 0 Henoc & Maurice",
                        "***    AtomElectronRangeModel              = 0 Kanaya & Okayama",
                        "***    XRayCSCharacteristicModel           = 0 Castani",
                        "***    XRayCSBremsstrahlungModel           = 0 Bethe & Heitler",
                        "***                                          1 Kirkpatrick & Wiedman",
                        "***                                          2 Ding",
                        "***                                          3 Gauvin",
                        "***    SampleEnergyLossModel               = 0 Bethe & Joy & Luo",
                        "***",
                        "********************************************************************************"]
        for line in headerLines:
            outputFile.write(line+'\r\n')

    @property
    def version(self):
        return self._version
    @version.setter
    def version(self, version):
        self._version = version

    @property
    def bremsstrahlungModel(self):
        return self._modelList[KEY_XRAY_CS_BREMSSTRAHLUNG_MODEL].getModel()
    @bremsstrahlungModel.setter
    def bremsstrahlungModel(self, bremsstrahlungModel):
        self._modelList[KEY_XRAY_CS_BREMSSTRAHLUNG_MODEL].setModel(bremsstrahlungModel)

if __name__ == '__main__': #pragma: no cover
    import DrixUtilities.Runner as Runner
    Runner.Runner().run(runFunction=None)
