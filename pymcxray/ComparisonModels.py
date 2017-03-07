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
from pymcxray import find_all_files, create_path

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
                reader = csv.DictReader(open(filepath, 'r'))

                validFieldnames = []
                for fieldname in reader.fieldnames:
                    if fieldname.strip() != "":
                        validFieldnames.append(fieldname)

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
                graphicFilepath = create_path(graphicFilepath)
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
                        except ValueError as message:
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
                graphicFilepath = create_path(graphicFilepath)
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
                        except ValueError as message:
                            logging.error(message)

                    plt.legend(loc='best')
                    plt.xlabel(r"$\theta$ (deg)")
                    plt.ylabel(r"A$^2$/(sr keV)")
                    #plt.ylim(ymin=0.0)

                    pdf.savefig()
                    plt.close()

                pdf.close()

    def graphicsXrayMassAbsorptionCoefficient(self):
        basename = "CompareModels_XrayMassAbsorptionCoefficient"

        graphicFilename = "%s.pdf" % (basename)
        graphicFilepath = os.path.join(self._dataPath, "Graphics")
        graphicFilepath = create_path(graphicFilepath)
        graphicFilepath = os.path.join(graphicFilepath, graphicFilename)
        pdf = PdfPages(graphicFilepath)

        for filepath in find_all_files(self._dataPath, "CompareModels_XrayMassAbsorptionCoefficient*.csv", single_level=True):
            logging.debug(filepath)

            filename = os.path.basename(filepath)
            name, _extension = os.path.splitext(filename)
            items = name.split('_')
            logging.debug(items[2])
            atomicNumber = int(items[2][1:])
            logging.debug(atomicNumber)

            reader = csv.DictReader(open(filepath, 'r'))

            fieldnames = reader.fieldnames
            logging.debug(fieldnames)
            fieldnames = fieldnames[:-1]

            data = {}
            for fieldname in fieldnames:
                data[fieldname] = []

            for row in reader:
                for fieldname in fieldnames:
                    try:
                        data[fieldname].append(float(row[fieldname]))
                    except ValueError:
                        data[fieldname].append(0.0)

            plt.figure()
            title = "Z = %i" % (atomicNumber)
            plt.title(title)

            x = data["X-ray Energy (keV)"]
            for fieldname in fieldnames[1:]:
                y = data[fieldname]
                plt.loglog(x, y, label=fieldname)

            plt.xlabel(r"Photon Energy (keV)")
            plt.ylabel(r"MAC (cm$^2$/g)")

            plt.legend(loc='best')

            pdf.savefig()
            #plt.close()

        pdf.close()

    def graphicsEnergyLoss(self):
        basename = "CompareModels_EnergyLoss"

        graphicFilename = "%s.pdf" % (basename)
        graphicFilepath = os.path.join(self._dataPath, "Graphics")
        graphicFilepath = create_path(graphicFilepath)
        graphicFilepath = os.path.join(graphicFilepath, graphicFilename)
        pdf = PdfPages(graphicFilepath)

        for filepath in find_all_files(self._dataPath, "CompareModels_RegionEnergyLoss_*.csv", single_level=True):
            logging.debug(filepath)

            filename = os.path.basename(filepath)
            name, _extension = os.path.splitext(filename)
            items = name.split('_')
            logging.debug(items[2])
            atomicNumber = int(items[2][1:])
            logging.debug(atomicNumber)
            energy_keV = int(items[3][1:-3])
            logging.debug(energy_keV)

            reader = csv.DictReader(open(filepath, 'r'))

            fieldnames = reader.fieldnames
            fieldnames = fieldnames[:-1]
            logging.debug(fieldnames)

            data = {}
            for fieldname in fieldnames:
                data[fieldname] = []

            for row in reader:
                for fieldname in fieldnames:
                    try:
                        data[fieldname].append(1.0e3*float(row[fieldname]))
                    except ValueError:
                        data[fieldname].append(0.0)

            plt.figure()
            title = r"Z = %i, $E_{0} = %.1f$ keV" % (atomicNumber, energy_keV)
            plt.title(title)

            yMin = 0.0
            x = data["Energy (keV)"]
            for fieldname in fieldnames[1:]:
                y = data[fieldname]
                yMin = min(yMin, np.min(y))
                plt.semilogx(x, y, label=fieldname)

            plt.xlabel(r"Energy (keV)")
            plt.ylabel(r"Energy Loss (eV/A)")
            plt.ylim(ymax=0.0, ymin=yMin)
            plt.legend(loc='best')

            pdf.savefig()
            plt.close()

        pdf.close()

    def graphicsIonizationCrossSection(self):
        basename = "CompareModels_IonizationCrossSection"

        graphicFilename = "%s.pdf" % (basename)
        graphicFilepath = os.path.join(self._dataPath, "Graphics")
        graphicFilepath = create_path(graphicFilepath)
        graphicFilepath = os.path.join(graphicFilepath, graphicFilename)
        pdf = PdfPages(graphicFilepath)

        for filepath in find_all_files(self._dataPath, "CompareModels_XrayCrossSectionCharacteristic_*.csv", single_level=True):
            logging.debug(filepath)

            filename = os.path.basename(filepath)
            name, _extension = os.path.splitext(filename)
            items = name.split('_')
            atomicNumber = int(items[2][1:])
            logging.debug(atomicNumber)
            subshell = items[3]
            logging.debug(subshell)

            reader = csv.DictReader(open(filepath, 'r'))

            fieldnames = reader.fieldnames
            fieldnames = fieldnames[:-1]
            logging.debug(fieldnames)

            data = {}
            for fieldname in fieldnames:
                data[fieldname] = []

            for row in reader:
                for fieldname in fieldnames:
                    try:
                        data[fieldname].append(float(row[fieldname]))
                    except ValueError:
                        data[fieldname].append(0.0)

            plt.figure()
            title = r"Z = %i, %s" % (atomicNumber, subshell)
            plt.title(title)

            x = data["Electron Energy (keV)"]
            #x = data["Overvoltage"]
            for fieldname in fieldnames[2:]:
                y = data[fieldname]
                plt.semilogx(x, y, label=fieldname)

            plt.xlabel(r"Energy (keV)")
            plt.ylabel(r"$\sigma$ (A$^{2}$)")
            plt.legend(loc='best')

            pdf.savefig()
            plt.close()

#             plt.figure()
#             title = r"Z = %i, %s" % (atomicNumber, subshell)
#             plt.title(title)
#
#             #x = data["Electron Energy (keV)"]
#             x = data["Overvoltage"]
#             for fieldname in fieldnames[2:]:
#                 y = data[fieldname]
#                 plt.semilogx(x, y, label=fieldname)
#
#             plt.xlabel(r"Energy (keV)")
#             plt.ylabel(r"$\sigma$ (A$^{2}$)")
#             plt.legend(loc='best')
#
#             pdf.savefig()
#             plt.close()

        pdf.close()

def runVersion1_2_3():
    dataPath = r"J:\hdemers\work\results\simulations\McXRay\ComparisonModels\2012-09-19_10h52m55s_MCXRay_v1.2.3.0\Results\CompareModelsData"
    comparisonModels = ComparisonModels(dataPath)

    #comparisonModels.graphicsXrayCrossSectionBremstrahlung()
    comparisonModels.graphicsXrayMassAbsorptionCoefficient()

def runVersion1_4_0():
    dataPath = r"J:\hdemers\work\results\simulations\McXRay\ComparisonModels\2013-04-11_16h37m42s_MCXRay_v1.4.0.0\Results\CompareModelsData"
    comparisonModels = ComparisonModels(dataPath)

    #comparisonModels.graphicsXrayCrossSectionBremstrahlung()
    comparisonModels.graphicsXrayMassAbsorptionCoefficient()

def runVersion1_4_1():
    dataPath = r"J:\hdemers\work\results\simulations\McXRay\ComparisonModels\2013-04-20_09h31m36s_MCXRay_v1.4.1.0\Results\CompareModelsData"
    comparisonModels = ComparisonModels(dataPath)

    #comparisonModels.graphicsXrayCrossSectionBremstrahlung()
    #comparisonModels.graphicsXrayMassAbsorptionCoefficient()
    #comparisonModels.graphicsEnergyLoss()
    comparisonModels.graphicsIonizationCrossSection()

if __name__ == '__main__': #pragma: no cover
    runVersion1_4_1()
