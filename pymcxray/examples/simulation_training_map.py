#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pymcxray.examples.simulation_test_maps
   :synopsis: Script to simulate mcxray maps for MM2017 with Nadi.

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Script to simulate mcxray maps for MM2017 with Nadi.
"""

###############################################################################
# Copyright 2017 Hendrix Demers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
###############################################################################

# Standard library modules.
import logging
import os.path

# Third party modules.
import matplotlib.pyplot as plt
import h5py
import numpy as np

# Local modules.

import pymcxray.mcxray as mcxray
import pymcxray.FileFormat.Results.XrayIntensities as XrayIntensities
import pymcxray.FileFormat.Results.XraySpectraSpecimenEmittedDetected as XraySpectraSpecimenEmittedDetected
import pymcxray.FileFormat.Results.ElectronResults as ElectronResults
import pymcxray.FileFormat.Results.XraySpectraRegionsEmitted as XraySpectraRegionsEmitted

from pymcxray.SimulationsParameters import SimulationsParameters, PARAMETER_INCIDENT_ENERGY_keV, PARAMETER_NUMBER_ELECTRONS, \
PARAMETER_BEAM_POSITION_nm, PARAMETER_NUMBER_XRAYS, PARAMETER_WEIGHT_FRACTIONS
from pymcxray.Simulation import createAlloyThinFilm

import pymcxray.FileFormat.Specimen as Specimen
import pymcxray.FileFormat.Region as Region
import pymcxray.FileFormat.RegionType as RegionType
import pymcxray.FileFormat.RegionDimensions as RegionDimensions
import pymcxray.FileFormat.Element as Element

# Project modules.
from pymcxray import get_current_module_path, get_mcxray_program_name

# Globals and constants variables.

class SimulationTrainingMapsMM2017(mcxray._Simulations):
    def _initData(self):
        self.use_hdf5 = True
        self.delete_result_files = False
        self.createBackup = True

        # Local variables for value and list if values.
        energy_keV = 30.0
        number_electrons = 10000
        number_xrays = 10
        weight_fract = [(0.975, 1.0-0.975)]  #Mass fraction of the two elements in the map
        
        xs_nm = np.linspace(-5.0e3, 5.0e3, 10) #Number of position acquired by side (# of pixel by side)
        probePositions_nm = [tuple(position_nm) for position_nm in
                             np.transpose([np.tile(xs_nm, len(xs_nm)), np.repeat(xs_nm, len(xs_nm))]).tolist()]

        # Simulation parameters
        self._simulationsParameters = SimulationsParameters()

        self._simulationsParameters.addVaried(PARAMETER_BEAM_POSITION_nm, probePositions_nm)
        
        self._simulationsParameters.addFixed(PARAMETER_WEIGHT_FRACTIONS, weight_fract)
        self._simulationsParameters.addFixed(PARAMETER_NUMBER_XRAYS, number_xrays)
        self._simulationsParameters.addFixed(PARAMETER_INCIDENT_ENERGY_keV, energy_keV)
        self._simulationsParameters.addFixed(PARAMETER_NUMBER_ELECTRONS, number_electrons)

    def getAnalysisName(self):
        return "SimulationTrainingMapsMM2017_wfFe975" # Name of the hdf5 file created

    def createSpecimen(self, parameters):
        weight_fract = parameters[PARAMETER_WEIGHT_FRACTIONS]
        
        elements = [(26, weight_fract[0]), (27, weight_fract[1])] # (Atomic number, mass fraction)
        
        filmThickness_nm = 200.0
        specimen = createAlloyThinFilm(elements, filmThickness_nm)
        
        return specimen

    def read_one_results_hdf5(self, simulation, hdf5_group):
        electronResults = ElectronResults.ElectronResults()
        electronResults.path = self.getSimulationsPath()
        electronResults.basename = simulation.resultsBasename
        electronResults.read()
        electronResults.write_hdf5(hdf5_group)

        xrayIntensities = XrayIntensities.XrayIntensities()
        xrayIntensities.path = self.getSimulationsPath()
        xrayIntensities.basename = simulation.resultsBasename
        xrayIntensities.read()
        xrayIntensities.write_hdf5(hdf5_group)

        spectrum = XraySpectraRegionsEmitted.XraySpectraRegionsEmitted()
        spectrum.path = self.getSimulationsPath()
        spectrum.basename = simulation.resultsBasename
        spectrum.read()
        spectrum.write_hdf5(hdf5_group)

        spectrum = XraySpectraSpecimenEmittedDetected.XraySpectraSpecimenEmittedDetected()
        spectrum.path = self.getSimulationsPath()
        spectrum.basename = simulation.resultsBasename
        spectrum.read()
        spectrum.write_hdf5(hdf5_group)

    def analyze_results_hdf5(self): #pragma: no cover
        self.readResults()

        file_path = self.get_hdf5_file_path()
        with h5py.File(file_path, 'r', driver='core') as hdf5_file:
            hdf5_group = self.get_hdf5_group(hdf5_file)
            logging.info(hdf5_group.name)

def run():
    # import the batch file class.
    from pymcxray.BatchFileConsole import BatchFileConsole

    # Find the configuration file path
    configuration_file_path = get_current_module_path(__file__, "MCXRay_latest.cfg")
    program_name = get_mcxray_program_name(configuration_file_path)

    # Create the batch file object.
    batch_file = BatchFileConsole("BatchSimulationTrainingMapsMM2017", program_name, numberFiles=10)

    # Create the simulation object and add the batch file object to it.
    analyze = SimulationTrainingMapsMM2017(relativePath=r"mcxray/SimulationTrainingMapsMM2017",
                                       configurationFilepath=configuration_file_path)
    analyze.run(batch_file)


if __name__ == '__main__': #pragma: no cover
    import sys
    logging.getLogger().setLevel(logging.INFO)
    logging.info(sys.argv)
    if len(sys.argv) == 1:
        #sys.argv.append(mcxray.ANALYZE_TYPE_GENERATE_INPUT_FILE)
        #sys.argv.append(mcxray.ANALYZE_TYPE_CHECK_PROGRESS)
        sys.argv.append(mcxray.ANALYZE_TYPE_READ_RESULTS)
        #sys.argv.append(mcxray.ANALYZE_TYPE_ANALYZE_RESULTS)
        #sys.argv.append(mcxray.ANALYZE_TYPE_ANALYZE_SCHEDULED_READ)
    run()

