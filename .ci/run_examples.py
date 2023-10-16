import os
import glob
import pathlib
import subprocess
import sys

import ansys.dpf.core as dpf
from ansys.dpf.core.examples import get_example_required_minimum_dpf_version


os.environ["PYVISTA_OFF_SCREEN"] = "true"
os.environ["MPLBACKEND"] = "Agg"

actual_path = pathlib.Path(__file__).parent.absolute()
print(os.path.join(actual_path, os.path.pardir, "examples"))

# Get the DPF server version
server = dpf.server.get_or_create_server(None)
server_version = server.version
server.shutdown()
print(f"Server version: {server_version}")

for root, subdirectories, files in os.walk(os.path.join(actual_path, os.path.pardir, "examples")):
    for subdirectory in subdirectories:
        subdir = os.path.join(root, subdirectory)
        for file in glob.iglob(os.path.join(subdir, "*.py")):
            if sys.platform == "linux" and "08-python-operators" in file:
                continue
            if "02-python_operators_with_dependencies" not in file:
                continue
            print("\n--------------------------------------------------")
            print(file)
            minimum_version_str = get_example_required_minimum_dpf_version(file)
            if float(server_version) - float(minimum_version_str) < -0.05:
                print(f"Example skipped as it requires DPF {minimum_version_str}.")
                continue
            try:
                subprocess.check_call([sys.executable, file])
            except subprocess.CalledProcessError as e:
                sys.stderr.write(str(e.args))
                if e.returncode != 3221225477:
                    raise e
            print("PASS")
