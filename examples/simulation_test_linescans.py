#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: mcxray.examples.simulation_test_linescans
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

# Local modules.

import mcxray.analyze_mcxray as mcxray

from mcxray.SimulationsParameters import SimulationsParameters, PARAMETER_INCIDENT_ENERGY_keV, \
    PARAMETER_NUMBER_ELECTRONS, PARAMETER_BEAM_POSITION_nm, PARAMETER_NUMBER_XRAYS

from mcxray.format.results.ElectronTrajectoriesResults import ElectronTrajectoriesResults, COLOR_REGION

# Project modules.
from mcxray import get_current_module_path, get_mcxray_program_name
from examples.simulation_test_map import SimulationTestMapsMM2017

# Globals and constants variables.


class SimulationTestLinescansMM2017(SimulationTestMapsMM2017):
    def _initData(self):
        self.use_hdf5 = False
        self.delete_result_files = False
        self.createBackup = True
        self.read_interval_h = 2
        self.read_interval_m = 10

        enegy_keV = 30.0
        number_electrons = 10000
        # number_xrays_list = [10, 20, 30, 50, 60, 100, 200, 500, 1000]
        number_xrays_list = [10]

        probePositions_nm = []
        probePositions_nm.append((0.0, -2559.0))
        probePositions_nm.append((0.0, -2480.0))
        probePositions_nm.append((0.0, -2401.0))
        probePositions_nm.append((0.0, 2401.0))
        probePositions_nm.append((0.0, 2480.0))
        probePositions_nm.append((0.0, 2559.0))

        self._simulationsParameters = SimulationsParameters()

        self._simulationsParameters.addVaried(PARAMETER_NUMBER_XRAYS, number_xrays_list)
        self._simulationsParameters.addVaried(PARAMETER_BEAM_POSITION_nm, probePositions_nm)

        self._simulationsParameters.addFixed(PARAMETER_INCIDENT_ENERGY_keV, enegy_keV)
        self._simulationsParameters.addFixed(PARAMETER_NUMBER_ELECTRONS, number_electrons)

    def getAnalysisName(self):
        return "SimulationTestLinescansMM2017"

    def readOneResults(self, simulation):
        filepath = os.path.join(self.getSimulationsPath(),
                                simulation.resultsBasename + "_ElectronTrajectoriesResults.csv")
        electronTrajectoriesResults = ElectronTrajectoriesResults(filepath)

        return electronTrajectoriesResults

    def analyzeResultsFiles(self):  # pragma: no cover
        self.readResults()

        allResults = self.getAllResults()

        figure_path = self.getAnalyzesPath()
        x_limit = (-1000.0, 1000.0)
        z_limit = (-200.0, 400.0)
        for key in allResults:
            position_y_nm = key[0][1]
            y_limit = (x_limit[0]+position_y_nm, x_limit[1]+position_y_nm)
            electronTrajectoriesResults = allResults[key]

            title = "Y = {} nm".format(int(position_y_nm))
            electronTrajectoriesResults.drawXZ(title=title, x_limit=x_limit, y_limit=z_limit)
            file_name = "trajectories_XZ_Y{}nm.png".format(int(position_y_nm))
            file_path = os.path.join(figure_path, file_name)
            plt.savefig(file_path)
            plt.close()
            electronTrajectoriesResults.drawXZ(colorType=COLOR_REGION, title=title, x_limit=x_limit, y_limit=z_limit)
            file_name = "trajectories_XZ_Y{}nm_region.png".format(int(position_y_nm))
            file_path = os.path.join(figure_path, file_name)
            plt.savefig(file_path)
            plt.close()
            electronTrajectoriesResults.drawXY(title=title, x_limit=x_limit, y_limit=y_limit)
            file_name = "trajectories_XY_Y{}nm.png".format(int(position_y_nm))
            file_path = os.path.join(figure_path, file_name)
            plt.savefig(file_path)
            plt.close()
            electronTrajectoriesResults.drawYZ(title=title, x_limit=y_limit, y_limit=z_limit)
            file_name = "trajectories_YZ_Y{}nm.png".format(int(position_y_nm))
            file_path = os.path.join(figure_path, file_name)
            plt.savefig(file_path)
            plt.close()


def run():
    import mcxray.BatchFileConsole as BatchFileConsole

    configurationFilepath = get_current_module_path(__file__, "../../MCXRay_latest.cfg")

    programName = get_mcxray_program_name(configurationFilepath)

    batchFile = BatchFileConsole.BatchFileConsole("BatchSimulationTestLinescansMM2017", programName, numberFiles=10)
    analyze = SimulationTestLinescansMM2017(relativePath=r"mcxray/SimulationTestLinescansMM2017",
                                            configurationFilepath=configurationFilepath)
    analyze.overwrite = False
    analyze.run(batchFile)

    plt.show()


if __name__ == '__main__':  # pragma: no cover
    import sys
    logging.getLogger().setLevel(logging.INFO)
    logging.info(sys.argv)
    sys.argv.append(mcxray.ANALYZE_TYPE_GENERATE_INPUT_FILE)
    # sys.argv.append(mcxray.ANALYZE_TYPE_CHECK_PROGRESS)
    # sys.argv.append(mcxray.ANALYZE_TYPE_ANALYZE_RESULTS)
    # sys.argv.append(mcxray.ANALYZE_TYPE_ANALYZE_SCHEDULED_READ)
    run()
