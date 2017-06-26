#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: test_Simulation
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module `Simulation`.
"""

###############################################################################
# Copyright 2017 Hendrix Demers
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

# Project modules
# import pymcxray.Simulation as Simulation
from pymcxray.Simulation import create_weight_fractions, Layer, create_multi_horizontal_layer

# Globals and constants variables.


class TestSimulation(unittest.TestCase):
    """
    TestCase class for the module `Simulation`.
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

    def test_create_weight_fractions(self):
        """
        First test to check if the testcase is working with the testing framework.
        """

        weight_fraction_ref = [0, 0.25, 0.5, 0.75, 1.0]
        weight_fraction_values = create_weight_fractions(0.25, 1)
        self.assertListEqual(weight_fraction_ref, list(weight_fraction_values))

        weight_fraction_ref = [(0.0, 1.0),
                               (0.25, 0.75),
                               (0.5, 0.5),
                               (0.75, 0.25),
                               (1.0, 0.0)]
        weight_fraction_values = create_weight_fractions(0.25, 2)
        self.assertListEqual(weight_fraction_ref, weight_fraction_values)

        weight_fraction_ref = [(0.0, 0.0, 1.0),
                               (0.0, 0.25, 0.75),
                               (0.0, 0.5, 0.5),
                               (0.0, 0.75, 0.25),
                               (0.0, 1.0, 0.0),
                               (0.25, 0.0, 0.75),
                               (0.25, 0.25, 0.5),
                               (0.25, 0.5, 0.25),
                               (0.25, 0.75, 0.0),
                               (0.5, 0.0, 0.5),
                               (0.5, 0.25, 0.25),
                               (0.5, 0.5, 0.0),
                               (0.75, 0.0, 0.25),
                               (0.75, 0.25, 0.0),
                               (1.0, 0.0, 0.0)]
        weight_fraction_values = create_weight_fractions(0.25, 3)
        self.assertListEqual(weight_fraction_ref, weight_fraction_values)

        weight_fraction_ref = [(0.0, 0.0, 0.0, 1.0),
                               (0.0, 0.0, 0.25, 0.75),
                               (0.0, 0.0, 0.5, 0.5),
                               (0.0, 0.0, 0.75, 0.25),
                               (0.0, 0.0, 1.0, 0.0),
                               (0.0, 0.25, 0.0, 0.75),
                               (0.0, 0.25, 0.25, 0.5),
                               (0.0, 0.25, 0.5, 0.25),
                               (0.0, 0.25, 0.75, 0.0),
                               (0.0, 0.5, 0.0, 0.5),
                               (0.0, 0.5, 0.25, 0.25),
                               (0.0, 0.5, 0.5, 0.0),
                               (0.0, 0.75, 0.0, 0.25),
                               (0.0, 0.75, 0.25, 0.0),
                               (0.0, 1.0, 0.0, 0.0),
                               (0.25, 0.0, 0.0, 0.75),
                               (0.25, 0.0, 0.25, 0.50),
                               (0.25, 0.0, 0.50, 0.25),
                               (0.25, 0.0, 0.75, 0.0),
                               (0.25, 0.25, 0.0, 0.50),
                               (0.25, 0.25, 0.25, 0.25),
                               (0.25, 0.25, 0.50, 0.0),
                               (0.25, 0.5, 0.0, 0.25),
                               (0.25, 0.5, 0.25, 0.0),
                               (0.25, 0.75, 0.0, 0.0),
                               (0.50, 0.0, 0.0, 0.50),
                               (0.50, 0.0, 0.25, 0.25),
                               (0.50, 0.0, 0.50, 0.0),
                               (0.50, 0.25, 0.0, 0.25),
                               (0.50, 0.25, 0.25, 0.0),
                               (0.50, 0.50, 0.0, 0.0),
                               (0.75, 0.0, 0.0, 0.25),
                               (0.75, 0.0, 0.25, 0.0),
                               (0.75, 0.25, 0.0, 0.0),
                               (1.0, 0.0, 0.0, 0.0)]
        weight_fraction_values = create_weight_fractions(0.25, 4)
        self.assertListEqual(weight_fraction_ref, weight_fraction_values)

        weight_fraction_ref = [(0.0, 1.0),
                               (0.5, 0.5),
                               (1.0, 0.0)]
        weight_fraction_values = create_weight_fractions(0.50, 2)
        self.assertListEqual(weight_fraction_ref, weight_fraction_values)

        weight_fraction_ref = [(0.0, 0.0, 1.0),
                               (0.0, 0.5, 0.5),
                               (0.0, 1.0, 0.0),
                               (0.5, 0.0, 0.5),
                               (0.5, 0.5, 0.0),
                               (1.0, 0.0, 0.0)]
        weight_fraction_values = create_weight_fractions(0.50, 3)
        self.assertListEqual(weight_fraction_ref, weight_fraction_values)

        weight_fraction_ref = [(0.0, 0.0, 0.0, 1.0),
                               (0.0, 0.0, 0.5, 0.5),
                               (0.0, 0.0, 1.0, 0.0),
                               (0.0, 0.5, 0.0, 0.5),
                               (0.0, 0.5, 0.5, 0.0),
                               (0.0, 1.0, 0.0, 0.0),
                               (0.50, 0.0, 0.0, 0.50),
                               (0.50, 0.0, 0.50, 0.0),
                               (0.50, 0.50, 0.0, 0.0),
                               (1.0, 0.0, 0.0, 0.0)]
        weight_fraction_values = create_weight_fractions(0.50, 4)
        self.assertListEqual(weight_fraction_ref, weight_fraction_values)

        # self.fail("Test if the testcase is working.")

    def test_create_multi_horizontal_layer(self):
        """
        Test the `create_multi_horizontal_layer` method.
        """

        substrate_elements = [(14, 1.0)]
        layers = []

        # 10.0 nm Al layer
        al_layer = Layer([(13, 1.0)], 10.0)
        layers.append(al_layer)

        mg_cu_layer = Layer([(12, 0.5), (29, 0.5)], 150.2)
        layers.append(mg_cu_layer)

        specimen = create_multi_horizontal_layer(substrate_elements, layers)

        self.assertEqual(3, specimen.numberRegions)

        self.assertEqual(1, specimen.regions[0].numberElements)
        self.assertEqual(1, specimen.regions[1].numberElements)
        self.assertEqual(2, specimen.regions[2].numberElements)

        self.assertAlmostEqual(0.0, specimen.regions[0].regionDimensions.minimumZ)
        self.assertAlmostEqual(0.0, specimen.regions[1].regionDimensions.minimumZ)
        self.assertAlmostEqual(100.0, specimen.regions[2].regionDimensions.minimumZ)

        self.assertAlmostEqual(20000000000.0, specimen.regions[0].regionDimensions.maximumZ)
        self.assertAlmostEqual(100.0, specimen.regions[1].regionDimensions.maximumZ)
        self.assertAlmostEqual(100.0 + 1502.0, specimen.regions[2].regionDimensions.maximumZ)

        self.assertEqual("Si100_Al100_T100.0nm_Mg50_Cu50_T1502.0nm", specimen.name)

        # self.fail("Test if the testcase is working.")


if __name__ == '__main__':  # pragma: no cover
    import nose
    nose.runmodule()
