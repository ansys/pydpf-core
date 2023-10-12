"""Version for ansys-dpf-core"""
# major, minor, patch
version_info = 0, 9, 1, "dev0"

# Nice string for the version
__version__ = ".".join(map(str, version_info))
min_server_version = "4.0"

server_to_ansys_grpc_dpf_version = {
    "1.0": "==0.2.2",
    "2.0": "==0.3.0",
    "3.0": ">=0.4.0",
    "4.0": ">=0.5.0",
    "5.0": ">=0.6.0",
    "6.0": ">=0.7.0",
    "7.0": ">=0.8dev",
}


class ServerToAnsysVersion:
    legacy_version_map = {
        "1.0": "2021R1",
        "2.0": "2021R2",
        "3.0": "2022R1",
        "4.0": "2022R2",
        "5.0": "2023R1",
        "6.0": "2023R2",
        "6.1": "2023R2",
        "6.2": "2023R2",
        "7.0": "2024R1",
        "7.1": "2024R1",
    }

    def __getitem__(self, item):
        if len(item) == 3:
            return self.legacy_version_map[item]
        else:
            split = item.split('.')
            return split[0]+'R'+split[1]


server_to_ansys_version = ServerToAnsysVersion()
