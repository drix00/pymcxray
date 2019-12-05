#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.format.test_version

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for module :py:mod:`mcxray.format.version`.
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
import os.path

# Third party modules.

# Local modules.

# Project modules
from mcxray.format.version import *
import tests.format.testUtilities as testUtilities

# Globals and constants variables.


class TestVersion(unittest.TestCase):
    """
    TestCase class for the module :py:mod:`mcxray.format.version`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

        self.test_data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../test_data"))
        if not os.path.isdir(self.test_data_path):
            raise unittest.SkipTest("Test file not found: {}".format(self.test_data_path))

        self.tempDataPath = testUtilities.createTempDataPath(self.test_data_path)

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

    def test_to_string(self):
        """
        Tests for method `to_string`.
        """

        version = Version(1, 2, 3)
        string_ref = "1.2.3"
        version_string = version.to_string()
        self.assertEqual(string_ref, version_string)

        # self.fail("Test if the testcase is working.")

    def test_from_string(self):
        """
        Tests for method `from_string`.
        """

        version = Version(1, 2, 3)
        string_ref = "4.5.6"
        version.from_string(string_ref)
        version_string = version.to_string()
        self.assertEqual(string_ref, version_string)

        self.assertEqual(4, version.major)
        self.assertEqual(5, version.minor)
        self.assertEqual(6, version.revision)

        # Test function
        version_ref = Version(1, 2, 3)
        version_string = "1.2.3"
        version = from_string(version_string)
        self.assertEqual(version_ref, version)

        # self.fail("Test if the testcase is working.")

    def test_VersionConstants(self):
        """
        Tests for version constants.
        """

        string_ref = "1.1.1"
        version_string = VERSION_1_1_1.to_string()
        self.assertEqual(string_ref, version_string)
        self.assertEqual(1, VERSION_1_1_1.major)
        self.assertEqual(1, VERSION_1_1_1.minor)
        self.assertEqual(1, VERSION_1_1_1.revision)

        string_ref = "1.2.0"
        version_string = VERSION_1_2_0.to_string()
        self.assertEqual(string_ref, version_string)
        self.assertEqual(1, VERSION_1_2_0.major)
        self.assertEqual(2, VERSION_1_2_0.minor)
        self.assertEqual(0, VERSION_1_2_0.revision)

        string_ref = "1.2.1"
        version_string = VERSION_1_2_1.to_string()
        self.assertEqual(string_ref, version_string)
        self.assertEqual(1, VERSION_1_2_1.major)
        self.assertEqual(2, VERSION_1_2_1.minor)
        self.assertEqual(1, VERSION_1_2_1.revision)

        string_ref = "1.2.2"
        version_string = VERSION_1_2_2.to_string()
        self.assertEqual(string_ref, version_string)
        self.assertEqual(1, VERSION_1_2_2.major)
        self.assertEqual(2, VERSION_1_2_2.minor)
        self.assertEqual(2, VERSION_1_2_2.revision)

        string_ref = "1.2.3"
        version_string = VERSION_1_2_3.to_string()
        self.assertEqual(string_ref, version_string)
        self.assertEqual(1, VERSION_1_2_3.major)
        self.assertEqual(2, VERSION_1_2_3.minor)
        self.assertEqual(3, VERSION_1_2_3.revision)

        string_ref = "1.2.4"
        version_string = VERSION_1_2_4.to_string()
        self.assertEqual(string_ref, version_string)
        self.assertEqual(1, VERSION_1_2_4.major)
        self.assertEqual(2, VERSION_1_2_4.minor)
        self.assertEqual(4, VERSION_1_2_4.revision)

        string_ref = "1.2.5"
        version_string = VERSION_1_2_5.to_string()
        self.assertEqual(string_ref, version_string)
        self.assertEqual(1, VERSION_1_2_5.major)
        self.assertEqual(2, VERSION_1_2_5.minor)
        self.assertEqual(5, VERSION_1_2_5.revision)

        string_ref = "1.3.0"
        version_string = VERSION_1_3_0.to_string()
        self.assertEqual(string_ref, version_string)
        self.assertEqual(1, VERSION_1_3_0.major)
        self.assertEqual(3, VERSION_1_3_0.minor)
        self.assertEqual(0, VERSION_1_3_0.revision)

        string_ref = "1.4.0"
        version_string = VERSION_1_4_0.to_string()
        self.assertEqual(string_ref, version_string)
        self.assertEqual(1, VERSION_1_4_0.major)
        self.assertEqual(4, VERSION_1_4_0.minor)
        self.assertEqual(0, VERSION_1_4_0.revision)

        string_ref = "1.4.1"
        version_string = VERSION_1_4_1.to_string()
        self.assertEqual(string_ref, version_string)
        self.assertEqual(1, VERSION_1_4_1.major)
        self.assertEqual(4, VERSION_1_4_1.minor)
        self.assertEqual(1, VERSION_1_4_1.revision)

        string_ref = "1.4.2"
        version_string = VERSION_1_4_2.to_string()
        self.assertEqual(string_ref, version_string)
        self.assertEqual(1, VERSION_1_4_2.major)
        self.assertEqual(4, VERSION_1_4_2.minor)
        self.assertEqual(2, VERSION_1_4_2.revision)

        string_ref = "2.1.1"
        version_string = VERSION_2_1_1.to_string()
        self.assertEqual(string_ref, version_string)
        self.assertEqual(2, VERSION_2_1_1.major)
        self.assertEqual(1, VERSION_2_1_1.minor)
        self.assertEqual(1, VERSION_2_1_1.revision)

        string_ref = "1.1.1"
        version_string = BEFORE_VERSION.to_string()
        self.assertEqual(string_ref, version_string)
        self.assertEqual(1, BEFORE_VERSION.major)
        self.assertEqual(1, BEFORE_VERSION.minor)
        self.assertEqual(1, BEFORE_VERSION.revision)

        self.assertEqual(VERSION_1_1_1, BEFORE_VERSION)
        self.assertNotEqual(VERSION_1_1_1, CURRENT_VERSION)

        string_ref = "2.2.0"
        version_string = CURRENT_VERSION.to_string()
        self.assertEqual(string_ref, version_string)
        self.assertEqual(2, CURRENT_VERSION.major)
        self.assertEqual(2, CURRENT_VERSION.minor)
        self.assertEqual(0, CURRENT_VERSION.revision)

        self.assertEqual(VERSION_2_2_0, CURRENT_VERSION)
        self.assertNotEqual(VERSION_1_5_2, BEFORE_VERSION)
        self.assertFalse(VERSION_1_5_2 == BEFORE_VERSION)

        # self.fail("Test if the testcase is working.")

    def test_comparison(self):
        """
        Test comparison operation on `Version` class.
        """
        self.assertTrue(VERSION_1_2_0 == VERSION_1_2_0)
        self.assertFalse(VERSION_1_2_0 == VERSION_1_1_1)
        self.assertFalse(VERSION_1_2_0 == VERSION_1_2_1)

        self.assertFalse(VERSION_1_2_0 != VERSION_1_2_0)
        self.assertTrue(VERSION_1_2_0 != VERSION_1_1_1)
        self.assertTrue(VERSION_1_2_0 != VERSION_1_2_1)

        self.assertTrue(VERSION_1_2_0 > VERSION_1_1_1)
        self.assertTrue(VERSION_1_2_0 < VERSION_1_2_1)
        self.assertTrue(VERSION_1_1_1 < VERSION_1_2_0)
        self.assertTrue(VERSION_1_2_1 > VERSION_1_2_0)

        self.assertTrue(VERSION_1_2_0 >= VERSION_1_1_1)
        self.assertTrue(VERSION_1_2_0 <= VERSION_1_2_1)
        self.assertTrue(VERSION_1_1_1 <= VERSION_1_2_0)
        self.assertTrue(VERSION_1_2_1 >= VERSION_1_2_0)

        # self.fail("Test if the testcase is working.")
