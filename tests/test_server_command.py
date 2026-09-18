"""Test local server command construction without initializing a DPF server."""

from pathlib import Path

from ansys.dpf.core.server_context import ServerContext
from ansys.dpf.core.server_factory import GrpcMode
from ansys.dpf.core.server_types import _build_launch_server_command


def _build_windows_command(**kwargs):
    return _build_launch_server_command(
        "Ans.Dpf.Grpc.bat",
        "127.0.0.1",
        50054,
        platform_name="nt",
        **kwargs,
    )


def test_windows_quotes_custom_context_path_with_spaces():
    command = _build_windows_command(
        context=ServerContext(
            2, r"C:\Program Files\ANSYS Inc\v271\dpf\utilities\DpfCoreStandalone.xml"
        )
    )

    assert (
        r'--context "C:\Program Files\ANSYS Inc\v271\dpf\utilities\DpfCoreStandalone.xml"'
        in command
    )


def test_windows_keeps_context_path_without_spaces_unquoted():
    command = _build_windows_command(context=ServerContext(2, r"C:\DPF\DpfCoreStandalone.xml"))

    assert r"--context C:\DPF\DpfCoreStandalone.xml" in command


def test_posix_keeps_custom_context_path_as_one_argument():
    xml_path = "/opt/ansys inc/custom context.xml"
    command = _build_launch_server_command(
        "./Ans.Dpf.Grpc.sh",
        "127.0.0.1",
        50054,
        context=ServerContext(2, xml_path),
        platform_name="posix",
    )

    assert command[command.index("--context") + 1] == xml_path


def test_uses_numeric_value_for_non_custom_context():
    command = _build_windows_command(context=ServerContext(3, "ignored.xml"))

    assert "--context 3" in command


def test_omits_context_for_default_context():
    command = _build_windows_command()

    assert "--context" not in command


def test_formats_address_and_port_as_separate_arguments_on_posix():
    command = _build_launch_server_command(
        "./Ans.Dpf.Grpc.sh", "127.0.0.1", 50054, platform_name="posix"
    )

    assert command[1:5] == ["--address", "127.0.0.1", "--port", "50054"]


def test_formats_insecure_mode():
    command = _build_windows_command(grpc_mode=GrpcMode.Insecure)

    assert command.endswith("--mode 0")


def test_formats_mtls_mode():
    command = _build_windows_command(grpc_mode=GrpcMode.mTLS)

    assert command.endswith("--mode 3")


def test_windows_quotes_certificates_directory_with_spaces():
    command = _build_windows_command(
        grpc_mode=GrpcMode.mTLS,
        certificates_dir=Path("client certificates"),
    )

    assert command.endswith('--mode 3 --certs-dir "client certificates"')