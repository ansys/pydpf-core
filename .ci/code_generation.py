# import subprocess

from ansys.dpf import core
from ansys.dpf.core.operators import build
import os
import glob
from pathlib import Path
import time
import shutil


core.set_default_server_context(core.AvailableServerContexts.premium)

if os.name == "posix":
    LIB_TO_GENERATE = [
        "libAns.Dpf.Native.so",
        "libAns.Dpf.FEMutils.so",
        "libmapdlOperatorsCore.so",
        "libmeshOperatorsCore.so",
        "libAns.Dpf.Math.so",
        "libAns.Dpf.Hdf5.so",
        "libAns.Dpf.LSDYNAHGP.so",
        "libAns.Dpf.LivePost.so",
        "libans.dpf.pointcloudsearch.so",
        "libAns.Dpf.Vtk.so",
        "libAns.Dpf.SystemCouplingMapping.so"
        "libAns.Dpf.MechanicalResults.so",
    ]
    LIB_OPTIONAL_TO_GENERATE = [
        "libAns.Dpf.SystemCouplingMapping.so",
    ]
else:
    LIB_TO_GENERATE = [
        "Ans.Dpf.Native.dll",
        "Ans.Dpf.FEMutils.dll",
        "meshOperatorsCore.dll",
        "mapdlOperatorsCore.dll",
        "Ans.Dpf.Math.dll",
        "Ans.Dpf.PythonPluginWrapper.dll",
        "Ans.Dpf.Hdf5.dll",
        "Ans.Dpf.FlowDiagram.dll",
        "Ans.Dpf.LSDYNAHGP.dll",
        "Ans.Dpf.LivePost.dll",
        "Ans.Dpf.PointCloudSearch.dll",
        "Ans.Dpf.Vtk.dll",
        "Ans.Dpf.SystemCouplingMapping.dll"
        "Ans.Dpf.MechanicalResults.dll",
    ]
    LIB_OPTIONAL_TO_GENERATE = [
        "Ans.Dpf.SystemCouplingMapping.dll",
    ]

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
core.start_local_server(config=core.AvailableServerConfigs.LegacyGrpcServer)
code_gen = core.Operator("python_generator")
code_gen.connect(1, TARGET_PATH)
for lib in LIB_TO_GENERATE:
    try:
        code_gen.connect(0, lib)
        if lib != LIB_TO_GENERATE[0]:
            code_gen.connect(2, False)
        else:
            code_gen.connect(2, True)
        print(f"Generating {lib} operators for server {core.SERVER.version}...")
        code_gen.run()
        time.sleep(0.1)
    except Exception as e:
        print(f"Could not generate operators for library {lib}:\n{str(e)}")
        raise e

for lib in LIB_OPTIONAL_TO_GENERATE:
    try:
        code_gen.connect(0, lib)
        if lib != LIB_OPTIONAL_TO_GENERATE[0]:
            code_gen.connect(2, False)
        else:
            code_gen.connect(2, True)
        print(f"Generating optional {lib} operators for server {core.SERVER.version}...")
        code_gen.run()
        time.sleep(0.1)
    except Exception as e:
        print(f"Could not generate operators for optional library {lib}:\n{str(e)}")

build.build_operators()
