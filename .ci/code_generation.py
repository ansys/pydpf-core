# import subprocess

from ansys.dpf import core
from ansys.dpf.core.operators import build
import os
import glob
from pathlib import Path
import shutil


local_dir = Path(__file__).parent
TARGET_PATH = local_dir.parent / "src" / "ansys" / "dpf" / "core" / "operators"
files = TARGET_PATH.glob("*")
for file_path in files:
    if file_path.stem == "specification":
        continue
    if file_path.name == "build.py":
        continue
    if file_path.name == "operator.mustache":
        continue
    try:
        if file_path.is_dir():
            shutil.rmtree(file_path)
        else:
            file_path.unlink()
    except:
        pass

core.set_default_server_context(core.AvailableServerContexts.premium)
core.start_local_server(config=core.AvailableServerConfigs.LegacyGrpcServer)

build.build_operators()
