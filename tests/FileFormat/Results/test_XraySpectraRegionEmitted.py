#!/usr/bin/env python
"""
.. py:currentmodule:: pymcxray.FileFormat.Results.test_XraySpectraRegionEmitted
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module `XraySpectraRegionEmitted`.
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
from pymcxray.FileFormat.Results.XraySpectraRegionEmitted import XraySpectraRegionEmitted

# Globals and constants variables.

class TestXraySpectraRegionEmitted(unittest.TestCase):
    """
    TestCase class for the module `XraySpectraRegionEmitted`.
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

    def test_readRegion_0_30kV(self):
        """
        Tests for method `readRegion_0`.
        """
        filename = "SimulationNanoparticleAg_Au_SpectraPerElectron_1_srkeV_Region_0.csv"
        filepath = os.path.join(self.testDataPath, filename)
        if not os.path.isfile(filepath):
            raise SkipTest

        spectra = XraySpectraRegionEmitted()
        spectra.path = self.testDataPath
        spectra.basename = "SimulationNanoparticleAg_Au"
        spectra.read()

        self.assertEqual(6000, len(spectra.energies_keV))
        self.assertEqual(6000, len(spectra.total_1_ekeVsr))
        self.assertEqual(6000, len(spectra.characteristic_1_ekeVsr))
        self.assertEqual(6000, len(spectra.bremsstrahlung_1_ekeVsr))

        self.assertAlmostEqual(0.0025, spectra.energies_keV[0], 6)
        self.assertAlmostEqual(29.9975, spectra.energies_keV[-1], 6)

        self.assertAlmostEqual(0.0, spectra.total_1_ekeVsr[0], 12)
        self.assertAlmostEqual(0.0, spectra.total_1_ekeVsr[-1], 12)

        self.assertAlmostEqual(0.0, spectra.characteristic_1_ekeVsr[0], 12)
        self.assertAlmostEqual(0.0, spectra.characteristic_1_ekeVsr[-1], 12)

        self.assertAlmostEqual(0.0, spectra.bremsstrahlung_1_ekeVsr[0], 12)
        self.assertAlmostEqual(0.0, spectra.bremsstrahlung_1_ekeVsr[-1], 12)

        # 58 0.2825, 0.0, 0.0, 0.0
        self.assertAlmostEqual(0.2825, spectra.energies_keV[56], 6)
        self.assertAlmostEqual(0.0, spectra.total_1_ekeVsr[56], 12)
        self.assertAlmostEqual(0.0, spectra.characteristic_1_ekeVsr[56], 12)
        self.assertAlmostEqual(0.0, spectra.bremsstrahlung_1_ekeVsr[56], 12)

        # 426 2.1225, 1.02186e-006, 8.96679e-007, 1.25179e-007
        self.assertAlmostEqual(2.1225, spectra.energies_keV[424], 6)
        self.assertAlmostEqual(0.0, spectra.total_1_ekeVsr[424], 12)
        self.assertAlmostEqual(0.0, spectra.characteristic_1_ekeVsr[424], 12)
        self.assertAlmostEqual(0.0, spectra.bremsstrahlung_1_ekeVsr[424], 12)

        # 598 2.9825, 0.0319011, 0.031818, 8.31376e-005
        self.assertAlmostEqual(2.9825, spectra.energies_keV[596], 6)
        self.assertAlmostEqual(0.0, spectra.total_1_ekeVsr[596], 12)
        self.assertAlmostEqual(0.0, spectra.characteristic_1_ekeVsr[596], 12)
        self.assertAlmostEqual(0.0, spectra.bremsstrahlung_1_ekeVsr[596], 12)

        #self.fail("Test if the testcase is working.")

    def test_readRegion_1_30kV(self):
        """
        Tests for method `readRegion_0`.
        """
        filename = "SimulationNanoparticleAg_Au_SpectraPerElectron_1_srkeV_Region_1.csv"
        filepath = os.path.join(self.testDataPath, filename)
        if not os.path.isfile(filepath):
            raise SkipTest

        spectra = XraySpectraRegionEmitted()
        spectra.path = self.testDataPath
        spectra.basename = "SimulationNanoparticleAg_Au"
        spectra.read(regionID=1)

        self.assertEqual(6000, len(spectra.energies_keV))
        self.assertEqual(6000, len(spectra.total_1_ekeVsr))
        self.assertEqual(6000, len(spectra.characteristic_1_ekeVsr))
        self.assertEqual(6000, len(spectra.bremsstrahlung_1_ekeVsr))

        self.assertAlmostEqual(0.0025, spectra.energies_keV[0], 6)
        self.assertAlmostEqual(29.9975, spectra.energies_keV[-1], 6)

        self.assertAlmostEqual(1.29326e-008, spectra.total_1_ekeVsr[0], 12)
        self.assertAlmostEqual(0.0, spectra.total_1_ekeVsr[-1], 12)

        self.assertAlmostEqual(0.0, spectra.characteristic_1_ekeVsr[0], 12)
        self.assertAlmostEqual(0.0, spectra.characteristic_1_ekeVsr[-1], 12)

        self.assertAlmostEqual(1.29326e-008, spectra.bremsstrahlung_1_ekeVsr[0], 12)
        self.assertAlmostEqual(0.0, spectra.bremsstrahlung_1_ekeVsr[-1], 12)

        # 58 0.2825, 1.12879e-006, 0, 1.12879e-006
        self.assertAlmostEqual(0.2825, spectra.energies_keV[56], 6)
        self.assertAlmostEqual(1.12879e-006, spectra.total_1_ekeVsr[56], 12)
        self.assertAlmostEqual(0.0, spectra.characteristic_1_ekeVsr[56], 12)
        self.assertAlmostEqual(1.12879e-006, spectra.bremsstrahlung_1_ekeVsr[56], 12)

        # 426 2.1225, 1.02186e-006, 8.96679e-007, 1.25179e-007
        self.assertAlmostEqual(2.1225, spectra.energies_keV[424], 6)
        self.assertAlmostEqual(1.02186e-006, spectra.total_1_ekeVsr[424], 12)
        self.assertAlmostEqual(8.96679e-007, spectra.characteristic_1_ekeVsr[424], 12)
        self.assertAlmostEqual(1.25179e-007, spectra.bremsstrahlung_1_ekeVsr[424], 12)

        # 598 2.9825, 8.64716e-008, 0, 8.64716e-008
        self.assertAlmostEqual(2.9825, spectra.energies_keV[596], 6)
        self.assertAlmostEqual(8.64716e-008, spectra.total_1_ekeVsr[596], 12)
        self.assertAlmostEqual(0.0, spectra.characteristic_1_ekeVsr[596], 12)
        self.assertAlmostEqual(8.64716e-008, spectra.bremsstrahlung_1_ekeVsr[596], 12)

        #self.fail("Test if the testcase is working.")

    def test_readRegion_2_30kV(self):
        """
        Tests for method `readRegion_0`.
        """
        filename = "SimulationNanoparticleAg_Au_SpectraPerElectron_1_srkeV_Region_2.csv"
        filepath = os.path.join(self.testDataPath, filename)
        if not os.path.isfile(filepath):
            raise SkipTest


        spectra = XraySpectraRegionEmitted()
        spectra.path = self.testDataPath
        spectra.basename = "SimulationNanoparticleAg_Au"
        spectra.read(regionID=2)

        self.assertEqual(6000, len(spectra.energies_keV))
        self.assertEqual(6000, len(spectra.total_1_ekeVsr))
        self.assertEqual(6000, len(spectra.characteristic_1_ekeVsr))
        self.assertEqual(6000, len(spectra.bremsstrahlung_1_ekeVsr))

        self.assertAlmostEqual(0.0025, spectra.energies_keV[0], 6)
        self.assertAlmostEqual(29.9975, spectra.energies_keV[-1], 6)

        self.assertAlmostEqual(1.47934e-006, spectra.total_1_ekeVsr[0], 12)
        self.assertAlmostEqual(0.0, spectra.total_1_ekeVsr[-1], 12)

        self.assertAlmostEqual(0.0, spectra.characteristic_1_ekeVsr[0], 12)
        self.assertAlmostEqual(0.0, spectra.characteristic_1_ekeVsr[-1], 12)

        self.assertAlmostEqual(1.47934e-006, spectra.bremsstrahlung_1_ekeVsr[0], 12)
        self.assertAlmostEqual(0.0, spectra.bremsstrahlung_1_ekeVsr[-1], 12)

        # 0.2825, 0.000126745, 0, 0.000126745
        self.assertAlmostEqual(0.2825, spectra.energies_keV[56], 6)
        self.assertAlmostEqual(0.000126745, spectra.total_1_ekeVsr[56], 12)
        self.assertAlmostEqual(0.0, spectra.characteristic_1_ekeVsr[56], 12)
        self.assertAlmostEqual(0.000126745, spectra.bremsstrahlung_1_ekeVsr[56], 12)

        # 426 2.1225, 8.165e-005, 0, 8.165e-005
        self.assertAlmostEqual(2.1225, spectra.energies_keV[424], 6)
        self.assertAlmostEqual(8.165e-005, spectra.total_1_ekeVsr[424], 12)
        self.assertAlmostEqual(0.0, spectra.characteristic_1_ekeVsr[424], 12)
        self.assertAlmostEqual(8.165e-005, spectra.bremsstrahlung_1_ekeVsr[424], 12)

        # 598 2.9825, 0.0319011, 0.031818, 8.31376e-005
        self.assertAlmostEqual(2.9825, spectra.energies_keV[596], 6)
        self.assertAlmostEqual(0.0319011, spectra.total_1_ekeVsr[596], 12)
        self.assertAlmostEqual(0.031818, spectra.characteristic_1_ekeVsr[596], 12)
        self.assertAlmostEqual(8.31376e-005, spectra.bremsstrahlung_1_ekeVsr[596], 12)

        #self.fail("Test if the testcase is working.")

    def test_readRegion_1_200kV(self):
        """
        Tests for method `readRegion_0`.
        """
        filename = "SimulationNanoparticleAg_C_SpectraPerElectron_1_srkeV_Region_1.csv"
        filepath = os.path.join(self.testDataPath, filename)
        if not os.path.isfile(filepath):
            raise SkipTest


        spectra = XraySpectraRegionEmitted()
        spectra.path = self.testDataPath
        spectra.basename = "SimulationNanoparticleAg_C"
        spectra.read(regionID=1)

        self.assertEqual(40000, len(spectra.energies_keV))
        self.assertEqual(40000, len(spectra.total_1_ekeVsr))
        self.assertEqual(40000, len(spectra.characteristic_1_ekeVsr))
        self.assertEqual(40000, len(spectra.bremsstrahlung_1_ekeVsr))

        self.assertAlmostEqual(0.0025, spectra.energies_keV[0], 6)
        self.assertAlmostEqual(199.998, spectra.energies_keV[-1], 6)

        self.assertAlmostEqual(1.18553e-011, spectra.total_1_ekeVsr[0], 17)
        self.assertAlmostEqual(0.0, spectra.total_1_ekeVsr[-1], 17)

        self.assertAlmostEqual(0.0, spectra.characteristic_1_ekeVsr[0], 17)
        self.assertAlmostEqual(0.0, spectra.characteristic_1_ekeVsr[-1], 17)

        self.assertAlmostEqual(1.18553e-011, spectra.bremsstrahlung_1_ekeVsr[0], 17)
        self.assertAlmostEqual(0.0, spectra.bremsstrahlung_1_ekeVsr[-1], 17)

        # 58 0.2825, 2.11852e-005, 2.11838e-005, 1.33965e-009
        self.assertAlmostEqual(0.2825, spectra.energies_keV[56], 6)
        self.assertAlmostEqual(2.11852e-005, spectra.total_1_ekeVsr[56], 17)
        self.assertAlmostEqual(2.11838e-005, spectra.characteristic_1_ekeVsr[56], 17)
        self.assertAlmostEqual(1.33965e-009, spectra.bremsstrahlung_1_ekeVsr[56], 17)

        # 426 2.1225, 7.34935e-009, 0, 7.34935e-009
        self.assertAlmostEqual(2.1225, spectra.energies_keV[424], 6)
        self.assertAlmostEqual(7.34935e-009, spectra.total_1_ekeVsr[424], 17)
        self.assertAlmostEqual(0.0, spectra.characteristic_1_ekeVsr[424], 17)
        self.assertAlmostEqual(7.34935e-009, spectra.bremsstrahlung_1_ekeVsr[424], 17)

        # 598 2.9825, 7.2569e-009, 0, 7.2569e-009
        self.assertAlmostEqual(2.9825, spectra.energies_keV[596], 6)
        self.assertAlmostEqual(7.2569e-009, spectra.total_1_ekeVsr[596], 17)
        self.assertAlmostEqual(0.0, spectra.characteristic_1_ekeVsr[596], 17)
        self.assertAlmostEqual(7.2569e-009, spectra.bremsstrahlung_1_ekeVsr[596], 17)

        #self.fail("Test if the testcase is working.")

    def test__indice(self):
        """
        Tests for method `_indice`.
        """
        filename = "SimulationNanoparticleAg_Au_SpectraPerElectron_1_srkeV_Region_1.csv"
        filepath = os.path.join(self.testDataPath, filename)
        if not os.path.isfile(filepath):
            raise SkipTest

        spectra = XraySpectraRegionEmitted()
        spectra.path = self.testDataPath
        spectra.basename = "SimulationNanoparticleAg_Au"
        spectra.read(regionID=1)

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
        self.assertRaises(IndexError, spectra._indice, 31.0)

        self.assertAlmostEqual(1.12879e-006, spectra.totalValue_1_ekeVsr(0.282), 12)
        self.assertAlmostEqual(1.02186e-006, spectra.totalValue_1_ekeVsr(2.123), 12)
        self.assertAlmostEqual(8.64716e-008, spectra.totalValue_1_ekeVsr(2.984), 12)

        self.assertAlmostEqual(0.0, spectra.characteristicValue_1_ekeVsr(0.282), 12)
        self.assertAlmostEqual(8.96679e-007, spectra.characteristicValue_1_ekeVsr(2.123), 12)
        self.assertAlmostEqual(0.0, spectra.characteristicValue_1_ekeVsr(2.984), 12)

        self.assertAlmostEqual(1.12879e-006, spectra.bremsstrahlungValue_1_ekeVsr(0.282), 12)
        self.assertAlmostEqual(1.25179e-007, spectra.bremsstrahlungValue_1_ekeVsr(2.123), 12)
        self.assertAlmostEqual(8.64716e-008, spectra.bremsstrahlungValue_1_ekeVsr(2.984), 12)

        # 66.82
        self.assertRaises(IndexError, spectra._indice, 66.82)

        spectra = XraySpectraRegionEmitted()
        spectra.path = self.testDataPath
        spectra.basename = "SimulationNanoparticleAg_C"
        spectra.read(regionID=1)

        self.assertEqual(13363, spectra._indice(66.82))
        self.assertAlmostEqual(0.0, spectra.characteristicValue_1_ekeVsr(66.82), 12)

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    import nose
    nose.runmodule()
