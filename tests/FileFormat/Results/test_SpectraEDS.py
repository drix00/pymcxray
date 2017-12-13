#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.test_SpectraEDS
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for module `SpectraEDS`.
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
import os.path

# Third party modules.

# Local modules.

# Project modules
import pymcxray.FileFormat.Results.SpectraEDS as SpectraEDS

# Globals and constants variables.

class TestSpectraEDS(unittest.TestCase):
    """
    TestCase class for the module `SpectraEDS`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

        self.testDataPath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../test_data"))

        self.spectraEdsRegion0Filepath = os.path.join(self.testDataPath, "version1.1/autoSavedFiles/DetectionLimits_N1000x_C_r10A_z11A_Au_E30d0keVEDSRegion0.txt")
        self.spectraEdsRegion1Filepath = os.path.join(self.testDataPath, "version1.1/autoSavedFiles/DetectionLimits_N1000x_C_r10A_z11A_Au_E30d0keVEDSRegion1.txt")

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

    def test_FindTestData(self):
        """
        Tests for method `FindTestData`.
        """

        self.assertTrue(os.path.isfile(self.spectraEdsRegion0Filepath))
        self.assertTrue(os.path.isfile(self.spectraEdsRegion1Filepath))

        #self.fail("Test if the testcase is working.")

    def test__isTestInputSection(self):
        """
        Tests for method `_isTestInputSection`.
        """

        lines = open(self.spectraEdsRegion0Filepath, 'r').readlines()
        self.assertFalse(SpectraEDS.SpectraEDS()._isTestInputSection(lines))

        lines = open(self.spectraEdsRegion1Filepath, 'r').readlines()
        self.assertFalse(SpectraEDS.SpectraEDS()._isTestInputSection(lines))

        lines = """TEST INPUT - START
E_C = %7.5e, I_C = %15.14e

E_Brut = %7.5e, I_Brut = %15.14e
E_Brut = %7.5e, I_Brut = %15.14e
E_Brut = %7.5e, I_Brut = %15.14e
E_Brut = %7.5e, I_Brut = %15.14e
E_Brut = %7.5e, I_Brut = %15.14e
TEST INPUT - STOP

        """.splitlines()
        self.assertTrue(SpectraEDS.SpectraEDS()._isTestInputSection(lines))

        #self.fail("Test if the testcase is working.")

    def test_readTestInputSection(self):
        """
        Tests for method `readTestInputSection`.
        """

        lines = """TEST INPUT - START
E_C = %7.5e, I_C = %15.14e

E_Brut = %7.5e, I_Brut = %15.14e
E_Brut = %7.5e, I_Brut = %15.14e
E_Brut = %7.5e, I_Brut = %15.14e
E_Brut = %7.5e, I_Brut = %15.14e
E_Brut = %7.5e, I_Brut = %15.14e
TEST INPUT - STOP

        """.splitlines()

        self.assertRaises(NotImplementedError, SpectraEDS.SpectraEDS().readTestInputSection, lines)

        #self.fail("Test if the testcase is working.")

    def test__isPartialSpectraReferenceSection(self):
        """
        Tests for method `_isTestInputSection`.
        """

        lines = open(self.spectraEdsRegion0Filepath, 'r').readlines()
        lines =[line.strip() for line in lines]
        self.assertTrue(SpectraEDS.SpectraEDS()._isPartialSpectraReferenceSection(lines))

        lines = open(self.spectraEdsRegion1Filepath, 'r').readlines()
        lines =[line.strip() for line in lines]
        self.assertTrue(SpectraEDS.SpectraEDS()._isPartialSpectraReferenceSection(lines))

        lines = """TEST INPUT - START
E_C = %7.5e, I_C = %15.14e

E_Brut = %7.5e, I_Brut = %15.14e
E_Brut = %7.5e, I_Brut = %15.14e
E_Brut = %7.5e, I_Brut = %15.14e
E_Brut = %7.5e, I_Brut = %15.14e
E_Brut = %7.5e, I_Brut = %15.14e
TEST INPUT - STOP

        """.splitlines()
        lines =[line.strip() for line in lines]
        self.assertFalse(SpectraEDS.SpectraEDS()._isPartialSpectraReferenceSection(lines))

        #self.fail("Test if the testcase is working.")

    def test_readPartialSpectraReferenceSection(self):
        """
        Tests for method `readTestInputSection`.
        """

        lines = """TEST INPUT - START
E_C = %7.5e, I_C = %15.14e

E_Brut = %7.5e, I_Brut = %15.14e
E_Brut = %7.5e, I_Brut = %15.14e
E_Brut = %7.5e, I_Brut = %15.14e
E_Brut = %7.5e, I_Brut = %15.14e
E_Brut = %7.5e, I_Brut = %15.14e
TEST INPUT - STOP

        """.splitlines()

        self.assertRaises(ValueError, SpectraEDS.SpectraEDS().readPartialSpectraReferenceSection, lines)

        lines = open(self.spectraEdsRegion0Filepath, 'r').readlines()
        lines =[line.strip() for line in lines]
        self.assertEquals(2097, SpectraEDS.SpectraEDS().readPartialSpectraReferenceSection(lines))

        lines = open(self.spectraEdsRegion1Filepath, 'r').readlines()
        lines =[line.strip() for line in lines]
        self.assertEquals(2097, SpectraEDS.SpectraEDS().readPartialSpectraReferenceSection(lines))

        #self.fail("Test if the testcase is working.")

    def test__extractTotalCounts(self):
        """
        Tests for method `_extractTotalCounts`.
        """

        line = "Counts original = 4.04611496446304e+011, Counts original inter = 4.04611496446304e+011, Counts syn = 3.83700037049714e+008"
        totalCountsOriginalRef = 4.04611496446304e+011
        totalCountsInterpolatedRef = 4.04611496446304e+011
        totalCountsSyntheticRef = 3.83700037049714e+008
        totalCountsOriginal, totalCountsInterpolated, totalCountsSynthetic = SpectraEDS.SpectraEDS()._extractTotalCounts(line)
        self.assertAlmostEquals(totalCountsOriginalRef, totalCountsOriginal, delta=1.0e4)
        self.assertAlmostEquals(totalCountsInterpolatedRef, totalCountsInterpolated, delta=1.0e4)
        self.assertAlmostEquals(totalCountsSyntheticRef, totalCountsSynthetic, delta=1.0e1)

        line = "Counts original = 3.16018197208457e+007, Counts original inter = 3.16018197208457e+007, Counts syn = 2.70058535894877e+004"
        totalCountsOriginalRef = 3.16018197208457e+007
        totalCountsInterpolatedRef = 3.16018197208457e+007
        totalCountsSyntheticRef = 2.70058535894877e+004
        totalCountsOriginal, totalCountsInterpolated, totalCountsSynthetic = SpectraEDS.SpectraEDS()._extractTotalCounts(line)
        self.assertAlmostEquals(totalCountsOriginalRef, totalCountsOriginal, delta=1.0)
        self.assertAlmostEquals(totalCountsInterpolatedRef, totalCountsInterpolated, delta=1.0)
        self.assertAlmostEquals(totalCountsSyntheticRef, totalCountsSynthetic)

        #self.fail("Test if the testcase is working.")

    def test__isRegionSpectraSection(self):
        """
        Tests for method `_isRegionSpectraSection`.
        """

        lines = open(self.spectraEdsRegion0Filepath, 'r').readlines()
        self.assertTrue(SpectraEDS.SpectraEDS()._isRegionSpectraSection(lines))

        lines = open(self.spectraEdsRegion1Filepath, 'r').readlines()
        self.assertTrue(SpectraEDS.SpectraEDS()._isRegionSpectraSection(lines))

        lines = """TEST INPUT - START
E_C = %7.5e, I_C = %15.14e

E_Brut = %7.5e, I_Brut = %15.14e
E_Brut = %7.5e, I_Brut = %15.14e
E_Brut = %7.5e, I_Brut = %15.14e
E_Brut = %7.5e, I_Brut = %15.14e
E_Brut = %7.5e, I_Brut = %15.14e
TEST INPUT - STOP

        """.splitlines()
        self.assertFalse(SpectraEDS.SpectraEDS()._isRegionSpectraSection(lines))

        #self.fail("Test if the testcase is working.")

    def test_readRegionSpectraSection(self):
        """
        Tests for method `readRegionSpectraSection`.
        """

        lines = """TEST INPUT - START
E_C = %7.5e, I_C = %15.14e

E_Brut = %7.5e, I_Brut = %15.14e
E_Brut = %7.5e, I_Brut = %15.14e
E_Brut = %7.5e, I_Brut = %15.14e
E_Brut = %7.5e, I_Brut = %15.14e
E_Brut = %7.5e, I_Brut = %15.14e
TEST INPUT - STOP

        """.splitlines()

        self.assertRaises(ValueError, SpectraEDS.SpectraEDS().readRegionSpectraSection, lines)

        spectraEDS = SpectraEDS.SpectraEDS()

        # Region 0 file.
        lines = open(self.spectraEdsRegion0Filepath, 'r').readlines()
        lines =[line.strip() for line in lines]

        self.assertEquals(6279, spectraEDS.readRegionSpectraSection(lines))

        self.assertEquals(0, spectraEDS.regionID)
        self.assertEquals(1, spectraEDS.numberElements)
        for symbol in spectraEDS.elements:
            weightFraction = spectraEDS.elements[symbol]
            self.assertEquals("Au", symbol)
            self.assertAlmostEquals(1.0, weightFraction)

        self.assertAlmostEquals(0.65211, spectraEDS.characteristicProbability)
        self.assertEquals(1000, spectraEDS.numberSimulatedPhotons)
        self.assertEquals(5, spectraEDS.numberCharateristicPeaks)

        self.assertEquals(1024, len(spectraEDS.iOutSpectrumEDS.channels))
        self.assertEquals(5, len(spectraEDS.eNetSpectrumEDS))
        self.assertEquals(1024, len(spectraEDS.eNetSpectrumEDS[0].channels))

        self.assertEquals(5, len(spectraEDS.pCharacteristic))
        self.assertEquals(1024, len(spectraEDS.pBackground))
        self.assertEquals(1024, len(spectraEDS.continuumCumulativeEquiprobableChannels))

        # Region 1 file
        lines = open(self.spectraEdsRegion1Filepath, 'r').readlines()
        lines =[line.strip() for line in lines]

        self.assertEquals(6263, spectraEDS.readRegionSpectraSection(lines))

        self.assertEquals(1, spectraEDS.regionID)
        self.assertEquals(1, spectraEDS.numberElements)
        for symbol in spectraEDS.elements:
            weightFraction = spectraEDS.elements[symbol]
            self.assertEquals("C", symbol)
            self.assertAlmostEquals(1.0, weightFraction)

        self.assertAlmostEquals(0.825861, spectraEDS.characteristicProbability)
        self.assertEquals(0, spectraEDS.numberSimulatedPhotons)
        self.assertEquals(1, spectraEDS.numberCharateristicPeaks)

        self.assertEquals(1024, len(spectraEDS.iOutSpectrumEDS.channels))
        self.assertEquals(1, len(spectraEDS.eNetSpectrumEDS))
        self.assertEquals(1024, len(spectraEDS.eNetSpectrumEDS[0].channels))

        self.assertEquals(1, len(spectraEDS.pCharacteristic))
        self.assertEquals(1024, len(spectraEDS.pBackground))
        self.assertEquals(1024, len(spectraEDS.continuumCumulativeEquiprobableChannels))

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    import nose
    nose.runmodule()
