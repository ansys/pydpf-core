import os
import glob
from pathlib import Path
import subprocess
import sys

import ansys.dpf.core as dpf
from ansys.dpf.core.examples import get_example_required_minimum_dpf_version


os.environ["PYVISTA_OFF_SCREEN"] = "true"
os.environ["MPLBACKEND"] = "Agg"

actual_path = Path(__file__).parent.absolute()
examples_path = actual_path.parent / "examples"
print(examples_path)

# Get the DPF server version
server = dpf.server.get_or_create_server(None)
server_version = server.version
server.shutdown()
print(f"Server version: {server_version}")

for root, subdirectories, files in os.walk(examples_path):
    for subdirectory in subdirectories:
        subdir = Path(root) / subdirectory
        for file in subdir.glob("*.py"):
            if sys.platform == "linux" and "08-python-operators" in str(file):
                continue
            elif "win" in sys.platform and "06-distributed_stress_averaging" in str(file):
                # Currently very unstable in the GH CI
                continue
            print("\n--------------------------------------------------")
            print(file)
            minimum_version_str = get_example_required_minimum_dpf_version(file)
            if float(server_version) - float(minimum_version_str) < -0.05:
                print(f"Example skipped as it requires DPF {minimum_version_str}.", flush=True)
                continue
            try:
                out = subprocess.check_output([sys.executable, str(file)])
            except subprocess.CalledProcessError as e:
                sys.stderr.write(str(e.args))
                if e.returncode != 3221225477:
                    print(out, flush=True)
                    raise e
            print("PASS", flush=True)
