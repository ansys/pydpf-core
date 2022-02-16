"""
.. _solution_combination:

Loadcase combination for principal stress and show max/min label.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This example shows how to get a principal stress loadcase combination using DPF
And highlight min/max values in the plot.

"""

###############################################################################
# First, import the DPF-Core module as ``dpf_core`` and import the
# included examples file and ``DpfPlotter``
from ansys.dpf.core.plotter import DpfPlotter

plot = DpfPlotter()
plot.show_figure(show_axes=True)
