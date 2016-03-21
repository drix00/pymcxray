#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.Dump
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

MCXRay dump results file.
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
import pymcxray.FileFormat.Results.Intersections as Intersections

# Globals and constants variables.

class Dump(object):
    def __init__(self):
        pass

    def read(self, filepath):
        lines = open(filepath, 'r').readlines()

        lineIndex = 2
        intersections = Intersections.Intersections()
        lineIndex += intersections.extractFromLines(lines[lineIndex:])


#    fprintf(prResultsDump, "##### Geometry Setup Start #####\n\n");
#    fprintf(prResultsDump, "\n");
#    rInter.bWriteIntersections(prResultsDump);
#    fprintf(prResultsDump, "\n");
#    fprintf(prResultsDump, "##### Geometry Setup End #####\n\n");
#
#    fprintf(prResultsDump, "##### Energy Update Start #####\n\n");
#    fprintf(prResultsDump, "Voxel total            = %d\n", iVoxTot);
#    fprintf(prResultsDump, "Voxel failed precision = %d\n", iVoxFail);
#    fprintf(prResultsDump, "\n");
#    fprintf(prResultsDump, "Coordinate faults      = %d\n", iFaultTot);
#    fprintf(prResultsDump, "   faults X neg = %d\tmin coord index = %d\n", (int)rFaultNbrNeg.dX, (int)rFaultMaxNeg.dX);
#    fprintf(prResultsDump, "   faults X pos = %d\tmax coord index = %d\n", (int)rFaultNbrPos.dX, (int)rFaultMaxPos.dX);
#    fprintf(prResultsDump, "   faults Y neg = %d\tmin coord index = %d\n", (int)rFaultNbrNeg.dY, (int)rFaultMaxNeg.dY);
#    fprintf(prResultsDump, "   faults Y pos = %d\tmax coord index = %d\n", (int)rFaultNbrPos.dY, (int)rFaultMaxPos.dY);
#    fprintf(prResultsDump, "   faults Z neg = %d\tmin coord index = %d\n", (int)rFaultNbrNeg.dZ, (int)rFaultMaxNeg.dZ);
#    fprintf(prResultsDump, "   faults Z pos = %d\tmax coord index = %d\n", (int)rFaultNbrPos.dZ, (int)rFaultMaxPos.dZ);
#    fprintf(prResultsDump, "\n##### Energy Update End #####\n");
