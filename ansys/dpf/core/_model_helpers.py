import weakref


class DataSourcesOrStreamsConnector:
    def __init__(self, metadata):
        self._metadata = weakref.ref(metadata)

    @property
    def streams_provider(self):
        if self._metadata():
            return self._metadata().streams_provider
        return None

    @property
    def time_freq_support(self):
        if self._metadata():
            return self._metadata().time_freq_support
        return None

    @property
    def mesh_provider(self):
        if self._metadata():
            return self._metadata()._mesh_provider_cached
        return None

    @property
    def data_sources(self):
        if self._metadata():
            return self._metadata().data_sources
        return None

    def named_selection(self, name):
        if self._metadata():
            return self._metadata().named_selection(name)
        return None

    def __connect_op__(self, op, mesh_by_default=True):
        """Connect the data sources or the streams to the operator."""
        if self.streams_provider is not None and hasattr(op.inputs, "streams"):
            op.inputs.streams.connect(self.streams_provider.outputs)
        elif self.streams_provider is not None and hasattr(op.inputs, "streams_container"):
            op.inputs.streams_container.connect(self.streams_provider.outputs)
        elif self.data_sources is not None and hasattr(
                op.inputs, "data_sources"
        ):
            op.inputs.data_sources.connect(self.data_sources)

        if mesh_by_default and self.mesh_provider and hasattr(op.inputs, "mesh"):
            op.inputs.mesh.connect(self.mesh_provider)
