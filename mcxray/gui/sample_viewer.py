#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: sample_viewer
   :synopsis: Script to view the mcxray sample in 3D.

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Script to view the mcxray sample in 3D.
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
import logging
from itertools import cycle

# Third party modules.
import vtk

# Local modules.

# Project modules.
from mcxray.format.SimulationInputs import SimulationInputs
from mcxray.format.Specimen import Specimen
from mcxray.format.RegionType import REGION_TYPE_BOX

# Globals and constants variables.
_colors = [(1.0, 0.0, 0.0), (1.0, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.5, 0.0), (0.0, 1.0, 1.0), (0.0, 0.0, 1.0), (1.0, 0.0, 1.0)]
colors = cycle(_colors)

class SampleViewer():
    def __init__(self):
        self.maximum_size_nm = 1.0

        self._create_render()
        self._create_render_window()
        self._create_interface_render()
        self._create_axes()

    def _create_interface_render(self):
        # create a renderwindowinteractor
        self.interface_render = vtk.vtkRenderWindowInteractor()
        self.interface_render.SetRenderWindow(self.render_window)

    def _create_render_window(self):
        self.render_window = vtk.vtkRenderWindow()
        self.render_window.AddRenderer(self.renderer)

    def _create_render(self):
        # create a rendering window and renderer
        self.renderer = vtk.vtkRenderer()
        self.renderer.SetBackground(0.1, .2, .3)

    def _create_axes(self):
        self.axes = vtk.vtkAxesActor()

        self._rescale_axes()
        # properties of the axes labels can be set as follows
        # this sets the x axis label to red
        # axes->GetXAxisCaptionActor2D()->GetCaptionTextProperty()->SetColor(1,0,0);
        # the actual text of the axis label can be changed:
        # axes->SetXAxisLabelText("test");
        self.renderer.AddActor(self.axes)

    def _rescale_axes(self):
        transform = vtk.vtkTransform()
        transform.Translate(self.maximum_size_nm, 0.0, 0.0)
        transform.Scale(self.maximum_size_nm/2.0, self.maximum_size_nm/2.0, self.maximum_size_nm/2.0)
        #  The axes are positioned with a user transform
        self.axes.SetUserTransform(transform)

    def open(self, file_path):
        logging.debug(file_path)
        simulation_inputs = SimulationInputs()
        simulation_inputs.read(file_path)

        base_path = os.path.dirname(file_path)
        logging.debug(base_path)
        specimen_file_path = os.path.join(base_path, simulation_inputs.specimenFilename)
        logging.debug(specimen_file_path)
        specimen = Specimen()
        specimen.read(specimen_file_path)

        for region in specimen.regions:
            logging.debug(region.numberElements)
            logging.debug(region.regionType)
            logging.debug(region.regionDimensions)

            if region.numberElements > 0:
                if region.regionType is REGION_TYPE_BOX:
                    self._add_box(region)

    def _add_box(self, region):
        # create cube
        cube = vtk.vtkCubeSource()
        dimensions = region.regionDimensions
        #cube.SetCenter(0.0, 0.0, 0.0)
        cube.SetBounds(dimensions.minimumX/10.0, dimensions.maximumX/10.0, dimensions.minimumY/10.0, dimensions.maximumY/10.0, dimensions.minimumZ/10.0, dimensions.maximumZ/10.0)
        self.maximum_size_nm = max(self.maximum_size_nm, dimensions.minimumX/10.0, dimensions.maximumX/10.0, dimensions.minimumY/10.0, dimensions.maximumY/10.0, dimensions.minimumZ/10.0, dimensions.maximumZ/10.0)

        # mapper
        cubeMapper = vtk.vtkPolyDataMapper()
        # cubeMapper.SetInputData(cube.GetOutput())
        cubeMapper.SetInputConnection(cube.GetOutputPort())

        # actor
        cubeActor = vtk.vtkActor()
        cubeActor.SetMapper(cubeMapper)
        cubeActor.GetProperty().SetColor(next(colors))
        cubeActor.GetProperty().SetOpacity(0.2)
        cubeActor.GetProperty().SetEdgeVisibility(True)

        self.renderer.AddActor(cubeActor)

        self._rescale_axes()

    def show(self):
        self.renderer.ResetCamera()
        self.render_window.Render()

        self.renderer.ResetCamera(-200, 200, -200, 200, -200, 200)
        self.render_window.Render()

        # enable user interface interactor
        self.interface_render.Initialize()
        self.render_window.Render()
        self.interface_render.Start()


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)

    file_path = r"D:\work\Dropbox\hdemers\professional\projects\MCXRay\maps\map_test_30kV.sim"

    viewer = SampleViewer()
    viewer.open(file_path)
    viewer.show()
