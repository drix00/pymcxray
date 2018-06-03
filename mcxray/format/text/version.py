#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: format.text.version
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
import os.path

# Third party modules.

# Local modules.

# Project modules
from mcxray.format.version import from_string

# Globals and constants variables.


key = "Version"


def write_line(version, output_file):
    line = "%s=%s\n" % (key, version.to_string())
    output_file.write(line)


def read_from_file(version, file_path):
    lines = open(file_path, 'r').readlines()

    for line in lines:
        line = line.strip()

        if line.startswith(key):
            items = line.split('=')
            version.from_string((items[-1]))
            return
    else:
        version.major = 1
        version.minor = 1
        version.revision = 1


def read_from_output_file(path, basename):
    file_name = "{}_ProgramVersion.dat".format(basename)
    file_path = os.path.join(path, file_name)

    with open(file_path) as version_file:
        version_line = version_file.readline()

        version_string = version_line.split('=')[-1]
        version = from_string(version_string)
        return version
