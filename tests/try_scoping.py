from ansys.dpf import core
from ansys.dpf.core.server import ServerConfig
from ansys.dpf.core.server import set_server_configuration, _global_server, shutdown_all_session_servers

server_configs = [None,
                  ServerConfig(),
                  ServerConfig(c_server=True),
                  ServerConfig(c_server=False,remote_protocol=None),
                  ServerConfig(c_server=True, remote_protocol=None),
                  ]


for config in server_configs:
    print(config)
    set_server_configuration(config)
    scoping = core.Scoping()
    ids = [1,2,3]
    scoping.ids = ids
    scoping.location = "elemental"
    scoping.set_id(0,4)
    print(scoping.id(0))
    print(scoping.index(1))
    print(scoping[0])
    print(scoping.location)
    print(scoping.size)
    del scoping

    shutdown_all_session_servers()

