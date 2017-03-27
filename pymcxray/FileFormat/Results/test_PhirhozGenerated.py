#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.test_PhirhozGenerated
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module `PhirhozGenerated`.#
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
import pymcxray.FileFormat.Results.PhirhozGenerated as PhirhozGenerated
import pymcxray.FileFormat.Results.test_ModelParameters as test_ModelParameters
import pymcxray.FileFormat.Results.test_SimulationParameters as test_SimulationParameters
import pymcxray.FileFormat.Results.test_MicroscopeParameters as test_MicroscopeParameters
import pymcxray.FileFormat.Results.test_ElectronParameters as test_ElectronParameters

# Globals and constants variables.

class TestPhirhozGenerated(unittest.TestCase):
    """
    TestCase class for the module `moduleName`.
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

        filepath = os.path.join(self.testDataPath, "version1.1", "autoSavedFiles", "DetectionLimits_N1000x_C_r10A_z11A_Au_E30d0keV.txt")
        phirhozFile = PhirhozGenerated.PhirhozGenerated()
        phirhozFile.read(filepath)

        modelParameters = phirhozFile.modelParameters
        modelParametersRef = self._getModelParametersReference()
        self.assertEquals(modelParametersRef.atomEnergyLossModel, modelParameters.atomEnergyLossModel)
        self.assertEquals(modelParametersRef.atomMeanIonizationPotentialModel, modelParameters.atomMeanIonizationPotentialModel)
        self.assertEquals(modelParametersRef.atomScreeningModel, modelParameters.atomScreeningModel)
        self.assertEquals(modelParametersRef.atomCrossSectionModel, modelParameters.atomCrossSectionModel)
        self.assertEquals(modelParametersRef.atomCrossSectionScreeningModel, modelParameters.atomCrossSectionScreeningModel)
        self.assertEquals(modelParametersRef.atomCollisionModel, modelParameters.atomCollisionModel)
        self.assertEquals(modelParametersRef.atomCollisionScreeningModel, modelParameters.atomCollisionScreeningModel)
        self.assertEquals(modelParametersRef.atomElectronRangeModel, modelParameters.atomElectronRangeModel)
        self.assertEquals(modelParametersRef.regionEnergyLossModel, modelParameters.regionEnergyLossModel)
        self.assertEquals(modelParametersRef.characterisitcCrossSectionModel, modelParameters.characterisitcCrossSectionModel)
        self.assertEquals(modelParametersRef.bremsstrahlungCrossSectionModel, modelParameters.bremsstrahlungCrossSectionModel)

        simulationParameters = phirhozFile.simulationParameters
        simulationParametersRef = self._getSimulationParametersReference()
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

        microscopeParameters = phirhozFile.microscopeParameters
        microscopeParametersRef = self._getMicroscopeParametersReference()

        beamParametersRef = microscopeParametersRef.beamParameters
        beamParameters = microscopeParameters.beamParameters
        self.assertAlmostEquals(beamParametersRef.incidentEnergy_keV, beamParameters.incidentEnergy_keV)
        self.assertAlmostEquals(beamParametersRef.current_A, beamParameters.current_A)
        self.assertAlmostEquals(beamParametersRef.acquisitionTime_s, beamParameters.acquisitionTime_s)
        self.assertAlmostEquals(beamParametersRef.diameter90_A, beamParameters.diameter90_A)
        self.assertAlmostEquals(beamParametersRef.tiltAngle_deg, beamParameters.tiltAngle_deg)
        self.assertAlmostEquals(beamParametersRef.gaussianMean, beamParameters.gaussianMean)
        self.assertAlmostEquals(beamParametersRef.gaussianSigma, beamParameters.gaussianSigma)

        detectorParametersRef = microscopeParametersRef.detectorParameters
        detectorParameters = microscopeParameters.detectorParameters
        self.assertEquals(detectorParametersRef.crystalName, detectorParameters.crystalName)
        self.assertAlmostEquals(detectorParametersRef.crystalDensity_g_cm3, detectorParameters.crystalDensity_g_cm3)
        #self.assertAlmostEquals(detectorParametersRef.crystalThickness_cm, detectorParameters.crystalThickness_cm)
        #self.assertAlmostEquals(detectorParametersRef.crystalRadius_cm, detectorParameters.crystalRadius_cm)
        #self.assertAlmostEquals(detectorParametersRef.beamDetectorDistance_cm, detectorParameters.beamDetectorDistance_cm)
        self.assertAlmostEquals(detectorParametersRef.deadLayerThickness_A, detectorParameters.deadLayerThickness_A)
        self.assertAlmostEquals(detectorParametersRef.diffusionLength_A, detectorParameters.diffusionLength_A)
        self.assertAlmostEquals(detectorParametersRef.surfaceQualityFactor, detectorParameters.surfaceQualityFactor)
        self.assertAlmostEquals(detectorParametersRef.noiseEdsDetector_eV, detectorParameters.noiseEdsDetector_eV)
        self.assertAlmostEquals(detectorParametersRef.thicknessBeWindow_um, detectorParameters.thicknessBeWindow_um)
        self.assertAlmostEquals(detectorParametersRef.thicknessAlWindow_um, detectorParameters.thicknessAlWindow_um)
        self.assertAlmostEquals(detectorParametersRef.thicknessTiWindow_um, detectorParameters.thicknessTiWindow_um)
        self.assertAlmostEquals(detectorParametersRef.thicknessOil_um, detectorParameters.thicknessOil_um)
        self.assertAlmostEquals(detectorParametersRef.thicknessH2O_um, detectorParameters.thicknessH2O_um)
        self.assertAlmostEquals(detectorParametersRef.thicknessMoxtek_um, detectorParameters.thicknessMoxtek_um)
        self.assertAlmostEquals(detectorParametersRef.thicknessAir_um, detectorParameters.thicknessAir_um)
        self.assertAlmostEquals(detectorParametersRef.angleBetweenDetectorSpecimenNormal_deg, detectorParameters.angleBetweenDetectorSpecimenNormal_deg)
        self.assertAlmostEquals(detectorParametersRef.angleBetweenDetectorXAxis_deg, detectorParameters.angleBetweenDetectorXAxis_deg)
        self.assertAlmostEquals(detectorParametersRef.takeoffAngleNormalIncidence_deg, detectorParameters.takeoffAngleNormalIncidence_deg)
        self.assertAlmostEquals(detectorParametersRef.takeoffAngleEffective_deg, detectorParameters.takeoffAngleEffective_deg)
        self.assertAlmostEquals(detectorParametersRef.solidAngle_deg, detectorParameters.solidAngle_deg)

        electronParameters = phirhozFile.electronParameters
        electronParametersRef = self._getElectronParametersReference()
        self.assertEquals(electronParametersRef.numberSimulatedElectrons, electronParameters.numberSimulatedElectrons)
        self.assertEquals(electronParametersRef.meanNumberCollisionPerElectrons, electronParameters.meanNumberCollisionPerElectrons)
        self.assertEquals(electronParametersRef.meanDistanceBetweenCollisions_A, electronParameters.meanDistanceBetweenCollisions_A)
        self.assertEquals(electronParametersRef.meanPolarAngleCollision_deg, electronParameters.meanPolarAngleCollision_deg)
        self.assertEquals(electronParametersRef.meanAzimuthalAngleCollision_deg, electronParameters.meanAzimuthalAngleCollision_deg)
        self.assertEquals(electronParametersRef.backscatteredRatio, electronParameters.backscatteredRatio)
        self.assertEquals(electronParametersRef.internalRatio, electronParameters.internalRatio)
        self.assertEquals(electronParametersRef.throughRatio, electronParameters.throughRatio)
        self.assertEquals(electronParametersRef.skirtRatio, electronParameters.skirtRatio)
        self.assertEquals(electronParametersRef.eRatio, electronParameters.eRatio)

        self.assertEquals(2, phirhozFile.numberRegions)

        #self.fail("Test if the testcase is working.")

    def _getModelParametersReference(self):
        _lines, modelParametersRef = test_ModelParameters.getLinesAndReference()
        return modelParametersRef

    def _getSimulationParametersReference(self):
        _lines, simulationParametersRef = test_SimulationParameters.getLinesAndReference()
        return simulationParametersRef

    def _getMicroscopeParametersReference(self):
        _lines, microscopeParametersRef = test_MicroscopeParameters.getLinesAndReference()
        return microscopeParametersRef

    def _getElectronParametersReference(self):
        _lines, electronParametersRef = test_ElectronParameters.getLinesAndReference()
        return electronParametersRef

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from pymcxray.Testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__, withCoverage=False)
