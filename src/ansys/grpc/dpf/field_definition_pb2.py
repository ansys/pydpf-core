# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: field_definition.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ansys.grpc.dpf.base_pb2 as base__pb2
import ansys.grpc.dpf.available_result_pb2 as available__result__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x66ield_definition.proto\x12!ansys.api.dpf.field_definition.v0\x1a\nbase.proto\x1a\x16\x61vailable_result.proto\"F\n\x0f\x46ieldDefinition\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.ansys.api.dpf.base.v0.EntityIdentifier\"\xb9\x01\n\tDimension\x12\x0c\n\x04mass\x18\x01 \x01(\x01\x12\x0e\n\x06length\x18\x02 \x01(\x01\x12\x0c\n\x04time\x18\x03 \x01(\x01\x12\x17\n\x0f\x65lectric_charge\x18\x04 \x01(\x01\x12\x13\n\x0btemperature\x18\x05 \x01(\x01\x12\r\n\x05\x61ngle\x18\x06 \x01(\x01\x12\x43\n\x0bhomogeneity\x18\x07 \x01(\x0e\x32..ansys.api.dpf.available_result.v0.Homogeneity\"M\n\x0e\x44imensionality\x12-\n\x06nature\x18\x01 \x01(\x0e\x32\x1d.ansys.api.dpf.base.v0.Nature\x12\x0c\n\x04size\x18\x02 \x03(\x05\"#\n\x11UnitParseBySymbol\x12\x0e\n\x06symbol\x18\x01 \x01(\t\"p\n\x04Unit\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x39\n\x03\x64im\x18\x02 \x01(\x0b\x32,.ansys.api.dpf.field_definition.v0.Dimension\x12\x0e\n\x06\x66\x61\x63tor\x18\x03 \x01(\x01\x12\r\n\x05shift\x18\x04 \x01(\x01\"+\n\x11ListQuantityTypes\x12\x16\n\x0equantity_types\x18\x01 \x03(\t\"\x8e\x03\n\x13\x46ieldDefinitionData\x12\x35\n\x04unit\x18\x01 \x01(\x0b\x32\'.ansys.api.dpf.field_definition.v0.Unit\x12\x31\n\x08location\x18\x02 \x01(\x0b\x32\x1f.ansys.api.dpf.base.v0.Location\x12J\n\x0f\x64imensionnality\x18\x03 \x01(\x0b\x32\x31.ansys.api.dpf.field_definition.v0.Dimensionality\x12\x44\n\x0cshell_layers\x18\x05 \x01(\x0e\x32..ansys.api.dpf.field_definition.v0.ShellLayers\x12L\n\x0equantity_types\x18\x06 \x01(\x0b\x32\x34.ansys.api.dpf.field_definition.v0.ListQuantityTypes\x12-\n\x04name\x18\x07 \x01(\x0b\x32\x1f.ansys.api.dpf.base.v0.PBString\"\xcc\x04\n\x1c\x46ieldDefinitionUpdateRequest\x12L\n\x10\x66ield_definition\x18\x01 \x01(\x0b\x32\x32.ansys.api.dpf.field_definition.v0.FieldDefinition\x12\x37\n\x04unit\x18\x02 \x01(\x0b\x32\'.ansys.api.dpf.field_definition.v0.UnitH\x00\x12K\n\x0bunit_symbol\x18\x03 \x01(\x0b\x32\x34.ansys.api.dpf.field_definition.v0.UnitParseBySymbolH\x00\x12\x31\n\x08location\x18\x04 \x01(\x0b\x32\x1f.ansys.api.dpf.base.v0.Location\x12J\n\x0f\x64imensionnality\x18\x05 \x01(\x0b\x32\x31.ansys.api.dpf.field_definition.v0.Dimensionality\x12\x44\n\x0cshell_layers\x18\x06 \x01(\x0e\x32..ansys.api.dpf.field_definition.v0.ShellLayers\x12L\n\x0equantity_types\x18\x07 \x01(\x0b\x32\x34.ansys.api.dpf.field_definition.v0.ListQuantityTypes\x12-\n\x04name\x18\x08 \x01(\x0b\x32\x1f.ansys.api.dpf.base.v0.PBStringB\x16\n\x14unit_definition_type*}\n\x0bShellLayers\x12\n\n\x06NOTSET\x10\x00\x12\x07\n\x03TOP\x10\x01\x12\n\n\x06\x42OTTOM\x10\x02\x12\r\n\tTOPBOTTOM\x10\x03\x12\x07\n\x03MID\x10\x04\x12\x10\n\x0cTOPBOTTOMMID\x10\x05\x12\r\n\tNONELAYER\x10\x06\x12\x14\n\x10LAYERINDEPENDENT\x10\x07\x32\xad\x03\n\x16\x46ieldDefinitionService\x12Z\n\x06\x43reate\x12\x1c.ansys.api.dpf.base.v0.Empty\x1a\x32.ansys.api.dpf.field_definition.v0.FieldDefinition\x12g\n\x06Update\x12?.ansys.api.dpf.field_definition.v0.FieldDefinitionUpdateRequest\x1a\x1c.ansys.api.dpf.base.v0.Empty\x12r\n\x04List\x12\x32.ansys.api.dpf.field_definition.v0.FieldDefinition\x1a\x36.ansys.api.dpf.field_definition.v0.FieldDefinitionData\x12Z\n\x06\x44\x65lete\x12\x32.ansys.api.dpf.field_definition.v0.FieldDefinition\x1a\x1c.ansys.api.dpf.base.v0.EmptyB#\xaa\x02 Ansys.Api.Dpf.FieldDefinition.V0b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'field_definition_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002 Ansys.Api.Dpf.FieldDefinition.V0'
  _SHELLLAYERS._serialized_start=1624
  _SHELLLAYERS._serialized_end=1749
  _FIELDDEFINITION._serialized_start=97
  _FIELDDEFINITION._serialized_end=167
  _DIMENSION._serialized_start=170
  _DIMENSION._serialized_end=355
  _DIMENSIONALITY._serialized_start=357
  _DIMENSIONALITY._serialized_end=434
  _UNITPARSEBYSYMBOL._serialized_start=436
  _UNITPARSEBYSYMBOL._serialized_end=471
  _UNIT._serialized_start=473
  _UNIT._serialized_end=585
  _LISTQUANTITYTYPES._serialized_start=587
  _LISTQUANTITYTYPES._serialized_end=630
  _FIELDDEFINITIONDATA._serialized_start=633
  _FIELDDEFINITIONDATA._serialized_end=1031
  _FIELDDEFINITIONUPDATEREQUEST._serialized_start=1034
  _FIELDDEFINITIONUPDATEREQUEST._serialized_end=1622
  _FIELDDEFINITIONSERVICE._serialized_start=1752
  _FIELDDEFINITIONSERVICE._serialized_end=2181
# @@protoc_insertion_point(module_scope)