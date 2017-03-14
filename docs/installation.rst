.. highlight:: shell

============
Installation
============


.. _stable-release-section:

Stable release
--------------

.. todo:: Add pypi installation for this project.

.. warning::

    Right now, the :ref:`Stable release <stable-release-section>` installation does not work.

To install pymcxray, run this command in your terminal:

.. code-block:: console

    $ pip install pymcxray

This is the preferred method to install pymcxray, as it will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


For developer
-------------

Clone the public repository:

.. code-block:: console

    $ git clone git://github.com/drix00/pymcxray

Go in the project folder and install it with pip in developer mode:

.. code-block:: console

    $ cd pymcxray
    $ pip install -e .

.. note::

   The project use Git LFS for the test data file. Follow the information on `Git LFS <https://git-lfs.github.com/>`_
   to get the test data when the repository is pull.

From sources
------------

The sources for pymcxray can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/drix00/pymcxray

Or download the `tarball`_:

.. code-block:: console

    $ curl  -OL https://github.com/drix00/pymcxray/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install


.. _Github repo: https://github.com/drix00/pymcxray
.. _tarball: https://github.com/drix00/pymcxray/tarball/master
