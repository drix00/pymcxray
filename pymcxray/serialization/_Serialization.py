#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2011 Hendrix Demers"
__license__ = ""

# Standard library modules.
import os.path
import logging
import stat
import shutil
import datetime

# Third party modules.

# Local modules.

# Project modules

# Globals and constants variables.

class _Serialization(object):
    def __init__(self, filename=None, verbose=True):
        # Set default.
        self._currentVersion = "0.0"
        self._fileVersion = ""

        self._pathname = None
        self._filename = None
        self._filepath = None

        self._verbose = verbose

        if filename:
            self.setFilename(filename)

    def setPathname(self, pathname):
        self._pathname = pathname

    def setFilename(self, filename):
        extension = self._getSerializationExtension()
        if not filename.endswith(extension):
            basename, dummy_extension = os.path.splitext(filename)
            filename = basename + extension

        self._filename = filename

    def setBasename(self, basename):
        self._filename = basename + self._getSerializationExtension()

    def _getSerializationExtension(self):
        return ".ser"

    def setFilepath(self, filepath):
        extension = self._getSerializationExtension()
        if not filepath.endswith(extension):
            basename, dummy_extension = os.path.splitext(filepath)
            filepath = basename + extension

        self._filepath = filepath

    def getFilepath(self):
        if self._filepath is not None:
            return self._filepath
        elif self._filename is None:
            message = "_filename not set."
            raise ValueError(message)
        elif self._pathname is None:
            return self._filename
        else:
            filepath = os.path.join(self._pathname, self._filename)
            filepath = os.path.normpath(filepath)
            return filepath

    def setCurrentVersion(self, version):
        if not isinstance(version, str):
            message = "version argument should be a string"
            raise TypeError(message)

        self._currentVersion = version

    def getCurrentVersion(self):
        return self._currentVersion

    def deleteFile(self):
        if self.isFile():
            filepath = self.getFilepath()
            if self._verbose:
                logging.info("Removing serialization file: %s.", filepath)

            os.remove(filepath)

    def isFile(self):
        filepath = self.getFilepath()
        isFile = os.path.isfile(filepath)
        return isFile

    def isOlderThan(self, filepath):
        if not self.isFile():
            return True

        if not os.path.isfile(filepath):
            return False

        filepathSerilization = self.getFilepath()

        statSerilization = os.stat(filepathSerilization)
        statOtherFile = os.stat(filepath)

        logging.debug("MTIME: o(%s) s(%s)", statOtherFile[stat.ST_MTIME], statSerilization[stat.ST_MTIME])
        logging.debug("CTIME: o(%s) s(%s)", statOtherFile[stat.ST_CTIME], statSerilization[stat.ST_CTIME])

        if statOtherFile[stat.ST_MTIME] > statSerilization[stat.ST_MTIME]:
            return True
        elif statOtherFile[stat.ST_CTIME] > statSerilization[stat.ST_MTIME] and statOtherFile[stat.ST_CTIME] > statSerilization[stat.ST_CTIME]:
            return True
        else:
            return False

        # todo: implement a true test for the version of the file and the current version of serialization object.
        #if self._currentVersion != self._fileVersion:
        #    return True

    def isNewVersion(self):
        if self._currentVersion > self._fileVersion:
            return True
        else:
            return False

    def load(self):
        raise NotImplementedError

    def save(self, serializedData):
        raise NotImplementedError

    def backupFile(self, suffix=None):
        sourceFilepath = self.getFilepath()

        if os.path.isfile(sourceFilepath):
            if suffix is None:
                suffix = self._generateTimeStamp()

            if suffix != "":
                destinationFilepath = sourceFilepath + "_" + suffix + ".bak"
            else:
                destinationFilepath = sourceFilepath + ".bak"

            shutil.copy2(sourceFilepath, destinationFilepath)
            logging.info("Backup created: %s", destinationFilepath)

    def _generateTimeStamp(self):
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
