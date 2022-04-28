from ansys.dpf import core as dpf
import os
import pytest
from ansys.dpf.core.check_version import meets_version, get_server_version

SERVER_VERSION_HIGHER_THAN_4_0 = meets_version(get_server_version(dpf._global_server()), "4.0")


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_4_0,
                    reason='Requires server version higher than 4.0')
def test_create_data_tree():
    data_tree = dpf.DataTree()
    assert data_tree._message.id != 0
    assert not data_tree.has("int")


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_4_0,
                    reason='Requires server version higher than 4.0')
def test_add_single_data_data_tree():
    data_tree = dpf.DataTree()
    data_tree.add(int=1)
    data_tree.add(double=1.)
    data_tree.add(string="hello")
    data_tree.add(list_int=[1, 2])
    data_tree.add(list_double=[1.5, 2.5])
    data_tree.add(list_string=["hello", "bye"])
    assert data_tree.has("int")
    assert data_tree.has("double")
    assert data_tree.has("string")
    assert data_tree.has("list_int")
    assert data_tree.has("list_double")
    assert data_tree.has("list_string")


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_4_0,
                    reason='Requires server version higher than 4.0')
def test_add_multiple_data_data_tree():
    data_tree = dpf.DataTree()
    data_tree.add(int=1, double=1., string="hello", list_int=[1, 2], list_double=[1.5, 2.5], list_string=["hello", "bye"])
    assert data_tree.has("int")
    assert data_tree.has("double")
    assert data_tree.has("string")
    assert data_tree.has("list_int")
    assert data_tree.has("list_double")
    assert data_tree.has("list_string")


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_4_0,
                    reason='Requires server version higher than 4.0')
def test_add_dict_data_tree():
    data_tree = dpf.DataTree()
    data_tree.add({"int": 1, "double": 1., "string": "hello", "list_int": [1, 2],
                   "list_double": [1.5, 2.5], "list_string": [1.5, 2.5]})
    assert data_tree.has("int")
    assert data_tree.has("double")
    assert data_tree.has("string")
    assert data_tree.has("list_int")
    assert data_tree.has("list_double")
    assert data_tree.has("list_string")


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_4_0,
                    reason='Requires server version higher than 4.0')
def test_add_data_to_fill_data_tree():
    data_tree = dpf.DataTree()
    with data_tree.to_fill() as to_fill:
        data_tree.int = 1
        data_tree.double = 1.
        data_tree.string = "hello"
        data_tree.list_int = [1, 2]
        data_tree.list_double = [1.5, 2.5]
        data_tree.list_string = ["hello", "bye"]
    assert data_tree.has("int")
    assert data_tree.has("double")
    assert data_tree.has("string")
    assert data_tree.has("list_int")
    assert data_tree.has("list_double")
    assert data_tree.has("list_string")


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_4_0,
                    reason='Requires server version higher than 4.0')
def test_get_as_data_tree():
    data_tree = dpf.DataTree()
    with data_tree.to_fill() as to_fill:
        data_tree.int = 1
        data_tree.double = 1.
        data_tree.string = "hello"
        data_tree.list_int = [1, 2]
        data_tree.list_double = [1.5, 2.5]
        data_tree.list_string = ["hello", "bye"]
    assert data_tree.get_as("int") == "1"
    assert data_tree.get_as("double") == "1.000000"
    assert data_tree.get_as("string") == "hello"
    assert data_tree.get_as("list_int") == "1;2"
    assert data_tree.get_as("list_double") == "1.500000;2.500000"
    assert data_tree.get_as("list_string") == "hello;bye"
    assert data_tree.get_as("int", dpf.types.int) == 1
    assert data_tree.get_as("double", dpf.types.double) == 1.
    assert data_tree.get_as("string", dpf.types.string) == "hello"
    assert data_tree.get_as("list_int", dpf.types.vec_int) == [1, 2]
    assert data_tree.get_as("list_double", dpf.types.vec_double) == [1.5, 2.5]
    assert data_tree.get_as("list_string", dpf.types.vec_string) == ["hello", "bye"]


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_4_0,
                    reason='Requires server version higher than 4.0')
def test_write_data_tree():
    data_tree = dpf.DataTree()
    data_tree.int = 1
    data_tree.double = 1.
    data_tree.string = "hello"
    data_tree.list_int = [1, 2]
    data_tree.list_double = [1.5, 2.5]
    data_tree.list_string = ["hello", "bye"]
    txt = data_tree.write_to_txt()
    assert "int" in txt
    assert "double" in txt
    assert "string" in txt
    assert "list_int" in txt
    assert "list_double" in txt
    assert "list_string" in txt
    assert "hello;bye" in txt
    assert "1.500000;2.500000" in txt
    txt = data_tree.write_to_json()
    assert "int" in txt
    assert "double" in txt
    assert "string" in txt
    assert "list_int" in txt
    assert "list_double" in txt
    assert "list_string" in txt
    assert "hello;bye" in txt
    assert "1.500000;2.500000" in txt


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_4_0,
                    reason='Requires server version higher than 4.0')
def test_write_to_file_data_tree(tmpdir):
    data_tree = dpf.DataTree()
    with data_tree.to_fill() as to_fill:
        to_fill.int = 1
        to_fill.double = 1.
        to_fill.string = "hello"
        to_fill.list_int = [1, 2]
        to_fill.list_double = [1.5, 2.5]
        to_fill.list_string = ["hello", "bye"]
    data_tree.write_to_txt(os.path.join(tmpdir, "file.txt"))
    data_tree = dpf.DataTree.read_from_txt(os.path.join(tmpdir, "file.txt"))
    assert data_tree.has("int")
    assert data_tree.has("double")
    assert data_tree.has("string")
    assert data_tree.has("list_int")
    assert data_tree.has("list_double")
    assert data_tree.has("list_string")
    data_tree.write_to_json(os.path.join(tmpdir, "file.json"))
    data_tree = dpf.DataTree.read_from_json(os.path.join(tmpdir, "file.json"))
    assert data_tree.has("int")
    assert data_tree.has("double")
    assert data_tree.has("string")
    assert data_tree.has("list_int")
    assert data_tree.has("list_double")
    assert data_tree.has("list_string")


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_4_0,
                    reason='Requires server version higher than 4.0')
def test_read_from_txt_data_tree():
    data_tree = dpf.DataTree()
    with data_tree.to_fill() as to_fill:
        to_fill.int = 1
        to_fill.double = 1.
        to_fill.string = "hello"
        to_fill.list_int = [1, 2]
        to_fill.list_double = [1.5, 2.5]
        to_fill.add(list_string = ["hello", "bye"])
    txt = data_tree.write_to_txt()
    data_tree = dpf.DataTree.read_from_txt(txt=txt)
    assert data_tree.has("int")
    assert data_tree.has("double")
    assert data_tree.has("string")
    assert data_tree.has("list_int")
    assert data_tree.has("list_double")
    assert data_tree.has("list_string")
    txt = data_tree.write_to_json()
    data_tree = dpf.DataTree.read_from_json(txt=txt)
    assert data_tree.has("int")
    assert data_tree.has("double")
    assert data_tree.has("string")
    assert data_tree.has("list_int")
    assert data_tree.has("list_double")
    assert data_tree.has("list_string")


@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_4_0,
                    reason='Requires server version higher than 4.0')
def test_sub_data_tree():
    data_tree = dpf.DataTree()
    data_tree2 = dpf.DataTree()
    with data_tree2.to_fill() as to_fill:
        to_fill.int = 1
    with data_tree.to_fill() as to_fill:
        to_fill.sub = data_tree2
    data_tree.sub2 = data_tree2
    assert data_tree.get_as("sub", dpf.types.data_tree).has("int")
    assert data_tree.get_as("sub2", dpf.types.data_tree).has("int")

@pytest.mark.skipif(not SERVER_VERSION_HIGHER_THAN_4_0,
                    reason='Requires server version higher than 4.0')
def test_runtime_client_config(server_clayer_remote_process):
    client_config = dpf.get_runtime_client_config(server=server_clayer_remote_process)
    use_cache_init = client_config.cache_enabled
    assert use_cache_init is True
    client_config.cache_enabled = False
    use_cache_set = client_config.cache_enabled
    assert use_cache_set is False
    client_config.cache_enabled = True
    use_cache_end = client_config.cache_enabled
    assert use_cache_end is True
