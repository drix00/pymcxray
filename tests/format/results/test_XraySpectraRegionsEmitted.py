#!/usr/bin/env python
"""
.. py:currentmodule:: mcxray.format.results.test_XraySpectraRegionsEmitted
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module `XraySpectraRegionsEmitted`.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = "0.1"
__date__ = "Feb 12, 2015"
__copyright__ = "Copyright (c) 2015 Hendrix Demers"
__license__ = "GPL 3"

# Standard library modules.
import unittest
import os.path

# Third party modules.
from nose import SkipTest

# Local modules.

# Project modules
from mcxray.format.results.XraySpectraRegionsEmitted import XraySpectraRegionsEmitted

# Globals and constants variables.

class TestXraySpectraRegionsEmitted(unittest.TestCase):
    """
    TestCase class for the module `XraySpectraRegionsEmitted`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)
        self.testDataPath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../test_data/results"))

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

    def test_readRegions_30kV(self):
        """
        Tests for method `readRegion_0`.
        """
        filename = "SimulationNanoparticleAg_Au_SpectraPerElectron_1_srkeV_Region_0.csv"
        filepath = os.path.join(self.testDataPath, filename)
        if not os.path.isfile(filepath):
            raise SkipTest("Test file not found: {}".format(filepath))

        spectra = XraySpectraRegionsEmitted()
        spectra.path = self.testDataPath
        spectra.basename = "SimulationNanoparticleAg_Au"
        spectra.read()

        self.assertEqual(6000, len(spectra.energies_keV))
        self.assertEqual(6000, len(spectra.total_1_ekeVsr))
        self.assertEqual(6000, len(spectra.characteristic_1_ekeVsr))
        self.assertEqual(6000, len(spectra.bremsstrahlung_1_ekeVsr))

        self.assertAlmostEqual(0.0025, spectra.energies_keV[0], 6)
        self.assertAlmostEqual(29.9975, spectra.energies_keV[-1], 6)

        self.assertAlmostEqual(0.0+1.29326e-008+1.47934e-006, spectra.total_1_ekeVsr[0], 12)
        self.assertAlmostEqual(0.0+0.0+0.0, spectra.total_1_ekeVsr[-1], 12)

        self.assertAlmostEqual(0.0+0.0+0.0, spectra.characteristic_1_ekeVsr[0], 12)
        self.assertAlmostEqual(0.0+0.0+0.0, spectra.characteristic_1_ekeVsr[-1], 12)

        self.assertAlmostEqual(0.0+1.29326e-008+1.47934e-006, spectra.bremsstrahlung_1_ekeVsr[0], 12)
        self.assertAlmostEqual(0.0+0.0+0.0, spectra.bremsstrahlung_1_ekeVsr[-1], 12)

        # 58 0.2825, 0.0, 0.0, 0.0
        self.assertAlmostEqual(0.2825, spectra.energies_keV[56], 6)
        self.assertAlmostEqual(0.0+1.12879e-006+0.000126745, spectra.total_1_ekeVsr[56], 12)
        self.assertAlmostEqual(0.0+0.0+0.0, spectra.characteristic_1_ekeVsr[56], 12)
        self.assertAlmostEqual(0.0+1.12879e-006+0.000126745, spectra.bremsstrahlung_1_ekeVsr[56], 12)

        # 426 2.1225, 1.02186e-006, 8.96679e-007, 1.25179e-007
        self.assertAlmostEqual(2.1225, spectra.energies_keV[424], 6)
        self.assertAlmostEqual(0.0+1.02186e-006+8.165e-005, spectra.total_1_ekeVsr[424], 12)
        self.assertAlmostEqual(0.0+8.96679e-007+0.0, spectra.characteristic_1_ekeVsr[424], 12)
        self.assertAlmostEqual(0.0+1.25179e-007+8.165e-005, spectra.bremsstrahlung_1_ekeVsr[424], 12)

        # 598 2.9825, 0.0319011, 0.031818, 8.31376e-005
        self.assertAlmostEqual(2.9825, spectra.energies_keV[596], 6)
        self.assertAlmostEqual(0.0+8.64716e-008+0.0319011, spectra.total_1_ekeVsr[596], 12)
        self.assertAlmostEqual(0.0+0.0+0.031818, spectra.characteristic_1_ekeVsr[596], 12)
        self.assertAlmostEqual(0.0+8.64716e-008+8.31376e-005, spectra.bremsstrahlung_1_ekeVsr[596], 12)

        #self.fail("Test if the testcase is working.")

    def test__indice(self):
        """
        Tests for method `_indice`.
        """
        filename = "SimulationNanoparticleAg_Au_SpectraPerElectron_1_srkeV_Region_1.csv"
        filepath = os.path.join(self.testDataPath, filename)
        if not os.path.isfile(filepath):
            raise SkipTest("Test file not found: {}".format(filepath))

        spectra = XraySpectraRegionsEmitted()
        spectra.path = self.testDataPath
        spectra.basename = "SimulationNanoparticleAg_Au"
        spectra.read()

        self.assertEqual(0, spectra._indice(0.0))
        self.assertEqual(0, spectra._indice(0.0024))
        self.assertEqual(0, spectra._indice(0.0025))
        self.assertEqual(0, spectra._indice(0.0026))
        self.assertEqual(0, spectra._indice(0.0049))
        self.assertEqual(0, spectra._indice(0.0050))
        self.assertEqual(1, spectra._indice(0.0051))

        self.assertEqual(56, spectra._indice(0.282))
        self.assertEqual(424, spectra._indice(2.123))
        self.assertEqual(596, spectra._indice(2.984))

        self.assertEqual(5999, spectra._indice(29.999))
        self.assertEqual(5999, spectra._indice(30.0))
        #self.assertRaises(IndexError, spectra._indice, 30.0)
        self.assertRaises(IndexError, spectra._indice, 31.0)

        self.assertAlmostEqual(1.12879e-006+0.000126745, spectra.totalValue_1_ekeVsr(0.282), 12)
        self.assertAlmostEqual(1.02186e-006+8.165e-005, spectra.totalValue_1_ekeVsr(2.123), 12)
        self.assertAlmostEqual(8.64716e-008+0.0319011, spectra.totalValue_1_ekeVsr(2.984), 12)

        self.assertAlmostEqual(0.0+0.0, spectra.characteristicValue_1_ekeVsr(0.282), 12)
        self.assertAlmostEqual(8.96679e-007, spectra.characteristicValue_1_ekeVsr(2.123), 12)
        self.assertAlmostEqual(0.0+0.031818, spectra.characteristicValue_1_ekeVsr(2.984), 12)

        self.assertAlmostEqual(1.12879e-006+0.000126745, spectra.bremsstrahlungValue_1_ekeVsr(0.282), 12)
        self.assertAlmostEqual(1.25179e-007+8.165e-005, spectra.bremsstrahlungValue_1_ekeVsr(2.123), 12)
        self.assertAlmostEqual(8.64716e-008+8.31376e-005, spectra.bremsstrahlungValue_1_ekeVsr(2.984), 12)

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    import nose
    nose.runmodule()
