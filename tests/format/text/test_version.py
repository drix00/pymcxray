#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: format.text.test_version
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for module `version`.
"""

###############################################################################
# Copyright 2018 Hendrix Demers
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
import logging
import os.path

# Third party modules.

# Local modules.

# Project modules
from mcxray.format.text.version import write_line, read_from_file
from mcxray.format.version import Version
import tests.format.testUtilities as testUtilities

# Globals and constants variables.


class TestVersion(unittest.TestCase):
    """
    TestCase class for the module `version`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

        self.testDataPath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../test_data"))
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
        self.assertTrue(True)

    def test_read_from_file(self):
        """
        Tests for method `read_from_file`.
        """

        title = "AlMgBulk5keV_version_1_4_1"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.sim".format(title)))

        version = Version(0, 0, 0)
        read_from_file(version, filepath)

        string_ref = "1.4.1"
        version_string = version.to_string()
        self.assertEqual(string_ref, version_string)

        self.assertEqual(1, version.major)
        self.assertEqual(4, version.minor)
        self.assertEqual(1, version.revision)

        # self.fail("Test if the testcase is working.")

    def test_read_from_file_BadFile(self):
        """
        Tests for method `read_from_file`.
        """

        title = "AlMgBulk5keV_version_1_1_1"
        filepath = os.path.abspath(os.path.join(self.testDataPath, "inputs", "{}.snp".format(title)))

        version = Version(0, 0, 0)
        read_from_file(version, filepath)

        string_ref = "1.1.1"
        version_string = version.to_string()
        self.assertEqual(string_ref, version_string)
        self.assertEqual(1, version.major)
        self.assertEqual(1, version.minor)
        self.assertEqual(1, version.revision)

        # self.fail("Test if the testcase is working.")

    def test_write_line(self):
        """
        Tests for method `write_line`.
        """

        title = "AlMgBulk5keV_version_3_4_5"
        filepath = os.path.join(self.tempDataPath, "{}.sim".format(title))
        logging.info(filepath)
        version = Version(3, 4, 5)
        output_file = open(filepath, 'w')
        write_line(version, output_file)
        output_file.close()

        version = Version(0, 0, 0)
        read_from_file(version, filepath)

        string_ref = "3.4.5"
        version_string = version.to_string()
        self.assertEqual(string_ref, version_string)

        self.assertEqual(3, version.major)
        self.assertEqual(4, version.minor)
        self.assertEqual(5, version.revision)

        # self.fail("Test if the testcase is working.")
