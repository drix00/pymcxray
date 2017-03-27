#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.test_Spectra
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module `Spectra`.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2012 Hendrix Demers"
__license__ = ""

# Subversion informations for the file.
__svnRevision__ = "$Revision$"
__svnDate__ = "$Date$"
__svnId__ = "$Id$"

# Standard library modules.
import unittest
import logging
import os.path

# Third party modules.

# Local modules.

# Project modules
import pymcxray.FileFormat.Results.Spectra as Spectra

# Globals and constants variables.

class TestSpectra(unittest.TestCase):
    """
    TestCase class for the module `Spectra`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

        self.testDataPath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../test_data"))

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

    def test_read(self):
        """
        Tests for method `read`.
        """

        filepath = os.path.join(self.testDataPath, "autoSavedFiles", "McXRayXABX.txt")
        spectraFile = Spectra.Spectra()
        spectraFile.read(filepath)

        spectrum = spectraFile.getSpecimenSpectrum()
        energies_keV = spectrum.energies_keV
        intensities = spectrum.intensities
        backgrounds = spectrum.backgroundIntensities

        self.assertEquals(1024, len(energies_keV))
        self.assertEquals(1024, len(intensities))

        self.assertAlmostEquals(0.009766, energies_keV[0], 6)
        self.assertAlmostEquals(19.970703, energies_keV[-2], 6)
        self.assertAlmostEquals(19.990234, energies_keV[-1], 6)

        self.assertAlmostEquals(1.872409e+010, intensities[0], 6)
        self.assertAlmostEquals(1.561892e+012, intensities[-2], 6)
        self.assertAlmostEquals(0.000000e+000, intensities[-1], 6)

        self.assertAlmostEquals(1.872409e+010, backgrounds[0], 6)
        self.assertAlmostEquals(1.561892e+012, backgrounds[-2], 6)
        self.assertAlmostEquals(0.000000e+000, backgrounds[-1], 6)

        spectrum = spectraFile.getRegionSpectrum(0)
        energies_keV = spectrum.energies_keV
        intensities = spectrum.intensities
        backgrounds = spectrum.backgroundIntensities

        self.assertEquals(1024, len(energies_keV))
        self.assertEquals(1024, len(intensities))

        self.assertAlmostEquals(0.009766, energies_keV[0], 6)
        self.assertAlmostEquals(19.970703, energies_keV[-2], 6)
        self.assertAlmostEquals(19.990234, energies_keV[-1], 6)

        self.assertAlmostEquals(1.872409e+010, intensities[0], 6)
        self.assertAlmostEquals(1.561892e+012, intensities[-2], 6)
        self.assertAlmostEquals(0.000000e+000, intensities[-1], 6)

        self.assertAlmostEquals(1.872409e+010, backgrounds[0], 6)
        self.assertAlmostEquals(1.561892e+012, backgrounds[-2], 6)
        self.assertAlmostEquals(0.000000e+000, backgrounds[-1], 6)

        spectrum = spectraFile.getElementSpectrum(regionID=0, elementName="Carbon")
        energies_keV = spectrum.energies_keV
        intensities = spectrum.intensities

        self.assertEquals(1024, len(energies_keV))
        self.assertEquals(1024, len(intensities))

        self.assertAlmostEquals(0.009766, energies_keV[0], 6)
        self.assertAlmostEquals(0.185547, energies_keV[9], 6)
        self.assertAlmostEquals(0.380859, energies_keV[19], 6)
        self.assertAlmostEquals(19.990234, energies_keV[-1], 6)

        self.assertAlmostEquals(0.0, intensities[0], 6)
        self.assertAlmostEquals(2.822840e+014, intensities[9], 6)
        self.assertAlmostEquals(2.100012e+014, intensities[19], 6)
        self.assertAlmostEquals(0.000000e+000, intensities[-1], 6)

        #self.fail("Test if the testcase is working.")

    def test_readSpecimen(self):
        """
        Tests for method `readSpecimen`.
        """

        filepath = os.path.join(self.testDataPath, "autoSavedFiles", "McXRayXABX.txt")
        lines = open(filepath, 'r').readlines()[:1070]
        spectraFile = Spectra.Spectra()
        lineIndex = spectraFile.readSpecimen(lines)
        self.assertEquals(1067, lineIndex)

        spectrum = spectraFile.getSpecimenSpectrum()
        energies_keV = spectrum.energies_keV
        intensities = spectrum.intensities
        backgrounds = spectrum.backgroundIntensities

        self.assertEquals(1024, len(energies_keV))
        self.assertEquals(1024, len(intensities))

        self.assertAlmostEquals(0.009766, energies_keV[0], 6)
        self.assertAlmostEquals(19.970703, energies_keV[-2], 6)
        self.assertAlmostEquals(19.990234, energies_keV[-1], 6)

        self.assertAlmostEquals(1.872409e+010, intensities[0], 6)
        self.assertAlmostEquals(1.561892e+012, intensities[-2], 6)
        self.assertAlmostEquals(0.000000e+000, intensities[-1], 6)

        self.assertAlmostEquals(1.872409e+010, backgrounds[0], 6)
        self.assertAlmostEquals(1.561892e+012, backgrounds[-2], 6)
        self.assertAlmostEquals(0.000000e+000, backgrounds[-1], 6)

        #self.fail("Test if the testcase is working.")

    def test_readRegion(self):
        """
        Tests for method `readRegion`.
        """

        filepath = os.path.join(self.testDataPath, "autoSavedFiles", "McXRayXABX.txt")
        lines = open(filepath, 'r').readlines()[1069:3143]
        spectraFile = Spectra.Spectra()
        spectraFile.readRegion(lines)

        regionParameters = spectraFile.getRegionParameters(0)

        self.assertEquals(0, regionParameters.regionID)
        self.assertEquals(1, regionParameters.numberElements)

        element = regionParameters.elements[0]
        self.assertEquals("Carbon", element.name)
        self.assertAlmostEquals(1.0, element.massFraction, 6)

        self.assertAlmostEquals(346.177758, regionParameters.layerThickness_A, 6)

        spectrum = spectraFile.getRegionSpectrum(0)
        energies_keV = spectrum.energies_keV
        intensities = spectrum.intensities
        backgrounds = spectrum.backgroundIntensities

        self.assertEquals(1024, len(energies_keV))
        self.assertEquals(1024, len(intensities))

        self.assertAlmostEquals(0.009766, energies_keV[0], 6)
        self.assertAlmostEquals(19.970703, energies_keV[-2], 6)
        self.assertAlmostEquals(19.990234, energies_keV[-1], 6)

        self.assertAlmostEquals(1.872409e+010, intensities[0], 6)
        self.assertAlmostEquals(1.561892e+012, intensities[-2], 6)
        self.assertAlmostEquals(0.000000e+000, intensities[-1], 6)

        self.assertAlmostEquals(1.872409e+010, backgrounds[0], 6)
        self.assertAlmostEquals(1.561892e+012, backgrounds[-2], 6)
        self.assertAlmostEquals(0.000000e+000, backgrounds[-1], 6)

        #self.fail("Test if the testcase is working.")

    def test__extractRegionHeader(self):
        """
        Tests for method `_extractRegionHeader`.
        """

        lines = \
"""Region 0 number of elements = 1
   Weight fraction of Carbon = 1.000000
Thickness of layers in phi-ro-z = 346.177758 (A)
""".splitlines()

        spectraFile = Spectra.Spectra()
        regionParameters = spectraFile._extractRegionHeader(lines)

        self.assertEquals(0, regionParameters.regionID)
        self.assertEquals(1, regionParameters.numberElements)

        element = regionParameters.elements[0]
        self.assertEquals("Carbon", element.name)
        self.assertAlmostEquals(1.0, element.massFraction, 6)

        self.assertAlmostEquals(346.177758, regionParameters.layerThickness_A, 6)

        #self.fail("Test if the testcase is working.")

    def test__extractElementHeader(self):
        """
        Tests for method `_extractElementHeader`.
        """

        lines = \
"""Carbon weight fraction = 1.000000


Emitted Intensity
   Ka 6.000000 1.794839e+006 (photon/e/str)
   Ka 6.000000 1.407736e+018 (photon)
Generated Intensity
   Ka 6.000000 1.589397e-007 (photon/e/str)
Peak to Background
   Ka 6.000000 0.000000e+000


Ratio of emitted x-ray Intensity to absorbed energy = 3.439050e-018
Ratio of emitted x-ray Intensity times energy to absorbed energy = 6.281129e-018

""".splitlines()

        spectraFile = Spectra.Spectra()
        elementParameters = spectraFile._extractElementHeader(lines)

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from pymcxray.Testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__)
