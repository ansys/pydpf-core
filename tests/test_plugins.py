# Copyright (C) 2020 - 2026 Synopsys, Inc. and ANSYS, Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from pathlib import Path
import sys

import pytest

from ansys.dpf import core as dpf
from ansys.dpf.core import errors, examples, plugins
import conftest


@pytest.fixture()
def try_load_lsdyna_operators():
    try:
        dpf.load_library("Ans.Dpf.LSDYNA.dll", "lsdyna")
        return True
    except:
        pytest.skip("Couldn't load lsdyna operators")
        return False


def test_lsdyna(d3plot_files, try_load_lsdyna_operators):
    dpf.load_library("Ans.Dpf.LSDYNA.dll", "lsdyna")
    ds = dpf.DataSources()
    ds.set_result_file_path(d3plot_files[0], "d3plot")
    streams = dpf.operators.metadata.streams_provider(ds)
    u = dpf.operators.result.displacement()
    u.inputs.streams_container(streams)
    fc = u.outputs.fields_container()
    assert len(fc[0]) == 3195


@pytest.fixture()
def try_load_composites_operators():
    try:
        dpf.load_library("composite_operators.dll", "compo")
        dpf.load_library("Ans.Dpf.EngineeringData.dll", "eng")
        return True
    except:
        pytest.skip("Couldn't load composites operators")
        return False


def test_eng(engineering_data_sources, try_load_composites_operators):
    dpf.load_library("composite_operators.dll", "compo")
    dpf.load_library("Ans.Dpf.EngineeringData.dll", "eng")
    m = dpf.Model(engineering_data_sources)
    stress_op = dpf.operators.result.stress()
    stress_op.inputs.data_sources.connect(engineering_data_sources)
    result_info_provider = dpf.operators.metadata.result_info_provider()
    result_info_provider.inputs.data_sources.connect(engineering_data_sources)
    mat_support_operator = dpf.operators.metadata.material_support_provider()
    mat_support_operator.inputs.data_sources.connect(engineering_data_sources)
    ans_mat_operator = dpf.Operator("eng_data::ans_mat_material_provider")
    ans_mat_operator.connect(0, mat_support_operator, 0)
    ans_mat_operator.connect(1, result_info_provider, 0)
    ans_mat_operator.connect(4, engineering_data_sources)
    field_variable_provider = dpf.Operator("composite::inistate_field_variables_provider")
    field_variable_provider.connect(4, engineering_data_sources)
    field_variable_provider.inputs.mesh.connect(m.metadata.mesh_provider)
    field_variable_provider.run()


def test_lsdynahgp(d3plot_files, server_type):
    ds = dpf.DataSources(server=server_type)
    ds.set_result_file_path(d3plot_files[0], "d3plot")
    streams = dpf.operators.metadata.streams_provider(ds, server=server_type)
    u = dpf.operators.result.displacement(server=server_type)
    u.inputs.streams_container(streams)
    fc = u.outputs.fields_container()
    assert len(fc[0]) == 3195
    assert dpf.Operator("lsdyna::stream_provider") is not None


def test_cgns(server_type):
    assert dpf.Operator("cgns::stream_provider", server=server_type) is not None


def test_vtk(server_type, tmpdir):
    op = dpf.Operator("vtu_export", server=server_type)
    try:
        rst_file = dpf.upload_file_in_tmp_folder(
            examples.download_pontoon(return_local_path=True), server=server_type
        )
    except dpf.errors.ServerTypeError as e:
        print(e)
        rst_file = examples.download_pontoon(return_local_path=True)
        pass

    assert op is not None
    model = dpf.Model(rst_file, server=server_type)
    u = model.operator("U")
    op.inputs.fields1.connect(u)
    op.inputs.mesh.connect(model.metadata.mesh_provider)
    op.inputs.directory.connect(str(Path(rst_file).parent))
    out_path = op.eval()
    # assert out_path.result_files is not []
    # try:
    #     out_path = dpf.core.download_file(
    #         out_path, tmp_path, server=server_type)
    # except dpf.errors.ServerTypeError as e:
    #     print(e)
    #     pass
    # assert os.path.exists(tmp_path)


@pytest.mark.xfail(raises=errors.DpfVersionNotSupported)
@pytest.mark.skipif(
    not conftest.SERVERS_VERSION_GREATER_THAN_OR_EQUAL_TO_10_0,
    reason="Use of custom XML broken before 252",
)
@pytest.mark.skipif(
    conftest.running_docker,
    reason="server start using custom XML not working on Docker",
)
def test_load_library_default_name(remote_config_server_type, testfiles_dir):
    # Test only for remote server configs as InProcess already ran and loaded plugins at this point
    server_context = dpf.AvailableServerContexts.no_context
    server_context.xml_path = Path(testfiles_dir) / "DpfCustomDefinedTest.xml"
    server = dpf.start_local_server(
        config=remote_config_server_type, context=server_context, as_global=False
    )
    assert len(server.plugins) == 2  # Only grpc and native are loaded
    assert "grpc" in server.plugins.keys()
    assert "native" in server.plugins.keys()
    if sys.platform.startswith("linux"):
        lib_name = "libmeshOperatorsCore.so"
    else:
        lib_name = "meshOperatorsCore.dll"
    dpf.load_library(filename=lib_name, server=server)
    assert len(server.plugins) == 3
    assert lib_name.split(".")[0] in server.plugins.keys()


@pytest.mark.parametrize("load_api", ["load_library", "load_plugin_on_server"])
@pytest.mark.parametrize(
    "failure_name, source, expected_phase, exception_type, cause_type",
    [
        (
            "import",
            "raise ImportError('plugin import failed') from ModuleNotFoundError('missing_plugin_dependency')\n",
            "module_import",
            "ImportError",
            "ModuleNotFoundError",
        ),
        (
            "entry",
            "def load_operators(*args):\n    raise ValueError('entry-point failure') from RuntimeError('original cause')\n",
            "entry_point",
            "ValueError",
            "RuntimeError",
        ),
        ("missing", "value = 42\n", "entry_point", "AttributeError", ""),
        ("noncallable", "load_operators = 42\n", "entry_point", "TypeError", ""),
        (
            "registration",
            "from ansys.dpf.core.custom_operator import record_operator\n"
            "class InvalidOperator:\n"
            "    def __init__(self):\n"
            "        raise ValueError('invalid operator registration') from RuntimeError('registration cause')\n"
            "def load_operators(*args):\n"
            "    record_operator(InvalidOperator, *args)\n",
            "operator_registration",
            "ValueError",
            "RuntimeError",
        ),
    ],
    ids=["import", "entry", "missing-entry", "noncallable-entry", "registration"],
)
def test_structured_python_plugin_load_errors(
    server_type_remote_process,
    tmp_path,
    monkeypatch,
    load_api,
    failure_name,
    source,
    expected_phase,
    exception_type,
    cause_type,
):
    server = server_type_remote_process
    if not server.meet_version("2027.2.pre0"):
        pytest.skip("Structured Python-plugin load errors require server 2027.2 or later.")

    plugin_name = f"structured_{failure_name}_{load_api}"
    plugin_path = tmp_path / plugin_name
    plugin_path.mkdir()
    (plugin_path / "__init__.py").write_text(source, encoding="utf-8")

    if load_api == "load_plugin_on_server":
        initializer = plugins.importlib_metadata.PackagePath(f"{plugin_name}/__init__.py")
        initializer.dist = plugins.importlib_metadata.PathDistribution(tmp_path / "plugin.dist-info")
        monkeypatch.setattr(plugins.importlib_metadata, "files", lambda package: [initializer])
    else:
        server_path = dpf.path_utilities.join(dpf.make_tmp_dir_server(server=server), plugin_name)
        dpf.upload_files_in_folder(server_path, plugin_path, specific_extension=".py", server=server)

    with pytest.raises(errors.DPFServerException) as exception_info:
        if load_api == "load_plugin_on_server":
            plugins.load_plugin_on_server(f"ansys-dpf-{plugin_name}", server=server)
        else:
            dpf.load_library(server_path, f"py_{plugin_name}", "load_operators", server=server)

    exception = exception_info.value
    assert exception.type == "python_exception"
    assert exception.fields["python_exception_type"] == exception_type
    assert exception.fields["python_cause_type"] == cause_type
    assert exception.fields["phase"] == expected_phase
    assert exception.fields["plugin_key"] == f"py_{plugin_name}"
    assert exception.fields["module_name"] == plugin_name
    assert exception.fields["plugin_path"].endswith(plugin_name)
    assert exception.fields["entry_point"] == "load_operators"
    assert exception.fields["python_traceback"]
    assert any(
        frame.get("type") == "plugin_load" and frame.get("plugin_key") == f"py_{plugin_name}"
        for frame in exception.frames
    )
    assert all("plugin_kind" not in frame for frame in exception.frames)
    assert "Unknown exception occurred" not in str(exception)


@pytest.mark.parametrize(
    "library_name, symbol, root_type, phase",
    [
        ("NativePluginLoadTestPlugin", "ThrowStandard", "cppexception", "registration"),
        ("NativePluginLoadTestPlugin", "ThrowStructured", "native_plugin_test_registration", "registration"),
        ("NativePluginLoadTestPlugin", "ThrowHgp", "native_plugin_test_hgp_registration", "registration"),
        ("NativePluginLoadTestPlugin", "ThrowNestedStandard", "cppexception", "registration"),
        ("NativePluginLoadTestPlugin", "ThrowNonStandard", "unknown", "registration"),
        ("NativePluginLoadTestPlugin", "ReturnFailure", "plugin_load", "registration"),
        ("NativePluginLoadTestPlugin", "MissingEntryPoint", "cppexception", "symbol_resolution"),
        ("NativePluginLoadTestWithDependency", "LoadOperators", "cppexception", "binary_load"),
        ("MissingNativePluginBinary", "LoadOperators", "cppexception", "binary_load"),
    ],
)
def test_structured_native_plugin_load_errors(server_type, library_name, symbol, root_type, phase):
    server = server_type
    if not server.meet_version("2027.2.pre0"):
        pytest.skip("Structured plugin-load errors require server 2027.2 or later.")
    if not server.local_server or not server.ansys_path:
        pytest.skip("Native plugin fixtures require a local test server installation.")
    runtime = Path(server.ansys_path)
    directory = runtime / "aisol" / ("dll/linx64" if sys.platform.startswith("linux") else "bin/winx64")
    prefix, suffix = ("lib", ".so") if sys.platform.startswith("linux") else ("", ".dll")
    if not (directory / f"{prefix}NativePluginLoadTestPlugin{suffix}").exists():
        pytest.skip("Native plugin-load test fixtures are not installed.")
    library = directory / f"{prefix}{library_name}{suffix}"
    plugin_key = f"shared_native_{library_name}_{symbol}"
    with pytest.raises(errors.DPFServerException) as exception_info:
        dpf.load_library(str(library), plugin_key, symbol, server=server)
    exception = exception_info.value
    assert exception.type == root_type
    assert exception.fields["plugin_key"] == plugin_key
    assert exception.fields["plugin_path"] == str(library)
    assert exception.fields["entry_point"] == symbol
    assert exception.fields["phase"] == phase
    assert any(frame.get("type") == "plugin_load" for frame in exception.frames)
    assert all("plugin_kind" not in frame for frame in exception.frames)
    if symbol == "ReturnFailure":
        assert exception.fields["return_code"] == "37"
    if symbol == "ThrowStructured":
        assert exception.fields["registration_name"] == "native_test_registration"
    if symbol == "ThrowHgp":
        assert exception.fields["registration_name"] == "hgp_native_test"
