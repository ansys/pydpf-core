import pyvista
mesh = pyvista.Sphere()
mesh.plot(screenshot="windows_latest.png", scalars=range(mesh.n_points), off_screen=True)