"""
RuntimeConfig
=============
"""

from ansys.dpf.gate import (
    data_processing_capi,
    dpf_data_tree_capi,
    integral_types,
    object_handler
)


class _RuntimeConfig:
    """ Parent class for configuration options.
    """

    def __init__(self, data_tree):
        if data_tree is not None:
            if isinstance(data_tree, int):
                self._data_tree = object_handler.ObjHandler(
                    data_processing_api=data_processing_capi.DataProcessingCAPI,
                    internal_obj=data_tree
                    )
            else:
                raise TypeError("data_tree attribute expected type is pointer on DataTree")
        self._data_tree_api = dpf_data_tree_capi.DpfDataTreeCAPI
        self._data_tree_api.init_dpf_data_tree_environment(self)

class RuntimeClientConfig(_RuntimeConfig):
    """ Enables to access and set runtime configuration
    options to DataProcessingCore binary.

    Parameters
    ----------
    data_tree: int
        DataTree pointer describing the existing parameters configuration
        of DataprocessingCore.

    Notes
    -----
    Available from 4.0 server version. Can only be used for
    a gRPC communication protocol using DPF CLayer.

    Examples
    --------
    Get runtime configuration for DataProcessingCore.

    >>> pass
    """
    def __init__(self, data_tree):
        super().__init__(data_tree=data_tree)

    @property
    def cache_enabled(self):
        to_return = integral_types.MutableInt32()
        self._data_tree_api.dpf_data_tree_get_int_attribute(
            data_tree=self._data_tree,
            attribute_name="use_cache",
            value=to_return
            )
        return bool(int(to_return))

    @cache_enabled.setter
    def cache_enabled(self, value):
        self._data_tree_api.dpf_data_tree_set_int_attribute(
            data_tree=self._data_tree,
            attribute_name="use_cache",
            value=value
            )