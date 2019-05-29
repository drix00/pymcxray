#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: mcxray.format.version

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
    """
    Version of MCXRay.
    """

    def __init__(self, major, minor, revision):
        """
        Create a version.

        :param major: version number
        :param minor: version number
        :param revision: version number
        """
        self.major = major
        self.minor = minor
        self.revision = revision

    def to_string(self):
        """
        Export the version to a string.

        :return: a string of the version.
        :see: :py:meth:`mcxray.format.version.Version.from_string`.
        """
        text = "%s.%s.%s" % (self.major, self.minor, self.revision)
        return text

    def from_string(self, version_string):
        """
        Read a version from a string.

        :param version_string:
        :return: version object.
        :see: :py:meth:`mcxray.format.version.Version.to_string`
        """
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
        """
        Major version number.

        :return: number
        """
        return self._major

    @major.setter
    def major(self, major):
        self._major = int(major)

    @property
    def minor(self):
        """
        Minor version number.

        :return: number
        """
        return self._minor

    @minor.setter
    def minor(self, minor):
        self._minor = int(minor)

    @property
    def revision(self):
        """
        Revision version number.

        :return: number
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        self._revision = int(revision)


def from_string(version_string):
    """
    Read a version from a string.

    :param version_string:
    :return: version object.
    :see: :py:meth:`mcxray.format.version.Version.to_string`
    """
    version = copy.deepcopy(CURRENT_VERSION)
    items = version_string.split('.')
    version.major = items[0]
    version.minor = items[1]
    version.revision = items[2]

    return version


#: Old version before implementation of ProgramVersion.
VERSION_1_1_1 = Version(1, 1, 1)

#: Version with implementation of ProgramVersion and corrected x-ray generation.
VERSION_1_2_0 = Version(1, 2, 0)

#: Correction of bug where the detector efficiency was not correctly applied to continuum x-ray spectrum.
VERSION_1_2_1 = Version(1, 2, 1)

#: Correction spelling of Casnati and add mode to compare all models in mcxray_console.
VERSION_1_2_2 = Version(1, 2, 2)

#: Add electron exit results with correction for beam tilt and rotation.
#: The correction is also applied to the electron trajectory results.
VERSION_1_2_3 = Version(1, 2, 3)

#: Correct bug with beam diameter. Now the beam diameter option is taken into account.
VERSION_1_2_4 = Version(1, 2, 4)

#: Add map and line scan simulation in MCXRayLite.
VERSION_1_2_5 = Version(1, 2, 5)

#: Correct bug in Browning Ratio calculation of scattering angle.
#: Change minimum and maximum values limit for microscope options.
#: Create the folder if results name in simulation options has a folder in it.
#: Add min/max x,y,z position in sample and relative to the beam.
VERSION_1_3_0 = Version(1, 3, 0)

#: Correct bug in the calculation of x-ray absorption in the sample.
#: Correct bug in Henke 1993 MAC implementation.
#: Refactor old ionization energy code.
#: Add Chantler 2005 ionization energy model.
#: Add results parameters file.
VERSION_1_4_0 = Version(1, 4, 0)

#: Add MAC Model option in file.
#: Add Chantler2005 MAC model option.
#: Add Bote 2009 ionization cross section.
#: Add CASINO energy loss: Bethe, Bethe relativistic, Joy & Luo & Gauvin, and Joy & Luo & Monsel.
VERSION_1_4_1 = Version(1, 4, 1)

#: Move the MAC Henke data file into the data folder.
VERSION_1_4_2 = Version(1, 4, 2)

#: Add result option to enable/disable simulated spectrum calculation.
VERSION_1_4_3 = Version(1, 4, 3)

#: Add simulation parameter option ElasticCrossSectionScalingFactor.
#: Add simulation parameter option EnergyLossScalingFactor.
VERSION_1_4_4 = Version(1, 4, 4)

#: Modify _Options.txt results file.
VERSION_1_4_5 = Version(1, 4, 5)

#: Correct spelling mistake in XRayMassAbsorptionCoefficientModel option key.
#: Upgrade boost library to version 1.54.
#: Use  Boost Random Number Library.
#: Change idum for each new simulation unless idum is -1.
#: Add RandomNumberGeneratorModel option
#: Add seed simulation option.
VERSION_1_4_6 = Version(1, 4, 6)

#: Update projects to visual studio 2013.
#: Correct warnings.
VERSION_1_5_0 = Version(1, 5, 0)

#: Lite version included EDS simulation.
#: Add console lite version.
VERSION_1_5_1 = Version(1, 5, 1)

#: Add x-ray results for XY, XZ, YZ distribution (similar to phirhoz distribution).
VERSION_1_5_2 = Version(1, 5, 2)

#: Export electron exit results in McXRayLite.
#: Correct bug with TE in the display.
#: Correct bug with saving input file with a folder other than the program folder.
#: Disable batch simulation from GUI interface.
#: Fixed issue #32: Acquisition time not saved in input file.
#: Fixed issue #30: Check writing float in option file.
#: Fixed issue #41: Bug in the linescan display when linescan Xend=0 or Yend=0.
#: Fixed issue #43: Change A unit to nm in MCXRay GUI.
#: Correct spelling of length in input files.
#: Rename variables.
#: Change graphic colors and point size.
VERSION_1_6_1 = Version(1, 6, 1)

#: Fixed issue #44: Cannot change TE detector angles in the GUI.
VERSION_1_6_2 = Version(1, 6, 2)

#: Add number of elastic collisions in electron exit results.
VERSION_1_6_3 = Version(1, 6, 3)

#: Add total electron path length in electron exit results.
VERSION_1_6_4 = Version(1, 6, 4)

#: Correct calculation of x-ray intensity for complex geometry.
VERSION_1_6_5 = Version(1, 6, 5)

#: Correct calculation of x-ray intensity for Ma1 lines of heavy elements.
VERSION_1_6_6 = Version(1, 6, 6)

#: Output the x-ray detector efficiency and x-ray detector parameters.
#: Remove the x-ray fudge factors.
#: Output the x-ray detector efficiency with the intensity of each line.
#: Remove atom spectra intensity results (wrong calculation).
#: Remove solid angle fudge factor.
VERSION_1_6_7 = Version(1, 6, 7)

#: Write files for x-ray spectrum in the Lite version.
VERSION_1_7_0 = Version(1, 7, 0)

#: Correct bug with energy loss scaling factor not set in the model.
VERSION_1_7_1 = Version(1, 7, 1)

#: Implement HDF5 file format for input and output.
VERSION_2_0_0 = Version(2, 0, 0)

#: In development version.
VERSION_2_1_0_DEV = Version(2, 1, 0)

#: Implement semi-sphere geometry (demi-sphere).
VERSION_2_1_0 = Version(2, 1, 0)

#: Height option in semi-sphere.
VERSION_2_1_1 = Version(2, 1, 1)

#: Refactor hdf5 structure.
VERSION_2_2_0 = Version(2, 2, 0)

#: Dummy version for file before version number was used in the project.
BEFORE_VERSION = copy.deepcopy(VERSION_1_1_1)

#: Current version of MCXRay.
CURRENT_VERSION = copy.deepcopy(VERSION_2_2_0)
