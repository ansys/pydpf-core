import weakref

import pytest
import numpy as np

from ansys import dpf
from ansys.dpf.core import FieldsContainer, Field, TimeFreqSupport
from ansys.dpf.core import errors as dpf_errors
from ansys.dpf.core import fields_factory


@pytest.fixture()
def disp_fc(allkindofcomplexity):
    """Return a displacement fields container"""
    model = dpf.core.Model(allkindofcomplexity)
    return model.results.displacement().outputs.fields_container()


def test_create_fields_container():
    fc = FieldsContainer()
    assert fc._message.id != 0


def test_empty_index():
    fc = FieldsContainer()
    with pytest.raises(IndexError):
        fc[0]


def test_createby_message_copy_fields_container():
    fc= FieldsContainer()
    fields_container2 = FieldsContainer(fields_container=fc._message)
    assert fc._message.id == fields_container2._message.id
    
    
def test_createbycopy_fields_container():
    fc= FieldsContainer()
    fields_container2 = FieldsContainer(fields_container=fc)
    assert fc._message.id == fields_container2._message.id


def test_set_get_field_fields_container(): 
    fc= FieldsContainer()
    fc.labels =['time','complex']
    for i in range(0,20):
        mscop = {"time":i+1,"complex":0}
        fc.add_field(mscop,Field(nentities=i+10))
    assert fc.get_available_ids_for_label() == list(range(1,21))
    for i in range(0,20):
        fieldid =fc.get_fields({"time":i+1,"complex":0})._message.id
        assert fieldid !=0
        assert fc.get_fields(i)._message.id !=0
        assert fc.get_fields_by_time_complex_ids(timeid=i+1,complexid=0)._message.id !=0
        assert fc[i]._message.id != 0
        
        
def test_get_label_scoping(): 
    fc= FieldsContainer()
    fc.labels =['time','complex']
    for i in range(0,20):
        mscop = {"time":i+1,"complex":0}
        fc.add_field(mscop,Field(nentities=i+10))
    scop = fc.get_label_scoping()
    assert scop._message.id != 0
    assert scop.ids == list(range(1,21))
        

def test_set_get_field_fields_container_new_label(): 
    fc= FieldsContainer()
    fc.labels =['time','complex']
    for i in range(0,20):
        mscop = {"time":i+1,"complex":0}
        fc.add_field(mscop,Field(nentities=i+10))
    assert fc.get_available_ids_for_label() == list(range(1,21))
    for i in range(0,20):
        fieldid =fc.get_fields({"time":i+1,"complex":0})._message.id
        assert fieldid !=0
        assert fc.get_fields(i)._message.id !=0
        assert fc.get_fields_by_time_complex_ids(timeid=i+1,complexid=0)._message.id !=0
        assert fc[i]._message.id != 0
        assert fc.get_label_space(i)=={"time":i+1,"complex":0}
    fc.add_label('shape')
    for i in range(0,20):
        mscop = {"time":i+1,"complex":0, 'shape':1}
        fc.add_field(mscop,Field(nentities=i+10))

    assert len(fc.get_fields({"time":i+1,"complex":0}))==2
        
    for i in range(0,20):
        fieldid =fc.get_fields({"time":i+1,"complex":0, 'shape':1})._message.id
        assert fieldid !=0
        assert fc.get_fields(i+20)._message.id !=0
        assert fc[i]._message.id != 0
        assert fc.get_label_space(i+20)=={"time":i+1,"complex":0, 'shape':1}
    
        


def test_set_get_field_fields_container_new_label_default_value(): 
    fc= FieldsContainer()
    fc.labels =['time','complex']
    for i in range(0,20):
        mscop = {"time":i+1,"complex":0}
        fc.add_field(mscop,Field(nentities=i+10))
    fc.add_label('shape',3)
    for i in range(0,20):
        mscop = {"time":i+1,"complex":0, 'shape':1}
        fc.add_field(mscop,Field(nentities=i+10))
    for i in range(0,20):
        fieldid =fc.get_fields({"time":i+1,"complex":0, 'shape':1})._message.id
        assert fieldid !=0
        assert fc.get_fields(i+20)._message.id !=0
        assert fc[i]._message.id != 0
        assert fc.get_label_space(i+20)=={"time":i+1,"complex":0, 'shape':1}
    for i in range(0,20):
        fieldid =fc.get_fields({"time":i+1,"complex":0, 'shape':3})._message.id
        assert fieldid !=0
        assert fc.get_fields(i)._message.id !=0
        assert fc[i]._message.id != 0
        assert fc.get_label_space(i)=={"time":i+1,"complex":0, 'shape':3}


def test_get_item_field_fields_container():
    fc= FieldsContainer()
    fc.labels =['time','complex']
    for i in range(0,20):
        mscop = {"time":i+1,"complex":0}
        fc.add_field(mscop,Field(nentities=i+10))
    for i in range(0,20):
        assert fc[i]._message.id !=0


def test_delete_fields_container():
    fc = FieldsContainer()
    ref = weakref.ref(fc)
    del fc
    assert ref() is None


# @pytest.mark.skipif(ON_WINDOWS_AZURE, reason='Causes segfault on Azure')
def test_delete_auto_fields_container():
    fc = FieldsContainer()
    fc2 = FieldsContainer(fields_container=fc)
    del fc
    with pytest.raises(dpf_errors.DPFServerNullObject):
        fc2._info


def test_str_fields_container(disp_fc):
    assert 'time' in str(disp_fc)
    assert 'location' in str(disp_fc)


def test_support_fields_container(disp_fc):
    support = disp_fc.time_freq_support
    assert len(support.time_frequencies) == 1


def test_getitem_fields_container(disp_fc):
    assert isinstance(disp_fc[0], dpf.core.Field)
    
    
def test_has_label(disp_fc):
    fc = FieldsContainer()
    fc.labels = ['time','complex']
    assert fc.has_label('time') == True
    assert fc.has_label('complex') == True
    assert fc.has_label('body') == False
    
    assert disp_fc.has_label('time') == True
    assert fc.has_label('body') == False
    
    
def test_add_field_by_time_id():
    fc = FieldsContainer()
    fc.labels = ['time','complex']
    f1 = Field(3)
    f1.append([10.2, 3.0, -11.8], 1)
    f1.data
    f1.append([10.2, 2.0, 11.8], 2)
    f1.append([10.2, 1.0, -11.8], 3)
    mscop1 = {"time": 1,"complex": 0}
    fc.add_field(mscop1, f1)
    assert len(fc) == 1
    f2 = Field(1)
    f2.append([4.0, 4.4, 3.6], 1)
    mscop2 = {"time": 1,"complex": 1}
    fc.add_field(mscop2, f2)
    assert len(fc) == 2
    f3 = Field(1)
    f3.append([0.0, 0.4, 0.6], 1)
    fc.add_field_by_time_id(f3, 2)
    field_to_compare = Field(1)
    field_to_compare.append([0.0, 0.4, 0.6], 1)
    field = fc.get_fields({'time': 2, 'complex': 0})
    assert len(fc) == 3
    assert np.allclose(field.data, field_to_compare.data)
    
    fc.add_field_by_time_id(f3, 1)
    field_result_1 = fc.get_fields({'time': 1, 'complex': 0})
    field_result_2 = fc.get_fields({'time': 2, 'complex': 0})
    assert np.allclose(field_result_1.data, field_result_2.data)
    
    fc.add_label('body')
    with pytest.raises(dpf_errors.DpfValueError):
        fc.add_field_by_time_id(f3, 10)
        

def test_add_imaginary_field():
    fc = FieldsContainer()
    fc.labels = ['time','complex']
    f1 = Field(3)
    f1.append([10.2, 3.0, -11.8], 1)
    f1.append([10.2, 2.0, 11.8], 2)
    f1.append([10.2, 1.0, -11.8], 3)
    mscop1 = {"time": 1,"complex": 1}
    fc.add_field(mscop1, f1)
    assert len(fc) == 1
    f2 = Field(1)
    f2.append([4.0, 4.4, 3.6], 1)
    mscop2 = {"time": 1,"complex": 0}
    fc.add_field(mscop2, f2)
    assert len(fc) == 2
    f3 = Field(1)
    f3.append([0.0, 0.4, 0.6], 1)
    fc.add_imaginary_field(f3, 2)
    field_to_compare = Field(1)
    field_to_compare.append([0.0, 0.4, 0.6], 1)
    field = fc.get_fields({'time': 2, 'complex': 1})
    assert len(fc) == 3
    assert np.allclose(field.data, field_to_compare.data)
    
    fc.add_imaginary_field(f3, 1)
    field_result_1 = fc.get_fields({'time': 1, 'complex': 1})
    field_result_2 = fc.get_fields({'time': 2, 'complex': 1})
    assert np.allclose(field_result_1.data, field_result_2.data)
    
    fc.add_label('body')
    with pytest.raises(dpf_errors.DpfValueError):
        fc.add_imaginary_field(f3, 10)
        

def test_get_imaginary_field(disp_fc):
    with pytest.raises(dpf_errors.DpfValueError):
        disp_fc.get_imaginary_fields(1)
    fc = FieldsContainer()
    fc.labels = ["complex"]
    with pytest.raises(dpf_errors.DpfValueError):
        fc.get_imaginary_fields(1)
    fc = FieldsContainer()
    fc.labels = ["time", "complex"]
    field_real = Field(1)
    field_real.append([0.0, 3.0, 4.1], 20)
    fc.add_field({"time" : 1, "complex" : 0}, field_real)
    field_to_check = fc.get_imaginary_fields(1)
    assert field_to_check is None
    field_img = Field(1)
    field_img.append([1.0, 301.2, 4.2], 20)
    fc.add_field({"time" : 1, "complex" : 1}, field_img)
    field_to_check_2 = fc.get_imaginary_fields(1)
    assert np.allclose(field_img.data, field_to_check_2.data)
    
def test_get_field_by_time_id():
    fc = FieldsContainer()
    fc.labels = ["complex"]
    with pytest.raises(dpf_errors.DpfValueError):
        fc.get_field_by_time_id(1)
    fc = FieldsContainer()
    fc.labels = ["time", "complex"]
    field_img = Field(1)
    field_img.append([0.0, 3.0, 4.1], 20)
    fc.add_field({"time" : 1, "complex" : 1}, field_img)
    field_to_check = fc.get_field_by_time_id(1)
    assert field_to_check is None
    field_real = Field(1)
    field_real.append([1.0, 301.2, 4.2], 20)
    fc.add_field({"time" : 1, "complex" : 0}, field_real)
    field_to_check_2 = fc.get_field_by_time_id(1)
    assert np.allclose(field_real.data, field_to_check_2.data)
    
    fc2 = FieldsContainer()
    fc2.labels = ["time"]
    f1 = Field(1)
    f1.append([0.0, 3.0, 4.1], 20)
    fc.add_field({"time" : 1, "complex" : 0}, f1)
    field_to_check = fc.get_field_by_time_id(1)
    assert np.allclose(f1.data, field_to_check.data)

def test_collection_update_support():
    # set time_freq_support
    fc = FieldsContainer()
    tfq = TimeFreqSupport()
    frequencies = fields_factory.create_scalar_field(3)
    frequencies.data = [0.1, 0.32, 0.4]
    tfq.time_frequencies = frequencies
    fc.time_freq_support = tfq
    # get time_freq_support
    tfq_check = fc.time_freq_support
    assert np.allclose(tfq.time_frequencies.data, tfq_check.time_frequencies.data) 
    
  
if __name__ == "__main__":   
    test_add_field_by_time_id()
