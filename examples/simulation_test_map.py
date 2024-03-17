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

import mcxray.format.Specimen as Specimen
import mcxray.format.Region as Region
import mcxray.format.RegionType as RegionType
import mcxray.format.RegionDimensions as RegionDimensions
import mcxray.format.Element as Element

# Project modules.
from mcxray import get_current_module_path, get_mcxray_program_name

# Globals and constants variables.


class SimulationTestMapsMM2017(mcxray._Simulations):
    def _initData(self):
        self.use_hdf5 = True
        self.delete_result_files = False
        self.createBackup = True

        # Local variables for value and list if values.
        energy_keV = 30.0
        number_electrons = 10000

        # number_xrays_list = [10, 20, 30, 50, 60, 100, 200, 500, 1000]
        number_xrays_list = [10]
        xs_nm = np.linspace(-5.0e3, 5.0e3, 3)
        probe_positions_nm = [tuple(position_nm) for position_nm in
                              np.transpose([np.tile(xs_nm, len(xs_nm)), np.repeat(xs_nm, len(xs_nm))]).tolist()]

        # Simulation parameters
        self._simulationsParameters = SimulationsParameters()

        self._simulationsParameters.addVaried(PARAMETER_NUMBER_XRAYS, number_xrays_list)
        self._simulationsParameters.addVaried(PARAMETER_BEAM_POSITION_nm, probe_positions_nm)

        self._simulationsParameters.addFixed(PARAMETER_INCIDENT_ENERGY_keV, energy_keV)
        self._simulationsParameters.addFixed(PARAMETER_NUMBER_ELECTRONS, number_electrons)

    def getAnalysisName(self):
        return "SimulationTestMapsMM2017"

    def createSpecimen(self, parameters):
        specimen = Specimen.Specimen()

        specimen.name = "Maps01"

        specimen.numberRegions = 10

        # Region 0
        region = Region.Region()
        region.numberElements = 0
        region.regionType = RegionType.REGION_TYPE_BOX
        parameters = [-10000000000.0, 10000000000.0, -10000000000.0, 10000000000.0, 0.0, 20000000000.0]
        region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
        specimen.regions.append(region)

        # Region 1
        region = Region.Region()
        region.numberElements = 2
        region.elements = [Element.Element(27, massFraction=0.01),
                           Element.Element(26, massFraction=0.99)]
        region.regionType = RegionType.REGION_TYPE_BOX
        parameters = [-7.5e4, -2.5e4, -7.5e4, -2.5e4, 0.0, 0.2e4]
        region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
        specimen.regions.append(region)

        # Region 2
        region = Region.Region()
        region.numberElements = 2
        region.elements = [Element.Element(27, massFraction=0.02),
                           Element.Element(26, massFraction=0.98)]
        region.regionType = RegionType.REGION_TYPE_BOX
        parameters = [-2.5e4, 2.5e4, -7.5e4, -2.5e4, 0.0, 0.2e4]
        region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
        specimen.regions.append(region)

        # Region 3
        region = Region.Region()
        region.numberElements = 2
        region.elements = [Element.Element(27, massFraction=0.05),
                           Element.Element(26, massFraction=0.95)]
        region.regionType = RegionType.REGION_TYPE_BOX
        parameters = [2.5e4, 7.5e4, -7.5e4, -2.5e4, 0.0, 0.2e4]
        region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
        specimen.regions.append(region)

        # Region 4
        region = Region.Region()
        region.numberElements = 2
        region.elements = [Element.Element(28, massFraction=0.01),
                           Element.Element(27, massFraction=0.99)]
        region.regionType = RegionType.REGION_TYPE_BOX
        parameters = [-7.5e4, -2.5e4, -2.5e4, 2.5e4, 0.0, 0.2e4]
        region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
        specimen.regions.append(region)

        # Region 5
        region = Region.Region()
        region.numberElements = 2
        region.elements = [Element.Element(28, massFraction=0.02),
                           Element.Element(27, massFraction=0.98)]
        region.regionType = RegionType.REGION_TYPE_BOX
        parameters = [-2.5e4, 2.5e4, -2.5e4, 2.5e4, 0.0, 0.2e4]
        region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
        specimen.regions.append(region)

        # Region 6
        region = Region.Region()
        region.numberElements = 2
        region.elements = [Element.Element(28, massFraction=0.05),
                           Element.Element(27, massFraction=0.95)]
        region.regionType = RegionType.REGION_TYPE_BOX
        parameters = [2.5e4, 7.5e4, -2.5e4, 2.5e4, 0.0, 0.2e4]
        region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
        specimen.regions.append(region)

        # Region 7
        region = Region.Region()
        region.numberElements = 3
        region.elements = [Element.Element(27, massFraction=0.01),
                           Element.Element(26, massFraction=0.495),
                           Element.Element(28, massFraction=0.495)]
        region.regionType = RegionType.REGION_TYPE_BOX
        parameters = [-7.5e4, -2.5e4, 2.5e4, 7.5e4, 0.0, 0.2e4]
        region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
        specimen.regions.append(region)

        # Region 8
        region = Region.Region()
        region.numberElements = 3
        region.elements = [Element.Element(27, massFraction=0.02),
                           Element.Element(26, massFraction=0.49),
                           Element.Element(28, massFraction=0.49)]
        region.regionType = RegionType.REGION_TYPE_BOX
        parameters = [-2.5e4, 2.5e4, 2.5e4, 7.5e4, 0.0, 0.2e4]
        region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
        specimen.regions.append(region)

        # Region 9
        region = Region.Region()
        region.numberElements = 3
        region.elements = [Element.Element(27, massFraction=0.05),
                           Element.Element(26, massFraction=0.475),
                           Element.Element(28, massFraction=0.475)]
        region.regionType = RegionType.REGION_TYPE_BOX
        parameters = [2.5e4, 7.5e4, 2.5e4, 7.5e4, 0.0, 0.2e4]
        region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
        specimen.regions.append(region)

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
    # import the batch file class.
    from mcxray.batch_file_console import BatchFileConsole

    # Find the configuration file path
    configuration_file_path = get_current_module_path(__file__, "MCXRay_latest.cfg")
    program_name = get_mcxray_program_name(str(configuration_file_path))

    # Create the batch file object.
    batch_file = BatchFileConsole("BatchSimulationTestMapsMM2017", program_name, number_files=6)

    # Create the simulation object and add the batch file object to it.
    analyze = SimulationTestMapsMM2017(relativePath=r"mcxray/SimulationTestMapsMM2017",
                                       configurationFilepath=configuration_file_path)
    analyze.run(batch_file)


if __name__ == '__main__':  # pragma: no cover
    import sys
    logging.getLogger().setLevel(logging.INFO)
    logging.info(sys.argv)
    if len(sys.argv) == 1:
        sys.argv.append(mcxray.ANALYZE_TYPE_GENERATE_INPUT_FILE)
        # sys.argv.append(mcxray.ANALYZE_TYPE_CHECK_PROGRESS)
        # sys.argv.append(mcxray.ANALYZE_TYPE_ANALYZE_RESULTS)
        # sys.argv.append(mcxray.ANALYZE_TYPE_ANALYZE_SCHEDULED_READ)
    run()