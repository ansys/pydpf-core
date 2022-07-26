import os
import glob
import pathlib
from ansys.dpf import core

core.settings.disable_off_screen_rendering()

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
                exec(
                    open(file, mode="r", encoding="utf8").read(),
                    globals(),
                    globals())
            except core.errors.ServerTypeError as e:
                if core.SERVER_CONFIGURATION != core.AvailableServerConfigs.InProcessServer:
                    raise e


