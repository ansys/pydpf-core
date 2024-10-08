# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meshed_region.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ansys.grpc.dpf.base_pb2 as base__pb2
import ansys.grpc.dpf.scoping_pb2 as scoping__pb2
import ansys.grpc.dpf.field_pb2 as field__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13meshed_region.proto\x12\x1e\x61nsys.api.dpf.meshed_region.v0\x1a\nbase.proto\x1a\rscoping.proto\x1a\x0b\x66ield.proto\"J\n\rCreateRequest\x12\x1a\n\x12num_nodes_reserved\x18\x01 \x01(\x05\x12\x1d\n\x15num_elements_reserved\x18\x02 \x01(\x05\"C\n\x0cMeshedRegion\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.ansys.api.dpf.base.v0.EntityIdentifier\"\xaa\x01\n\x11GetScopingRequest\x12:\n\x04mesh\x18\x01 \x01(\x0b\x32,.ansys.api.dpf.meshed_region.v0.MeshedRegion\x12.\n\x03loc\x18\x02 \x01(\x0b\x32\x1f.ansys.api.dpf.base.v0.LocationH\x00\x12\x19\n\x0fnamed_selection\x18\x03 \x01(\tH\x00\x42\x0e\n\x0cscoping_type\"\xa3\x01\n\x18SetNamedSelectionRequest\x12:\n\x04mesh\x18\x01 \x01(\x0b\x32,.ansys.api.dpf.meshed_region.v0.MeshedRegion\x12\x17\n\x0fnamed_selection\x18\x02 \x01(\t\x12\x32\n\x07scoping\x18\x03 \x01(\x0b\x32!.ansys.api.dpf.scoping.v0.Scoping\"\xc0\x01\n\x0fSetFieldRequest\x12:\n\x04mesh\x18\x01 \x01(\x0b\x32,.ansys.api.dpf.meshed_region.v0.MeshedRegion\x12,\n\x05\x66ield\x18\x02 \x01(\x0b\x32\x1d.ansys.api.dpf.field.v0.Field\x12\x43\n\rproperty_type\x18\x03 \x01(\x0b\x32,.ansys.api.dpf.meshed_region.v0.PropertyType\"%\n\x0cPropertyName\x12\x15\n\rproperty_name\x18\x01 \x01(\t\"\xa0\x01\n\x0cPropertyType\x12\x43\n\rproperty_name\x18\x01 \x01(\x0b\x32,.ansys.api.dpf.meshed_region.v0.PropertyName\x12K\n\x11property_location\x18\x02 \x01(\x0e\x32\x30.ansys.api.dpf.meshed_region.v0.PropertyLocation\"\xc6\x01\n\x18\x45lementalPropertyRequest\x12:\n\x04mesh\x18\x01 \x01(\x0b\x32,.ansys.api.dpf.meshed_region.v0.MeshedRegion\x12\x43\n\rproperty_name\x18\x02 \x01(\x0b\x32,.ansys.api.dpf.meshed_region.v0.PropertyName\x12\x0f\n\x05index\x18\x03 \x01(\x05H\x00\x12\x0c\n\x02id\x18\x04 \x01(\x05H\x00\x42\n\n\x08index_id\"\x96\x01\n\x13ListPropertyRequest\x12:\n\x04mesh\x18\x01 \x01(\x0b\x32,.ansys.api.dpf.meshed_region.v0.MeshedRegion\x12\x43\n\rproperty_type\x18\x02 \x01(\x0b\x32,.ansys.api.dpf.meshed_region.v0.PropertyType\")\n\x19\x45lementalPropertyResponse\x12\x0c\n\x04prop\x18\x01 \x01(\x05\"6\n\x04Node\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05index\x18\x02 \x01(\x05\x12\x13\n\x0b\x63oordinates\x18\x03 \x03(\x01\"Y\n\x07\x45lement\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05index\x18\x02 \x01(\x05\x12\x33\n\x05nodes\x18\x03 \x03(\x0b\x32$.ansys.api.dpf.meshed_region.v0.Node\"s\n\nGetRequest\x12:\n\x04mesh\x18\x01 \x01(\x0b\x32,.ansys.api.dpf.meshed_region.v0.MeshedRegion\x12\x0f\n\x05index\x18\x03 \x01(\x05H\x00\x12\x0c\n\x02id\x18\x04 \x01(\x05H\x00\x42\n\n\x08index_id\"\xbd\x01\n\x0cListResponse\x12\x0c\n\x04unit\x18\x02 \x01(\t\x12\x16\n\x0e\x61vailable_prop\x18\x03 \x03(\t\x12\x11\n\tnum_nodes\x18\x04 \x01(\x05\x12\x13\n\x0bnum_element\x18\x05 \x01(\x05\x12L\n\x12\x65lement_shape_info\x18\x06 \x01(\x0b\x32\x30.ansys.api.dpf.meshed_region.v0.ElementShapeInfo\x12\x11\n\tnum_faces\x18\x07 \x01(\x05\"X\n\x1aListNamedSelectionsRequest\x12:\n\x04mesh\x18\x01 \x01(\x0b\x32,.ansys.api.dpf.meshed_region.v0.MeshedRegion\"7\n\x1bListNamedSelectionsResponse\x12\x18\n\x10named_selections\x18\x01 \x03(\t\"\xe0\x01\n\x10\x45lementShapeInfo\x12\x1a\n\x12has_shell_elements\x18\x01 \x01(\x08\x12\x19\n\x11has_beam_elements\x18\x02 \x01(\x08\x12\x1a\n\x12has_solid_elements\x18\x03 \x01(\x08\x12\x1a\n\x12has_point_elements\x18\x04 \x01(\x08\x12\x19\n\x11has_skin_elements\x18\x05 \x01(\x08\x12\x14\n\x0chas_polygons\x18\x06 \x01(\x08\x12\x17\n\x0fhas_polyhedrons\x18\x07 \x01(\x08\x12\x13\n\x0bhas_gaskets\x18\x08 \x01(\x08\"\xc6\x01\n\nAddRequest\x12:\n\x04mesh\x18\x01 \x01(\x0b\x32,.ansys.api.dpf.meshed_region.v0.MeshedRegion\x12:\n\x05nodes\x18\x02 \x03(\x0b\x32+.ansys.api.dpf.meshed_region.v0.NodeRequest\x12@\n\x08\x65lements\x18\x03 \x03(\x0b\x32..ansys.api.dpf.meshed_region.v0.ElementRequest\"o\n\x0e\x45lementRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12;\n\x05shape\x18\x02 \x01(\x0e\x32,.ansys.api.dpf.meshed_region.v0.ElementShape\x12\x14\n\x0c\x63onnectivity\x18\x03 \x03(\x05\".\n\x0bNodeRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x13\n\x0b\x63oordinates\x18\x04 \x03(\x01\"n\n\x19UpdateMeshedRegionRequest\x12\x43\n\rmeshed_region\x18\x01 \x01(\x0b\x32,.ansys.api.dpf.meshed_region.v0.MeshedRegion\x12\x0c\n\x04unit\x18\x02 \x01(\t*,\n\x10PropertyLocation\x12\t\n\x05NODAL\x10\x00\x12\r\n\tELEMENTAL\x10\x01*A\n\x0c\x45lementShape\x12\t\n\x05SHELL\x10\x00\x12\t\n\x05SOLID\x10\x01\x12\x08\n\x04\x42\x45\x41M\x10\x02\x12\x11\n\rUNKNOWN_SHAPE\x10\x03\x32\xe0\n\n\x13MeshedRegionService\x12\x65\n\x06\x43reate\x12-.ansys.api.dpf.meshed_region.v0.CreateRequest\x1a,.ansys.api.dpf.meshed_region.v0.MeshedRegion\x12O\n\x03\x41\x64\x64\x12*.ansys.api.dpf.meshed_region.v0.AddRequest\x1a\x1c.ansys.api.dpf.base.v0.Empty\x12\x62\n\nGetScoping\x12\x31.ansys.api.dpf.meshed_region.v0.GetScopingRequest\x1a!.ansys.api.dpf.scoping.v0.Scoping\x12k\n\x11SetNamedSelection\x12\x38.ansys.api.dpf.meshed_region.v0.SetNamedSelectionRequest\x1a\x1c.ansys.api.dpf.base.v0.Empty\x12Y\n\x08SetField\x12/.ansys.api.dpf.meshed_region.v0.SetFieldRequest\x1a\x1c.ansys.api.dpf.base.v0.Empty\x12\x8b\x01\n\x14GetElementalProperty\x12\x38.ansys.api.dpf.meshed_region.v0.ElementalPropertyRequest\x1a\x39.ansys.api.dpf.meshed_region.v0.ElementalPropertyResponse\x12h\n\rUpdateRequest\x12\x39.ansys.api.dpf.meshed_region.v0.UpdateMeshedRegionRequest\x1a\x1c.ansys.api.dpf.base.v0.Empty\x12\x62\n\x0cListProperty\x12\x33.ansys.api.dpf.meshed_region.v0.ListPropertyRequest\x1a\x1d.ansys.api.dpf.field.v0.Field\x12\x62\n\x04List\x12,.ansys.api.dpf.meshed_region.v0.MeshedRegion\x1a,.ansys.api.dpf.meshed_region.v0.ListResponse\x12\x8e\x01\n\x13ListNamedSelections\x12:.ansys.api.dpf.meshed_region.v0.ListNamedSelectionsRequest\x1a;.ansys.api.dpf.meshed_region.v0.ListNamedSelectionsResponse\x12[\n\x07GetNode\x12*.ansys.api.dpf.meshed_region.v0.GetRequest\x1a$.ansys.api.dpf.meshed_region.v0.Node\x12\x61\n\nGetElement\x12*.ansys.api.dpf.meshed_region.v0.GetRequest\x1a\'.ansys.api.dpf.meshed_region.v0.Element\x12T\n\x06\x44\x65lete\x12,.ansys.api.dpf.meshed_region.v0.MeshedRegion\x1a\x1c.ansys.api.dpf.base.v0.EmptyB \xaa\x02\x1d\x41nsys.Api.Dpf.MeshedRegion.v0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'meshed_region_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\035Ansys.Api.Dpf.MeshedRegion.v0'
  _globals['_PROPERTYLOCATION']._serialized_start=2677
  _globals['_PROPERTYLOCATION']._serialized_end=2721
  _globals['_ELEMENTSHAPE']._serialized_start=2723
  _globals['_ELEMENTSHAPE']._serialized_end=2788
  _globals['_CREATEREQUEST']._serialized_start=95
  _globals['_CREATEREQUEST']._serialized_end=169
  _globals['_MESHEDREGION']._serialized_start=171
  _globals['_MESHEDREGION']._serialized_end=238
  _globals['_GETSCOPINGREQUEST']._serialized_start=241
  _globals['_GETSCOPINGREQUEST']._serialized_end=411
  _globals['_SETNAMEDSELECTIONREQUEST']._serialized_start=414
  _globals['_SETNAMEDSELECTIONREQUEST']._serialized_end=577
  _globals['_SETFIELDREQUEST']._serialized_start=580
  _globals['_SETFIELDREQUEST']._serialized_end=772
  _globals['_PROPERTYNAME']._serialized_start=774
  _globals['_PROPERTYNAME']._serialized_end=811
  _globals['_PROPERTYTYPE']._serialized_start=814
  _globals['_PROPERTYTYPE']._serialized_end=974
  _globals['_ELEMENTALPROPERTYREQUEST']._serialized_start=977
  _globals['_ELEMENTALPROPERTYREQUEST']._serialized_end=1175
  _globals['_LISTPROPERTYREQUEST']._serialized_start=1178
  _globals['_LISTPROPERTYREQUEST']._serialized_end=1328
  _globals['_ELEMENTALPROPERTYRESPONSE']._serialized_start=1330
  _globals['_ELEMENTALPROPERTYRESPONSE']._serialized_end=1371
  _globals['_NODE']._serialized_start=1373
  _globals['_NODE']._serialized_end=1427
  _globals['_ELEMENT']._serialized_start=1429
  _globals['_ELEMENT']._serialized_end=1518
  _globals['_GETREQUEST']._serialized_start=1520
  _globals['_GETREQUEST']._serialized_end=1635
  _globals['_LISTRESPONSE']._serialized_start=1638
  _globals['_LISTRESPONSE']._serialized_end=1827
  _globals['_LISTNAMEDSELECTIONSREQUEST']._serialized_start=1829
  _globals['_LISTNAMEDSELECTIONSREQUEST']._serialized_end=1917
  _globals['_LISTNAMEDSELECTIONSRESPONSE']._serialized_start=1919
  _globals['_LISTNAMEDSELECTIONSRESPONSE']._serialized_end=1974
  _globals['_ELEMENTSHAPEINFO']._serialized_start=1977
  _globals['_ELEMENTSHAPEINFO']._serialized_end=2201
  _globals['_ADDREQUEST']._serialized_start=2204
  _globals['_ADDREQUEST']._serialized_end=2402
  _globals['_ELEMENTREQUEST']._serialized_start=2404
  _globals['_ELEMENTREQUEST']._serialized_end=2515
  _globals['_NODEREQUEST']._serialized_start=2517
  _globals['_NODEREQUEST']._serialized_end=2563
  _globals['_UPDATEMESHEDREGIONREQUEST']._serialized_start=2565
  _globals['_UPDATEMESHEDREGIONREQUEST']._serialized_end=2675
  _globals['_MESHEDREGIONSERVICE']._serialized_start=2791
  _globals['_MESHEDREGIONSERVICE']._serialized_end=4167
# @@protoc_insertion_point(module_scope)
