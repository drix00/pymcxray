#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: mcxray.examples.simulation_test_maps
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

# Third party modules.
import h5py
import numpy as np

# Local modules.

import mcxray.analyze_mcxray as mcxray
import mcxray.format.results.XrayIntensities as XrayIntensities
import mcxray.format.results.XraySpectraSpecimenEmittedDetected as XraySpectraSpecimenEmittedDetected
import mcxray.format.results.ElectronResults as ElectronResults
import mcxray.format.results.XraySpectraRegionsEmitted as XraySpectraRegionsEmitted

from mcxray.SimulationsParameters import SimulationsParameters, PARAMETER_INCIDENT_ENERGY_keV, \
    PARAMETER_NUMBER_ELECTRONS, PARAMETER_BEAM_POSITION_nm, PARAMETER_NUMBER_XRAYS
from mcxray.SimulationOld import createAlloyThinFilm

# Project modules.
from mcxray import get_current_module_path, get_mcxray_program_name

# Globals and constants variables.


class SimulationTrainingMapsMM2017(mcxray._Simulations):
    def __init__(self, simulation_name, elements, **kwargs):
        super().__init__(**kwargs)

        self.elements = elements
        self.simulation_name = simulation_name

    def _initData(self):
        self.use_hdf5 = True
        self.delete_result_files = False
        self.createBackup = True

        # Local variables for value and list if values.
        energy_keV = 30.0
        number_electrons = 10000
        number_xrays = 10

        xs_nm = np.linspace(-5.0e3, 5.0e3, 10)  # Number of position acquired by side (# of pixel by side)
        probe_positions_nm = [tuple(position_nm) for position_nm in np.transpose([np.tile(xs_nm, len(xs_nm)),
                                                                                  np.repeat(xs_nm, len(xs_nm))
                                                                                  ]).tolist()]

        # Simulation parameters
        self._simulationsParameters = SimulationsParameters()

        self._simulationsParameters.addVaried(PARAMETER_BEAM_POSITION_nm, probe_positions_nm)

        self._simulationsParameters.addFixed(PARAMETER_NUMBER_XRAYS, number_xrays)
        self._simulationsParameters.addFixed(PARAMETER_INCIDENT_ENERGY_keV, energy_keV)
        self._simulationsParameters.addFixed(PARAMETER_NUMBER_ELECTRONS, number_electrons)

    def getAnalysisName(self):
        return self.simulation_name

    def createSpecimen(self, parameters):
        film_thickness_nm = 200.0
        specimen = createAlloyThinFilm(self.elements, film_thickness_nm)

        return specimen

    def read_one_results_hdf5(self, simulation, hdf5_group):
        electron_results = ElectronResults.ElectronResults()
        electron_results.path = self.getSimulationsPath()
        electron_results.basename = simulation.resultsBasename
        electron_results.read()
        electron_results.write_hdf5(hdf5_group)

        xray_intensities = XrayIntensities.XrayIntensities()
        xray_intensities.path = self.getSimulationsPath()
        xray_intensities.basename = simulation.resultsBasename
        xray_intensities.read()
        xray_intensities.write_hdf5(hdf5_group)

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

    def analyze_results_hdf5(self):  # pragma: no cover
        self.readResults()

        file_path = self.get_hdf5_file_path()
        with h5py.File(file_path, 'r', driver='core') as hdf5_file:
            hdf5_group = self.get_hdf5_group(hdf5_file)
            logging.info(hdf5_group.name)


def run():
    simulation_name = "SimulationTrainingMapsMM2017_Fe075"
    elements = [(26, 0.75), (27, 0.25)]

    # import the batch file class.
    from mcxray.BatchFileConsole import BatchFileConsole

    # Find the configuration file path
    configuration_file_path = get_current_module_path(__file__, "MCXRay_latest.cfg")
    program_name = get_mcxray_program_name(str(configuration_file_path))

    # Create the batch file object.
    batch_file = BatchFileConsole("BatchSimulationTrainingMapsMM2017", program_name, numberFiles=10)

    # Create the simulation object and add the batch file object to it.
    analyze = SimulationTrainingMapsMM2017(simulation_name, elements,
                                           relativePath=r"mcxray/SimulationTrainingMapsMM2017",
                                           configurationFilepath=configuration_file_path)
    analyze.run(batch_file)


if __name__ == '__main__':  # pragma: no cover
    import sys
    logging.getLogger().setLevel(logging.INFO)
    logging.info(sys.argv)
    if len(sys.argv) == 1:
        sys.argv.append(mcxray.ANALYZE_TYPE_GENERATE_INPUT_FILE)
        # sys.argv.append(mcxray.ANALYZE_TYPE_CHECK_PROGRESS)
        # sys.argv.append(mcxray.ANALYZE_TYPE_READ_RESULTS)
        # sys.argv.append(mcxray.ANALYZE_TYPE_ANALYZE_RESULTS)
        # sys.argv.append(mcxray.ANALYZE_TYPE_ANALYZE_SCHEDULED_READ)
    run()
