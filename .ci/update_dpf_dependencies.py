"""Script to update ansys.dpf.gate.generated, ansys.dpf.gatebin and ansys.grpc.dpf.

This script should only be used to quickly test changes to any of these dependencies.
Actual commit of updated code should not occur.
The GitHub pipelines take care of the actual update in ansys-dpf-core.

Define environment variables to know where to get the code from:
- "DPFDV_ROOT" defines the DPF repo where ansys-grpc-dpf resides.
  Will unzip the latest wheel built in DPF/proto/dist/.
- "ANSYSDPFPYGATE_ROOT" defines where the ansys-dpf-pygate repository resides.

It will update the current repo
or the repo defined by the environment variable "ANSYSDPFCORE_ROOT" if it exists.
"""
import os
import glob
import pathlib
import platform
import shutil
import zipfile


grpc_path_key = "DPFDV_ROOT"
gate_path_key = "ANSYSDPFPYGATE_ROOT"
core_path = pathlib.Path(__file__).parent.parent.resolve()
if "ANSYSDPFCORE_ROOT" in os.environ:
    core_path = os.environ["ANSYSDPFCORE_ROOT"]

grpc_path = os.getenv(grpc_path_key, None)
gate_path = os.getenv(gate_path_key, None)

if grpc_path is not None:
    # Update ansys-grpc-dpf with latest in proto/dist
    print("Updating ansys.grpc.dpf")
    dist_path = os.path.join(grpc_path, "proto", "dist", "*")
    print(f"from {dist_path}")
    destination = os.path.join(core_path, "src")
    print(f"into {destination}")
    latest_wheel = max(glob.glob(dist_path), key=os.path.getctime)
    with zipfile.ZipFile(latest_wheel, "r") as wheel:
        for file in wheel.namelist():
            # print(file)
            if file.startswith("ansys/"):
                wheel.extract(
                    file,
                    path=destination,
                )
    print("Done updating ansys.grpc.dpf")
else:
    print(f"{grpc_path_key} environment variable is not defined. " "Cannot update ansys-grpc-dpf.")

if gate_path is not None:
    # Update ansys-dpf-gate
    print("Updating ansys.dpf.gate generated code")
    dist_path = os.path.join(gate_path, "ansys-dpf-gate", "ansys", "dpf", "gate", "generated")
    print(f"from {dist_path}")
    destination = os.path.join(core_path, "src", "ansys", "dpf", "gate", "generated")
    print(f"into {destination}")
    shutil.copytree(
        src=dist_path,
        dst=destination,
        dirs_exist_ok=True,
        ignore=lambda directory, contents: ["__pycache__"] if directory[-5:] == "gate" else [],
    )
    dist_path = os.path.join(gate_path, "ansys-dpf-gate", "ansys", "dpf", "gate", "__init__.py")
    print(f"from {dist_path}")
    destination = os.path.join(core_path, "src", "ansys", "dpf", "gate", "__init__.py")
    print(f"into {destination}")
    shutil.copy(
        src=dist_path,
        dst=destination,
    )
    print("Done updating ansys.dpf.gate generated code")

    # Update ansys-dpf-gatebin
    print("Updating ansys.dpf.gatebin")
    dist_path = os.path.join(gate_path, "ansys-dpf-gatebin", "ansys")
    print(f"from {dist_path}")
    destination = os.path.join(core_path, "src", "ansys")
    print(f"into {destination}")
    shutil.copytree(
        src=dist_path,
        dst=destination,
        dirs_exist_ok=True,
    )
    print(f"Done updating ansys.dpf.gatebin for {platform.system()}")
else:
    print(
        f"{gate_path_key} environment variable is not defined. "
        "Cannot update ansys.dpf.gate or ansys.dpf.gatebin."
    )
