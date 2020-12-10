import pytest

from ansys.dpf import core

ansys_path = core.misc.find_ansys()
if ansys_path is not None:
    try:
        invalid_version = int(ansys_path[-3:]) < 211
    except:
        invalid_version = True


@pytest.mark.skipif(ansys_path is None or invalid_version,
                    reason='Requires local install of ANSYS v211')
def test_start_local():
    starting_channel = id(core.CHANNEL)
    n_init = len(core._server_instances)
    core.start_local_server(as_global=False)
    assert len(core._server_instances) == n_init + 1
    core._server_instances[-1].shutdown()

    # ensure global channel didn't change
    assert starting_channel == id(core.CHANNEL)


def test_start_local_failed():
    with pytest.raises(NotADirectoryError):
        core.start_local_server(ansys_path='')
