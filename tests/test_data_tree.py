from ansys.dpf import core as dpf
import os
import pytest
import conftest


@conftest.raises_for_servers_version_under("4.0")
def test_create_data_tree(server_type):
    data_tree = dpf.DataTree(server=server_type)
    assert data_tree._internal_obj
    assert not data_tree.has("int")


@conftest.raises_for_servers_version_under("4.0")
def test_add_single_data_data_tree(server_type):
    data_tree = dpf.DataTree(server=server_type)
    data_tree.add(int=1)
    data_tree.add(double=1.0)
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


@conftest.raises_for_servers_version_under("4.0")
def test_add_multiple_data_data_tree(server_type):
    data_tree = dpf.DataTree(server=server_type)
    data_tree.add(
        int=1,
        double=1.0,
        string="hello",
        list_int=[1, 2],
        list_double=[1.5, 2.5],
        list_string=["hello", "bye"],
    )
    assert data_tree.has("int")
    assert data_tree.has("double")
    assert data_tree.has("string")
    assert data_tree.has("list_int")
    assert data_tree.has("list_double")
    assert data_tree.has("list_string")


@conftest.raises_for_servers_version_under("4.0")
def test_add_dict_data_tree(server_type):
    data_tree = dpf.DataTree(server=server_type)
    data_tree.add(
        {
            "int": 1,
            "double": 1.0,
            "string": "hello",
            "list_int": [1, 2],
            "list_double": [1.5, 2.5],
            "list_string": [1.5, 2.5],
        }
    )
    assert data_tree.has("int")
    assert data_tree.has("double")
    assert data_tree.has("string")
    assert data_tree.has("list_int")
    assert data_tree.has("list_double")
    assert data_tree.has("list_string")


@conftest.raises_for_servers_version_under("4.0")
def test_add_data_to_fill_data_tree():
    data_tree = dpf.DataTree()
    with data_tree.to_fill() as to_fill:
        data_tree.int = 1
        data_tree.double = 1.0
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


@conftest.raises_for_servers_version_under("4.0")
def test_get_as_data_tree(server_type):
    data_tree = dpf.DataTree(server=server_type)
    with data_tree.to_fill() as to_fill:
        to_fill.int = 1
        to_fill.double = 1.0
        to_fill.string = "hello"
        to_fill.list_int = [1, 2]
        to_fill.list_double = [1.5, 2.5]
        to_fill.list_string = ["hello", "bye"]
    assert data_tree.get_as("int") == "1"
    assert float(data_tree.get_as("double")) == 1.0
    assert data_tree.get_as("string") == "hello"
    assert data_tree.get_as("list_int") == "1;2"
    assert float(data_tree.get_as("list_double").split(";")[0]) == 1.5
    assert float(data_tree.get_as("list_double").split(";")[1]) == 2.50000
    assert data_tree.get_as("list_string") == "hello;bye"
    assert data_tree.get_as("int", dpf.types.int) == 1
    assert data_tree.get_as("double", dpf.types.double) == 1.0
    assert data_tree.get_as("string", dpf.types.string) == "hello"
    assert data_tree.get_as("list_int", dpf.types.vec_int) == [1, 2]
    assert data_tree.get_as("list_double", dpf.types.vec_double) == [1.5, 2.5]
    assert data_tree.get_as("list_string", dpf.types.vec_string) == ["hello", "bye"]


@conftest.raises_for_servers_version_under("4.0")
def test_write_data_tree():
    data_tree = dpf.DataTree()
    data_tree.int = 1
    data_tree.double = 1.0
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
    assert "1.5" in txt
    assert "2.5" in txt
    txt = data_tree.write_to_json()
    assert "int" in txt
    assert "double" in txt
    assert "string" in txt
    assert "list_int" in txt
    assert "list_double" in txt
    assert "list_string" in txt
    assert "hello;bye" in txt
    assert "1.5" in txt
    assert "2.5" in txt


@conftest.raises_for_servers_version_under("4.0")
def test_write_to_file_data_tree(tmpdir, server_type):
    data_tree = dpf.DataTree(server=server_type)
    with data_tree.to_fill() as to_fill:
        to_fill.int = 1
        to_fill.double = 1.0
        to_fill.string = "hello"
        to_fill.list_int = [1, 2]
        to_fill.list_double = [1.5, 2.5]
        to_fill.list_string = ["hello", "bye"]
    data_tree.write_to_txt(os.path.join(tmpdir, "file.txt"))
    data_tree = dpf.DataTree.read_from_txt(os.path.join(tmpdir, "file.txt"), server=server_type)
    assert data_tree.has("int")
    assert data_tree.has("double")
    assert data_tree.has("string")
    assert data_tree.has("list_int")
    assert data_tree.has("list_double")
    assert data_tree.has("list_string")
    data_tree.write_to_json(os.path.join(tmpdir, "file.json"))
    data_tree = dpf.DataTree.read_from_json(os.path.join(tmpdir, "file.json"), server=server_type)
    assert data_tree.has("int")
    assert data_tree.has("double")
    assert data_tree.has("string")
    assert data_tree.has("list_int")
    assert data_tree.has("list_double")
    assert data_tree.has("list_string")


@conftest.raises_for_servers_version_under("4.0")
def test_write_to_file_remote_data_tree(tmpdir, server_clayer_remote_process):
    server_connected = dpf.connect_to_server(
        server_clayer_remote_process.external_ip,
        server_clayer_remote_process.external_port,
        as_global=False,
    )
    data_tree = dpf.DataTree(server=server_connected)
    with data_tree.to_fill() as to_fill:
        to_fill.int = 1
        to_fill.double = 1.0
        to_fill.string = "hello"
        to_fill.list_int = [1, 2]
        to_fill.list_double = [1.5, 2.5]
        to_fill.list_string = ["hello", "bye"]
    data_tree.write_to_txt(os.path.join(tmpdir, "file.txt"))
    data_tree = dpf.DataTree.read_from_txt(
        os.path.join(tmpdir, "file.txt"), server=server_connected
    )
    assert data_tree.has("int")
    assert data_tree.has("double")
    assert data_tree.has("string")
    assert data_tree.has("list_int")
    assert data_tree.has("list_double")
    assert data_tree.has("list_string")
    data_tree.write_to_json(os.path.join(tmpdir, "file.json"))
    data_tree = dpf.DataTree.read_from_json(
        os.path.join(tmpdir, "file.json"), server=server_connected
    )
    assert data_tree.has("int")
    assert data_tree.has("double")
    assert data_tree.has("string")
    assert data_tree.has("list_int")
    assert data_tree.has("list_double")
    assert data_tree.has("list_string")


@conftest.raises_for_servers_version_under("4.0")
def test_read_from_txt_data_tree(server_type):
    data_tree = dpf.DataTree(server=server_type)
    with data_tree.to_fill() as to_fill:
        to_fill.int = 1
        to_fill.double = 1.0
        to_fill.string = "hello"
        to_fill.list_int = [1, 2]
        to_fill.list_double = [1.5, 2.5]
        to_fill.add(list_string=["hello", "bye"])
    txt = data_tree.write_to_txt()
    data_tree = dpf.DataTree.read_from_txt(txt=txt, server=server_type)
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


@conftest.raises_for_servers_version_under("4.0")
def test_print_data_tree(server_type):
    data_tree = dpf.DataTree(server=server_type)
    with data_tree.to_fill() as to_fill:
        to_fill.int = 1
        to_fill.double = 1.0
        to_fill.string = "hello"
        to_fill.list_int = [1, 2]
        to_fill.list_double = [1.5, 2.5]
        to_fill.add(list_string=["hello", "bye"])
    assert str(data_tree) != ""


@conftest.raises_for_servers_version_under("4.0")
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


@conftest.raises_for_servers_version_under("4.0")
def test_runtime_client_config(server_type_remote_process):
    client_config = dpf.settings.get_runtime_client_config(server=server_type_remote_process)
    use_cache_init = client_config.cache_enabled
    client_config.cache_enabled = False
    use_cache_set = client_config.cache_enabled
    assert use_cache_set is False
    client_config.cache_enabled = True
    use_cache_end = client_config.cache_enabled
    assert use_cache_end is True
    client_config.cache_enabled = use_cache_init
    use_cache_set_end = client_config.cache_enabled
    assert use_cache_set_end is use_cache_init

    streaming_buffer_size_init = client_config.streaming_buffer_size
    client_config.streaming_buffer_size = 100000
    streaming_buffer_size = client_config.streaming_buffer_size
    assert streaming_buffer_size == 100000
    client_config.streaming_buffer_size = streaming_buffer_size_init
    assert client_config.streaming_buffer_size == streaming_buffer_size_init

    stream_floats_instead_of_doubles_init = client_config.stream_floats_instead_of_doubles
    client_config.stream_floats_instead_of_doubles = True
    stream_floats_instead_of_doubles = client_config.stream_floats_instead_of_doubles
    assert stream_floats_instead_of_doubles == True
    client_config.stream_floats_instead_of_doubles = stream_floats_instead_of_doubles_init
    assert client_config.stream_floats_instead_of_doubles == stream_floats_instead_of_doubles_init


@conftest.raises_for_servers_version_under("4.0")
def test_runtime_client_config_arrays(server_type):
    client_config = dpf.settings.get_runtime_client_config(server=server_type)
    return_arrays_init = client_config.return_arrays
    client_config.return_arrays = False
    return_arrays = client_config.return_arrays
    assert return_arrays is False
    client_config.return_arrays = True
    return_arrays = client_config.return_arrays
    assert return_arrays is True
    client_config.return_arrays = return_arrays_init
    return_arrays = client_config.return_arrays
    assert return_arrays is return_arrays_init


@conftest.raises_for_servers_version_under("4.0")
def test_runtime_core_config(server_type):
    core_config = dpf.settings.get_runtime_core_config(server=server_type)
    num_threads_init = core_config.num_threads
    core_config.num_threads = 4
    num_threads = core_config.num_threads
    assert num_threads == 4
    core_config.num_threads = num_threads_init
    assert core_config.num_threads == num_threads_init
    timeout_init = core_config.license_timeout_in_seconds
    core_config.license_timeout_in_seconds = 4.0
    license_timeout_in_seconds = core_config.license_timeout_in_seconds
    assert license_timeout_in_seconds == 4.0
    core_config.license_timeout_in_seconds = timeout_init
    assert core_config.license_timeout_in_seconds == timeout_init


@conftest.raises_for_servers_version_under("4.0")
def test_unsupported_types_data_tree(server_type):
    data_tree = dpf.DataTree(server=server_type)
    with pytest.raises(TypeError):
        data_tree.add(data1=[[1]])
    with pytest.raises(TypeError):
        data_tree.add(data1=(1, 2))


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0, reason="Available for servers >=7.0"
)
def test_list_attributes_data_tree(server_type):
    data_tree = dpf.DataTree(server=server_type)
    with data_tree.to_fill() as to_fill:
        to_fill.int = 1
        to_fill.double = 1.0
        to_fill.string = "hello"
        to_fill.list_int = [1, 2]
        to_fill.list_double = [1.5, 2.5]
        to_fill.add(list_string=["hello", "bye"])

    attributes = data_tree.get_attribute_names

    assert ["double", "int", "list_double", "list_int", "list_string", "string"] == attributes


@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_7_0, reason="Available for servers >=7.0"
)
def test_list_attributes_recursive_data_tree(server_type):
    data_tree = dpf.DataTree(server=server_type)
    with data_tree.to_fill() as to_fill:
        to_fill.attribute01 = 1
        sub_tree01 = dpf.DataTree(server=server_type)
        with sub_tree01.to_fill() as to_fill01:
            to_fill01.attribute02 = 2
        to_fill.sub_tree01 = sub_tree01
        sub_tree02 = dpf.DataTree(server=server_type)
        to_fill.sub_tree02 = sub_tree02

    attributes = data_tree.get_attribute_names
    sub_trees = data_tree.get_sub_tree_names

    assert attributes == ["attribute01"]
    assert sub_trees == ["sub_tree01", "sub_tree02"]

    dic = data_tree.to_dict()

    assert ["attribute01", "sub_tree01", "sub_tree02"] == list(dic.keys())
    assert {"attribute02": "2"} == dic["sub_tree01"]
    assert {} == dic["sub_tree02"]
