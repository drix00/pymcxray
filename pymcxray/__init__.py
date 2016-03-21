#!/usr/bin/env python
"""
.. py:currentmodule:: __init__
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>


"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2012 Hendrix Demers"
__license__ = ""

# Standard library modules.
import os.path
import configparser
import logging
import fnmatch

# Third party modules.

# Local modules.

# Globals and constants variables.

def getCurrentModulePath(modulePath, relativePath=""):
    basepath = os.path.dirname(modulePath)
    #logging.debug(basepath)

    filepath = os.path.join(basepath, relativePath)
    #logging.debug(filepath)
    filepath = os.path.normpath(filepath)

    return filepath

def createPath(path):
    """
    Create a path from the input string if does not exists.

    Does not try to distinct between file and directory in the input string.
    path = "dir1/filename.ext" => "dir1/filename.ext/"
    where the new directory "filename.ext" is created.

    @param[in] path input string.

    @return the path with the path separator at the end.

    """
    path = os.path.normpath(path)
    if not os.path.exists(path):
        os.makedirs(path)

    if len(path) > 0 and path[-1] != os.sep:
        path += os.sep

    return path

def getBinPath(configurationFile, relativePath=""):
        """
        Read the configuration file for the works path.

        The configuration file need to have this entry:
        [Paths]
        binPath=C:\hdemers\bin

        """
        sectionName = "Paths"
        keyName = "binPath"

        filepath = _readPathFromConfigurationFile(configurationFile, relativePath, sectionName, keyName)

        return filepath

def getMCXRayDevPath(configurationFile, relativePath=""):
        """
        Read the configuration file for the MCXRay\Dev path.

        The configuration file need to have this entry:
        [Paths]
        mcxrayDevPath=J:\hdemers\work\mcgill2012\coding\MCXRay\mcxray-110218-hd\Dev

        """
        sectionName = "Paths"
        keyName = "mcxrayDevPath"

        filepath = _readPathFromConfigurationFile(configurationFile, relativePath, sectionName, keyName)

        return filepath

def _readPathFromConfigurationFile(configurationFile, relativePath, sectionName, keyName):
        path = readValueFromConfigurationFile(configurationFile, sectionName, keyName)

        if relativePath.startswith('/'):
            relativePath = relativePath[1:]

        filepath = os.path.join(path, relativePath)
        filepath = os.path.normpath(filepath)
        return filepath

def readValueFromConfigurationFile(configurationFile, sectionName, keyName, default=None):
        config = configparser.SafeConfigParser()
        config.readfp(open(configurationFile))
        if config.has_section(sectionName):
                if config.has_option(sectionName, keyName):
                        value = config.get(sectionName, keyName)
                        return value
                else:
                    logging.error("Configuration file (%s) does not have this option in section %s: %s", configurationFile, keyName, sectionName)
                    if default == None:
                        raise configparser.NoOptionError(keyName, sectionName)
                    else:
                        return default
        else:
            logging.error("Configuration file (%s) does not have this section: %s", configurationFile, sectionName)
            if default == None:
                raise configparser.NoSectionError(sectionName)
            else:
                return default

def findAllFiles(root, patterns='*', ignorePathPatterns='', ignoreNamePatterns='', single_level=False, yield_folders=False):
    """
    Find all files in a root folder.

    From Python Cookbook section 2.16 pages 88--90

    Mandatory arguments:


    Optional arguments:


    Extra arguments:


    Return parameters:

    """
    # Expand patterns from semicolon-separated string to list
    patterns = patterns.split(';')
    ignorePathPatterns = ignorePathPatterns.split(';')

    root = os.path.abspath(root)
    for path, subdirs, files in os.walk(root):
        if yield_folders:
            files.extend(subdirs)

        addPath = True
        for ignorePathPattern in ignorePathPatterns:
            if fnmatch.fnmatch(path, ignorePathPattern):
                addPath = False

        files.sort()

        for name in files:
            for pattern in patterns:
                if fnmatch.fnmatch(name, pattern):
                    addName = True
                    for ignorePattern in ignoreNamePatterns:
                        if fnmatch.fnmatch(name, ignoreNamePatterns):
                            addName = False

                    if addPath and addName:
                        yield os.path.join(path, name)
                        break

        if single_level:
            logging.debug("single_level")
            break

def getMCXRayProgramName(configurationFile, default=None):
        """
        Read the configuration file for the MCXRay program name.

        The configuration file need to have this entry:
        [Paths]
        mcxrayProgramName=McXRayLite.exe

        """
        sectionName = "Paths"
        keyName = "mcxrayProgramName"

        programName = readValueFromConfigurationFile(configurationFile, sectionName, keyName, default)

        return programName

def getResultsMcGillPath(configurationFile, relativePath=""):
        """
        Read the configuration file for the results path for McGill.

        The configuration file need to have this entry:
        [Paths]
        resultsMcGillPath=/home/hdemers/resultsUdeS

        """
        sectionName = "Paths"
        keyName = "resultsMcGillPath"

        filepath = _readPathFromConfigurationFile(configurationFile, relativePath, sectionName, keyName)

        return filepath

def getMCXRayProgramPath(configurationFile, relativePath=""):
        """
        Read the configuration file for the MCXRay program path.

        The configuration file need to have this entry:
        [Paths]
        mcxrayProgramPath=C:\hdemers\codings\devcasino

        """
        sectionName = "Paths"
        keyName = "mcxrayProgramPath"

        filepath = _readPathFromConfigurationFile(configurationFile, relativePath, sectionName, keyName)

        return filepath

def getMCXRayArchivePath(configurationFile, relativePath=""):
        """
        Read the configuration file for the MCXRay archive path.

        The configuration file need to have this entry:
        [Paths]
        mcxrayArchivePath=C:\hdemers\bin\mcxray\MCXRay\archives

        """
        sectionName = "Paths"
        keyName = "mcxrayArchivePath"

        filepath = _readPathFromConfigurationFile(configurationFile, relativePath, sectionName, keyName)

        return filepath

def getMCXRayArchiveName(configurationFile, default=None):
        """
        Read the configuration file for the MCXRay archive name.

        The configuration file need to have this entry:
        [Paths]
        mcxrayArchiveName=2012-05-10_16h26m07s_MCXRay_v1.1.1.1.zip

        """
        sectionName = "Paths"
        keyName = "mcxrayArchiveName"

        programName = readValueFromConfigurationFile(configurationFile, sectionName, keyName, default)

        return programName
