from ansys.dpf import core
import os
import glob
from pathlib import Path

if (os.environ.get('AWP_ROOTDV_DEV', False) is False):
    raise ValueError("AWP_ROOTDV_DEV environment variable is expected")

if os.name == 'posix':
    LIB_TO_GENERATE =["libAns.Dpf.Native.so",
                      "libAns.Dpf.FEMutils.so",
                      "libmapdlOperatorsCore.so",
                      "libmeshOperatorsCore.so"]
else:
    LIB_TO_GENERATE =["Ans.Dpf.Native.dll",
                      "Ans.Dpf.FEMutils.dll",
                      "meshOperatorsCore.dll",
                      "mapdlOperatorsCore.dll"]

local_dir =os.path.dirname(os.path.abspath(__file__))
TARGET_PATH = os.path.join(local_dir,os.pardir,"ansys", "dpf","core", "operators")
files = glob.glob(os.path.join(TARGET_PATH, "*"))
for f in files:
    if Path(f).stem=="specification":
        continue
    try:
        os.remove(f)
    except:
        pass
core.start_local_server(ansys_path= os.environ["AWP_ROOTDV_DEV"])
code_gen = core.Operator("python_generator")
code_gen.connect(1,TARGET_PATH)
for lib in LIB_TO_GENERATE:
    code_gen.connect(0, lib)
    if lib != LIB_TO_GENERATE[0]:
        code_gen.connect(2,False)
    else:        
        code_gen.connect(2,True)
    code_gen.run()

core.SERVER.shutdown()