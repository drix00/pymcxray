#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: setup

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Setup script for the project pymcxray.
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
import os

# Third party modules.
from setuptools import setup, find_packages

# Local modules.
from pymcxray import __version__

# Globals and constants variables.
with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

packages = find_packages()

requirements = [
    'numpy',
    'matplotlib',
    'scipy',
    'h5py',
    'apscheduler',
    'Pillow',
]

test_requirements = [
    'nose', 'coverage'
]

setup(name="pymcxray",
      version=__version__,
      description="Python scripts for using mcxray software",
      long_description=readme + '\n\n' + history,
      author="Hendrix Demers",
      author_email="hendrix.demers@mail.mcgill.ca",
      url='https://github.com/drix00/pymcxray',
      packages=packages,
      package_dir={'pymcxray': 'pymcxray'},
      include_package_data=True,
      install_requires=requirements,
      license="Apache Software License 2.0",
      zip_safe=False,
      keywords='pymcxray',
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'Intended Audience :: Science/Research',
                   'Natural Language :: English',
                   'License :: OSI Approved :: Apache Software License',
                   'Programming Language :: Python',
                   'Operating System :: OS Independent',
                   'Topic :: Scientific/Engineering',
                   'Topic :: Scientific/Engineering :: Physics'],

      setup_requires=test_requirements,

      test_suite='nose.collector',
      tests_require=test_requirements
)

