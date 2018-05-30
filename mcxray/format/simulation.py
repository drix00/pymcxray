#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: mcxray.simulation

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Simulation data structure for mcxray Monte Carlo simulation program.
"""

###############################################################################
# Copyright 2018 Hendrix Demers
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

# Third party modules.

# Local modules.

# Project modules.
from mcxray.format.version import CURRENT_VERSION

# Globals and constants variables.


class Simulation(object):
    def __init__(self):
        """
        Constructor.
        """
        self.name = ""
        self.version = CURRENT_VERSION

    def __eq__(self, other):
        """
        Comparison between two objects.

        :param other:
        :return: if two objects are equal.
        """
        is_equal = self.name == other.name and \
                   self.version == other.version

        return is_equal
