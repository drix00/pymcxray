#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.ElectronExistResults
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Read electron exit results simulated with MCXRay.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2012 Hendrix Demers"
__license__ = ""

# Standard library modules.
import csv
import math

# Third party modules.
import numpy as np
import scipy.stats

# Local modules.

# Project modules
import pymcxray.FileFormat.Results.BaseResults as BaseResults

# Globals and constants variables.
X_nm = "X (nm)"
Y_nm = "Y (nm)"
Z_nm = "Z (nm)"
CORRECTED_X_nm = "Corrected X (nm)"
CORRECTED_Y_nm = "Corrected Y (nm)"
CORRECTED_Z_nm = "Corrected Z (nm)"
MINIMUM_X_SAMPLE_nm = "Minimum X (nm)"
MINIMUM_Y_SAMPLE_nm = "Minimum Y (nm)"
MINIMUM_Z_SAMPLE_nm = "Minimum Z (nm)"
MAXIMUM_X_SAMPLE_nm = "Maximum X (nm)"
MAXIMUM_Y_SAMPLE_nm = "Maximum Y (nm)"
MAXIMUM_Z_SAMPLE_nm = "Maximum Z (nm)"
MINIMUM_X_BEAM_nm = "Minimum X (nm) Beam"
MINIMUM_Y_BEAM_nm = "Minimum Y (nm) Beam"
MINIMUM_Z_BEAM_nm = "Minimum Z (nm) Beam"
MAXIMUM_X_BEAM_nm = "Maximum X (nm) Beam"
MAXIMUM_Y_BEAM_nm = "Maximum Y (nm) Beam"
MAXIMUM_Z_BEAM_nm = "Maximum Z (nm) Beam"
E_keV = "E (keV)"
DELTA_E_keV = "DeltaE (keV)"
THETA_rad = "Theta (rad)"
CORRECTED_THETA_rad = "Corrected Theta (rad)"
PHI_rad = "Phi (rad)"
CORRECTED_PHI_rad = "Corrected Phi (rad)"

class ElectronDetector(object):
    def __init__(self):
        self.energyRange_keV = (None, None)
        self.polarAngleRange_deg = (0.0, math.degrees(math.pi))
        self.azimuthalAngleRange_deg = (0.0, math.degrees(2.0*math.pi))

    def detectElectrons(self, data):
        pass

    @property
    def minimumEnergy_keV(self):
        return self._miniumEnergy_keV
    @minimumEnergy_keV.setter
    def minimumEnergy_keV(self, minimumEnergy_keV):
        self._minimumEnergy_keV = minimumEnergy_keV
    @property
    def maximumEnergy_keV(self):
        return self._maxniumEnergy_keV
    @maximumEnergy_keV.setter
    def maximumEnergy_keV(self, maximumEnergy_keV):
        self._maximumEnergy_keV = maximumEnergy_keV
    @property
    def energyRange_keV(self):
        return (self.minimumEnergy_keV, self.maximumEnergy_keV)
    @energyRange_keV.setter
    def energyRange_keV(self, energyRange_keV):
        self.minimumEnergy_keV, self.maximumEnergy_keV = energyRange_keV

    @property
    def minimumPolarAngle_deg(self):
        return self._miniumPolarAngle_deg
    @minimumPolarAngle_deg.setter
    def minimumPolarAngle_deg(self, minimumPolarAngle_deg):
        self._minimumPolarAngle_deg = minimumPolarAngle_deg
    @property
    def maximumPolarAngle_deg(self):
        return self._maxniumPolarAngle_deg
    @maximumPolarAngle_deg.setter
    def maximumPolarAngle_deg(self, maximumPolarAngle_deg):
        self._maximumPolarAngle_deg = maximumPolarAngle_deg
    @property
    def polarAngleRange_deg(self):
        return (self.minimumPolarAngle_deg, self.maximumPolarAngle_deg)
    @polarAngleRange_deg.setter
    def polarAngleRange_deg(self, polarAngleRange_deg):
        self.minimumPolarAngle_deg, self.maximumPolarAngle_deg = polarAngleRange_deg

    @property
    def minimumAzimuthalAngle_deg(self):
        return self._miniumAzimuthalAngle_deg
    @minimumAzimuthalAngle_deg.setter
    def minimumAzimuthalAngle_deg(self, minimumAzimuthalAngle_deg):
        self._minimumAzimuthalAngle_deg = minimumAzimuthalAngle_deg
    @property
    def maximumAzimuthalAngle_deg(self):
        return self._maxniumAzimuthalAngle_deg
    @maximumAzimuthalAngle_deg.setter
    def maximumAzimuthalAngle_deg(self, maximumAzimuthalAngle_deg):
        self._maximumAzimuthalAngle_deg = maximumAzimuthalAngle_deg
    @property
    def azimuthalAngleRange_deg(self):
        return (self.minimumAzimuthalAngle_deg, self.maximumAzimuthalAngle_deg)
    @azimuthalAngleRange_deg.setter
    def azimuthalAngleRange_deg(self, azimuthalAngleRange_deg):
        self.minimumAzimuthalAngle_deg, self.maximumAzimuthalAngle_deg = azimuthalAngleRange_deg

class ElectronExistResults(BaseResults.BaseResults):
    def __init__(self, *args, **kargs):
        super(ElectronExistResults, self).__init__(*args, **kargs)

        self._data = {}

    def _createFilename(self):
        suffix = "_ElectronExitResults.csv"
        filename = self.basename + suffix
        return filename

    def read(self):
        reader = csv.DictReader(open(self.filepath, 'r'))
        data = {}
        for fieldname in reader.fieldnames:
            data.setdefault(fieldname.strip(), [])

        for row in reader:
            for fieldname in reader.fieldnames:
                data[fieldname.strip()].append(float(row[fieldname]))

        for key in data:
            data[key] = np.array(data[key])

        self._data = data

    def getEnergyDistribution(self, numberBins=10):
        if self.numberData == 0:
            self.read()

        histogram, low_range, binsize, _extrapoints = scipy.stats.histogram(self.data[E_keV], numbins=numberBins)

        startEnergy_keV = low_range + binsize/2.0
        endEnergy_keV = startEnergy_keV + len(histogram) *binsize
        stepEnergy_keV = binsize
        energies_keV = np.arange(startEnergy_keV, endEnergy_keV, stepEnergy_keV)

        return energies_keV, histogram

    @property
    def numberData(self):
        try:
            return len(self._data[X_nm]);
        except KeyError:
            return 0

    @property
    def data(self):
        return self._data
