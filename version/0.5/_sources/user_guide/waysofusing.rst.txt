.. _user_guide_waysofusing:

=================
Ways of Using DPF
=================
DPF is available as a standalone tool and as a tool in Ansys Mechanical. 
Each one uses a different language for scripting, so you should decide 
whether you want to use standalone DPF or DPF in Mechanical before 
creating any scripts. 

``Standalone DPF`` uses CPython and can be accessed via any Python console. 
Data can be exported to universal file formats (VTK, hdf5, txt files). 
Use it to generate TH-plots, screenshots, animations, and so on, or create 
custom results plots using numpy and matplotlib libraries.

.. image:: ../images/drawings/dpf-reports.png

``DPF in Mechanical`` uses IronPython and is accessible via the ACT console. 
Use it to perform custom postprocessing and visualization of results directly 
within the Mechanical application.

.. image:: ../images/drawings/dpf-mech.png