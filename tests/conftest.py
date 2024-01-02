#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.conftest
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

A Pytest local plugin for testing the project.
"""

###############################################################################
# Copyright 2024 Hendrix Demers
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
from pathlib import Path

# Third party modules.
import pytest

# Local modules.

# Project modules.
from mcxray import get_current_module_path

# Globals and constants variables.


# pytest options.
def pytest_addoption(parser):
    parser.addoption(
        "--runslow", action="store_true", default=False, help="run slow tests"
    )


def pytest_configure(config):
    config.addinivalue_line("markers", "slow: mark test as slow to run")


def pytest_collection_modifyitems(config, items):  # pragma no cover
    if not config.getoption("--runslow"):
        skip_slow = pytest.mark.skip(reason="need --runslow option to run")
        for item in items:
            if "slow" in item.keywords:
                item.add_marker(skip_slow)


# Test files.
@pytest.fixture
def panorama_file():
    path = get_current_module_path(__file__, r"../test_data\lyra\panorama")
    file_path = path / Path(r"Da2020-42fresh1\panorama.png")
    return file_path


# Test data.
@pytest.fixture
def panorama_scalebar_data(panorama_file):
    scalebar = ScaleBar(panorama_file)

    return scalebar
