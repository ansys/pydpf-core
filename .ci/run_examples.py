import glob
import os
import pathlib

from ansys.dpf import core

core.settings.disable_off_screen_rendering()

actual_path = pathlib.Path(__file__).parent.absolute()
print(os.path.join(actual_path, os.path.pardir, "examples"))
for root, subdirectories, files in os.walk(os.path.join(actual_path, os.path.pardir, "examples")):
    for subdirectory in subdirectories:
        subdir = os.path.join(root, subdirectory)
        for file in glob.iglob(os.path.join(subdir, "*.py")):
            print("\n\n--------------------------------------------------\n")
            print(file)
            print("--------------------------------------------------\n")
            exec(open(file, mode="r", encoding="utf8").read(), globals(), globals())
