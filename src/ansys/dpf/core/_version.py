"""Version for ansys-dpf-core"""
# Minimal DPF server version supported
min_server_version = "4.0"


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
        "8.0": "2024R2",
        "8.1": "2024R2",
        "8.2": "2024R2",
        "9.0": "2025R1",
    }

    def __getitem__(self, item):
        if len(item) == 3:
            return self.legacy_version_map[item]
        else:
            split = item.split(".")
            return split[0] + "R" + split[1]


server_to_ansys_version = ServerToAnsysVersion()
