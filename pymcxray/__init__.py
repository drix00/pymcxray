#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: __init__
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>


"""

# Standard library modules.
import os.path
import configparser
import logging
import fnmatch

# Third party modules.

# Local modules.

# Globals and constants variables.
__author__ = """Hendrix Demers"""
__email__ = 'hendrix.demers@mail.mcgill.ca'
__version__ = '0.1.3'

def get_current_module_path(module_path, relative_path=""):
    """
    Extract the current module path and combine it with the relative path and return it.

    :param str module_path: Pass the `__FILE__` python keyword for this parameter
    :param str relative_path: The relative path to combine with the module path
    :return: The path obtained when combine the module path and relative path
    :rtype: str
    """
    base_path = os.path.dirname(module_path)
    file_path = os.path.join(base_path, relative_path)
    file_path = os.path.normpath(file_path)

    return file_path

def create_path(path):
    """
    Create a path from the input string if does not exists.

    Does not try to distinct between file and directory in the input string.
    path = "dir1/filename.ext" => "dir1/filename.ext/"
    where the new directory "filename.ext" is created.

    :param str path: The path input string.
    :return: The path with the path separator at the end
    :rtype: str
    """
    path = os.path.normpath(path)
    if not os.path.exists(path):
        os.makedirs(path)

    if len(path) > 0 and path[-1] != os.sep:
        path += os.sep

    return path


def _read_path_from_configuration_file(configurationFile, relativePath, sectionName, keyName):
    path = read_value_from_configuration_file(configurationFile, sectionName, keyName)

    if relativePath.startswith('/'):
        relativePath = relativePath[1:]

    filepath = os.path.join(path, relativePath)
    filepath = os.path.normpath(filepath)
    return filepath

def read_value_from_configuration_file(configuration_file, section_name, key_name, default=None):
    """
    Read a value from an entry in a section from a configuration file.

    :param str configuration_file: The file path of the configuration file
    :param str section_name: Name of the section
    :param str key_name: Name of the entry to read
    :param default: Default value of the entry if not found
    :return: The value read or default value
    :rtype: str
    """
    config = configparser.SafeConfigParser()
    config.readfp(open(configuration_file))
    if config.has_section(section_name):
        if config.has_option(section_name, key_name):
            value = config.get(section_name, key_name)
            return value
        else:
            logging.error("Configuration file (%s) does not have this option in section %s: %s", configuration_file, key_name, section_name)
            if default == None:
                raise configparser.NoOptionError(key_name, section_name)
            else:
                return default
    else:
        logging.error("Configuration file (%s) does not have this section: %s", configuration_file, section_name)
        if default == None:
            raise configparser.NoSectionError(section_name)
        else:
            return default

def find_all_files(root, patterns='*', ignore_path_patterns='', ignore_name_patterns='',
                   single_level=False, yield_folders=False):
    """
    Find all files in a root folder.

    From Python Cookbook section 2.16 pages 88--90

    :param root:
    :param patterns:
    :param ignore_path_patterns:
    :param ignore_name_patterns:
    :param single_level:
    :param yield_folders:
    :return:
    """

    # Expand patterns from semicolon-separated string to list
    patterns = patterns.split(';')
    ignore_path_patterns = ignore_path_patterns.split(';')

    root = os.path.abspath(root)
    for path, subdirs, files in os.walk(root):
        if yield_folders:
            files.extend(subdirs)

        addPath = True
        for ignorePathPattern in ignore_path_patterns:
            if fnmatch.fnmatch(path, ignorePathPattern):
                addPath = False

        files.sort()

        for name in files:
            for pattern in patterns:
                if fnmatch.fnmatch(name, pattern):
                    addName = True
                    for ignorePattern in ignore_name_patterns:
                        if fnmatch.fnmatch(name, ignore_name_patterns):
                            addName = False

                    if addPath and addName:
                        yield os.path.join(path, name)
                        break

        if single_level:
            logging.debug("single_level")
            break

def get_mcxray_program_name(configuration_file_path, default=None):
    """
    Read the MCXRay program name in the configuration file.

    This option specify which executable to use in the script.
    The `console_mcxray_x64.exe` should be OK for most situation.
    If you have a 32-bit system, you have to use `console_mcxray.exe` (32-bit version).

    The configuration file need to have this entry in the section [Paths]:

    .. code-block:: console

        [Paths]
        mcxrayProgramName=console_mcxray_x64.exe

    :param str configuration_file_path: The fule path of the configuration file
    :param str default: Default value to use if the entry is not found
    :return: The MCXRay program name
    :rtype: str
    """
    section_name = "Paths"
    key_name = "mcxrayProgramName"

    program_name = read_value_from_configuration_file(configuration_file_path, section_name, key_name, default)

    return program_name

def get_results_mcgill_path(configuration_file_path, relative_path=""):
    """
    Read the results path for McGill in the configuration file.
    The results path read in the configuration file is combine with the `relative_path` and return.

    The configuration file need to have this entry in the section [Paths]:

    .. code-block:: console

        [Paths]
        resultsMcGillPath=D:\Dropbox\hdemers\professional\\results\simulations

    :param str configuration_file_path: The file path of the configuration file
    :param str relative_path: Relative path to add to the path read in the configuration file
    :return: Path where the simulation input and results will be written
    :rtype: str
    """

    section_name = "Paths"
    key_name = "resultsMcGillPath"

    file_path = _read_path_from_configuration_file(configuration_file_path, relative_path, section_name, key_name)

    return file_path

def get_mcxray_program_path(configuration_file_path, relative_path=""):
    """
    Read the MCXRay program path in the configuration file.

    The configuration file need to have this entry in the section [Paths]:

    .. code-block:: console

        [Paths]
        mcxrayProgramPath=C:\hdemers\codings\devcasino

    :param str configuration_file_path: The file path of the configuration file
    :param str relative_path: Relative path to add to the path read in the configuration file
    :return: Path where the mcxray program can be found.
    :rtype: str

    .. deprecated:: 0.1

    .. seealso:: function :py:func:`pymcxray.get_mcxray_archive_path`
    """
    section_name = "Paths"
    key_name = "mcxrayProgramPath"

    file_path = _read_path_from_configuration_file(configuration_file_path, relative_path, section_name, key_name)

    return file_path

def get_mcxray_archive_path(configuration_file_path, relative_path=""):
    """
    Read the MCXRay archive path in the configuration file.

    The configuration file need to have this entry in the section [Paths]:

    .. code-block:: console

        [Paths]
        mcxrayArchivePath=D:\Dropbox\hdemers\professional\softwareRelease\mcxray

    :param str configuration_file_path: The file path of the configuration file
    :param str relative_path: Relative path to add to the path read in the configuration file
    :return: Path where the mcxray archive can be found.
    :rtype: str
    """
    section_name = "Paths"
    key_name = "mcxrayArchivePath"

    file_path = _read_path_from_configuration_file(configuration_file_path, relative_path, section_name, key_name)

    return file_path

def get_mcxray_archive_name(configuration_file_path, default=None):
    """
    Read the MCXRay archive name in the configuration file.
    This option allows to choose which version of MCXRay to use for the simulations.

    The configuration file need to have this entry in the section [Paths]:

    .. code-block:: console

        [Paths]
        mcxrayArchiveName=2016-04-11_11h41m28s_MCXRay_v1.6.6.0.zip

    :param str configuration_file_path: The file path of the configuration file
    :param str default: Default value to use if the entry is not found
    :return: The MCXRay archive name
    :rtype: str
    """
    section_name = "Paths"
    key_name = "mcxrayArchiveName"

    program_name = read_value_from_configuration_file(configuration_file_path, section_name, key_name, default)

    return program_name
