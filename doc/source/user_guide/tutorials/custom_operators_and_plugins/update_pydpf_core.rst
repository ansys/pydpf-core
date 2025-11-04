
Install module
--------------

Once an Ansys-unified installation is complete, you must install the ``ansys-dpf-core`` module in the Ansys
installer's Python interpreter.

#. Download the script for you operating system:

   - For Windows, download this :download:`PowerShell script </user_guide/tutorials/enriching_dpf_capabilities/install_ansys_dpf_core_in_ansys.ps1>`.
   - For Linux, download this :download:`Shell script </user_guide/tutorials/enriching_dpf_capabilities/install_ansys_dpf_core_in_ansys.sh>`

#. Run the downloaded script for installing with optional arguments:

   - ``-awp_root``: Path to the Ansys root installation folder. For example, the 2023 R1 installation folder ends
     with ``Ansys Inc/v231``, and the default environment variable is ``AWP_ROOT231``.
   - ``-pip_args``: Optional arguments to add to the ``pip`` command. For example, ``--index-url`` or
     ``--trusted-host``.

If you ever want to uninstall the ``ansys-dpf-core`` module from the Ansys installation, you can do so.

#. Download the script for your operating system:

   - For Windows, download this :download:`PowerShell script </user_guide/tutorials/enriching_dpf_capabilities/uninstall_ansys_dpf_core_in_ansys.ps1>`.
   - For Linux, download this :download:`Shell script </user_guide/tutorials/enriching_dpf_capabilities/uninstall_ansys_dpf_core_in_ansys.sh>`.

#. Run the downloaded script for uninstalling with the optional argument:

   - ``-awp_root``: Path to the Ansys root installation folder.  For example, the 2023 R1 installation folder ends
     with ``Ansys Inc/v231``, and the default environment variable is ``AWP_ROOT231``.