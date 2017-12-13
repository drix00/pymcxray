#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2011 Hendrix Demers"
__license__ = ""

# Standard library modules.
import unittest
import logging
import os.path
import tempfile
import shutil
import time

# Third party modules.
from nose.plugins.skip import SkipTest

# Local modules.
from pymcxray import get_current_module_path

# Project modules
import pymcxray.serialization._Serialization as _Serialization

# Globals and constants variables.

class Test_Serialization(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        self.serialization = _Serialization._Serialization()

        self.tempPath = tempfile.mkdtemp(prefix="Test_Serialization_")

    def tearDown(self):
        unittest.TestCase.tearDown(self)

        shutil.rmtree(self.tempPath)

    def testSkeleton(self):
        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_init(self):
        serialization = _Serialization._Serialization()
        self.assertEquals(None, serialization._filename)
        self.assertEquals(True, serialization._verbose)

        serialization = _Serialization._Serialization(verbose=True)
        self.assertEquals(None, serialization._filename)
        self.assertEquals(True, serialization._verbose)

        serialization = _Serialization._Serialization(verbose=False)
        self.assertEquals(None, serialization._filename)
        self.assertEquals(False, serialization._verbose)

        filenameRef = "_Serialization.ser"
        serialization = _Serialization._Serialization(filename=filenameRef)
        self.assertEquals(filenameRef, serialization._filename)
        self.assertEquals(True, serialization._verbose)

        filenameRef = "_Serialization2.ser"
        serialization = _Serialization._Serialization(filenameRef)
        self.assertEquals(filenameRef, serialization._filename)
        self.assertEquals(True, serialization._verbose)

        #self.fail("Test if the testcase is working.")

    def test_getFilepath(self):
        serialization = _Serialization._Serialization()
        self.assertRaises(ValueError, serialization.getFilepath)

        filenameRef = "_Serialization.ser"
        filepathRef = filenameRef
        filepathRef = os.path.normpath(filepathRef)
        serialization = _Serialization._Serialization(filename=filenameRef)
        filepath = serialization.getFilepath()
        self.assertEquals(filepathRef, filepath)

        filenameRef = "_Serialization.ser"
        pathRef = "/casd/csadf/asdfsdaf/"
        filepathRef = os.path.join(pathRef, filenameRef)
        filepathRef = os.path.normpath(filepathRef)
        serialization = _Serialization._Serialization()
        serialization.setFilename(filenameRef)
        serialization.setPathname(pathRef)
        filepath = serialization.getFilepath()
        self.assertEquals(filepathRef, filepath)

        filenameRef = "_Serialization.ser"
        pathRef = "/casd/csadf/asdfsdaf/"
        filepathRef = os.path.join(filepathRef, filenameRef)
        filepathRef = os.path.normpath(filepathRef)
        serialization = _Serialization._Serialization()
        serialization.setFilepath(filepathRef)
        filepath = serialization.getFilepath()
        self.assertEquals(filepathRef, filepath)

        #self.fail("Test if the testcase is working.")

    def test_setCurrentVersion(self):
        version = "1.2.3"
        self.serialization.setCurrentVersion(version)
        self.assertEquals(version, self.serialization._currentVersion)
        self.assertEquals(version, self.serialization.getCurrentVersion())

        version = 1.2
        self.assertRaises(TypeError, self.serialization.setCurrentVersion, version)

        #self.fail("Test if the testcase is working.")

    def test_isFile(self):
        filepathRef = "/casd/csadf/asdfsdaf/sadfsdaf.ser"
        self.serialization.setFilepath(filepathRef)
        self.assertFalse(self.serialization.isFile())

        filepathRef = get_current_module_path(__file__, "../../test_data/serialization/empty.ser")
        if not os.path.isfile(filepathRef):
            raise SkipTest

        self.serialization.setFilepath(filepathRef)
        self.assertTrue(self.serialization.isFile())

        #self.fail("Test if the testcase is working.")

    def test_deleteFile(self):
        filename = "empty.ser"
        filepathRef = get_current_module_path(__file__, "../../test_data/serialization/")
        filepathRef = os.path.join(filepathRef, filename)
        if not os.path.isfile(filepathRef):
            raise SkipTest

        filepath = os.path.join(self.tempPath, filename)
        shutil.copy2(filepathRef, filepath)

        self.serialization.setFilepath(filepath)
        self.assertTrue(os.path.isfile(filepath))
        self.serialization.deleteFile()
        self.assertFalse(os.path.isfile(filepath))

        #self.fail("Test if the testcase is working.")

    def test_isOlderThan(self):

        filename = "empty"
        filepathRef = get_current_module_path(__file__, "../../test_data/serialization/")
        filepathRef = os.path.join(filepathRef, filename+'.ser')
        if not os.path.isfile(filepathRef):
            raise SkipTest

        filepath1 = os.path.join(self.tempPath, filename+'_1'+'.ser')
        time.sleep(1.0)
        shutil.copy(filepathRef, filepath1)

        filepath2 = os.path.join(self.tempPath, filename+'_2'+'.ser')
        time.sleep(1.0)
        shutil.copy(filepathRef, filepath2)

        filepath3 = os.path.join(self.tempPath, filename+'_3'+'.ser')
        time.sleep(1.0)
        shutil.copy(filepathRef, filepath3)

        self.serialization.setFilepath(filepath2)

        self.assertFalse(self.serialization.isOlderThan(filepath1))
        self.assertFalse(self.serialization.isOlderThan(filepath2))
        self.assertTrue(self.serialization.isOlderThan(filepath3))

        filepath = "/casd/csadf/asdfsdaf/sadfsdaf.ser"
        self.assertFalse(self.serialization.isOlderThan(filepath))

        filepath = "/casd/csadf/asdfsdaf/sadfsdaf.ser"
        self.serialization.setFilepath(filepath)
        self.assertTrue(self.serialization.isOlderThan(filepath3))

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    import nose
    nose.runmodule()

