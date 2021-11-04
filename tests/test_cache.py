from ansys.dpf import core as dpf

def test_unit_mesh_cache(simple_bar):
    model = dpf.Model(simple_bar)
    mesh = model.metadata.meshed_region
    initunit = mesh.unit
    assert len(mesh._cache.cached) == 1
    assert mesh.unit == initunit
    mesh.unit = "cm"
    assert len(mesh._cache.cached) == 0
    assert mesh.unit == "cm"
    assert len(mesh._cache.cached) == 1


def test_named_selections_mesh_cache(simple_bar):
    model = dpf.Model(simple_bar)
    mesh = model.metadata.meshed_region
    init = mesh.available_named_selections
    assert len(mesh._cache.cached) == 1
    assert mesh.available_named_selections == init
    assert len(mesh._cache.cached) == 1
    ns = mesh.named_selection(init[0])
    assert len(mesh._cache.cached) == 2


def test_mismatch_instances_cache(simple_bar):
    model = dpf.Model(simple_bar)
    model2 = dpf.Model(simple_bar)
    mesh = model.metadata.meshed_region
    mesh2 = model2.metadata.meshed_region
    initunit = mesh.unit
    assert len(mesh._cache.cached) == 1
    assert len(mesh2._cache.cached) == 0
    assert mesh.unit == initunit
    mesh.unit = "cm"
    assert len(mesh._cache.cached) == 0
    mesh2.unit
    assert len(mesh2._cache.cached) == 1


def test_available_results_cache(simple_bar):
    model = dpf.Model(simple_bar)
    res_info = model.metadata.result_info
    for res in res_info:
        pass
    assert len(res_info._cache.cached) == len(res_info) + len(dpf.ResultInfo._to_cache)-1

def test_physics_type_cache(simple_bar):
    ds = dpf.DataSources(simple_bar)
    provider = dpf.operators.metadata.result_info_provider(data_sources=ds)
    res_info = provider.outputs.result_info()
    assert len(res_info._cache.cached) == 0
    res_info.unit_system
    assert len(res_info._cache.cached) == 1
    res_info.physics_type
    assert len(res_info._cache.cached) == 1