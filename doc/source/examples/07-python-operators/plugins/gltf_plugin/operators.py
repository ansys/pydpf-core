from gltf_plugin import gltf_export
from ansys.dpf.core.custom_operator import CustomOperatorBase
from ansys.dpf.core.operator_specification import CustomSpecification, PinSpecification, \
    SpecificationProperties
from ansys.dpf import core as dpf


class WriteGLTF(CustomOperatorBase):
    def run(self):
        path = self.get_input(0, str)
        mesh = self.get_input(1, dpf.MeshedRegion)
        field = self.get_input(2, dpf.Field)

        mesh_element_types = mesh.elements.element_types_field.data_as_list
        if mesh_element_types.count(dpf.element_types.Tri3.value) != len(mesh_element_types) \
                or not mesh_element_types:
            raise Exception("Elements of mesh are not triangles.")

        norm_op = dpf.operators.math.norm()
        norm_op.inputs.field.connect(field)

        min_max_op = dpf.operators.min_max.min_max()
        min_max_op.inputs.field.connect(norm_op.outputs.field())
        field_max = min_max_op.outputs.field_max().data[0]
        field_min = min_max_op.outputs.field_min().data[0]
        field_range = field_max - field_min

        uv = []
        for value in norm_op.outputs.field().data:
            uv.append([value / field_range, 0])

        path = gltf_export.export(
            path,
            mesh.nodes.coordinates_field.data,
            mesh.elements.connectivities_field.data_as_list,
            uv
        )

        self.set_output(0, path)
        self.set_succeeded()

    @property
    def specification(self):
        spec = CustomSpecification("Writes a GLTF file for a surface MeshedRegion with triangles "
                                   "elements and a Field using pygltflib python module.")
        spec.inputs = {
            0: PinSpecification("path", type_names=str, document="path to write GLTF file"),
            1: PinSpecification("mesh", type_names=dpf.MeshedRegion),
            2: PinSpecification("field", type_names=dpf.Field,
                                document="3D vector Field to export (ie displacement Field)."),
        }
        spec.outputs = {
            0: PinSpecification("path", type_names=str),
        }
        spec.properties = SpecificationProperties(user_name="GLTF export", category="serialization")
        return spec

    @property
    def name(self):
        return "gltf_export"
