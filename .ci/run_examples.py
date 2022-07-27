import os
import glob
from ansys.dpf import core
import pathlib
import subprocess
import sys

os.environ["PYVISTA_OFF_SCREEN"] = "true"
os.environ["MPLBACKEND"] = "Agg"

actual_path = pathlib.Path(__file__).parent.absolute()
print(os.path.join(actual_path, os.path.pardir, "examples"))


DPF_SERVER_TYPE = os.environ.get("DPF_SERVER_TYPE", None)
if DPF_SERVER_TYPE:
    if DPF_SERVER_TYPE == "INPROCESS":
        core.SERVER_CONFIGURATION = core.AvailableServerConfigs.InProcessServer
    elif DPF_SERVER_TYPE == "GRPC":
        core.SERVER_CONFIGURATION = core.AvailableServerConfigs.GrpcServer
    elif DPF_SERVER_TYPE == "LEGACYGRPC":
        core.SERVER_CONFIGURATION = core.AvailableServerConfigs.LegacyGrpcServer

for root, subdirectories, files in os.walk(os.path.join(actual_path, os.path.pardir, "examples")):
    for subdirectory in subdirectories:
        subdir = os.path.join(root, subdirectory)
        for file in glob.iglob(os.path.join(subdir, "*.py")):
            print("\n\n--------------------------------------------------\n")
            print(file)
            print("--------------------------------------------------\n")
            try:
                subprocess.check_call([sys.executable, file])
            except Exception as e:
                sys.stderr.write(str(e.args))
                raise e
