"""
.. _compare_results:

Compare Results Using the Plotter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This example shows how to plot several meshes/results combination
over the same plotter, in order to compare them. The usecase will be
to compare results at different time steps.

"""
from ansys.dpf.core.plotter import DpfPlotter

###############################################################################
# Now we create an :class:`ansys.dpf.core.plotter.DpfPlotter` and add the
# first mesh and the first result
pl = DpfPlotter()
pl.show_figure(show_axes=True)
