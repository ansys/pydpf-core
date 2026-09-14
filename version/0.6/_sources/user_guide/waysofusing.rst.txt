.. _user_guide_waysofusing:

=======================
DPF scripting languages
=======================
DPF is available as a standalone tool and as a tool in Ansys Mechanical. 
Each one uses a different language for scripting, so you should decide 
whether you want to use standalone DPF or DPF in Mechanical before 
creating any scripts. 

CPython
-------
Standalone DPF uses CPython and can be accessed with any Python console. 
Data can be exported to universal file formats, such as VTK, HDF5, and TXT
files. You can use it to generate TH-plots, screenshots, and animations or
to create custom result plots using `numpy <https://numpy.org/>`_
and `matplotlib <https://matplotlib.org/>`_ packages.

.. image:: ../images/drawings/dpf-reports.png

IronPython
----------
DPF in Mechanical uses IronPython and is accessible with the **ACT Console**. 
Use it to perform custom postprocessing and visualization of results directly 
within the Mechanical application.

.. image:: ../images/drawings/dpf-mech.png