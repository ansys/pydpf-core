import os
import packaging.version
import pkg_resources
import importlib
from ansys.dpf.gate.generated import capi
from ansys.dpf.gate import utils, errors
from ansys.dpf.gate._version import __ansys_version__


def _find_outdated_ansys_version(arg: str):
    arg_to_compute = str(arg)
    ver_check = 221  # 221 or lower versions are not supported
    c = "v"
    char_pos = [pos for pos, char in enumerate(arg_to_compute) if char == c]
    # check if len after char is > 3
    for pos in char_pos:
        is_digit_after = False
        i = pos + 1
        n = i + 3
        if n < len(arg_to_compute):
            str_after = arg_to_compute[n]
            if str_after.isdigit():
                is_digit_after = True
        str_test = arg_to_compute[i:n]
        # check if 3 characters after char is int
        if len(str_test) >= 3:
            if str_test.isdigit():
                check = int(str_test)
                if check > int(__ansys_version__):
                    continue
                if check <= ver_check:
                    if not is_digit_after:
                        # ensure digit chain has size 3
                        return True
    return False


def _get_path_in_install(is_posix: bool = None, internal_folder="dll"):
    if not is_posix:
        is_posix = os.name == "posix"
    if not is_posix:
        path_in_install = os.path.join("aisol", "bin", "winx64")
    else:
        path_in_install = os.path.join("aisol", internal_folder, "linx64")
    return path_in_install


def _pythonize_awp_version(version):
    if len(version) != 3:
        return version
    return "20" + version[0:2] + "." + version[2]


def _find_latest_ansys_versions():
    awp_versions = [key[-3:] for key in os.environ.keys() if "AWP_ROOT" in key]
    installed_packages_list = {}

    for awp_version in awp_versions:
        if not awp_version.isnumeric():
            continue
        ansys_path = os.environ.get("AWP_ROOT" + awp_version)
        if ansys_path:
            installed_packages_list[
                packaging.version.parse(_pythonize_awp_version(awp_version))
            ] = ansys_path

    installed_packages = pkg_resources.working_set
    for i in installed_packages:
        if "ansys-dpf-server" in i.key:
            file_name = pkg_resources.to_filename(i.project_name.replace("ansys-dpf-", ""))
            try:
                module = importlib.import_module("ansys.dpf." + file_name)
                installed_packages_list[
                    packaging.version.parse(module.__version__)
                ] = module.__path__[0]
            except ModuleNotFoundError:
                pass
            except AttributeError:
                pass
    if len(installed_packages_list) > 0:
        return installed_packages_list[sorted(installed_packages_list)[-1]]


def _unified_installer_path_if_exists():
    return _find_latest_ansys_versions()


def _get_api_path_from_installer_or_package(ansys_path: str, is_posix: bool):
    is_ansys_version_old = _find_outdated_ansys_version(ansys_path)
    gatebin_found = _try_use_gatebin()
    dpf_client_found = False
    if gatebin_found and not is_ansys_version_old:
        # should work from the gatebin package
        from ansys.dpf import gatebin

        path = os.path.abspath(gatebin.__path__._path[0])
        dpf_client_found = True
    else:
        if ansys_path is not None:
            dpf_inner_path = _get_path_in_install(is_posix)
            path_gathered = path = os.path.join(ansys_path, dpf_inner_path)
            if os.path.isdir(path_gathered):
                path = path_gathered  # should work from the installer
            else:
                path = ansys_path
            if os.path.isdir(path):
                dpf_client_found = True
    if not dpf_client_found and not is_ansys_version_old:
        raise ModuleNotFoundError(
            "To use ansys-dpf-gate as a client API "
            "install ansys-dpf-gatebin "
            "with :\n pip install ansys-dpf-gatebin."
        )
    return path


def _try_use_gatebin():
    import shutil
    try:
        from ansys.dpf import gatebin
        if isinstance(gatebin.__path__, str):
            gatebin_path = gatebin.__path__
        elif gatebin.__path__ is None:
            return False
        else:
            gatebin_path = gatebin.__path__[0]
        for archive_format in shutil.get_unpack_formats():
            extensions = archive_format[1]
            if any([x in gatebin_path for x in extensions]):
                return False
        gatebin.__doc__
        return True
    except ModuleNotFoundError:
        return False
    except ImportError:
        return False
    except Exception as e:
        raise e
        return False


def _try_load_api(path, name):
    api_path = os.path.join(path, name)
    try:
        capi.load_api(api_path)
        return api_path
    except Exception as e:
        b_outdated_ansys_version_found = False
        b_module_not_found = False
        for arg in e.args:
            if hasattr(e, "winerror"):
                # if on Windows, we can check the error code
                # cases where the OSError is just saying "module not found"
                # without specifying the path
                if e.winerror == 126 and _find_outdated_ansys_version(path):
                    b_module_not_found = True
                    break
            if isinstance(arg, str):
                if (
                        len(arg) > 3
                ):  # at least 4 characters to have v*** defined, e.g. v221
                    if _find_outdated_ansys_version(arg):
                        b_outdated_ansys_version_found = True
        if b_outdated_ansys_version_found or b_module_not_found:
            raise errors.DpfVersionNotSupported("4.0")
        else:
            if not os.path.isdir(path):
                raise NotADirectoryError(
                    f'Unable to locate the directory containing DPF at '
                    f'"{path}"'
                )
            elif not os.path.isfile(api_path):
                raise FileNotFoundError(
                    f'DPF file not found at "{api_path}".  '
                    f'Unable to locate the following file: "{name}"'
                )
            else:
                raise e


def load_client_api(ansys_path=None):
    ISPOSIX = os.name == "posix"
    name = "DPFClientAPI.dll"
    if ISPOSIX:
        name = "libDPFClientAPI.so"

    ANSYS_PATH = ansys_path
    if ANSYS_PATH is None:
        ANSYS_PATH = _unified_installer_path_if_exists()
    path = _get_api_path_from_installer_or_package(ANSYS_PATH, ISPOSIX)

    return _try_load_api(path=path, name=name)


def load_grpc_client(ansys_path=None):
    path = ""
    ISPOSIX = os.name == "posix"
    name = "Ans.Dpf.GrpcClient"
    if ISPOSIX:
        name = "libAns.Dpf.GrpcClient"

    ANSYS_PATH = ansys_path
    if ANSYS_PATH is None:
        ANSYS_PATH = _unified_installer_path_if_exists()
    path = _get_api_path_from_installer_or_package(ANSYS_PATH, ISPOSIX)

    # PATH should be set only on Windows and only if working
    # from the installer because of runtime dependencies
    # on libcrypto and libssl
    previous_path = ""
    if not ISPOSIX and ANSYS_PATH is not None:
        previous_path = os.getenv("PATH", "")
        os.environ["PATH"] = path + ";" + previous_path

    grpc_client_api_path = os.path.join(path, name)
    try:
        utils.data_processing_core_load_api(grpc_client_api_path, "remote")
    except Exception as e:
        if not ISPOSIX:
            os.environ["PATH"] = previous_path
        raise e

    # reset of PATH
    if not ISPOSIX and ANSYS_PATH is not None:
        os.environ["PATH"] = previous_path

    return grpc_client_api_path
