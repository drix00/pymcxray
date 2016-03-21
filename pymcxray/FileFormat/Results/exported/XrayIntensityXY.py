#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.exported.XrayIntensityXY
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Read x-ray intensity distribution in XY exported from mcxray GUI.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2014 Hendrix Demers"
__license__ = ""

# Standard library modules.

# Third party modules.

# Local modules.

# Project modules

# Globals and constants variables.

class XrayIntensityXY(object):
    def __init__(self):
        pass

    def readData(self, filepath):
        self_filepath = filepath
