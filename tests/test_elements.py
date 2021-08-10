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

def check_element_attributes(descriptor, enum_id, description, 
                             name, shape, n_corner_nodes, n_mid_nodes, 
                             n_nodes, is_solid, is_shell, is_beam, 
                             is_quadratic):
    assert isinstance(descriptor, dpf.ElementDescriptor)
    assert descriptor.enum_id == enum_id
    assert descriptor.description == description
    assert descriptor.name == name
    assert descriptor.shape == shape
    assert descriptor.n_corner_nodes == n_corner_nodes
    assert descriptor.n_mid_nodes == n_mid_nodes
    assert descriptor.n_nodes == n_nodes
    assert descriptor.is_solid == is_solid
    assert descriptor.is_shell == is_shell
    assert descriptor.is_beam == is_beam
    assert descriptor.is_quadratic == is_quadratic

def test_hexa_element_descriptor(hexa_element_descriptor):
    check_element_attributes(hexa_element_descriptor, 1, 'Quadratic 20-nodes Hexa', 
                             'hex20', 'solid', 8, 12, 20, True, False, False, True)
    
def test_quad_element_descriptor(quad_element_descriptor):
    check_element_attributes(quad_element_descriptor, 16, 'Linear 4-nodes Quadrangle', 
                             'quad4', 'shell', 4, 0, 4, False, True, False, False)

def test_tetra_element_descriptor(tetra_element_descriptor):
    check_element_attributes(tetra_element_descriptor, 10, 'Quadratic 10-nodes Tetrahedron', 
                             'tet10', 'solid', 4, 6, 10, True, False, False, True)
    
def test_line_element_descriptor(line_element_descriptor):
    check_element_attributes(line_element_descriptor, 18, 'Linear 2-nodes Line', 
                             'line2', 'beam', 2, 0, 2, False, False, True, False)
    
def test_no_element_descriptor():
    # descriptor = dpf.element_types.descriptor(89)
    # assert not descriptor
    descriptor = dpf.element_types.descriptor(dpf.element_types.General)
    print(descriptor)
    unknown_shape = "unknown_shape"
    assert descriptor.shape == unknown_shape
    assert dpf.element_types.descriptor(dpf.element_types.General).shape == unknown_shape

def test_descriptor_with_int_value(allkindofcomplexity):
    # int as attribute instead of element_types.VALUE
    descriptor = dpf.element_types.descriptor(1)
    check_element_attributes(descriptor, 1, 'Quadratic 20-nodes Hexa', 
                             'hex20', 'solid', 8, 12, 20, True, False, False, True)
    
    