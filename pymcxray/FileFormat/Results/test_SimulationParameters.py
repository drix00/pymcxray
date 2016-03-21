#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.test_SimulationParameters
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module `SimulationParameters`.
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
import pymcxray.FileFormat.Results.SimulationParameters as SimulationParameters

# Globals and constants variables.

class TestSimulationParameters(unittest.TestCase):
    """
    TestCase class for the module `SimulationParameters`.
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

    def test_readFromLines(self):
        """
        Tests for method `readFromLines`.
        """

        lines, simulationParametersRef = getLinesAndReference()

        simulationParameters = SimulationParameters.SimulationParameters()
        simulationParameters.readFromLines(lines)

        self.assertEquals(simulationParametersRef.numberElectrons, simulationParameters.numberElectrons)
        self.assertEquals(simulationParametersRef.numberPhotons, simulationParameters.numberPhotons)
        self.assertEquals(simulationParametersRef.numberEnergyWindows, simulationParameters.numberEnergyWindows)
        self.assertEquals(simulationParametersRef.numberLayersX, simulationParameters.numberLayersX)
        self.assertEquals(simulationParametersRef.numberLayersY, simulationParameters.numberLayersY)
        self.assertEquals(simulationParametersRef.numberLayersZ, simulationParameters.numberLayersZ)
        self.assertEquals(simulationParametersRef.numberChannels, simulationParameters.numberChannels)
        self.assertEquals(simulationParametersRef.interpolationType, simulationParameters.interpolationType)
        self.assertEquals(simulationParametersRef.edsMaximumEnergy_keV, simulationParameters.edsMaximumEnergy_keV)
        self.assertEquals(simulationParametersRef.generalizedWalk, simulationParameters.generalizedWalk)
        self.assertEquals(simulationParametersRef.useLiveTime_s, simulationParameters.useLiveTime_s)
        self.assertEquals(simulationParametersRef.maximumLiveTime_s, simulationParameters.maximumLiveTime_s)

        #self.fail("Test if the testcase is working.")

def getLinesAndReference():
    lines = """Simulation Parameters:
   Total simulated electrons      = 10000
   Total simulated photons in EDS = 1000
   Number of energy windows       = 64
   Number of layers in PhiRoX     = 128
   Number of layers in PhiRoY     = 128
   Number of layers in PhiRoZ     = 128
   Number of channels in spectras = 1024
   Spectras interpolation type    = 2
   EDS spectras maximum energy    = 0
   Generalized Walk               = 0
   Use Live Time                  = 0
   Live Time Max                  = 1.000000e-014
""".splitlines()

    simulationParametersRef = SimulationParameters.SimulationParameters()
    simulationParametersRef.numberElectrons = 10000
    simulationParametersRef.numberPhotons = 1000
    simulationParametersRef.numberEnergyWindows = 64
    simulationParametersRef.numberLayersX = 128
    simulationParametersRef.numberLayersY = 128
    simulationParametersRef.numberLayersZ = 128
    simulationParametersRef.numberChannels = 1024
    simulationParametersRef.interpolationType = 2
    simulationParametersRef.edsMaximumEnergy_keV = 0.0
    simulationParametersRef.generalizedWalk = 0
    simulationParametersRef.useLiveTime_s = 0.0
    simulationParametersRef.maximumLiveTime_s = 1.0e-014

    return lines, simulationParametersRef

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from pymcxray.Testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__)
