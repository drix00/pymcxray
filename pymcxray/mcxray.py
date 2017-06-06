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
import datetime
import filecmp

# Third party modules.
import numpy as np
import h5py
from apscheduler.schedulers.blocking import BlockingScheduler

# Local modules.
from pymcxray import get_current_module_path, create_path, get_results_mcgill_path, get_mcxray_program_path, get_mcxray_program_name, get_mcxray_archive_path, get_mcxray_archive_name
import pymcxray.serialization.SerializationPickle as SerializationPickle

# Project modules
import pymcxray.Simulation as Simulation
from pymcxray.SimulationsParameters import PARAMETER_SPECIMEN

# Globals and constants variables.
ANALYZE_TYPE_GENERATE_INPUT_FILE = "generate"
ANALYZE_TYPE_CHECK_PROGRESS = "check"
ANALYZE_TYPE_READ_RESULTS = "read"
ANALYZE_TYPE_ANALYZE_RESULTS = "analyze"
ANALYZE_TYPE_ANALYZE_SCHEDULED_READ = "scheduled_read"

SAVE_EVERY_SIMULATIONS = 10

HDF5_SIMULATIONS = "simulations"
HDF5_PARAMETERS = "parameters"

def _getOptions():
    analyzeTypes = []
    analyzeTypes.append(ANALYZE_TYPE_GENERATE_INPUT_FILE)
    analyzeTypes.append(ANALYZE_TYPE_CHECK_PROGRESS)
    analyzeTypes.append(ANALYZE_TYPE_READ_RESULTS)
    analyzeTypes.append(ANALYZE_TYPE_ANALYZE_RESULTS)
    analyzeTypes.append(ANALYZE_TYPE_ANALYZE_SCHEDULED_READ)

    parser = argparse.ArgumentParser(description='Analyze MCXRay x-ray background problem.')
    parser.add_argument('type', metavar='AnalyzeType', type=str, choices=analyzeTypes, nargs='?',
                        default=ANALYZE_TYPE_GENERATE_INPUT_FILE,
                        help='Type of analyze to do')

    parser.add_argument('args', nargs=argparse.REMAINDER)

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
            self._configurationFilepath = get_current_module_path(__file__, "../../pyMcGill.cfg")
        else:
            self._configurationFilepath = configurationFilepath
        self._output = None

        self.overwrite = True
        self.resetCache = False
        self.useSerialization = True
        self.verbose = True
        self.createBackup = True
        self.use_hdf5 = False
        self.delete_result_files = False
        self.read_interval_h = 1
        self.read_interval_m = None

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

        self.format_digit = {}

    def getSimulationPath(self):
        try:
            if self._simulationPath is not None:
                return self._simulationPath
            elif self._relativePath is not None:
                path = get_results_mcgill_path(self._configurationFilepath)
                path = os.path.join(path, self._relativePath)
            elif self._basepath is not None:
                name = self.getAnalysisName()
                path = get_results_mcgill_path(self._configurationFilepath)
                path = os.path.join(path, self._basepath, "%s" % (name))
            else:
                name = self.getAnalysisName()
                path = get_results_mcgill_path(self._configurationFilepath, "%s" % (name))

            if not os.path.isdir(path):
                os.makedirs(path)

            self._simulationPath = path
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
        inputPath = create_path(inputPath)

        return inputPath

    def get_hdf5_file_path(self):
        result_path = self.getResultsPath()
        name = self.getAnalysisName()
        file_path = os.path.join(result_path, name + ".hdf5")
        logging.debug(file_path)
        return file_path

    def get_hdf5_group(self, hdf5_file):
        try:
            hdf5_group = hdf5_file[HDF5_SIMULATIONS]
            return hdf5_group
        except KeyError as message:
            logging.error(message)
            message = "Filename: %s" % (hdf5_file.filename)
            logging.error(message)
            return None

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
        basePath = get_mcxray_program_path(self._configurationFilepath)

        programName = get_mcxray_program_name(self._configurationFilepath, default="McXRay.exe")
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
        archivesPath = get_mcxray_archive_path(self._configurationFilepath)
        archiveFilename = get_mcxray_archive_name(self._configurationFilepath)
        archiveFilepath = os.path.join(archivesPath, archiveFilename)

        destinationPath = self.getSimulationsPath()
        self._extractZipfile(archiveFilename, archiveFilepath, destinationPath)

    def _extractZipfile(self, archiveFilename, archiveFilepath, destinationPath):
        versionBasename, dummyExtension = os.path.splitext(os.path.basename(archiveFilepath))
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

        file_path = self.get_hdf5_file_path()
        if self.use_hdf5 and os.path.isfile(file_path):
            with h5py.File(file_path, 'r', driver='core') as hdf5_file:
                hdf5_group = self.get_hdf5_group(hdf5_file)
                self._generate_input_files(batchFile, hdf5_group)
        else:
            hdf5_group = None
            self._generate_input_files(batchFile, hdf5_group)

    def _generate_input_files(self, batchFile, hdf5_group):
        numberSimulations = 0
        numberSimulationsTodo = 0
        numberSimulationsDone = 0
        simulationTodoNames = []

        for simulation in self.getAllSimulationParameters():
            simulation.createSimulationFiles(self.getInputPath(), self.getSimulationsPath(), hdf5_group)

            if simulation.isDone(self.getSimulationsPath(), hdf5_group):
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
        file_path = self.get_hdf5_file_path()
        if self.use_hdf5 and os.path.isfile(file_path):
            with h5py.File(file_path, 'r', driver='core') as hdf5_file:
                hdf5_group = self.get_hdf5_group(hdf5_file)
                self._check_progress(hdf5_group)
        else:
            hdf5_group = None
            self._check_progress(hdf5_group)

    def _check_progress(self, hdf5_group):
        numberSimulations = 0
        numberSimulationsTodo = 0
        numberSimulationsDone = 0
        simulationTodoNames = []

        inputPath = os.path.join(self.getSimulationsPath(), "input")
        inputPath = create_path(inputPath)

        for simulation in self.getAllSimulationParameters():
            if simulation.isDone(self.getSimulationsPath(), hdf5_group):
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
            simulation.format_digit = self.format_digit
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

        if self.use_hdf5:
            self._read_all_results_hdf5()
        else:
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

    def _read_all_results_hdf5(self):
        logging.info("_read_all_results_hdf5")
        starting_time_all = time.perf_counter()
        number_simulations_read = 0

        file_path = self.get_hdf5_file_path()
        backup_file_path = ""
        if os.path.isfile(file_path):
            backup_file_path = self.backup_hdf5_File(file_path)

        with h5py.File(file_path, 'a', driver='core', backing_store=True) as hdf5_file:
            hdf5_root = hdf5_file.require_group(HDF5_SIMULATIONS)

            _numberError = 0
            simulations = self.getAllSimulationParameters()

            self._write_parameters_hdf5(hdf5_root)

            total = len(simulations)
            for index, simulation in enumerate(simulations):
                if simulation.isDone(self.getSimulationsPath(), None):
                    starting_time = time.perf_counter()
                    try:
                        filepath = simulation.getProgramVersionFilepath(self.getSimulationsPath())
                        logging.info("Processing file %i/%i", (index+1), total)

                        if os.path.isfile(filepath):
                            logging.debug(filepath)

                            name = simulation.name
                            if name in hdf5_root:
                                del hdf5_root[name]
                            hdf5_group = hdf5_root.require_group(name)

                            parameters = simulation.getParameters()
                            for parameter_name in parameters:
                                hdf5_group.attrs[parameter_name] = parameters[parameter_name]

                            self.read_one_results_hdf5(simulation, hdf5_group)

                            # if number_simulations_read%50 == 0:
                            #     hdf5_root.file.flush()

                            if self.delete_result_files:
                                self.delete_simulation_result_files(simulation)
                        else:
                            logging.warning("File not found: %s", filepath)
                    except UnboundLocalError as message:
                        logging.error("UnboundLocalError in %s for %s", "_read_all_results_hdf5", filepath)
                        logging.error(message)
                    except ValueError as message:
                        logging.error("ValueError in %s for %s", "_read_all_results_hdf5", filepath)
                        logging.error(message)
                    except AssertionError as message:
                        logging.error("AssertionError in %s for %s", "_read_all_results_hdf5", filepath)
                        logging.error(message)
                    except IOError as message:
                        logging.warning(message)
                        logging.warning(simulation.name)
                        _numberError += 1

                    elapse_time = time.perf_counter() - starting_time
                    logging.info("Elapse time for one simulation: %.1f s", elapse_time)
                    number_simulations_read += 1

            if _numberError > 0:
                logging.info("Number of IO error: %i", _numberError)

            elapse_time_all = time.perf_counter() - starting_time_all
            logging.info("Elapse time for all simulations (%i): %.1f s", number_simulations_read, elapse_time_all)

        if not self.createBackup and os.path.isfile(backup_file_path):
            file_path = self.get_hdf5_file_path()
            if self.use_hdf5 and os.path.isfile(file_path):
                with h5py.File(file_path, 'r', driver='core') as hdf5_file:
                    logging.info("Remove file: %s", backup_file_path)
                    os.remove(backup_file_path)

    def _write_parameters_hdf5(self, hdf5_root):
        hdf5_parameters_group = hdf5_root.require_group(HDF5_PARAMETERS)

        for fixed_parameter_name, fixed_parameter_value in self._simulationsParameters.fixedParameters.items():
            hdf5_parameters_group.attrs[fixed_parameter_name] = fixed_parameter_value

        for varied_parameter_name, varied_parameter_value in self._simulationsParameters.variedParameters.items():
            if varied_parameter_name in hdf5_parameters_group:
                del hdf5_parameters_group[varied_parameter_name]

            if type(varied_parameter_value[0]) is str:
                length = np.max([len(item) for item in varied_parameter_value])
                data_type = "S{:d}".format(length)
                data = np.array(varied_parameter_value, dtype=data_type)
            else:
                data = np.array(varied_parameter_value)

            data_set = hdf5_parameters_group.create_dataset(varied_parameter_name, data=data)


    def backup_hdf5_File(self, file_path):
        backup_file_path = None
        if os.path.isfile(file_path):
            suffix = self.generate_time_stamp()
            index_extension = file_path.rfind('.hdf5')
            base_name = file_path[:index_extension]
            backup_file_path = base_name + "_" + suffix + ".hdf5"

            shutil.copy2(file_path, backup_file_path)
            logging.info("Backup created: %s", backup_file_path)

        return backup_file_path

    def generate_time_stamp(self):
        dateTime = datetime.datetime.now()

        year = dateTime.year
        month = dateTime.month
        day = dateTime.day
        hour = dateTime.hour
        minute = dateTime.minute
        second = dateTime.second

        arguments = (year, month, day, hour, minute, second)
        name = "%04i-%02i-%02i_%02ih%02im%02is" % (arguments)

        return name

    def delete_simulation_result_files(self, simulation):
        simulation_name = simulation.name.replace('.', 'd')
        for file_name in os.listdir(self.getResultsPath()):
            if file_name.startswith(simulation_name):
                file_path = os.path.join(self.getResultsPath(), file_name)
                logging.debug("Remove file: %s", file_name)
                os.remove(file_path)

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
            if self.use_hdf5:
                self.analyze_results_hdf5()
            else:
                self.analyzeResultsFiles()
        if options == ANALYZE_TYPE_ANALYZE_SCHEDULED_READ:
            self.readResultsFiles()
            scheduler = BlockingScheduler()
            if self.read_interval_h is not None and self.read_interval_m is None:
                scheduler.add_job(self.readResultsFiles, 'interval', hours=self.read_interval_h, coalesce=True)
            else:
                scheduler.add_job(self.readResultsFiles, 'interval', minutes=self.read_interval_m, coalesce=True)
            print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

            try:
                scheduler.start()
            except (KeyboardInterrupt, SystemExit):
                pass

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
