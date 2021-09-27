from ansys.dpf.core.server import DpfServer
from ansys.dpf import core
from ansys.dpf.core import LOCALHOST
import weakref

"""Aeneid-specific functions and classes."""


def start_server_using_service_manager():  # pragma: no cover
    if core.module_exists("grpc_interceptor_headers"):
        import grpc_interceptor_headers  # noqa: F401
        from grpc_interceptor_headers.header_manipulator_client_interceptor import (
            header_adder_interceptor,
        )
    else:
        raise ValueError(
            "Module grpc_interceptor_headers is missing. To use Service "
            "Manager, install it using pip install grpc_interceptor_headers."
        )

    service_manager_url = f"http://{LOCALHOST}:8089/v1"

    definition = requests.get(url=service_manager_url + "/definitions/dpf").json()
    rsp = requests.post(url=service_manager_url + "/jobs", json=definition)
    job = rsp.json()

    dpf_task = job["taskGroups"][0]["tasks"][0]
    dpf_service = dpf_task["services"][0]
    dpf_service_name = dpf_service["name"]
    dpf_url = f"{dpf_service['host']}:{dpf_service['port']}"

    channel = grpc.insecure_channel(dpf_url)
    header_adder = header_adder_interceptor("service-name", dpf_service_name)
    intercept_channel = grpc.intercept_channel(channel, header_adder)
    core.SERVER = DpfJob(service_manager_url, dpf_service_name, intercept_channel)

    core._server_instances.append(weakref.ref(core.SERVER))


class DpfJob(DpfServer):
    def __init__(self, service_manager_url, job_name, channel):
        self.sm_url = service_manager_url
        self.job_name = job_name
        super().channel = channel

    def shutdown(self):
        requests.delete(url=f"{self.sm_url}/jobs/{self.job_name}")

    def __del__(self):
        try:
            self.shutdown()
        except:
            pass
