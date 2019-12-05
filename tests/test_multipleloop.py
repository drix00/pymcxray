#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.test_multipleloop

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`mcxray.multipleloop`.
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

# Third party modules.

# Local modules.

# Project modules.
from mcxray.multipleloop import combine


# Globals and constants variables.


class TestMultipleloop(unittest.TestCase):
    """
    TestCase class for the module `mcxray.multipleloop`.
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

    def test_combine(self):
        """
        Test the combine method.
        """
        import numpy as np
        dx = np.array([1.0 / 2 ** k for k in range(2, 5)])
        self.assertListEqual([0.25, 0.125, 0.0625, ], list(dx))
        dt = 3 * dx
        dt = dt[:-1]
        dx = list(dx)
        dt = list(dt)
        self.assertListEqual([0.75, 0.375, ], list(dt))
        p = {'dt': dt, 'dx': dx}

        self.assertEqual({'dt': [0.75, 0.375, ], 'dx': [0.25, 0.125, 0.0625, ]}, p)

        all_combination, names, varied = combine(p)
        self.assertListEqual([[0.75, 0.25], [0.375, 0.25], [0.75, 0.125],
                              [0.375, 0.125], [0.75, 0.0625], [0.375, 0.0625]], all_combination)

        # self.fail("Test if the testcase is working.")
