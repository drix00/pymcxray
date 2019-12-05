#!/usr/bin/env python
"""
.. py:currentmodule:: format.results.test_PhirhozGenerated
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
import mcxray.format.results.PhirhozGenerated as PhirhozGenerated
import tests.format.results.test_ModelParameters as test_ModelParameters
import tests.format.results.test_SimulationParameters as test_SimulationParameters
import tests.format.results.test_MicroscopeParameters as test_MicroscopeParameters
import tests.format.results.test_ElectronParameters as test_ElectronParameters

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
        self.assertTrue(True)

    def test_read(self):
        """
        Tests for method `read`.
        """

        filepath = os.path.join(self.testDataPath, "version1.1", "autoSavedFiles", "DetectionLimits_N1000x_C_r10A_z11A_Au_E30d0keV.txt")
        phirhozFile = PhirhozGenerated.PhirhozGenerated()
        phirhozFile.read(filepath)

        modelParameters = phirhozFile.modelParameters
        modelParametersRef = self._getModelParametersReference()
        self.assertEqual(modelParametersRef.atomEnergyLossModel, modelParameters.atomEnergyLossModel)
        self.assertEqual(modelParametersRef.atomMeanIonizationPotentialModel, modelParameters.atomMeanIonizationPotentialModel)
        self.assertEqual(modelParametersRef.atomScreeningModel, modelParameters.atomScreeningModel)
        self.assertEqual(modelParametersRef.atomCrossSectionModel, modelParameters.atomCrossSectionModel)
        self.assertEqual(modelParametersRef.atomCrossSectionScreeningModel, modelParameters.atomCrossSectionScreeningModel)
        self.assertEqual(modelParametersRef.atomCollisionModel, modelParameters.atomCollisionModel)
        self.assertEqual(modelParametersRef.atomCollisionScreeningModel, modelParameters.atomCollisionScreeningModel)
        self.assertEqual(modelParametersRef.atomElectronRangeModel, modelParameters.atomElectronRangeModel)
        self.assertEqual(modelParametersRef.regionEnergyLossModel, modelParameters.regionEnergyLossModel)
        self.assertEqual(modelParametersRef.characterisitcCrossSectionModel, modelParameters.characterisitcCrossSectionModel)
        self.assertEqual(modelParametersRef.bremsstrahlungCrossSectionModel, modelParameters.bremsstrahlungCrossSectionModel)

        simulationParameters = phirhozFile.simulationParameters
        simulationParametersRef = self._getSimulationParametersReference()
        self.assertEqual(simulationParametersRef.numberElectrons, simulationParameters.numberElectrons)
        self.assertEqual(simulationParametersRef.numberPhotons, simulationParameters.numberPhotons)
        self.assertEqual(simulationParametersRef.numberEnergyWindows, simulationParameters.numberEnergyWindows)
        self.assertEqual(simulationParametersRef.numberLayersX, simulationParameters.numberLayersX)
        self.assertEqual(simulationParametersRef.numberLayersY, simulationParameters.numberLayersY)
        self.assertEqual(simulationParametersRef.numberLayersZ, simulationParameters.numberLayersZ)
        self.assertEqual(simulationParametersRef.numberChannels, simulationParameters.numberChannels)
        self.assertEqual(simulationParametersRef.interpolationType, simulationParameters.interpolationType)
        self.assertEqual(simulationParametersRef.edsMaximumEnergy_keV, simulationParameters.edsMaximumEnergy_keV)
        self.assertEqual(simulationParametersRef.generalizedWalk, simulationParameters.generalizedWalk)
        self.assertEqual(simulationParametersRef.useLiveTime_s, simulationParameters.useLiveTime_s)
        self.assertEqual(simulationParametersRef.maximumLiveTime_s, simulationParameters.maximumLiveTime_s)

        microscopeParameters = phirhozFile.microscopeParameters
        microscopeParametersRef = self._getMicroscopeParametersReference()

        beamParametersRef = microscopeParametersRef.beamParameters
        beamParameters = microscopeParameters.beamParameters
        self.assertAlmostEqual(beamParametersRef.incidentEnergy_keV, beamParameters.incidentEnergy_keV)
        self.assertAlmostEqual(beamParametersRef.current_A, beamParameters.current_A)
        self.assertAlmostEqual(beamParametersRef.acquisitionTime_s, beamParameters.acquisitionTime_s)
        self.assertAlmostEqual(beamParametersRef.diameter90_A, beamParameters.diameter90_A)
        self.assertAlmostEqual(beamParametersRef.tiltAngle_deg, beamParameters.tiltAngle_deg)
        self.assertAlmostEqual(beamParametersRef.gaussianMean, beamParameters.gaussianMean)
        self.assertAlmostEqual(beamParametersRef.gaussianSigma, beamParameters.gaussianSigma)

        detectorParametersRef = microscopeParametersRef.detectorParameters
        detectorParameters = microscopeParameters.detectorParameters
        self.assertEqual(detectorParametersRef.crystalName, detectorParameters.crystalName)
        self.assertAlmostEqual(detectorParametersRef.crystalDensity_g_cm3, detectorParameters.crystalDensity_g_cm3)
        #self.assertAlmostEqual(detectorParametersRef.crystalThickness_cm, detectorParameters.crystalThickness_cm)
        #self.assertAlmostEqual(detectorParametersRef.crystalRadius_cm, detectorParameters.crystalRadius_cm)
        #self.assertAlmostEqual(detectorParametersRef.beamDetectorDistance_cm, detectorParameters.beamDetectorDistance_cm)
        self.assertAlmostEqual(detectorParametersRef.deadLayerThickness_A, detectorParameters.deadLayerThickness_A)
        self.assertAlmostEqual(detectorParametersRef.diffusionLength_A, detectorParameters.diffusionLength_A)
        self.assertAlmostEqual(detectorParametersRef.surfaceQualityFactor, detectorParameters.surfaceQualityFactor)
        self.assertAlmostEqual(detectorParametersRef.noiseEdsDetector_eV, detectorParameters.noiseEdsDetector_eV)
        self.assertAlmostEqual(detectorParametersRef.thicknessBeWindow_um, detectorParameters.thicknessBeWindow_um)
        self.assertAlmostEqual(detectorParametersRef.thicknessAlWindow_um, detectorParameters.thicknessAlWindow_um)
        self.assertAlmostEqual(detectorParametersRef.thicknessTiWindow_um, detectorParameters.thicknessTiWindow_um)
        self.assertAlmostEqual(detectorParametersRef.thicknessOil_um, detectorParameters.thicknessOil_um)
        self.assertAlmostEqual(detectorParametersRef.thicknessH2O_um, detectorParameters.thicknessH2O_um)
        self.assertAlmostEqual(detectorParametersRef.thicknessMoxtek_um, detectorParameters.thicknessMoxtek_um)
        self.assertAlmostEqual(detectorParametersRef.thicknessAir_um, detectorParameters.thicknessAir_um)
        self.assertAlmostEqual(detectorParametersRef.angleBetweenDetectorSpecimenNormal_deg, detectorParameters.angleBetweenDetectorSpecimenNormal_deg)
        self.assertAlmostEqual(detectorParametersRef.angleBetweenDetectorXAxis_deg, detectorParameters.angleBetweenDetectorXAxis_deg)
        self.assertAlmostEqual(detectorParametersRef.takeoffAngleNormalIncidence_deg, detectorParameters.takeoffAngleNormalIncidence_deg)
        self.assertAlmostEqual(detectorParametersRef.takeoffAngleEffective_deg, detectorParameters.takeoffAngleEffective_deg)
        self.assertAlmostEqual(detectorParametersRef.solidAngle_deg, detectorParameters.solidAngle_deg)

        electronParameters = phirhozFile.electronParameters
        electronParametersRef = self._getElectronParametersReference()
        self.assertEqual(electronParametersRef.numberSimulatedElectrons, electronParameters.numberSimulatedElectrons)
        self.assertEqual(electronParametersRef.meanNumberCollisionPerElectrons, electronParameters.meanNumberCollisionPerElectrons)
        self.assertEqual(electronParametersRef.meanDistanceBetweenCollisions_A, electronParameters.meanDistanceBetweenCollisions_A)
        self.assertEqual(electronParametersRef.meanPolarAngleCollision_deg, electronParameters.meanPolarAngleCollision_deg)
        self.assertEqual(electronParametersRef.meanAzimuthalAngleCollision_deg, electronParameters.meanAzimuthalAngleCollision_deg)
        self.assertEqual(electronParametersRef.backscatteredRatio, electronParameters.backscatteredRatio)
        self.assertEqual(electronParametersRef.internalRatio, electronParameters.internalRatio)
        self.assertEqual(electronParametersRef.throughRatio, electronParameters.throughRatio)
        self.assertEqual(electronParametersRef.skirtRatio, electronParameters.skirtRatio)
        self.assertEqual(electronParametersRef.eRatio, electronParameters.eRatio)

        self.assertEqual(2, phirhozFile.numberRegions)

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
    from tests.testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__, withCoverage=False)
