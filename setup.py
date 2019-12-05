#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: setup

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Setup script for the project mcxray.
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
import os.path
import io
import sys

# Third party modules.
from setuptools import setup, find_packages
from setuptools import setup, find_namespace_packages
from setuptools.command.test import test as TestCommand

# Local modules.
from mcxray import __author__, __email__, __version__, __copyright__, __project_name__

# Globals and constants variables.
here = os.path.abspath(os.path.dirname(__file__))

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read()

with open('requirements_test.txt') as requirements_file:
    test_requirements = requirements_file.read()


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


setup(
    name=__project_name__,
    version=__version__,
    author=__author__,
    author_email=__email__,
    maintainer=__author__,
    maintainer_email=__email__,
    description="Python scripts for using mcxray software",
    long_description=readme + '\n\n' + history,
    keywords='mcxray',
    url='https://github.com/drix00/pymcxray',
    project_urls={
        "Bug Tracker": "https://github.com/pytrim/pytrim/issues",
        "Documentation": "https://pytrim.readthedocs.io/",
        "Source Code": "https://github.com/pytrim/pytrim",
    },

    packages=find_packages(),
    package_dir={'mcxray': 'mcxray'},
    platforms='any',
    zip_safe=False,
    cmdclass={'test': PyTest},
    include_package_data=True,

    install_requires=requirements,
    setup_requires=test_requirements,
    tests_require=test_requirements,

    license="Apache Software License 2.0",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Physics'
    ],
)
