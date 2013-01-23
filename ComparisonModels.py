#!/usr/bin/env python
"""
.. py:currentmodule:: ComparisonModels
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Comparison of the models used by MCXray.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2012 Hendrix Demers"
__license__ = ""

# Standard library modules.
import os.path
import csv
import logging
import math

# Third party modules.
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np

# Local modules.
import DrixUtilities.Files as Files

# Project modules

# Globals and constants variables.

KEY_XRAY_ENERGY_keV = "X-ray energy (keV)"
KEY_THETA_rad = " Theta (rad)"

class ComparisonModels(object):
    def __init__(self, dataPath):
        self._dataPath = dataPath

    def graphicsXrayCrossSectionBremstrahlung(self):
        basename = "CompareModels_XrayCrossSectionBremstrahlung"

        atomicNumbers = [6, 13, 29, 40, 47, 60, 79, 92]
        electronEnergies_keV = [1.0, 5.0, 10.0, 20.0, 30.0, 40.0, 50.0, 100.0, 200.0, 300.0, 400.0, 500.0]

        #atomicNumbers = [6, 79]
        #electronEnergies_keV = [200.0]

        for atomicNumber in atomicNumbers:
            for electronEnergy_keV in electronEnergies_keV:
                # CompareModels_XrayCrossSectionBremstrahlung_Z6_E1keV.csv
                filename = "%s_Z%i_E%ikeV.csv" % (basename, atomicNumber, int(electronEnergy_keV))
                filepath = os.path.join(self._dataPath, filename)
                logging.info("Reading filepath: %s", filepath)

                data = {}
                reader = csv.DictReader(open(filepath, 'rb'))

                validFieldnames = []
                for fieldname in reader.fieldnames:
                    if fieldname.strip() != "":
                        validFieldnames.append(fieldname)

                # Skip header row
                #reader.next()

                for key in validFieldnames:
                    data.setdefault(key, [])

                for rowDict in reader:
                    for key in validFieldnames:
                        data[key].append(float(rowDict[key]))

                logging.info("Number of data: %i", len(data[KEY_XRAY_ENERGY_keV]))

                xrayEnergies_keV = sorted(set(data[KEY_XRAY_ENERGY_keV]))
                thetas_rad = sorted(set(data[KEY_THETA_rad]))
                modelNames = []
                for fieldname in validFieldnames:
                    if fieldname != KEY_XRAY_ENERGY_keV and fieldname != KEY_THETA_rad:
                        modelNames.append(fieldname)

                modelNames = sorted(modelNames)

                graphicFilename = "%s_%s_Z%i_E%ikeV.pdf" % (basename, "XrayEnergy", atomicNumber, int(electronEnergy_keV))
                graphicFilepath = os.path.join(self._dataPath, "Graphics")
                graphicFilepath = Files.createPath(graphicFilepath)
                graphicFilepath = os.path.join(graphicFilepath, graphicFilename)
                pdf = PdfPages(graphicFilepath)

                for theta_rad in thetas_rad:
                    plt.figure()
                    theta_deg = math.degrees(theta_rad)
                    title = r"%i, $E_{0} = %i$ keV, $\theta = %.2f$ deg" % (atomicNumber, int(electronEnergy_keV), theta_deg)
                    plt.title(title)

                    maskArray = np.ma.masked_not_equal(np.array(data[KEY_THETA_rad]), theta_rad)
                    for modelName in modelNames:
                        try:
                            x = np.array(data[KEY_XRAY_ENERGY_keV])[~maskArray.mask]
                            y = np.array(data[modelName])[~maskArray.mask]
                            plt.semilogy(x, y, label=modelName)
                        except ValueError, message:
                            logging.error(message)

                    plt.legend(loc='best')
                    plt.xlabel(r"$E_{x}$ (keV)")
                    plt.ylabel(r"A$^2$/(sr keV)")
                    #plt.ylim(ymin=0.0)

                    pdf.savefig()
                    plt.close()

                pdf.close()

                graphicFilename = "%s_%s_Z%i_E%ikeV.pdf" % (basename, "XrayTheta", atomicNumber, int(electronEnergy_keV))
                graphicFilepath = os.path.join(self._dataPath, "Graphics")
                graphicFilepath = Files.createPath(graphicFilepath)
                graphicFilepath = os.path.join(graphicFilepath, graphicFilename)
                pdf = PdfPages(graphicFilepath)

                for xrayEnergy_keV in xrayEnergies_keV:
                    plt.figure()
                    title = r"%i, $E_{0} = %i$ keV, $E_{X} = %.3f$ keV" % (atomicNumber, int(electronEnergy_keV), xrayEnergy_keV)
                    plt.title(title)

                    maskArray = np.ma.masked_not_equal(np.array(data[KEY_XRAY_ENERGY_keV]), xrayEnergy_keV)
                    for modelName in modelNames:
                        try:
                            x = np.array(data[KEY_THETA_rad])[~maskArray.mask]
                            x = np.degrees(x)
                            y = np.array(data[modelName])[~maskArray.mask]
                            plt.semilogy(x, y, label=modelName)
                        except ValueError, message:
                            logging.error(message)

                    plt.legend(loc='best')
                    plt.xlabel(r"$\theta$ (deg)")
                    plt.ylabel(r"A$^2$/(sr keV)")
                    #plt.ylim(ymin=0.0)

                    pdf.savefig()
                    plt.close()

                pdf.close()

def runVersion1_2_3():
    dataPath = r"J:\hdemers\work\mcgill2012\results\simulations\McXRay\ComparisonModels\2012-09-19_10h52m55s_MCXRay_v1.2.3.0\Results\CompareModelsData"
    comparisonModels = ComparisonModels(dataPath)

    comparisonModels.graphicsXrayCrossSectionBremstrahlung()

if __name__ == '__main__': #pragma: no cover
    import DrixUtilities.Runner as Runner
    Runner.Runner().run(runFunction=runVersion1_2_3)
