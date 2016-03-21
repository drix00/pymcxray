#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.MCXRayModel
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Model type used in MCXRay.
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
import abc

# Third party modules.

# Local modules.

# Project modules

# Globals and constants variables.

class MCXRayModel(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, currentModel=None):
        self._models = []
        self._modelNames = {}

        self._initModel()

        if currentModel is not None:
            self.setModel(currentModel)

    @abc.abstractmethod
    def _initModel(self): # pragma: no cover
        raise NotImplementedError

    def setModel(self, modelType):
        self._currentModel = self._models[modelType]

    def getModel(self):
        return self._currentModel

    def setModelFromString(self, text):
        for modelType in self._modelNames:
            if self._modelNames[modelType] == text.strip():
                self.setModel(modelType)
                return
        else:
            message = "Model not found from the string: %s" % (text)
            raise ValueError(message)

class AtomMeanIonizationPotentialModel(MCXRayModel):
    TYPE_JOY_LUO = 0

    def _initModel(self):
        self._models.append(self.TYPE_JOY_LUO)
        self._modelNames[self.TYPE_JOY_LUO] = "Joy & Luo"

        self.setModel(self.TYPE_JOY_LUO)

class AtomEnergyLossModel(MCXRayModel):
    TYPE_BETHE = 0

    def _initModel(self):
        self._models.append(self.TYPE_BETHE)
        self._modelNames[self.TYPE_BETHE] = "Bethe"

        self.setModel(self.TYPE_BETHE)

class AtomScreeningModel(MCXRayModel):
    TYPE_HENOC_MAURICE = 0

    def _initModel(self):
        self._models.append(self.TYPE_HENOC_MAURICE)
        self._modelNames[self.TYPE_HENOC_MAURICE] = "Henoc & Maurice"

        self.setModel(self.TYPE_HENOC_MAURICE)

class AtomCrossSectionModel(MCXRayModel):
    TYPE_BROWNING = 0
    TYPE_GAUVIN_DROUIN = 1

    def _initModel(self):
        self._models.append(self.TYPE_BROWNING)
        self._models.append(self.TYPE_GAUVIN_DROUIN)
        self._modelNames[self.TYPE_BROWNING] = "Mott & Browning"
        self._modelNames[self.TYPE_GAUVIN_DROUIN] = "Gauvin & Drouin"

        self.setModel(self.TYPE_BROWNING)

class AtomCrossSectionScreeningModel(MCXRayModel):
    TYPE_HENOC_MAURICE = 0

    def _initModel(self):
        self._models.append(self.TYPE_HENOC_MAURICE)
        self._modelNames[self.TYPE_HENOC_MAURICE] = "Henoc & Maurice"

        self.setModel(self.TYPE_HENOC_MAURICE)

class AtomCollisionModel(MCXRayModel):
    TYPE_RUTHERFORD = 0
    TYPE_BROWNING = 1
    TYPE_GAUVIN = 2

    def _initModel(self):
        self._models.append(self.TYPE_RUTHERFORD)
        self._models.append(self.TYPE_BROWNING)
        self._models.append(self.TYPE_GAUVIN)
        self._modelNames[self.TYPE_RUTHERFORD] = "Rutherford"
        self._modelNames[self.TYPE_BROWNING] = "Browning"
        self._modelNames[self.TYPE_GAUVIN] = "Gauvin"

        self.setModel(self.TYPE_BROWNING)

class AtomCollisionScreeningModel(MCXRayModel):
    TYPE_HENOC_MAURICE = 0

    def _initModel(self):
        self._models.append(self.TYPE_HENOC_MAURICE)
        self._modelNames[self.TYPE_HENOC_MAURICE] = "Henoc & Maurice"

        self.setModel(self.TYPE_HENOC_MAURICE)

class AtomElectronRangeModel(MCXRayModel):
    TYPE_KANAYA_OKAYAMA = 0

    def _initModel(self):
        self._models.append(self.TYPE_KANAYA_OKAYAMA)
        self._modelNames[self.TYPE_KANAYA_OKAYAMA] = "Kanaya & Okayama"

        self.setModel(self.TYPE_KANAYA_OKAYAMA)

class XRayCSCharacteristicModel(MCXRayModel):
    TYPE_CASTANI1982 = 0
    TYPE_BOTE2009 = 1

    def _initModel(self):
        self._models.append(self.TYPE_CASTANI1982)
        self._models.append(self.TYPE_BOTE2009)
        self._modelNames[self.TYPE_CASTANI1982] = "Castani"
        self._modelNames[self.TYPE_BOTE2009] = "Bote (2009)"

        self.setModel(self.TYPE_BOTE2009)

class XRayCSBremsstrahlungModel(MCXRayModel):
    TYPE_BETHE_HEITLER = 0
    TYPE_KIRKPATRICK_WIEDMAN = 1
    TYPE_DING = 2
    TYPE_GAUVIN = 3

    def _initModel(self):
        self._models.append(self.TYPE_BETHE_HEITLER)
        self._models.append(self.TYPE_KIRKPATRICK_WIEDMAN)
        self._models.append(self.TYPE_DING)
        self._models.append(self.TYPE_GAUVIN)
        self._modelNames[self.TYPE_BETHE_HEITLER] = "Bethe & Heitler"
        self._modelNames[self.TYPE_KIRKPATRICK_WIEDMAN] = "Kirkpatrick & Wiedman"
        self._modelNames[self.TYPE_DING] = "Ding"
        self._modelNames[self.TYPE_GAUVIN] = "Gauvin"

        self.setModel(self.TYPE_KIRKPATRICK_WIEDMAN)

class MassAbsorptionCoefficientModel(MCXRayModel):
    TYPE_HENKE = 0
    TYPE_HEINRICH_DATA = 1
    TYPE_HEINRICH_PARAMETERIZATION = 2
    TYPE_CHANTLER2005 = 3

    def _initModel(self):
        self._models.append(self.TYPE_HENKE)
        self._models.append(self.TYPE_HEINRICH_DATA)
        self._models.append(self.TYPE_HEINRICH_PARAMETERIZATION)
        self._models.append(self.TYPE_CHANTLER2005)
        self._modelNames[self.TYPE_HENKE] = "Henke"
        self._modelNames[self.TYPE_HEINRICH_DATA] = "Heinrich Data (1966)"
        self._modelNames[self.TYPE_HEINRICH_PARAMETERIZATION] = "Heinrich Parameters (1987)"
        self._modelNames[self.TYPE_CHANTLER2005] = "Chantler (2005)"

        self.setModel(self.TYPE_CHANTLER2005)

class SampleEnergyLossModel(MCXRayModel):
    TYPE_BETHE_JOY_LUO = 0

    def _initModel(self):
        self._models.append(self.TYPE_BETHE_JOY_LUO)
        self._modelNames[self.TYPE_BETHE_JOY_LUO] = "Bethe & Joy & Luo"

        self.setModel(self.TYPE_BETHE_JOY_LUO)

class RegionEnergyLossModel(MCXRayModel):
    TYPE_BETHE_JOY_LUO = 0
    TYPE_BETHE = 1
    TYPE_BETHE_RELATIVISTIC = 2
    TYPE_JOY_LUO_KGAUVIN = 3
    TYPE_JOY_LUO_MONSEL = 4

    def _initModel(self):
        self._models.append(self.TYPE_BETHE_JOY_LUO)
        self._models.append(self.TYPE_BETHE)
        self._models.append(self.TYPE_BETHE_RELATIVISTIC)
        self._models.append(self.TYPE_JOY_LUO_KGAUVIN)
        self._models.append(self.TYPE_JOY_LUO_MONSEL)
        self._modelNames[self.TYPE_BETHE_JOY_LUO] = "Bethe & Joy & Luo"
        self._modelNames[self.TYPE_BETHE] = "Bethe"
        self._modelNames[self.TYPE_BETHE_RELATIVISTIC] = "Bethe Relativistic"
        self._modelNames[self.TYPE_JOY_LUO_KGAUVIN] = "Joy & Luo & Gauvin"
        self._modelNames[self.TYPE_JOY_LUO_MONSEL] = "Joy & Luo & Monsel"

        self.setModel(self.TYPE_BETHE_JOY_LUO)

class SpectrumInterpolationModel(MCXRayModel):
    TYPE_COPY = 0
    TYPE_LINEAR = 1
    TYPE_LINEAR_DOUBLE = 2
    TYPE_SPLINE = 3
    TYPE_SPLINE_BATCH = 4
    TYPE_SPLINE_POINT = 5

    def _initModel(self):
        self._models.append(self.TYPE_COPY)
        self._models.append(self.TYPE_LINEAR)
        self._models.append(self.TYPE_LINEAR_DOUBLE)
        self._models.append(self.TYPE_SPLINE)
        self._models.append(self.TYPE_SPLINE_BATCH)
        self._models.append(self.TYPE_SPLINE_POINT)
        self._modelNames[self.TYPE_COPY] = "Copy"
        self._modelNames[self.TYPE_LINEAR] = "Linear"
        self._modelNames[self.TYPE_LINEAR_DOUBLE] = "Linear Double"
        self._modelNames[self.TYPE_SPLINE] = "Spline"
        self._modelNames[self.TYPE_SPLINE_BATCH] = "Spline Batch"
        self._modelNames[self.TYPE_SPLINE_POINT] = "Spline Point"

        self.setModel(self.TYPE_LINEAR_DOUBLE)
