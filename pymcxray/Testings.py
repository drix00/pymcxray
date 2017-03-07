#!/usr/bin/env python

""" """
# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2007 Hendrix Demers"
__license__ = ""

# Standard library modules.
import os
import sys
import unittest
import logging
if __name__ == '__main__': #pragma: no cover
    print("Python version: %s" % sys.version)
# TODO: Remove this module after removing the two filters.
import warnings

# Third party modules.
import nose #@UnresolvedImport

# Local modules.
from pymcxray import get_current_module_path, read_value_from_configuration_file

# Globals and constants variables.
PLATFORM_ALL = 'all'
PLATFORM_NT = 'nt'
PLATFORM_MAC = 'Darwin'
PLATFORM_LINUX = 'Linux'
PLATFORM_JAVA = 'java'
PLATFORM_POSIX = 'posix'

def slow(function):
    function.slow = True
    return function

class ignore(object):
    def __init__(self, platforms=PLATFORM_ALL):
        self._platforms = platforms

    def __call__(self, function):
        if self._platforms == PLATFORM_ALL:
            function.ignore = True
        elif getPlatformName() in self._platforms:
            function.ignore = True

        return function

def getPlatformName():
    platformName = ""
    try:
        name = getOsName()
        if name == PLATFORM_NT:
            return PLATFORM_NT
        elif name == PLATFORM_JAVA:
            return PLATFORM_JAVA
        elif name == PLATFORM_MAC:
            return PLATFORM_MAC
        elif name == PLATFORM_LINUX:
            return PLATFORM_LINUX
    except AttributeError as status:
        logging.error(status)

    return platformName

def checkEquality(testCase, referenceValue, value):
    if isinstance(referenceValue, (int, str)):
        return testCase.assertEquals(referenceValue, value)
    elif isinstance(referenceValue, (float)):
        return testCase.assertAlmostEquals(referenceValue, value)

    testCase.fail("No equality test for this type %s." % type(referenceValue))

def _createIgnoredModules(configurationFile):
    ignoredModules = _createIgnoredModulesCommon()

    try:
        platformName = getPlatformName()
        if platformName == PLATFORM_MAC:
            ignoredModules.extend(_createIgnoredModulesDarwin())
        elif platformName == PLATFORM_LINUX:
            ignoredModules.extend(_createIgnoredModulesLinux())
    except AttributeError as status:
        logging.error(status)

    moduleNames = _createIgnoredItems("ignoredModules", configurationFile)

    ignoredModules.extend(moduleNames)

    return ignoredModules

def _createIgnoredItems(sectionName, configurationFile):
    configurationFilepath = get_current_module_path(__file__, configurationFile)

    values = read_value_from_configuration_file(configurationFilepath, "Testings", sectionName, default="")

    names = []
    for item in values.split(','):
        names.append(item.strip())

    return names

def _createIgnoredProjects(configurationFile):
    ignoredProjects = _createIgnoredProjectsCommon()

    projectNames = _createIgnoredItems("ignoredProjects", configurationFile)

    ignoredProjects.extend(projectNames)

    return ignoredProjects

def getComputerName():
    try:
        name = getOsName()
        if name == PLATFORM_NT:
            return os.environ['COMPUTERNAME']
        elif name == PLATFORM_JAVA:
            return sys.platform
        else:
            return name
    except AttributeError as status:
        logging.error(status)

def getOsName():
    name = os.name

    if name == PLATFORM_POSIX:
        name = os.uname()[0] #@UndefinedVariable

    return name

def _createIgnoredModulesCommon():
        ignoredModules = []
        return ignoredModules

def _createIgnoredProjectsCommon():
    ignoredProjects = []
    return ignoredProjects

def _createIgnoredModulesLinux():
        ignoredModules = ["test_Controller.py"
                                            , "test_CurrentSourceFrame.py"
                                            , "test_PumpController.py"
                                            , "test_PumpManager.py"
                                            , "test_pyLiveHistogram.py"
                                            , "test_application.py"
                                            , "test_CurrentVoltageSourcesFrame.py"
                                            , "test_DigitalMultimeterFrame.py"
                                            , "test_DigitalMultimeterVA18B.py"
                                            , "test_perimeter.py"
                                            , "test_PortListing.py"
                                            , "test_Analyze3dDataSets.py"
                                            , "test_Figures3DStem.py"]
        return ignoredModules

def _createIgnoredModulesDarwin():
        ignoredModules = ["test_pyLiveHistogram.py"
                                            , "test_CheckSvnStatus.py"
                                            , "test_FindSvnFolders.py"
                                            , "test_AnalyzeChristianSampleDepthProfiles.py"
                                            , "test_AnalyzeCurrentDensitySamples.py"
                                            , "test_TrajectoryDisplay.py"
                                            , "test_PortListing.py"
                                            , "test_PumpControllerFrame.py"
                                            , "test_PumpFrame.py"
                                            , "test_PumpController.py"
                                            , "test_PumpManager.py"
                                            , "test_PumpManagerFrame.py"
                                            , "test_ExperimentalData20090128.py"
                                            , "test_ExperimentalData20090129.py"
                                            , "test_ExperimentalData20090203.py"
                                            , "test_ExperimentalData20090427.py"
                                            , "test_ExperimentalData80Anneal.py"
                                            , "test_ExperimentalData80AnnealAlbany.py"
                                            , "test_FluorescenceYieldData.py"
                                            , "test_GraphsFactory.py"
                                            , "test_Graphs.py"
                                            , "test_CutoffEnergyLossGraphs.py"
                                            , "test_lowenergy.py"
                                            , "test_composition.py"
                                            , "test_runner.py"
                                            , "test_Analyze3dDataSets.py"
                                            , "test_ConvergentBeamModel.py"
                                            , "test_Figures3DStem.py"]
        return ignoredModules

def _logPythonInfo():
    logging.info("%s", "*"*80)
    logging.info("Executable: %s", sys.executable)
    logging.info("Version:    %s", sys.version)
    logging.info("Platform:   %s", sys.platform)
    logging.info("%s", "*"*80)

class Testings(object):
    def __init__(self, configurationFilename, basepath=None):
        self._configurationFilename = configurationFilename

        self._basepaths = self._initBasepaths(basepath)

        self._initFilterWarnings()

        self._ignoredModules = _createIgnoredModules(self._configurationFilename)

        self._ignoredPatterns = self._createIgnoredPatterns()

        self._ignoredProjects = _createIgnoredProjects(self._configurationFilename)

        self._importErrorModules = []

    def _initBasepaths(self, basepath):
        if basepath:
            return [basepath]
        else:
            return self._getBasepaths()

    def _getBasepaths(self):
        """
        Read basepaths to search for tests modules from a configuration files.

        The paths are seperated by a comma.

        """
        configurationFile = self._configurationFilename
        configurationFilepath = Files.getCurrentModulePath(__file__, configurationFile)
        value = Files.readValueFromConfigurationFile(configurationFilepath, "Paths", "testingPaths")

        basepaths = []
        for item in value.split(','):
            basepaths.append(item.strip())

        return basepaths

    def _initFilterWarnings(self):
        # TODO: Remove this filter.
        warnings.filterwarnings("ignore", category=UserWarning)

    def _createIgnoredPatterns(self):
        return "*.svn*;*boost_*"

    def runTestSuiteOld(self, verbosity=2):
        _logPythonInfo()

        suite = self._createProjectTestSuite()
        unittest.TextTestRunner(verbosity=verbosity).run(suite)

        if verbosity > 1:
            self._displayIgnoredModules()

        self._displayImportErrorModules()

    def runTestSuite(self, options='-a !slow,!ignore'):
        _logPythonInfo()

        # TODO: nose '--with-isolation' options does not work with all projects, disable for now.
        argv = sys.argv
        argv.extend(options.split())
        #argv.append('-w')
        argv.append('.')

        for basepath in self._basepaths:
            if len(basepath.strip()) > 0:
                #argv.append('-w')
                argv.append('%s' % basepath)

        for ignoredModule in self._ignoredModules:
            if len(ignoredModule.strip()) > 0:
                argv.append("-e")
                argv.append(ignoredModule)

        for ignoredProject in self._ignoredProjects:
            if len(ignoredProject.strip()) > 0:
                argv.append("-e")
                argv.append(ignoredProject)

        nose.main(argv=argv)

        self._displayIgnoredModules()
        self._displayImportErrorModules()

    def runTestSuiteByProjects(self, options='-a !slow,!ignore'):
        _logPythonInfo()

        # TODO: nose '--with-isolation' options does not work with all projects, disable for now.
        originalArguments = []

        for basepath in self._basepaths:
            for item in os.listdir(basepath):
                path = os.path.join(basepath, item)
                if os.path.isdir(path):
                    logging.info("Testing project: %s", item)
                    argv = originalArguments[:]
                    argv.extend(options.split())
                    #argv.append('-w')
                    argv.append('.')
                    #argv.append('-w')
                    argv.append('%s' % path)

                    for ignoredModule in self._ignoredModules:
                        argv.append("-e")
                        argv.append(ignoredModule)

                    nose.main(argv=argv, exit=False)

        self._displayIgnoredModules()
        self._displayImportErrorModules()

    def runAllTests(self, verbosity=1):
        _logPythonInfo()

        logging.debug("Before getProjectTestSuite")
        suite = self._createProjectTestSuite()
        logging.debug("After getProjectTestSuite")

        unittest.TextTestRunner(verbosity=verbosity).run(suite)

        if verbosity > 1:
            self._displayIgnoredModules()

        self._displayImportErrorModules()

    def _createProjectTestSuite(self):
        testModuleFilepaths = self._findAllTestModules()

        testModuleFilenames, testModulesFolder = self._splitPathsAndFilenames(testModuleFilepaths)

        self._addSourcesFoldersToPath(testModulesFolder)

        moduleNames = self._extractModuleNames(testModuleFilenames)

        importedTestModules = self._importTestModules(moduleNames)

        loadedTests = self._loadTestsFromModules(importedTestModules)

        suite = unittest.TestSuite(loadedTests)

        return suite

    def _findAllTestModules(self):
        searchPattern = "test_*.py"

        single_level = False
        ignoredPatterns = self._ignoredPatterns

        testModulePathnames = []
        for searchPath in self._basepaths:
            logging.debug("searchPath: %s", searchPath)
            for filename in Files.findAllFiles(searchPath
                                                                                 , searchPattern
                                                                                 , ignoredPatterns
                                                                                 , single_level=single_level):
                logging.debug("TestModulepathname: %s", filename)
                testModulePathnames.append(filename)

        return testModulePathnames

    def _importTestModules(self, moduleNames):
            modules = []
            for moduleName in moduleNames:
                    try:
                            modules.append(__import__(moduleName))
                    except ImportError as error:
                            self._importErrorModules.append(moduleName)
                            logging.error("Import error in module %s: %s", moduleName, error)
                    except OSError as error:
                            self._importErrorModules.append(moduleName)
                            logging.error("Import error in module %s: %s", moduleName, error)

            return modules

    def _loadTestsFromModules(self, importedTestModules):
        load = unittest.defaultTestLoader.loadTestsFromModule

        loadedTests = [load(module) for module in importedTestModules]
        return loadedTests

    def _addSourcesFoldersToPath(self, sourceFolders):
        for folder in sourceFolders:
            sys.path.append(folder)

    def _displayIgnoredModules(self):
        self._displayModuleNames("Ignored", self._ignoredModules)

    def _displayModuleNames(self, message, modules):
        print("="*40)
        print("%s modules for %s" % (message, self.getComputerName()))

        for moduleName in modules:
            print("\t%s" % (moduleName))

        print("="*40)

    def _displayImportErrorModules(self):
        self._displayModuleNames("Import error", self._importErrorModules)

    def _extractModuleNames(self, testModulesName):
            filenameToModuleName = lambda f: os.path.splitext(f)[0]
            moduleNames = [filenameToModuleName(f) for f in testModulesName]
            return moduleNames

    def _splitPathsAndFilenames(self, testModuleFilepaths):
            testModulesFolder = []
            testModuleFilenames = []

            for filepath in testModuleFilepaths:
                    testModuleFolder, testModuleFilename = os.path.split(filepath)
                    if self._isIgnoredTestModule(testModuleFilename):
                            testModuleFilenames.append(testModuleFilename)
                            testModulesFolder.append(testModuleFolder)
                    else:
                            logging.warning("Ignored test module: %s", testModuleFilename)

            return testModuleFilenames, testModulesFolder

    def _isIgnoredTestModule(self, testModuleFilename):
            return testModuleFilename not in self._ignoredModules

def runTestSuiteOld():
    projectPath = os.path.abspath(os.path.dirname(sys.argv[0]))
    testings = Testings(projectPath)
    testings.runTestSuite()

def runTestSuite():
    runTestSuiteWithoutCoverage()

def runTestSuiteWithoutCoverage():
    _runTestSuite(options='-s -v -a !slow,!ignore')

def runTestSuiteWithCoverage(packageName):
    _runTestSuite(options='-s -v -a !slow,!ignore --with-coverage --cover-erase --cover-inclusive', packageName=packageName)

def _runTestSuite(options, packageName=None):
    """
    Run a test suite with nose testing framework.

    By default: don't capture stdout, print each testMethod name and skip slow
    and ignore testMethod.

    :param options: options string to pass to nose.main argv parameter.
    :type options: string

    .. note::
        The options string extend the sys.argv and the new argv is passed to nose.main.
    """
    _logPythonInfo()

    if packageName is not None:
        try:
            index = packageName.rindex('.')
            packageName = packageName[:index]
        except ValueError:
            pass
        options += " --cover-package=%s" % (packageName)
    argv = sys.argv
    argv.extend(options.split())

#     for ignoredModule in self._ignoredModules:
#         argv.append("-e")
#         argv.append(ignoredModule)

    nose.main(argv=argv)

def runTestModule():
    _runTestModule()

def runTestModuleWithCoverage(moduleFilepath, withCoverage=True):
    if withCoverage:
        _runTestModule(moduleFilepath, options='-v --with-isolation -a !ignore --with-coverage --cover-erase')
    else:
        _runTestModule(moduleFilepath, options='-v --with-isolation -a !ignore')

def _runTestModule(moduleFilepath=None, options='-v -a !ignore'):
    """
    Run a test suite with nose testing framework on the specified module.

    By default: print each testMethod name and test slow
    and skip ignore testMethod.

    In the test module, the function should is normaly called:

        Testings.runTestModule()

    :param moduleFilepath: path of the module to test.
    :type moduleFilepath: string
    :param options: options string to pass to nose.main argv parameter.
    :type options: string

    .. note::
        The options string extend the sys.argv and the new argv is passed to nose.main.
    """
    _logPythonInfo()

    argv = sys.argv
    argv.extend(options.split())
    if moduleFilepath is not None:
        nose.main(defaultTest=moduleFilepath, argv=argv)
    else:
        nose.main(argv=argv)

def run():
    if len(sys.argv) > 1:
        configurationFilename = sys.argv[1]
    else:
        configurationFilename = "Testings.cfg"
    testings = Testings(configurationFilename=configurationFilename)
    if configurationFilename in sys.argv:
        sys.argv.remove(configurationFilename)

    #testings.runTestSuite(verbosity=1)
    testings.runTestSuite()
    #testings.runTestSuiteByProjects()

if __name__ == '__main__': #pragma: no cover
    handler = logging.NullHandler()
    handler.setLevel(logging.ERROR)
    logging.getLogger().addHandler(handler)

    run()
