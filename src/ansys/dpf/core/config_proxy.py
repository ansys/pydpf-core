from ansys.dpf.core.config import Config
class _ConfigProxy:
    """ Proxy config class that syncs Config modifications back to operator.
        Ensures that all Config writes happen on server.
        Reads are delegated to Config class objects
    """

    def __init__(self, operator):
        self._operator = operator
    def set_config_option(self, config_name, config_value):
        """Create a temp config, modify and write back to server"""
        cfg = self._get_temp_config()
        cfg.set_config_option(config_name, config_value)
        self._operator.config = cfg

    def _get_temp_config(self):
        """Get current config from server"""
        config = self._operator._api.operator_get_config(self._operator)
        return Config(config=config, server=self._operator._server, spec=self._operator._spec)

    def __getattr__(self, item):
        """Delegates all calls to Config class"""
        return getattr(self._get_temp_config(), item)