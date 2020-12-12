import weakref

import pytest
from grpc._channel import _InactiveRpcError

from ansys import dpf
from ansys.dpf.core import FieldsContainer, Field
from ansys.dpf.core import errors as dpf_errors


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
    field = fc[0]
    assert field is None


def test_createbycopy_fields_container():
    fc= FieldsContainer()
    fields_container2 = FieldsContainer(fields_container=fc._message)
    assert fc._message.id == fields_container2._message.id


def test_set_get_field_fields_container(): 
    fc= FieldsContainer()
    fc.labels =['time','complex']
    for i in range(0,20):
        mscop = {"time":i+1,"complex":0}
        fc.add_field(mscop,Field(nentities=i+10))
    assert fc.get_ids() == list(range(1,21))
    for i in range(0,20):
        fieldid =fc.get_fields({"time":i+1,"complex":0})._message.id
        assert fieldid !=0
        assert fc.get_fields(i)._message.id !=0
        assert fc.get_fields_by_time_complex_ids(timeid=i+1,complexid=0)._message.id !=0
        assert fc[i]._message.id != 0
        
    
def test_set_get_field_fields_container_new_label(): 
    fc= FieldsContainer()
    fc.labels =['time','complex']
    for i in range(0,20):
        mscop = {"time":i+1,"complex":0}
        fc.add_field(mscop,Field(nentities=i+10))
    assert fc.get_ids() == list(range(1,21))
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
    try :
        fc.get_fields({"time":i+1,"complex":0})
        assert False
    except :
        assert True
    for i in range(0,20):
        fieldid =fc.get_fields({"time":i+1,"complex":0, 'shape':1})._message.id
        assert fieldid !=0
        assert fc.get_fields(i+20)._message.id !=0
        assert fc[i]._message.id != 0
        assert fc.get_label_space(i+20)=={"time":i+1,"complex":0, 'shape':1}


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


def test_delete_auto_fields_container():
    fc = FieldsContainer()
    fc2 = FieldsContainer(fields_container=fc)
    del fc
    with pytest.raises(dpf_errors.DPFServerNullObject):
        fc2._info


def test_str_fields_container(disp_fc):
    assert 'time' in str(disp_fc)


def test_support_fields_container(disp_fc):
    support = disp_fc.time_freq_support
    assert len(support.frequencies) == 1


def test_getitem_fields_container(disp_fc):
    assert isinstance(disp_fc[0], dpf.core.Field)
