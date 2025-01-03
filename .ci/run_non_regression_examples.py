import os
from ansys.dpf import core
import pathlib
import subprocess
import sys

os.environ["PYVISTA_OFF_SCREEN"] = "true"
os.environ["MPLBACKEND"] = "Agg"

actual_path = pathlib.Path(__file__).parent.absolute()
examples_path = actual_path.parent / "examples"
print(examples_path)


list_tests = [
    examples_path / "00-basic",
    examples_path / "01-transient_analyses",
    examples_path / "02-modal_analyses",
    examples_path / "03-harmonic_analyses",
    examples_path / "06-plotting" / "00-basic_plotting.py",
    examples_path / "06-plotting" / "05-plot_on_warped_mesh.py",
    examples_path / "07-distributed-post" / "00-distributed_total_disp.py",
]

if core.SERVER_CONFIGURATION != core.AvailableServerConfigs.InProcessServer:
    list_tests.append(examples_path / "08-python-operators" / "00-wrapping_numpy_capabilities.py")

for path in list_tests:
    if path.is_dir():
        for file in path.glob("*.py"):
            print("\n--------------------------------------------------")
            print(file)
            try:
                subprocess.check_call([sys.executable, str(file)])
            except subprocess.CalledProcessError as e:
                sys.stderr.write(str(e.args))
                if e.returncode != 3221225477:
                    raise e
            print("PASS")
    else:
        print("\n--------------------------------------------------")
        print(path)
        try:
            subprocess.check_call([sys.executable, str(file)])
        except subprocess.CalledProcessError as e:
            sys.stderr.write(str(e.args))
            if e.returncode != 3221225477:
                raise e
        print("PASS")
