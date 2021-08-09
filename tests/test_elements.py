import pytest

from ansys.dpf import core as dpf


@pytest.fixture()
def model_elements(allkindofcomplexity):
    model = dpf.Model(allkindofcomplexity)
    elements = model.metadata.meshed_region.elements
    return elements

@pytest.fixture()
def hexa_element_descriptor(model_elements):
    el_index = model_elements.scoping.index(251)
    descriptor = dpf.element_types.descriptor(model_elements[el_index].type)
    return descriptor

@pytest.fixture()
def quad_element_descriptor(model_elements):
    el_index = model_elements.scoping.index(10660)
    return dpf.element_types.descriptor(model_elements[el_index].type)

@pytest.fixture()
def tetra_element_descriptor(model_elements):
    el_index = model_elements.scoping.index(3905)
    return dpf.element_types.descriptor(model_elements[el_index].type)

@pytest.fixture()
def line_element_descriptor(model_elements):
    el_index = model_elements.scoping.index(10834)
    return dpf.element_types.descriptor(model_elements[el_index].type)

def test_hexa_element_descriptor(hexa_element_descriptor):
    assert isinstance(hexa_element_descriptor, dpf.ElementDescriptor)
    assert hexa_element_descriptor.element_id == 1
    assert hexa_element_descriptor.description == 'Quadratic 20-nodes Hexa'
    assert hexa_element_descriptor.name == 'hex20'
    assert hexa_element_descriptor.shape == 'solid'
    assert hexa_element_descriptor.number_of_corner_nodes == 8
    assert hexa_element_descriptor.number_of_mid_nodes == 12
    assert hexa_element_descriptor.number_of_nodes == 20
    assert hexa_element_descriptor.is_solid == True
    assert hexa_element_descriptor.is_shell == False
    assert hexa_element_descriptor.is_beam == False
    assert hexa_element_descriptor.is_quadratic == True
    
def test_quad_element_descriptor(quad_element_descriptor):
    assert isinstance(quad_element_descriptor, dpf.ElementDescriptor)
    assert quad_element_descriptor.element_id == 16
    assert quad_element_descriptor.description == 'Linear 4-nodes Quadrangle'
    assert quad_element_descriptor.name == 'quad4'
    assert quad_element_descriptor.shape == 'shell'
    assert quad_element_descriptor.number_of_corner_nodes == 4
    assert quad_element_descriptor.number_of_mid_nodes == 0
    assert quad_element_descriptor.number_of_nodes == 4
    assert quad_element_descriptor.is_solid == False
    assert quad_element_descriptor.is_shell == True
    assert quad_element_descriptor.is_beam == False
    assert quad_element_descriptor.is_quadratic == False

def test_tetra_element_descriptor(tetra_element_descriptor):
    assert isinstance(tetra_element_descriptor, dpf.ElementDescriptor)
    assert tetra_element_descriptor.element_id == 10
    assert tetra_element_descriptor.description == 'Quadratic 10-nodes Tetrahedron'
    assert tetra_element_descriptor.name == 'tet10'
    assert tetra_element_descriptor.shape == 'solid'
    assert tetra_element_descriptor.number_of_corner_nodes == 4
    assert tetra_element_descriptor.number_of_mid_nodes == 6
    assert tetra_element_descriptor.number_of_nodes == 10
    assert tetra_element_descriptor.is_solid == True
    assert tetra_element_descriptor.is_shell == False
    assert tetra_element_descriptor.is_beam == False
    assert tetra_element_descriptor.is_quadratic == True
    
def test_line_element_descriptor(line_element_descriptor):
    assert isinstance(line_element_descriptor, dpf.ElementDescriptor)
    assert line_element_descriptor.element_id == 18
    assert line_element_descriptor.description == 'Linear 2-nodes Line'
    assert line_element_descriptor.name == 'line2'
    assert line_element_descriptor.shape == 'beam'
    assert line_element_descriptor.number_of_corner_nodes == 2
    assert line_element_descriptor.number_of_mid_nodes == 0
    assert line_element_descriptor.number_of_nodes == 2
    assert line_element_descriptor.is_solid == False
    assert line_element_descriptor.is_shell == False
    assert line_element_descriptor.is_beam == True
    assert line_element_descriptor.is_quadratic == False
    
def test_no_element_descriptor():
    # descriptor = dpf.element_types.descriptor(89)
    # assert not descriptor
    descriptor = dpf.element_types.descriptor(dpf.element_types.General)
    unknown_shape = "unknown_shape"
    assert descriptor.shape == unknown_shape
    assert dpf.element_types.descriptor(dpf.element_types.General).shape == unknown_shape
