import os
import glob
import pathlib
from ansys.dpf.core.misc import module_exists
import subprocess

if module_exists("matplotlib"):
    import matplotlib as mpl

    mpl.use("Agg")

# enable off_screen plotting to avoid test interruption

if module_exists("pyvista"):
    import pyvista as pv

    pv.OFF_SCREEN = True

actual_path = pathlib.Path(__file__).parent.absolute()
print(os.path.join(actual_path,os.path.pardir, "examples"))
for root, subdirectories, files in os.walk(os.path.join(actual_path, os.path.pardir, "examples")):
    for subdirectory in subdirectories:
        subdir = os.path.join(root, subdirectory)
        for file in glob.iglob(os.path.join(subdir, "*.py")):
            print("\n\n--------------------------------------------------\n")
            print(file)
            print("--------------------------------------------------\n")
            exec(
                open(file, mode="r", encoding="utf8").read(),
                globals(),
                globals(),
            )