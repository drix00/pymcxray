#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.test_RegionVolume
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module `RegionVolume`.
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

# Third party modules.

# Local modules.

# Project modules
import pymcxray.FileFormat.Results.RegionVolume as RegionVolume
import pymcxray.FileFormat.RegionType as RegionType
import pymcxray.FileFormat.RegionDimensions as RegionDimensions

# Globals and constants variables.

class TestRegionVolume(unittest.TestCase):
    """
    TestCase class for the module `RegionVolume`.
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

    def NOtest_readFromLines(self):
        """
        Tests for method `readFromLines`.
        """

        lines, regionVolumeRef = getLinesAndReference()

        regionVolume = RegionVolume.RegionVolume()
        regionVolume.readFromLines(lines)

        self.assertEquals(regionVolumeRef.regionID, regionVolume.regionID)
        self.assertEquals(regionVolumeRef.volumeSize, regionVolume.volumeSize)
        self.assertEquals(regionVolumeRef.volumeMinimum_A, regionVolume.volumeMinimum_A)
        self.assertEquals(regionVolumeRef.volumeMaximum_A, regionVolume.volumeMaximum_A)
        self.assertEquals(regionVolumeRef.volumeType, regionVolume.volumeType)
        self.assertEquals(regionVolumeRef.volumeParameters, regionVolume.volumeParameters)
        self.assertEquals(regionVolumeRef.isExclusion, regionVolume.isExclusion)
        self.assertEquals(regionVolumeRef.isCompact, regionVolume.isCompact)
        self.assertEquals(regionVolumeRef.isEmpty, regionVolume.isEmpty)

        self.fail("Test if the testcase is working.")

def getLinesAndReference():
    lines = """Volume ID   = 0
Volume size = 8.000000e+030
Volume extents min (-1.000000e+010, -1.000000e+010,  0.000000e+000)
Volume extents max ( 1.000000e+010,  1.000000e+010,  2.000000e+010)
BOX
-10000000000.000000 10000000000.000000 -10000000000.000000 10000000000.000000 0.000000 20000000000.000000
Exclusion region
Volume has holes

""".splitlines()

    regionVolumeRef = RegionVolume.RegionVolume()
    regionVolumeRef.volumeID = 0
    regionVolumeRef.volumeSize = 8.000000e+030
    regionVolumeRef.volumeMinimum_A = (-1.0e10, -1.0e10, 0.0)
    regionVolumeRef.volumeMaximum_A = (1.0e10, 1.0e10, 2.0e10)
    regionVolumeRef.volumeType = RegionType.REGION_TYPE_BOX
    parameters = [-10000000000.0, 10000000000.0, -10000000000.0, 10000000000.0, 0.0, 20000000000.0]
    regionVolumeRef.volumeParameters = RegionDimensions.RegionDimensionsBox(parameters)
    regionVolumeRef.isExclusion = True
    regionVolumeRef.isCompact = False
    regionVolumeRef.isEmpty = False

    return lines, regionVolumeRef

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from pymcxray.Testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__)
