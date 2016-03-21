#!/usr/bin/env python
"""
.. py:currentmodule:: FileFormat.Results.Spectra
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

MCXRay spectra result file.
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
import pymcxray.FileFormat.Results.Tags as Tags
import pymcxray.FileFormat.Results.Spectrum as Spectrum
import pymcxray.FileFormat.Results.RegionParameters as RegionParameters
import pymcxray.FileFormat.Results.ElementParameters as ElementParameters
import pymcxray.FileFormat.Element as Element

# Globals and constants variables.
TAG_SPECTRUM_SPECIMEN = "Specimen spectra and background"
TAG_SPECTRUM_REGION = "Region"

class Spectra(object):
    def __init__(self):
        self._regionSpectra = {}
        self._regionParametersList = {}
        self._elementParameters = {}
        self._elementSpectra = {}

    def read(self, filepath):
        lines = open(filepath, 'r').readlines()

        lineIndex = 0

        lineIndex += self.readSpecimen(lines)

        self.readRegions(lines)

    def readSpecimen(self, lines):
        lineIndex = 0

        lineIndex += self._extracSpecimenHeader(lines)

        lineIndex = Tags.findTag(TAG_SPECTRUM_SPECIMEN, lines)

        energies_keV = []
        intensities = []
        backgrounds = []
        for line in lines[lineIndex+1:]:
            lineIndex += 1

            if line.strip() == "":
                break
            else:
                items = line.split()
                energies_keV.append(float(items[0]))
                intensities.append(float(items[1]))
                backgrounds.append(float(items[2]))

        self._specimenSpectrum = Spectrum.Spectrum()
        self._specimenSpectrum.energies_keV = energies_keV
        self._specimenSpectrum.intensities = intensities
        self._specimenSpectrum.backgroundIntensities = backgrounds

        return lineIndex

    def _extracSpecimenHeader(self, lines):
        lineIndex = 0
#    fprintf(prFile, "Number of simulated electron trajectories = %d \n",                            ulElectronNbr);
#    fprintf(prFile, "Number of regions in the specimen = %d \n",                                    iRegionNbr);
#
#    fprintf(prFile, "\nElectron incident energy = %lf \n",                                            dBeamEnergy);
#    fprintf(prFile, "Beam Current = %e (A) \n",                                                        dBeamCurrent);
#    fprintf(prFile, "Acquisition Time = %lf (S) \n",                                                dBeamTime);
#    fprintf(prFile, "\n\nThe negative Z axis is the e Beam axis \n");
#    fprintf(prFile, "A positive tilt angle gives a negative projection on X Axis \n");
#    fprintf(prFile, "The Y axis is the rotation axis \n\n");
#    fprintf(prFile, "Tilt angle = %lf (Deg.) \n",                                                    dToDegrees(rBeamAngle.dTheta));
#    fprintf(prFile, "Angle between X-Ray detector axis and specimen normal = %lf (Deg.) \n",        dToDegrees(rDetectorAngle.dTheta));
#    fprintf(prFile, "Angle between X-Ray detector  and x axis on the X-Y plane = %lf (Deg.) \n",    dToDegrees(rDetectorAngle.dPhi));
#    fprintf(prFile, "Take Off Angle at Normal Incidence = %lf (Deg.) \n",                            dToDegrees(dTOA));
#    fprintf(prFile, "Effective Take Off Angle = %lf (Deg.) \n\n\n",                                    dToDegrees(dXsi));
#    fprintf(prFile, "Thickness of Be window = %lf (um) \n",                                            dBeThick * 10000.0);
#    fprintf(prFile, "Thickness of Al window = %lf (um) \n",                                            dAlThick * 10000.0);
#    fprintf(prFile, "Thickness of Ti window = %lf (um) \n",                                            dTiThick * 10000.0);
#    fprintf(prFile, "Thickness of Oil = %lf (um) \n",                                                dOilThick * 10000.0);
#    fprintf(prFile, "Thickness of Moxtek = %lf (um) \n",                                            dMoxtekThick * 10000.0);
#    fprintf(prFile, "Thickness of H2O = %lf (um) \n",                                                dH2OThick * 10000.0);
#    fprintf(prFile, "Thickness of air path = %lf (cm) \n",                                            dAirThick);
#    fprintf(prFile, "Radius of detector crystal = %lf (mm) \n",                                        dCrystalRadius * 10.0);
#    fprintf(prFile, "Distance e-beam to x-ray detector = %lf (cm) \n",                                dCrystalDist);
#
#    fprintf(prFile, "\n\nNumber of windows in continuum computation = %d \n",                        Nb_Win);
#    fprintf(prFile, "Number of layers in phi-ro-z = %d  \n",                                        rFilmNbr.tZ);
#
#    fprintf(prFile, "\n\nMean number of collisions per e = %lf \n",                                    dElecCollNbrMean);
#    fprintf(prFile, "Mean distance between collisions = %lf \n",                                    dElecCollDistMean);
#    fprintf(prFile, "Mean polar angle of collision = %lf \n",                                        dToDegrees(rElecCollAngleMean.dTheta));
#    fprintf(prFile, "Mean azimuthal angle of collision = %lf \n",                                    dToDegrees(rElecCollAngleMean.dPhi));
#    fprintf(prFile, "Backscattering coefficient = %lf \n",                                            dElecBackScattCoeff);
#    fprintf(prFile, "Internal electron coefficient = %lf \n",                                        dElecInternalCoeff);

        return lineIndex

    def getSpecimenSpectrum(self):
        return self._specimenSpectrum

    def getRegionParameters(self, regionID):
        return self._regionParametersList[regionID]

    def getRegionSpectrum(self, regionID):
        return self._regionSpectra[regionID]

    def getElementSpectrum(self, regionID, elementName):
        return self._elementSpectra[regionID][elementName]

    def getElementSpectra(self):
        return self._elementSpectra

    def readRegions(self, lines):
        self._regionSpectra = {}
        self._regionParametersList = {}
        self._elementParameters = {}
        self._elementSpectra = {}

        indexList = Tags.findAllTag(TAG_SPECTRUM_REGION, lines, contains="number of elements =")

        for lineIndex in indexList:
            self.readRegion(lines[lineIndex:])

    def readRegion(self, lines):
        lineIndex = 0
        regionLines = lines[lineIndex:]
        regionParameters = self._extractRegionHeader(regionLines)

        self._regionParametersList[regionParameters.regionID] = regionParameters

        tag = "Region %i spectra and background:" % (regionParameters.regionID)
        lineIndex = Tags.findTag(tag, regionLines)

        energies_keV = []
        intensities = []
        backgrounds = []
        for line in regionLines[lineIndex+1:]:
            lineIndex += 1

            if line.strip() == "":
                break
            else:
                items = line.split()
                energies_keV.append(float(items[0]))
                intensities.append(float(items[1]))
                backgrounds.append(float(items[2]))

        regionSpectrum = Spectrum.Spectrum()
        regionSpectrum.energies_keV = energies_keV
        regionSpectrum.intensities = intensities
        regionSpectrum.backgroundIntensities = backgrounds

        self._regionSpectra[regionParameters.regionID] = regionSpectrum

        self._elementParameters.setdefault(regionParameters.regionID, {})
        self._elementSpectra.setdefault(regionParameters.regionID, {})

        for element in regionParameters.elements:
            elementLines = regionLines[lineIndex:]
            tag = "%s weight fraction = %.6f" % (element.name, element.massFraction)
            elementLineIndex = Tags.findTag(tag, elementLines)

            elementParameters = self._extractElementHeader(elementLines[elementLineIndex:])

            tag = "%s spectra:" % (element.name)
            elementLineIndex = Tags.findTag(tag, elementLines)

            energies_keV = []
            intensities = []
            for line in elementLines[elementLineIndex+1:]:
                elementLineIndex += 1

                if line.strip() == "":
                    break
                else:
                    items = line.split()
                    energies_keV.append(float(items[0]))
                    intensities.append(float(items[1]))

            elementSpectrum = Spectrum.Spectrum()
            elementSpectrum.energies_keV = energies_keV
            elementSpectrum.intensities = intensities

            self._elementParameters[regionParameters.regionID][element.name] = elementParameters
            self._elementSpectra[regionParameters.regionID][element.name] = elementSpectrum

            lineIndex += elementLineIndex

    def _extractRegionHeader(self, lines):
        regionParameters = RegionParameters.RegionParameters()

        lineIndex = 0

        # Region 0 number of elements = 1
        line = lines[lineIndex]
        lineIndex += 1

        items = line.split('=')
        regionParameters.regionID = int(items[0].replace('Region', '').replace('number of elements', ''))
        regionParameters.numberElements = int(items[-1])

        regionParameters.elements = []

        #    Weight fraction of Carbon = 1.000000
        for _indexElement in range(regionParameters.numberElements):
            line = lines[lineIndex]
            lineIndex += 1

            items = line.split("=")
            name = items[0].replace("Weight fraction of", '').strip()
            weightFraction = float(items[-1])

            element = Element.Element()
            element.name = name
            element.massFraction = weightFraction

            regionParameters.elements.append(element)

        # Thickness of layers in phi-ro-z = 346.177758 (A)
        line = lines[lineIndex]
        lineIndex += 1
        items = line.split('=')
        thickness_A = float(items[-1].replace('(A)', ''))
        regionParameters.layerThickness_A = thickness_A

        return regionParameters

    def _extractElementHeader(self, lines):
        elementParameters = ElementParameters.ElementParameters()

        return elementParameters

    @property
    def numberRegions(self):
        assert len(self._regionSpectra) == len(self._regionParametersList)
        return len(self._regionSpectra)
