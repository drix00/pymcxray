#!/usr/bin/env python

# Standard library modules.
import os

# Third party modules.
from setuptools import setup, find_packages

# Local modules.

# Globals and constants variables.
with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'numpy',
                        'matplotlib',
                        'scipy',
                        'Pillow', # Fork of PIL (Python 3 compatible)
                        'apscheduler'
]

test_requirements = [
    'nose', 'coverage'
]

setup(name="pymcxray",
    version='0.1.2',
    description="Python scripts for using mcxray software",
    long_description=readme + '\n\n' + history,
    author="Hendrix Demers",
    author_email="hendrix.demers@mail.mcgill.ca",
    url='https://github.com/drix00/pymcxray',
    packages=[
        'pymcxray',
    ],
    package_dir={'pymcxray':
                 'pymcxray'},
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

