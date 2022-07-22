
class DataSourcesOrStreamsConnector:
    def __init__(self, data_sources, stream_provider, mesh_provider=None):
        self._data_sources = data_sources
        self._stream_provider = stream_provider
        self._mesh_provider = mesh_provider

    def __connect_op__(self, op, mesh_by_default=True):
        """Connect the data sources or the streams to the operator."""
        if self._stream_provider is not None and hasattr(op.inputs, "streams"):
            op.inputs.streams.connect(self._stream_provider.outputs)
        elif self._stream_provider is not None and hasattr(op.inputs, "streams_container"):
            op.inputs.streams_container.connect(self._stream_provider.outputs)
        elif self._data_sources is not None and hasattr(
                op.inputs, "data_sources"
        ):
            op.inputs.data_sources.connect(self._data_sources)

        if mesh_by_default and self._mesh_provider and hasattr(op.inputs, "mesh"):
            op.inputs.mesh.connect(self._mesh_provider)
