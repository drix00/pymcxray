#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.test_Snr
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module `SnrParameters`.
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
import os.path

# Third party modules.

# Local modules.

# Project modules
import pymcxray.FileFormat.SnrParameters as SnrParameters
import pymcxray.FileFormat.testUtilities as testUtilities

# Globals and constants variables.

class TestSnrParameters(unittest.TestCase):
    """
    TestCase class for the module `SnrParameters`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

        self.testDataPath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../test_data"))
        self.tempDataPath = testUtilities.createTempDataPath(self.testDataPath)

    def tearDown(self):
        """
        Teardown method.
        """

        unittest.TestCase.tearDown(self)

        testUtilities.removeTempDataPath(self.tempDataPath)

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

        for title in ["BioRitchieNew111017"]:
            snrParameters = SnrParameters.SnrParameters()

            filepath = os.path.abspath(os.path.join(self.testDataPath, "%s/%s.snp" % (title, title)))
            snrParameters.read(filepath)

            snrParametersRef = self.getSnrParametersReference(title)
            self.assertEquals(snrParametersRef.snrType, snrParameters.snrType)
            self.assertEquals(snrParametersRef.energyStart_keV, snrParameters.energyStart_keV)
            self.assertEquals(snrParametersRef.energyEnd_keV, snrParameters.energyEnd_keV)
            self.assertEquals(snrParametersRef.numberEnergySteps, snrParameters.numberEnergySteps)
            self.assertEquals(snrParametersRef.backgroundEnergyWindowsSize, snrParameters.backgroundEnergyWindowsSize)
            self.assertEquals(snrParametersRef.spectrumEnergyWindowsSize, snrParameters.spectrumEnergyWindowsSize)

        #self.fail("Test if the testcase is working.")

    def getSnrParametersReference(self, title):
        snrParameters = SnrParameters.SnrParameters()

        if title == "BioRitchieNew111017":
            snrParameters.snrType = 0
            snrParameters.energyStart_keV = 1.0
            snrParameters.energyEnd_keV = 20.0
            snrParameters.numberEnergySteps = 100
            snrParameters.backgroundEnergyWindowsSize = 5.0e-3
            snrParameters.spectrumEnergyWindowsSize = 40.0

        return snrParameters

    def test__createKeys(self):
        """
        Tests for method `_createKeys`.
        """

        numberKeys = 6

        keys = SnrParameters.SnrParameters()._createKeys()
        self.assertEquals(numberKeys, len(keys))

        #self.fail("Test if the testcase is working.")

    def test_write(self):
        """
        Tests for method `write`.
        """
        self.maxDiff = None

        for title in ["BioRitchieNew111017"]:
            snrParametersRef = self.getSnrParametersReference(title)

            filepathReference = os.path.abspath(os.path.join(self.testDataPath, "%s/%s.snp" % (title, title)))

            filepath = os.path.join(self.tempDataPath, "%s.snp" % (title))
            snrParameters = SnrParameters.SnrParameters()
            snrParameters = snrParametersRef

            snrParameters.write(filepath)

            self.assertEquals(snrParametersRef.snrType, snrParameters.snrType)
            self.assertEquals(snrParametersRef.energyStart_keV, snrParameters.energyStart_keV)
            self.assertEquals(snrParametersRef.energyEnd_keV, snrParameters.energyEnd_keV)
            self.assertEquals(snrParametersRef.numberEnergySteps, snrParameters.numberEnergySteps)
            self.assertEquals(snrParametersRef.backgroundEnergyWindowsSize, snrParameters.backgroundEnergyWindowsSize)
            self.assertEquals(snrParametersRef.spectrumEnergyWindowsSize, snrParameters.spectrumEnergyWindowsSize)

            linesRef = open(filepathReference, 'r').readlines()
            lines = open(filepath, 'r').readlines()

            self.assertListEqual(linesRef, lines)

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from pymcxray.Testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__)
