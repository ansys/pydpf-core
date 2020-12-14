"""Aeneid specific functions and classes"""

def start_server_using_service_manager():  # pragma: no cover
    if dpf.core.module_exists("grpc_interceptor_headers"):
        import grpc_interceptor_headers
        from  grpc_interceptor_headers.header_manipulator_client_interceptor import header_adder_interceptor    
    else:
        raise ValueError('Module grpc_interceptor_headers is missing to use service manager, please install it using pip install grpc_interceptor_headers')

    service_manager_url = f"http://{LOCALHOST}:8089/v1"

    definition = requests.get(url=service_manager_url + "/definitions/dpf").json()
    rsp = requests.post(url=service_manager_url + "/jobs", json=definition)
    job = rsp.json()

    dpf_task = job['taskGroups'][0]['tasks'][0]
    dpf_service = dpf_task['services'][0]
    dpf_service_name = dpf_service['name']
    dpf_url = f"{dpf_service['host']}:{dpf_service['port']}"

    channel = channel = grpc.insecure_channel(dpf_url)
    header_adder =  header_adder_interceptor('service-name', dpf_service_name)
    intercept_channel = grpc.intercept_channel(channel, header_adder)
    dpf.core.CHANNEL = intercept_channel

    dpf.core._server_instances.append(DpfJob(service_manager_url, dpf_service_name))


class DpfJob:  # pragma: no cover
    def __init__(self, service_manager_url, job_name):
        self.sm_url = service_manager_url
        self.job_name = job_name

    def shutdown(self):
        requests.delete(url=f'{self.sm_url}/jobs/{self.job_name}')

    def __del__(self):
        try:
            self.shutdown()
        except:
            pass
