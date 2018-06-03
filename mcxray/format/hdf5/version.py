#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: mcxray.format.hdf5.version
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

MCXray version information.
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

# Project modules
from mcxray.format.version import Version

# Globals and constants variables.


GROUP_VERSION = "version"

ATTRIBUTE_MAJOR = "major"
ATTRIBUTE_MINOR = "minor"
ATTRIBUTE_REVISION = "revision"


def read_from_file(group):
    version_group = group[GROUP_VERSION]

    version = Version(0, 0, 0)
    version.major = version_group.attrs[ATTRIBUTE_MAJOR]
    version.minor = version_group.attrs[ATTRIBUTE_MINOR]
    version.revision = version_group.attrs[ATTRIBUTE_REVISION]

    return version


def write_file(group, version):
    version_group = group.require_group(GROUP_VERSION)

    version_group.attrs[ATTRIBUTE_MAJOR] = version.major
    version_group.attrs[ATTRIBUTE_MINOR] = version.minor
    version_group.attrs[ATTRIBUTE_REVISION] = version.revision
