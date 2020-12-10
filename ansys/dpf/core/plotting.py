from ansys import dpf
from ansys.dpf.core.misc import module_exists


if module_exists("pyvista"):
    import pyvista as pv
    import numpy as np
    import scooby
    # python is being run from within a jupyter notebook
    IN_NOTEBOOK = scooby.in_ipykernel() and module_exists('itkwidgets')


def check_pyvista_warning():
    if not module_exists("pyvista"):
        raise ImportError("Plotting tools are only available if pyvista module is installed")


def plot_nodal(field, comp=None, **kwargs):
    """Plots the field values as nodal values

    Parameters
    ----------
    comp : str, int (optional)
        Component name or index.  Required when the number of
        components is greater than 1.

    **kwargs : keyword arguments
        See help(pyvista.plot) for additional keyword arguments
        for controlling the plot type.

    Returns
    -------
    cpos : list
       Camera position of the vtk plotter when it was closed.
    """
    check_pyvista_warning()
    grid = field._model.meshed_region.grid  # this only handles the entire grid

    if field.ndim > 1 and comp is None:
        raise ValueError(f'There are {field.ndim} components.  ' +
                         f'Please specify a component from:\n{field.components}')
    elif comp is not None:
        field = field[comp]
    else:
        field = field

    # convert from elemental_nodal if necessary
    if field.location in [dpf.core.Location.elemental_nodal, dpf.core.Location.elemental]:
        field = field.to_nodal()

    # remap scalars to grid indexing
    field_ids = np.array(field.scoping.ids)
    grid_ids = grid.point_arrays['node_ids']

    # map the indices to the grid to be plotted
    map_ind = np.empty(np.max(grid_ids) + 1, np.int32)
    map_ind[grid_ids] = np.arange(grid_ids.size)
    ind = map_ind[field_ids]

    # generate scalars
    scalars = np.empty(grid.n_points)
    scalars[:] = 0  # consider np.nan
    scalars[ind] = field.asarray()

    # consider allowing user to over-ride plotting in a notebook
    # notebook = kwargs.pop('notebook', True)
    if IN_NOTEBOOK:
        pl = pv.PlotterITK()
        pl.add_mesh(grid, scalars=scalars, **kwargs)
    else:
        pl = pv.Plotter()
        pl.add_mesh(grid, scalars=scalars, stitle=field.name, **kwargs)

    return pl.show()


def plot_elemental(field, comp=None, **kwargs):
    """Plots the active field overlaid on the active grid.

    Parameters
    ----------
    comp : str, int (optional)
        Component name or index.  Required when the number of
        components is greater than 1.

    **kwargs : keyword arguments
        See help(pyvista.plot) for additional keyword arguments
        for controlling the plot type.

    Returns
    -------
    cpos : list
       Camera position of the vtk plotter when it was closed.
    """
    check_pyvista_warning()
    if field.type != dpf.core.Location.elemental:
        raise RuntimeError('Field type must be elemental')

    grid = field._model.meshed_region.grid  # this only handles the entire grid

    if field.ndim > 1 and comp is None:
        raise ValueError(f'There are {field.ndim} components.  ' +
                         'Please specify a component')
    elif comp is not None:
        field = field[comp]
    else:
        field = field

    field_ids = np.array(field.scoping.ids)
    grid_ids = grid.cell_arrays['element_ids']

    # map the indices to the grid to be plotted
    map_ind = np.empty(np.max(grid_ids) + 1, np.int32)
    map_ind[grid_ids] = np.arange(grid_ids.size)
    ind = map_ind[field_ids]

    # generate scalars
    scalars = np.empty(grid.n_cells)
    scalars[:] = 0  # consider np.nan
    scalars[ind] = field.asarray()

    return grid.plot(scalars=scalars, stitle=field.name, **kwargs)


def plot_lines(self, linestyle='-', legend=True, show=True):
    """Plot lines...TOOD: add documentation

    Returns
    -------
    figure : matplotlib.pyplot.Figure
        Figure of plotted field
    """
    import matplotlib.pyplot as plt

    # get scoping ids
    x = self.scoping.ids

    # generate figure
    fig = plt.figure(num=None, figsize=(8, 6), dpi=80,
                     facecolor='w', edgecolor='k')

    if self._component_info:
        plt.title('%s %s' % (self._component_info, self._readable_name))
    else:
        plt.title(self._readable_name)

    for comp in self.components:
        y = self[comp].data[:len(x)]  # BUG: x.size is temp, waiting on fix
        plt.plot(x, y, label=comp, linestyle=linestyle)

    # add legend if displaying multiple components
    if legend and self.component_count > 1:
        plt.legend()

    # TODO: Better label
    plt.xlabel('Result Set')

    # add y-axis label
    if self.unit:
        ylabel = f'{self._readable_name} ({self.unit})'
    else:
        ylabel = self._readable_name
    plt.ylabel(ylabel)

    if show:
        fig.show()
    return fig
