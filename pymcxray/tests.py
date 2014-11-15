#!/usr/bin/env python
"""
.. py:currentmodule:: tests
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Regression testing for the project.
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
import pyHendrixDemersTools.Testings as Testings

# Project modules

# Globals and constants variables.

if __name__ == "__main__": #pragma: no cover
    Testings.runTestSuiteWithCoverage(packageName=__file__)
