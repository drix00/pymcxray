#!/usr/bin/env python
"""
.. py:currentmodule:: format.results.test_ModelParameters
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

ModelParameters
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
import mcxray.format.results.ModelParameters as ModelParameters
import mcxray.format.MCXRayModel as MCXRayModel

# Globals and constants variables.

class TestModelParameters(unittest.TestCase):
    """
    TestCase class for the module `ModelParameters`.
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
        self.assertTrue(True)

    def test_readFromLines(self):
        """
        Tests for method `readFromLines`.
        """

        lines, modelParametersRef = getLinesAndReference()

        modelParameters = ModelParameters.ModelParameters()
        modelParameters.readFromLines(lines)

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

        #self.fail("Test if the testcase is working.")

def getLinesAndReference():
    lines = """Model Parameters:
   Atom Energy Loss: Bethe
   Atom Mean Ionization Potential: Joy & Luo
   Atom Screening: Henoc & Maurice
   Atom Cross Section: Mott & Browning
   Atom Screening: Henoc & Maurice
   Atom Collision: Browning
   Atom Screening: Henoc & Maurice
   Atom Electron Range: Kanaya & Okayama
   Region Energy Loss: Bethe & Joy & Luo
   XRay Characteristic Cross Section: Castani
   XRay Bremsstrahlung Cross Section: Kirkpatrick & Wiedman
""".splitlines()

    modelParametersRef = ModelParameters.ModelParameters()
    modelParametersRef.atomEnergyLossModel = MCXRayModel.AtomEnergyLossModel.TYPE_BETHE
    modelParametersRef.atomMeanIonizationPotentialModel = MCXRayModel.AtomMeanIonizationPotentialModel.TYPE_JOY_LUO
    modelParametersRef.atomScreeningModel = MCXRayModel.AtomScreeningModel.TYPE_HENOC_MAURICE
    modelParametersRef.atomCrossSectionModel = MCXRayModel.AtomCrossSectionModel.TYPE_BROWNING
    modelParametersRef.atomCrossSectionScreeningModel = MCXRayModel.AtomCrossSectionScreeningModel.TYPE_HENOC_MAURICE
    modelParametersRef.atomCollisionModel = MCXRayModel.AtomCollisionModel.TYPE_BROWNING
    modelParametersRef.atomCollisionScreeningModel = MCXRayModel.AtomScreeningModel.TYPE_HENOC_MAURICE
    modelParametersRef.atomElectronRangeModel = MCXRayModel.AtomElectronRangeModel.TYPE_KANAYA_OKAYAMA
    modelParametersRef.regionEnergyLossModel = MCXRayModel.SampleEnergyLossModel.TYPE_BETHE_JOY_LUO
    modelParametersRef.characterisitcCrossSectionModel = MCXRayModel.XRayCSCharacteristicModel.TYPE_CASTANI1982
    modelParametersRef.bremsstrahlungCrossSectionModel = MCXRayModel.XRayCSBremsstrahlungModel.TYPE_KIRKPATRICK_WIEDMAN

    return lines, modelParametersRef

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from tests.testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__, withCoverage=False)
