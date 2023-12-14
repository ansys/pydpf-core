DEFAULT_FILE_CHUNK_SIZE = None
COMMON_PROGRESS_BAR = None
class LocalClientConfig(dict):
    """Behaves as a RuntimeClientConfig"""
    __delattr__ = dict.__delitem__
    __len__ = dict.__len__

    def copy_config(self, config):
        config._data_tree.add(**self)

    def __getattr__(self, key):
        if key == "stream_floats_instead_of_doubles":
            return self["stream_floats"]
        return self.__getitem__(key)

    def __setattr__(self, key, value):
        if key == "stream_floats_instead_of_doubles":
            self["stream_floats"] = value
        return self.__setitem__(key, value)


_CLIENT_CONFIG = LocalClientConfig()

def client_config():
    if len(_CLIENT_CONFIG) == 0:
        _CLIENT_CONFIG.use_cache = False
        _CLIENT_CONFIG.streaming_buffer_size = DEFAULT_FILE_CHUNK_SIZE
        _CLIENT_CONFIG.stream_floats_instead_of_doubles = False
        _CLIENT_CONFIG.return_arrays = True
    return _CLIENT_CONFIG
