#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.format.test_Models

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests module :py:mod:`mcxray.format.Models`.
"""

###############################################################################
# Copyright 2019 Hendrix Demers
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

import os.path
# Standard library modules.
import unittest

import mcxray.format.MCXRayModel as MCXRayModel
# Project modules
import mcxray.format.Models as Models
import mcxray.format.version as version
import tests.format.testUtilities as testUtilities


# Third party modules.
# Local modules.


# Globals and constants variables.

class TestModels(unittest.TestCase):
    """
    TestCase class for the module :py:mod:`mcxray.format.Models`.
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

        # self.fail("Test if the testcase is working.")
        self.assertTrue(True)

    def test_read(self):
        """
        Tests for method `read`.
        """

        models = Models.Models()

        for title in testUtilities.getSimulationTitles():
            filepath = os.path.abspath(os.path.join(self.testDataPath, "%s/%s.mdl" % (title, title)))
            models.read(filepath)

            modelList = models.getModelList()
            self.assertEqual(self.numberModels, len(modelList))

            self.assertEqual(MCXRayModel.AtomMeanIonizationPotentialModel.TYPE_JOY_LUO,
                              modelList[Models.KEY_ATOM_MEAN_IONIZATION_POTENTIAL_MODEL].getModel())
            self.assertEqual(MCXRayModel.AtomEnergyLossModel.TYPE_BETHE,
                              modelList[Models.KEY_ATOM_ENERGY_LOSS_MODEL].getModel())
            self.assertEqual(MCXRayModel.AtomScreeningModel.TYPE_HENOC_MAURICE,
                              modelList[Models.KEY_ATOM_SCREENING_MODEL].getModel())
            self.assertEqual(MCXRayModel.AtomCrossSectionModel.TYPE_BROWNING,
                              modelList[Models.KEY_ATOM_CROSS_SECTION_MODEL].getModel())
            self.assertEqual(MCXRayModel.AtomCrossSectionScreeningModel.TYPE_HENOC_MAURICE,
                              modelList[Models.KEY_ATOM_CROSS_SECTION_SCREENING_MODEL].getModel())
            self.assertEqual(MCXRayModel.AtomCollisionModel.TYPE_BROWNING,
                              modelList[Models.KEY_ATOM_COLLISION_MODEL].getModel())
            self.assertEqual(MCXRayModel.AtomCollisionScreeningModel.TYPE_HENOC_MAURICE,
                              modelList[Models.KEY_ATOM_COLLISION_SCREENING_MODEL].getModel())
            self.assertEqual(MCXRayModel.AtomElectronRangeModel.TYPE_KANAYA_OKAYAMA,
                              modelList[Models.KEY_ATOM_ELECTRON_RANGE_MODEL].getModel())
            self.assertEqual(MCXRayModel.XRayCSCharacteristicModel.TYPE_CASTANI1982,
                              modelList[Models.KEY_XRAY_CS_CHARACTERISTIC_MODEL].getModel())
            self.assertEqual(MCXRayModel.XRayCSBremsstrahlungModel.TYPE_DING,
                              modelList[Models.KEY_XRAY_CS_BREMSSTRAHLUNG_MODEL].getModel())
            self.assertEqual(MCXRayModel.SampleEnergyLossModel.TYPE_BETHE_JOY_LUO,
                              modelList[Models.KEY_SAMPLE_ENERGY_LOSS_MODEL].getModel())
            self.assertEqual(MCXRayModel.RegionEnergyLossModel.TYPE_BETHE_JOY_LUO,
                              modelList[Models.KEY_REGION_ENERGY_LOSS_MODEL].getModel())
            self.assertEqual(MCXRayModel.MassAbsorptionCoefficientModel.TYPE_CHANTLER2005,
                              modelList[Models.KEY_MASS_ABSORPTION_COEFFICIENT_MODEL].getModel())

        # self.fail("Test if the testcase is working.")

    def test_read_1_1_1(self):
        """
        Tests for method `read`.
        """

        models = Models.Models()

        title = "AlMgBulk5keV_version_1_1_1"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.mdl".format(title)))
        models.read(filepath)

        self.assertEqual(version.VERSION_1_1_1.major, models.version.major)
        self.assertEqual(version.VERSION_1_1_1.minor, models.version.minor)
        self.assertEqual(version.VERSION_1_1_1.revision, models.version.revision)
        self.assertEqual(version.VERSION_1_1_1, models.version)

        modelList = models.getModelList()
        self.assertEqual(self.numberModels, len(modelList))

        self.assertEqual(MCXRayModel.AtomMeanIonizationPotentialModel.TYPE_JOY_LUO,
                          modelList[Models.KEY_ATOM_MEAN_IONIZATION_POTENTIAL_MODEL].getModel())
        self.assertEqual(MCXRayModel.AtomEnergyLossModel.TYPE_BETHE,
                          modelList[Models.KEY_ATOM_ENERGY_LOSS_MODEL].getModel())
        self.assertEqual(MCXRayModel.AtomScreeningModel.TYPE_HENOC_MAURICE,
                          modelList[Models.KEY_ATOM_SCREENING_MODEL].getModel())
        self.assertEqual(MCXRayModel.AtomCrossSectionModel.TYPE_BROWNING,
                          modelList[Models.KEY_ATOM_CROSS_SECTION_MODEL].getModel())
        self.assertEqual(MCXRayModel.AtomCrossSectionScreeningModel.TYPE_HENOC_MAURICE,
                          modelList[Models.KEY_ATOM_CROSS_SECTION_SCREENING_MODEL].getModel())
        self.assertEqual(MCXRayModel.AtomCollisionModel.TYPE_BROWNING,
                          modelList[Models.KEY_ATOM_COLLISION_MODEL].getModel())
        self.assertEqual(MCXRayModel.AtomCollisionScreeningModel.TYPE_HENOC_MAURICE,
                          modelList[Models.KEY_ATOM_COLLISION_SCREENING_MODEL].getModel())
        self.assertEqual(MCXRayModel.AtomElectronRangeModel.TYPE_KANAYA_OKAYAMA,
                          modelList[Models.KEY_ATOM_ELECTRON_RANGE_MODEL].getModel())
        self.assertEqual(MCXRayModel.XRayCSCharacteristicModel.TYPE_CASTANI1982,
                          modelList[Models.KEY_XRAY_CS_CHARACTERISTIC_MODEL].getModel())
        self.assertEqual(MCXRayModel.XRayCSBremsstrahlungModel.TYPE_KIRKPATRICK_WIEDMAN,
                          modelList[Models.KEY_XRAY_CS_BREMSSTRAHLUNG_MODEL].getModel())
        self.assertEqual(MCXRayModel.SampleEnergyLossModel.TYPE_BETHE_JOY_LUO,
                          modelList[Models.KEY_SAMPLE_ENERGY_LOSS_MODEL].getModel())

        # self.fail("Test if the testcase is working.")

    def test_read_1_2_0(self):
        """
        Tests for method `read`.
        """

        models = Models.Models()

        title = "AlMgBulk5keV_version_1_2_0"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.mdl".format(title)))
        models.read(filepath)

        self.assertEqual(version.VERSION_1_2_0.major, models.version.major)
        self.assertEqual(version.VERSION_1_2_0.minor, models.version.minor)
        self.assertEqual(version.VERSION_1_2_0.revision, models.version.revision)
        self.assertEqual(version.VERSION_1_2_0, models.version)

        modelList = models.getModelList()
        self.assertEqual(self.numberModels, len(modelList))

        self.assertEqual(MCXRayModel.AtomMeanIonizationPotentialModel.TYPE_JOY_LUO,
                          modelList[Models.KEY_ATOM_MEAN_IONIZATION_POTENTIAL_MODEL].getModel())
        self.assertEqual(MCXRayModel.AtomEnergyLossModel.TYPE_BETHE,
                          modelList[Models.KEY_ATOM_ENERGY_LOSS_MODEL].getModel())
        self.assertEqual(MCXRayModel.AtomScreeningModel.TYPE_HENOC_MAURICE,
                          modelList[Models.KEY_ATOM_SCREENING_MODEL].getModel())
        self.assertEqual(MCXRayModel.AtomCrossSectionModel.TYPE_GAUVIN_DROUIN,
                          modelList[Models.KEY_ATOM_CROSS_SECTION_MODEL].getModel())
        self.assertEqual(MCXRayModel.AtomCrossSectionScreeningModel.TYPE_HENOC_MAURICE,
                          modelList[Models.KEY_ATOM_CROSS_SECTION_SCREENING_MODEL].getModel())
        self.assertEqual(MCXRayModel.AtomCollisionModel.TYPE_RUTHERFORD,
                          modelList[Models.KEY_ATOM_COLLISION_MODEL].getModel())
        self.assertEqual(MCXRayModel.AtomCollisionScreeningModel.TYPE_HENOC_MAURICE,
                          modelList[Models.KEY_ATOM_COLLISION_SCREENING_MODEL].getModel())
        self.assertEqual(MCXRayModel.AtomElectronRangeModel.TYPE_KANAYA_OKAYAMA,
                          modelList[Models.KEY_ATOM_ELECTRON_RANGE_MODEL].getModel())
        self.assertEqual(MCXRayModel.XRayCSCharacteristicModel.TYPE_CASTANI1982,
                          modelList[Models.KEY_XRAY_CS_CHARACTERISTIC_MODEL].getModel())
        self.assertEqual(MCXRayModel.XRayCSBremsstrahlungModel.TYPE_DING,
                          modelList[Models.KEY_XRAY_CS_BREMSSTRAHLUNG_MODEL].getModel())
        self.assertEqual(MCXRayModel.SampleEnergyLossModel.TYPE_BETHE_JOY_LUO,
                          modelList[Models.KEY_SAMPLE_ENERGY_LOSS_MODEL].getModel())

        # self.fail("Test if the testcase is working.")

    def test_read_1_2_1(self):
        """
        Tests for method `read`.
        """

        models = Models.Models()

        title = "AlMgBulk5keV_version_1_2_1"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.mdl".format(title)))
        models.read(filepath)

        self.assertEqual(version.VERSION_1_2_1.major, models.version.major)
        self.assertEqual(version.VERSION_1_2_1.minor, models.version.minor)
        self.assertEqual(version.VERSION_1_2_1.revision, models.version.revision)
        self.assertEqual(version.VERSION_1_2_1, models.version)

        modelList = models.getModelList()
        self.assertEqual(self.numberModels, len(modelList))

        self.assertEqual(MCXRayModel.AtomMeanIonizationPotentialModel.TYPE_JOY_LUO,
                          modelList[Models.KEY_ATOM_MEAN_IONIZATION_POTENTIAL_MODEL].getModel())
        self.assertEqual(MCXRayModel.AtomEnergyLossModel.TYPE_BETHE,
                          modelList[Models.KEY_ATOM_ENERGY_LOSS_MODEL].getModel())
        self.assertEqual(MCXRayModel.AtomScreeningModel.TYPE_HENOC_MAURICE,
                          modelList[Models.KEY_ATOM_SCREENING_MODEL].getModel())
        self.assertEqual(MCXRayModel.AtomCrossSectionModel.TYPE_GAUVIN_DROUIN,
                          modelList[Models.KEY_ATOM_CROSS_SECTION_MODEL].getModel())
        self.assertEqual(MCXRayModel.AtomCrossSectionScreeningModel.TYPE_HENOC_MAURICE,
                          modelList[Models.KEY_ATOM_CROSS_SECTION_SCREENING_MODEL].getModel())
        self.assertEqual(MCXRayModel.AtomCollisionModel.TYPE_RUTHERFORD,
                          modelList[Models.KEY_ATOM_COLLISION_MODEL].getModel())
        self.assertEqual(MCXRayModel.AtomCollisionScreeningModel.TYPE_HENOC_MAURICE,
                          modelList[Models.KEY_ATOM_COLLISION_SCREENING_MODEL].getModel())
        self.assertEqual(MCXRayModel.AtomElectronRangeModel.TYPE_KANAYA_OKAYAMA,
                          modelList[Models.KEY_ATOM_ELECTRON_RANGE_MODEL].getModel())
        self.assertEqual(MCXRayModel.XRayCSCharacteristicModel.TYPE_CASTANI1982,
                          modelList[Models.KEY_XRAY_CS_CHARACTERISTIC_MODEL].getModel())
        self.assertEqual(MCXRayModel.XRayCSBremsstrahlungModel.TYPE_DING,
                          modelList[Models.KEY_XRAY_CS_BREMSSTRAHLUNG_MODEL].getModel())
        self.assertEqual(MCXRayModel.SampleEnergyLossModel.TYPE_BETHE_JOY_LUO,
                          modelList[Models.KEY_SAMPLE_ENERGY_LOSS_MODEL].getModel())

        # self.fail("Test if the testcase is working.")

    def test_read_1_4_1(self):
        """
        Tests for method `read`.
        """

        models = Models.Models()

        title = "AlMgBulk5keV_version_1_4_1"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.mdl".format(title)))
        models.read(filepath)

        self.assertEqual(version.VERSION_1_4_1.major, models.version.major)
        self.assertEqual(version.VERSION_1_4_1.minor, models.version.minor)
        self.assertEqual(version.VERSION_1_4_1.revision, models.version.revision)
        self.assertEqual(version.VERSION_1_4_1, models.version)

        modelList = models.getModelList()
        self.assertEqual(self.numberModels, len(modelList))

        self.assertEqual(MCXRayModel.AtomMeanIonizationPotentialModel.TYPE_JOY_LUO,
                          modelList[Models.KEY_ATOM_MEAN_IONIZATION_POTENTIAL_MODEL].getModel())
        self.assertEqual(MCXRayModel.AtomEnergyLossModel.TYPE_BETHE,
                          modelList[Models.KEY_ATOM_ENERGY_LOSS_MODEL].getModel())
        self.assertEqual(MCXRayModel.AtomScreeningModel.TYPE_HENOC_MAURICE,
                          modelList[Models.KEY_ATOM_SCREENING_MODEL].getModel())
        self.assertEqual(MCXRayModel.AtomCrossSectionModel.TYPE_GAUVIN_DROUIN,
                          modelList[Models.KEY_ATOM_CROSS_SECTION_MODEL].getModel())
        self.assertEqual(MCXRayModel.AtomCrossSectionScreeningModel.TYPE_HENOC_MAURICE,
                          modelList[Models.KEY_ATOM_CROSS_SECTION_SCREENING_MODEL].getModel())
        self.assertEqual(MCXRayModel.AtomCollisionModel.TYPE_RUTHERFORD,
                          modelList[Models.KEY_ATOM_COLLISION_MODEL].getModel())
        self.assertEqual(MCXRayModel.AtomCollisionScreeningModel.TYPE_HENOC_MAURICE,
                          modelList[Models.KEY_ATOM_COLLISION_SCREENING_MODEL].getModel())
        self.assertEqual(MCXRayModel.AtomElectronRangeModel.TYPE_KANAYA_OKAYAMA,
                          modelList[Models.KEY_ATOM_ELECTRON_RANGE_MODEL].getModel())
        self.assertEqual(MCXRayModel.XRayCSCharacteristicModel.TYPE_CASTANI1982,
                          modelList[Models.KEY_XRAY_CS_CHARACTERISTIC_MODEL].getModel())
        self.assertEqual(MCXRayModel.XRayCSBremsstrahlungModel.TYPE_DING,
                          modelList[Models.KEY_XRAY_CS_BREMSSTRAHLUNG_MODEL].getModel())
        self.assertEqual(MCXRayModel.SampleEnergyLossModel.TYPE_BETHE_JOY_LUO,
                          modelList[Models.KEY_SAMPLE_ENERGY_LOSS_MODEL].getModel())
        self.assertEqual(MCXRayModel.RegionEnergyLossModel.TYPE_BETHE_JOY_LUO,
                          modelList[Models.KEY_REGION_ENERGY_LOSS_MODEL].getModel())
        self.assertEqual(MCXRayModel.MassAbsorptionCoefficientModel.TYPE_CHANTLER2005,
                          modelList[Models.KEY_MASS_ABSORPTION_COEFFICIENT_MODEL].getModel())

        # self.fail("Test if the testcase is working.")

    def test__createKeys(self):
        """
        Tests for method `_create_keys`.
        """

        keys = Models.Models()._createKeys()
        self.assertEqual(self.numberModels, len(keys))

        # self.fail("Test if the testcase is working.")

    def testDefaultModels(self):
        """
        Tests for method `read`.
        """

        models = Models.Models()

        modelList = models.getModelList()

        self.assertEqual(self.numberModels, len(modelList))

        self.assertEqual(MCXRayModel.AtomMeanIonizationPotentialModel.TYPE_JOY_LUO,
                          modelList[Models.KEY_ATOM_MEAN_IONIZATION_POTENTIAL_MODEL].getModel())
        self.assertEqual(MCXRayModel.AtomEnergyLossModel.TYPE_BETHE,
                          modelList[Models.KEY_ATOM_ENERGY_LOSS_MODEL].getModel())
        self.assertEqual(MCXRayModel.AtomScreeningModel.TYPE_HENOC_MAURICE,
                          modelList[Models.KEY_ATOM_SCREENING_MODEL].getModel())
        self.assertEqual(MCXRayModel.AtomCrossSectionModel.TYPE_BROWNING,
                          modelList[Models.KEY_ATOM_CROSS_SECTION_MODEL].getModel())
        self.assertEqual(MCXRayModel.AtomCrossSectionScreeningModel.TYPE_HENOC_MAURICE,
                          modelList[Models.KEY_ATOM_CROSS_SECTION_SCREENING_MODEL].getModel())
        self.assertEqual(MCXRayModel.AtomCollisionModel.TYPE_BROWNING,
                          modelList[Models.KEY_ATOM_COLLISION_MODEL].getModel())
        self.assertEqual(MCXRayModel.AtomCollisionScreeningModel.TYPE_HENOC_MAURICE,
                          modelList[Models.KEY_ATOM_COLLISION_SCREENING_MODEL].getModel())
        self.assertEqual(MCXRayModel.AtomElectronRangeModel.TYPE_KANAYA_OKAYAMA,
                          modelList[Models.KEY_ATOM_ELECTRON_RANGE_MODEL].getModel())
        self.assertEqual(MCXRayModel.XRayCSCharacteristicModel.TYPE_BOTE2009,
                          modelList[Models.KEY_XRAY_CS_CHARACTERISTIC_MODEL].getModel())
        self.assertEqual(MCXRayModel.XRayCSBremsstrahlungModel.TYPE_KIRKPATRICK_WIEDMAN,
                          modelList[Models.KEY_XRAY_CS_BREMSSTRAHLUNG_MODEL].getModel())
        self.assertEqual(MCXRayModel.SampleEnergyLossModel.TYPE_BETHE_JOY_LUO,
                          modelList[Models.KEY_SAMPLE_ENERGY_LOSS_MODEL].getModel())

        # self.fail("Test if the testcase is working.")

    def test_write(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        for title in testUtilities.getSimulationTitles():

            filepath = os.path.join(self.tempDataPath, "{}.mdl".format(title))
            models = Models.Models()
            models._modelList[Models.KEY_XRAY_CS_BREMSSTRAHLUNG_MODEL].setModel(
                MCXRayModel.XRayCSBremsstrahlungModel.TYPE_DING)

            models.write(filepath)

            # .. todo:: Make the lines comparison work.
            # filepathReference = os.path.abspath(os.path.join(self.testDataPath, "{}/{}.mdl".format(title, title)))
            # linesRef = open(filepathReference, 'r').readlines()
            # lines = open(filepath, 'r').readlines()
            # self.assertListEqual(linesRef, lines)

        # self.fail("Test if the testcase is working.")

    def test_write_1_1_1(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        title = "AlMgBulk5keV_version_1_1_1"

        filepath = os.path.join(self.tempDataPath, "{}.par".format(title))
        models = Models.Models()
        models._modelList[Models.KEY_XRAY_CS_BREMSSTRAHLUNG_MODEL].setModel(
            MCXRayModel.XRayCSBremsstrahlungModel.TYPE_DING)

        models.write(filepath)

        # .. todo:: Make the lines comparison work.
        # filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.mdl".format(title)))
        # linesRef = open(filepathReference, 'r').readlines()
        # lines = open(filepath, 'r').readlines()
        # self.assertListEqual(linesRef, lines)

        # self.fail("Test if the testcase is working.")

    def test_write_1_2_0(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        title = "AlMgBulk5keV_version_1_2_0"

        filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.mdl".format(title)))

        filepath = os.path.join(self.tempDataPath, "{}.par".format(title))
        models = Models.Models()
        models.version = version.VERSION_1_2_0
        models._modelList[Models.KEY_XRAY_CS_CHARACTERISTIC_MODEL].setModel(
            MCXRayModel.XRayCSCharacteristicModel.TYPE_CASTANI1982)
        models._modelList[Models.KEY_XRAY_CS_BREMSSTRAHLUNG_MODEL].setModel(
            MCXRayModel.XRayCSBremsstrahlungModel.TYPE_DING)
        models._modelList[Models.KEY_ATOM_CROSS_SECTION_MODEL].setModel(
            MCXRayModel.AtomCrossSectionModel.TYPE_GAUVIN_DROUIN)
        models._modelList[Models.KEY_ATOM_COLLISION_MODEL].setModel(MCXRayModel.AtomCollisionModel.TYPE_RUTHERFORD)

        models.write(filepath)

        linesRef = open(filepathReference, 'r').readlines()
        lines = open(filepath, 'r').readlines()

        self.assertListEqual(linesRef, lines)

        # self.fail("Test if the testcase is working.")

    def test_write_1_2_1(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        title = "AlMgBulk5keV_version_1_2_1"

        filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.mdl".format(title)))

        filepath = os.path.join(self.tempDataPath, "{}.par".format(title))
        models = Models.Models()
        models.version = version.VERSION_1_2_1
        models._modelList[Models.KEY_XRAY_CS_CHARACTERISTIC_MODEL].setModel(
            MCXRayModel.XRayCSCharacteristicModel.TYPE_CASTANI1982)
        models._modelList[Models.KEY_XRAY_CS_BREMSSTRAHLUNG_MODEL].setModel(
            MCXRayModel.XRayCSBremsstrahlungModel.TYPE_DING)
        models._modelList[Models.KEY_ATOM_CROSS_SECTION_MODEL].setModel(
            MCXRayModel.AtomCrossSectionModel.TYPE_GAUVIN_DROUIN)
        models._modelList[Models.KEY_ATOM_COLLISION_MODEL].setModel(MCXRayModel.AtomCollisionModel.TYPE_RUTHERFORD)

        models.write(filepath)

        linesRef = open(filepathReference, 'r').readlines()
        lines = open(filepath, 'r').readlines()

        self.assertListEqual(linesRef, lines)

        # self.fail("Test if the testcase is working.")

    def test_write_1_4_1(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        title = "AlMgBulk5keV_version_1_4_1"

        filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.mdl".format(title)))

        filepath = os.path.join(self.tempDataPath, "{}.par".format(title))
        models = Models.Models()
        models.version = version.VERSION_1_4_1
        models._modelList[Models.KEY_XRAY_CS_CHARACTERISTIC_MODEL].setModel(
            MCXRayModel.XRayCSCharacteristicModel.TYPE_CASTANI1982)
        models._modelList[Models.KEY_XRAY_CS_BREMSSTRAHLUNG_MODEL].setModel(
            MCXRayModel.XRayCSBremsstrahlungModel.TYPE_DING)
        models._modelList[Models.KEY_ATOM_CROSS_SECTION_MODEL].setModel(
            MCXRayModel.AtomCrossSectionModel.TYPE_GAUVIN_DROUIN)
        models._modelList[Models.KEY_ATOM_COLLISION_MODEL].setModel(MCXRayModel.AtomCollisionModel.TYPE_RUTHERFORD)

        models.write(filepath)

        linesRef = open(filepathReference, 'r').readlines()
        lines = open(filepath, 'r').readlines()

        self.assertListEqual(linesRef, lines)

        # self.fail("Test if the testcase is working.")
