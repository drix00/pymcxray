#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.format.test_SimulationInputs

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Test the module :py:mod:`mcxray.format.SimulationInputs`.
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

# Standard library modules.
import unittest
import os.path
import copy

# Third party modules.

# Local modules.

# Project modules
import mcxray.format.SimulationInputs as SimulationInputs
import tests.format.testUtilities as testUtilities
import mcxray.format.version as version

# Globals and constants variables.


class TestSimulationInputs(unittest.TestCase):
    """
    TestCase class for the module :py:mod:`mcxray.format.moduleName`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

        self.testDataPath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../test_data"))
        self.tempDataPath = testUtilities.createTempDataPath(self.testDataPath)

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
        self.assert_(True)

    def test_read(self):
        """
        Tests for method `read`.
        """

        simulationInputs = SimulationInputs.SimulationInputs()

        for title in testUtilities.getSimulationTitles():
            filepath = os.path.abspath(os.path.join(self.testDataPath, "{}/{}.sim".format(title, title)))
            simulationInputs.read(filepath)

            self.assertEquals(title, simulationInputs.title)

            self.assertEquals("{}.sam".format(title), simulationInputs.specimenFilename)
            self.assertEquals("{}.mdl".format(title), simulationInputs.modelFilename)
            self.assertEquals("{}.mic".format(title), simulationInputs.microsopeFilename)
            self.assertEquals("{}.par".format(title), simulationInputs.simulationParametersFilename)

        # self.fail("Test if the testcase is working.")

    def test_read_1_1_1(self):
        """
        Tests for method `read`.
        """

        simulationInputs = SimulationInputs.SimulationInputs()

        title = "AlMgBulk5keV_version_1_1_1"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.sim".format(title)))
        simulationInputs.read(filepath)

        self.assertEquals(title, simulationInputs.title)

        self.assertEquals(version.VERSION_1_1_1.major, simulationInputs.version.major)
        self.assertEquals(version.VERSION_1_1_1.minor, simulationInputs.version.minor)
        self.assertEquals(version.VERSION_1_1_1.revision, simulationInputs.version.revision)
        self.assertEquals(version.VERSION_1_1_1, simulationInputs.version)

        self.assertEquals("{}.sam".format(title), simulationInputs.specimenFilename)
        self.assertEquals("{}.mdl".format(title), simulationInputs.modelFilename)
        self.assertEquals("{}.mic".format(title), simulationInputs.microsopeFilename)
        self.assertEquals("{}.par".format(title), simulationInputs.simulationParametersFilename)

        # self.fail("Test if the testcase is working.")

    def test_read_1_2_0(self):
        """
        Tests for method `read`.
        """

        simulationInputs = SimulationInputs.SimulationInputs()

        title = "AlMgBulk5keV_version_1_2_0"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.sim".format(title)))
        simulationInputs.read(filepath)

        self.assertEquals(title, simulationInputs.title)

        self.assertEquals(version.VERSION_1_2_0.major, simulationInputs.version.major)
        self.assertEquals(version.VERSION_1_2_0.minor, simulationInputs.version.minor)
        self.assertEquals(version.VERSION_1_2_0.revision, simulationInputs.version.revision)
        self.assertEquals(version.VERSION_1_2_0, simulationInputs.version)

        self.assertEquals("{}.sam".format(title), simulationInputs.specimenFilename)
        self.assertEquals("{}.mdl".format(title), simulationInputs.modelFilename)
        self.assertEquals("{}.mic".format(title), simulationInputs.microsopeFilename)
        self.assertEquals("{}.par".format(title), simulationInputs.simulationParametersFilename)

        # self.fail("Test if the testcase is working.")

    def test_read_1_2_1(self):
        """
        Tests for method `read`.
        """

        simulationInputs = SimulationInputs.SimulationInputs()

        title = "AlMgBulk5keV_version_1_2_1"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.sim".format(title)))
        simulationInputs.read(filepath)

        self.assertEquals(title, simulationInputs.title)

        self.assertEquals(version.VERSION_1_2_1.major, simulationInputs.version.major)
        self.assertEquals(version.VERSION_1_2_1.minor, simulationInputs.version.minor)
        self.assertEquals(version.VERSION_1_2_1.revision, simulationInputs.version.revision)
        self.assertEquals(version.VERSION_1_2_1, simulationInputs.version)

        self.assertEquals("{}.sam".format(title), simulationInputs.specimenFilename)
        self.assertEquals("{}.mdl".format(title), simulationInputs.modelFilename)
        self.assertEquals("{}.mic".format(title), simulationInputs.microsopeFilename)
        self.assertEquals("{}.par".format(title), simulationInputs.simulationParametersFilename)
        self.assertEquals("{}.mpp".format(title), simulationInputs.mapFilename)

        # self.fail("Test if the testcase is working.")

    def test_read_1_4_1(self):
        """
        Tests for method `read`.
        """

        simulationInputs = SimulationInputs.SimulationInputs()

        title = "AlMgBulk5keV_version_1_4_1"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.sim".format(title)))
        simulationInputs.read(filepath)

        self.assertEquals(title, simulationInputs.title)

        self.assertEquals(version.VERSION_1_4_1.major, simulationInputs.version.major)
        self.assertEquals(version.VERSION_1_4_1.minor, simulationInputs.version.minor)
        self.assertEquals(version.VERSION_1_4_1.revision, simulationInputs.version.revision)
        self.assertEquals(version.VERSION_1_4_1, simulationInputs.version)

        self.assertEquals("{}.sam".format(title), simulationInputs.specimenFilename)
        self.assertEquals("{}.mdl".format(title), simulationInputs.modelFilename)
        self.assertEquals("{}.mic".format(title), simulationInputs.microsopeFilename)
        self.assertEquals("{}.par".format(title), simulationInputs.simulationParametersFilename)
        self.assertEquals("{}.mpp".format(title), simulationInputs.mapFilename)
        self.assertEquals("{}.rp".format(title), simulationInputs.resultParametersFilename)

        # self.fail("Test if the testcase is working.")

    def test__createKeys(self):
        """
        Tests for method `_createKeys`.
        """

        numberKeys = 6

        keys = SimulationInputs.SimulationInputs()._createKeys()
        self.assertEquals(numberKeys, len(keys))

        # self.fail("Test if the testcase is working.")

    def test_write(self):
        """
        Tests for method `write`.
        """
        raise unittest.SkipTest("Test test_write not implemented")

        self.maxDiff = None

        # .. todo:: make test pass using testUtilities.getSimulationTitles().
        for title in ["BioRitchieNew111017"]:
            filepathReference = os.path.abspath(os.path.join(self.testDataPath, "{}/{}.sim".format(title, title)))

            filepath = os.path.join(self.tempDataPath, "{}.sim".format(title))
            simulationInputs = SimulationInputs.SimulationInputs()
            simulationInputs.write(filepath)

            self.assertEquals("{}.sam".format(title), simulationInputs.specimenFilename)
            self.assertEquals("{}.mdl".format(title), simulationInputs.modelFilename)
            self.assertEquals("{}.mic".format(title), simulationInputs.microsopeFilename)
            self.assertEquals("{}.par".format(title), simulationInputs.simulationParametersFilename)

            linesRef = open(filepathReference, 'r').readlines()
            lines = open(filepath, 'r').readlines()

            self.assertListEqual(linesRef, lines)

        # self.fail("Test if the testcase is working.")

    def test_write_1_1_1(self):
        """
        Tests for method `write`.
        """
        raise unittest.SkipTest("Test test_write_1_1_1 not implemented")

        self.maxDiff = None

        simulationInputsRef = SimulationInputs.SimulationInputs()
        simulationInputsRef.version = copy.deepcopy(version.VERSION_1_1_1)

        title = "AlMgBulk5keV_version_1_1_1"
        filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.sim".format(title)))
        simulationInputsRef.read(filepathReference)

        self.assertEquals(title, simulationInputsRef.title)

        filepath = os.path.join(self.tempDataPath, "{}.sim".format(title))
        simulationInputs = SimulationInputs.SimulationInputs()
        simulationInputs.version = copy.deepcopy(version.VERSION_1_1_1)
        simulationInputs.write(filepath)

        self.assertEquals("{}.sam".format(title), simulationInputs.specimenFilename)
        self.assertEquals("{}.mdl".format(title), simulationInputs.modelFilename)
        self.assertEquals("{}.mic".format(title), simulationInputs.microsopeFilename)
        self.assertEquals("{}.par".format(title), simulationInputs.simulationParametersFilename)

        self.assertEquals(simulationInputsRef.version.major, simulationInputs.version.major)
        self.assertEquals(simulationInputsRef.version.minor, simulationInputs.version.minor)
        self.assertEquals(simulationInputsRef.version.revision, simulationInputs.version.revision)
        self.assertEquals(simulationInputsRef.version, simulationInputs.version)

        linesRef = open(filepathReference, 'r').readlines()
        lines = open(filepath, 'r').readlines()

        self.assertListEqual(linesRef, lines)

        self.fail("Test if the testcase is working.")

    def test_write_1_2_0(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        simulationInputsRef = SimulationInputs.SimulationInputs()
        simulationInputsRef.version = copy.deepcopy(version.VERSION_1_2_0)

        title = "AlMgBulk5keV_version_1_2_0"
        filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.sim".format(title)))
        simulationInputsRef.read(filepathReference)

        self.assertEquals(title, simulationInputsRef.title)

        filepath = os.path.join(self.tempDataPath, "{}.sim".format(title))
        simulationInputs = SimulationInputs.SimulationInputs()
        simulationInputs.version = copy.deepcopy(version.VERSION_1_2_0)
        simulationInputs.write(filepath)

        self.assertEquals("{}.sam".format(title), simulationInputs.specimenFilename)
        self.assertEquals("{}.mdl".format(title), simulationInputs.modelFilename)
        self.assertEquals("{}.mic".format(title), simulationInputs.microsopeFilename)
        self.assertEquals("{}.par".format(title), simulationInputs.simulationParametersFilename)

        self.assertEquals(simulationInputsRef.version.major, simulationInputs.version.major)
        self.assertEquals(simulationInputsRef.version.minor, simulationInputs.version.minor)
        self.assertEquals(simulationInputsRef.version.revision, simulationInputs.version.revision)
        self.assertEquals(simulationInputsRef.version, simulationInputs.version)

        linesRef = open(filepathReference, 'r').readlines()
        lines = open(filepath, 'r').readlines()

        self.assertListEqual(linesRef, lines)

        # self.fail("Test if the testcase is working.")

    def test_write_1_2_1(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        simulationInputsRef = SimulationInputs.SimulationInputs()
        simulationInputsRef.version = copy.deepcopy(version.VERSION_1_2_1)

        title = "AlMgBulk5keV_version_1_2_1"
        filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.sim".format(title)))
        simulationInputsRef.read(filepathReference)

        self.assertEquals(title, simulationInputsRef.title)

        filepath = os.path.join(self.tempDataPath, "{}.sim".format(title))
        simulationInputs = SimulationInputs.SimulationInputs()
        simulationInputs.version = copy.deepcopy(version.VERSION_1_2_1)
        simulationInputs.write(filepath)

        self.assertEquals("{}.sam".format(title), simulationInputs.specimenFilename)
        self.assertEquals("{}.mdl".format(title), simulationInputs.modelFilename)
        self.assertEquals("{}.mic".format(title), simulationInputs.microsopeFilename)
        self.assertEquals("{}.par".format(title), simulationInputs.simulationParametersFilename)

        self.assertEquals(simulationInputsRef.version.major, simulationInputs.version.major)
        self.assertEquals(simulationInputsRef.version.minor, simulationInputs.version.minor)
        self.assertEquals(simulationInputsRef.version.revision, simulationInputs.version.revision)
        self.assertEquals(simulationInputsRef.version, simulationInputs.version)

        linesRef = open(filepathReference, 'r').readlines()
        lines = open(filepath, 'r').readlines()

        self.assertListEqual(linesRef, lines)

        # self.fail("Test if the testcase is working.")

    def test_write_1_4_1(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        simulationInputsRef = SimulationInputs.SimulationInputs()
        simulationInputsRef.version = copy.deepcopy(version.VERSION_1_4_1)

        title = "AlMgBulk5keV_version_1_4_1"
        filepathReference = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.sim".format(title)))
        simulationInputsRef.read(filepathReference)

        self.assertEquals(title, simulationInputsRef.title)

        filepath = os.path.join(self.tempDataPath, "{}.sim".format(title))
        simulationInputs = SimulationInputs.SimulationInputs()
        simulationInputs.version = version.Version(1, 4, 1)
        simulationInputs.write(filepath)

        self.assertEquals("{}.sam".format(title), simulationInputs.specimenFilename)
        self.assertEquals("{}.mdl".format(title), simulationInputs.modelFilename)
        self.assertEquals("{}.mic".format(title), simulationInputs.microsopeFilename)
        self.assertEquals("{}.par".format(title), simulationInputs.simulationParametersFilename)
        self.assertEquals("{}.mpp".format(title), simulationInputs.mapFilename)
        self.assertEquals("{}.rp".format(title), simulationInputs.resultParametersFilename)

        self.assertEquals(simulationInputsRef.version.major, simulationInputs.version.major)
        self.assertEquals(simulationInputsRef.version.minor, simulationInputs.version.minor)
        self.assertEquals(simulationInputsRef.version.revision, simulationInputs.version.revision)
        self.assertEquals(simulationInputsRef.version, simulationInputs.version)

        linesRef = open(filepathReference, 'r').readlines()
        lines = open(filepath, 'r').readlines()

        self.assertListEqual(linesRef, lines)

        # self.fail("Test if the testcase is working.")

    def test__extractTitleFromFilepath(self):
        """
        Tests for method `_extractTitleFromFilepath`.
        """

        simulationInputs = SimulationInputs.SimulationInputs()

        for titleRef in testUtilities.getSimulationTitles():
            filepath = os.path.abspath(os.path.join(self.testDataPath, "{}/{}.sim".format(titleRef, titleRef)))
            title = simulationInputs._extractTitleFromFilepath(filepath)

            self.assertEquals(titleRef, title)

        # self.fail("Test if the testcase is working.")
