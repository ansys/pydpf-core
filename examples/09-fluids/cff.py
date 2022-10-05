import os
from ansys.dpf import core as dpf
from ansys.dpf.core import examples

from ansys.dpf.core.dpf_operator import available_operator_names


server = dpf.start_local_server()
available_operators = available_operator_names(server=server)
cff_operators = [operator for operator in available_operators if "cff::" in operator]
print(cff_operators)

# Ok to plot all CFX models
# Ok to plot all fluent models except for Polys (which is logical)
data_path = r"D:\ANSYSDev\Sandbox\cff\Ans.Dpf.CFF\Ans.Dpf.CFFTest\test_models\fluent\3D"
cas_path = dat_path = os.path.join(data_path, r"Polys\Polys.cas.h5")
# cas_path = dat_path = os.path.join(data_path, r"Hex\Hex.cas.h5")
# fluent_files = examples.download_fluent_files()
# cas_path = fluent_files["cas"]
# dat_path = fluent_files["dat"]
# data_path = r"D:\ANSYSDev\Sandbox\cff\Ans.Dpf.CFF\Ans.Dpf.CFFTest\test_models\CFX"
# file_path = os.path.join(data_path, r"HeatingCoil\HeatingCoil.res")
ds = dpf.DataSources()
ds.set_result_file_path(cas_path, "cas")
ds.add_file_path(dat_path, "dat")
print(ds)

model = dpf.Model(data_sources=ds)
print(model)
model.plot(opacity=0.3)

# print(dir(model.results))
