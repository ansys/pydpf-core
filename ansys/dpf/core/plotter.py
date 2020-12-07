"""Dpf plotter class is contained in this module. 
Allows to plot a mesh and a fields container 
using pyvista."""

import pyvista as pv
import matplotlib.pyplot as pyplot
import os
import sys
from ansys import dpf
from ansys.dpf.core.rescoper import Rescoper as _Rescoper
from ansys.dpf.core.common import locations

class Plotter:
    def __init__(self, mesh):
        self._mesh = mesh
        
    def plot_mesh(self, notebook=True):
        """Plot the mesh using pyvista.
        
        Parameters
        ----------
        notebook (default: True):
            bool, that mention if the plotting must be 3D (notebook=False) or not (notebook=True)
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
        """
        tfq = fields_container.time_freq_support
        time_field = tfq.frequencies
        normOp = dpf.core.Operator("norm_fc")
        minmaxOp = dpf.core.Operator("min_max_fc")
        normOp.inputs.fields_container.connect(fields_container)
        minmaxOp.inputs.connect(normOp.outputs)
        fieldMin = minmaxOp.outputs.field_min()
        fieldMax = minmaxOp.outputs.field_max()
        pyplot.plot(time_field.data,fieldMax.data,'r',label='Maximum')
        pyplot.plot(time_field.data,fieldMin.data,'b',label='Minimum')
        pyplot.xlabel("time (s)")
        substr = fields_container[0].name.split("_")
        pyplot.ylabel(substr[0] + fieldMin.unit)
        pyplot.title( substr[0] + ": min/max values over time")
        return pyplot.legend()
    
    def plot_contour(self, fields_container, notebook=True):
        """Plot the contour result on its mesh support. The obtained figure depends on the 
        support (can be a meshed_region or a time_freq_support).
        If transient analysis, plot the last result if no time_scoping has been specified.
        
        Parameters
        ----------
        fields_container
            dpf.core.FieldsContainer thats contains the result to plot.
        notebook (default: True):
            bool, that mention if the plotting must be 3D (notebook=False) or not (notebook=True)
        """
        if not sys.warnoptions:
            import warnings
            warnings.simplefilter("ignore")
        plotter = pv.Plotter(notebook=notebook)
        mesh = self._mesh
        grid = mesh.grid
        nan_color = "grey"
        
        rescoperOp = dpf.core.Operator("Rescope")
        mesh_scoping = None
        if (fields_container[0].location == locations.nodal):
            mesh_scoping = mesh.nodes.scoping
        elif(fields_container[0].location == locations.elemental):
            mesh_scoping = mesh.elements.scoping
        else:
            raise Exception("Only elemental or nodal location are supported for plotting.")
        rescoperOp.inputs.mesh_scoping.connect(mesh_scoping)
        rescoperOp.connect(2,float("nan"))
        
        #rescoper = _Rescoper(mesh, fields_container[0].location, 
        #                     fields_container[0].component_count) #location will be the same on all fields
        if (len(fields_container) == 1):
            #field = rescoper.rescope(fields_container[0])
            rescoperOp.inputs.fields_container.connect(fields_container)
            fields2 = rescoperOp.outputs.fields_container()
            dataR = fields2[0].data
            plotter.add_mesh(grid, scalars = dataR, opacity=1.0, nan_color=nan_color, 
                              stitle = fields_container[0].name, show_edges=True)
        else:
            for field_to_rescope in fields_container:
                forward = dpf.core.Operator("forward_fc")
                forward.inputs.fields.connect(field_to_rescope)
                rescoperOp.inputs.fields_container.connect(forward.outputs.fields_container)
                field = rescoperOp.outputs.fields_container()[0]
                name = field_to_rescope.name.split("_")[0]
                #field = rescoper.rescope(field_to_rescope)
                dataR = field.data
                plotter.add_mesh(grid, scalars = dataR, nan_color=nan_color, stitle = name, show_edges=True)
        plotter.add_axes()
        return plotter.show()
    
    def _plot_contour_using_vtk_file(self, fields_container, notebook=True):
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