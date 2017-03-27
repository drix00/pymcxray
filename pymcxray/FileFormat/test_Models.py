#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.test_Models
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests module `Models`.
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
import unittest
import logging
import os.path

# Third party modules.
from nose.plugins.skip import SkipTest

# Local modules.

# Project modules
import pymcxray.FileFormat.Models as Models
import pymcxray.FileFormat.MCXRayModel as MCXRayModel
import pymcxray.FileFormat.testUtilities as testUtilities
import pymcxray.FileFormat.Version as Version

# Globals and constants variables.

class TestModels(unittest.TestCase):
    """
    TestCase class for the module `Models`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

        self.testDataPath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../test_data"))

        self.tempDataPath = testUtilities.createTempDataPath(self.testDataPath)

        self.numberModels = 13

    def tearDown(self):
        """
        Teardown method.
        """

        unittest.TestCase.tearDown(self)

        testUtilities.removeTempDataPath(self.tempDataPath)

    def testSkeleton(self):
        """
        First test to check if the testcase is working with the testing framework.
        """

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_read(self):
        """
        Tests for method `read`.
        """

        models = Models.Models()

        for title in testUtilities.getSimulationTitles():
            filepath = os.path.abspath(os.path.join(self.testDataPath, "%s/%s.mdl" % (title, title)))
            models.read(filepath)

            modelList = models.getModelList()
            self.assertEquals(self.numberModels, len(modelList))

            self.assertEquals(MCXRayModel.AtomMeanIonizationPotentialModel.TYPE_JOY_LUO, modelList[Models.KEY_ATOM_MEAN_IONIZATION_POTENTIAL_MODEL].getModel())
            self.assertEquals(MCXRayModel.AtomEnergyLossModel.TYPE_BETHE, modelList[Models.KEY_ATOM_ENERGY_LOSS_MODEL].getModel())
            self.assertEquals(MCXRayModel.AtomScreeningModel.TYPE_HENOC_MAURICE, modelList[Models.KEY_ATOM_SCREENING_MODEL].getModel())
            self.assertEquals(MCXRayModel.AtomCrossSectionModel.TYPE_BROWNING, modelList[Models.KEY_ATOM_CROSS_SECTION_MODEL].getModel())
            self.assertEquals(MCXRayModel.AtomCrossSectionScreeningModel.TYPE_HENOC_MAURICE, modelList[Models.KEY_ATOM_CROSS_SECTION_SCREENING_MODEL].getModel())
            self.assertEquals(MCXRayModel.AtomCollisionModel.TYPE_BROWNING, modelList[Models.KEY_ATOM_COLLISION_MODEL].getModel())
            self.assertEquals(MCXRayModel.AtomCollisionScreeningModel.TYPE_HENOC_MAURICE, modelList[Models.KEY_ATOM_COLLISION_SCREENING_MODEL].getModel())
            self.assertEquals(MCXRayModel.AtomElectronRangeModel.TYPE_KANAYA_OKAYAMA, modelList[Models.KEY_ATOM_ELECTRON_RANGE_MODEL].getModel())
            self.assertEquals(MCXRayModel.XRayCSCharacteristicModel.TYPE_CASTANI1982, modelList[Models.KEY_XRAY_CS_CHARACTERISTIC_MODEL].getModel())
            self.assertEquals(MCXRayModel.XRayCSBremsstrahlungModel.TYPE_DING, modelList[Models.KEY_XRAY_CS_BREMSSTRAHLUNG_MODEL].getModel())
            self.assertEquals(MCXRayModel.SampleEnergyLossModel.TYPE_BETHE_JOY_LUO, modelList[Models.KEY_SAMPLE_ENERGY_LOSS_MODEL].getModel())
            self.assertEquals(MCXRayModel.RegionEnergyLossModel.TYPE_BETHE_JOY_LUO, modelList[Models.KEY_REGION_ENERGY_LOSS_MODEL].getModel())
            self.assertEquals(MCXRayModel.MassAbsorptionCoefficientModel.TYPE_CHANTLER2005, modelList[Models.KEY_MASS_ABSORPTION_COEFFICIENT_MODEL].getModel())

        #self.fail("Test if the testcase is working.")

    def test_read_1_1_1(self):
        """
        Tests for method `read`.
        """

        models = Models.Models()

        title = "AlMgBulk5keV_version_1_1_1"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.mdl" % (title)))
        models.read(filepath)

        self.assertEquals(Version.VERSION_1_1_1.major, models.version.major)
        self.assertEquals(Version.VERSION_1_1_1.minor, models.version.minor)
        self.assertEquals(Version.VERSION_1_1_1.revision, models.version.revision)
        self.assertEquals(Version.VERSION_1_1_1, models.version)

        modelList = models.getModelList()
        self.assertEquals(self.numberModels, len(modelList))

        self.assertEquals(MCXRayModel.AtomMeanIonizationPotentialModel.TYPE_JOY_LUO, modelList[Models.KEY_ATOM_MEAN_IONIZATION_POTENTIAL_MODEL].getModel())
        self.assertEquals(MCXRayModel.AtomEnergyLossModel.TYPE_BETHE, modelList[Models.KEY_ATOM_ENERGY_LOSS_MODEL].getModel())
        self.assertEquals(MCXRayModel.AtomScreeningModel.TYPE_HENOC_MAURICE, modelList[Models.KEY_ATOM_SCREENING_MODEL].getModel())
        self.assertEquals(MCXRayModel.AtomCrossSectionModel.TYPE_BROWNING, modelList[Models.KEY_ATOM_CROSS_SECTION_MODEL].getModel())
        self.assertEquals(MCXRayModel.AtomCrossSectionScreeningModel.TYPE_HENOC_MAURICE, modelList[Models.KEY_ATOM_CROSS_SECTION_SCREENING_MODEL].getModel())
        self.assertEquals(MCXRayModel.AtomCollisionModel.TYPE_BROWNING, modelList[Models.KEY_ATOM_COLLISION_MODEL].getModel())
        self.assertEquals(MCXRayModel.AtomCollisionScreeningModel.TYPE_HENOC_MAURICE, modelList[Models.KEY_ATOM_COLLISION_SCREENING_MODEL].getModel())
        self.assertEquals(MCXRayModel.AtomElectronRangeModel.TYPE_KANAYA_OKAYAMA, modelList[Models.KEY_ATOM_ELECTRON_RANGE_MODEL].getModel())
        self.assertEquals(MCXRayModel.XRayCSCharacteristicModel.TYPE_CASTANI1982, modelList[Models.KEY_XRAY_CS_CHARACTERISTIC_MODEL].getModel())
        self.assertEquals(MCXRayModel.XRayCSBremsstrahlungModel.TYPE_KIRKPATRICK_WIEDMAN, modelList[Models.KEY_XRAY_CS_BREMSSTRAHLUNG_MODEL].getModel())
        self.assertEquals(MCXRayModel.SampleEnergyLossModel.TYPE_BETHE_JOY_LUO, modelList[Models.KEY_SAMPLE_ENERGY_LOSS_MODEL].getModel())

        #self.fail("Test if the testcase is working.")

    def test_read_1_2_0(self):
        """
        Tests for method `read`.
        """

        models = Models.Models()

        title = "AlMgBulk5keV_version_1_2_0"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.mdl" % (title)))
        models.read(filepath)

        self.assertEquals(Version.VERSION_1_2_0.major, models.version.major)
        self.assertEquals(Version.VERSION_1_2_0.minor, models.version.minor)
        self.assertEquals(Version.VERSION_1_2_0.revision, models.version.revision)
        self.assertEquals(Version.VERSION_1_2_0, models.version)

        modelList = models.getModelList()
        self.assertEquals(self.numberModels, len(modelList))

        self.assertEquals(MCXRayModel.AtomMeanIonizationPotentialModel.TYPE_JOY_LUO, modelList[Models.KEY_ATOM_MEAN_IONIZATION_POTENTIAL_MODEL].getModel())
        self.assertEquals(MCXRayModel.AtomEnergyLossModel.TYPE_BETHE, modelList[Models.KEY_ATOM_ENERGY_LOSS_MODEL].getModel())
        self.assertEquals(MCXRayModel.AtomScreeningModel.TYPE_HENOC_MAURICE, modelList[Models.KEY_ATOM_SCREENING_MODEL].getModel())
        self.assertEquals(MCXRayModel.AtomCrossSectionModel.TYPE_GAUVIN_DROUIN, modelList[Models.KEY_ATOM_CROSS_SECTION_MODEL].getModel())
        self.assertEquals(MCXRayModel.AtomCrossSectionScreeningModel.TYPE_HENOC_MAURICE, modelList[Models.KEY_ATOM_CROSS_SECTION_SCREENING_MODEL].getModel())
        self.assertEquals(MCXRayModel.AtomCollisionModel.TYPE_RUTHERFORD, modelList[Models.KEY_ATOM_COLLISION_MODEL].getModel())
        self.assertEquals(MCXRayModel.AtomCollisionScreeningModel.TYPE_HENOC_MAURICE, modelList[Models.KEY_ATOM_COLLISION_SCREENING_MODEL].getModel())
        self.assertEquals(MCXRayModel.AtomElectronRangeModel.TYPE_KANAYA_OKAYAMA, modelList[Models.KEY_ATOM_ELECTRON_RANGE_MODEL].getModel())
        self.assertEquals(MCXRayModel.XRayCSCharacteristicModel.TYPE_CASTANI1982, modelList[Models.KEY_XRAY_CS_CHARACTERISTIC_MODEL].getModel())
        self.assertEquals(MCXRayModel.XRayCSBremsstrahlungModel.TYPE_DING, modelList[Models.KEY_XRAY_CS_BREMSSTRAHLUNG_MODEL].getModel())
        self.assertEquals(MCXRayModel.SampleEnergyLossModel.TYPE_BETHE_JOY_LUO, modelList[Models.KEY_SAMPLE_ENERGY_LOSS_MODEL].getModel())

        #self.fail("Test if the testcase is working.")

    def test_read_1_2_1(self):
        """
        Tests for method `read`.
        """

        models = Models.Models()

        title = "AlMgBulk5keV_version_1_2_1"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.mdl" % (title)))
        models.read(filepath)

        self.assertEquals(Version.VERSION_1_2_1.major, models.version.major)
        self.assertEquals(Version.VERSION_1_2_1.minor, models.version.minor)
        self.assertEquals(Version.VERSION_1_2_1.revision, models.version.revision)
        self.assertEquals(Version.VERSION_1_2_1, models.version)

        modelList = models.getModelList()
        self.assertEquals(self.numberModels, len(modelList))

        self.assertEquals(MCXRayModel.AtomMeanIonizationPotentialModel.TYPE_JOY_LUO, modelList[Models.KEY_ATOM_MEAN_IONIZATION_POTENTIAL_MODEL].getModel())
        self.assertEquals(MCXRayModel.AtomEnergyLossModel.TYPE_BETHE, modelList[Models.KEY_ATOM_ENERGY_LOSS_MODEL].getModel())
        self.assertEquals(MCXRayModel.AtomScreeningModel.TYPE_HENOC_MAURICE, modelList[Models.KEY_ATOM_SCREENING_MODEL].getModel())
        self.assertEquals(MCXRayModel.AtomCrossSectionModel.TYPE_GAUVIN_DROUIN, modelList[Models.KEY_ATOM_CROSS_SECTION_MODEL].getModel())
        self.assertEquals(MCXRayModel.AtomCrossSectionScreeningModel.TYPE_HENOC_MAURICE, modelList[Models.KEY_ATOM_CROSS_SECTION_SCREENING_MODEL].getModel())
        self.assertEquals(MCXRayModel.AtomCollisionModel.TYPE_RUTHERFORD, modelList[Models.KEY_ATOM_COLLISION_MODEL].getModel())
        self.assertEquals(MCXRayModel.AtomCollisionScreeningModel.TYPE_HENOC_MAURICE, modelList[Models.KEY_ATOM_COLLISION_SCREENING_MODEL].getModel())
        self.assertEquals(MCXRayModel.AtomElectronRangeModel.TYPE_KANAYA_OKAYAMA, modelList[Models.KEY_ATOM_ELECTRON_RANGE_MODEL].getModel())
        self.assertEquals(MCXRayModel.XRayCSCharacteristicModel.TYPE_CASTANI1982, modelList[Models.KEY_XRAY_CS_CHARACTERISTIC_MODEL].getModel())
        self.assertEquals(MCXRayModel.XRayCSBremsstrahlungModel.TYPE_DING, modelList[Models.KEY_XRAY_CS_BREMSSTRAHLUNG_MODEL].getModel())
        self.assertEquals(MCXRayModel.SampleEnergyLossModel.TYPE_BETHE_JOY_LUO, modelList[Models.KEY_SAMPLE_ENERGY_LOSS_MODEL].getModel())

        #self.fail("Test if the testcase is working.")

    def test_read_1_4_1(self):
        """
        Tests for method `read`.
        """

        models = Models.Models()

        title = "AlMgBulk5keV_version_1_4_1"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.mdl" % (title)))
        models.read(filepath)

        self.assertEquals(Version.VERSION_1_4_1.major, models.version.major)
        self.assertEquals(Version.VERSION_1_4_1.minor, models.version.minor)
        self.assertEquals(Version.VERSION_1_4_1.revision, models.version.revision)
        self.assertEquals(Version.VERSION_1_4_1, models.version)

        modelList = models.getModelList()
        self.assertEquals(self.numberModels, len(modelList))

        self.assertEquals(MCXRayModel.AtomMeanIonizationPotentialModel.TYPE_JOY_LUO, modelList[Models.KEY_ATOM_MEAN_IONIZATION_POTENTIAL_MODEL].getModel())
        self.assertEquals(MCXRayModel.AtomEnergyLossModel.TYPE_BETHE, modelList[Models.KEY_ATOM_ENERGY_LOSS_MODEL].getModel())
        self.assertEquals(MCXRayModel.AtomScreeningModel.TYPE_HENOC_MAURICE, modelList[Models.KEY_ATOM_SCREENING_MODEL].getModel())
        self.assertEquals(MCXRayModel.AtomCrossSectionModel.TYPE_GAUVIN_DROUIN, modelList[Models.KEY_ATOM_CROSS_SECTION_MODEL].getModel())
        self.assertEquals(MCXRayModel.AtomCrossSectionScreeningModel.TYPE_HENOC_MAURICE, modelList[Models.KEY_ATOM_CROSS_SECTION_SCREENING_MODEL].getModel())
        self.assertEquals(MCXRayModel.AtomCollisionModel.TYPE_RUTHERFORD, modelList[Models.KEY_ATOM_COLLISION_MODEL].getModel())
        self.assertEquals(MCXRayModel.AtomCollisionScreeningModel.TYPE_HENOC_MAURICE, modelList[Models.KEY_ATOM_COLLISION_SCREENING_MODEL].getModel())
        self.assertEquals(MCXRayModel.AtomElectronRangeModel.TYPE_KANAYA_OKAYAMA, modelList[Models.KEY_ATOM_ELECTRON_RANGE_MODEL].getModel())
        self.assertEquals(MCXRayModel.XRayCSCharacteristicModel.TYPE_CASTANI1982, modelList[Models.KEY_XRAY_CS_CHARACTERISTIC_MODEL].getModel())
        self.assertEquals(MCXRayModel.XRayCSBremsstrahlungModel.TYPE_DING, modelList[Models.KEY_XRAY_CS_BREMSSTRAHLUNG_MODEL].getModel())
        self.assertEquals(MCXRayModel.SampleEnergyLossModel.TYPE_BETHE_JOY_LUO, modelList[Models.KEY_SAMPLE_ENERGY_LOSS_MODEL].getModel())
        self.assertEquals(MCXRayModel.RegionEnergyLossModel.TYPE_BETHE_JOY_LUO, modelList[Models.KEY_REGION_ENERGY_LOSS_MODEL].getModel())
        self.assertEquals(MCXRayModel.MassAbsorptionCoefficientModel.TYPE_CHANTLER2005, modelList[Models.KEY_MASS_ABSORPTION_COEFFICIENT_MODEL].getModel())

        #self.fail("Test if the testcase is working.")

    def test__createKeys(self):
        """
        Tests for method `_createKeys`.
        """

        keys = Models.Models()._createKeys()
        self.assertEquals(self.numberModels, len(keys))

        #self.fail("Test if the testcase is working.")

    def testDefaultModels(self):
        """
        Tests for method `read`.
        """

        models = Models.Models()

        modelList = models.getModelList()

        self.assertEquals(self.numberModels, len(modelList))

        self.assertEquals(MCXRayModel.AtomMeanIonizationPotentialModel.TYPE_JOY_LUO, modelList[Models.KEY_ATOM_MEAN_IONIZATION_POTENTIAL_MODEL].getModel())
        self.assertEquals(MCXRayModel.AtomEnergyLossModel.TYPE_BETHE, modelList[Models.KEY_ATOM_ENERGY_LOSS_MODEL].getModel())
        self.assertEquals(MCXRayModel.AtomScreeningModel.TYPE_HENOC_MAURICE, modelList[Models.KEY_ATOM_SCREENING_MODEL].getModel())
        self.assertEquals(MCXRayModel.AtomCrossSectionModel.TYPE_BROWNING, modelList[Models.KEY_ATOM_CROSS_SECTION_MODEL].getModel())
        self.assertEquals(MCXRayModel.AtomCrossSectionScreeningModel.TYPE_HENOC_MAURICE, modelList[Models.KEY_ATOM_CROSS_SECTION_SCREENING_MODEL].getModel())
        self.assertEquals(MCXRayModel.AtomCollisionModel.TYPE_BROWNING, modelList[Models.KEY_ATOM_COLLISION_MODEL].getModel())
        self.assertEquals(MCXRayModel.AtomCollisionScreeningModel.TYPE_HENOC_MAURICE, modelList[Models.KEY_ATOM_COLLISION_SCREENING_MODEL].getModel())
        self.assertEquals(MCXRayModel.AtomElectronRangeModel.TYPE_KANAYA_OKAYAMA, modelList[Models.KEY_ATOM_ELECTRON_RANGE_MODEL].getModel())
        self.assertEquals(MCXRayModel.XRayCSCharacteristicModel.TYPE_BOTE2009, modelList[Models.KEY_XRAY_CS_CHARACTERISTIC_MODEL].getModel())
        self.assertEquals(MCXRayModel.XRayCSBremsstrahlungModel.TYPE_KIRKPATRICK_WIEDMAN, modelList[Models.KEY_XRAY_CS_BREMSSTRAHLUNG_MODEL].getModel())
        self.assertEquals(MCXRayModel.SampleEnergyLossModel.TYPE_BETHE_JOY_LUO, modelList[Models.KEY_SAMPLE_ENERGY_LOSS_MODEL].getModel())

        #self.fail("Test if the testcase is working.")

    def test_write(self):
        """
        Tests for method `write`.
        """
        raise SkipTest

        self.maxDiff = None

        for title in testUtilities.getSimulationTitles():
            filepathReference = os.path.abspath(os.path.join(self.testDataPath, "%s/%s.mdl" % (title, title)))

            filepath = os.path.join(self.tempDataPath, "%s.mdl" % (title))
            models = Models.Models()
            models._modelList[Models.KEY_XRAY_CS_BREMSSTRAHLUNG_MODEL].setModel(MCXRayModel.XRayCSBremsstrahlungModel.TYPE_DING)

            models.write(filepath)

            linesRef = open(filepathReference, 'r').readlines()
            lines = open(filepath, 'r').readlines()

            self.assertListEqual(linesRef, lines)

        #self.fail("Test if the testcase is working.")

    def test_write_1_1_1(self):
        """
        Tests for method `write`.
        """
        raise SkipTest

        self.maxDiff = None

        title = "AlMgBulk5keV_version_1_1_1"

        filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.mdl" % (title)))

        filepath = os.path.join(self.tempDataPath, "%s.par" % (title))
        models = Models.Models()
        models._modelList[Models.KEY_XRAY_CS_BREMSSTRAHLUNG_MODEL].setModel(MCXRayModel.XRayCSBremsstrahlungModel.TYPE_DING)

        models.write(filepath)

        linesRef = open(filepathReference, 'r').readlines()
        lines = open(filepath, 'r').readlines()

        self.assertListEqual(linesRef, lines)

        self.fail("Test if the testcase is working.")

    def test_write_1_2_0(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        title = "AlMgBulk5keV_version_1_2_0"

        filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.mdl" % (title)))

        filepath = os.path.join(self.tempDataPath, "%s.par" % (title))
        models = Models.Models()
        models.version = Version.VERSION_1_2_0
        models._modelList[Models.KEY_XRAY_CS_CHARACTERISTIC_MODEL].setModel(MCXRayModel.XRayCSCharacteristicModel.TYPE_CASTANI1982)
        models._modelList[Models.KEY_XRAY_CS_BREMSSTRAHLUNG_MODEL].setModel(MCXRayModel.XRayCSBremsstrahlungModel.TYPE_DING)
        models._modelList[Models.KEY_ATOM_CROSS_SECTION_MODEL].setModel(MCXRayModel.AtomCrossSectionModel.TYPE_GAUVIN_DROUIN)
        models._modelList[Models.KEY_ATOM_COLLISION_MODEL].setModel(MCXRayModel.AtomCollisionModel.TYPE_RUTHERFORD)

        models.write(filepath)

        linesRef = open(filepathReference, 'r').readlines()
        lines = open(filepath, 'r').readlines()

        self.assertListEqual(linesRef, lines)

        #self.fail("Test if the testcase is working.")

    def test_write_1_2_1(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        title = "AlMgBulk5keV_version_1_2_1"

        filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.mdl" % (title)))

        filepath = os.path.join(self.tempDataPath, "%s.par" % (title))
        models = Models.Models()
        models.version = Version.VERSION_1_2_1
        models._modelList[Models.KEY_XRAY_CS_CHARACTERISTIC_MODEL].setModel(MCXRayModel.XRayCSCharacteristicModel.TYPE_CASTANI1982)
        models._modelList[Models.KEY_XRAY_CS_BREMSSTRAHLUNG_MODEL].setModel(MCXRayModel.XRayCSBremsstrahlungModel.TYPE_DING)
        models._modelList[Models.KEY_ATOM_CROSS_SECTION_MODEL].setModel(MCXRayModel.AtomCrossSectionModel.TYPE_GAUVIN_DROUIN)
        models._modelList[Models.KEY_ATOM_COLLISION_MODEL].setModel(MCXRayModel.AtomCollisionModel.TYPE_RUTHERFORD)

        models.write(filepath)

        linesRef = open(filepathReference, 'r').readlines()
        lines = open(filepath, 'r').readlines()

        self.assertListEqual(linesRef, lines)

        #self.fail("Test if the testcase is working.")

    def test_write_1_4_1(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        title = "AlMgBulk5keV_version_1_4_1"

        filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "%s.mdl" % (title)))

        filepath = os.path.join(self.tempDataPath, "%s.par" % (title))
        models = Models.Models()
        models.version = Version.VERSION_1_4_1
        models._modelList[Models.KEY_XRAY_CS_CHARACTERISTIC_MODEL].setModel(MCXRayModel.XRayCSCharacteristicModel.TYPE_CASTANI1982)
        models._modelList[Models.KEY_XRAY_CS_BREMSSTRAHLUNG_MODEL].setModel(MCXRayModel.XRayCSBremsstrahlungModel.TYPE_DING)
        models._modelList[Models.KEY_ATOM_CROSS_SECTION_MODEL].setModel(MCXRayModel.AtomCrossSectionModel.TYPE_GAUVIN_DROUIN)
        models._modelList[Models.KEY_ATOM_COLLISION_MODEL].setModel(MCXRayModel.AtomCollisionModel.TYPE_RUTHERFORD)

        models.write(filepath)

        linesRef = open(filepathReference, 'r').readlines()
        lines = open(filepath, 'r').readlines()

        self.assertListEqual(linesRef, lines)

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    import nose
    nose.runmodule()
