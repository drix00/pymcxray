#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: FileFormat.Results.ElectronTrajectoriesResults

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Read MCXray electron trajectories results file.
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
import os.path
import csv
import logging
import math

# Third party modules.
import matplotlib.pyplot as plt
import numpy as np

# Local modules.
from pymcxray import get_current_module_path

# Project modules

# Globals and constants variables.
COLOR_TRAJECTORY_TYPE = "colorTrajectoryType"
COLOR_REGION = "colorRegion"
COLOR_ENERGY = "colorEnergy"

COLLISION_TYPE_UNKNOWN = 0
COLLISION_TYPE_ELECTRON_GUN = 1
COLLISION_TYPE_REGION = 2
COLLISION_TYPE_OUT = 3
COLLISION_TYPE_EMPTY_REGION = 4
COLLISION_TYPE_ELASTIC = 5

HDF5_ELECTRON_TRAJECTORIES_RESULTS = "ElectronTrajectoriesResults"
HDF5_ELECTRON_TRAJECTORIES = "ElectronTrajectories"
HDF5_ELECTRON_TRAJECTORIES_TRAJECTORY_TYPE = 0
HDF5_ELECTRON_TRAJECTORIES_X_A = 1
HDF5_ELECTRON_TRAJECTORIES_Y_A = 2
HDF5_ELECTRON_TRAJECTORIES_Z_A = 3
HDF5_ELECTRON_TRAJECTORIES_CORRECTED_X_A = 4
HDF5_ELECTRON_TRAJECTORIES_CORRECTED_Y_A = 5
HDF5_ELECTRON_TRAJECTORIES_CORRECTED_Z_A = 6
HDF5_ELECTRON_TRAJECTORIES_ENERGY_keV = 7
HDF5_ELECTRON_TRAJECTORIES_INDEX_REGION = 8
HDF5_ELECTRON_TRAJECTORIES_COLLISION_TYPE = 9


class Collision(object):

    @property
    def x_A(self):
        return self._x_A
    @x_A.setter
    def x_A(self, x_A):
        self._x_A = x_A

    @property
    def y_A(self):
        return self._y_A
    @y_A.setter
    def y_A(self, y_A):
        self._y_A = y_A

    @property
    def z_A(self):
        return self._z_A
    @z_A.setter
    def z_A(self, z_A):
        self._z_A = z_A

    @property
    def correctedX_A(self):
        return self._correctedX_A
    @correctedX_A.setter
    def correctedX_A(self, correctedX_A):
        self._correctedX_A = correctedX_A

    @property
    def correctedY_A(self):
        return self._correctedY_A
    @correctedY_A.setter
    def correctedY_A(self, correctedY_A):
        self._correctedY_A = correctedY_A

    @property
    def correctedZ_A(self):
        return self._correctedZ_A
    @correctedZ_A.setter
    def correctedZ_A(self, correctedZ_A):
        self._correctedZ_A = correctedZ_A

    @property
    def energy_keV(self):
        return self._energy_keV
    @energy_keV.setter
    def energy_keV(self, energy_keV):
        self._energy_keV = energy_keV

    @property
    def indexRegion(self):
        return self._indexRegion
    @indexRegion.setter
    def indexRegion(self, indexRegion):
        self._indexRegion = indexRegion

    @property
    def collisionType(self):
        return self._collisionType
    @collisionType.setter
    def collisionType(self, collisionType):
        self._collisionType = collisionType


class Trajectory(object):
    def __init__(self):
        self._collisions = []

    def addCollision(self, collision):
        self._collisions.append(collision)

    @property
    def index(self):
        return self._index
    @index.setter
    def index(self, index):
        self._index = index

    @property
    def trajectoryType(self):
        return self._trajectoryType
    @trajectoryType.setter
    def trajectoryType(self, trajectoryType):
        self._trajectoryType = trajectoryType

    @property
    def collisions(self):
        return self._collisions
    @collisions.setter
    def collisions(self, collisions):
        self._collisions = collisions


class ElectronTrajectoriesResults(object):
    def __init__(self, filepath):
        self.number_trajectories = 0
        self.maximum_number_collisions = 0

        self.read(filepath)

    def read(self, filepath):
        reader = csv.reader(open(filepath, 'r'))

        #Skip header line
        next(reader)

        self._trajectories = []
        currentTrajectoryIndex = -1
        trajectory = None
        for row in reader:
            trajectoryIndex = int(row[0])
            trajectoryType = int(row[1])

            if trajectoryIndex != currentTrajectoryIndex:
                if trajectory != None:
                    self._trajectories.append(trajectory)
                    self.number_trajectories += 1
                    self.maximum_number_collisions = max(self.maximum_number_collisions, number_collisions)

                trajectory = Trajectory()
                trajectory.index = trajectoryIndex
                trajectory.trajectoryType = trajectoryType
                currentTrajectoryIndex = trajectoryIndex
                number_collisions = 0
            if len(row) == 8:
                collision = Collision()
                collision.x_A = float(row[2])
                collision.y_A = float(row[3])
                collision.z_A = float(row[4])

                collision.energy_keV = float(row[5])
                collision.indexRegion = int(row[6])
                collision.collisionType = int(row[7])
            elif len(row) == 11:
                collision = Collision()
                collision.x_A = float(row[2])
                collision.y_A = float(row[3])
                collision.z_A = float(row[4])
                collision.correctedX_A = float(row[5])
                collision.correctedY_A = float(row[6])
                collision.correctedZ_A = float(row[7])
                collision.energy_keV = float(row[8])
                collision.indexRegion = int(row[9])
                collision.collisionType = int(row[10])

            trajectory.addCollision(collision)
            number_collisions += 1

        logging.info("Number trajectories: %i", len(self._trajectories))

    def write_hdf5(self, hdf5_group):
        hdf5_group = hdf5_group.require_group(HDF5_ELECTRON_TRAJECTORIES_RESULTS)

        shape = (10, self.number_trajectories, self.maximum_number_collisions)
        electron_trajectories_data = np.zeros(shape, dtype=float)

        for trajectory_id, trajectory in enumerate(self._trajectories):
            for collision_id, collision in enumerate(trajectory.collisions):
                electron_trajectories_data[HDF5_ELECTRON_TRAJECTORIES_TRAJECTORY_TYPE, trajectory_id, collision_id] = trajectory.trajectoryType
                electron_trajectories_data[HDF5_ELECTRON_TRAJECTORIES_X_A, trajectory_id, collision_id] = collision.x_A
                electron_trajectories_data[HDF5_ELECTRON_TRAJECTORIES_Y_A, trajectory_id, collision_id] = collision.y_A
                electron_trajectories_data[HDF5_ELECTRON_TRAJECTORIES_Z_A, trajectory_id, collision_id] = collision.z_A
                electron_trajectories_data[HDF5_ELECTRON_TRAJECTORIES_CORRECTED_X_A, trajectory_id, collision_id] = collision.correctedX_A
                electron_trajectories_data[HDF5_ELECTRON_TRAJECTORIES_CORRECTED_Y_A, trajectory_id, collision_id] = collision.correctedY_A
                electron_trajectories_data[HDF5_ELECTRON_TRAJECTORIES_CORRECTED_Z_A, trajectory_id, collision_id] = collision.correctedZ_A
                electron_trajectories_data[HDF5_ELECTRON_TRAJECTORIES_ENERGY_keV, trajectory_id, collision_id] = collision.energy_keV
                electron_trajectories_data[HDF5_ELECTRON_TRAJECTORIES_INDEX_REGION, trajectory_id, collision_id] = collision.indexRegion
                electron_trajectories_data[HDF5_ELECTRON_TRAJECTORIES_COLLISION_TYPE, trajectory_id, collision_id] = collision.collisionType

        hdf5_group.create_dataset(HDF5_ELECTRON_TRAJECTORIES, data=electron_trajectories_data)

    def getElectronGunPositions_nm(self):
        positions_nm = []

        for trajectory in self._trajectories:
            for collision in trajectory.collisions:
                if collision.collisionType == COLLISION_TYPE_ELECTRON_GUN:
                    position_nm = (collision.x_A*0.1, collision.y_A*0.1, collision.z_A*0.1)
                    positions_nm.append(position_nm)

        assert len(positions_nm) == len(self._trajectories)

        return positions_nm

    def drawXZ(self, title="", corrected=False, theta_deg=0.0, colorType=COLOR_TRAJECTORY_TYPE, trajectoryIndexes=None,
               x_limit=None, y_limit=None):
        theta_rad = math.radians(theta_deg)
        sinTheta = math.sin(theta_rad)
        cosTheta = math.cos(theta_rad)

        plt.figure()
        plt.title(title)

        indexUniqueRegionsAllTrajectories = set()
        if trajectoryIndexes is None:
            trajectoryIndexes = range(1, len(self._trajectories)+1)

        for trajectoryIndex in trajectoryIndexes:
            trajectory = self._trajectories[trajectoryIndex-1]
            if colorType == COLOR_TRAJECTORY_TYPE:
                color = self._getColor(trajectory.trajectoryType)

                x = []
                z = []
                for collision in trajectory.collisions:
                    if corrected:
                        x.append(collision.correctedX_A/10.0)
                        z.append(collision.correctedZ_A/10.0)
                    else:
                        xx = collision.x_A/10.0
                        zz = collision.z_A/10.0
                        x.append(cosTheta*xx + sinTheta*zz)
                        z.append(-sinTheta*xx + cosTheta*zz)

                plt.plot(x, z, '-', color=color)
            elif colorType == COLOR_REGION:
                color = self._getColor(trajectory.trajectoryType)

                x = []
                z = []
                indexRegions = []
                indexUniqueRegions = set()
                for collision in trajectory.collisions:
                    indexRegions.append(collision.indexRegion)
                    indexUniqueRegions.add(collision.indexRegion)
                    indexUniqueRegionsAllTrajectories.add(collision.indexRegion)

                    if corrected:
                        x.append(collision.correctedX_A/10.0)
                        z.append(collision.correctedZ_A/10.0)
                    else:
                        xx = collision.x_A/10.0
                        zz = collision.z_A/10.0
                        x.append(cosTheta*xx + sinTheta*zz)
                        z.append(-sinTheta*xx + cosTheta*zz)

                x = np.array(x)
                z = np.array(z)
                indexRegions = np.array(indexRegions)
                for indexRegion in sorted(indexUniqueRegions):
                    zz = np.ma.masked_where(indexRegions != indexRegion, z)
                    color = self._getColorRegion(indexRegion)
                    plt.plot(x, zz, '.', color=color)

                plt.plot(x, z, '-', color="gray")

        plt.xlabel('X (nm)')
        plt.ylabel('Z (nm)')
        if x_limit is not None:
            plt.xlim(x_limit)
        if y_limit is not None:
            plt.ylim(y_limit)
        plt.grid(True)
        plt.gca().set_aspect('equal', 'datalim')
        plt.gca().invert_yaxis()

        print(sorted(indexUniqueRegionsAllTrajectories))

    def drawXY(self, title="", corrected=False, x_limit=None, y_limit=None):
        plt.figure()
        plt.title(title)

        for trajectory in self._trajectories:
            color = self._getColor(trajectory.trajectoryType)

            x = []
            y = []
            for collision in trajectory.collisions:
                if corrected:
                    x.append(collision.correctedX_A/10.0)
                    y.append(collision.correctedY_A/10.0)
                else:
                    x.append(collision.x_A/10.0)
                    y.append(collision.y_A/10.0)

            plt.plot(x, y, '-', color=color)

        plt.xlabel('X (nm)')
        plt.ylabel('Y (nm)')
        if x_limit is not None:
            plt.xlim(x_limit)
        if y_limit is not None:
            plt.ylim(y_limit)
        plt.gca().set_aspect('equal', 'datalim')
        plt.grid(True)

    def drawYZ(self, title="", corrected=False, x_limit=None, y_limit=None):
        plt.figure()
        plt.title(title)

        for trajectory in self._trajectories:
            color = self._getColor(trajectory.trajectoryType)

            y = []
            z = []
            for collision in trajectory.collisions:
                if corrected:
                    y.append(collision.correctedY_A/10.0)
                    z.append(collision.correctedZ_A/10.0)
                else:
                    y.append(collision.y_A/10.0)
                    z.append(collision.z_A/10.0)

            plt.plot(y, z, '-', color=color)

        plt.xlabel('Y (nm)')
        plt.ylabel('Z (nm)')
        if x_limit is not None:
            plt.xlim(x_limit)
        if y_limit is not None:
            plt.ylim(y_limit)

        plt.grid(True)
        plt.gca().set_aspect('equal', 'datalim')
        plt.gca().invert_yaxis()

    def _getColor(self, trajectoryType):
        if trajectoryType == 1:
            color = 'b'
        elif trajectoryType == 2:
            color = 'r'
        elif trajectoryType == 3:
            color = 'b'
        elif trajectoryType == 4:
            color = 'm'

        return color

    def _getColorRegion(self, indexRegion):
        colors = ["blue", "green", "red", "black", "magenta", "yellow", "cyan"]
        if indexRegion < len(colors):
            color = colors[indexRegion]
        else:
            color = colors[indexRegion-len(colors)]
        return color

def run():
    path = get_current_module_path(__file__, "../../../test_data/version1.2")
    filepath = os.path.join(path, "SimulationsComplexPhiRhoZ_Cr_T5nm_Z0nm_Al_E10d0keV_ElectronTrajectoriesResults.csv")
    #filepath = os.path.join(path, "SimulationsComplexPhiRhoZ_Cr100T50A_IsolatedLayer_E10d0keV_ElectronTrajectoriesResults.csv")

    electronTrajectoriesResults = ElectronTrajectoriesResults(filepath)

    electronTrajectoriesResults.drawXZ()
    electronTrajectoriesResults.drawXY()
    electronTrajectoriesResults.drawYZ()

    plt.show()

def runFogging():
    path = r"K:\hdemers\results\simulations\MCXRay\foggingElectron"
    filepath = os.path.join(path, "McXRay_ElectronTrajectoriesResults.csv")

    electronTrajectoriesResults = ElectronTrajectoriesResults(filepath)

    electronTrajectoriesResults.drawXZ()
    electronTrajectoriesResults.drawXY()
    electronTrajectoriesResults.drawYZ()

    plt.show()

def runAuCThinFilm():
    path = r"D:\work\results\simulations\MCXRay\SimulationAuCThinFilm\MCXRay_v1_4_6\simulations\Results"
    filepath = os.path.join(path, "SimulationAuCThinFilm_Au_d100A_C_E5d0keV_N1000000e_PX1000d0PY0d0nm_ElectronTrajectoriesResults.csv")

    electronTrajectoriesResults = ElectronTrajectoriesResults(filepath)

    electronTrajectoriesResults.drawXZ()
    #electronTrajectoriesResults.drawXY()
    #electronTrajectoriesResults.drawYZ()

    filepath = os.path.join(path, "SimulationAuCThinFilm_Au_d100A_C_E5d0keV_N1000000e_PX0d0PY0d0nm_ElectronTrajectoriesResults.csv")

    electronTrajectoriesResults = ElectronTrajectoriesResults(filepath)

    electronTrajectoriesResults.drawXZ()
    #electronTrajectoriesResults.drawXY()
    #electronTrajectoriesResults.drawYZ()

    plt.show()

if __name__ == '__main__': #pragma: no cover
    runAuCThinFilm()
