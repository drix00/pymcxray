#!/usr/bin/env python
"""Regression testing for the project."""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2011 Hendrix Demers"
__license__ = ""

# Standard library modules.

# Third party modules.

# Local modules.

# Project modules

# Globals and constants variables.

if __name__ == "__main__": #pragma: no cover
    import logging
    logging.getLogger().setLevel(logging.INFO)
    from pymcxray.Testings import runTestSuiteWithCoverage
    runTestSuiteWithCoverage(__file__)
