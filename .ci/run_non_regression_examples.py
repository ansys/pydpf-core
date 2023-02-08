import glob
import os
import pathlib
import subprocess
import sys

from ansys.dpf import core

os.environ["PYVISTA_OFF_SCREEN"] = "true"
os.environ["MPLBACKEND"] = "Agg"

actual_path = pathlib.Path(__file__).parent.absolute()
print(os.path.join(actual_path, os.path.pardir, "examples"))


list_tests = [
    os.path.join(actual_path, os.path.pardir, "examples", "00-basic"),
    os.path.join(actual_path, os.path.pardir, "examples", "01-transient_analyses"),
    os.path.join(actual_path, os.path.pardir, "examples", "02-modal-harmonic"),
    os.path.join(actual_path, os.path.pardir, "examples", "05-plotting", "00-basic_plotting.py"),
    os.path.join(
        actual_path,
        os.path.pardir,
        "examples",
        "05-plotting",
        "05-plot_on_warped_mesh.py",
    ),
    os.path.join(
        actual_path,
        os.path.pardir,
        "examples",
        "06-distributed-post",
        "00-distributed_total_disp.py",
    ),
]

if core.SERVER_CONFIGURATION != core.AvailableServerConfigs.InProcessServer:
    list_tests.append(
        os.path.join(
            actual_path,
            os.path.pardir,
            "examples",
            "07-python-operators",
            "00-wrapping_numpy_capabilities.py",
        )
    )

for path in list_tests:
    if os.path.isdir(path):
        for file in glob.iglob(os.path.join(path, "*.py")):
            print("\n--------------------------------------------------")
            print(file)
            try:
                subprocess.check_call([sys.executable, file])
            except subprocess.CalledProcessError as e:
                sys.stderr.write(str(e.args))
                if e.returncode != 3221225477:
                    raise e
            print("PASS")
    else:
        print("\n--------------------------------------------------")
        print(path)
        try:
            subprocess.check_call([sys.executable, file])
        except subprocess.CalledProcessError as e:
            sys.stderr.write(str(e.args))
            if e.returncode != 3221225477:
                raise e
        print("PASS")
