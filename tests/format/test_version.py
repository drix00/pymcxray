#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.format.test_version

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for module :py:mod:`mcxray.format.version`.
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
import pytest

# Local modules.

# Project modules
from mcxray.format.version import *

# Globals and constants variables.


@pytest.fixture()
def version_123_string():
    version = Version(1, 2, 3)
    string = "1.2.3"

    return version, string, (1, 2, 3)


@pytest.fixture()
def version_456_string():
    version = Version(4, 5, 6)
    string = "4.5.6"

    return version, string, (4, 5, 6)


@pytest.fixture()
def current_version_string():
    version = copy.deepcopy(VERSION_2_2_0)
    string = "2.2.0"

    return version, string, (2, 2, 0)


def test_module_is_working():
    # assert False, "Verify if the test module is working."
    assert True


def test_to_string(version_123_string):
    """
    Test for method `to_string`.
    """
    version, version_string_ref, (major, minor, revision) = version_123_string
    version_string = version.to_string()

    assert version_string_ref == version_string
    assert major == version.major
    assert minor == version.minor
    assert revision == version.revision


def test_from_string(version_456_string):
    """
    Test for method `from_string`.
    """
    version_ref, version_string_ref, (major, minor, revision) = version_456_string

    version = copy.deepcopy(CURRENT_VERSION)
    version.from_string(version_string_ref)
    version_string = version.to_string()

    assert version_string_ref == version_string

    assert major == version.major
    assert minor == version.minor
    assert revision == version.revision


def test_from_string_function(version_123_string):
    """
    Test for method `from_string`.
    """
    version_ref, version_string, (major, minor, revision) = version_123_string

    version_ref = Version(1, 2, 3)
    version = from_string(version_string)

    assert version_ref == version
    assert major == version.major
    assert minor == version.minor
    assert revision == version.revision


versions_to_try = (("1.1.1", VERSION_1_1_1, (1, 1, 1)),
                   ("1.1.1", BEFORE_VERSION, (1, 1, 1)),
                   ("1.2.0", VERSION_1_2_0, (1, 2, 0)),
                   ("1.2.1", VERSION_1_2_1, (1, 2, 1)),
                   ("1.2.3", VERSION_1_2_3, (1, 2, 3)),
                   ("1.2.4", VERSION_1_2_4, (1, 2, 4)),
                   ("1.2.5", VERSION_1_2_5, (1, 2, 5)),
                   ("1.3.0", VERSION_1_3_0, (1, 3, 0)),
                   ("1.4.0", VERSION_1_4_0, (1, 4, 0)),
                   ("1.4.1", VERSION_1_4_1, (1, 4, 1)),
                   ("1.4.2", VERSION_1_4_2, (1, 4, 2)),
                   ("2.1.1", VERSION_2_1_1, (2, 1, 1)),
                   ("2.2.0", VERSION_2_2_0, (2, 2, 0)),
                   )


@pytest.fixture(params=versions_to_try)
def version_constant(request):
    return request.param


def test_version_constants(version_constant):
    """
    Tests for version constants.
    """
    string_ref, version, (major, minor, revision) = version_constant
    version_string = version.to_string()
    assert string_ref == version_string
    assert major == version.major
    assert minor == version.minor
    assert revision == version.revision


def test_before_version():
    assert VERSION_1_1_1 == BEFORE_VERSION
    assert VERSION_1_1_1 != CURRENT_VERSION


def test_current_version(current_version_string):
    current_version_ref, current_string_ref, (major, minor, revision) = current_version_string
    assert current_version_ref == CURRENT_VERSION

    version_string = CURRENT_VERSION.to_string()
    assert current_string_ref == version_string
    assert major == CURRENT_VERSION.major
    assert minor == CURRENT_VERSION.minor
    assert revision == CURRENT_VERSION.revision

    assert current_version_ref == CURRENT_VERSION
    assert current_version_ref != BEFORE_VERSION


def test_comparison():
    """
    Test comparison operation on `Version` class.
    """
    assert VERSION_1_2_0 == VERSION_1_2_0
    assert VERSION_1_2_0 != VERSION_1_1_1
    assert VERSION_1_2_0 != VERSION_1_2_1

    assert VERSION_1_2_0 == VERSION_1_2_0
    assert VERSION_1_2_0 != VERSION_1_1_1
    assert VERSION_1_2_0 != VERSION_1_2_1

    assert VERSION_1_2_0 > VERSION_1_1_1
    assert VERSION_1_2_0 < VERSION_1_2_1
    assert VERSION_1_1_1 < VERSION_1_2_0
    assert VERSION_1_2_1 > VERSION_1_2_0

    assert VERSION_1_2_0 >= VERSION_1_1_1
    assert VERSION_1_2_0 <= VERSION_1_2_1
    assert VERSION_1_1_1 <= VERSION_1_2_0
    assert VERSION_1_2_1 >= VERSION_1_2_0
