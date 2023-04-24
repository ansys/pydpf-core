
class ObjHandler:
    def __init__(self, data_processing_api, internal_obj=None, server=None):
        self._internal_obj = internal_obj
        self.data_processing_api = data_processing_api
        self._server = server
        self.owned = False

    def get_ownership(self):
        self.owned = True
        if hasattr(self._internal_obj, "id"):
            if isinstance(self._internal_obj.id, int) and self._internal_obj.id!=0:
                return self._internal_obj
            elif hasattr(self._internal_obj.id, "id") and self._internal_obj.id.id!=0:
                return self._internal_obj

    def __del__(self):
        try:
            if hasattr(self, "_internal_obj") and not self.owned:
                self.data_processing_api.data_processing_delete_shared_object(self)
        except Exception as e:
            pass
        #     print("Deletion failed:", e)

