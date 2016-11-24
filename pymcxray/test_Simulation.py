#!/usr/bin/env python
"""
.. py:currentmodule:: test_Simulation
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module `Simulation`.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2012 Hendrix Demers"
__license__ = ""

# Standard library modules.
import unittest
import logging

# Third party modules.

# Local modules.

# Project modules
import pymcxray.Simulation as Simulation
from pymcxray.Simulation import create_weight_fractions

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

        #self.fail("Test if the testcase is working.")
        self.assert_(True)
    
    
    def test_create_weight_fractions2(self):
        """
        First test to check if the testcase is working with the testing framework.
        """

        weight_fraction_ref = [0, 0.25, 0.5, 0.75, 1.0]
        weight_fraction_values = create_weight_fractions(0.25, 1)
        self.assertEqual((5, ), weight_fraction_values.shape)
        self.assertListEqual(weight_fraction_ref, list(weight_fraction_values))

        weight_fraction_ref = [[0.0, 1.0],
                               [0.25, 0.75],
                               [0.5, 0.5],
                               [0.75, 0.25],
                               [1.0, 0.0]]
        weight_fraction_values = create_weight_fractions(0.25, 2)
        self.assertEqual((5, 2), weight_fraction_values.shape)
        self.assertListEqual(weight_fraction_ref, weight_fraction_values.tolist())

        weight_fraction_ref = [[0.0, 0.0, 1.0],
                               [0.0, 0.25, 0.75],
                               [0.0, 0.5, 0.5],
                               [0.0, 0.75, 0.25],
                               [0.0, 1.0, 0.0],
                               [0.25, 0.0, 0.75],
                               [0.25, 0.25, 0.5],
                               [0.25, 0.5, 0.25],
                               [0.25, 0.75, 0.0],
                               [0.5, 0.0, 0.5],
                               [0.5, 0.25, 0.25],
                               [0.5, 0.5, 0.0],
                               [0.75, 0.0, 0.25],
                               [0.75, 0.25, 0.0],
                               [1.0, 0.0, 0.0]]
        weight_fraction_values = create_weight_fractions(0.25, 3)
        self.assertEqual((15, 3), weight_fraction_values.shape)
        self.assertListEqual(weight_fraction_ref, weight_fraction_values.tolist())

        weight_fraction_ref = [[0.0, 0.0, 0.0, 1.0],
                               [0.0, 0.0, 0.25, 0.75],
                               [0.0, 0.0, 0.5, 0.5],
                               [0.0, 0.0, 0.75, 0.25],
                               [0.0, 0.0, 1.0, 0.0],
                               [0.0, 0.25, 0.0, 0.75],
                               [0.0, 0.25, 0.25, 0.5],
                               [0.0, 0.25, 0.5, 0.25],
                               [0.0, 0.25, 0.75, 0.0],
                               [0.0, 0.5, 0.0, 0.5],
                               [0.0, 0.5, 0.25, 0.25],
                               [0.0, 0.5, 0.5, 0.0],
                               [0.0, 0.75, 0.0, 0.25],
                               [0.0, 0.75, 0.25, 0.0],
                               [0.0, 1.0, 0.0, 0.0],
                               [0.25, 0.0, 0.0, 0.75],
                               [0.25, 0.0, 0.25, 0.50],
                               [0.25, 0.0, 0.50, 0.25],
                               [0.25, 0.0, 0.75, 0.0],
                               [0.25, 0.25, 0.0, 0.50],
                               [0.25, 0.25, 0.25, 0.25],
                               [0.25, 0.25, 0.50, 0.0],
                               [0.25, 0.5, 0.0, 0.25],
                               [0.25, 0.5, 0.25, 0.0],
                               [0.25, 0.75, 0.0, 0.0],
                               [0.50, 0.0, 0.0, 0.50],
                               [0.50, 0.0, 0.25, 0.25],
                               [0.50, 0.0, 0.50, 0.0],
                               [0.50, 0.25, 0.0, 0.25],
                               [0.50, 0.25, 0.25, 0.0],
                               [0.50, 0.50, 0.0, 0.0],
                               [0.75, 0.0, 0.0, 0.25],
                               [0.75, 0.0, 0.25, 0.0],
                               [0.75, 0.25, 0.0, 0.0],
                               [1.0, 0.0, 0.0, 0.0]]
        weight_fraction_values = create_weight_fractions(0.25, 4)
        self.assertEqual((35, 4), weight_fraction_values.shape)
        self.assertListEqual(weight_fraction_ref, weight_fraction_values.tolist())
        
        weight_fraction_ref = [[0.0, 1.0],
                               [0.5, 0.5],
                               [1.0, 0.0]]
        weight_fraction_values = create_weight_fractions(0.50, 2)
        self.assertEqual((3, 2), weight_fraction_values.shape)
        self.assertListEqual(weight_fraction_ref, weight_fraction_values.tolist())

        weight_fraction_ref = [[0.0, 0.0, 1.0],
                               [0.0, 0.5, 0.5],
                               [0.0, 1.0, 0.0],
                               [0.5, 0.0, 0.5],
                               [0.5, 0.5, 0.0],
                               [1.0, 0.0, 0.0]]
        weight_fraction_values = create_weight_fractions(0.50, 3)
        self.assertEqual((6, 3), weight_fraction_values.shape)
        self.assertListEqual(weight_fraction_ref, weight_fraction_values.tolist())

        weight_fraction_ref = [[0.0, 0.0, 0.0, 1.0],
                               [0.0, 0.0, 0.5, 0.5],
                               [0.0, 0.0, 1.0, 0.0],
                               [0.0, 0.5, 0.0, 0.5],
                               [0.0, 0.5, 0.5, 0.0],
                               [0.0, 1.0, 0.0, 0.0],
                               [0.50, 0.0, 0.0, 0.50],
                               [0.50, 0.0, 0.50, 0.0],
                               [0.50, 0.50, 0.0, 0.0],
                               [1.0, 0.0, 0.0, 0.0]]
        weight_fraction_values = create_weight_fractions(0.50, 4)
        self.assertEqual((10, 4), weight_fraction_values.shape)
        self.assertListEqual(weight_fraction_ref, weight_fraction_values.tolist())

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    import nose

    nose.runmodule()
