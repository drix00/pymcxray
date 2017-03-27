#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.test_ExportedSpectrum
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for module `ExportedSpectrum`.
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
import shutil

# Third party modules.

# Local modules.

# Project modules
import pymcxray.FileFormat.ExportedSpectrum as ExportedSpectrum

# Globals and constants variables.

class TestExportedSpectrum(unittest.TestCase):
    """
    TestCase class for the module `moduleName`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

        self.testDataPath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../test_data", "exportedFiles"))

        self.tempDataPath = os.path.join(self.testDataPath, "tmp")
        if not os.path.isdir(self.tempDataPath):
            os.mkdir(self.tempDataPath)

    def tearDown(self):
        """
        Teardown method.
        """

        unittest.TestCase.tearDown(self)

        if os.path.expanduser(self.tempDataPath):
            shutil.rmtree(self.tempDataPath)

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

        exportedSpectrum = ExportedSpectrum.ExportedSpectrum()
        self.assertEquals(None, exportedSpectrum.getSpectrumType())
        self.assertEquals(0, len(exportedSpectrum._energies_keV))
        self.assertEquals(0, len(exportedSpectrum._intensities))

        filepath = os.path.join(self.testDataPath, "bulkC_E20keV_w64BW.txt")
        exportedSpectrum.read(filepath)

        self.assertEquals("Specimen Spectra", exportedSpectrum.getSpectrumType())
        self.assertEquals(1024, len(exportedSpectrum._energies_keV))
        self.assertEquals(1024, len(exportedSpectrum._intensities))

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from pymcxray.Testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__)
