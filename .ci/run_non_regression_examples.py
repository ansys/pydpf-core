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

list_tests = [
    os.path.join(actual_path, os.path.pardir, "examples", "00-basic"),
    os.path.join(actual_path, os.path.pardir, "examples", "01-static-transient"),
    os.path.join(actual_path, os.path.pardir, "examples", "02-modal-harmonic"),
    os.path.join(actual_path, os.path.pardir, "examples", "05-plotting", "00-basic_plotting.py"),
    os.path.join(actual_path, os.path.pardir, "examples", "05-plotting", "05-plot_on_warped_mesh.py"),
    os.path.join(actual_path, os.path.pardir, "examples", "06-distributed-post",
                 "00-distributed_total_disp.py"),
    ]

if core.SERVER_CONFIGURATION != core.AvailableServerConfigs.InProcessServer:
    list_tests.append(os.path.join(actual_path, os.path.pardir, "examples", "07-python-operators",
                 "00-wrapping_numpy_capabilities.py"))

for path in list_tests:
    if os.path.isdir(path):
        for file in glob.iglob(os.path.join(path, "*.py")):
            print("\n\n--------------------------------------------------\n")
            print(file)
            print("--------------------------------------------------\n")
            try:
                subprocess.check_call([sys.executable, file])
            except Exception as e:
                sys.stderr.write(str(e.args))
    else:
        print("\n\n--------------------------------------------------\n")
        print(path)
        print("--------------------------------------------------\n")
        try:
            subprocess.check_call([sys.executable, path])
        except Exception as e:
            sys.stderr.write(str(e.args))

