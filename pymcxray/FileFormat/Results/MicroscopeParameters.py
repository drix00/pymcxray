#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.Microscope
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

MCXRay microscope parameter in results file.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2012 Hendrix Demers"
__license__ = ""

# Subversion informations for the file.
__svnRevision__ = "$Revision$"
__svnDate__ = "$Date$"
__svnId__ = "$Id$"

# Standard library modules.

# Third party modules.

# Local modules.

# Project modules
import pymcxray.FileFormat.Results.BeamParameters as BeamParameters
import pymcxray.FileFormat.Results.DetectorParameters as DetectorParameters

# Globals and constants variables.
KEY_MICROSCOPE_PARAMETERS = "MicroscopeParameters"

class MicroscopeParameters(object):
    def __init__(self):
        self._parameters = {}

    def readFromLines(self, lines):
        indexLine = 0

        self.beamParameters = BeamParameters.BeamParameters()
        indexLine += self.beamParameters.readFromLines(lines[indexLine:])

        # Skip empty line.
        indexLine += 1

        self.detectorParameters = DetectorParameters.DetectorParameters()
        indexLine += self.detectorParameters.readFromLines(lines[indexLine:])

        return indexLine

    @property
    def beamParameters(self):
        return self._parameters[BeamParameters.KEY_BEAM_PARAMETERS]
    @beamParameters.setter
    def beamParameters(self, beamParameters):
        self._parameters[BeamParameters.KEY_BEAM_PARAMETERS] = beamParameters

    @property
    def detectorParameters(self):
        return self._parameters[DetectorParameters.KEY_DETECTOR_PARAMETERS]
    @detectorParameters.setter
    def detectorParameters(self, detectorParameters):
        self._parameters[DetectorParameters.KEY_DETECTOR_PARAMETERS] = detectorParameters
