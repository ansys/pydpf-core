import numpy as np

import pyvista as pv

# sphinx_gallery_thumbnail_number = 3
from pyvista import examples

mesh = examples.load_uniform().slice()

###############################################################################
p = pv.Plotter()

# Add the mesh:
p.add_mesh(mesh, scalars="Spatial Point Data", show_edges=True)
# Add the points with scalar labels:
p.add_point_scalar_labels(mesh, "Spatial Point Data", point_size=20, font_size=36)

# Use a nice camera position:
p.camera_position = [(7, 4, 5), (4.4, 7.0, 7.2), (0.8, 0.5, 0.25)]

p.show()