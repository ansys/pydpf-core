"""
.. _ref_pyvista_legends_test:

PyVista Legends Test
~~~~~~~~~~~~~~~~~~~~
"""

import pyvista as pv
mesh = pv.Sphere()
mesh.plot(screenshot="sc.png", scalars=range(mesh.n_points))