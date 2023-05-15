"""Script to update ansys-dpf-gate, ansys-dpf-gatebin and ansys-grpc-dpf based on repositories

Define environment variables to know where to get the code from:
- "ANSYS_DPF_GRPC_ROOT" defines where ansys-grpc-dpf resides (DPF/proto/).
  Will unzip the latest wheel built in DPF/proto/dist/.
- "ANSYS_DPF_GATE_ROOT" defines where ansys-dpf-gate and ansys-dpf-gatebin are gathered from
"""
import os
import glob
import platform
import shutil
import zipfile


grpc_path_key = "ANSYS_DPF_GRPC_ROOT"
gate_path_key = "ANSYS_DPF_GATE_ROOT"

grpc_path = os.getenv(grpc_path_key, None)
gate_path = os.getenv(gate_path_key, None)

if grpc_path is not None:
    # Update ansys-grpc-dpf with latest in proto/dist
    dist_path = os.path.join(grpc_path, "dist", "*")
    latest_wheel = max(glob.glob(dist_path), key=os.path.getctime)
    with zipfile.ZipFile(latest_wheel, 'r') as wheel:
        for file in wheel.namelist():
            # print(file)
            if file.startswith('ansys/'):
                wheel.extract(
                    file,
                    path=os.path.join(os.getcwd(), "..", "src"),
                )
    print("Done updating ansys-grpc-dpf")
else:
    print(f"{grpc_path_key} environment variable is not defined. "
          "Cannot update ansys-grpc-dpf.")

if gate_path is not None:
    # Update ansys-dpf-gate
    shutil.copytree(
        src=os.path.join(gate_path, "ansys-dpf-gate", "ansys"),
        dst=os.path.join(os.getcwd(), "..", "src", "ansys"),
        dirs_exist_ok=True,
        ignore=lambda directory, contents: ["__pycache__"] if directory[-5:] == "gate" else [],
    )
    print("Done updating ansys-dpf-gate")

    # Update ansys-dpf-gatebin
    shutil.copytree(
        src=os.path.join(gate_path, "ansys-dpf-gatebin", "ansys"),
        dst=os.path.join(os.getcwd(), "..", "src", "ansys"),
        dirs_exist_ok=True,
    )
    print(f"Done updating ansys-dpf-gatebin for {platform.system()}")
else:
    print(f"{gate_path_key} environment variable is not defined. "
          "Cannot update ansys-dpf-gate or ansys-dpf-gatebin.")
