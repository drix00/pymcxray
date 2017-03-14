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
PARAMETER_BEAM_POSITION_nm, PARAMETER_NUMBER_XRAYS

import pymcxray.FileFormat.Specimen as Specimen
import pymcxray.FileFormat.Region as Region
import pymcxray.FileFormat.RegionType as RegionType
import pymcxray.FileFormat.RegionDimensions as RegionDimensions
import pymcxray.FileFormat.Element as Element

# Project modules.
from pymcxray import get_current_module_path, get_mcxray_program_name

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
        probePositions_nm = [tuple(position_nm) for position_nm in
                             np.transpose([np.tile(xs_nm, len(xs_nm)), np.repeat(xs_nm, len(xs_nm))]).tolist()]

        # Simulation parameters
        self._simulationsParameters = SimulationsParameters()

        self._simulationsParameters.addVaried(PARAMETER_NUMBER_XRAYS, number_xrays_list)
        self._simulationsParameters.addVaried(PARAMETER_BEAM_POSITION_nm, probePositions_nm)

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
        region.elements = [Element.Element(27, massFraction=0.01), Element.Element(26, massFraction=0.99)]
        region.regionType = RegionType.REGION_TYPE_BOX
        parameters = [-7.5e4, -2.5e4, -7.5e4, -2.5e4, 0.0, 0.2e4]
        region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
        specimen.regions.append(region)

        # Region 2
        region = Region.Region()
        region.numberElements = 2
        region.elements = [Element.Element(27, massFraction=0.02), Element.Element(26, massFraction=0.98)]
        region.regionType = RegionType.REGION_TYPE_BOX
        parameters = [-2.5e4, 2.5e4, -7.5e4, -2.5e4, 0.0, 0.2e4]
        region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
        specimen.regions.append(region)

        # Region 3
        region = Region.Region()
        region.numberElements = 2
        region.elements = [Element.Element(27, massFraction=0.05), Element.Element(26, massFraction=0.95)]
        region.regionType = RegionType.REGION_TYPE_BOX
        parameters = [2.5e4, 7.5e4, -7.5e4, -2.5e4, 0.0, 0.2e4]
        region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
        specimen.regions.append(region)

        # Region 4
        region = Region.Region()
        region.numberElements = 2
        region.elements = [Element.Element(28, massFraction=0.01), Element.Element(27, massFraction=0.99)]
        region.regionType = RegionType.REGION_TYPE_BOX
        parameters = [-7.5e4, -2.5e4, -2.5e4, 2.5e4, 0.0, 0.2e4]
        region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
        specimen.regions.append(region)

        # Region 5
        region = Region.Region()
        region.numberElements = 2
        region.elements = [Element.Element(28, massFraction=0.02), Element.Element(27, massFraction=0.98)]
        region.regionType = RegionType.REGION_TYPE_BOX
        parameters = [-2.5e4, 2.5e4, -2.5e4, 2.5e4, 0.0, 0.2e4]
        region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
        specimen.regions.append(region)

        # Region 6
        region = Region.Region()
        region.numberElements = 2
        region.elements = [Element.Element(28, massFraction=0.05), Element.Element(27, massFraction=0.95)]
        region.regionType = RegionType.REGION_TYPE_BOX
        parameters = [2.5e4, 7.5e4, -2.5e4, 2.5e4, 0.0, 0.2e4]
        region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
        specimen.regions.append(region)

        # Region 7
        region = Region.Region()
        region.numberElements = 3
        region.elements = [Element.Element(27, massFraction=0.01), Element.Element(26, massFraction=0.495), Element.Element(28, massFraction=0.495)]
        region.regionType = RegionType.REGION_TYPE_BOX
        parameters = [-7.5e4, -2.5e4, 2.5e4, 7.5e4, 0.0, 0.2e4]
        region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
        specimen.regions.append(region)

        # Region 8
        region = Region.Region()
        region.numberElements = 3
        region.elements = [Element.Element(27, massFraction=0.02), Element.Element(26, massFraction=0.49), Element.Element(28, massFraction=0.49)]
        region.regionType = RegionType.REGION_TYPE_BOX
        parameters = [-2.5e4, 2.5e4, 2.5e4, 7.5e4, 0.0, 0.2e4]
        region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
        specimen.regions.append(region)

        # Region 9
        region = Region.Region()
        region.numberElements = 3
        region.elements = [Element.Element(27, massFraction=0.05), Element.Element(26, massFraction=0.475), Element.Element(28, massFraction=0.475)]
        region.regionType = RegionType.REGION_TYPE_BOX
        parameters = [2.5e4, 7.5e4, 2.5e4, 7.5e4, 0.0, 0.2e4]
        region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
        specimen.regions.append(region)

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
    batch_file = BatchFileConsole("BatchSimulationTestMapsMM2017", program_name, numberFiles=6)

    # Create the simulation object and add the batch file object to it.
    analyze = SimulationTestMapsMM2017(relativePath=r"mcxray/SimulationTestMapsMM2017",
                                       configurationFilepath=configuration_file_path)
    analyze.run(batch_file)


if __name__ == '__main__': #pragma: no cover
    import sys
    logging.getLogger().setLevel(logging.INFO)
    logging.info(sys.argv)
    if len(sys.argv) == 1:
        sys.argv.append(mcxray.ANALYZE_TYPE_GENERATE_INPUT_FILE)
        #sys.argv.append(mcxray.ANALYZE_TYPE_CHECK_PROGRESS)
        #sys.argv.append(mcxray.ANALYZE_TYPE_ANALYZE_RESULTS)
        #sys.argv.append(mcxray.ANALYZE_TYPE_ANALYZE_SCHEDULED_READ)
    run()

