from ansys.dpf import core
import os
import glob
from pathlib import Path
import time
import shutil

if os.name == "posix":
    LIB_TO_GENERATE = [
        "libAns.Dpf.Native.so",
        "libAns.Dpf.FEMutils.so",
        "libmapdlOperatorsCore.so",
        "libmeshOperatorsCore.so",
        "libAns.Dpf.Math.so",
        "libAns.Dpf.Hdf5.so",
    ]
else:
    LIB_TO_GENERATE = [
        "Ans.Dpf.Native.dll",
        "Ans.Dpf.FEMutils.dll",
        "meshOperatorsCore.dll",
        "mapdlOperatorsCore.dll",
        "Ans.Dpf.Math.dll",
        "Ans.Dpf.Hdf5.dll",
    ]

local_dir = os.path.dirname(os.path.abspath(__file__))
TARGET_PATH = os.path.join(local_dir, os.pardir, "ansys", "dpf", "core", "operators")
files = glob.glob(os.path.join(TARGET_PATH, "*"))
for f in files:
    if Path(f).stem == "specification":
        continue
    try:
        if os.path.isdir(f):
            shutil.rmtree(f)
        else:
            os.remove(f)
    except:
        pass
core.start_local_server()
code_gen = core.Operator("python_generator")
code_gen.connect(1, TARGET_PATH)
for lib in LIB_TO_GENERATE:
    code_gen.connect(0, lib)
    if lib != LIB_TO_GENERATE[0]:
        code_gen.connect(2, False)
    else:
        code_gen.connect(2, True)
    code_gen.run()
    time.sleep(0.1)

core.SERVER.shutdown()
