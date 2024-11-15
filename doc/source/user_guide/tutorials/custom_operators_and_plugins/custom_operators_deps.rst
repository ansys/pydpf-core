To add third-party modules as dependencies to a plug-in package, you should create
and reference a folder or ZIP file with the sites of the dependencies in an XML file
located next to the folder for the plug-in package. The XML file must have the same
name as the plug-in package plus an ``.xml`` extension.

When the :py:func:`ansys.dpf.core.core.load_library` method is called, PyDPF-Core uses the
``site`` Python module to add custom sites to the path for the Python interpreter.


To create these custom sites, do the following:

#. Install the requirements of the plug-in package in a Python virtual environment.
#. Remove unnecessary folders from the site packages and compress them to a ZIP file.
#. Place the ZIP file in the plug-in package.
#. Reference the path to the ZIP file in the XML file as indicated above.

To simplify this step, you can add a requirements file in the plug-in package:

.. literalinclude:: /examples/07-python-operators/plugins/gltf_plugin/requirements.txt


For this approach, do the following:

#. Download the script for your operating system:

   - For Windows, download this :download:`PowerShell script </user_guide/tutorials/enriching_dpf_capabilities/create_sites_for_python_operators.ps1>`.
   - For Linux, download this :download:`Shell script </user_guide/tutorials/enriching_dpf_capabilities/create_sites_for_python_operators.sh>`.
  
3. Run the downloaded script with the mandatory arguments:

   - ``-pluginpath``: Path to the folder with the plug-in package.
   - ``-zippath``: Path and name for the ZIP file.
   
   Optional arguments are:

   - ``-pythonexe``: Path to a Python executable of your choice.
   - ``-tempfolder``: Path to a temporary folder to work in. The default is the environment variable
     ``TEMP`` on Windows and ``/tmp/`` on Linux.

#. Run the command for your operating system.

  - From Windows PowerShell, run:

    .. code-block::
   
       create_sites_for_python_operators.ps1 -pluginpath /path/to/plugin -zippath /path/to/plugin/assets/winx64.zip

  - From Linux Shell, run:

    .. code-block::

       create_sites_for_python_operators.sh -pluginpath /path/to/plugin -zippath /path/to/plugin/assets/linx64.zip

