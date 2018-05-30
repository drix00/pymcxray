#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: format.test_version
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
from mcxray.format.version import *
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

    def test_to_string(self):
        """
        Tests for method `to_string`.
        """

        version = Version(1, 2, 3)
        string_ref = "1.2.3"
        version_string = version.to_string()
        self.assertEquals(string_ref, version_string)

        # self.fail("Test if the testcase is working.")

    def test_from_string(self):
        """
        Tests for method `from_string`.
        """

        version = Version(1, 2, 3)
        string_ref = "4.5.6"
        version.from_string(string_ref)
        version_string = version.to_string()
        self.assertEquals(string_ref, version_string)

        self.assertEquals(4, version.major)
        self.assertEquals(5, version.minor)
        self.assertEquals(6, version.revision)

        # self.fail("Test if the testcase is working.")

    def test_VersionConstants(self):
        """
        Tests for version constants.
        """

        string_ref = "1.1.1"
        version_string = VERSION_1_1_1.to_string()
        self.assertEquals(string_ref, version_string)
        self.assertEquals(1, VERSION_1_1_1.major)
        self.assertEquals(1, VERSION_1_1_1.minor)
        self.assertEquals(1, VERSION_1_1_1.revision)

        string_ref = "1.2.0"
        version_string = VERSION_1_2_0.to_string()
        self.assertEquals(string_ref, version_string)
        self.assertEquals(1, VERSION_1_2_0.major)
        self.assertEquals(2, VERSION_1_2_0.minor)
        self.assertEquals(0, VERSION_1_2_0.revision)

        string_ref = "1.2.1"
        version_string = VERSION_1_2_1.to_string()
        self.assertEquals(string_ref, version_string)
        self.assertEquals(1, VERSION_1_2_1.major)
        self.assertEquals(2, VERSION_1_2_1.minor)
        self.assertEquals(1, VERSION_1_2_1.revision)

        string_ref = "1.2.2"
        version_string = VERSION_1_2_2.to_string()
        self.assertEquals(string_ref, version_string)
        self.assertEquals(1, VERSION_1_2_2.major)
        self.assertEquals(2, VERSION_1_2_2.minor)
        self.assertEquals(2, VERSION_1_2_2.revision)

        string_ref = "1.2.3"
        version_string = VERSION_1_2_3.to_string()
        self.assertEquals(string_ref, version_string)
        self.assertEquals(1, VERSION_1_2_3.major)
        self.assertEquals(2, VERSION_1_2_3.minor)
        self.assertEquals(3, VERSION_1_2_3.revision)

        string_ref = "1.2.4"
        version_string = VERSION_1_2_4.to_string()
        self.assertEquals(string_ref, version_string)
        self.assertEquals(1, VERSION_1_2_4.major)
        self.assertEquals(2, VERSION_1_2_4.minor)
        self.assertEquals(4, VERSION_1_2_4.revision)

        string_ref = "1.2.5"
        version_string = VERSION_1_2_5.to_string()
        self.assertEquals(string_ref, version_string)
        self.assertEquals(1, VERSION_1_2_5.major)
        self.assertEquals(2, VERSION_1_2_5.minor)
        self.assertEquals(5, VERSION_1_2_5.revision)

        string_ref = "1.3.0"
        version_string = VERSION_1_3_0.to_string()
        self.assertEquals(string_ref, version_string)
        self.assertEquals(1, VERSION_1_3_0.major)
        self.assertEquals(3, VERSION_1_3_0.minor)
        self.assertEquals(0, VERSION_1_3_0.revision)

        string_ref = "1.4.0"
        version_string = VERSION_1_4_0.to_string()
        self.assertEquals(string_ref, version_string)
        self.assertEquals(1, VERSION_1_4_0.major)
        self.assertEquals(4, VERSION_1_4_0.minor)
        self.assertEquals(0, VERSION_1_4_0.revision)

        string_ref = "1.4.1"
        version_string = VERSION_1_4_1.to_string()
        self.assertEquals(string_ref, version_string)
        self.assertEquals(1, VERSION_1_4_1.major)
        self.assertEquals(4, VERSION_1_4_1.minor)
        self.assertEquals(1, VERSION_1_4_1.revision)

        string_ref = "1.4.2"
        version_string = VERSION_1_4_2.to_string()
        self.assertEquals(string_ref, version_string)
        self.assertEquals(1, VERSION_1_4_2.major)
        self.assertEquals(4, VERSION_1_4_2.minor)
        self.assertEquals(2, VERSION_1_4_2.revision)

        string_ref = "1.1.1"
        version_string = BEFORE_VERSION.to_string()
        self.assertEquals(string_ref, version_string)
        self.assertEquals(1, BEFORE_VERSION.major)
        self.assertEquals(1, BEFORE_VERSION.minor)
        self.assertEquals(1, BEFORE_VERSION.revision)

        self.assertEquals(VERSION_1_1_1, BEFORE_VERSION)
        self.assertNotEquals(VERSION_1_1_1, CURRENT_VERSION)

        string_ref = "1.5.2"
        version_string = CURRENT_VERSION.to_string()
        self.assertEquals(string_ref, version_string)
        self.assertEquals(1, CURRENT_VERSION.major)
        self.assertEquals(5, CURRENT_VERSION.minor)
        self.assertEquals(2, CURRENT_VERSION.revision)

        self.assertEquals(VERSION_1_5_2, CURRENT_VERSION)
        self.assertNotEquals(VERSION_1_5_2, BEFORE_VERSION)
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


if __name__ == '__main__':  # pragma: no cover
    import nose
    nose.runmodule()
