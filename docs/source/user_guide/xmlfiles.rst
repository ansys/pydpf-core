.. _user_guide_xmlfiles:

=============
DPF XML files
=============
This page describes the ``DataProcessingCore.xml`` and ``Plugin.xml`` XML files
provided with DPF. These XML files work on both Linux and Windows
because they contain content for both of these operating systems.

These XML files must be located alongside the plugin DLL files on Windows or
SO files on Linux.

``DataProcessingCore.xml`` file
-------------------------------
The ``DataProcessingCore.xml`` file provides for configuring the plugins to load.

Here is the content of this XML file:

.. code-block:: html

	<?xml version="1.0"?> 
	<DPF version="1.0"> 
		<Environment> 
			<Linux> 
				<ANSYS_ROOT_FOLDER>/usr/local/ansys_inc/v222</ANSYS_ROOT_FOLDER> 
			</Linux> 
			<Windows> 
				<ANSYS_ROOT_FOLDER>E:\ANSYSDev\ANSYS Inc\v222</ANSYS_ROOT_FOLDER> 
			</Windows> 
		</Environment> 
		<DefaultPlugins> 
			<Linux> 
				<native> 
					<Path>libAns.Dpf.Native.so</Path> 
					<Loader>LoadOperators</Loader>	 
					<UsePluginXml>false</UsePluginXml> 
				</native> 
			</Linux> 
			<Windows> 
				<Debug> 
					<native> 
						<Path>$(THIS_XML_FOLDER)\Ans.Dpf.NativeD.dll</Path> 
						<Loader>LoadOperators</Loader> 
					</native> 
				</Debug> 
				<Release> 
					<native> 
						<Path>Ans.Dpf.Native.dll</Path> 
						<Loader>LoadOperators</Loader> 
					</native> 
					<fem_utils> 
						<Path>$(THIS_XML_FOLDER)\Ans.Dpf.FEMUtils.dll</Path> 
						<Loader>LoadOperators</Loader> 
						<UsePluginXml>true</UsePluginXml> 
					</fem_utils> 
				</Release> 
			</Windows> 
		</DefaultPlugins> 
	</DPF> 	


In this XML file, some of the elements are optional, and many of the
elements have Linux-specific versus Windows-specific child elements.

.. caution::
	To ensure that DPF operates correctly, modify this XML file
	carefully. All paths specified in this XML file must adhere to the path
	conventions of the respective operating system. For Linux paths, use
	forward slashes (/). For Windows paths, use backward slashes (\\). 


``<Environment>`` element
~~~~~~~~~~~~~~~~~~~~~~~~~
The ``<Environment>`` element is used only for defining the root folder
of the Ansys software. Its child ``<ANSYS_ROOT_FOLDER>`` elements can
define the root folders for Ansys software installed on Linux and on Windows.

The path for the root folder ends with Ansys version information, ``v###``,
where ``###`` is the three-digit format for the installed version. For example,
on Windows, the path for the root folder for Ansys 2022 R2 likely ends with
``\ANSYS Inc\v222``.

The ``ANSYS_ROOT_FOLDER`` element defines a variable 
that can be used in the other XML files. For example, you might use it to find required
third-party software.

If the ``ANSYS_ROOT_FOLDER`` element is not defined in the ``DataProcessing.xml``
file, an attempt is made to
find the root folder relative to the ``DataProcessingCore`` DLL or SO file. This
works only if the ``DataProcessingCore.xml`` file is located in its default
location.

If the ``ANSYS_ROOT_FOLDER`` element is still not defined, the root folder is 
determined by reading the ``AWP_ROOT###`` environment variable specific to your 
installed Ansys version. For example, if you are using Ansys 2022 R2, it looks 
for the ``AWP_ROOT222`` environment variable to find the root folder.

ANSYS_ROOT_FOLDER is not an environment variable and cannot be set accordingly.

``<DefaultPlugin>`` element
~~~~~~~~~~~~~~~~~~~~~~~~~~~
The ``<DefaultPlugin>`` element defines the plugins to load. The ``<Linux>`` or
``<Windows>`` child element contains the operating system for the plugins defined
in the child elements.

The ``<native>`` element defines DPF native operators. The further subdividing of
plugins into ``<Debug>`` or ``<Release>`` elements is optional. The ``<Debug>``
element, for example, would only be used with a debug version of the
``DataProcessingCore DLL/SO`` file.

The element names for plugins, such as ``<native>`` and ``<fem_utils>``, are used as 
**keys** when loading plugins. Each plugin must have a unique key.

The element for each plug-in has child elements:

- ``<Path>``: Contains the location of the plugin to load. The normal mechanism
  that the operating system uses to find a DLL or SO file is used. The DLL
  file could be in the Windows path, or the SO file could be in the Linux
  ``LD_LIBRARY_PATH`` system environment variable.
- ``<Loader>``: Contains how the plugin is loaded. Only ``LoadOperators`` is
  supported. It loads all operators within the plugin.
- ``<UsePluginXml>``: Contains a ``true`` or  ``false`` value that indicates
  whether to use the ``PLUGIN.XML`` file defined in the next element to load
  the plugin. This element is optional. The default value is ``true``.

To provide an absolute path to a plugin, you can use these predefined variables:

- ``ANSYS_ROOT_FOLDER``, which is described in the preceding section.
- ``THIS_XML_FOLDER``, which defines the location of where the current XML file
  is located. In this case, it defines the location of the ``DataProcessingCore.xml``
  file.

You can also use any other environment variable. For example, if you always have your
plugins in a folder defined by a ``MY_PLUGINS`` environment variable, you could use
it in the XML file.

You specify environment variables in the same way as the ``ANSYS_ROOT_FOLDER``
or ``THIS_XML_FOLDER`` variable. They are defined as ``$(…)``.

In the Ansys installation, the default ``DataProcessingCore.xml`` file is located
next to the ``DataProcessingCore`` DLL or SO file. If you want to use a different
one, you can initialize DPF using a specific ``DataProcessingCore.xml`` file.

``Plugin.xml`` file
-------------------
The ``Plugin.xml`` file allows you to configure a specific environment for loading a
plugin.

Here is the content of this XML file:

.. code-block:: html

		<?xml version="1.0"?> 
		<DPF version="1.0"> 
			<Environment> 
				<Linux> 
					<LD_LIBRARY_PATH>$(ANSYS_ROOT_FOLDER)/aisol/dll/linx64:$(ANSYS_ROOT_FOLDER)/aisol/lib/linx64:$(ANSYS_ROOT_FOLDER)/tp/IntelMKL/2020.0.166/linx64/lib/intel64:$(LD_LIBRARY_PATH)</LD_LIBRARY_PATH> 
				</Linux> 
				<Windows> 
					<MY_FOLDER>c:\temp</MY_FOLDER> 
					<PATH>$(ANSYS_ROOT_FOLDER)\aisol\bin\winx64;$(ANSYS_ROOT_FOLDER)\tp\IntelMKL\2020.0.166\winx64;$(ANSYS_ROOT_FOLDER)\tp\IntelCompiler\2019.5.281\winx64;$(MY_FOLDER);$(PATH)</PATH> 
				</Windows> 
			</Environment> 
		</DPF> 


The ``<Environment>`` element within this XML file is defined the same way
as the ``DataProcessingCore.xml`` file.

Any environment variables that are defined or used have the values at the time
that they are defined or used. You can effectively define a variable multiple times
and keep appending it.
