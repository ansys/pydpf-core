DEFAULT_FILE_CHUNK_SIZE = None
COMMON_PROGRESS_BAR = None
_CLIENT_CONFIG = {}


def client_config():
    if len(_CLIENT_CONFIG) == 0:
        _CLIENT_CONFIG["use_cache"] = False
        _CLIENT_CONFIG["streaming_buffer_size"] = DEFAULT_FILE_CHUNK_SIZE
        _CLIENT_CONFIG["stream_floats"] = False
    return _CLIENT_CONFIG
