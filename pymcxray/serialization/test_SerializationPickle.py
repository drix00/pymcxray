#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2007 Hendrix Demers"
__license__ = ""

# Standard library modules.
import unittest
import logging
import tempfile
import shutil
import os.path

# Third party modules.

# Local modules.
import pymcxray.serialization.SerializationPickle as SerializationPickle

# Globals and constants variables.

class TestSerialization(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        self.tempPath = tempfile.mkdtemp(prefix="Test_Serialization_")

    def tearDown(self):
        unittest.TestCase.tearDown(self)

        shutil.rmtree(self.tempPath)

    def testSkeleton(self):
        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def test_loadSave(self):
        dataRef = range(1, 10)

        serialization = SerializationPickle.SerializationPickle()
        filepath = os.path.join(self.tempPath, "SerializationPickle.ser")
        serialization.setFilepath(filepath)

        serialization.save(dataRef)

        data = serialization.load()

        self.assertEquals(dataRef, data)

        #self.fail("Test if the testcase is working.")

    def test_version(self):
        dataRef = range(1, 10)

        serialization = SerializationPickle.SerializationPickle()
        filepath = os.path.join(self.tempPath, "SerializationPickle.ser")
        serialization.setFilepath(filepath)
        serialization.setCurrentVersion("0.1")
        serialization.save(dataRef)

        serialization = SerializationPickle.SerializationPickle()
        filepath = os.path.join(self.tempPath, "SerializationPickle.ser")
        serialization.setFilepath(filepath)
        serialization.setCurrentVersion("0.2")

        self.assertTrue(serialization.isNewVersion())

        data = serialization.load()
        self.assertEquals(dataRef, data)

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__': #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from pymcxray.Testings import runTestModule
    runTestModule()
