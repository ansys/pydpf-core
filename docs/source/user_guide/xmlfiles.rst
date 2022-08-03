.. _user_guide_xmlfiles:

=============
DPF XML Files
=============
This section describes the XML files associated with DataProcessingCore 
and DPF plugins. These DPF files work on both Windows and Linux 
operating systems. The files can contain content for both operating systems. 

The XML files must be located alongside the plugin DLL files on Windows, 
or SO files on Linux. 

DataProcessingCore File
-----------------------
The content and format of the DataProcessingCore.xml file is as follows:

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

The DataProcessingCore.xml file is provided with the DPF software. 
Modify the file carefully to ensure that the DPF software operates correctly. 

Some of the sections in the file are optional, and many of the sections 
have Windows and Linux specific subsections. 

The ``<Environment>`` section is used only for defining the ROOT folder 
of the Ansys software. This is done with an ``<ANSYS_ROOT_FOLDER>`` tag. 
The root folder of the Ansys software ends with the v### folder. 
It could be something like ``C:\ansys_inc\v222``. The ANSYS_ROOT_FOLDER tag 
defines a variable like an environment variable that can be used in the other 
XML files. You might use it to find required third party software. 

If the ANSYS_ROOT_FOLDER tag is not defined within the DataProcessing.xml file,
the root folder is determined by reading the AWP_ROOT### environment 
variable specific to the version of the DPF code. For example, if you are 
using V222 DPF code, it looks for AWP_ROOT222 to find the root folder. 

If the ANSYS_ROOT_FOLDER tag is still not defined, the code attempts to find the 
root folder relative to the DataProcessingCore DLL/SO file. This only works 
if DataProcessingCore is located in its default location. 

The ``<LoadOperators>`` section is used for loading the default plugins. 
The further subdividing of the plugins into ``<Debug>`` or ``<Release>`` 
sections is optional. The ``<Debug>`` section would only be used with a 
debug version of the DataProcessingCore DLL/SO file. 

The plugins to load are defined within their own section that is named 
by a tag like ``<native>`` or ``<fem_utils>``. This tag is used as 
the ``Key`` when loading the plugin. Each plugin must have a unique key. 

Within the Key section are two tags that define the location of the plugin 
and the method of loading. The location is defined by the ``<Path>`` tag 
and the loading method is defined by the ``<Loader>`` tag. 
These are used as arguments to the loading plugin mechanism. 

Currently, only ``LoadOperators`` is supported for the ``<Loader>`` tag.
This loads all operators within the plugin. 

The ``<Path>`` tag contains the location of the plugin to load. 
The normal mechanism that the OS uses to find a DLL/SO is used. 
The DLL could be in the Windows path, or the SO could be within 
the Linux LD_LIBRARY_PATH. 

The ``<UsePluginXml>`` tag contains a value that must be set to 
``true`` or ``false``. It defines if the PLUGIN.XML file 
(defined in next section) will be used to load the plugin or not. 
This tag is optional. The default value is ``true``. 

Any path specified with the XML file must adhere to the path conventions 
of the OS. “\\” for Windows and “/” for Linux. 

Two pre-defined variables can be used to provide an absolute path to 
the plugin: 

- ANSYS_ROOT_FOLDER as defined above. 
- THIS_XML_FOLDER defining the location of where the current XML file is located. In this case DataProcessingCore.xml.

Any other environment variable could be used. If you always had your plugins 
in a folder defined by the environment variable MY_PLUGINS, 
you could use that in the XML file. 

The environment variables are specified the same way as ANSYS_ROOT_FOLDER 
or THIS_XML_FOLDER. They are defined as $(…). 

In the Ansys installation, the default DataProcessingCore.xml file is located 
next to the DataProcessingCore DLL/SO file. 
If you want to use a different one, you can initialize DPF using a 
specific DataProcessingCore.xml file.

PLUGIN.XML File
---------------
The content and format of the Plugin.xml file is as follows:

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

This file allows for a specific environment to be configured for loading a plugin. 
The ``<Environment>`` section within the plugin-specific XML file is defined 
the same way as the DataProcessingCore.xml file.

Any environment variables defined or used have the values at the time they are 
defined or used. You can effectively define a variable multiple times 
and keep appending it. 
