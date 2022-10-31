import os
import glob
import pathlib
import subprocess
import sys

os.environ["PYVISTA_OFF_SCREEN"] = "true"
os.environ["MPLBACKEND"] = "Agg"

actual_path = pathlib.Path(__file__).parent.absolute()
print(os.path.join(actual_path, os.path.pardir, "examples"))


for root, subdirectories, files in os.walk(os.path.join(actual_path, os.path.pardir, "examples")):
    for subdirectory in subdirectories:
        subdir = os.path.join(root, subdirectory)
        for file in glob.iglob(os.path.join(subdir, "*.py")):
            if sys.platform == "linux" and "07-python-operators" in file:
                continue
            print("\n--------------------------------------------------")
            print(file)
            try:
                subprocess.check_call([sys.executable, file])
            except subprocess.CalledProcessError as e:
                sys.stderr.write(str(e.args))
                if e.returncode != 3221225477:
                    raise e
            print("PASS")
