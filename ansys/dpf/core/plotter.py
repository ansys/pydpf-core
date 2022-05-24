"""
Plotter
=======
This module contains the DPF plotter class.

Contains classes used to plot a mesh and a fields container using PyVista.
"""

import tempfile
import os
import sys
import numpy as np
import inspect
import warnings

from ansys import dpf
from ansys.dpf import core
from ansys.dpf.core.common import locations, DefinitionLabels
from ansys.dpf.core.common import shell_layers as eshell_layers
from ansys.dpf.core import errors as dpf_errors
from ansys.dpf.core.check_version import meets_version


class _InternalPlotter:
    """The _InternalPlotter class is based on PyVista."""
    def __init__(self, **kwargs):
        try:
            import pyvista as pv
        except ModuleNotFoundError:
            raise ModuleNotFoundError(
                "To use plotting capabilities, please install pyvista "
                "with :\n pip install pyvista>=0.24.0"
            )
        mesh = kwargs.pop("mesh", None)
        self._plotter = pv.Plotter(**kwargs)
        if mesh is not None:
            self._plotter.add_mesh(mesh.grid)

    def _sort_supported_kwargs(self, bound_method, **kwargs):
        supported_args = inspect.getargspec(bound_method).args
        kwargs_in = {}
        kwargs_not_avail = {}
        for key, item in kwargs.items():
            if key in supported_args:
                kwargs_in[key] = item
            else:
                kwargs_not_avail[key] = item

        if len(kwargs_not_avail) > 0:
            txt = "The following arguments are not supported: "
            txt += str(kwargs_not_avail)
            warnings.warn(txt)

        return kwargs_in

    def add_mesh(self, meshed_region, **kwargs):
        try:
            import pyvista as pv
        except ModuleNotFoundError:
            raise ModuleNotFoundError(
                "To use plotting capabilities, please install pyvista "
                "with :\n pip install pyvista>=0.24.0"
            )
        pv_version = pv.__version__
        version_to_reach = '0.30.0' # when stitle started to be deprecated
        meet_ver = meets_version(pv_version, version_to_reach)
        if meet_ver:
            # use scalar_bar_args
            scalar_bar_args = {'title': 'Mesh'}
            kwargs.setdefault("scalar_bar_args", scalar_bar_args)
        else:
            # use stitle
            has_attribute_scalar_bar = False
            try:
                has_attribute_scalar_bar = hasattr(self._plotter, 'scalar_bar')
            except:
                has_attribute_scalar_bar = False

            if not has_attribute_scalar_bar:
                kwargs.setdefault("stitle", "Mesh")
            else:
                if self._plotter.scalar_bar.GetTitle() is None:
                    kwargs.setdefault("stitle", "Mesh")
        kwargs.setdefault("show_edges", True)
        kwargs.setdefault("nan_color", "grey")

        kwargs_in = self._sort_supported_kwargs(
            bound_method=self._plotter.add_mesh,
            **kwargs
            )
        self._plotter.add_mesh(meshed_region.grid, **kwargs_in)

    def add_point_labels(self, nodes, meshed_region, labels=None, **kwargs):
        label_actors = []
        node_indexes = [meshed_region.nodes.mapping_id_to_index.get(node.id) for node in nodes]
        grid_points = [meshed_region.grid.points[node_index] for node_index in node_indexes]

        def get_label_at_grid_point(index):
            try:
                label = labels[index]
            except:
                label = None
            return label

        for index, grid_point in enumerate(grid_points):
            label_at_grid_point = get_label_at_grid_point(index)
            if label_at_grid_point:
                label_actors.append(self._plotter.add_point_labels(grid_point,
                                                                   [labels[index]],
                                                                   **kwargs))
            else:
                scalar_at_index = meshed_region.grid.active_scalars[index]
                scalar_at_grid_point = f"{scalar_at_index:.2f}"
                label_actors.append(self._plotter.add_point_labels(grid_point,
                                                                   [scalar_at_grid_point],
                                                                   **kwargs))
        return label_actors

    def add_field(self, field, meshed_region=None, show_max=False, show_min=False,
                  label_text_size=30, label_point_size=20, **kwargs):
        name = field.name.split("_")[0]
        try:
            import pyvista as pv
        except ModuleNotFoundError:
            raise ModuleNotFoundError(
                "To use plotting capabilities, please install pyvista "
                "with :\n pip install pyvista>=0.24.0"
            )
        pv_version = pv.__version__
        version_to_reach = '0.30.0'
        meet_ver = meets_version(pv_version, version_to_reach)
        if meet_ver:
            # use scalar_bar_args
            scalar_bar_args = {'title': name}
            kwargs.setdefault("scalar_bar_args", scalar_bar_args)
        else:
            # use stitle
            kwargs.setdefault("stitle", name)
        kwargs.setdefault("show_edges", True)
        kwargs.setdefault("nan_color", "grey")

        # get the meshed region location
        if meshed_region is None:
            meshed_region = field.meshed_region
        location = field.location
        if location == locations.nodal:
            mesh_location = meshed_region.nodes
        elif location == locations.elemental:
            mesh_location = meshed_region.elements
            if show_max or show_min:
                warnings.warn("`show_max` and `show_min` is only supported for Nodal results.")
                show_max = False
                show_min = False
        else:
            raise ValueError(
                "Only elemental or nodal location are supported for plotting."
            )
        component_count = field.component_count
        if component_count > 1:
            overall_data = np.full((len(mesh_location), component_count), np.nan)
        else:
            overall_data = np.full(len(mesh_location), np.nan)
        ind, mask = mesh_location.map_scoping(field.scoping)
        overall_data[ind] = field.data[mask]

        # plot
        kwargs_in = self._sort_supported_kwargs(
            bound_method=self._plotter.add_mesh,
            **kwargs
            )
        self._plotter.add_mesh(meshed_region.grid, scalars=overall_data, **kwargs_in)

        if show_max or show_min:
            # Get Min-Max for the field
            min_max = core.operators.min_max.min_max()
            min_max.inputs.connect(field)

        # Add Min and Max Labels
        labels = []
        grid_points = []
        if show_max:
            max_field = min_max.outputs.field_max()
            # Get Node ID at max.
            node_id_at_max = max_field.scoping.id(0)
            labels.append(f"Max: {max_field.data[0]:.2f}\nNodeID: {node_id_at_max}")
            # Get Node index at max value.
            node_index_at_max = meshed_region.nodes.scoping.index(node_id_at_max)
            # Append the corresponding Grid Point.
            grid_points.append(meshed_region.grid.points[node_index_at_max])

        if show_min:
            min_field = min_max.outputs.field_min()
            # Get Node ID at min.
            node_id_at_min = min_field.scoping.id(0)
            labels.append(f"Min: {min_field.data[0]:.2f}\nNodeID: {node_id_at_min}")
            # Get Node index at min. value.
            node_index_at_min = meshed_region.nodes.scoping.index(node_id_at_min)
            # Append the corresponding Grid Point.
            grid_points.append(meshed_region.grid.points[node_index_at_min])

        # Plot labels:
        for index, grid_point in enumerate(grid_points):
            self._plotter.add_point_labels(grid_point, [labels[index]],
                                           font_size=label_text_size, point_size=label_point_size)

    def show_figure(self, **kwargs):
        background = kwargs.pop("background", None)
        if background is not None:
            self._plotter.set_background(background)

        # show result
        show_axes = kwargs.pop("show_axes", None)
        if show_axes:
            self._plotter.add_axes()

        kwargs_in = self._sort_supported_kwargs(
            bound_method=self._plotter.show,
            **kwargs
            )
        return self._plotter.show(**kwargs_in)


class DpfPlotter:
    """DpfPlotter class. Can be used in order to plot
    results over a mesh.

    The current DpfPlotter is a PyVista based object.

    That means that PyVista must be installed, and that
    it supports **kwargs as parameter (the argument
    must be supported by the installed PyVista version).
    More information about the available arguments are
    available at :func:`pyvista.plot` .
    """
    def __init__(self, **kwargs):
        """Create a DpfPlotter object.

        The current DpfPlotter is a PyVista based object.

        That means that PyVista must be installed, and that
        it supports **kwargs as parameter (the argument
        must be supported by the installed PyVista version).
        More information about the available arguments are
        available at :func:`pyvista.plot` .

        Parameters
        ----------
        **kwargs : optional
            Additional keyword arguments for the plotter. More information
            are available at :func:`pyvista.plot` .

        Examples
        --------
        >>> from ansys.dpf.core.plotter import DpfPlotter
        >>> pl = DpfPlotter(notebook=False)

        """
        self._internal_plotter = _InternalPlotter(**kwargs)
        self._labels = []

    @property
    def labels(self):
        """Return a list of labels.

        Returns
        --------
        list
            List of Label(s). Each list member or member group
            will share same properties.
        """
        return self._labels

    def add_node_labels(self, nodes, meshed_region, labels=None, **kwargs):
        """Add labels at the nodal locations.

        Parameters
        ----------
        nodes : list
            Nodes where the labels should be added.
        meshed_region: MeshedRegion
            MeshedRegion to plot.
        labels: : list of str or str, optional
            If label for grid point is not defined, scalar value at that point is shown.
        kwargs: dict, optional
                Keyword arguments controlling label properties.
                See :func:`pyvista.Plotter.add_point_labels`.
        """
        self._labels.append(self._internal_plotter.add_point_labels(nodes=nodes,
                                                                    meshed_region=meshed_region,
                                                                    labels=labels,
                                                                    **kwargs))

    def add_mesh(self, meshed_region, **kwargs):
        """Add a mesh to plot.

        Parameters
        ----------
        meshed_region : MeshedRegion
            MeshedRegion to plot.
        **kwargs : optional
            Additional keyword arguments for the plotter. More information
            are available at :func:`pyvista.plot`.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.multishells_rst)
        >>> mesh = model.metadata.meshed_region
        >>> from ansys.dpf.core.plotter import DpfPlotter
        >>> pl = DpfPlotter()
        >>> pl.add_mesh(mesh)

        """
        self._internal_plotter.add_mesh(meshed_region=meshed_region, **kwargs)

    def add_field(self, field, meshed_region=None, show_max=False, show_min=False,
                  label_text_size=30, label_point_size=20, **kwargs):
        """Add a field containing data to the plotter.

        A meshed_region to plot on can be added.
        If no ``meshed_region`` is specified, the field
        support will be used. Ensure that the field
        support is a ``meshed_region``.

        Parameters
        ----------
        field : Field
            Field data to plot
        meshed_region : MeshedRegion, optional
            ``MeshedRegion`` to plot the field on.
        show_max : bool, optional
            Label the point with the maximum value.
        show_min : bool, optional
            Label the point with the minimum value.
        **kwargs : optional
            Additional keyword arguments for the plotter. More information
            are available at :func:`pyvista.plot`.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.multishells_rst)
        >>> mesh = model.metadata.meshed_region
        >>> field = model.results.displacement().outputs.fields_container()[0]
        >>> from ansys.dpf.core.plotter import DpfPlotter
        >>> pl = DpfPlotter()
        >>> pl.add_field(field, mesh)

        """
        self._internal_plotter.add_field(field=field,
                                         meshed_region=meshed_region,
                                         show_max=show_max,
                                         show_min=show_min,
                                         label_text_size=label_text_size,
                                         label_point_size=label_point_size,
                                         **kwargs)

    def show_figure(self, **kwargs):
        """Plot the figure built by the plotter object.

        Parameters
        ----------
        **kwargs : optional
            Additional keyword arguments for the plotter. More information
            are available at :func:`pyvista.plot`.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.multishells_rst)
        >>> mesh = model.metadata.meshed_region
        >>> field = model.results.displacement().outputs.fields_container()[0]
        >>> from ansys.dpf.core.plotter import DpfPlotter
        >>> pl = DpfPlotter()
        >>> pl.add_field(field, mesh)
        >>> pl.show_figure()

        """
        return self._internal_plotter.show_figure(**kwargs)


def plot_chart(fields_container):
    """Plot the minimum/maximum result values over time.

    This is a valid method if ``time_freq_support`` contains
    several time_steps, such as in a transient analysis.

    Parameters
    ----------
    field_container : dpf.core.FieldsContainer
        Fields container that must contains a result for each
        time step of ``time_freq_support``.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> from ansys.dpf.core import examples
    >>> model = dpf.Model(examples.transient_therm)
    >>> t = model.results.temperature.on_all_time_freqs()
    >>> fc = t.outputs.fields_container()
    >>> plotter = dpf.plotter.plot_chart(fc)

    """
    p = Plotter(None)
    return p.plot_chart(fields_container)


class Plotter:
    """Plots fields and meshed regions in DPF-Core.

    Parameters
    ----------
    mesh : str
        Name of the mesh.

    """

    def __init__(self, mesh, **kwargs):
        self._internal_plotter = _InternalPlotter(mesh=mesh, **kwargs)
        self._mesh = mesh

    def plot_mesh(self, **kwargs):
        """Plot the mesh using PyVista.

        Parameters
        ----------
        notebook : bool, optional
            When ``None`` (default) plot a static image within an
            iPython notebook if available.  When ``False``, plot
            external to the notebook with an interactive window.  When
            ``True``, always plot within a notebook.
        **kwargs : optional
            Additional keyword arguments for the plotter. For more information,
            ee ``help(pyvista.plot)``.

        """
        kwargs.setdefault("color", "w")
        kwargs.setdefault("show_edges", True)
        return self._mesh.grid.plot(**kwargs)

    def plot_chart(self, fields_container):
        """Plot the minimum/maximum result values over time.

        This is a valid method if ``time_freq_support`` contains
        several time steps, such as in a transient analysis.

        Parameters
        ----------
        fields_container : dpf.core.FieldsContainer
            Fields container that must contain a result for each
            time step of ``time_freq_support``.

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> from ansys.dpf.core import examples
        >>> model = dpf.Model(examples.simple_bar)
        >>> disp = model.results.displacement()
        >>> scoping = dpf.Scoping()
        >>> scoping.ids = range(1, len(model.metadata.time_freq_support.time_frequencies) + 1)
        >>> disp.inputs.time_scoping.connect(scoping)
        >>> fc = disp.outputs.fields_container()
        >>> plotter = dpf.plotter.Plotter(model.metadata.meshed_region)
        >>> pl = plotter.plot_chart(fc)

        """
        try:
            import matplotlib.pyplot as pyplot
        except ModuleNotFoundError:
            raise ModuleNotFoundError(
                "To use plot_chart capabilities, please install "
                "matplotlib with :\n pip install matplotlib>=3.2"
            )
        tfq = fields_container.time_freq_support
        if len(fields_container) != len(tfq.time_frequencies):
            raise Exception(
                "Fields container must contain real fields at all time "
                "steps of the time_freq_support."
            )
        time_field = tfq.time_frequencies
        normOp = dpf.core.Operator("norm_fc")
        minmaxOp = dpf.core.Operator("min_max_fc")
        normOp.inputs.fields_container.connect(fields_container)
        minmaxOp.inputs.connect(normOp.outputs)
        fieldMin = minmaxOp.outputs.field_min()
        fieldMax = minmaxOp.outputs.field_max()
        pyplot.plot(time_field.data, fieldMax.data, "r", label="Maximum")
        pyplot.plot(time_field.data, fieldMin.data, "b", label="Minimum")
        unit = tfq.time_frequencies.unit
        if unit == "Hz":
            pyplot.xlabel("frequencies (Hz)")
        elif unit == "s":
            pyplot.xlabel("time (s)")
        elif unit is not None:
            pyplot.xlabel(unit)
        substr = fields_container[0].name.split("_")
        pyplot.ylabel(substr[0] + fieldMin.unit)
        pyplot.title(substr[0] + ": min/max values over time")
        return pyplot.legend()

    def plot_contour(
            self,
            field_or_fields_container,
            notebook=None,
            shell_layers=None,
            off_screen=None,
            show_axes=True,
            meshed_region=None,
            **kwargs
    ):
        """Plot the contour result on its mesh support.

        You cannot plot a fields container containing results at several
        time steps.

        Parameters
        ----------
        field_or_fields_container : dpf.core.Field or dpf.core.FieldsContainer
            Field or field container that contains the result to plot.
        notebook : bool, optional
            Whether to plot a static image within an iPython notebook
            if available. The default is `None`, in which case an attempt is
            made to plot a static imaage within an iPython notebook. When ``False``,
            a plot external to the notebook is generated with an interactive window.
            When ``True``, a plot is always generated within a notebook.
        shell_layers : core.shell_layers, optional
            Enum used to set the shell layers if the model to plot
            contains shell elements.
        off_screen : bool, optional
            Whether to render off screen, which is useful for automated
            screenshots. The default is ``None``.
        show_axes : bool, optional
            Whether to show a VTK axes widget. The default is ``True``.
        **kwargs : optional
            Additional keyword arguments for the plotter. For more information,
            see ``help(pyvista.plot)``.
        """
        if not sys.warnoptions:
            import warnings

            warnings.simplefilter("ignore")

        if isinstance(
                field_or_fields_container, (dpf.core.Field, dpf.core.FieldsContainer)
        ):
            fields_container = None
            if isinstance(field_or_fields_container, dpf.core.Field):
                fields_container = dpf.core.FieldsContainer(
                    server=field_or_fields_container._server
                )
                fields_container.add_label(DefinitionLabels.time)
                fields_container.add_field(
                    {DefinitionLabels.time: 1}, field_or_fields_container
                )
            elif isinstance(field_or_fields_container, dpf.core.FieldsContainer):
                fields_container = field_or_fields_container
        else:
            raise TypeError("Only field or fields_container can be plotted.")

        # pre-loop to check if the there are several time steps
        labels = fields_container.get_label_space(0)
        if DefinitionLabels.complex in labels.keys():
            raise dpf_errors.ComplexPlottingError
        if DefinitionLabels.time in labels.keys():
            first_time = labels[DefinitionLabels.time]
            for i in range(1, len(fields_container)):
                label = fields_container.get_label_space(i)
                if label[DefinitionLabels.time] != first_time:
                    raise dpf_errors.FieldContainerPlottingError

        if meshed_region is not None:
            mesh = meshed_region
        else:
            mesh = self._mesh

        # get mesh scoping
        location = None
        component_count = None
        name = None

        # pre-loop to get location and component count
        for field in fields_container:
            if len(field.data) != 0:
                location = field.location
                component_count = field.component_count
                name = field.name.split("_")[0]
                break

        if location == locations.nodal:
            mesh_location = mesh.nodes
        elif location == locations.elemental:
            mesh_location = mesh.elements
        else:
            raise ValueError(
                "Only elemental or nodal location are supported for plotting."
            )

        # pre-loop: check if shell layers for each field, if yes, set the shell layers
        changeOp = core.Operator("change_shellLayers")
        for field in fields_container:
            shell_layer_check = field.shell_layers
            if shell_layer_check in [
                eshell_layers.topbottom,
                eshell_layers.topbottommid,
            ]:
                changeOp.inputs.fields_container.connect(fields_container)
                sl = eshell_layers.top
                if shell_layers is not None:
                    if not isinstance(shell_layers, eshell_layers):
                        raise TypeError(
                            "shell_layer attribute must be a core.shell_layers instance."
                        )
                    sl = shell_layers
                changeOp.inputs.e_shell_layer.connect(sl.value)  # top layers taken
                fields_container = changeOp.get_output(0, core.types.fields_container)
                break

        # Merge field data into a single array
        if component_count > 1:
            overall_data = np.full((len(mesh_location), component_count), np.nan)
        else:
            overall_data = np.full(len(mesh_location), np.nan)

        for field in fields_container:
            ind, mask = mesh_location.map_scoping(field.scoping)
            overall_data[ind] = field.data[mask]

        # create the plotter and add the meshes
        background = kwargs.pop("background", None)
        cpos = kwargs.pop("cpos", None)
        return_cpos = kwargs.pop("return_cpos", None)

        # plotter = pv.Plotter(notebook=notebook, off_screen=off_screen)
        if notebook is not None:
            self._internal_plotter._plotter.notebook = notebook
        if off_screen is not None:
            self._internal_plotter._plotter.off_screen = off_screen

        # add meshes
        kwargs.setdefault("show_edges", True)
        kwargs.setdefault("nan_color", "grey")
        kwargs.setdefault("stitle", name)
        text = kwargs.pop('text', None)
        if text is not None:
            self._internal_plotter._plotter.add_text(text, position='lower_edge')
        self._internal_plotter._plotter.add_mesh(mesh.grid, scalars=overall_data, **kwargs)

        if background is not None:
            self._internal_plotter._plotter.set_background(background)

        if cpos is not None:
            self._internal_plotter._plotter.camera_position = cpos

        # show result
        if show_axes:
            self._internal_plotter._plotter.add_axes()
        if return_cpos is None:
            return self._internal_plotter._plotter.show()
        else:
            import pyvista as pv
            pv_version = pv.__version__
            version_to_reach = '0.32.0'
            meet_ver = meets_version(pv_version, version_to_reach)
            if meet_ver:
                return self._internal_plotter._plotter.show(return_cpos=return_cpos)
            else:
                txt = """To use the return_cpos option, please upgrade
                your pyvista module with a version higher than """
                txt += version_to_reach
                raise core.errors.DpfVersionNotSupported(version_to_reach, txt)

    def _plot_contour_using_vtk_file(self, fields_container, notebook=None):
        """Plot the contour result on its mesh support.

        The resulting figure depends on the support, which can be a meshed region
        or a time freq support. If a transient analysis, the last result is plotted.

        This method is private.  DPF publishes a VTK file and displays
        this file using PyVista.
        """
        try:
            import pyvista as pv
        except ModuleNotFoundError:
            raise ModuleNotFoundError(
                "To use plotting capabilities, please install pyvista "
                "with :\n pip install pyvista>=0.24.0"
            )

        plotter = pv.Plotter(notebook=notebook)
        # mesh_provider = Operator("MeshProvider")
        # mesh_provider.inputs.data_sources.connect(self._evaluator._model.metadata.data_sources)

        # create a temporary file at the default temp directory
        path = os.path.join(tempfile.gettempdir(), "dpf_temp_hokflb2j9s.vtk")

        vtk_export = dpf.core.Operator("vtk_export")
        vtk_export.inputs.mesh.connect(self._mesh)
        vtk_export.inputs.fields1.connect(fields_container)
        vtk_export.inputs.file_path.connect(path)
        vtk_export.run()
        grid = pv.read(path)

        if os.path.exists(path):
            os.remove(path)

        names = grid.array_names
        field_name = fields_container[0].name
        for n in names:  # get new name (for example if time_steps)
            if field_name in n:
                field_name = n  # default: will plot the last time_step
        val = grid.get_array(field_name)
        plotter.add_mesh(grid, scalars=val, stitle=field_name, show_edges=True)
        plotter.add_axes()
        plotter.show()
