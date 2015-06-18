#!/usr/bin/env python
"""
.. py:currentmodule:: MCXRay.BackgroundProblem.mcxray
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Base module to create and analuyze MCXRay simulations.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2012 Hendrix Demers"
__license__ = ""

# Standard library modules.
import os.path
import shutil
import time
import argparse
import logging
import zipfile
import stat
import math

# Third party modules.
import numpy as np

# Local modules.
import pyHendrixDemersTools.Files as Files
import pyHendrixDemersTools.serialization.SerializationPickle as SerializationPickle

# Project modules
import pymcxray.Simulation as Simulation
from pymcxray.SimulationsParameters import PARAMETER_SPECIMEN

# Globals and constants variables.
ANALYZE_TYPE_GENERATE_INPUT_FILE = "generate"
ANALYZE_TYPE_CHECK_PROGRESS = "check"
ANALYZE_TYPE_READ_RESULTS = "read"
ANALYZE_TYPE_ANALYZE_RESULTS = "analyze"

SAVE_EVERY_SIMULATIONS = 10

def _getOptions():
    analyzeTypes = []
    analyzeTypes.append(ANALYZE_TYPE_GENERATE_INPUT_FILE)
    analyzeTypes.append(ANALYZE_TYPE_CHECK_PROGRESS)
    analyzeTypes.append(ANALYZE_TYPE_READ_RESULTS)
    analyzeTypes.append(ANALYZE_TYPE_ANALYZE_RESULTS)

    parser = argparse.ArgumentParser(description='Analyze MCXRay x-ray background problem.')
    parser.add_argument('type', metavar='AnalyzeType', type=str, choices=analyzeTypes, nargs='?',
                        default=ANALYZE_TYPE_GENERATE_INPUT_FILE,
                        help='Type of analyze to do')

    args = parser.parse_args()
    logging.debug(args.type)

    return args.type

class _Simulations(object):
    SIMULATIONS_FOLDER = "simulations"
    RESULTS_FOLDER = os.path.join(SIMULATIONS_FOLDER, "Results")
    ANALYSES_FOLDER = "analyzes"
    INPUTS_FOLDER = "input"

    def __init__(self, simulationPath=None, basepath=None, relativePath=None, configurationFilepath=None):
        if configurationFilepath is None:
            self._configurationFilepath = Files.getCurrentModulePath(__file__, "../../pyMcGill.cfg")
        else:
            self._configurationFilepath = configurationFilepath
        self._output = None

        self.overwrite = True
        self.resetCache = False
        self.useSerialization = True
        self.verbose = True
        self.createBackup = True

        if simulationPath is not None:
            self._simulationPath = os.path.normpath(simulationPath)
        else:
            self._simulationPath = None

        if basepath is not None:
            self._basepath = os.path.normpath(basepath)
        else:
            self._basepath = None

        if relativePath is not None:
            self._relativePath = os.path.normpath(relativePath)
        else:
            self._relativePath = None

        self._createAllFolders(self.getSimulationPath())

        self._simulationResultsList = {}
        self._serializationExtension = '.ser'

    def getSimulationPath(self):
        try:
            if self._simulationPath is not None:
                return self._simulationPath
            elif self._relativePath is not None:
                path = Files.getResultsMcGillPath(self._configurationFilepath)
                path = os.path.join(path, "Simulations", self._relativePath)
            elif self._basepath is not None:
                name = self.getAnalysisName()
                path = Files.getResultsMcGillPath(self._configurationFilepath)
                path = os.path.join(path, "Simulations", self._basepath, "%s" % (name))
            else:
                name = self.getAnalysisName()
                path = Files.getResultsMcGillPath(self._configurationFilepath, "Simulations/%s" % (name))

            if not os.path.isdir(path):
                os.makedirs(path)
            return path
        except NotImplementedError:
            return None

    def getSimulationsPath(self):
        path = os.path.join(self.getSimulationPath(), self.SIMULATIONS_FOLDER)
        return path

    def getResultsPath(self):
        path = os.path.join(self.getSimulationPath(), self.RESULTS_FOLDER)
        return path

    def getAnalyzesPath(self):
        path = os.path.join(self.getSimulationPath(), self.ANALYSES_FOLDER)
        return path

    def getInputPath(self):
        inputPath = os.path.join(self.getSimulationsPath(), self.INPUTS_FOLDER)
        inputPath = Files.createPath(inputPath)

        return inputPath

    def _createAllFolders(self, basePath):
        if basePath is not None:
            if not os.path.isdir(basePath):
                os.makedirs(basePath)

            newPaths = [self.SIMULATIONS_FOLDER, self.RESULTS_FOLDER, self.ANALYSES_FOLDER]
            for newPath in newPaths:
                path = os.path.join(basePath, newPath)
                if not os.path.isdir(path):
                    os.makedirs(path)

    def _copyMCXRayProgramOld(self):
        basePath = Files.getMCXRayProgramPath(self._configurationFilepath)

        programName = Files.getMCXRayProgramName(self._configurationFilepath, default="McXRay.exe")
        sourceFilepath = os.path.join(basePath, programName)
        destinationPath = os.path.join(self.getSimulationsPath(), programName)

        #if self._overwrite or not os.path.isfile(destinationPath) or os.stat(sourceFilepath).st_mtime > os.stat(destinationPath).st_mtime:
        if self._overwrite or not os.path.isfile(destinationPath):
            shutil.copy2(sourceFilepath, destinationPath)

        optionFilenames = ["PhiRhoZPjm.txt", "MapPjm.txt", "SnrPjm.txt", "TomoPjm.txt"]
        for optionFilename in optionFilenames:
            sourceFilepath = os.path.join(basePath, optionFilename)
            if os.path.isfile(sourceFilepath):
                destinationPath = os.path.join(self.getSimulationsPath(), optionFilename)
                if self._overwrite or not os.path.isfile(destinationPath):
                    shutil.copy2(sourceFilepath, destinationPath)

        macPathName = "MACHenke"
        sourcePath = os.path.join(basePath, macPathName)
        destinationPath = os.path.join(self.getSimulationsPath(), macPathName)
        if self._overwrite or not os.path.isdir(destinationPath) or os.stat(sourceFilepath).st_mtime > os.stat(destinationPath).st_mtime:
            if os.path.isdir(destinationPath):
                shutil.rmtree(destinationPath)
                time.sleep(1)
            shutil.copytree(sourcePath, destinationPath)

    def _copyMCXRayProgram(self):
        archivesPath = Files.getMCXRayArchivePath(self._configurationFilepath)
        archiveFilename = Files.getMCXRayArchiveName(self._configurationFilepath)
        archiveFilepath = os.path.join(archivesPath, archiveFilename)

        destinationPath = self.getSimulationsPath()
        self._extractZipfile(archiveFilename, archiveFilepath, destinationPath)

    def _extractZipfile(self, archiveFilename, archiveFilepath, destinationPath):
        versionBasename, dummyExtension = os.path.splitext(archiveFilepath)
        versionFilename = versionBasename + ".txt"
        versionFilepath = os.path.join(destinationPath, versionFilename)

        logging.debug("Extracting archive %s to %s.", archiveFilepath, destinationPath)
        #shutil.rmtree(destinationPath, ignore_errors=True)

        if not os.path.isdir(destinationPath):
            self._createPath(destinationPath)

        destinationFilepath = os.path.join(destinationPath, archiveFilename)

        shutil.copy2(archiveFilepath, destinationFilepath)

        zipFile = zipfile.ZipFile(destinationFilepath, 'r')
        try:
            zipFile.extractall(destinationPath)
        except IOError as message:
            logging.error(message)
        zipFile.close()

        fileVersion = open(versionFilepath, 'w')
        fileVersion.write(versionBasename)
        fileVersion.close()

        try:
            os.remove(destinationFilepath)
        except WindowsError as message:
            logging.error(message)

    def logNumberSimulations(self):
        numberSimulations = 0
        numberSimulationsTodo = 0
        numberSimulationsDone = 0

        for simulation in self.getAllSimulationParameters():
            if simulation.isDone(self.getSimulationsPath()):
                numberSimulationsDone += 1
            else:
                numberSimulationsTodo += 1

            numberSimulations += 1

        percentage = 100.0*float(numberSimulationsDone)/float(numberSimulations)
        logging.info("Number of done: %4i/%i (%5.2f%%)", numberSimulationsDone, numberSimulations, percentage)
        percentage = 100.0*float(numberSimulationsTodo)/float(numberSimulations)
        logging.info("Number of todo: %4i/%i (%5.2f%%)", numberSimulationsTodo, numberSimulations, percentage)

    def generateInputFiles(self, batchFile):
        logging.info("generateInputFiles for analysis: %s", self.getAnalysisName())

        self._copyMCXRayProgram()

        numberSimulations = 0
        numberSimulationsTodo = 0
        numberSimulationsDone = 0
        simulationTodoNames = []

        for simulation in self.getAllSimulationParameters():
            simulation.createSimulationFiles(self.getInputPath(), self.getSimulationsPath())

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

    def checkProgress(self):
        numberSimulations = 0
        numberSimulationsTodo = 0
        numberSimulationsDone = 0
        simulationTodoNames = []

        inputPath = os.path.join(self.getSimulationsPath(), "input")
        inputPath = Files.createPath(inputPath)

        for simulation in self.getAllSimulationParameters():
            if simulation.isDone(self.getSimulationsPath()):
                numberSimulationsDone += 1
            else:
                numberSimulationsTodo += 1
                simulationTodoNames.append(simulation.name)
            numberSimulations += 1

        if self._verbose:
            for simulationTodoName in simulationTodoNames:
                logging.debug("Todo: \t%s", simulationTodoName)

        logging.info("Check progress for %s", self.getAnalysisName())
        percentage = 100.0*float(numberSimulationsDone)/float(numberSimulations)
        logging.info("Number of done: %4i/%i (%5.2f%%)", numberSimulationsDone, numberSimulations, percentage)
        percentage = 100.0*float(numberSimulationsTodo)/float(numberSimulations)
        logging.info("Number of todo: %4i/%i (%5.2f%%)", numberSimulationsTodo, numberSimulations, percentage)

    def getAllSimulationParameters(self):
        simulationParametersList = []

        for parameters in self._simulationsParameters.getAllSimulationParameters():
            simulation = Simulation.Simulation(overwrite=self._overwrite)
            simulation.basename = self.getAnalysisName()

            simulation.setParameters(parameters)

            if PARAMETER_SPECIMEN in parameters:
                simulation._specimen = parameters[PARAMETER_SPECIMEN]
            else:
                simulation._specimen = self.createSpecimen(parameters)

            simulation.generateBaseFilename()

            simulationParametersList.append(simulation)

        return simulationParametersList

    def _isAllResultFileExist(self, resultFilepath, simulationFilepath):
        resultSerializedFilepath = resultFilepath.replace('.cas', '_numpy.npz')

        if os.path.isfile(resultFilepath) and not self.isOlderThan(resultFilepath, simulationFilepath):
            logging.debug("Done: %s", resultFilepath)
            return True
        else:
            logging.debug("missing: %s", resultFilepath)

        if os.path.isfile(resultSerializedFilepath) and not self.isOlderThan(resultSerializedFilepath, simulationFilepath):
            logging.debug("Done: %s", resultSerializedFilepath)
            return True
        else:
            logging.debug("missing: %s", resultSerializedFilepath)

        return False

    def isOlderThan(self, resultFilepath, simulationFilepath):
        if not os.path.isfile(resultFilepath):
            return True

        statMainFile = os.stat(resultFilepath)
        statOtherFile = os.stat(simulationFilepath)

        if statOtherFile[stat.ST_MTIME] > statMainFile[stat.ST_MTIME]:
            return True
        elif statOtherFile[stat.ST_CTIME] > statMainFile[stat.ST_MTIME] and statOtherFile[stat.ST_CTIME] > statMainFile[stat.ST_CTIME]:
            return True
        else:
            return False

    def readResults(self, resultFilepaths=None, serializationFilename="", isResultsKeep=True):
        logging.info("readResults")

        self._readAllResults(serializationFilename, isResultsKeep)

    def _readAllResults(self, serializationFilename="", isResultsKeep=True):
        if self.useSerialization:
            if serializationFilename == "":
                serializationFilename = self.getAnalysisName() + ".ser"
            self._readAllResultsSerialization(serializationFilename, isResultsKeep)
        else:
            self._readAllResultsNoSerialization(isResultsKeep)

    def _readResultsSerialization(self, serializationFilename):
        logging.info("_readAllResultsSerialization")

        simulationsResults = SerializationPickle.SerializationPickle()
        simulationsResults.setPathname(self.getResultsPath())
        simulationsResults.setFilename(serializationFilename)

        if self.resetCache:
            simulationsResults.deleteFile()

        simulationResultsList = {}
        if simulationsResults.isFile():
            simulationResultsList = simulationsResults.load()

        self._simulationResultsList = simulationResultsList
        logging.info("Number of simulation results: %i", len(self._simulationResultsList))

    def _readAllResultsSerialization(self, serializationFilename, isResultsKeep):
        logging.info("_readAllResultsSerialization")

        simulationsResults = SerializationPickle.SerializationPickle()
        simulationsResults.setPathname(self.getResultsPath())
        simulationsResults.setFilename(serializationFilename)

        if self.createBackup:
            simulationsResults.backupFile()

        newResults = False
        if self.resetCache:
            simulationsResults.deleteFile()

        simulationResultsList = {}
        if simulationsResults.isFile():
            simulationResultsList = simulationsResults.load()

        _numberError = 0
        simulations = self.getAllSimulationParameters()
        total = len(simulations)
        for index, simulation in enumerate(simulations):
            if simulation.isDone(self.getSimulationsPath()):
                try:
                    key = self.generateResultsKey(simulation)
                    filepath = simulation.getProgramVersionFilepath(self.getSimulationsPath())
                    if simulationsResults.isOlderThan(filepath) or key not in simulationResultsList:
                        logging.info("Processing file %i/%i", (index+1), total)
                        if os.path.isfile(filepath):
                            logging.debug(filepath)
                            simulationResultsList[key] = self.readOneResults(simulation)
                            newResults = True
                            if index % SAVE_EVERY_SIMULATIONS == 0:
                                simulationsResults.save(simulationResultsList)
                        else:
                            logging.warning("File not found: %s", filepath)
                except UnboundLocalError as message:
                    logging.error("UnboundLocalError in %s for %s", "_readAllResultsSerialization", filepath)
                    logging.error(message)
                except ValueError as message:
                    logging.error("ValueError in %s for %s", "_readAllResultsSerialization", filepath)
                    logging.error(message)
                except AssertionError as message:
                    logging.error("AssertionError in %s for %s", "_readAllResultsSerialization", filepath)
                    logging.error(message)
                except IOError as message:
                    logging.warning(message)
                    logging.warning(simulation.name)
                    _numberError += 1

        if _numberError > 0:
            logging.info("Number of IO error: %i", _numberError)

        if newResults:
            simulationsResults.save(simulationResultsList)

        if isResultsKeep:
            self._simulationResultsList = simulationResultsList
            logging.info("Number of simulation results: %i", len(self._simulationResultsList))
        else:
            del simulationResultsList

    def _readAllResultsNoSerialization(self, isResultsKeep):
        logging.info("_readAllResultsNoSerialization")

        simulationResultsList = {}

        _numberError = 0
        simulations = self.getAllSimulationParameters()
        total = len(simulations)
        for index, simulation in enumerate(simulations):
            if simulation.isDone(self.getSimulationsPath()):
                try:
                    key = self.generateResultsKey(simulation)
                    if key not in simulationResultsList:
                        if self.verbose:
                            logging.info("Processing file %i/%i", (index+1), total)
                        else:
                            logging.debug("Processing file %i/%i", (index+1), total)
                        filepath = simulation.getProgramVersionFilepath(self.getSimulationsPath())
                        if os.path.isfile(filepath):
                            logging.debug(filepath)
                            simulationResultsList[key] = self.readOneResults(simulation)
                        else:
                            logging.warning("File not found: %s", filepath)
                except UnboundLocalError as message:
                    logging.error("UnboundLocalError in %s for %s", "_readAllResultsSerialization", filepath)
                    logging.error(message)
                except ValueError as message:
                    logging.error("ValueError in %s for %s", "_readAllResultsSerialization", filepath)
                    logging.error(message)
                except AssertionError as message:
                    logging.error("AssertionError in %s for %s", "_readAllResultsSerialization", filepath)
                    logging.error(message)
                except IOError as message:
                    logging.warning(message)
                    logging.warning(simulation.name)
                    _numberError += 1

        if _numberError > 0:
            logging.info("Number of IO error: %i", _numberError)

        if isResultsKeep:
            self._simulationResultsList = simulationResultsList
            logging.info("Number of simulation results: %i", len(self._simulationResultsList))
        else:
            del simulationResultsList

    def getResults(self, parameters):
        return self._simulationResultsList[parameters]

    def getAllResults(self):
        return self._simulationResultsList

    def _initData(self): #pragma: no cover
        raise NotImplementedError

    def getAnalysisName(self): #pragma: no cover
        raise NotImplementedError

    def createSpecimen(self, parameters): #pragma: no cover
        raise NotImplementedError

    def readResultsFiles(self):
        logging.info("readResultsFiles")

        self.readResults()

    def analyzeResultsFiles(self): #pragma: no cover
        raise NotImplementedError

    def readOneResults(self, simulation):
        raise NotImplementedError

    def generateResultsKey(self, simulation):
        variedParameterLabels = self.getVariedParameterLabels()

        simulation.createSimulationFiles(self.getInputPath(), self.getSimulationsPath())

        key = self._createKey(variedParameterLabels, simulation)

        return tuple(key)


    def run(self, batchFile):
        self._initData()

        options = _getOptions()

        if options == ANALYZE_TYPE_GENERATE_INPUT_FILE:
            self.generateInputFiles(batchFile)
            batchFile.write(self.getSimulationsPath())
        if options == ANALYZE_TYPE_CHECK_PROGRESS:
            self.checkProgress()
        if options == ANALYZE_TYPE_READ_RESULTS:
            self.readResultsFiles()
        if options == ANALYZE_TYPE_ANALYZE_RESULTS:
            self.analyzeResultsFiles()

    def _computeMCXrayFwhm_keV(self, detectorNoise_eV, xrayEnergy_keV):
        xrayEnergy_eV = xrayEnergy_keV*1.0e3
        factorK_eV = 2.6231

        fwhm_eV = math.sqrt(detectorNoise_eV*detectorNoise_eV + factorK_eV*xrayEnergy_eV)

        fwhm_keV = fwhm_eV * 1.0e-3
        return fwhm_keV

    def countsFromFixedWidth(self, xrayEnergies_keV, position_keV, width_keV, counts):
        counts = np.array(counts)

        v1 = position_keV - width_keV/2.0
        v2 = position_keV + width_keV/2.0
        maskArray = np.ma.masked_outside(xrayEnergies_keV, v1, v2)

        counts = np.sum(counts[~maskArray.mask])
        return counts

    def _computeSNR(self, IA, IB):
        snr = IA/math.sqrt(2.0*IB)
        return snr

    def _computeCDmin(self, CD0, snr0):
        CDmin = 3.0 * CD0 / snr0
        return CDmin

    def getVariedParameterLabels(self):
        return self._simulationsParameters.getVariedParameterLabels()

    def _createKey(self, variedParameterLabels, simulation):
        parameters = simulation.getParameters()

        key = []

        for label in variedParameterLabels:
            value = parameters[label]
            key.append(value)

        return key

    @property
    def overwrite(self):
        return self._overwrite
    @overwrite.setter
    def overwrite(self, overwrite):
        self._overwrite = overwrite

    @property
    def resetCache(self):
        return self._resetCache
    @resetCache.setter
    def resetCache(self, resetCache):
        self._resetCache = resetCache

    @property
    def useSerialization(self):
        return self._useSerialization
    @useSerialization.setter
    def useSerialization(self, useSerialization):
        self._useSerialization = useSerialization

    @property
    def verbose(self):
        return self._verbose
    @verbose.setter
    def verbose(self, verbose):
        self._verbose = verbose

    @property
    def createBackup(self):
        return self._createBackup
    @createBackup.setter
    def createBackup(self, createBackup):
        self._createBackup = createBackup

if __name__ == '__main__': #pragma: no cover
    import pyHendrixDemersTools.Runner as Runner
    Runner.Runner().run(runFunction=None)
