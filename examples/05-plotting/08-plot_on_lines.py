"""
.. _plot_on_lines:

Plot on Line object
~~~~~~~~~~~~~~~~~~~
This example shows how to plot a Field on a Line object.

.. note::
    This example requires the Premium ServerContext.
    For more information, see :ref:`user_guide_server_context`.

"""


###############################################################################
# Imports and load model
# ~~~~~~~~~~~~~~~~~~~~~~
# Import modules and set context as Premium.
import matplotlib.pyplot as plt

from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core import operators as ops
from ansys.dpf.core.geometry import Line
from ansys.dpf.core.plotter import DpfPlotter

dpf.set_default_server_context(dpf.AvailableServerContexts.premium)

###############################################################################
# Load model from examples and print information
model = dpf.Model(examples.find_static_rst())
print(model)

###############################################################################
# Create Line object
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Create line passing through the geometry's diagonal
line = Line([[0.03, 0.03, 0.05], [0.0, 0.06, 0.0]], n_points=50)

###############################################################################
# Get mesh from model
mesh = model.metadata.meshed_region

###############################################################################
# Define the camera position (obtained with ``cpos=pl.show_figure(return_cpos=True)``)
cpos = [
    (0.07635352356975698, 0.1200500294271993, 0.041072502929096165),
    (0.015, 0.045, 0.015),
    (-0.16771051558419411, -0.1983722658245161, 0.9656715938216944),
]

###############################################################################
# Plot the line with the mesh in the background
line.plot(mesh, cpos=cpos)

###############################################################################
# Map displacement field to Line
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Use :class:`on_coordinates <ansys.dpf.core.operators.mapping.on_coordinates.on_coordinates>`:
# mapping opretor to obtain the displacement Field on the line:
disp = model.results.displacement
mapping_operator = ops.mapping.on_coordinates(
    fields_container=disp,
    coordinates=line.mesh.nodes.coordinates_field,
    create_support=True,
    mesh=mesh,
)
fields_mapped = mapping_operator.outputs.fields_container()
field_line = fields_mapped[0]

###############################################################################
# 3D plot of the line and the mesh
pl = DpfPlotter()
pl.add_field(field_line, line.mesh, line_width=5)
pl.add_mesh(mesh, style="surface", show_edges=True, color="w", opacity=0.3)
pl.show_figure(show_axes=True, cpos=cpos)

###############################################################################
# 2D Plot displacement field alogn line length
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Get norm of the displacement using
# :class:`norm <ansys.dpf.core.operators.math.norm.norm>`:
norm_op = dpf.operators.math.norm()  # operator instantiation
norm_op.inputs.field.connect(field_line)
norm = norm_op.outputs.field()

###############################################################################
# Get discretized line's path
path = line.path[field_line.scoping.ids - 1]

###############################################################################
# 2D plot (graph) of Line (line length vs displacement field)
plt.plot(path, norm.data)
plt.xlabel("Line length")
plt.ylabel("Displacement norm field")
plt.show()
