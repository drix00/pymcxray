=====
Usage
=====

To use pymcxray in a project look in the `examples` folder.

To run the example, you need to specify the task you want to do.

.. code-block:: console

   $python simulation_test_maps.py generate

.. note::

   On windows use the ``py`` command and not ``python`` if you have more than one python version installed.

Currently these tasks are available:

* ``generate``
* ``check``
* ``read``
* ``analyze``
* ``scheduled_read``

At first, the script may look complex, but starting with a previous script it is easy to create a new script
for you simulation.

Each script has two parts:

* a class that subclass `mcxray._Simulations` were
    - the simulation parameters are specified
    - results needed extracted from the simulation
    - analysis of the results can be done (this can be also done in another script)
* a main section were
    - batch files are generated for the simulation
    - the different task are selected using commend line argument.

.. note::

    These two parts could be separate in two python script (file) without problem. But it seem more logical to kept
    them together and only have one python script file.

--------------------
simulation_test_maps
--------------------

To explain this example, we are going to start from the main section.

The batch file is define in a run method, which is called by the `__main__`, i.e., only run if the script is called
from the command line, but not run if imported.

When the script is ready, these task are run in that order:

#. ``generate``
#. ``check``
#. ``read``
#. ``analyze``

.. code-block:: console

   $python simulation_test_maps.py generate

Start the batch files in parallel. It is easier to just select them all in Windows Explorer and
right-click and open them.

.. code-block:: console

   BatchSimulationTestMapsMM2017_1.bat
   BatchSimulationTestMapsMM2017_2.bat

To check the progress of all simulations, i.e., how many simulations are done and todo

.. code-block:: console

   $python simulation_test_maps.py check

When all simulations are done, extract the results and save it in a hdf5 file.

.. code-block:: console

   $python simulation_test_maps.py read

The specified results can be analysed using the script (from the hdf5 file) or
analysed using another script. For example, xray-spectrum-modeling project analyse the hdf5 file
generate by this script.

An alternative to use the command line argument for these tasks, it to add them directly
in the script and uncommenting the task you want to run in the main section of the script.

.. code-block:: python

    if __name__ == '__main__': #pragma: no cover
        import sys
        ...
        if len(sys.argv) == 1:
            sys.argv.append(mcxray.ANALYZE_TYPE_GENERATE_INPUT_FILE)
            #sys.argv.append(mcxray.ANALYZE_TYPE_CHECK_PROGRESS)
            #sys.argv.append(mcxray.ANALYZE_TYPE_ANALYZE_RESULTS)
            #sys.argv.append(mcxray.ANALYZE_TYPE_ANALYZE_SCHEDULED_READ)
        ...

By default the logging level is set at `logging.WARN` and above, but `pymcxray` gives a lot information
at the `logging.INFO` level so it is recommanded to set the logger level as follow

.. code-block:: python

    ...
    logging.getLogger().setLevel(logging.INFO)
    ...

The complete `__main__` is given below

.. code-block:: python

    if __name__ == '__main__': #pragma: no cover
        import sys
        logging.getLogger().setLevel(logging.INFO)
        logging.info(sys.argv)
        if len(sys.argv) == 1:
            sys.argv.append(mcxray.ANALYZE_TYPE_GENERATE_INPUT_FILE)
            #sys.argv.append(mcxray.ANALYZE_TYPE_CHECK_PROGRESS)
            #sys.argv.append(mcxray.ANALYZE_TYPE_ANALYZE_RESULTS)
            #sys.argv.append(mcxray.ANALYZE_TYPE_ANALYZE_SCHEDULED_READ)
        run()

The ``run`` method have three components

* a configuration file, see :ref:`Configuration file`
* a batch file object, see :ref:`Batch file`
* one or more simulation subclass, see :ref:`Simulation subclass`

Here is a example of a complete ``run`` method

.. code-block:: python

    def run():
        # import the batch file class.
        from pymcxray.BatchFileConsole import BatchFileConsole

        # Find the configuration file path
        configuration_file_path = get_current_module_path(__file__, "MCXRay_latest.cfg")
        program_name = get_mcxray_program_name(configuration_file_path)

        # Create the batch file object.
        batch_file = BatchFileConsole("BatchSimulationTestMapsMM2017", program_name, numberFiles=10)

        # Create the simulation object and add the batch file object to it.
        analyze = SimulationTestMapsMM2017(relativePath=r"mcxray/SimulationTestMapsMM2017",
                                           configurationFilepath=configuration_file_path)
        analyze.run(batch_file)

------------------
Configuration file
------------------

The configuration file is a ini style configuration file for using pymcxray.
It define the paths needed to generate and run the simulations.

.. code-block:: console

    [Paths]
    mcxrayProgramName=console_mcxray_x64.exe
    resultsMcGillPath=D:\Dropbox\hdemers\professional\results\simulations
    mcxrayArchivePath=D:\Dropbox\hdemers\professional\softwareRelease\mcxray
    mcxrayArchiveName=2016-04-11_11h41m28s_MCXRay_v1.6.6.0.zip

See the documentation of these functions for more detail on each option

* :py:func:`pymcxray.get_mcxray_program_name`
* :py:func:`pymcxray.get_results_mcgill_path`
* :py:func:`pymcxray.get_mcxray_program_path`
* :py:func:`pymcxray.get_mcxray_archive_path`

----------
Batch file
----------

The batch file is responsible to create the simulation structure with a copy of mcxray program.
Batch files are generated to easily run the simulations.
One important parameter to set is the `numberFiles`, this is the number of batch files generated
and that can be run in parallel. For maximum efficiency it should be set as the number of logical processors minus 1 or 2.
For example, on a computer with 12 logical processors, the `numberFiles` should be set at 10.

See :py:class:`pymcxray.BatchFileConsole.BatchFileConsole` documentation for more information about the other parameters.

-------------------
Simulation subclass
-------------------

The simulation subclass allows to generate a lot of simulations by varying simulations parameters.

The main features are

* generate input files
    - regenerate input files of simulations not done
* check the progress of the simulations: done and todo
* extract results from the completed simulation
    - save the results in a hdf5 file for easier analysis
* optionally do the analysis of the results

To do that the user need to subclass :py:class:`pymcxray.mcxray._Simulations`
and overwrite these method

* :py:meth:`pymcxray.mcxray._Simulations._initData` (required)
* :py:meth:`pymcxray.mcxray._Simulations.getAnalysisName` (required)
* :py:meth:`pymcxray.mcxray._Simulations.createSpecimen` (required)
* :py:meth:`pymcxray.mcxray._Simulations.read_one_results_hdf5` (optional)
* :py:meth:`pymcxray.mcxray._Simulations.analyze_results_hdf5` (optional)

.. warning::

    If any of the required method is modified, the simulation have to be redone completely.
    It is recommended to just delete the root path for the analysis and generate the input files and do the simulations.
    For this example, delete `SimulationTestMapsMM2017` folder.

.. warning::

    If :py:meth:`pymcxray.mcxray._Simulations.read_one_results_hdf5` is modified.
    In some case, the hdf5 need to be deleted.1
    Furthermore, if the results were deleted: `delete_result_files` is `True`, the simulation have to be redone.

Below are given example for each method, for more detail see the method documentation.

Init data
`````````
This method is used to specify the options for the analysis and also the parameters used in the simulations.

The most important options for the anslysis are:

* `use_hdf5` to use the recommended hdf5 method. If it is `False` the older serial method will be used.
* `delete_result_files` if it is `True`, the result file are deleted after added in the hdf5 file. Very useful when creating a lot files like for a map.
* `createBackup` if `True` create a backup of the hdf5 file before adding more results to it. Usefull to not loss data in case of error or crash, but you should delete backup file manually as they can take a lot of space.

.. warning::

    If `delete_result_files` is `True`, all results are deleted for a simulation and only the results specified in :py:meth:`pymcxray.mcxray._Simulations.read_one_results_hdf5` are kept.
    If :py:meth:`pymcxray.mcxray._Simulations.read_one_results_hdf5` is modified to extract more results, the simulation have to be simulate again.

This is the recommended values for the options, only change them when you are sure everything is working OK.

.. code-block:: python

    def _initData(self):
        self.use_hdf5 = True
        self.delete_result_files = False
        self.createBackup = True

The simulation parameters are specified in this method.

.. note::

    If not specified, the script use MCXRay default parameters.
    Start MCXRay program to see the default value of each parameters.

To change simulation parameters, create a :py:class:`pymcxray.SimulationsParameters.SimulationsParameters` object

.. code-block:: python

        self._simulationsParameters = SimulationsParameters()

Two kinds of parameter can be added:

* varied specified with a list of values
* fixed specified with a single value

The script will automatically generate a simulation for all combination of the varied parameters.

.. warning::

    Adding a lot of varied parameters with a lot of values can generate a lot of simulations.
    Above 1000 simulations, all tasks of the script will be slow because of the generation or reading of a lot of files.
    It is recommended to start with 2 or 3 varied parameters and short list of values and test all tasks of the script.
    When the tests are OK and results make sense, you can increase the list of values.
    To add more varied parameters, it is receommended to create a new script with again only 2 or 3 varied parameters.

The parameters that can be added are defined as keyword starting with `PARAMETER_` in the module :py:mod:`pymcxray.SimulationsParameters`.
If you don't find the parameter you want request an "enhancement" at https://github.com/drix00/pymcxray/issues.

Here is an example how-to add simulation parameters

.. code-block:: python

    from pymcxray.SimulationsParameters import SimulationsParameters, PARAMETER_INCIDENT_ENERGY_keV, PARAMETER_NUMBER_ELECTRONS, \
    PARAMETER_BEAM_POSITION_nm, PARAMETER_NUMBER_XRAYS
    ...

    class SimulationTestMapsMM2017(mcxray._Simulations):
        def _initData(self):
            ...

            # Local variables for value and list if values.
            energy_keV = 30.0
            number_electrons = 10000

            #number_xrays_list = [10, 20, 30, 50, 60, 100, 200, 500, 1000]
            number_xrays_list = [10]
            xs_nm = np.linspace(-5.0e3, 5.0e3, 3)
            probePositions_nm = [tuple(position_nm) for position_nm in np.transpose([np.tile(xs_nm, len(xs_nm)), np.repeat(xs_nm, len(xs_nm))]).tolist()]

            # Simulation parameters
            self._simulationsParameters = SimulationsParameters()

            self._simulationsParameters.addVaried(PARAMETER_NUMBER_XRAYS, number_xrays_list)
            self._simulationsParameters.addVaried(PARAMETER_BEAM_POSITION_nm, probePositions_nm)

            self._simulationsParameters.addFixed(PARAMETER_INCIDENT_ENERGY_keV, energy_keV)
            self._simulationsParameters.addFixed(PARAMETER_NUMBER_ELECTRONS, number_electrons)

Analysis name
`````````````
This method specify the name of the analysis or experiment for which the simulation are done.
Normally similar to the name of the class and mostly used as basename for the input files and result files.
In case of two scripts writing the same path, it allows to differentiate them, but it is not recommended to run two scripts in the same folde.

.. code-block:: python

    class SimulationTestMapsMM2017(mcxray._Simulations):
        ...
        def getAnalysisName(self):
            return "SimulationTestMapsMM2017"
        ...

Create specimen
```````````````

This method is used to create the specimen for each simulation.
The argument of the method contains the option of the specific simulation and can be used to create the specimen.
The :py:mod:`pymcxray.Simulation.Simulation` module contains predefined specimen which can be use in this method.

Here an example how-to use the `parameters` argument and the predefined specimen

.. code-block:: python

    def createSpecimen(self, parameters):
        weightFractions = parameters[PARAMETER_WEIGHT_FRACTIONS]

        elements = [(self.atomicNumberA, weightFractions[0]),
                    (self.atomicNumberB, weightFractions[1])]
        specimen = Simulation.createAlloyBulkSample(elements)
        return specimen

A more complex example, where each region are specified is given below

.. code-block:: python

    def createSpecimen(self, parameters):
        # Create the specimen with a name and number of regions.
        specimen = Specimen.Specimen()
        specimen.name = "Maps01"
        specimen.numberRegions = 10

        # Region 0
        region = Region.Region()
        region.numberElements = 0
        region.regionType = RegionType.REGION_TYPE_BOX
        parameters = [-10000000000.0, 10000000000.0, -10000000000.0, 10000000000.0, 0.0, 20000000000.0]
        region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
        specimen.regions.append(region)

        # Region 1
        region = Region.Region()
        region.numberElements = 2
        region.elements = [Element.Element(27, massFraction=0.01), Element.Element(26, massFraction=0.99)]
        region.regionType = RegionType.REGION_TYPE_BOX
        parameters = [-7.5e4, -2.5e4, -7.5e4, -2.5e4, 0.0, 0.2e4]
        region.regionDimensions = RegionDimensions.RegionDimensionsBox(parameters)
        specimen.regions.append(region)
        ...

.. warning::

    Creating a specimen in MCXRay is complicate as sometime you need to create a empty region 0.
    Look at the predefined specimen in :py:mod:`pymcxray.Simulation.Simulation` for help.
    Drawing the trajectory with the :py:mod:`FileFormat.Results.ElectronTrajectoriesResults` will help debug the specimen.
    You can also request a "help wanted" at https://github.com/drix00/pymcxray/issues.

Read one simulation results
```````````````````````````

This method extract results from one complete simulation and added them in a hdf5 group for this simulation.
The result that can be extracted are in the package :py:mod:`pymcxray.FileFormat.Results`
and only the class implementing :py:meth:`write_hdf5` can be extracted.
If the desired results does not implement the :py:meth:`write_hdf5` method, request an "enhancement" at https://github.com/drix00/pymcxray/issues.

.. note::

    The format of the hdf5 file is not well documented.
    Check the implementation of the :py:meth:`write_hdf5` method and request an "enhancement"
    at https://github.com/drix00/pymcxray/issues for the documentation.

.. note::

    The program HDFView is useful to look at the hdf5 file. See https://support.hdfgroup.org/products/java/hdfview/.

Here is an example how-to extract the electron results (BSE, TE, ...)

.. code-block:: python

    def read_one_results_hdf5(self, simulation, hdf5_group):
        electronResults = ElectronResults.ElectronResults()
        electronResults.path = self.getSimulationsPath()
        electronResults.basename = simulation.resultsBasename
        electronResults.read()
        electronResults.write_hdf5(hdf5_group)

So far this class are implemented with hdf5 support

* :py:class:`pymcxray.FileFormat.Results.ElectronResults.ElectronResults`
* :py:class:`pymcxray.FileFormat.Results.PhirhozEmittedCharacteristic.PhirhozEmittedCharacteristic`
* :py:class:`pymcxray.FileFormat.Results.PhirhozGeneratedCharacteristic.PhirhozGeneratedCharacteristic`
* :py:class:`pymcxray.FileFormat.Results.PhirhozGeneratedCharacteristicThinFilm.PhirhozGeneratedCharacteristicThinFilm`
* :py:class:`pymcxray.FileFormat.Results.XrayIntensities.XrayIntensities`
* :py:class:`pymcxray.FileFormat.Results.XraySpectraRegionsEmitted.XraySpectraRegionsEmitted`
* :py:class:`pymcxray.FileFormat.Results.XraySpectraSpecimenEmittedDetected.XraySpectraSpecimenEmittedDetected`

Analyze all simulations
````````````````````````

This method is only needed for the task ``analyze``.

Often the method start by calling :py:meth:`mcxray._Simulations.readResults` to read all new results and add them in the hdf5 file.

The example below shows how-to open the hdf5 file in memory for somewhat fast analysis simulation.
The file is read only at the beginning and stored in memory.

.. code-block:: python

    def analyze_results_hdf5(self): #pragma: no cover
        self.readResults()

        file_path = self.get_hdf5_file_path()
        with h5py.File(file_path, 'r', driver='core') as hdf5_file:
            hdf5_group = self.get_hdf5_group(hdf5_file)
            logging.info(hdf5_group.name)

.. todo:: Document :py:mod:`pymcxray.mcxray`
.. todo:: Document :py:mod:`pymcxray.SimulationsParameters`
.. todo:: Document :py:mod:`pymcxray.Simulation`
.. todo:: Document :py:class:`pymcxray.FileFormat.Results.ElectronResults.ElectronResults`
.. todo:: Document :py:class:`pymcxray.FileFormat.Results.PhirhozEmittedCharacteristic.PhirhozEmittedCharacteristic`
.. todo:: Document :py:class:`pymcxray.FileFormat.Results.PhirhozGeneratedCharacteristic.PhirhozGeneratedCharacteristic`
.. todo:: Document :py:class:`pymcxray.FileFormat.Results.PhirhozGeneratedCharacteristicThinFilm.PhirhozGeneratedCharacteristicThinFilm`
.. todo:: Document :py:class:`pymcxray.FileFormat.Results.XrayIntensities.XrayIntensities`
.. todo:: Document :py:class:`pymcxray.FileFormat.Results.XraySpectraRegionsEmitted.XraySpectraRegionsEmitted`
.. todo:: Document :py:class:`pymcxray.FileFormat.Results.XraySpectraSpecimenEmittedDetected.XraySpectraSpecimenEmittedDetected`


