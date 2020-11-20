# -*- coding: utf-8 -*-

import os
import numpy as np
from ansys import dpf


if 'AWP_UNIT_TEST_FILES' in os.environ:
    unit_test_files = os.environ['AWP_UNIT_TEST_FILES']
else:
    raise KeyError('Please add the location of the DataProcessing '
                   'test files "AWP_UNIT_TEST_FILES" to your env')

TEST_FILE_PATH = os.path.join(unit_test_files, 'DataProcessing', 'rst_operators',
                              'ASimpleBar.rst')


if not dpf.core.has_local_server():
    dpf.core.start_local_server()
    
try:

    base = dpf.core.BaseService(ip=dpf.core._global_ip(), port = dpf.core._global_port())
    base.load_library("Ans.Dpf.Hdf5.dll","hdf5")
    hdf5_loaded = True
    
except:
     hdf5_loaded = False

def test_hdf5_loaded():
    if hdf5_loaded:
        op = dpf.core.Operator("serialize_to_hdf5")
        assert op.inputs != None
        
def test_hdf5_ellipsis_any_pins():
    if hdf5_loaded:
        model=dpf.core.Model(TEST_FILE_PATH)
        u = model.operator("U")
        s= model.operator("S")
        op = dpf.core.Operator("serialize_to_hdf5")
        op.inputs.file_path.connect(r'c:/temp/hdf5.h5')
        op.inputs.data(u.outputs)
        op.inputs.data(s.outputs)
        assert len(op.inputs._connected_inputs)==3