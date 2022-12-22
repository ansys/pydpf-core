"""
.. _plot_on_points:

Plot on geometry elements
~~~~~~~~~~~~~~~~~~~~~~~~~
This example shows how to plot a Field on a Points object.

.. note::
    This example requires the Premium ServerContext.
    For more information, see :ref:`user_guide_server_context`.

"""


###############################################################################
# Imports and load model
# ~~~~~~~~~~~~~~~~~~~~~~
# Import modules and set context as Premium.
from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core import operators as ops
from ansys.dpf.core.geometry import Points
from ansys.dpf.core.plotter import DpfPlotter
from ansys.dpf.core.fields_factory import field_from_array

dpf.set_default_server_context(dpf.AvailableServerContexts.premium)

###############################################################################
# Load model from examples and print information
model = dpf.Model(examples.find_static_rst())
print(model)

###############################################################################
# Create Points object
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Create 8 points in the corners and one in the middle
points = Points(
    [
        [0.0, 0.03, 0.0],
        [0.0, 0.03, 0.03],
        [0.0, 0.06, 0.00],
        [0.0, 0.06, 0.03],
        [0.03, 0.03, 0.0],
        [0.03, 0.03, 0.03],
        [0.03, 0.06, 0.00],
        [0.03, 0.06, 0.03],
        [0.015, 0.045, 0.015],
    ]
)

###############################################################################
# Get mesh from model
mesh = model.metadata.meshed_region

###############################################################################
# Set camera position (obtained with ``cpos=pl.show_figure(return_cpos=True)``)
cpos = [
    (0.07635352356975698, 0.1200500294271993, 0.041072502929096165),
    (0.015, 0.045, 0.015),
    (-0.16771051558419411, -0.1983722658245161, 0.9656715938216944),
]
###############################################################################
# Show points together with the mesh
points.plot(mesh, cpos=cpos)

###############################################################################
# Map displacement field to Points
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Use :class:`on_coordinates <ansys.dpf.core.operators.mapping.on_coordinates.
# on_coordinates>`: mapping opretor
disp = model.results.displacement
mapping_operator = ops.mapping.on_coordinates(
    fields_container=disp,
    coordinates=field_from_array(points.coordinates.data),
    create_support=True,
    mesh=mesh,
)
fields_mapped = mapping_operator.outputs.fields_container()
field_points = fields_mapped[0]

###############################################################################
# Plotting displacement field on the geometry objects
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3D plot of Points and display mesh
pl = DpfPlotter()
pl.add_field(field_points, render_points_as_spheres=True, point_size=10)
pl.add_mesh(mesh, style="surface", show_edges=True, color="w", opacity=0.3)
pl.show_figure(show_axes=True, cpos=cpos)
