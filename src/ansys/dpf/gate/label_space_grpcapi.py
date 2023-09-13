from ansys.dpf.gate.generated import label_space_abstract_api

#-------------------------------------------------------------------------------
# LabelSpace
#-------------------------------------------------------------------------------

class LabelSpaceGRPCAPI(label_space_abstract_api.LabelSpaceAbstractAPI):

    @staticmethod
    def init_label_space_environment(object):
        object._deleter_func = (lambda obj:None, lambda obj: obj._internal_obj)

    @staticmethod
    def label_space_new_for_object(object):
        from ansys.grpc.dpf import collection_pb2
        if hasattr(collection_pb2, "LabelSpace"):
            return collection_pb2.LabelSpace()
        from ansys.grpc.dpf import label_space_pb2
        return label_space_pb2.LabelSpace()

    @staticmethod
    def label_space_add_data(space, label, id):
        space._internal_obj.label_space[label] = id

    @staticmethod
    def label_space_get_size(space):
        return len(space._internal_obj.label_space)

    @staticmethod
    def label_space_get_labels_name(space, index):
        for i, tuple in enumerate(space._internal_obj.label_space):
            if i == index:
                return tuple

    @staticmethod
    def label_space_get_labels_value(space, index):
        for i, tuple in enumerate(space._internal_obj.label_space.items()):
            if i == index:
                return tuple[1]

    @staticmethod
    def list_label_spaces_size(list):
        return len(list._internal_obj)

    @staticmethod
    def list_label_spaces_at(list, index):
        return list._internal_obj[index]
