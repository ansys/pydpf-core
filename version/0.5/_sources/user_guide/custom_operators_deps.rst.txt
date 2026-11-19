To add third party modules as dependencies to a custom DPF python plugin, a folder or zip file
with the sites of the dependencies needs to be created and referenced in an xml located next to the plugin's folder
and having the same name as the plugin plus the ``.xml`` extension. The ``site`` python module is used by DPF when
calling :py:func:`ansys.dpf.core.core.load_library` function to add these custom sites to the python interpreter path.
To create these custom sites, the requirements of the custom plugin should be installed in a python virtual
environment, the site-packages (with unnecessary folders removed) should be zipped and put with the plugin. The
path to this zip should be referenced in the xml as done above.

To simplify this step, a requirements file can be added in the plugin, like:

.. dropdown:: requirements.txt

   .. literalinclude:: /examples/07-python-operators/plugins/gltf_plugin/requirements.txt

And this :download:`powershell script </user_guide/create_sites_for_python_operators.ps1>` for windows or
this :download:`shell script </user_guide/create_sites_for_python_operators.sh>` can be ran with the mandatory arguments:

- -pluginpath : path to the folder of the plugin.
- -zippath : output zip file name.

optional arguments are:

- -pythonexe : path to a python executable of your choice.
- -tempfolder : path to a temporary folder to work on, default is the environment variable ``TEMP`` on Windows and /tmp/ on Linux.

For windows powershell, call::

    create_sites_for_python_operators.ps1 -pluginpath /path/to/plugin -zippath /path/to/plugin/assets/winx64.zip

For linux shell, call::

   create_sites_for_python_operators.sh -pluginpath /path/to/plugin -zippath /path/to/plugin/assets/linx64.zip
