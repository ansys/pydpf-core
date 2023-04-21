import ctypes
from ansys.dpf.core.gate import utils
from ansys.dpf.core.gate import errors
from ansys.dpf.core.gate.generated import capi
from ansys.dpf.core.gate.generated import generic_data_container_abstract_api
from ansys.dpf.core.gate.generated.data_processing_capi import DataProcessingCAPI

# -------------------------------------------------------------------------------
# GenericDataContainer
# -------------------------------------------------------------------------------


class GenericDataContainerCAPI(generic_data_container_abstract_api.GenericDataContainerAbstractAPI):
    @staticmethod
    def init_generic_data_container_environment(object):
        # get core api
        DataProcessingCAPI.init_data_processing_environment(object)
        object._deleter_func = (
            DataProcessingCAPI.data_processing_delete_shared_object,
            lambda obj: obj,
        )

    @staticmethod
    def generic_data_container_new():
        errorSize = ctypes.c_int(0)
        sError = ctypes.c_wchar_p()
        res = capi.dll.GenericDataContainer_new(
            ctypes.byref(utils.to_int32(errorSize)), ctypes.byref(sError)
        )
        if errorSize.value != 0:
            raise errors.DPFServerException(sError.value)
        return res

    @staticmethod
    def generic_data_container_get_property_any(container, name):
        errorSize = ctypes.c_int(0)
        sError = ctypes.c_wchar_p()
        res = capi.dll.GenericDataContainer_getPropertyAny(
            container._internal_obj if container is not None else None,
            utils.to_char_ptr(name),
            ctypes.byref(utils.to_int32(errorSize)),
            ctypes.byref(sError),
        )
        if errorSize.value != 0:
            raise errors.DPFServerException(sError.value)
        return res

    @staticmethod
    def generic_data_container_set_property_any(container, name, any):
        errorSize = ctypes.c_int(0)
        sError = ctypes.c_wchar_p()
        res = capi.dll.GenericDataContainer_setPropertyAny(
            container._internal_obj if container is not None else None,
            utils.to_char_ptr(name),
            any._internal_obj if any is not None else None,
            ctypes.byref(utils.to_int32(errorSize)),
            ctypes.byref(sError),
        )
        if errorSize.value != 0:
            raise errors.DPFServerException(sError.value)
        return res
