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

# Third party modules.
import numpy as np

# Local modules.

# Project modules
import pymcxray.serialization.SerializationNumpy as SerializationNumpy

# Globals and constants variables.

class TestSerializationNumpy(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        self.tempPath = tempfile.mkdtemp(prefix="Test_Serialization_")

    def tearDown(self):
        unittest.TestCase.tearDown(self)

        try:
            shutil.rmtree(self.tempPath)
        except OSError as message:
            logging.error(message)

    def testSkeleton(self):
        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_loadSaveSerializationNumpy(self):
        dataRef = np.arange(1.0, 10.0)

        serialization = SerializationNumpy.SerializationNumpy()
        filepath = os.path.join(self.tempPath, "SerializationNumpy.dat")
        serialization.setFilepath(filepath)

        serialization.save(dataRef)

        data = serialization.load()

        self.assertEquals(len(dataRef), len(data))
        for valueRef, value in zip(dataRef, data):
            self.assertAlmostEquals(valueRef, value)

        #self.fail("Test if the testcase is working.")

    def test_loadSaveSerializationNumpyTxt(self):
        dataRef = np.arange(1.0, 10.0)

        serialization = SerializationNumpy.SerializationNumpyTxt()
        filepath = os.path.join(self.tempPath, "SerializationNumpy.dat")
        serialization.setFilepath(filepath)

        serialization.save(dataRef)

        data = serialization.load()

        self.assertEquals(len(dataRef), len(data))
        for valueRef, value in zip(dataRef, data):
            self.assertAlmostEquals(valueRef, value)

        #self.fail("Test if the testcase is working.")

    def test_loadSaveSerializationNumpyTxtGz(self):
        dataRef = np.arange(1.0, 10.0)

        serialization = SerializationNumpy.SerializationNumpyTxtGz()
        filepath = os.path.join(self.tempPath, "SerializationNumpy.dat")
        serialization.setFilepath(filepath)

        serialization.save(dataRef)

        data = serialization.load()

        self.assertEquals(len(dataRef), len(data))
        for valueRef, value in zip(dataRef, data):
            self.assertAlmostEquals(valueRef, value)

        #self.fail("Test if the testcase is working.")

    def test_loadSaveSerializationNumpyNPY(self):
        dataRef = np.arange(1.0, 10.0)

        serialization = SerializationNumpy.SerializationNumpyNPY()
        filepath = os.path.join(self.tempPath, "SerializationNumpy.npy")
        serialization.setFilepath(filepath)

        serialization.save(dataRef)

        data = serialization.load()

        self.assertEquals(len(dataRef), len(data))
        for valueRef, value in zip(dataRef, data):
            self.assertAlmostEquals(valueRef, value)

        #self.fail("Test if the testcase is working.")

    def test_loadSaveSerializationNumpyNPZ(self):
        dataRef = {}
        dataRef['x'] = np.arange(1.0, 10.0)
        dataRef['Raw'] = np.ones((20, 3))

        serialization = SerializationNumpy.SerializationNumpyNPZ()
        filepath = os.path.join(self.tempPath, "SerializationNumpy.npz")
        serialization.setFilepath(filepath)

        serialization.save(dataRef)

        data = serialization.load()

        self.assertEquals(len(dataRef), len(data))
        for key in data:
            self.assertEquals(len(dataRef[key]), len(data[key]))
            self.assertEquals(dataRef[key].shape, data[key].shape)
            self.assertEquals(dataRef[key].ndim, data[key].ndim)
            self.assertEquals(dataRef[key].dtype, data[key].dtype)

            for valueRef, value in zip(dataRef[key].flat, data[key].flat):
                self.assertAlmostEquals(valueRef, value)

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from pymcxray.Testings import runTestModule
    runTestModule()
