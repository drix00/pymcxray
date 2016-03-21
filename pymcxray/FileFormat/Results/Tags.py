#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.Tags
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

MCXRay tags used in output files.
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

# Globals and constants variables.
class TagNotFoundError(ValueError): pass

def findTag(tag, lines):
    for index, line in enumerate(lines):
        line = line.strip()
        if line.startswith(tag):
            return index

    message = "Tag %s not found in the lines" % (tag)
    raise TagNotFoundError(message)

def findAllTag(tag, lines, contains=None):
    indexList = []
    for index, line in enumerate(lines):
        line = line.strip()
        if line.startswith(tag):
            if contains is not None:
                if contains in line:
                    indexList.append(index)
            else:
                indexList.append(index)

    return indexList
