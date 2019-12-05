#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.format.text.test_read

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`mcxray.format.text.read`.
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

# Project modules.
from mcxray.format.text.read import read_text_input, read_text_output
from mcxray import get_current_module_path
from tests.format.test_simulation import get_simulation_text_input_ref, get_simulation_text_output_ref


# Globals and constants variables.


class TestRead(unittest.TestCase):
    """
    TestCase class for the module :py:mod:`mcxray.format.text.read`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

    def tearDown(self):
        """
        Teardown method.
        """

        unittest.TestCase.tearDown(self)

    def testSkeleton(self):
        """
        First test to check if the testcase is working with the testing framework.
        """

        # self.fail("Test if the testcase is working.")
        self.assertTrue(True)

    def test_read_text_input(self):
        """
        Test method read_text_input.
        """

        file_path = r"..\..\..\test_data\format\text\options\CuFeGrainBoundary20kV_5um\CuFeGrainBoundary20kV_5um.sim"
        file_path = get_current_module_path(__file__, file_path)
        if not os.path.isfile(file_path):
            raise unittest.SkipTest("Test file not found: {}".format(file_path))

        simulation = read_text_input(file_path)

        simulation_ref = get_simulation_text_input_ref()

        self.assertEqual(simulation_ref, simulation)

        # self.fail("Test if the testcase is working.")
        self.assertTrue(True)

    def test_read_text_output(self):
        """
        Test method read_text_output.
        """

        path = r"..\..\..\test_data\format\text\results\CuFeGrainBoundary20kV_5um"
        basename = "CuFeGrainBoundary20kV"
        path = get_current_module_path(__file__, path)
        file_path = os.path.join(path, basename + "_Options.txt")
        if not os.path.isdir(path) or not os.path.isfile(file_path):
            raise unittest.SkipTest("Test file not found: {}".format(file_path))

        simulation = read_text_output(path, basename)

        simulation_ref = get_simulation_text_output_ref()

        self.assertEqual(simulation_ref, simulation)

        # self.fail("Test if the testcase is working.")
        self.assertTrue(True)
