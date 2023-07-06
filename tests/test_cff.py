import pytest
import conftest
import platform
from ansys.dpf import core as dpf
from ansys.dpf.core import examples


def fluent_multi_species_on_server(server):
    ds = dpf.DataSources(server=server)
    files = examples.download_fluent_multi_species(server=server)
    ds.set_result_file_path(files["cas"], "cas")
    ds.add_file_path(files["dat"], "dat")
    return ds

@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0 or platform.system() == "Linux",
    reason="CFF source operators where not supported before 7.0,",
)
def test_cff_model_in_process(server_in_process, fluent_multi_species):
    ds = fluent_multi_species_on_server(server_in_process)
    model = dpf.Model(ds, server=server_in_process)
    print(model)
    assert model is not None


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0,
    reason="CFF source operators where not supported before 7.0,",
)
def test_cff_model_grpc_servers(server_type_remote_process, fluent_multi_species):
    ds = fluent_multi_species_on_server(server_type_remote_process)
    model = dpf.Model(ds, server=server_type_remote_process)
    print(model)
    assert model is not None
