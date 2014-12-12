#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2009 Hendrix Demers"
__license__ = ""

# Subversion informations for the file.
__svnRevision__ = "$Revision$"
__svnDate__ = "$Date$"
__svnId__ = "$Id$"

# Standard library modules.
import os
import logging
import datetime
import tempfile
import shutil
import zipfile
import errno
import stat

# Third party modules.

# Local modules.
import pyHendrixDemersTools.Files as Files

# Globals and constants variables.

FOLDER_LATEST = "latest"
FOLDER_LAST_X_VERSION = "lastXVersion"
FOLDER_LAST_WEEK = "lastWeek"
FOLDER_LAST_MONTH = "lastMonth"
FOLDER_ARCHIVES = "archives"

FOLDER_DATA = "data"

class Package(object):
    def __init__(self, releaseBasePath, developmentPath, packageName=None, overWrite=False):
        self._releaseBasePath = releaseBasePath
        self._developmentPath = developmentPath

        self._packageName = packageName

        self._overWrite = overWrite
        self._initData()

    def _initData(self):
        raise NotImplementedError

    def run(self, isSimulationRunning=False):
        self._checkfolderStructure()
        self._createZipFileFromLastCompile()

        if not isSimulationRunning:
            self._generateTemporalFolders()

    def _checkfolderStructure(self):
        self._createPath(self._releaseBasePath, name="release base")

        path = os.path.join(self._releaseBasePath, FOLDER_LATEST)
        self._createPath(path, name="release")

        path = os.path.join(self._releaseBasePath, FOLDER_ARCHIVES)
        self._createPath(path, name="archives")

    def _createPath(self, path, name=""):
        if not os.path.isdir(path):
            if name == "":
                logging.info("Create path: %s", path)
            else:
                logging.info("Create %s path: %s", name, path)

            os.makedirs(path)

    def _createZipFileFromLastCompile(self):
        version = self._getProgramVersion()
        logging.info("Latest development version: %s.", version)
        dateTime = self._getLatestDateTime()
        basename = self._createBasenameFromDate(dateTime, version)

        zipFilename = basename + ".zip"
        zipFilepath = os.path.join(self._releaseBasePath, FOLDER_ARCHIVES, zipFilename)
        if self._overWrite or not self._isArchiveExist(zipFilepath):
            temporaryPath = tempfile.mkdtemp()
            temporaryPath = os.path.join(temporaryPath, "mcxray")
            try:
                self._copyData(temporaryPath)
                self._copyPrograms(temporaryPath)
                self._copyLibraries(temporaryPath)
                self._copyDocumentations(temporaryPath)
                self._copyLicenses(temporaryPath)
                self._copyVersionFile(zipFilepath, temporaryPath)
            except IOError as message:
                logging.error("Cannot copy all files, zip file not created.")
                logging.error(message)
                return

            logging.info("Create zip file: %s", zipFilepath)
            zipFile = zipfile.ZipFile(zipFilepath, 'wb')

            oldPath = os.getcwd()
            os.chdir(temporaryPath)
            for (dirPath, dummyDirNames, filenames) in os.walk(temporaryPath):
                for filename in filenames:
                    path = os.path.relpath(dirPath, temporaryPath)
                    filepath = os.path.normpath(os.path.join(path, filename))
                    zipFile.write(filepath)

            zipFile.close()
            del zipFile
            os.chdir(oldPath)

            try:
                shutil.rmtree(temporaryPath, ignore_errors=False, onerror=handleRemoveReadonly)
            except WindowsError as message:
                logging.warning(message)

    def _getProgramVersion(self):
        version = "Unknown"
        wincasinoResourceFilepath = os.path.join(self._developmentPath, self.RESOURCE_FILEPATH)
        wincasinoResourceFilepath = os.path.normpath(wincasinoResourceFilepath)

        lines = open(wincasinoResourceFilepath, 'rb').readlines()

        for line in lines:
            line = line.strip()
            if line.startswith("FILEVERSION"):
                items = line.split()
                versionNumbers = items[-1].split(',')
                version = ".".join(versionNumbers)
        return version

    def _getLatestDateTime(self):
        dateTime = datetime.datetime.min
        for programName in self._generateProgramName():
            programPath = os.path.join(self._developmentPath, self.FOLDER_CASINO_BIN, programName)
            programPath = os.path.normpath(programPath)
            try:
                lastModifiedDateTime = datetime.datetime.fromtimestamp(os.path.getmtime(programPath))
                dateTime = max(dateTime, lastModifiedDateTime)
            except WindowsError:
                pass

        logging.debug("Latest date-time: %s.", dateTime)
        return dateTime

    def _generateProgramName(self):
        raise NotImplementedError

    def _createBasenameFromDate(self, dateTime, version):
        year = dateTime.year
        month = dateTime.month
        day = dateTime.day
        hour = dateTime.hour
        minute = dateTime.minute
        second = dateTime.second

        arguments = (year, month, day, hour, minute, second)
        name = "%04i-%02i-%02i_%02ih%02im%02is" % (arguments)
        name += "_%s" % (self.NAME_MCXRAY)
        name += "_v%s" % (version)
        if self._packageName is not None:
            name += "_%s" % (self._packageName)

        return name

    def _getDateFromBasename(self, basename):
        try:
            name = "_%s" % (self.NAME_MCXRAY)
            index = basename.rindex(name)
            basename = basename[:index]
        except ValueError:
            try:
                index = basename.rindex("_v")
                basename = basename[:index]
            except ValueError:
                logging.info(basename)

        timestampFormat = "%Y-%m-%d_%Hh%Mm%Ss"
        date = datetime.datetime.strptime(basename, timestampFormat)
        return date

    def _isArchiveExist(self, zipFilepath):
        return os.path.isfile(zipFilepath)

    def _copyData(self, temporaryPath):
        dataPath = os.path.join(self._developmentPath, FOLDER_DATA)

        temporaryDataPath = os.path.join(temporaryPath, "data")
        shutil.copytree(dataPath, temporaryDataPath)

        self._removeCvs(temporaryDataPath)

    def _removeCvs(self, path):
        for (dirPath, dummyDirNames, dummyFilenames) in os.walk(path):
            if dirPath.endswith("CVS"):
                logging.info("Remove CVS folder: %s", dirPath)
                shutil.rmtree(dirPath)

    def _copyPrograms(self, temporaryPath):
        programPath = os.path.join(self._developmentPath, self.FOLDER_CASINO_BIN)

        for programName in self._generateProgramName():
            sourceFilepath = os.path.join(programPath, programName)
            newProgramName = self._renameProgram(programName)
            destinationFilepath = os.path.join(temporaryPath, newProgramName)
            shutil.copy2(sourceFilepath, destinationFilepath)

    def _renameProgram(self, programName):
        return programName

    def _copyLibraries(self, temporaryPath):
        programPath = os.path.join(self._developmentPath, self.FOLDER_DLL)

        for libraryName in self._libraryFilenames:
            sourceFilepath = os.path.join(programPath, libraryName)
            destinationFilepath = os.path.join(temporaryPath, libraryName)
            shutil.copy2(sourceFilepath, destinationFilepath)

    def _copyDocumentations(self, temporaryPath):
        docPath = os.path.join(self._developmentPath, self.FOLDER_DOCUMENTATIONS)

        for name in self._documentFilenames:
            sourceFilepath = os.path.join(docPath, name)
            newName = name.replace('_', '')
            path = os.path.join(temporaryPath, "Documentations")
            path = Files.createPath(path)
            destinationFilepath = os.path.join(path, newName)
            shutil.copy2(sourceFilepath, destinationFilepath)

    def _copyLicenses(self, temporaryPath):
        sourcePath = os.path.join(self._developmentPath, self.FOLDER_LICENSES)
        destinationPath = os.path.join(temporaryPath, self.FOLDER_LICENSES)

        shutil.copytree(sourcePath, destinationPath)

        self._removeCvs(destinationPath)

    def _generateTemporalFolders(self):
        archiveFiles = {}

        archivesPath = os.path.join(self._releaseBasePath, FOLDER_ARCHIVES)
        for filename in os.listdir(archivesPath):
            if filename.endswith('.zip'):
                try:
                    basename, dummyExtension = os.path.splitext(filename)
                    date = self._getDateFromBasename(basename)
                    archiveFiles[date] = filename
                except ValueError as message:
                    logging.warning(message)

        if len(archiveFiles) > 0:
            latestDate = max(archiveFiles.keys())

            filename = archiveFiles[latestDate]
            path = os.path.join(self._releaseBasePath, FOLDER_LATEST)
            self._createPath(path, name="release")
            self._extractZipfile(filename, path)

            dates = sorted(archiveFiles.keys(), reverse=True)
            if len(dates) > 5:
                lastFiveArchives = dates[1:6]
            else:
                lastFiveArchives = dates[1:]

            for index,date in enumerate(lastFiveArchives):
                filename = archiveFiles[date]
                foldename = FOLDER_LAST_X_VERSION.replace('X', str(index+1))
                path = os.path.join(self._releaseBasePath, foldename)

                try:
                    self._createPath(path, name="last %i version" % (index+1))
                    self._extractZipfile(filename, path)
                except WindowsError as message:
                    logging.error(message)
                    logging.error("Cannot create the path: %s", path)

            today = datetime.datetime.now()

            oneWeekDelta = datetime.timedelta(weeks=1)
            oneWeek = today - oneWeekDelta
            self._createTemporalFolder(dates, archiveFiles, oneWeek, "last week", FOLDER_LAST_WEEK)

            oneMonthDelta = datetime.timedelta(weeks=4)
            oneMonth = today - oneMonthDelta
            self._createTemporalFolder(dates, archiveFiles, oneMonth, "last month", FOLDER_LAST_MONTH)

    def _createTemporalFolder(self, dates, archiveFiles, timeLimit, name, folder):
        for date in dates:
            if date <= timeLimit:
                logging.debug("Date for %s: %s", name, date)
                filename = archiveFiles[date]
                path = os.path.join(self._releaseBasePath, folder)
                self._createPath(path, name=name)
                self._extractZipfile(filename, path)
                break

    def _extractZipfile(self, archiveFilename, destinationPath):
        archivesPath = os.path.join(self._releaseBasePath, FOLDER_ARCHIVES)
        sourceFilepath = os.path.join(archivesPath, archiveFilename)

        versionFilepath = self._getVersionFilepath(archiveFilename, destinationPath)

        if self._overWrite or not os.path.isfile(versionFilepath):
            logging.info("Extracting archive %s to %s.", archiveFilename, destinationPath)
            shutil.rmtree(destinationPath, ignore_errors=True)

            if not os.path.isdir(destinationPath):
                self._createPath(destinationPath)

            destinationFilepath = os.path.join(destinationPath, archiveFilename)

            shutil.copy2(sourceFilepath, destinationFilepath)

            zipFile = zipfile.ZipFile(destinationFilepath, 'rb')
            zipFile.extractall(destinationPath)
            zipFile.close()

            self._createVersionFile(archiveFilename, destinationPath)

            os.remove(destinationFilepath)
        else:
            logging.info("Folder %s already contain archive %s.", destinationPath, archiveFilename)

    def _copyVersionFile(self, archiveFilepath, destinationPath):
        archiveFilename = os.path.basename(archiveFilepath)

        self._createVersionFile(archiveFilename, destinationPath)

    def _createVersionFile(self, archiveFilename, destinationPath):
        versionFilepath = self._getVersionFilepath(archiveFilename, destinationPath)

        fileVersion = open(versionFilepath, 'wb')
        versionBasename, dummyExtension = os.path.splitext(archiveFilename)
        fileVersion.write(versionBasename)
        fileVersion.close()

    def _getVersionFilepath(self, archiveFilename, destinationPath):
        versionBasename, dummyExtension = os.path.splitext(archiveFilename)
        versionFilename = versionBasename + ".txt"
        versionFilepath = os.path.join(destinationPath, versionFilename)

        return versionFilepath

class PackageMCXRay(Package):
    FOLDER_CASINO_BIN = "bin"
    FOLDER_DLL = ""
    FOLDER_DOCUMENTATIONS = r"documentations/Manual"
    FOLDER_LICENSES = "licenses"
    PROGRAM_NAME = "McXRay"
    CONSOLE_PROGRAM_NAME = "console_mcxray"
    RESOURCE_FILEPATH = "MCXRay/McXRay.rc"

    NAME_MCXRAY = "MCXRay"

    def _initData(self):
        self._libraryFilenames = []
        self._documentFilenames = ["MCXRayLiteManual_1.2_20121024.pdf"]

        self._programNames = {"mcxray_console_Release_32.exe": "console_mcxray.exe",
                        "mcxray_console_Release_64.exe": "console_mcxray_x64.exe",
                        "McXRay_Release_32.exe": "McXRay.exe",
                        "McXRay_Release_64.exe": "McXRay_x64.exe"}

    def _generateProgramName(self):
        programNames = self._programNames.keys()
        for programName in programNames:
            yield programName

    def _renameProgram(self, programName):
        return self._programNames[programName]

class PackageMCXRayLite(Package):
    FOLDER_CASINO_BIN = "bin"
    FOLDER_DLL = ""
    FOLDER_DOCUMENTATIONS = r"documentations/Manual"
    FOLDER_LICENSES = "licenses"
    PROGRAM_NAME = "McXRayLite"
    RESOURCE_FILEPATH = "MCXRay/McXRayLite.rc"

    NAME_MCXRAY = "MCXRayLite"

    def _initData(self):
        self._libraryFilenames = []
        self._documentFilenames = ["MCXRayLiteManual_1.2_20121024.pdf"]

        self._programNames = {"McXRayLite_Release_32.exe": "McXRayLite.exe",
                        "McXRayLite_Release_64.exe": "McXRayLite_x64.exe"}

    def _generateProgramName(self):
        programNames = self._programNames.keys()
        for programName in programNames:
            yield programName

    def _renameProgram(self, programName):
        return self._programNames[programName]

def handleRemoveReadonly(func, path, exc_info):
    """
    Error handler for ``shutil.rmtree``.

    If the error is due to an access error (read only file)
    it attempts to add write permission and then retries.

    If the error is for another reason it re-raises the error.

    Usage : ``shutil.rmtree(path, onerror=onerror)``
    """
    excvalue = exc_info[1]
    if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
        os.chmod(path, stat.S_IRWXU| stat.S_IRWXG| stat.S_IRWXO) # 0777
        func(path)
    elif not os.access(path, os.W_OK):
        # Is the error an access error ?
        os.chmod(path, stat.S_IWUSR)
        func(path)
    else:
        raise

def runMCXRayLite():
    logging.info("*"*30)
    logging.info("MCXRayLite")

    configurationFilepath = Files.getCurrentModulePath(__file__, "../pymcxray.cfg")
    try:
        releaseBasePath = Files.getBinPath(configurationFilepath, "mcxray/MCXRayLite")
        developmentPath = Files.getMCXRayDevPath(configurationFilepath)
    except IOError as message:
        logging.info(configurationFilepath)
        logging.error(message)

    package = PackageMCXRayLite(releaseBasePath, developmentPath, overWrite=True)
    package.run(isSimulationRunning=False)
    logging.info("*"*30)

def runMCXRay(packageName=None):
    logging.info("*"*30)
    logging.info("MCXRay")
    configurationFilepath = Files.getCurrentModulePath(__file__, "../pymcxray.cfg")
    try:
        releaseBasePath = Files.getBinPath(configurationFilepath, "mcxray/MCXRay")
        developmentPath = Files.getMCXRayDevPath(configurationFilepath)
    except IOError as message:
        logging.info(configurationFilepath)
        logging.error(message)

    package = PackageMCXRay(releaseBasePath, developmentPath, packageName=packageName, overWrite=True)
    package.run(isSimulationRunning=False)
    logging.info("*"*30)

def run():
    runMCXRayLite()
    runMCXRay()

if __name__ == '__main__':    #pragma: no cover
    import pyHendrixDemersTools.Runner as Runner
    Runner.Runner().run(runFunction=run)
