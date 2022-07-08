
def __connect_op__(op, metadata, mesh_by_default=True):
    """Connect the data sources or the streams to the operator."""
    if metadata._stream_provider is not None and hasattr(op.inputs, "streams"):
        op.inputs.streams.connect(metadata._stream_provider.outputs)
    elif metadata._stream_provider is not None and hasattr(op.inputs, "streams_container"):
        op.inputs.streams_container.connect(metadata._stream_provider.outputs)
    elif metadata._data_sources is not None and hasattr(
            op.inputs, "data_sources"
    ):
        op.inputs.data_sources.connect(metadata._data_sources)

    if mesh_by_default and metadata.mesh_provider and hasattr(op.inputs, "mesh"):
        op.inputs.mesh.connect(metadata.mesh_provider)
