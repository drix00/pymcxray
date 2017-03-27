#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.exported.DataMap
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Read data map exported by MCXRay.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2012 Hendrix Demers"
__license__ = ""

# Standard library modules.

# Third party modules.
import numpy as np
from PIL import Image

# Local modules.

# Project modules

# Globals and constants variables.

class DataMap(object):
    def __init__(self, filepath):
        self._filepath = filepath

        self.size = (0, 0)

    def read(self):
        lines = open(self._filepath, 'r').readlines()

        line = lines[0]
        index = line.rfind('(')
        self.imageName = line[:index].strip()

        text = line[index:].strip()

        items = text[1:-1].split(',')
        self.size = (int(items[0]), int(items[1]))

        pixels = np.zeros(self.size)

        for indexX, line in enumerate(lines[2:]):
            for indexY, value in enumerate(line.split()):
                pixels[indexX][indexY] = float(value)

        self.pixels = pixels

    def showImage(self):
        image = Image.fromarray(self.pixels)

        image.show()

    def saveImage(self, imageFilepath=None):
        if imageFilepath == None:
            imageFilepath = self._filepath[:-4] + '.tiff'
        image = Image.fromarray(self.pixels)

        image.save(imageFilepath)

    @property
    def imageName(self):
        return self._imageName

    @imageName.setter
    def imageName(self, imageName):
        self._imageName = imageName

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    @property
    def pixels(self):
        return self._pixels

    @pixels.setter
    def pixels(self, pixels):
        self._pixels = pixels

def run():
    from pymcxray import get_current_module_path

    filepath = get_current_module_path(__file__, "../../../../test_data/exportedFiles/CNTsFePt_30keV_100e_100pixels_BF.txt")

    dataMap = DataMap(filepath)
    dataMap.read()

    dataMap.showImage()
    dataMap.saveImage()

if __name__ == '__main__': #pragma: no cover
    run()
