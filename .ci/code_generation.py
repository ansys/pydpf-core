# import subprocess

from ansys.dpf import core
from ansys.dpf.core.operators import build
import os
import glob
from pathlib import Path
import shutil


local_dir = os.path.dirname(os.path.abspath(__file__))
TARGET_PATH = os.path.join(local_dir, os.pardir, "src", "ansys", "dpf", "core", "operators")
files = glob.glob(os.path.join(TARGET_PATH, "*"))
for f in files:
    if Path(f).stem == "specification":
        continue
    if Path(f).name == "build.py":
        continue
    if Path(f).name == "operator.mustache":
        continue
    try:
        if os.path.isdir(f):
            shutil.rmtree(f)
        else:
            os.remove(f)
    except:
        pass

core.set_default_server_context(core.AvailableServerContexts.premium)
core.start_local_server(config=core.AvailableServerConfigs.LegacyGrpcServer)

build.build_operators()
