#!/usr/bin/env python
"""
.. py:currentmodule:: SystemTesting.SystemTesting
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

System testing of MCXray.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2012 Hendrix Demers"
__license__ = ""

# Standard library modules.
import logging
import os.path

# Third party modules.
import matplotlib.pyplot as plt
import numpy as np

# Local modules.
import pyHendrixDemersTools.Files as Files

# Project modules
import pymcxray.Simulation as Simulation
import pymcxray.FileFormat.MCXRayModel as MCXRayModel
import pymcxray.FileFormat.Results.Spectra as Spectra
import pymcxray.BatchFileConsole as BatchFileConsole
import pymcxray.mcxray as mcxray

# Globals and constants variables.

class SimulationsBulk(mcxray._Simulations):

    def _createPath(self, path, name=""):
        if not os.path.isdir(path):
            if name == "":
                logging.info("Create path: %s", path)
            else:
                logging.info("Create %s path: %s", name, path)

            os.makedirs(path)

    def _initData(self):
        self._atomicNumbers = [6, 13, 29, 47, 79, 92]

        self._energies_keV = [1.0, 5.0, 10.0, 20.0, 30.0, 40.0]
        self._numberElectrons = 100000
        self._numberPhotons = 1000000

    def getAnalysisName(self):
        return "Bulk"

    def generateInputFiles(self, batchFile):
        logging.info("generateInputFiles for analysis: %s", self.getAnalysisName())

        numberSimulations = 0
        numberSimulationsTodo = 0
        numberSimulationsDone = 0
        simulationTodoNames = []

        inputPath = os.path.join(self.getSimulationsPath(), "input")
        inputPath = Files.createPath(inputPath)

        for energy_keV in self._energies_keV:
            for atomicNumber in self._atomicNumbers:
                simulation = Simulation.Simulation(overwrite=self._overwrite)
                simulation.basename = self.getAnalysisName()

                simulation.energy_keV = energy_keV
                simulation.numberElectrons = self._numberElectrons
                simulation.numberPhotons = self._numberPhotons

                simulation._specimen = Simulation.createPureBulkSample(atomicNumber)

                simulation.createSimulationFiles(inputPath, self.getSimulationsPath())

                if simulation.isDone(self.getSimulationsPath()):
                    numberSimulationsDone += 1
                else:
                    numberSimulationsTodo += 1
                    simulationTodoNames.append(simulation.name)
                    filename = os.path.join("input", simulation.filename)
                    batchFile.addSimulationName(filename)
                numberSimulations += 1

        #batchFile.write(self.getSimulationsPath())

        if self._verbose:
            for simulationTodoName in simulationTodoNames:
                logging.info("Todo: \t%s", simulationTodoName)

        percentage = 100.0*float(numberSimulationsDone)/float(numberSimulations)
        logging.info("Number of done: %4i/%i (%5.2f%%)", numberSimulationsDone, numberSimulations, percentage)
        percentage = 100.0*float(numberSimulationsTodo)/float(numberSimulations)
        logging.info("Number of todo: %4i/%i (%5.2f%%)", numberSimulationsTodo, numberSimulations, percentage)

    def readResultsFiles(self):
        logging.info("readResultsFiles")

        results = {}
        for energy_keV in self._energies_keV:
            results[energy_keV] = {}
            for atomicNumber in self._atomicNumbers:
                simulation = Simulation.Simulation(overwrite=self._overwrite)
                simulation.basename = self.getAnalysisName()

                simulation.energy_keV = energy_keV
                simulation.numberElectrons = self._numberElectrons
                simulation.numberPhotons = self._numberPhotons

                simulation._specimen = Simulation.createPureBulkSample(atomicNumber)

                simulation.createSimulationFiles(inputPath, self.getSimulationsPath())

                if simulation.isDone(self.getSimulationsPath()):
                    filepath = os.path.join(self.getSimulationsPath(), simulation.resultsBasename + "XABX.txt")
                    spectraFile = Spectra.Spectra()
                    spectraFile.read(filepath)

                    spectrum = spectraFile.getSpecimenSpectrum()
                    results[energy_keV][atomicNumber] = spectrum

        return results

    def analyzeResultsFiles(self):
        logging.info("analyzeResultsFiles")

        results = self.readResultsFiles()

        figurePath = os.path.join(self.getAnalyzesPath(), "figures")
        figurePath = Files.createPath(figurePath)

        # Complete spectrum
        for energy_keV in results:
            for atomicNumber in results[energy_keV]:
                plt.figure()
                title = r"Z = %i, E$_{0}$ = %.1f keV" % (atomicNumber, energy_keV)
                plt.title(title)

                spectrum = results[energy_keV][atomicNumber]

                energies_keV = np.array(spectrum.energies_keV)
                intensities = np.array(spectrum.intensities)

                plt.semilogy(energies_keV, intensities)

                plt.xlabel(r"$E_{X}$ (keV)")
                plt.ylabel("Counts")

                graphicName = "CompleteSpectrum_%02i_E%03.1fkeV" % (atomicNumber, energy_keV)
                graphicFilepath = os.path.join(figurePath, graphicName+'.png')
                plt.savefig(graphicFilepath)

class SimulationsRepetitions(SimulationsBulk):
    def _initData(self):
        self._atomicNumber = 6

        self._energy_keV = 10.0
        self._numberElectrons = 100000
        self._numberPhotons = 1000000

        self._repetitions = 10

    def getAnalysisName(self):
        return "Repetitions"

    def generateInputFiles(self, batchFile):
        logging.info("generateInputFiles for analysis: %s", self.getAnalysisName())

        numberSimulations = 0
        numberSimulationsTodo = 0
        numberSimulationsDone = 0
        simulationTodoNames = []

        inputPath = os.path.join(self.getSimulationsPath(), "input")
        inputPath = Files.createPath(inputPath)

        for repetitionID in range(1, self._repetitions+1):
            simulation = Simulation.Simulation(overwrite=self._overwrite)
            label = "_X%02i" % (repetitionID)
            simulation.basename = self.getAnalysisName() + label

            simulation.energy_keV = self._energy_keV
            simulation.numberElectrons = self._numberElectrons
            simulation.numberPhotons = self._numberPhotons

            simulation._specimen = Simulation.createPureBulkSample(self._atomicNumber)

            simulation.createSimulationFiles(inputPath, self.getSimulationsPath())

            if simulation.isDone(self.getSimulationsPath()):
                numberSimulationsDone += 1
            else:
                numberSimulationsTodo += 1
                simulationTodoNames.append(simulation.name)
                filename = os.path.join("input", simulation.filename)
                batchFile.addSimulationName(filename)
            numberSimulations += 1

        #batchFile.write(self.getSimulationsPath())

        if self._verbose:
            for simulationTodoName in simulationTodoNames:
                logging.info("Todo: \t%s", simulationTodoName)

        percentage = 100.0*float(numberSimulationsDone)/float(numberSimulations)
        logging.info("Number of done: %4i/%i (%5.2f%%)", numberSimulationsDone, numberSimulations, percentage)
        percentage = 100.0*float(numberSimulationsTodo)/float(numberSimulations)
        logging.info("Number of todo: %4i/%i (%5.2f%%)", numberSimulationsTodo, numberSimulations, percentage)

    def readResultsFiles(self):
        logging.info("readResultsFiles")

        results = {}
        for repetitionID in range(1, self._repetitions+1):
            simulation = Simulation.Simulation(overwrite=self._overwrite)
            label = "_X%02i" % (repetitionID)
            simulation.basename = self.getAnalysisName() + label

            simulation.energy_keV = self._energy_keV
            simulation.numberElectrons = self._numberElectrons
            simulation.numberPhotons = self._numberPhotons

            simulation._specimen = Simulation.createPureBulkSample(self._atomicNumber)

            simulation.createSimulationFiles(inputPath, self.getSimulationsPath())

            if simulation.isDone(self.getSimulationsPath()):
                filepath = os.path.join(self.getSimulationsPath(), simulation.resultsBasename + "XABX.txt")
                spectraFile = Spectra.Spectra()
                spectraFile.read(filepath)

                spectrum = spectraFile.getSpecimenSpectrum()
                results[repetitionID] = spectrum

        return results

    def analyzeResultsFiles(self):
        logging.info("analyzeResultsFiles")

        results = self.readResultsFiles()

        figurePath = os.path.join(self.getAnalyzesPath(), "figures")
        figurePath = Files.createPath(figurePath)

        # Complete spectrum
        plt.figure()
        plt.title("Complete")

        for repetitionID in sorted(results.keys()):
            spectrum = results[repetitionID]
            energies_keV = np.array(spectrum.energies_keV)
            intensities = np.array(spectrum.intensities)

            label = "%02i" % (repetitionID)
            plt.semilogy(energies_keV, intensities, label=label)

        plt.xlabel(r"$E_{X}$ (keV)")
        plt.ylabel("Counts")

        plt.legend(loc='best')

        graphicName = "CompleteSpectrum"
        graphicFilepath = os.path.join(figurePath, graphicName+'.png')
        plt.savefig(graphicFilepath)

        # Background spectrum
        plt.figure()
        plt.title("Background")

        for repetitionID in sorted(results.keys()):
            spectrum = results[repetitionID]
            energies_keV = np.array(spectrum.energies_keV)
            intensities = np.array(spectrum.intensities)
            backgrounds = np.array(spectrum.backgroundIntensities)

            label = "%02i" % (repetitionID)
            plt.semilogy(energies_keV, backgrounds, label=label)

        plt.xlabel(r"$E_{X}$ (keV)")
        plt.ylabel("Counts")

        plt.legend(loc='best')

        graphicName = "BackgroundSpectrum"
        graphicFilepath = os.path.join(figurePath, graphicName+'.png')
        plt.savefig(graphicFilepath)

        # Characteristic spectrum
        plt.figure()
        plt.title("Characteristic")

        for repetitionID in sorted(results.keys()):
            spectrum = results[repetitionID]
            energies_keV = np.array(spectrum.energies_keV)
            intensities = np.array(spectrum.intensities)
            backgrounds = np.array(spectrum.backgroundIntensities)

            label = "%02i" % (repetitionID)
            plt.plot(energies_keV, intensities-backgrounds, label=label)

        plt.xlabel(r"$E_{X}$ (keV)")
        plt.ylabel("Counts")

        plt.legend(loc='best')

        graphicName = "CharacteristicSpectrum"
        graphicFilepath = os.path.join(figurePath, graphicName+'.png')
        plt.savefig(graphicFilepath)

        # Difference spectrum
        plt.figure()
        plt.title("Difference")

        repetitionIDs = sorted(results.keys())
        if len(repetitionIDs) > 0:
            spectrum = results[repetitionIDs[0]]
            intensitiesRef = np.array(spectrum.intensities)
            for repetitionID in repetitionIDs[1:]:
                spectrum = results[repetitionID]
                energies_keV = np.array(spectrum.energies_keV)
                intensities = np.array(spectrum.intensities)

                label = "01 - %02i" % (repetitionID)
                plt.plot(energies_keV, intensitiesRef-intensities, label=label)

            plt.xlabel(r"$E_{X}$ (keV)")
            plt.ylabel("Counts")

            plt.legend(loc='best')

            graphicName = "DifferenceSpectrum"
            graphicFilepath = os.path.join(figurePath, graphicName+'.png')
            plt.savefig(graphicFilepath)

            # Difference relative spectrum
            plt.figure()
            plt.title("Difference Relative")

            repetitionIDs = sorted(results.keys())
            spectrum = results[repetitionIDs[0]]
            intensitiesRef = np.array(spectrum.intensities)
            for repetitionID in repetitionIDs[1:]:
                spectrum = results[repetitionID]
                energies_keV = np.array(spectrum.energies_keV)
                intensities = np.array(spectrum.intensities)

                label = "01 - %02i" % (repetitionID)
                plt.plot(energies_keV, (intensitiesRef-intensities)/intensitiesRef, label=label)

            plt.xlabel(r"$E_{X}$ (keV)")
            plt.ylabel("Fraction")

            plt.legend(loc='best')

            graphicName = "DifferenceRelativeSpectrum"
            graphicFilepath = os.path.join(figurePath, graphicName+'.png')
            plt.savefig(graphicFilepath)

            #plt.show()

class SimulationsNumberElectrons(SimulationsBulk):
    def _initData(self):
        self._atomicNumber = 6

        self._energy_keV = 10.0
        self._numberElectronsList = [1, 10, 100, 1000, 10000, 100000, 1000000]
        self._numberPhotons = 1000000

    def getAnalysisName(self):
        return "NumberElectrons"

    def generateInputFiles(self, batchFile):
        logging.info("generateInputFiles for analysis: %s", self.getAnalysisName())

        numberSimulations = 0
        numberSimulationsTodo = 0
        numberSimulationsDone = 0
        simulationTodoNames = []

        inputPath = os.path.join(self.getSimulationsPath(), "input")
        inputPath = Files.createPath(inputPath)

        for numberElectrons in self._numberElectronsList:
            simulation = Simulation.Simulation(overwrite=self._overwrite)
            label = "_N%ie" % (numberElectrons)
            simulation.basename = self.getAnalysisName() + label

            simulation.energy_keV = self._energy_keV
            simulation.numberElectrons = numberElectrons
            simulation.numberPhotons = self._numberPhotons

            simulation._specimen = Simulation.createPureBulkSample(self._atomicNumber)

            simulation.createSimulationFiles(inputPath, self.getSimulationsPath())

            if simulation.isDone(self.getSimulationsPath()):
                numberSimulationsDone += 1
            else:
                numberSimulationsTodo += 1
                simulationTodoNames.append(simulation.name)
                filename = os.path.join("input", simulation.filename)
                batchFile.addSimulationName(filename)
            numberSimulations += 1

        #batchFile.write(self.getSimulationsPath())

        if self._verbose:
            for simulationTodoName in simulationTodoNames:
                logging.info("Todo: \t%s", simulationTodoName)

        percentage = 100.0*float(numberSimulationsDone)/float(numberSimulations)
        logging.info("Number of done: %4i/%i (%5.2f%%)", numberSimulationsDone, numberSimulations, percentage)
        percentage = 100.0*float(numberSimulationsTodo)/float(numberSimulations)
        logging.info("Number of todo: %4i/%i (%5.2f%%)", numberSimulationsTodo, numberSimulations, percentage)

    def readResultsFiles(self):
        logging.info("readResultsFiles")

        results = {}

        for numberElectrons in self._numberElectronsList:
            simulation = Simulation.Simulation(overwrite=self._overwrite)
            label = "_N%ie" % (numberElectrons)
            simulation.basename = self.getAnalysisName() + label

            simulation.energy_keV = self._energy_keV
            simulation.numberElectrons = numberElectrons
            simulation.numberPhotons = self._numberPhotons

            simulation._specimen = Simulation.createPureBulkSample(self._atomicNumber)

            simulation.createSimulationFiles(inputPath, self.getSimulationsPath())

            if simulation.isDone(self.getSimulationsPath()):
                filepath = os.path.join(self.getSimulationsPath(), simulation.resultsBasename + "XABX.txt")
                spectraFile = Spectra.Spectra()
                spectraFile.read(filepath)

                spectrum = spectraFile.getSpecimenSpectrum()
                results[numberElectrons] = spectrum

        return results

    def analyzeResultsFiles(self):
        logging.info("analyzeResultsFiles")

        results = self.readResultsFiles()

        figurePath = os.path.join(self.getAnalyzesPath(), "figures")
        figurePath = Files.createPath(figurePath)

        numberElectronsList = sorted(results.keys())

        # Complete spectrum
        for numberElectrons in numberElectronsList:
            plt.figure()
            title = r"N = %i electrons" % (numberElectrons)
            plt.title(title)

            spectrum = results[numberElectrons]

            energies_keV = np.array(spectrum.energies_keV)
            intensities = np.array(spectrum.intensities)

            plt.semilogy(energies_keV, intensities)

            plt.xlabel(r"$E_{X}$ (keV)")
            plt.ylabel("Counts")

            graphicName = "CompleteSpectrum_N%ie" % (numberElectrons)
            graphicFilepath = os.path.join(figurePath, graphicName+'.png')
            plt.savefig(graphicFilepath)

        plt.figure()
        title = r"Number of electrons"
        plt.title(title)
        for numberElectrons in numberElectronsList:

            spectrum = results[numberElectrons]

            energies_keV = np.array(spectrum.energies_keV)
            intensities = np.array(spectrum.intensities)

            label = "N=%i" % (numberElectrons)
            plt.semilogy(energies_keV, intensities, label=label)

        plt.xlabel(r"$E_{X}$ (keV)")
        plt.ylabel("Counts")

        plt.legend(loc='best')

        graphicName = "CompleteSpectrum_NumberElectrons"
        graphicFilepath = os.path.join(figurePath, graphicName+'.png')
        plt.savefig(graphicFilepath)

        # Background spectrum
        for numberElectrons in numberElectronsList:
            plt.figure()
            title = r"N = %i electrons" % (numberElectrons)
            plt.title(title)

            spectrum = results[numberElectrons]

            energies_keV = np.array(spectrum.energies_keV)
            backgrounds = np.array(spectrum.backgroundIntensities)

            plt.semilogy(energies_keV, backgrounds)

            plt.xlabel(r"$E_{X}$ (keV)")
            plt.ylabel("Counts")

            graphicName = "BackgroundSpectrum_N%ie" % (numberElectrons)
            graphicFilepath = os.path.join(figurePath, graphicName+'.png')
            plt.savefig(graphicFilepath)

        plt.figure()
        title = r"Number of electrons"
        plt.title(title)
        for numberElectrons in numberElectronsList:

            spectrum = results[numberElectrons]

            energies_keV = np.array(spectrum.energies_keV)
            backgrounds = np.array(spectrum.backgroundIntensities)

            label = "N=%i" % (numberElectrons)
            plt.semilogy(energies_keV, backgrounds, label=label)

        plt.xlabel(r"$E_{X}$ (keV)")
        plt.ylabel("Counts")

        plt.legend(loc='best')

        graphicName = "BackgroundSpectrum_NumberElectrons"
        graphicFilepath = os.path.join(figurePath, graphicName+'.png')
        plt.savefig(graphicFilepath)

        # Characteristic spectrum
        for numberElectrons in numberElectronsList:
            plt.figure()
            title = r"N = %i electrons" % (numberElectrons)
            plt.title(title)

            spectrum = results[numberElectrons]

            energies_keV = np.array(spectrum.energies_keV)
            intensities = np.array(spectrum.intensities)
            backgrounds = np.array(spectrum.backgroundIntensities)

            plt.plot(energies_keV, intensities-backgrounds)

            plt.xlabel(r"$E_{X}$ (keV)")
            plt.ylabel("Counts")

            graphicName = "CharacteristicSpectrum_N%ie" % (numberElectrons)
            graphicFilepath = os.path.join(figurePath, graphicName+'.png')
            plt.savefig(graphicFilepath)

        plt.figure()
        title = r"Number of electrons"
        plt.title(title)
        for numberElectrons in numberElectronsList:

            spectrum = results[numberElectrons]

            energies_keV = np.array(spectrum.energies_keV)
            intensities = np.array(spectrum.intensities)
            backgrounds = np.array(spectrum.backgroundIntensities)

            label = "N=%i" % (numberElectrons)
            plt.plot(energies_keV, (intensities-backgrounds), label=label)

        plt.xlabel(r"$E_{X}$ (keV)")
        plt.ylabel("Counts")

        plt.legend(loc='best')

        graphicName = "CharacteristicSpectrum_NumberElectrons"
        graphicFilepath = os.path.join(figurePath, graphicName+'.png')
        plt.savefig(graphicFilepath)

class SimulationsCurrentTime(SimulationsBulk):
    def _initData(self):
        self._atomicNumber = 6

        self._energy_keV = 10.0
        self._numberElectrons = 100000
        self._numberPhotons = 1000000
        self._currentTimeList = [(1.0e-9, 1.0), (1.0e-8, 1.0), (1.0e-7, 1.0), (1.0e-9, 10.0), (1.0e-9, 10.0), (1.0e-9, 100.0)]

    def getAnalysisName(self):
        return "CurrentTime"

    def generateInputFiles(self, batchFile):
        logging.info("generateInputFiles for analysis: %s", self.getAnalysisName())

        numberSimulations = 0
        numberSimulationsTodo = 0
        numberSimulationsDone = 0
        simulationTodoNames = []

        inputPath = os.path.join(self.getSimulationsPath(), "input")
        inputPath = Files.createPath(inputPath)

        for current_A, time_s in self._currentTimeList:
            simulation = Simulation.Simulation(overwrite=self._overwrite)
            label = "_I%inA_t%is" % (current_A*1.0e9, time_s)
            simulation.basename = self.getAnalysisName() + label

            simulation.energy_keV = self._energy_keV
            simulation.numberElectrons = self._numberElectrons
            simulation.numberPhotons = self._numberPhotons
            simulation.current_A = current_A
            simulation.time_s = time_s

            simulation._specimen = Simulation.createPureBulkSample(self._atomicNumber)

            simulation.createSimulationFiles(inputPath, self.getSimulationsPath())

            if simulation.isDone(self.getSimulationsPath()):
                numberSimulationsDone += 1
            else:
                numberSimulationsTodo += 1
                simulationTodoNames.append(simulation.name)
                filename = os.path.join("input", simulation.filename)
                batchFile.addSimulationName(filename)
            numberSimulations += 1

        #batchFile.write(self.getSimulationsPath())

        if self._verbose:
            for simulationTodoName in simulationTodoNames:
                logging.info("Todo: \t%s", simulationTodoName)

        percentage = 100.0*float(numberSimulationsDone)/float(numberSimulations)
        logging.info("Number of done: %4i/%i (%5.2f%%)", numberSimulationsDone, numberSimulations, percentage)
        percentage = 100.0*float(numberSimulationsTodo)/float(numberSimulations)
        logging.info("Number of todo: %4i/%i (%5.2f%%)", numberSimulationsTodo, numberSimulations, percentage)

    def readResultsFiles(self):
        logging.info("readResultsFiles")

        results = {}

        for numberElectrons in self._numberElectronsList:
            simulation = Simulation.Simulation(overwrite=self._overwrite)
            label = "_N%ie" % (numberElectrons)
            simulation.basename = self.getAnalysisName() + label

            simulation.energy_keV = self._energy_keV
            simulation.numberElectrons = numberElectrons
            simulation.numberPhotons = self._numberPhotons

            simulation._specimen = Simulation.createPureBulkSample(self._atomicNumber)

            simulation.createSimulationFiles(inputPath, self.getSimulationsPath())

            if simulation.isDone(self.getSimulationsPath()):
                filepath = os.path.join(self.getSimulationsPath(), simulation.resultsBasename + "XABX.txt")
                spectraFile = Spectra.Spectra()
                spectraFile.read(filepath)

                spectrum = spectraFile.getSpecimenSpectrum()
                results[numberElectrons] = spectrum

        return results

    def analyzeResultsFiles(self):
        logging.info("analyzeResultsFiles")

        results = self.readResultsFiles()

        figurePath = os.path.join(self.getAnalyzesPath(), "figures")
        figurePath = Files.createPath(figurePath)

        numberElectronsList = sorted(results.keys())

        # Complete spectrum
        for numberElectrons in numberElectronsList:
            plt.figure()
            title = r"N = %i electrons" % (numberElectrons)
            plt.title(title)

            spectrum = results[numberElectrons]

            energies_keV = np.array(spectrum.energies_keV)
            intensities = np.array(spectrum.intensities)

            plt.semilogy(energies_keV, intensities)

            plt.xlabel(r"$E_{X}$ (keV)")
            plt.ylabel("Counts")

            graphicName = "CompleteSpectrum_N%ie" % (numberElectrons)
            graphicFilepath = os.path.join(figurePath, graphicName+'.png')
            plt.savefig(graphicFilepath)

        plt.figure()
        title = r"Number of electrons"
        plt.title(title)
        for numberElectrons in numberElectronsList:

            spectrum = results[numberElectrons]

            energies_keV = np.array(spectrum.energies_keV)
            intensities = np.array(spectrum.intensities)

            label = "N=%i" % (numberElectrons)
            plt.semilogy(energies_keV, intensities, label=label)

        plt.xlabel(r"$E_{X}$ (keV)")
        plt.ylabel("Counts")

        plt.legend(loc='best')

        graphicName = "CompleteSpectrum_NumberElectrons"
        graphicFilepath = os.path.join(figurePath, graphicName+'.png')
        plt.savefig(graphicFilepath)

        # Background spectrum
        for numberElectrons in numberElectronsList:
            plt.figure()
            title = r"N = %i electrons" % (numberElectrons)
            plt.title(title)

            spectrum = results[numberElectrons]

            energies_keV = np.array(spectrum.energies_keV)
            backgrounds = np.array(spectrum.backgroundIntensities)

            plt.semilogy(energies_keV, backgrounds)

            plt.xlabel(r"$E_{X}$ (keV)")
            plt.ylabel("Counts")

            graphicName = "BackgroundSpectrum_N%ie" % (numberElectrons)
            graphicFilepath = os.path.join(figurePath, graphicName+'.png')
            plt.savefig(graphicFilepath)

        plt.figure()
        title = r"Number of electrons"
        plt.title(title)
        for numberElectrons in numberElectronsList:

            spectrum = results[numberElectrons]

            energies_keV = np.array(spectrum.energies_keV)
            backgrounds = np.array(spectrum.backgroundIntensities)

            label = "N=%i" % (numberElectrons)
            plt.semilogy(energies_keV, backgrounds, label=label)

        plt.xlabel(r"$E_{X}$ (keV)")
        plt.ylabel("Counts")

        plt.legend(loc='best')

        graphicName = "BackgroundSpectrum_NumberElectrons"
        graphicFilepath = os.path.join(figurePath, graphicName+'.png')
        plt.savefig(graphicFilepath)

        # Characteristic spectrum
        for numberElectrons in numberElectronsList:
            plt.figure()
            title = r"N = %i electrons" % (numberElectrons)
            plt.title(title)

            spectrum = results[numberElectrons]

            energies_keV = np.array(spectrum.energies_keV)
            intensities = np.array(spectrum.intensities)
            backgrounds = np.array(spectrum.backgroundIntensities)

            plt.plot(energies_keV, intensities-backgrounds)

            plt.xlabel(r"$E_{X}$ (keV)")
            plt.ylabel("Counts")

            graphicName = "CharacteristicSpectrum_N%ie" % (numberElectrons)
            graphicFilepath = os.path.join(figurePath, graphicName+'.png')
            plt.savefig(graphicFilepath)

        plt.figure()
        title = r"Number of electrons"
        plt.title(title)
        for numberElectrons in numberElectronsList:

            spectrum = results[numberElectrons]

            energies_keV = np.array(spectrum.energies_keV)
            intensities = np.array(spectrum.intensities)
            backgrounds = np.array(spectrum.backgroundIntensities)

            label = "N=%i" % (numberElectrons)
            plt.plot(energies_keV, (intensities-backgrounds), label=label)

        plt.xlabel(r"$E_{X}$ (keV)")
        plt.ylabel("Counts")

        plt.legend(loc='best')

        graphicName = "CharacteristicSpectrum_NumberElectrons"
        graphicFilepath = os.path.join(figurePath, graphicName+'.png')
        plt.savefig(graphicFilepath)

class SimulationsBremsstrahlungModel(SimulationsBulk):
    def _initData(self):
        self._atomicNumbers = [6, 13, 29, 47, 79, 92]

        self._energies_keV = [1.0, 5.0, 10.0, 20.0, 30.0, 40.0]
        self._numberElectrons = 100000
        self._numberPhotons = 1000000

        self._bremsstrahlungModels = []
        self._bremsstrahlungModels.append(MCXRayModel.XRayCSBremsstrahlungModel.TYPE_BETHE_HEITLER)
        self._bremsstrahlungModels.append(MCXRayModel.XRayCSBremsstrahlungModel.TYPE_KIRKPATRICK_WIEDMAN)
        self._bremsstrahlungModels.append(MCXRayModel.XRayCSBremsstrahlungModel.TYPE_DING)
        #self._bremsstrahlungModels.append(MCXRayModel.XRayCSBremsstrahlungModel.TYPE_GAUVIN)

    def getAnalysisName(self):
        return "BremsstrahlungModel"

    def generateInputFiles(self, batchFile):
        logging.info("generateInputFiles for analysis: %s", self.getAnalysisName())

        numberSimulations = 0
        numberSimulationsTodo = 0
        numberSimulationsDone = 0
        simulationTodoNames = []

        inputPath = os.path.join(self.getSimulationsPath(), "input")
        inputPath = Files.createPath(inputPath)

        for model in self._bremsstrahlungModels:
            for energy_keV in self._energies_keV:
                for atomicNumber in self._atomicNumbers:
                    simulation = Simulation.Simulation(overwrite=self._overwrite)
                    label = "_BM%i" % (model)
                    simulation.basename = self.getAnalysisName() + label

                    simulation.energy_keV = energy_keV
                    simulation.numberElectrons = self._numberElectrons
                    simulation.numberPhotons = self._numberPhotons
                    simulation.bremsstrahlungModel = model

                    simulation._specimen = Simulation.createPureBulkSample(atomicNumber)

                    simulation.createSimulationFiles(inputPath, self.getSimulationsPath())

                    if simulation.isDone(self.getSimulationsPath()):
                        numberSimulationsDone += 1
                    else:
                        numberSimulationsTodo += 1
                        simulationTodoNames.append(simulation.name)
                        filename = os.path.join("input", simulation.filename)
                        batchFile.addSimulationName(filename)
                    numberSimulations += 1

        #batchFile.write(self.getSimulationsPath())

        if self._verbose:
            for simulationTodoName in simulationTodoNames:
                logging.info("Todo: \t%s", simulationTodoName)

        percentage = 100.0*float(numberSimulationsDone)/float(numberSimulations)
        logging.info("Number of done: %4i/%i (%5.2f%%)", numberSimulationsDone, numberSimulations, percentage)
        percentage = 100.0*float(numberSimulationsTodo)/float(numberSimulations)
        logging.info("Number of todo: %4i/%i (%5.2f%%)", numberSimulationsTodo, numberSimulations, percentage)

    def readResultsFiles(self):
        logging.info("readResultsFiles")

    def analyzeResultsFiles(self):
        logging.info("analyzeResultsFiles")

class SimulationsNumberEnergyWindows(SimulationsBulk):
    def _initData(self):
        self._atomicNumbers = [6]

        self._energies_keV = [1.0, 5.0, 10.0, 20.0, 30.0, 40.0]
        self._numberElectrons = 100000
        self._numberPhotons = 1000000

        self._numberEnergyWindowsList = [32, 64, 128, 256, 512, 1024]

    def getAnalysisName(self):
        return "NumberEnergyWindows"

    def generateInputFiles(self, batchFile):
        logging.info("generateInputFiles for analysis: %s", self.getAnalysisName())

        numberSimulations = 0
        numberSimulationsTodo = 0
        numberSimulationsDone = 0
        simulationTodoNames = []

        inputPath = os.path.join(self.getSimulationsPath(), "input")
        inputPath = Files.createPath(inputPath)

        for numberEnergyWindows in self._numberEnergyWindowsList:
            for energy_keV in self._energies_keV:
                for atomicNumber in self._atomicNumbers:
                    simulation = Simulation.Simulation(overwrite=self._overwrite)
                    label = "_NEW%04i" % (numberEnergyWindows)
                    simulation.basename = self.getAnalysisName() + label

                    simulation.energy_keV = energy_keV
                    simulation.numberElectrons = self._numberElectrons
                    simulation.numberPhotons = self._numberPhotons
                    simulation.numberEnergyWindows = numberEnergyWindows

                    simulation._specimen = Simulation.createPureBulkSample(atomicNumber)

                    simulation.createSimulationFiles(inputPath, self.getSimulationsPath())

                    if simulation.isDone(self.getSimulationsPath()):
                        numberSimulationsDone += 1
                    else:
                        numberSimulationsTodo += 1
                        simulationTodoNames.append(simulation.name)
                        filename = os.path.join("input", simulation.filename)
                        batchFile.addSimulationName(filename)
                    numberSimulations += 1

        #batchFile.write(self.getSimulationsPath())

        if self._verbose:
            for simulationTodoName in simulationTodoNames:
                logging.info("Todo: \t%s", simulationTodoName)

        percentage = 100.0*float(numberSimulationsDone)/float(numberSimulations)
        logging.info("Number of done: %4i/%i (%5.2f%%)", numberSimulationsDone, numberSimulations, percentage)
        percentage = 100.0*float(numberSimulationsTodo)/float(numberSimulations)
        logging.info("Number of todo: %4i/%i (%5.2f%%)", numberSimulationsTodo, numberSimulations, percentage)

    def readResultsFiles(self):
        logging.info("readResultsFiles")

        results = {}
        for energy_keV in self._energies_keV:
            results[energy_keV] = {}
            for atomicNumber in self._atomicNumbers:
                results[energy_keV][atomicNumber] = {}
                for numberEnergyWindows in self._numberEnergyWindowsList:
                    simulation = Simulation.Simulation(overwrite=self._overwrite)
                    label = "_NEW%04i" % (numberEnergyWindows)
                    simulation.basename = self.getAnalysisName() + label

                    simulation.energy_keV = energy_keV
                    simulation.numberElectrons = self._numberElectrons
                    simulation.numberPhotons = self._numberPhotons
                    simulation.numberEnergyWindows = numberEnergyWindows

                    simulation._specimen = Simulation.createPureBulkSample(atomicNumber)

                    simulation.createSimulationFiles(inputPath, self.getSimulationsPath())

                    if simulation.isDone(self.getSimulationsPath()):
                        filepath = os.path.join(self.getSimulationsPath(), simulation.resultsBasename + "XABX.txt")
                        spectraFile = Spectra.Spectra()
                        spectraFile.read(filepath)

                        spectrum = spectraFile.getSpecimenSpectrum()
                        results[energy_keV][atomicNumber][numberEnergyWindows] = spectrum

        return results

    def analyzeResultsFiles(self):
        logging.info("analyzeResultsFiles")

        results = self.readResultsFiles()

        figurePath = os.path.join(self.getAnalyzesPath(), "figures")
        figurePath = Files.createPath(figurePath)

        # Complete spectrum
        for energy_keV in results:
            for atomicNumber in results[energy_keV]:
                plt.figure()
                title = r"Z = %i, E$_{0}$ = %.1f keV" % (atomicNumber, energy_keV)
                plt.title(title)

                for numberEnergyWindows in sorted(results[energy_keV][atomicNumber]):
                    spectrum = results[energy_keV][atomicNumber][numberEnergyWindows]

                    energies_keV = np.array(spectrum.energies_keV)
                    intensities = np.array(spectrum.intensities)
                    backgroundIntensities = np.array(spectrum.backgroundIntensities)

                    label = "Nw=%i" % (numberEnergyWindows)
                    plt.semilogy(energies_keV, backgroundIntensities, label=label)

                plt.xlabel(r"$E_{X}$ (keV)")
                plt.ylabel("Counts")

                plt.legend(loc='best')

                graphicName = "CompleteSpectrum_%02i_E%03.1fkeV" % (atomicNumber, energy_keV)
                graphicFilepath = os.path.join(figurePath, graphicName+'.png')
                plt.savefig(graphicFilepath)

                plt.figure()
                title = r"Z = %i, E$_{0}$ = %.1f keV" % (atomicNumber, energy_keV)
                plt.title(title)

                for numberEnergyWindows in sorted(results[energy_keV][atomicNumber]):
                    spectrum = results[energy_keV][atomicNumber][numberEnergyWindows]

                    energies_keV = np.array(spectrum.energies_keV)
                    intensities = np.array(spectrum.intensities)
                    backgroundIntensities = np.array(spectrum.backgroundIntensities)

                    label = "Nw=%i" % (numberEnergyWindows)
                    plt.semilogy(energies_keV, backgroundIntensities/numberEnergyWindows, label=label)

                plt.xlabel(r"$E_{X}$ (keV)")
                plt.ylabel("Counts/Number of windows")

                plt.legend(loc='best')

                graphicName = "CompleteSpectrumNormalized_%02i_E%03.1fkeV" % (atomicNumber, energy_keV)
                graphicFilepath = os.path.join(figurePath, graphicName+'.png')
                plt.savefig(graphicFilepath)

        plt.show()

class SimulationsNumberEnergyChannels(SimulationsBulk):
    def _initData(self):
        self._atomicNumbers = [6, 13, 29, 47, 79, 92]

        self._energies_keV = [1.0, 5.0, 10.0, 20.0, 30.0, 40.0]
        self._numberElectrons = 100000
        self._numberPhotons = 1000000

        self._numberEnergyChannelsList = [512, 1024, 2048]

    def getAnalysisName(self):
        return "NumberEnergyChannels"

    def generateInputFiles(self, batchFile):
        logging.info("generateInputFiles for analysis: %s", self.getAnalysisName())

        numberSimulations = 0
        numberSimulationsTodo = 0
        numberSimulationsDone = 0
        simulationTodoNames = []

        inputPath = os.path.join(self.getSimulationsPath(), "input")
        inputPath = Files.createPath(inputPath)

        for numberEnergyChannels in self._numberEnergyChannelsList:
            for energy_keV in self._energies_keV:
                for atomicNumber in self._atomicNumbers:
                    simulation = Simulation.Simulation(overwrite=self._overwrite)
                    label = "_NEW%04i" % (numberEnergyChannels)
                    simulation.basename = self.getAnalysisName() + label

                    simulation.energy_keV = energy_keV
                    simulation.numberElectrons = self._numberElectrons
                    simulation.numberPhotons = self._numberPhotons
                    simulation.numberEnergyChannels = numberEnergyChannels

                    simulation._specimen = Simulation.createPureBulkSample(atomicNumber)

                    simulation.createSimulationFiles(inputPath, self.getSimulationsPath())

                    if simulation.isDone(self.getSimulationsPath()):
                        numberSimulationsDone += 1
                    else:
                        numberSimulationsTodo += 1
                        simulationTodoNames.append(simulation.name)
                        filename = os.path.join("input", simulation.filename)
                        batchFile.addSimulationName(filename)
                    numberSimulations += 1

        #batchFile.write(self.getSimulationsPath())

        if self._verbose:
            for simulationTodoName in simulationTodoNames:
                logging.info("Todo: \t%s", simulationTodoName)

        percentage = 100.0*float(numberSimulationsDone)/float(numberSimulations)
        logging.info("Number of done: %4i/%i (%5.2f%%)", numberSimulationsDone, numberSimulations, percentage)
        percentage = 100.0*float(numberSimulationsTodo)/float(numberSimulations)
        logging.info("Number of todo: %4i/%i (%5.2f%%)", numberSimulationsTodo, numberSimulations, percentage)

    def readResultsFiles(self):
        logging.info("readResultsFiles")

        results = {}
        for energy_keV in self._energies_keV:
            results[energy_keV] = {}
            for atomicNumber in self._atomicNumbers:
                results[energy_keV][atomicNumber] = {}
                for numberEnergyChannels in self._numberEnergyChannelsList:
                    simulation = Simulation.Simulation(overwrite=self._overwrite)
                    label = "_NEW%04i" % (numberEnergyChannels)
                    simulation.basename = self.getAnalysisName() + label

                    simulation.energy_keV = energy_keV
                    simulation.numberElectrons = self._numberElectrons
                    simulation.numberPhotons = self._numberPhotons
                    simulation.numberEnergyChannels = numberEnergyChannels

                    simulation._specimen = Simulation.createPureBulkSample(atomicNumber)

                    simulation.createSimulationFiles(inputPath, self.getSimulationsPath())

                    if simulation.isDone(self.getSimulationsPath()):
                        filepath = os.path.join(self.getSimulationsPath(), simulation.resultsBasename + "XABX.txt")
                        spectraFile = Spectra.Spectra()
                        spectraFile.read(filepath)

                        spectrum = spectraFile.getSpecimenSpectrum()
                        results[energy_keV][atomicNumber][numberEnergyChannels] = spectrum

        return results

    def analyzeResultsFiles(self):
        logging.info("analyzeResultsFiles")

        results = self.readResultsFiles()

        figurePath = os.path.join(self.getAnalyzesPath(), "figures")
        figurePath = Files.createPath(figurePath)

        # Complete spectrum
        for energy_keV in results:
            for atomicNumber in results[energy_keV]:
                plt.figure()
                title = r"Z = %i, E$_{0}$ = %.1f keV" % (atomicNumber, energy_keV)
                plt.title(title)

                for numberEnergyWindows in sorted(results[energy_keV][atomicNumber]):
                    spectrum = results[energy_keV][atomicNumber][numberEnergyWindows]

                    energies_keV = np.array(spectrum.energies_keV)
                    intensities = np.array(spectrum.intensities)
                    backgroundIntensities = np.array(spectrum.backgroundIntensities)

                    label = "Nw=%i" % (numberEnergyWindows)
                    plt.semilogy(energies_keV, backgroundIntensities, label=label)

                plt.xlabel(r"$E_{X}$ (keV)")
                plt.ylabel("Counts")

                plt.legend(loc='best')

                graphicName = "CompleteSpectrum_%02i_E%03.1fkeV" % (atomicNumber, energy_keV)
                graphicFilepath = os.path.join(figurePath, graphicName+'.png')
                plt.savefig(graphicFilepath)

                plt.figure()
                title = r"Z = %i, E$_{0}$ = %.1f keV" % (atomicNumber, energy_keV)
                plt.title(title)

                for numberEnergyChannels in sorted(results[energy_keV][atomicNumber]):
                    spectrum = results[energy_keV][atomicNumber][numberEnergyChannels]

                    energies_keV = np.array(spectrum.energies_keV)
                    intensities = np.array(spectrum.intensities)
                    backgroundIntensities = np.array(spectrum.backgroundIntensities)

                    label = "Nw=%i" % (numberEnergyWindows)
                    plt.semilogy(energies_keV, backgroundIntensities/numberEnergyChannels, label=label)

                plt.xlabel(r"$E_{X}$ (keV)")
                plt.ylabel("Counts/Number of windows")

                plt.legend(loc='best')

                graphicName = "CompleteSpectrumNormalized_%02i_E%03.1fkeV" % (atomicNumber, energy_keV)
                graphicFilepath = os.path.join(figurePath, graphicName+'.png')
                plt.savefig(graphicFilepath)

        plt.show()

class SimulationsSpectrumInterpolationModel(SimulationsBulk):
    def _initData(self):
        self._atomicNumbers = [6, 13, 29, 47, 79, 92]

        self._energies_keV = [1.0, 5.0, 10.0, 20.0, 30.0, 40.0]
        self._numberElectrons = 100000
        self._numberPhotons = 1000000

        self._models = []
        self._models.append(MCXRayModel.SpectrumInterpolationModel.TYPE_COPY)
        self._models.append(MCXRayModel.SpectrumInterpolationModel.TYPE_LINEAR)
        self._models.append(MCXRayModel.SpectrumInterpolationModel.TYPE_LINEAR_DOUBLE)
        self._models.append(MCXRayModel.SpectrumInterpolationModel.TYPE_SPLINE)
        self._models.append(MCXRayModel.SpectrumInterpolationModel.TYPE_SPLINE_BATCH)
        self._models.append(MCXRayModel.SpectrumInterpolationModel.TYPE_SPLINE_POINT)

    def getAnalysisName(self):
        return "SpectrumInterpolationModel"

    def generateInputFiles(self, batchFile):
        logging.info("generateInputFiles for analysis: %s", self.getAnalysisName())

        numberSimulations = 0
        numberSimulationsTodo = 0
        numberSimulationsDone = 0
        simulationTodoNames = []

        inputPath = os.path.join(self.getSimulationsPath(), "input")
        inputPath = Files.createPath(inputPath)

        for model in self._models:
            for energy_keV in self._energies_keV:
                for atomicNumber in self._atomicNumbers:
                    simulation = Simulation.Simulation(overwrite=self._overwrite)
                    label = "_SIM%i" % (model)
                    simulation.basename = self.getAnalysisName() + label

                    simulation.energy_keV = energy_keV
                    simulation.numberElectrons = self._numberElectrons
                    simulation.numberPhotons = self._numberPhotons
                    simulation.spectrumInterpolationModel = model

                    simulation._specimen = Simulation.createPureBulkSample(atomicNumber)

                    simulation.createSimulationFiles(inputPath, self.getSimulationsPath())

                    if simulation.isDone(self.getSimulationsPath()):
                        numberSimulationsDone += 1
                    else:
                        numberSimulationsTodo += 1
                        simulationTodoNames.append(simulation.name)
                        filename = os.path.join("input", simulation.filename)
                        batchFile.addSimulationName(filename)
                    numberSimulations += 1

        #batchFile.write(self.getSimulationsPath())

        if self._verbose:
            for simulationTodoName in simulationTodoNames:
                logging.info("Todo: \t%s", simulationTodoName)

        percentage = 100.0*float(numberSimulationsDone)/float(numberSimulations)
        logging.info("Number of done: %4i/%i (%5.2f%%)", numberSimulationsDone, numberSimulations, percentage)
        percentage = 100.0*float(numberSimulationsTodo)/float(numberSimulations)
        logging.info("Number of todo: %4i/%i (%5.2f%%)", numberSimulationsTodo, numberSimulations, percentage)

    def readResultsFiles(self):
        logging.info("readResultsFiles")

    def analyzeResultsFiles(self):
        logging.info("analyzeResultsFiles")

class SimulationsAlloy(SimulationsBulk):
    def _initData(self):
        self._elementsList = [[(13, 0.1), (12, 0.9)],
                              [(13, 0.2), (12, 0.8)],
                              [(13, 0.3), (12, 0.7)],
                              [(13, 0.4), (12, 0.6)],
                              [(13, 0.5), (12, 0.5)],
                              [(13, 0.6), (12, 0.4)],
                              [(13, 0.7), (12, 0.3)],
                              [(13, 0.8), (12, 0.2)],
                              [(13, 0.9), (12, 0.1)],
                              [(12, 0.5), (30, 0.5)],
                              [(47, 0.5), (79, 0.5)],
                              [(29, 0.5), (79, 0.5)]]

        self._energy_keV = 5.0
        self._numberElectrons = 100000
        self._numberPhotons = 1000000

    def getAnalysisName(self):
        return "SimulationsAlloy"

    def generateInputFiles(self, batchFile):
        logging.info("generateInputFiles for analysis: %s", self.getAnalysisName())

        numberSimulations = 0
        numberSimulationsTodo = 0
        numberSimulationsDone = 0
        simulationTodoNames = []

        inputPath = os.path.join(self.getSimulationsPath(), "input")
        inputPath = Files.createPath(inputPath)

        specimens = self._createSpecimen()

        for specimen in specimens:
            simulation = Simulation.Simulation(overwrite=self._overwrite)
            label = "_%s" % (specimen.name)
            simulation.basename = self.getAnalysisName() + label

            simulation.energy_keV = self._energy_keV
            simulation.numberElectrons = self._numberElectrons
            simulation.numberPhotons = self._numberPhotons

            simulation._specimen = specimen

            simulation.createSimulationFiles(inputPath, self.getSimulationsPath())

            if simulation.isDone(self.getSimulationsPath()):
                numberSimulationsDone += 1
            else:
                numberSimulationsTodo += 1
                simulationTodoNames.append(simulation.name)
                filename = os.path.join("input", simulation.filename)
                batchFile.addSimulationName(filename)
            numberSimulations += 1

        #batchFile.write(self.getSimulationsPath())

        if self._verbose:
            for simulationTodoName in simulationTodoNames:
                logging.info("Todo: \t%s", simulationTodoName)

        percentage = 100.0*float(numberSimulationsDone)/float(numberSimulations)
        logging.info("Number of done: %4i/%i (%5.2f%%)", numberSimulationsDone, numberSimulations, percentage)
        percentage = 100.0*float(numberSimulationsTodo)/float(numberSimulations)
        logging.info("Number of todo: %4i/%i (%5.2f%%)", numberSimulationsTodo, numberSimulations, percentage)

    def _createSpecimen(self):
        specimens = []

        for elements in self._elementsList:
                specimen = Simulation.createAlloyBulkSample(elements)
                specimens.append(specimen)

        return specimens

    def readResultsFiles(self):
        logging.info("readResultsFiles")

        results = {}
        for repetitionID in range(1, self._repetitions+1):
            simulation = Simulation.Simulation(overwrite=self._overwrite)
            label = "_X%02i" % (repetitionID)
            simulation.basename = self.getAnalysisName() + label

            simulation.energy_keV = self._energy_keV
            simulation.numberElectrons = self._numberElectrons
            simulation.numberPhotons = self._numberPhotons

            simulation._specimen = Simulation.createPureBulkSample(self._atomicNumber)

            simulation.createSimulationFiles(inputPath, self.getSimulationsPath())

            if simulation.isDone(self.getSimulationsPath()):
                filepath = os.path.join(self.getSimulationsPath(), simulation.resultsBasename + "XABX.txt")
                spectraFile = Spectra.Spectra()
                spectraFile.read(filepath)

                spectrum = spectraFile.getSpecimenSpectrum()
                results[repetitionID] = spectrum

        return results

    def analyzeResultsFiles(self):
        logging.info("analyzeResultsFiles")

        results = self.readResultsFiles()

        figurePath = os.path.join(self.getAnalyzesPath(), "figures")
        figurePath = Files.createPath(figurePath)

        # Complete spectrum
        plt.figure()
        plt.title("Complete")

        for repetitionID in sorted(results.keys()):
            spectrum = results[repetitionID]
            energies_keV = np.array(spectrum.energies_keV)
            intensities = np.array(spectrum.intensities)

            label = "%02i" % (repetitionID)
            plt.semilogy(energies_keV, intensities, label=label)

        plt.xlabel(r"$E_{X}$ (keV)")
        plt.ylabel("Counts")

        plt.legend(loc='best')

        graphicName = "CompleteSpectrum"
        graphicFilepath = os.path.join(figurePath, graphicName+'.png')
        plt.savefig(graphicFilepath)

        # Background spectrum
        plt.figure()
        plt.title("Background")

        for repetitionID in sorted(results.keys()):
            spectrum = results[repetitionID]
            energies_keV = np.array(spectrum.energies_keV)
            intensities = np.array(spectrum.intensities)
            backgrounds = np.array(spectrum.backgroundIntensities)

            label = "%02i" % (repetitionID)
            plt.semilogy(energies_keV, backgrounds, label=label)

        plt.xlabel(r"$E_{X}$ (keV)")
        plt.ylabel("Counts")

        plt.legend(loc='best')

        graphicName = "BackgroundSpectrum"
        graphicFilepath = os.path.join(figurePath, graphicName+'.png')
        plt.savefig(graphicFilepath)

        # Characteristic spectrum
        plt.figure()
        plt.title("Characteristic")

        for repetitionID in sorted(results.keys()):
            spectrum = results[repetitionID]
            energies_keV = np.array(spectrum.energies_keV)
            intensities = np.array(spectrum.intensities)
            backgrounds = np.array(spectrum.backgroundIntensities)

            label = "%02i" % (repetitionID)
            plt.plot(energies_keV, intensities-backgrounds, label=label)

        plt.xlabel(r"$E_{X}$ (keV)")
        plt.ylabel("Counts")

        plt.legend(loc='best')

        graphicName = "CharacteristicSpectrum"
        graphicFilepath = os.path.join(figurePath, graphicName+'.png')
        plt.savefig(graphicFilepath)

        # Difference spectrum
        plt.figure()
        plt.title("Difference")

        repetitionIDs = sorted(results.keys())
        if len(repetitionIDs) > 0:
            spectrum = results[repetitionIDs[0]]
            intensitiesRef = np.array(spectrum.intensities)
            for repetitionID in repetitionIDs[1:]:
                spectrum = results[repetitionID]
                energies_keV = np.array(spectrum.energies_keV)
                intensities = np.array(spectrum.intensities)

                label = "01 - %02i" % (repetitionID)
                plt.plot(energies_keV, intensitiesRef-intensities, label=label)

            plt.xlabel(r"$E_{X}$ (keV)")
            plt.ylabel("Counts")

            plt.legend(loc='best')

            graphicName = "DifferenceSpectrum"
            graphicFilepath = os.path.join(figurePath, graphicName+'.png')
            plt.savefig(graphicFilepath)

            # Difference relative spectrum
            plt.figure()
            plt.title("Difference Relative")

            repetitionIDs = sorted(results.keys())
            spectrum = results[repetitionIDs[0]]
            intensitiesRef = np.array(spectrum.intensities)
            for repetitionID in repetitionIDs[1:]:
                spectrum = results[repetitionID]
                energies_keV = np.array(spectrum.energies_keV)
                intensities = np.array(spectrum.intensities)

                label = "01 - %02i" % (repetitionID)
                plt.plot(energies_keV, (intensitiesRef-intensities)/intensitiesRef, label=label)

            plt.xlabel(r"$E_{X}$ (keV)")
            plt.ylabel("Fraction")

            plt.legend(loc='best')

            graphicName = "DifferenceRelativeSpectrum"
            graphicFilepath = os.path.join(figurePath, graphicName+'.png')
            plt.savefig(graphicFilepath)

            #plt.show()

class SimulationsPhirhoz(SimulationsBulk):
    def _initData(self):
        self._numberElectrons = 10000

        self._energies_keV = {}

        """
        Cr Ka in Al: 10 and 12 keV for tracer thickness of 4 and 12 ug/cm2
        """
        self._energies_keV[24] = [10.0, 12.0]

        self._atomicNumberMatrixList = {}
        self._atomicNumberMatrixList[24] = 13
        self._tracerThicknesses_nm = {}
        factor_ug_cm2_to_nm = 10.0/7.19
        self._tracerThicknesses_nm[24] = [int(4.0*factor_ug_cm2_to_nm), int(12.0*factor_ug_cm2_to_nm)]
        self._maximumThickness_nm = int(400.0*factor_ug_cm2_to_nm)

#        """
#        Zn Ka in Cu at 20 and 30 keV
#        """
#        self._energies_keV[30] = [20.0, 30.0]
#
#        """
#        Si Ka in Au 10 and 30 keV
#        """
#        self._energies_keV[14] = [10.0, 30.0]


    def getAnalysisName(self):
        return "SimulationsPhirhoz"

    def generateInputFiles(self, batchFile):
        logging.info("generateInputFiles for analysis: %s", self.getAnalysisName())

        numberSimulations = 0
        numberSimulationsTodo = 0
        numberSimulationsDone = 0
        simulationTodoNames = []

        inputPath = os.path.join(self.getSimulationsPath(), "input")
        inputPath = Files.createPath(inputPath)

        for atomicNumberTracer in self._energies_keV:
            atomicNumberMatrix = self._atomicNumberMatrixList[atomicNumberTracer]
            for tracerThickness_nm in self._tracerThicknesses_nm[24]:
                specimens = Simulation.createPhirhozSpecimens(atomicNumberTracer, atomicNumberMatrix, tracerThickness_nm, self._maximumThickness_nm)
                for specimen in specimens:
                    energies_keV = self._energies_keV[atomicNumberTracer]
                    for energy_keV in energies_keV:
                        simulation = Simulation.Simulation(overwrite=self._overwrite)
                        simulation.basename = self.getAnalysisName()

                        simulation.energy_keV = energy_keV
                        simulation.numberElectrons = self._numberElectrons

                        simulation._specimen = specimen

                        simulation.createSimulationFiles(inputPath, self.getSimulationsPath())

                        if simulation.isDone(self.getSimulationsPath()):
                            numberSimulationsDone += 1
                        else:
                            numberSimulationsTodo += 1
                            simulationTodoNames.append(simulation.name)
                            filename = os.path.join("input", simulation.filename)
                            batchFile.addSimulationName(filename)
                        numberSimulations += 1

        if self._verbose:
            for simulationTodoName in simulationTodoNames:
                logging.info("Todo: \t%s", simulationTodoName)

        if numberSimulations != 0:
            percentage = 100.0*float(numberSimulationsDone)/float(numberSimulations)
        else:
            percentage = 100
        logging.info("Number of done: %4i/%i (%5.2f%%)", numberSimulationsDone, numberSimulations, percentage)
        if numberSimulations != 0:
            percentage = 100.0*float(numberSimulationsTodo)/float(numberSimulations)
        else:
            percentage = 100
        logging.info("Number of todo: %4i/%i (%5.2f%%)", numberSimulationsTodo, numberSimulations, percentage)

    def analyzeResultsFiles(self):
        logging.info("analyzeResultsFiles")

        figurePath = os.path.join(self.getAnalyzesPath(), "figures")
        figurePath = Files.createPath(figurePath)

        # Isolated layer.
        filmIntensityCr_K = {}

        thickness_nm = 5.0
        filename = "SimulationsComplexPhiRhoZ_Cr100T50A_IsolatedLayer_E10d0keV_Spectra.txt"
        filepath = os.path.join(self.getSimulationsPath(), "Results", filename)
        spectraFile = Spectra.Spectra()
        spectraFile.read(filepath)

        regionID = 0
        elementSpectrumCr = spectraFile.getElementSpectrum(regionID=regionID, elementName="Chromium")
        energies_keV = np.array(elementSpectrumCr.energies_keV)
        intensitiesCr = np.array(elementSpectrumCr.intensities)
        intensitiesCr_K = np.zeros_like(energies_keV)
        eMin_keV = 5.0
        eMax_keV = np.max(energies_keV)
        maskArray = np.ma.masked_inside(energies_keV, eMin_keV, eMax_keV)
        intensitiesCr_K[maskArray.mask] += intensitiesCr[maskArray.mask]
        filmIntensityCr_K[thickness_nm] = np.sum(intensitiesCr_K)

        thickness_nm = 16.0
        filename = "SimulationsComplexPhiRhoZ_Cr100T160A_IsolatedLayer_E10d0keV_Spectra.txt"
        filepath = os.path.join(self.getSimulationsPath(), "Results", filename)
        spectraFile = Spectra.Spectra()
        spectraFile.read(filepath)

        regionID = 0
        elementSpectrumCr = spectraFile.getElementSpectrum(regionID=regionID, elementName="Chromium")
        energies_keV = np.array(elementSpectrumCr.energies_keV)
        intensitiesCr = np.array(elementSpectrumCr.intensities)
        intensitiesCr_K = np.zeros_like(energies_keV)
        eMin_keV = 5.0
        eMax_keV = np.max(energies_keV)
        maskArray = np.ma.masked_inside(energies_keV, eMin_keV, eMax_keV)
        intensitiesCr_K[maskArray.mask] += intensitiesCr[maskArray.mask]
        filmIntensityCr_K[thickness_nm] = np.sum(intensitiesCr_K)

        # SimulationsComplexPhiRhoZ_Cr_T5nm_Z0nm_Al_E10d0keV
        intensityCr_K = {}
        depths_nm = {}

        patterns = "SimulationsComplexPhiRhoZ_Cr_*_E10d0keV_Spectra.txt"
        path = os.path.join(self.getSimulationsPath(), "Results")
        for filepath in Files.findAllFiles(path, patterns):
            thickness_nm, position_nm = self._extractParametersFromFilepath(filepath)

            intensityCr_K.setdefault(thickness_nm, [])
            depths_nm.setdefault(thickness_nm, [])

            spectraFile = Spectra.Spectra()
            spectraFile.read(filepath)
            regionID = 1
            elementSpectrumCr = spectraFile.getElementSpectrum(regionID=regionID, elementName="Chromium")
            energies_keV = np.array(elementSpectrumCr.energies_keV)
            intensitiesCr = np.array(elementSpectrumCr.intensities)
            intensitiesCr_K = np.zeros_like(energies_keV)
            eMin_keV = 5.0
            eMax_keV = np.max(energies_keV)
            maskArray = np.ma.masked_inside(energies_keV, eMin_keV, eMax_keV)
            intensitiesCr_K[maskArray.mask] += intensitiesCr[maskArray.mask]
            intensityCr_K[thickness_nm].append(np.sum(intensitiesCr_K))

            depths_nm[thickness_nm].append(position_nm)

        for thickness_nm in depths_nm:
            plt.figure()
            plt.title(thickness_nm)

            x, y = Sorting.sortXYs(depths_nm[thickness_nm], intensityCr_K[thickness_nm])
            x = np.array(x)
            y = np.array(y)/filmIntensityCr_K[thickness_nm]
            plt.plot(x, y)

        plt.show()

    def _extractParametersFromFilepath(self, filepath):
        # SimulationsComplexPhiRhoZ_Cr_T5nm_Z0nm_Al_E10d0keV.txt
        basename = os.path.basename(filepath)
        items = basename.split('_')
        thickness_nm = float(items[2][1:-2])
        position_nm = float(items[3][1:-2])

        return thickness_nm, position_nm

class SimulationsParticle(SimulationsBulk):
    def _initData(self):
        self._particleRadiusList_nm = []
        self._particleRadiusList_nm.extend([100.0, 250.0, 500.0])
        self._particleRadiusList_nm.extend(np.arange(0.1, 1.0, 0.1).tolist())
        self._particleRadiusList_nm.extend(np.arange(1.0, 10.0, 1.0).tolist())
        self._particleRadiusList_nm.extend(np.arange(10.0, 100.0, 10.0).tolist())

        self._particleRadiusList_nm = [d_nm/2.0 for d_nm in [0.2, 1.0, 10.0, 100.0, 200.0]]

        self._energies_keV = []
        self._energies_keV.extend(np.arange(1.0, 10.0, 1.0).tolist())
        self._energies_keV.extend(np.arange(10.0, 60.0, 1.0).tolist())
        self._numberElectrons = 10000
        self._numberPhotons = 1000

    def getAnalysisName(self):
        return "SimulationsParticle"

    def generateInputFiles(self, batchFile):
        logging.info("generateInputFiles for analysis: %s", self.getAnalysisName())

        numberSimulations = 0
        numberSimulationsTodo = 0
        numberSimulationsDone = 0
        simulationTodoNames = []

        inputPath = os.path.join(self.getSimulationsPath(), "input")
        inputPath = Files.createPath(inputPath)

        specimens  = self._generateSpecimens()

        for specimen in specimens:
            for energy_keV in self._energies_keV:
                simulation = Simulation.Simulation(overwrite=self._overwrite)
                simulation.basename = self.getAnalysisName()

                simulation.energy_keV = energy_keV
                simulation.numberElectrons = self._numberElectrons
                simulation.numberPhotons = self._numberPhotons

                simulation._specimen = specimen

                simulation.createSimulationFiles(inputPath, self.getSimulationsPath())

                if simulation.isDone(self.getSimulationsPath()):
                    numberSimulationsDone += 1
                else:
                    numberSimulationsTodo += 1
                    simulationTodoNames.append(simulation.name)
                    filename = os.path.join("input", simulation.filename)
                    batchFile.addSimulationName(filename)
                numberSimulations += 1

        if self._verbose:
            for simulationTodoName in simulationTodoNames:
                logging.info("Todo: \t%s", simulationTodoName)

        percentage = 100.0*float(numberSimulationsDone)/float(numberSimulations)
        logging.info("Number of done: %4i/%i (%5.2f%%)", numberSimulationsDone, numberSimulations, percentage)
        percentage = 100.0*float(numberSimulationsTodo)/float(numberSimulations)
        logging.info("Number of todo: %4i/%i (%5.2f%%)", numberSimulationsTodo, numberSimulations, percentage)

    def _generateSpecimens(self):
        atomicNumberSubstrate = 13
        elementsParticle = [(40, 0.91025), (13, 0.08975)]
        specimens = []

        for particleRadius_nm in self._particleRadiusList_nm:
            specimen = Simulation.createAlloyParticleInSubstrate(elementsParticle, atomicNumberSubstrate, particleRadius_nm)
            specimens.append(specimen)

        return specimens

    def readResultsFiles(self):
        logging.info("readResultsFiles")

        seriliazationFile = SerializationPickle.SerializationPickle()
        filepath = os.path.join(self.getSimulationsPath(), self.getAnalysisName()+".ser")
        seriliazationFile.setFilepath(filepath)

        if seriliazationFile.isFile():
            results = seriliazationFile.load()
        else:
            results = {}

        specimens  = self._generateSpecimens()

        for specimen in specimens:
            for energy_keV in self._energies_keV:
                simulation = Simulation.Simulation(overwrite=self._overwrite)
                simulation.basename = self.getAnalysisName()

                simulation.energy_keV = energy_keV
                simulation.numberElectrons = self._numberElectrons
                simulation.numberPhotons = self._numberPhotons

                simulation._specimen = specimen

                simulation.createSimulationFiles(self.getSimulationsPath())

                if simulation.isDone(self.getSimulationsPath()):
                    filepath = os.path.join(self.getSimulationsPath(), simulation.resultsBasename + "_Spectra.txt")
                    if seriliazationFile.isOlderThan(filepath):
                        spectraFile = Spectra.Spectra()
                        spectraFile.read(filepath)

                        regionID = 1
                        specimenSpectrum = spectraFile.getSpecimenSpectrum()
                        particleSpectrum = spectraFile.getRegionSpectrum(regionID=1)
                        elementSpectrum = spectraFile.getElementSpectrum(regionID, "Zirconium")

                        assert len(specimenSpectrum.energies_keV) == len(particleSpectrum.energies_keV)
                        assert len(specimenSpectrum.energies_keV) == len(elementSpectrum.energies_keV)

                        key = (specimen.name, energy_keV)
                        results[key] = {}
                        results[key][RESULTS_SPECIMEN] = specimenSpectrum
                        results[key][RESULTS_PARTICLE] = particleSpectrum
                        results[key][RESULTS_PARTICLE_ELEMENT] = elementSpectrum

        seriliazationFile.backupFile()
        seriliazationFile.save(results)

        return results

    def analyzeResultsFiles(self):
        logging.info("analyzeResultsFiles")

        results = self.readResultsFiles()

        figurePath = os.path.join(self.getAnalyzesPath(), "figures")
        figurePath = Files.createPath(figurePath)

        #self._createAllSpectraFigures(figurePath, results)

        #self._createDminFigures(figurePath, results)

        self._createAbstractFigure1(figurePath, results)
        #self._createAbstractFigure2(figurePath, results)

class SimulationsFilm(SimulationsBulk):
    def _initData(self):
        self._atomicNumbersList = [(6, 79), (79, 6)]
        self._filmThickness_nm = [1.0, 10.0, 20.0, 50.0, 100.0]
        self._energies_keV = [1.0, 5.0, 10.0, 20.0, 30.0]
        self._numberElectrons = 100000
        self._numberPhotons = 1000000

    def getAnalysisName(self):
        return "SimulationsFilm"

    def generateInputFiles(self, batchFile):
        logging.info("generateInputFiles for analysis: %s", self.getAnalysisName())

        numberSimulations = 0
        numberSimulationsTodo = 0
        numberSimulationsDone = 0
        simulationTodoNames = []

        inputPath = os.path.join(self.getSimulationsPath(), "input")
        inputPath = Files.createPath(inputPath)

        specimens = self._createSpecimen()

        for specimen in specimens:
            for energy_keV in self._energies_keV:
                simulation = Simulation.Simulation(overwrite=self._overwrite)
                label = "_%s_E%ikeV" % (specimen.name, energy_keV)
                simulation.basename = self.getAnalysisName() + label

                simulation.energy_keV = energy_keV
                simulation.numberElectrons = self._numberElectrons
                simulation.numberPhotons = self._numberPhotons

                simulation._specimen = specimen

                simulation.createSimulationFiles(inputPath, self.getSimulationsPath())

                if simulation.isDone(self.getSimulationsPath()):
                    numberSimulationsDone += 1
                else:
                    numberSimulationsTodo += 1
                    simulationTodoNames.append(simulation.name)
                    filename = os.path.join("input", simulation.filename)
                    batchFile.addSimulationName(filename)
                numberSimulations += 1

        if self._verbose:
            for simulationTodoName in simulationTodoNames:
                logging.info("Todo: \t%s", simulationTodoName)

        percentage = 100.0*float(numberSimulationsDone)/float(numberSimulations)
        logging.info("Number of done: %4i/%i (%5.2f%%)", numberSimulationsDone, numberSimulations, percentage)
        percentage = 100.0*float(numberSimulationsTodo)/float(numberSimulations)
        logging.info("Number of todo: %4i/%i (%5.2f%%)", numberSimulationsTodo, numberSimulations, percentage)

    def _createSpecimen(self):
        specimens = []

        for atomicNumberFilm, atomicNumberSubstrate in self._atomicNumbersList:
            for filmThickness_nm in self._filmThickness_nm:
                specimen = Simulation.createFilmOverSubstrate(atomicNumberFilm, atomicNumberSubstrate, filmThickness_nm)
                specimens.append(specimen)

        return specimens

    def readResultsFiles(self):
        logging.info("readResultsFiles")

        results = {}
        for repetitionID in range(1, self._repetitions+1):
            simulation = Simulation.Simulation(overwrite=self._overwrite)
            label = "_X%02i" % (repetitionID)
            simulation.basename = self.getAnalysisName() + label

            simulation.energy_keV = self._energy_keV
            simulation.numberElectrons = self._numberElectrons
            simulation.numberPhotons = self._numberPhotons

            simulation._specimen = Simulation.createPureBulkSample(self._atomicNumber)

            simulation.createSimulationFiles(inputPath, self.getSimulationsPath())

            if simulation.isDone(self.getSimulationsPath()):
                filepath = os.path.join(self.getSimulationsPath(), simulation.resultsBasename + "XABX.txt")
                spectraFile = Spectra.Spectra()
                spectraFile.read(filepath)

                spectrum = spectraFile.getSpecimenSpectrum()
                results[repetitionID] = spectrum

        return results

def runBulk():
    configurationFilepath = Files.getCurrentModulePath(__file__, "../MCXRay_20120511.cfg")
    programName = Files.getMCXRayProgramName(configurationFilepath)
    batchFile = BatchFileConsole.BatchFileConsole("BatchSystemTests", programName, numberFiles=1)

    analyzes = []

    # Done.
    # Todo.

    analyze = SimulationsBulk(overwrite=False, relativePath=r"MCXRay/SystemTesting/MCXRay_20120511/SimulationsBulk", configurationFilepath=configurationFilepath)
    analyzes.append(analyze)

    analyze = SimulationsRepetitions(overwrite=False, relativePath=r"MCXRay/SystemTesting/MCXRay_20120511/SimulationsBulk", configurationFilepath=configurationFilepath)
    analyzes.append(analyze)

    analyze = SimulationsNumberElectrons(overwrite=False, relativePath=r"MCXRay/SystemTesting/MCXRay_20120511/SimulationsBulk", configurationFilepath=configurationFilepath)
    analyzes.append(analyze)

    analyze = SimulationsCurrentTime(overwrite=False, relativePath=r"MCXRay/SystemTesting/MCXRay_20120511/SimulationsBulk", configurationFilepath=configurationFilepath)
    analyzes.append(analyze)

    analyze = SimulationsBremsstrahlungModel(overwrite=False, relativePath=r"MCXRay/SystemTesting/MCXRay_20120511/SimulationsBulk", configurationFilepath=configurationFilepath)
    analyzes.append(analyze)

    analyze = SimulationsNumberEnergyWindows(overwrite=False, relativePath=r"MCXRay/SystemTesting/MCXRay_20120511/SimulationsBulk", configurationFilepath=configurationFilepath)
    analyzes.append(analyze)

    analyze = SimulationsNumberEnergyChannels(overwrite=False, relativePath=r"MCXRay/SystemTesting/MCXRay_20120511/SimulationsBulk", configurationFilepath=configurationFilepath)
    analyzes.append(analyze)

    analyze = SimulationsSpectrumInterpolationModel(overwrite=False, relativePath=r"MCXRay/SystemTesting/MCXRay_20120511/SimulationsBulk", configurationFilepath=configurationFilepath)
    analyzes.append(analyze)

    options = mcxray._getOptions()

    if options == mcxray.ANALYZE_TYPE_GENERATE_INPUT_FILE:
        for analyze in analyzes:
            analyze.generateInputFiles(batchFile)

        batchFile.write(analyze.getSimulationsPath())
    if options == mcxray.ANALYZE_TYPE_READ_RESULTS:
        for analyze in analyzes:
            analyze.readResultsFiles()
    if options == mcxray.ANALYZE_TYPE_ANALYZE_RESULTS:
        for analyze in analyzes:
            analyze.analyzeResultsFiles()

def runAlloy():
    configurationFilepath = Files.getCurrentModulePath(__file__, "../MCXRay_20120511.cfg")
    programName = Files.getMCXRayProgramName(configurationFilepath)
    batchFile = BatchFileConsole.BatchFileConsole("BatchSystemTests", programName, numberFiles=1)

    analyzes = []

    # Done.
    # Todo.

    analyze = SimulationsAlloy(overwrite=False, relativePath=r"MCXRay/SystemTesting/MCXRay_20120511/SimulationsAlloy", configurationFilepath=configurationFilepath)
    analyzes.append(analyze)

    options = mcxray._getOptions()

    if options == mcxray.ANALYZE_TYPE_GENERATE_INPUT_FILE:
        for analyze in analyzes:
            analyze.generateInputFiles(batchFile)

        batchFile.write(analyze.getSimulationsPath())
    if options == mcxray.ANALYZE_TYPE_READ_RESULTS:
        for analyze in analyzes:
            analyze.readResultsFiles()
    if options == mcxray.ANALYZE_TYPE_ANALYZE_RESULTS:
        for analyze in analyzes:
            analyze.analyzeResultsFiles()

def runGeometry():
    configurationFilepath = Files.getCurrentModulePath(__file__, "../MCXRay_20120511.cfg")
    programName = Files.getMCXRayProgramName(configurationFilepath)
    batchFile = BatchFileConsole.BatchFileConsole("BatchSystemTests", programName, numberFiles=8)

    analyzes = []

    # Done.
    # Todo.

    analyze = SimulationsPhirhoz(overwrite=False, relativePath=r"MCXRay/SystemTesting/MCXRay_20120511/SimulationsGeometry", configurationFilepath=configurationFilepath)
    analyzes.append(analyze)

    analyze = SimulationsParticle(overwrite=False, relativePath=r"MCXRay/SystemTesting/MCXRay_20120511/SimulationsGeometry", configurationFilepath=configurationFilepath)
    analyzes.append(analyze)

    analyze = SimulationsFilm(overwrite=False, relativePath=r"MCXRay/SystemTesting/MCXRay_20120511/SimulationsGeometry", configurationFilepath=configurationFilepath)
    analyzes.append(analyze)

    options = mcxray._getOptions()

    if options == mcxray.ANALYZE_TYPE_GENERATE_INPUT_FILE:
        for analyze in analyzes:
            analyze.generateInputFiles(batchFile)

        batchFile.write(analyze.getSimulationsPath())
    if options == mcxray.ANALYZE_TYPE_READ_RESULTS:
        for analyze in analyzes:
            analyze.readResultsFiles()
    if options == mcxray.ANALYZE_TYPE_ANALYZE_RESULTS:
        for analyze in analyzes:
            analyze.analyzeResultsFiles()

def run():
    runBulk()
    runAlloy()
    runGeometry()

if __name__ == '__main__': #pragma: no cover
    import pyHendrixDemersTools.Runner as Runner
    Runner.Runner().run(runFunction=run)
