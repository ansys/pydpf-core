# import subprocess

import glob
import os
from pathlib import Path
import shutil

from ansys.dpf import core
from ansys.dpf.core.operators import build

core.set_default_server_context(core.AvailableServerContexts.premium)
core.start_local_server(config=core.AvailableServerConfigs.LegacyGrpcServer)

files_to_keep = {
    "operator.mustache": "",
    "build.py": "",
    "specification.py": "",
    "translator.py": "",
    # Deprecated operator scripting names
    "result": [
        "gasket_deformation.py",
        "gasket_deformation_X.py",
        "gasket_deformation_XY.py",
        "gasket_deformation_XZ.py",
    ],
}

local_dir = Path(__file__).parent
TARGET_PATH = local_dir.parent / "src" / "ansys" / "dpf" / "core" / "operators"
files = TARGET_PATH.glob("*")
for file_path in files:
    if file_path.is_file() and (file_path.name in files_to_keep):
        continue
    if file_path.is_dir():
        shutil.rmtree(file_path / "__pycache__", ignore_errors=True)
        if file_path.name in files_to_keep:
            sub_files = file_path.glob("*")
            for sub_file in sub_files:
                if sub_file.name not in files_to_keep[file_path.name]:
                    sub_file.unlink()
        else:
            shutil.rmtree(file_path)
    else:
        file_path.unlink()

build.build_operators()
