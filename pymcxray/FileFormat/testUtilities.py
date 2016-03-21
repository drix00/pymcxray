#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.testUtilities
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Utilities used for testing this package.
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
import os.path
import shutil

# Third party modules.

# Local modules.

# Project modules

# Globals and constants variables.

def getSimulationTitles():
    titles = []

    titles.append("AuBC cyl")
    titles.append("BioRitchieNew111017")
    titles.append("Bug Al Zr Sphere")
    titles.append("Mg2SiAlCube3kev")

    return titles

def createTempDataPath(path):
    tempDataPath = os.path.join(path, "tmp")
    if not os.path.isdir(tempDataPath):
        os.mkdir(tempDataPath)

    return tempDataPath

def removeTempDataPath(path):
    if os.path.expanduser(path):
        shutil.rmtree(path)
