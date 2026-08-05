import os
from pathlib import Path
import subprocess
import sys

from packaging.version import Version as PkgVersion

import ansys.dpf.core as dpf
from ansys.dpf.core.examples import get_example_required_minimum_dpf_version

_WINDOWS_ACCESS_VIOLATION_RETURNCODE = 3221225477  # 0xC0000005 STATUS_ACCESS_VIOLATION

os.environ["PYVISTA_OFF_SCREEN"] = "true"
os.environ["MPLBACKEND"] = "Agg"

actual_path = Path(__file__).parent.absolute()
examples_path = actual_path.parent / "doc" / "sphinx_gallery_examples"
print(examples_path)

# Get the DPF server version
server = dpf.server.get_or_create_server(None)
server_version = server.version
server.shutdown()
print(f"Server version: {server_version}")

skipped_docker = [
    "03-distributed-msup_expansion_steps.py",
    "06-distributed_stress_averaging.py",
    "01-distributed_workflows_on_remote.py",
    "00-distributed_total_disp.py",
    "02-distributed-msup_expansion.py",
]

for root, subdirectories, files in os.walk(examples_path):
    for subdirectory in subdirectories:
        subdir = Path(root) / subdirectory
        for file in subdir.glob("*.py"):
            if ("08-python-operators" in str(file) or "12-fluids" in str(file)) and (
                sys.platform == "linux" or server_version == "2027.1.0pre0"
            ):
                continue
            elif "win" in sys.platform and "06-distributed_stress_averaging" in str(file):
                # Currently very unstable in the GH CI
                continue
            if os.environ.get("DPF_DOCKER", None) is not None and Path(file).name in skipped_docker:
                print(f"Skipping ${file} in Docker context", flush=True)
                continue

            print("\n--------------------------------------------------")
            print(file)
            minimum_version_str = get_example_required_minimum_dpf_version(file)
            if PkgVersion(server_version) < PkgVersion(minimum_version_str):
                print(f"Example skipped as it requires DPF {minimum_version_str}.", flush=True)
                continue
            try:
                out = subprocess.check_output([sys.executable, str(file)])
            except subprocess.CalledProcessError as e:
                sys.stderr.write(str(e.args))
                if e.returncode != _WINDOWS_ACCESS_VIOLATION_RETURNCODE:
                    print(out, flush=True)
                    raise e
            print("PASS", flush=True)
