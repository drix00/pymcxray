#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: format.version
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
import copy

# Third party modules.

# Local modules.

# Project modules

# Globals and constants variables.


class Version(object):
    def __init__(self, major, minor, revision):
        self.major = major
        self.minor = minor
        self.revision = revision

    def to_string(self):
        text = "%s.%s.%s" % (self.major, self.minor, self.revision)
        return text

    def from_string(self, version_string):
        items = version_string.split('.')
        self.major = items[0]
        self.minor = items[1]
        self.revision = items[2]

    def __eq__(self, other):
        if self.major == other.major and self.minor == other.minor and self.revision == other.revision:
            return True
        else:
            return False

    def __lt__(self, other):
        if self == other:
            return False

        if self.major < other.major:
            return True
        elif self.major > other.major:
            return False

        if self.minor < other.minor:
            return True
        elif self.minor > other.minor:
            return False

        if self.revision < other.revision:
            return True
        elif self.revision > other.revision:
            return False

    def __ge__(self, other):
        if self == other:
            return True
        if self < other:
            return False
        else:
            return True

    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, major):
        self._major = int(major)

    @property
    def minor(self):
        return self._minor

    @minor.setter
    def minor(self, minor):
        self._minor = int(minor)

    @property
    def revision(self):
        return self._revision

    @revision.setter
    def revision(self, revision):
        self._revision = int(revision)


VERSION_1_1_1 = Version(1, 1, 1)

VERSION_1_2_0 = Version(1, 2, 0)

VERSION_1_2_1 = Version(1, 2, 1)

VERSION_1_2_2 = Version(1, 2, 2)

VERSION_1_2_3 = Version(1, 2, 3)

VERSION_1_2_4 = Version(1, 2, 4)

VERSION_1_2_5 = Version(1, 2, 5)

VERSION_1_3_0 = Version(1, 3, 0)

VERSION_1_4_0 = Version(1, 4, 0)

VERSION_1_4_1 = Version(1, 4, 1)

VERSION_1_4_2 = Version(1, 4, 2)

VERSION_1_4_3 = Version(1, 4, 3)

VERSION_1_4_4 = Version(1, 4, 4)

VERSION_1_4_5 = Version(1, 4, 5)

VERSION_1_4_6 = Version(1, 4, 6)

VERSION_1_5_0 = Version(1, 5, 0)

VERSION_1_5_1 = Version(1, 5, 1)

VERSION_1_5_2 = Version(1, 5, 2)

BEFORE_VERSION = copy.deepcopy(VERSION_1_1_1)
CURRENT_VERSION = copy.deepcopy(VERSION_1_5_2)
