"""Module to create gRPC channels with different transport modes.

This module provides functions to create gRPC channels based on the specified
transport mode, including insecure, Unix Domain Sockets (UDS), Windows Named User
Authentication (WNUA), and Mutual TLS (mTLS).

Example
-------
    channel = create_channel(
        host="localhost",
        port=50051,
        transport_mode="mtls",
        certs_dir="path/to/certs",
        grpc_options=[('grpc.max_receive_message_length', 50 * 1024 * 1024)],
    )
    stub = hello_pb2_grpc.GreeterStub(channel)

"""

# Only the create_channel function is exposed for external use
__all__ = ["create_channel", "verify_transport_mode", "verify_uds_socket"]

import logging
import os
from dataclasses import dataclass
from pathlib import Path
from typing import cast
from warnings import warn
from typing import TypeGuard

import grpc

_IS_WINDOWS = os.name == "nt"
LOOPBACK_HOSTS = ("localhost", "127.0.0.1")

logger = logging.getLogger(__name__)

@dataclass
class CertificateFiles:
    cert_file: str | Path | None = None
    key_file: str | Path | None = None
    ca_file: str | Path | None = None

def create_channel(
    transport_mode: str,
    host: str | None = None,
    port: int | str | None = None,
    uds_service: str | None = None,
    uds_dir: str | Path | None = None,
    uds_id: str | None = None,
    certs_dir: str | Path | None = None,
    cert_files: CertificateFiles | None = None,
    grpc_options: list[tuple[str, object]] | None = None,
) -> grpc.Channel:
    """Create a gRPC channel based on the transport mode.

    Parameters
    ----------
    transport_mode : str
        Transport mode selected by the user.
        Options are: "insecure", "uds", "wnua", "mtls"
    host : str | None
        Hostname or IP address of the server.
        By default `None` - however, if not using UDS transport mode,
        it will be requested.
    port : int | str | None
        Port in which the server is running.
        By default `None` - however, if not using UDS transport mode,
        it will be requested.
    uds_service : str | None
        Optional service name for the UDS socket.
        By default `None` - however, if UDS is selected, it will
        be requested.
    uds_dir : str | Path | None
        Directory to use for Unix Domain Sockets (UDS) transport mode.
        By default `None` and thus it will use the "~/.conn" folder.
    uds_id : str | None
        Optional ID to use for the UDS socket filename.
        By default `None` and thus it will use "<uds_service>.sock".
        Otherwise, the socket filename will be "<uds_service>-<uds_id>.sock".
    certs_dir : str | Path | None
        Directory to use for TLS certificates.
        By default `None` and thus search for the "ANSYS_GRPC_CERTIFICATES" environment variable.
        If not found, it will use the "certs" folder assuming it is in the current working
        directory.
    cert_files: CertificateFiles | None = None
        Path to the client certificate file, client key file, and issuing certificate authority.
        By default `None`.
        If all three file paths are not all provided, use the certs_dir parameter.
    grpc_options: list[tuple[str, object]] | None
        gRPC channel options to pass when creating the channel.
        Each option is a tuple of the form ("option_name", value).
        By default `None` and thus no extra options are added.

    Returns
    -------
    grpc.Channel
        The created gRPC channel

    """
    def check_host_port(transport_mode, host, port) -> tuple[str, str, str]:
        if host is None:
            raise ValueError(f"When using {transport_mode.lower()} transport mode, 'host' must be provided.")
        if port is None:
            raise ValueError(f"When using {transport_mode.lower()} transport mode, 'port' must be provided.")
        return transport_mode, host, port

    match transport_mode.lower():
        case "insecure":
            transport_mode, host, port = check_host_port(transport_mode, host, port)
            return create_insecure_channel(host, port, grpc_options)
        case "uds":
            return create_uds_channel(uds_service, uds_dir, uds_id, grpc_options)
        case "wnua":
            transport_mode, host, port = check_host_port(transport_mode, host, port)
            return create_wnua_channel(host, port, grpc_options)
        case "mtls":
            transport_mode, host, port = check_host_port(transport_mode, host, port)
            return create_mtls_channel(host, port, certs_dir, cert_files, grpc_options)
        case _:
            raise ValueError(
                f"Unknown transport mode: {transport_mode}. "
                "Valid options are: 'insecure', 'uds', 'wnua', 'mtls'."
            )


##################################### TRANSPORT MODE CHANNELS #####################################


def create_insecure_channel(
    host: str, port: int | str, grpc_options: list[tuple[str, object]] | None = None
) -> grpc.Channel:
    """Create an insecure gRPC channel without TLS.

    Parameters
    ----------
    host : str
        Hostname or IP address of the server.
    port : int | str
        Port in which the server is running.
    grpc_options: list[tuple[str, object]] | None
        gRPC channel options to pass when creating the channel.
        Each option is a tuple of the form ("option_name", value).
        By default `None` and thus no extra options are added.

    Returns
    -------
    grpc.Channel
        The created gRPC channel

    """
    target = f"{host}:{port}"
    warn(
        f"Starting gRPC client without TLS on {target}. This is INSECURE. "
        "Consider using a secure connection."
    )
    logger.info(f"Connecting using INSECURE -> {target}")
    return grpc.insecure_channel(target, options=grpc_options)


def create_uds_channel(
    uds_service: str | None,
    uds_dir: str | Path | None = None,
    uds_id: str | None = None,
    grpc_options: list[tuple[str, object]] | None = None,
) -> grpc.Channel:
    """Create a gRPC channel using Unix Domain Sockets (UDS).

    Parameters
    ----------
    uds_service : str
        Service name for the UDS socket.
    uds_dir : str | Path | None
        Directory to use for Unix Domain Sockets (UDS) transport mode.
        By default `None` and thus it will use the "~/.conn" folder.
    uds_id : str | None
        Optional ID to use for the UDS socket filename.
        By default `None` and thus it will use "<uds_service>.sock".
        Otherwise, the socket filename will be "<uds_service>-<uds_id>.sock".
    grpc_options: list[tuple[str, object]] | None
        gRPC channel options to pass when creating the channel.
        Each option is a tuple of the form ("option_name", value).
        By default `None` and thus only the default authority option is added.

    Returns
    -------
    grpc.Channel
        The created gRPC channel

    """
    if not is_uds_supported():
        raise RuntimeError(
            "Unix Domain Sockets are not supported on this platform or gRPC version."
        )

    if not uds_service:
        raise ValueError("When using UDS transport mode, 'uds_service' must be provided.")

    # Determine UDS folder
    uds_folder = determine_uds_folder(uds_dir)

    # Make sure the folder exists
    uds_folder.mkdir(parents=True, exist_ok=True)

    # Generate socket filename with optional ID
    socket_filename = f"{uds_service}-{uds_id}.sock" if uds_id else f"{uds_service}.sock"
    target = f"unix:{uds_folder / socket_filename}"
    # Set default authority to "localhost" for UDS connection
    # This is needed to avoid issues with some gRPC implementations,
    # see https://github.com/grpc/grpc/issues/34305
    options: list[tuple[str, object]] = [
        ("grpc.default_authority", "localhost"),
    ]
    if grpc_options:
        options.extend(grpc_options)
    logger.info(f"Connecting using UDS -> {target}")
    return grpc.insecure_channel(target, options=options)


def create_wnua_channel(
    host: str,
    port: int | str,
    grpc_options: list[tuple[str, object]] | None = None,
) -> grpc.Channel:
    """Create a gRPC channel using Windows Named User Authentication (WNUA).

    Parameters
    ----------
    host : str
        Hostname or IP address of the server.
    port : int | str
        Port in which the server is running.
    grpc_options: list[tuple[str, object]] | None
        gRPC channel options to pass when creating the channel.
        Each option is a tuple of the form ("option_name", value).
        By default `None` and thus only the default authority option is added.

    Returns
    -------
    grpc.Channel
        The created gRPC channel

    """
    if not _IS_WINDOWS:
        raise ValueError("Windows Named User Authentication (WNUA) is only supported on Windows.")
    if host not in LOOPBACK_HOSTS:
        raise ValueError("Remote host connections are not supported with WNUA.")

    target = f"{host}:{port}"
    # Set default authority to "localhost" for WNUA connection
    # This is needed to avoid issues with some gRPC implementations,
    # see https://github.com/grpc/grpc/issues/34305
    options: list[tuple[str, object]] = [
        ("grpc.default_authority", "localhost"),
    ]
    if grpc_options:
        options.extend(grpc_options)
    logger.info(f"Connecting using WNUA -> {target}")
    return grpc.insecure_channel(target, options=options)


def create_mtls_channel(
    host: str,
    port: int | str,
    certs_dir: str | Path | None = None,
    cert_files: CertificateFiles | None = None,
    grpc_options: list[tuple[str, object]] | None = None,
) -> grpc.Channel:
    """Create a gRPC channel using Mutual TLS (mTLS).

    Parameters
    ----------
    host : str
        Hostname or IP address of the server.
    port : int | str
        Port in which the server is running.
    certs_dir : str | Path | None
        Directory to use for TLS certificates.
        By default `None` and thus search for the "ANSYS_GRPC_CERTIFICATES" environment variable.
        If not found, it will use the "certs" folder assuming it is in the current working
        directory.
    cert_files: CertificateFiles | None
        Path to the client certificate file, client key file, and issuing certificate authority.
        By default `None`.
        If all three file paths are not all provided, use the certs_dir parameter.
    grpc_options: list[tuple[str, object]] | None
        gRPC channel options to pass when creating the channel.
        Each option is a tuple of the form ("option_name", value).
        By default `None` and thus no extra options are added.

    Returns
    -------
    grpc.Channel
        The created gRPC channel

    """
    certs_folder = None
    if cert_files is not None and cert_files.cert_file is not None and cert_files.key_file is not None and cert_files.ca_file is not None:
        cert_file = Path(cert_files.cert_file).resolve()
        key_file = Path(cert_files.key_file).resolve()
        ca_file = Path(cert_files.ca_file).resolve()
    else:
        # Determine certificates folder
        if certs_dir:
            certs_folder = Path(certs_dir)
        elif os.environ.get("ANSYS_GRPC_CERTIFICATES"):
            certs_folder = Path(cast(str, os.environ.get("ANSYS_GRPC_CERTIFICATES")))
        else:
            certs_folder = Path("certs")
        ca_file = certs_folder / "ca.crt"
        cert_file = certs_folder / "client.crt"
        key_file = certs_folder / "client.key"

    # Load certificates
    try:
        with (ca_file).open("rb") as f:
            trusted_certs = f.read()
        with (cert_file).open("rb") as f:
            client_cert = f.read()
        with (key_file).open("rb") as f:
            client_key = f.read()
    except FileNotFoundError as e:
        error_message = f"Certificate file not found: {e.filename}. "
        if certs_folder is not None:
            error_message += f"Ensure that the certificates are present in the '{certs_folder}' folder or " \
            "set the 'ANSYS_GRPC_CERTIFICATES' environment variable."
        raise FileNotFoundError(error_message) from e

    # Create SSL credentials
    credentials = grpc.ssl_channel_credentials(
        root_certificates=trusted_certs, private_key=client_key, certificate_chain=client_cert
    )

    target = f"{host}:{port}"
    logger.info(f"Connecting using mTLS -> {target}")
    return grpc.secure_channel(target, credentials, options=grpc_options)


######################################## HELPER FUNCTIONS ########################################


def version_tuple(version_str: str) -> tuple[int, ...]:
    """Convert a version string into a tuple of integers for comparison.

    Parameters
    ----------
    version_str : str
        The version string to convert.

    Returns
    -------
    tuple[int, ...]
        A tuple of integers representing the version.

    """
    return tuple(int(x) for x in version_str.split("."))


def check_grpc_version():
    """Check if the installed gRPC version meets the minimum requirement.

    Returns
    -------
    bool
        True if the gRPC version is sufficient, False otherwise.

    """
    min_version = "1.63.0"
    current_version = grpc.__version__

    try:
        return version_tuple(current_version) >= version_tuple(min_version)
    except ValueError:
        logger.warning("Unable to parse gRPC version.")
        return False


def is_uds_supported():
    """Check if Unix Domain Sockets (UDS) are supported on the current platform.

    Returns
    -------
    bool
        True if UDS is supported, False otherwise.

    """
    is_grpc_version_ok = check_grpc_version()
    return is_grpc_version_ok if _IS_WINDOWS else True


def determine_uds_folder(uds_dir: str | Path | None = None) -> Path:
    """Determine the directory to use for Unix Domain Sockets (UDS).

    Parameters
    ----------
    uds_dir : str | Path | None
        Directory to use for Unix Domain Sockets (UDS) transport mode.
        By default `None` and thus it will use the "~/.conn" folder.

    Returns
    -------
    Path
        The path to the UDS directory.

    """
    # If no directory is provided, use default based on OS
    if uds_dir:
        return uds_dir if isinstance(uds_dir, Path) else Path(uds_dir)
    else:
        if _IS_WINDOWS:
            return Path(os.environ["USERPROFILE"]) / ".conn"
        else:
            # Linux/POSIX
            return Path(os.environ["HOME"], ".conn")


def verify_transport_mode(transport_mode: str, mode: str | None = None) -> None:
    """Verify that the provided transport mode is valid.

    Parameters
    ----------
    transport_mode : str
        The transport mode to verify.
    mode : str | None
        Can be one of "all", "local" or "remote" to restrict the valid transport modes.
        By default `None` and thus all transport modes are accepted.

    Raises
    ------
    ValueError
        If the transport mode is not one of the accepted values.

    """
    if mode == "local":
        valid_modes = {"insecure", "uds", "wnua"}
    elif mode == "remote":
        valid_modes = {"insecure", "mtls"}
    elif mode == "all" or mode is None:
        valid_modes = {"insecure", "uds", "wnua", "mtls"}
    else:
        raise ValueError(f"Invalid mode: {mode}. Valid options are: 'all', 'local', 'remote'.")

    if transport_mode.lower() not in valid_modes:
        raise ValueError(
            f"Invalid transport mode: {transport_mode}. "
            f"Valid options are: {', '.join(valid_modes)}."
        )


def verify_uds_socket(
    uds_service: str, uds_dir: Path | None = None, uds_id: str | None = None
) -> bool:
    """Verify that the UDS socket file has been created.

    Parameters
    ----------
    uds_service : str
        Service name for the UDS socket.
    uds_dir : Path | None
        Directory where the UDS socket file is expected to be (optional).
        By default `None` and thus it will use the "~/.conn" folder.
    uds_id : str | None
        Unique identifier for the UDS socket (optional).
        By default `None` and thus it will use "<uds_service>.sock".
        Otherwise, the socket filename will be "<uds_service>-<uds_id>.sock".

    Returns
    -------
    bool
        True if the UDS socket file exists, False otherwise.
    """
    # Generate socket filename with optional ID
    uds_filename = f"{uds_service}-{uds_id}.sock" if uds_id else f"{uds_service}.sock"

    # Full path to the UDS socket file
    uds_socket_path = determine_uds_folder(uds_dir) / uds_filename

    # Check if the UDS socket file exists
    return uds_socket_path.exists()
