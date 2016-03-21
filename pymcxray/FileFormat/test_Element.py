#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.test_Element
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for module `Element`.
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
import unittest
import logging

# Third party modules.

# Local modules.

# Project modules
import pymcxray.FileFormat.Element as Element

# Globals and constants variables.

class TestElement(unittest.TestCase):
    """
    TestCase class for the module `Element`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

    def tearDown(self):
        """
        Teardown method.
        """

        unittest.TestCase.tearDown(self)

    def testSkeleton(self):
        """
        First test to check if the testcase is working with the testing framework.
        """

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_extractFromLineOldVersion(self):
        """
        Tests for method `extractFromLineOldVersion`.
        """

        line = "6 1.000000000000000"
        element = Element.Element()
        element.extractFromLineOldVersion(line)
        self.assertEquals(6, element.atomicNumber)
        self.assertEquals(1.0, element.massFraction)

        line = "79 1.000000000000000"
        element = Element.Element()
        element.extractFromLineOldVersion(line)
        self.assertEquals(79, element.atomicNumber)
        self.assertEquals(1.0, element.massFraction)

        line = "6 0.700000000000000"
        element = Element.Element()
        element.extractFromLineOldVersion(line)
        self.assertEquals(6, element.atomicNumber)
        self.assertEquals(0.7, element.massFraction)

        line = "8 0.280000000000000"
        element = Element.Element()
        element.extractFromLineOldVersion(line)
        self.assertEquals(8, element.atomicNumber)
        self.assertEquals(0.28, element.massFraction)

        line = "17 0.020000000000000"
        element = Element.Element()
        element.extractFromLineOldVersion(line)
        self.assertEquals(17, element.atomicNumber)
        self.assertEquals(0.02, element.massFraction)

        #self.fail("Test if the testcase is working.")

    def test_createLineOldVersion(self):
        """
        Tests for method `createLineOldVersion`.
        """

        lineRef = "6 1.000000000000000"
        element = Element.Element()
        element.atomicNumber = 6
        element.massFraction = 1.0
        line = element.createLineOldVersion()
        self.assertEquals(lineRef, line)

        lineRef = "79 1.000000000000000"
        element = Element.Element()
        element.atomicNumber = 79
        element.massFraction = 1.0
        line = element.createLineOldVersion()
        self.assertEquals(lineRef, line)

        lineRef = "6 0.700000000000000"
        element = Element.Element()
        element.atomicNumber = 6
        element.massFraction = 0.7
        line = element.createLineOldVersion()
        self.assertEquals(lineRef, line)

        lineRef = "8 0.280000000000000"
        element = Element.Element()
        element.atomicNumber = 8
        element.massFraction = 0.28
        line = element.createLineOldVersion()
        self.assertEquals(lineRef, line)

        lineRef = "17 0.020000000000000"
        element = Element.Element()
        element.atomicNumber = 17
        element.massFraction = 0.02
        line = element.createLineOldVersion()
        self.assertEquals(lineRef, line)

        #self.fail("Test if the testcase is working.")

    def test_extractFromLineWithKey(self):
        """
        Tests for method `extractFromLinesWithKey`.
        """
        lines = \
"""AtomicNumber=14
WeightFraction=0.400000000000000
""".splitlines()
        element = Element.Element()
        element.extractFromLinesWithKey(lines)
        self.assertEquals(14, element.atomicNumber)
        self.assertEquals(0.4, element.massFraction)

        lines = \
"""AtomicNumber=15
WeightFraction=0.600000000000000
""".splitlines()
        element = Element.Element()
        element.extractFromLinesWithKey(lines)
        self.assertEquals(15, element.atomicNumber)
        self.assertEquals(0.6, element.massFraction)

        lines = \
"""AtomicNumber=7
WeightFraction=1.000000000000000
""".splitlines()
        element = Element.Element()
        element.extractFromLinesWithKey(lines)
        self.assertEquals(7, element.atomicNumber)
        self.assertEquals(1.0, element.massFraction)

        lines = \
"""AtomicNumber=56
WeightFraction=1.000000000000000
""".splitlines()
        element = Element.Element()
        element.extractFromLinesWithKey(lines)
        self.assertEquals(56, element.atomicNumber)
        self.assertEquals(1.0, element.massFraction)

        #self.fail("Test if the testcase is working.")

    def test_createLineWithKey(self):
        """
        Tests for method `createLineOldVersion`.
        """

        linesRef = \
"""AtomicNumber=14
WeightFraction=0.400000000000000
""".splitlines()
        element = Element.Element()
        element.atomicNumber = 14
        element.massFraction = 0.4
        lines = element.createLinesWithKey()
        self.assertEquals(linesRef, lines)

        linesRef = \
"""AtomicNumber=15
WeightFraction=0.600000000000000
""".splitlines()
        element = Element.Element()
        element.atomicNumber = 15
        element.massFraction = 0.6
        lines = element.createLinesWithKey()
        self.assertEquals(linesRef, lines)

        linesRef = \
"""AtomicNumber=7
WeightFraction=1.000000000000000
""".splitlines()
        element = Element.Element()
        element.atomicNumber = 7
        element.massFraction = 1.0
        lines = element.createLinesWithKey()
        self.assertEquals(linesRef, lines)

        linesRef = \
"""AtomicNumber=56
WeightFraction=1.000000000000000
""".splitlines()
        element = Element.Element()
        element.atomicNumber = 56
        element.massFraction = 1.0
        lines = element.createLinesWithKey()
        self.assertEquals(linesRef, lines)

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    from pymcxray.Testings import runTestModuleWithCoverage
    runTestModuleWithCoverage(__file__, withCoverage=True)
