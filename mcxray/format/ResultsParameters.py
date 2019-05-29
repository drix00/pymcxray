#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: mcxray.format.ResultsParameters

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

MCXRay ResultsParameters input file.
"""

###############################################################################
# Copyright 2019 Hendrix Demers
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
import copy

# Third party modules.

# Local modules.

# Project modules
from mcxray.format.text.version import read_from_file, write_line
from mcxray.format.version import CURRENT_VERSION, VERSION_1_4_3, VERSION_1_4_0

# Globals and constants variables.
KEY_COMPUTE_XRAY_CHARACTERISTIC = "ComputeXrayCharacteristic"
KEY_COMPUTE_XRAY_BREMSSTRAHLUNG = "ComputeXrayBremsstrahlung"
KEY_COMPUTE_XRAY_PHIRHOZ = "ComputeXrayPhirhoz"
KEY_COMPUTE_XRAY_SIMULATED_SPECTRUM = "ComputeXraySimulatedSpectrum"


def _create_keys():
    keys = [
        KEY_COMPUTE_XRAY_CHARACTERISTIC,
        KEY_COMPUTE_XRAY_BREMSSTRAHLUNG,
        KEY_COMPUTE_XRAY_PHIRHOZ,
        KEY_COMPUTE_XRAY_SIMULATED_SPECTRUM
    ]

    return keys


class ResultsParameters(object):
    def __init__(self, version=None):
        if version is None:
            self.version = copy.deepcopy(CURRENT_VERSION)
        else:
            self.version = version

        self._keys = _create_keys()

        self._parameters = {}

        self.default_values()

    def default_values(self):
        self.isComputeXrayCharacteristic = True
        self.isComputeXrayBremsstrahlung = True
        self.isComputeXrayPhirhoz = True
        self.isComputeXraySimulatedSpectrum = False

    def read(self, filepath):
        if self.version >= VERSION_1_4_0:
            read_from_file(self.version, filepath)

            lines = open(filepath, 'r').readlines()

            extractMethods = _create_extract_method()

            for line in lines:
                line = line.strip()

                for key in self._keys:
                    if line.startswith(key):
                        items = line.split('=')
                        self._parameters[key] = extractMethods[key](items[-1])
        else:
            self.default_values()

    def write(self, filepath):
        outputFile = open(filepath, 'w')

        _write_header(outputFile)

        write_line(self.version, outputFile)

        keys = _create_keys()
        if self.version < VERSION_1_4_3:
            keys.remove(KEY_COMPUTE_XRAY_SIMULATED_SPECTRUM)

        for key in keys:
            value = self._parameters[key]
            if value is not None:
                line = "%s=%i\n" % (key, int(value))
                outputFile.write(line)

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, version):
        self._version = version

    @property
    def isComputeXrayCharacteristic(self):
        return bool(self._parameters[KEY_COMPUTE_XRAY_CHARACTERISTIC])

    @isComputeXrayCharacteristic.setter
    def isComputeXrayCharacteristic(self, isComputeXrayCharacteristic):
        self._parameters[KEY_COMPUTE_XRAY_CHARACTERISTIC] = bool(isComputeXrayCharacteristic)

    @property
    def isComputeXrayBremsstrahlung(self):
        return bool(self._parameters[KEY_COMPUTE_XRAY_BREMSSTRAHLUNG])

    @isComputeXrayBremsstrahlung.setter
    def isComputeXrayBremsstrahlung(self, isComputeXrayBremsstrahlung):
        self._parameters[KEY_COMPUTE_XRAY_BREMSSTRAHLUNG] = bool(isComputeXrayBremsstrahlung)

    @property
    def isComputeXrayPhirhoz(self):
        return bool(self._parameters[KEY_COMPUTE_XRAY_PHIRHOZ])

    @isComputeXrayPhirhoz.setter
    def isComputeXrayPhirhoz(self, isComputeXrayPhirhoz):
        self._parameters[KEY_COMPUTE_XRAY_PHIRHOZ] = bool(isComputeXrayPhirhoz)

    @property
    def isComputeXraySimulatedSpectrum(self):
        return bool(self._parameters[KEY_COMPUTE_XRAY_SIMULATED_SPECTRUM])

    @isComputeXraySimulatedSpectrum.setter
    def isComputeXraySimulatedSpectrum(self, isComputeXraySimulatedSpectrum):
        self._parameters[KEY_COMPUTE_XRAY_SIMULATED_SPECTRUM] = bool(isComputeXraySimulatedSpectrum)


def _create_extract_method():
    extract_methods = {
        KEY_COMPUTE_XRAY_CHARACTERISTIC: _extract_bool,
        KEY_COMPUTE_XRAY_BREMSSTRAHLUNG: _extract_bool,
        KEY_COMPUTE_XRAY_PHIRHOZ: _extract_bool,
        KEY_COMPUTE_XRAY_SIMULATED_SPECTRUM: _extract_bool
    }

    return extract_methods


def _extract_bool(item_str):
    return bool(int(item_str))


def _write_header(output_file):
    headerLines = ["********************************************************************************",
                   "***                           Results Parameters",
                   "***",
                   "***",
                   "********************************************************************************"]

    for line in headerLines:
        output_file.write(line + '\n')

