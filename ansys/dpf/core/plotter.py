"""Dpf plotter class is contained in this module. 
Allows to plot a mesh and a fields container 
using pyvista."""

import pyvista as pv
import matplotlib.pyplot as pyplot
import os
import sys
import numpy as np
from ansys import dpf
from ansys.dpf import core
from ansys.dpf.core.common import locations, ShellLayers, DefinitionLabels

class Plotter:
    def __init__(self, mesh):
        self._mesh = mesh
        
    def plot_mesh(self, notebook=None):
        """Plot the mesh using pyvista.
        
        Parameters
        ----------
        notebook : bool, optional
            When ``None`` (default) plot a static image within an
            iPython notebook if available.  When ``False``, plot
            external to the notebook with an interactive window.  When
            ``True``, always plot within a notebook.

        """
        return self._mesh.grid.plot(notebook=notebook)
        
    def plot_chart(self, fields_container):
        """Plot the minimum/maximum result values over time 
        if the time_freq_support contains several time_steps 
        (for example: transient analysis)
        
        Parameters
        ----------
        field_container
            dpf.core.FieldsContainer that must contains a result for each time step of the time_freq_support.
            
        Examples
        --------
        >>> from ansys.dpf import core
        >>> model = core.Model('file.rst')
        >>> stress = model.results.stress()
        >>> scoping = core.Scoping()
        >>> scoping.ids = list(range(1, len(model.metadata.time_freq_support.frequencies) + 1))
        >>> stress.inputs.time_scoping.connect(scoping)
        >>> fc = stress.outputs.fields_container()
        >>> plotter = core.plotter.Plotter(model.metadata.meshed_region)
        >>> plotter.plot_chart(fc)
        """
        tfq = fields_container.time_freq_support
        if len(fields_container) != len(tfq.frequencies):
            raise Exception("Fields container must contain real fields at all time steps of the time_freq_support.")
        time_field = tfq.frequencies
        normOp = dpf.core.Operator("norm_fc")
        minmaxOp = dpf.core.Operator("min_max_fc")
        normOp.inputs.fields_container.connect(fields_container)
        minmaxOp.inputs.connect(normOp.outputs)
        fieldMin = minmaxOp.outputs.field_min()
        fieldMax = minmaxOp.outputs.field_max()
        pyplot.plot(time_field.data,fieldMax.data,'r',label='Maximum')
        pyplot.plot(time_field.data,fieldMin.data,'b',label='Minimum')
        unit = tfq.frequencies.unit
        if unit == "Hz":
            pyplot.xlabel("frequencies (Hz)")
        elif unit == "s":
            pyplot.xlabel("time (s)")
        elif unit is not None:
            pyplot.xlabel(unit)
        substr = fields_container[0].name.split("_")
        pyplot.ylabel(substr[0] + fieldMin.unit)
        pyplot.title( substr[0] + ": min/max values over time")
        return pyplot.legend()

    def plot_contour(self, field_or_fields_container, notebook=None, shell_layers = None):
        """Plot the contour result on its mesh support.
        Can not plot fields container containing results at several time steps.

        Parameters
        ----------
        fields_container : dpf.core.FieldsContainer
            Field container that contains the result to plot.

        notebook : bool, optional
            When ``None`` (default) plot a static image within an
            iPython notebook if available.  When ``False``, plot
            external to the notebook with an interactive window.  When
            ``True``, always plot within a notebook.
        
        shell_layers : core.ShellLayers, optional
            Enum used to set the shell layers if the model to plot 
            contains shell elements.
        """
        if not sys.warnoptions:
            import warnings
            warnings.simplefilter("ignore")
            
        if isinstance(field_or_fields_container, dpf.core.Field) or isinstance(field_or_fields_container, dpf.core.FieldsContainer):
            fields_container = None
            if isinstance(field_or_fields_container, dpf.core.Field):
                fields_container = dpf.core.FieldsContainer()
                fields_container.add_label(DefinitionLabels.time)
                fields_container.add_field({DefinitionLabels.time:1}, field_or_fields_container)
            elif isinstance(field_or_fields_container, dpf.core.FieldsContainer):
                fields_container = field_or_fields_container
        else:
            raise Exception("Field or Fields Container only can be plotted.")
            
        #pre-loop to check if the there are several time steps
        labels = fields_container.get_label_space(0)
        if DefinitionLabels.complex in labels.keys():
            raise Exception("Complex field can not be plotted. Use operators to get the amplitude or the result at a defined sweeping phase before plotting.")
        if DefinitionLabels.time in labels.keys():
            i = 1
            size = len(fields_container)
            first_time = labels[DefinitionLabels.time]
            while i < size:
                label = fields_container.get_label_space(i)
                if label[DefinitionLabels.time] != first_time:
                    raise Exception("Several time steps are contained in this fields container. Only one time-step result can be plotted.")
                i += 1
        
        plotter = pv.Plotter(notebook=notebook)
        mesh = self._mesh
        grid = mesh.grid
        nan_color = "grey"
        
        #get mesh scoping
        mesh_scoping = None
        m_id_to_index = None
        location = None
        component_count = None
        name = None
        #pre-loop to get location and component count
        for field in fields_container:
            if len(field.data) != 0:
                location = field.location
                component_count = field.component_count
                name = field.name.split("_")[0]
                break
        
        if (location == locations.nodal):
            mesh_scoping = mesh.nodes.scoping
            m_id_to_index = mesh.nodes.mapping_id_to_index
        elif(location == locations.elemental):
            mesh_scoping = mesh.elements.scoping
            m_id_to_index = mesh.elements.mapping_id_to_index
        else:
            raise Exception("Only elemental or nodal location are supported for plotting.")
            
        #request all data to compute the final field to plot
        overall_data = np.empty((len(mesh_scoping), component_count))
        overall_data[:] = np.nan
        
        #pre-loop: check if shell layers for each field, if yes, set the shell layers
        changeOp = core.Operator("change_shellLayers")
        for field in fields_container:
            shell_layer_check = field.shell_layers
            if (shell_layer_check == ShellLayers.TOPBOTTOM 
                or shell_layer_check == ShellLayers.TOPBOTTOMMID):
                changeOp.inputs.fields_container.connect(fields_container)
                sl = ShellLayers.TOP
                if (shell_layers is not None):
                    if not isinstance(shell_layers, ShellLayers):
                        raise TypeError("shell_layer attribute must be a core.ShellLayers instance.")
                    sl = shell_layers
                changeOp.inputs.e_shell_layer.connect(sl.value) #top layers taken
                fields_container = changeOp.outputs.fields_container()
                break
             
        #loop: merge fields
        for field in fields_container:
            data = field.data
            scop_ids = field.scoping.ids
            size = len(scop_ids)
            i = 0
            while i < size:
                ind = m_id_to_index[scop_ids[i]]
                overall_data[ind] = data[i]
                i += 1
                    
        #add meshes
        plotter.add_mesh(grid, scalars = overall_data, stitle = name, nan_color=nan_color, show_edges=True)
            
        #show result
        plotter.add_axes()
        return plotter.show()
    
    def _plot_contour_using_vtk_file(self, fields_container, notebook=None):
        """Plot the contour result on its mesh support. The obtained figure depends on the 
        support (can be a meshed_region or a time_freq_support).
        If transient analysis, plot the last result.
        
        This method is private, publishes a vtk file and print (using pyvista) from this file."""
        plotter = pv.Plotter(notebook=notebook)
        # mesh_provider = Operator("MeshProvider")
        # mesh_provider.inputs.data_sources.connect(self._evaluator._model.metadata.data_sources)
        vtk_export = dpf.core.Operator("vtk_export")
        path = os.getcwd()
        file_name = "dpf_temporary_hokflb2j9sjd0a3.vtk"
        path += "/" + file_name
        vtk_export.inputs.mesh.connect(self._mesh)
        vtk_export.inputs.fields1.connect(fields_container)
        vtk_export.inputs.file_path.connect(path)
        vtk_export.run()
        grid = pv.read(path)
        if os.path.exists(path):
            os.remove(path)
        names = grid.array_names
        field_name = fields_container[0].name
        for n in names: #get new name (for example if time_steps)
            if field_name in n:
                field_name = n #default: will plot the last time_step 
        val = grid.get_array(field_name)
        plotter.add_mesh(grid, scalars=val, stitle = field_name, show_edges=True)
        plotter.add_axes()
        plotter.show()
