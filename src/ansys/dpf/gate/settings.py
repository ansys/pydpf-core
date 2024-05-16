
def forward_settings(default_file_chunk_size, common_progress_bar):
    from ansys.dpf.gate import misc
    misc.DEFAULT_FILE_CHUNK_SIZE = default_file_chunk_size
    misc.COMMON_PROGRESS_BAR = common_progress_bar