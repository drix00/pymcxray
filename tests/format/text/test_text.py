#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.format.text

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`mcxray.format.text`.
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
import os

# Third party modules.

# Local modules.

# Project modules.
from mcxray.format.text import extract_basename


# Globals and constants variables.


class TestText(unittest.TestCase):
    """
    TestCase class for the module `${moduleName}`.
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
        self.assert_(True)

    def test_extract_basename(self):
        """
        Test extract_basename method.
        """

        basename_ref = "CuFeGrainBoundary20kV_5um"

        file_path = "CuFeGrainBoundary20kV_5um"
        basename = extract_basename(file_path)
        self.assertEqual(basename_ref, basename)

        file_path = "CuFeGrainBoundary20kV_5um.sim"
        basename = extract_basename(file_path)
        self.assertEqual(basename_ref, basename)

        if os.sep == '\\':
            file_path = r"C:\options\CuFeGrainBoundary20kV_5um\CuFeGrainBoundary20kV_5um.sim"
            basename = extract_basename(file_path)
            self.assertEqual(basename_ref, basename)

        # self.fail("Test if the testcase is working.")
        self.assert_(True)


if __name__ == '__main__':  # pragma: no cover
    import nose

    nose.runmodule()
