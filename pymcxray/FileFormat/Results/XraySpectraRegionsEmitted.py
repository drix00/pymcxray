#!/usr/bin/env python
"""
.. py:currentmodule:: pymcxray.FileFormat.Results.XraySpectraRegionsEmitted
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Read all XraySpectraRegionsEmitted mcxray result files for all regions.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = "0.1"
__date__ = "Feb 12, 2015"
__copyright__ = "Copyright (c) 2015 Hendrix Demers"
__license__ = "GPL 3"

# Standard library modules.

# Third party modules.
import numpy as np

# Local modules.

# Project modules
from pymcxray.FileFormat.Results.XraySpectraRegionEmitted import XraySpectraRegionEmitted

# Globals and constants variables.

class XraySpectraRegionsEmitted(XraySpectraRegionEmitted):

    def read(self):
        regionID = 0
        super(XraySpectraRegionsEmitted, self).read(regionID=regionID)

        energies_keV = np.array(self.energies_keV)
        total_1_ekeVsr = np.array(self.total_1_ekeVsr)
        characteristic_1_ekeVsr = np.array(self.characteristic_1_ekeVsr)
        bremsstrahlung_1_ekeVsr = np.array(self.bremsstrahlung_1_ekeVsr)

        regionID += 1

        while True or regionID < 20:
            try:
                super(XraySpectraRegionsEmitted, self).read(regionID=regionID)

                total_1_ekeVsr += np.array(self.total_1_ekeVsr)
                characteristic_1_ekeVsr += np.array(self.characteristic_1_ekeVsr)
                bremsstrahlung_1_ekeVsr += np.array(self.bremsstrahlung_1_ekeVsr)
                regionID += 1
            except ValueError:
                break

        self.energies_keV = list(energies_keV)
        self.total_1_ekeVsr = list(total_1_ekeVsr)
        self.characteristic_1_ekeVsr = list(characteristic_1_ekeVsr)
        self.bremsstrahlung_1_ekeVsr = list(bremsstrahlung_1_ekeVsr)

def run():
    pass

if __name__ == '__main__':  #pragma: no cover
    run()