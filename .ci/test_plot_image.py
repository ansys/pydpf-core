import pyvista
mesh = pyvista.Sphere()
mesh.plot(screenshot="tmp.png", scalars=range(mesh.n_points), off_screen=True)
print("Finished test.")