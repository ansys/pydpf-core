import pytest
import conftest
import platform
from ansys.dpf import core as dpf


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0,
    reason="CFF source operators where not supported before 7.0,",
)
def test_cff_model_grpc_servers(server_type, fluent_multi_species):
    ds = fluent_multi_species(server_type)
    model = dpf.Model(ds, server=server_type)
    print(model)
    assert model is not None
    m = model.metadata.meshed_region
    print(m)
