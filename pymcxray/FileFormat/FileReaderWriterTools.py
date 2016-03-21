#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.FileReaderWriterTools
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

description
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2012 Hendrix Demers"
__license__ = ""

# Standard library modules.

# Third party modules.

# Local modules.

# Project modules

# Globals and constants variables.

def reduceAfterDot(value):
    valueStr = str(value)
    indexDot = valueStr.find('.')
    if indexDot != -1:
        while len(valueStr) > indexDot:
            if valueStr[-1] == '0':
                valueStr = valueStr[:-1]
            else:
                break

    if valueStr[-1] == '.':
        valueStr = valueStr[:-1]

    return valueStr
