# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: operator.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ansys.grpc.dpf.collection_pb2 as collection__pb2
import ansys.grpc.dpf.field_pb2 as field__pb2
import ansys.grpc.dpf.scoping_pb2 as scoping__pb2
import ansys.grpc.dpf.base_pb2 as base__pb2
import ansys.grpc.dpf.data_sources_pb2 as data__sources__pb2
import ansys.grpc.dpf.meshed_region_pb2 as meshed__region__pb2
import ansys.grpc.dpf.time_freq_support_pb2 as time__freq__support__pb2
import ansys.grpc.dpf.result_info_pb2 as result__info__pb2
import ansys.grpc.dpf.operator_config_pb2 as operator__config__pb2
import ansys.grpc.dpf.cyclic_support_pb2 as cyclic__support__pb2
import ansys.grpc.dpf.workflow_message_pb2 as workflow__message__pb2
import ansys.grpc.dpf.dpf_any_message_pb2 as dpf__any__message__pb2
import ansys.grpc.dpf.data_tree_pb2 as data__tree__pb2
import ansys.grpc.dpf.label_space_pb2 as label__space__pb2
import ansys.grpc.dpf.generic_data_container_pb2 as generic__data__container__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eoperator.proto\x12\x1d\x61nsys.api.dpf.dpf_operator.v0\x1a\x10\x63ollection.proto\x1a\x0b\x66ield.proto\x1a\rscoping.proto\x1a\nbase.proto\x1a\x12\x64\x61ta_sources.proto\x1a\x13meshed_region.proto\x1a\x17time_freq_support.proto\x1a\x11result_info.proto\x1a\x15operator_config.proto\x1a\x14\x63yclic_support.proto\x1a\x16workflow_message.proto\x1a\x15\x64pf_any_message.proto\x1a\x0f\x64\x61ta_tree.proto\x1a\x11label_space.proto\x1a\x1cgeneric_data_container.proto\"M\n\x08Operator\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.ansys.api.dpf.base.v0.EntityIdentifier\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x88\x05\n\rSpecification\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12]\n\x12map_input_pin_spec\x18\x02 \x03(\x0b\x32\x41.ansys.api.dpf.dpf_operator.v0.Specification.MapInputPinSpecEntry\x12_\n\x13map_output_pin_spec\x18\x03 \x03(\x0b\x32\x42.ansys.api.dpf.dpf_operator.v0.Specification.MapOutputPinSpecEntry\x12J\n\x0b\x63onfig_spec\x18\x04 \x01(\x0b\x32\x35.ansys.api.dpf.operator_config.v0.ConfigSpecification\x12P\n\nproperties\x18\x05 \x03(\x0b\x32<.ansys.api.dpf.dpf_operator.v0.Specification.PropertiesEntry\x1ag\n\x14MapInputPinSpecEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12>\n\x05value\x18\x02 \x01(\x0b\x32/.ansys.api.dpf.dpf_operator.v0.PinSpecification:\x02\x38\x01\x1ah\n\x15MapOutputPinSpecEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12>\n\x05value\x18\x02 \x01(\x0b\x32/.ansys.api.dpf.dpf_operator.v0.PinSpecification:\x02\x38\x01\x1a\x31\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x86\x01\n\x10PinSpecification\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ntype_names\x18\x02 \x03(\t\x12\x10\n\x08optional\x18\x03 \x01(\x08\x12\x10\n\x08\x64ocument\x18\x04 \x01(\t\x12\x10\n\x08\x65llipsis\x18\x05 \x01(\x08\x12\x1a\n\x12name_derived_class\x18\x06 \x01(\t\"Y\n\rOperatorInput\x12\x38\n\x07inputop\x18\x01 \x01(\x0b\x32\'.ansys.api.dpf.dpf_operator.v0.Operator\x12\x0e\n\x06pinOut\x18\x03 \x01(\x05\"\xa5\t\n\rUpdateRequest\x12\x33\n\x02op\x18\x01 \x01(\x0b\x32\'.ansys.api.dpf.dpf_operator.v0.Operator\x12\x0b\n\x03pin\x18\x02 \x01(\x05\x12\r\n\x03str\x18\x03 \x01(\tH\x00\x12\r\n\x03int\x18\x04 \x01(\x05H\x00\x12\x10\n\x06\x64ouble\x18\x05 \x01(\x01H\x00\x12\x0e\n\x04\x62ool\x18\x06 \x01(\x08H\x00\x12.\n\x05\x66ield\x18\x07 \x01(\x0b\x32\x1d.ansys.api.dpf.field.v0.FieldH\x00\x12=\n\ncollection\x18\x08 \x01(\x0b\x32\'.ansys.api.dpf.collection.v0.CollectionH\x00\x12\x34\n\x07scoping\x18\t \x01(\x0b\x32!.ansys.api.dpf.scoping.v0.ScopingH\x00\x12\x42\n\x0c\x64\x61ta_sources\x18\n \x01(\x0b\x32*.ansys.api.dpf.data_sources.v0.DataSourcesH\x00\x12<\n\x04mesh\x18\x0b \x01(\x0b\x32,.ansys.api.dpf.meshed_region.v0.MeshedRegionH\x00\x12\x30\n\x04vint\x18\x0c \x01(\x0b\x32 .ansys.api.dpf.base.v0.IntVectorH\x00\x12\x36\n\x07vdouble\x18\r \x01(\x0b\x32#.ansys.api.dpf.base.v0.DoubleVectorH\x00\x12\x45\n\x0b\x63yc_support\x18\x0e \x01(\x0b\x32..ansys.api.dpf.cyclic_support.v0.CyclicSupportH\x00\x12P\n\x11time_freq_support\x18\x0f \x01(\x0b\x32\x33.ansys.api.dpf.time_freq_support.v0.TimeFreqSupportH\x00\x12?\n\x08workflow\x18\x10 \x01(\x0b\x32+.ansys.api.dpf.workflow_message.v0.WorkflowH\x00\x12\x39\n\tdata_tree\x18\x12 \x01(\x0b\x32$.ansys.api.dpf.data_tree.v0.DataTreeH\x00\x12:\n\x06\x61s_any\x18\x13 \x01(\x0b\x32(.ansys.api.dpf.dpf_any_message.v0.DpfAnyH\x00\x12?\n\x0blabel_space\x18\x14 \x01(\x0b\x32(.ansys.api.dpf.label_space.v0.LabelSpaceH\x00\x12\x44\n\x11operator_as_input\x18\x15 \x01(\x0b\x32\'.ansys.api.dpf.dpf_operator.v0.OperatorH\x00\x12_\n\x16generic_data_container\x18\x16 \x01(\x0b\x32=.ansys.api.dpf.generic_data_container.v0.GenericDataContainerH\x00\x12?\n\x07inputop\x18\x11 \x01(\x0b\x32,.ansys.api.dpf.dpf_operator.v0.OperatorInputH\x00\x42\x07\n\x05input\"\x8c\x01\n\x13UpdateConfigRequest\x12\x33\n\x02op\x18\x01 \x01(\x0b\x32\'.ansys.api.dpf.dpf_operator.v0.Operator\x12@\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x30.ansys.api.dpf.operator_config.v0.OperatorConfig\"\xb6\x01\n\x19OperatorEvaluationRequest\x12\x33\n\x02op\x18\x01 \x01(\x0b\x32\'.ansys.api.dpf.dpf_operator.v0.Operator\x12\x0b\n\x03pin\x18\x02 \x01(\x05\x12)\n\x04type\x18\x03 \x01(\x0e\x32\x1b.ansys.api.dpf.base.v0.Type\x12,\n\x07subtype\x18\x04 \x01(\x0e\x32\x1b.ansys.api.dpf.base.v0.Type\"g\n\x15\x43reateOperatorRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12@\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x30.ansys.api.dpf.operator_config.v0.OperatorConfig\"\xb0\x07\n\x10OperatorResponse\x12\r\n\x03str\x18\x03 \x01(\tH\x00\x12\r\n\x03int\x18\x04 \x01(\x05H\x00\x12\x10\n\x06\x64ouble\x18\x05 \x01(\x01H\x00\x12\x0e\n\x04\x62ool\x18\x06 \x01(\x08H\x00\x12.\n\x05\x66ield\x18\x07 \x01(\x0b\x32\x1d.ansys.api.dpf.field.v0.FieldH\x00\x12=\n\ncollection\x18\x08 \x01(\x0b\x32\'.ansys.api.dpf.collection.v0.CollectionH\x00\x12\x34\n\x07scoping\x18\t \x01(\x0b\x32!.ansys.api.dpf.scoping.v0.ScopingH\x00\x12<\n\x04mesh\x18\n \x01(\x0b\x32,.ansys.api.dpf.meshed_region.v0.MeshedRegionH\x00\x12?\n\x0bresult_info\x18\x0b \x01(\x0b\x32(.ansys.api.dpf.result_info.v0.ResultInfoH\x00\x12P\n\x11time_freq_support\x18\x0c \x01(\x0b\x32\x33.ansys.api.dpf.time_freq_support.v0.TimeFreqSupportH\x00\x12\x42\n\x0c\x64\x61ta_sources\x18\r \x01(\x0b\x32*.ansys.api.dpf.data_sources.v0.DataSourcesH\x00\x12\x45\n\x0b\x63yc_support\x18\x0e \x01(\x0b\x32..ansys.api.dpf.cyclic_support.v0.CyclicSupportH\x00\x12?\n\x08workflow\x18\x0f \x01(\x0b\x32+.ansys.api.dpf.workflow_message.v0.WorkflowH\x00\x12\x37\n\x03\x61ny\x18\x10 \x01(\x0b\x32(.ansys.api.dpf.dpf_any_message.v0.DpfAnyH\x00\x12;\n\x08operator\x18\x11 \x01(\x0b\x32\'.ansys.api.dpf.dpf_operator.v0.OperatorH\x00\x12\x39\n\tdata_tree\x18\x12 \x01(\x0b\x32$.ansys.api.dpf.data_tree.v0.DataTreeH\x00\x12_\n\x16generic_data_container\x18\x13 \x01(\x0b\x32=.ansys.api.dpf.generic_data_container.v0.GenericDataContainerH\x00\x42\x08\n\x06output\"\x9d\x01\n\x0cListResponse\x12\x0f\n\x07op_name\x18\x01 \x01(\t\x12@\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x30.ansys.api.dpf.operator_config.v0.OperatorConfig\x12:\n\x04spec\x18\x03 \x01(\x0b\x32,.ansys.api.dpf.dpf_operator.v0.Specification\"G\n\x10GetStatusRequest\x12\x33\n\x02op\x18\x01 \x01(\x0b\x32\'.ansys.api.dpf.dpf_operator.v0.Operator\"#\n\x11GetStatusResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x19\n\x17ListAllOperatorsRequest\")\n\x18ListAllOperatorsResponse\x12\r\n\x05\x61rray\x18\x01 \x01(\x0c\x32\xcb\x06\n\x0fOperatorService\x12g\n\x06\x43reate\x12\x34.ansys.api.dpf.dpf_operator.v0.CreateOperatorRequest\x1a\'.ansys.api.dpf.dpf_operator.v0.Operator\x12T\n\x06Update\x12,.ansys.api.dpf.dpf_operator.v0.UpdateRequest\x1a\x1c.ansys.api.dpf.base.v0.Empty\x12`\n\x0cUpdateConfig\x12\x32.ansys.api.dpf.dpf_operator.v0.UpdateConfigRequest\x1a\x1c.ansys.api.dpf.base.v0.Empty\x12p\n\x03Get\x12\x38.ansys.api.dpf.dpf_operator.v0.OperatorEvaluationRequest\x1a/.ansys.api.dpf.dpf_operator.v0.OperatorResponse\x12\\\n\x04List\x12\'.ansys.api.dpf.dpf_operator.v0.Operator\x1a+.ansys.api.dpf.dpf_operator.v0.ListResponse\x12n\n\tGetStatus\x12/.ansys.api.dpf.dpf_operator.v0.GetStatusRequest\x1a\x30.ansys.api.dpf.dpf_operator.v0.GetStatusResponse\x12O\n\x06\x44\x65lete\x12\'.ansys.api.dpf.dpf_operator.v0.Operator\x1a\x1c.ansys.api.dpf.base.v0.Empty\x12\x85\x01\n\x10ListAllOperators\x12\x36.ansys.api.dpf.dpf_operator.v0.ListAllOperatorsRequest\x1a\x37.ansys.api.dpf.dpf_operator.v0.ListAllOperatorsResponse0\x01\x42\x1c\xaa\x02\x19\x41nsys.Api.Dpf.Operator.V0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'operator_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\031Ansys.Api.Dpf.Operator.V0'
  _SPECIFICATION_MAPINPUTPINSPECENTRY._options = None
  _SPECIFICATION_MAPINPUTPINSPECENTRY._serialized_options = b'8\001'
  _SPECIFICATION_MAPOUTPUTPINSPECENTRY._options = None
  _SPECIFICATION_MAPOUTPUTPINSPECENTRY._serialized_options = b'8\001'
  _SPECIFICATION_PROPERTIESENTRY._options = None
  _SPECIFICATION_PROPERTIESENTRY._serialized_options = b'8\001'
  _globals['_OPERATOR']._serialized_start=350
  _globals['_OPERATOR']._serialized_end=427
  _globals['_SPECIFICATION']._serialized_start=430
  _globals['_SPECIFICATION']._serialized_end=1078
  _globals['_SPECIFICATION_MAPINPUTPINSPECENTRY']._serialized_start=818
  _globals['_SPECIFICATION_MAPINPUTPINSPECENTRY']._serialized_end=921
  _globals['_SPECIFICATION_MAPOUTPUTPINSPECENTRY']._serialized_start=923
  _globals['_SPECIFICATION_MAPOUTPUTPINSPECENTRY']._serialized_end=1027
  _globals['_SPECIFICATION_PROPERTIESENTRY']._serialized_start=1029
  _globals['_SPECIFICATION_PROPERTIESENTRY']._serialized_end=1078
  _globals['_PINSPECIFICATION']._serialized_start=1081
  _globals['_PINSPECIFICATION']._serialized_end=1215
  _globals['_OPERATORINPUT']._serialized_start=1217
  _globals['_OPERATORINPUT']._serialized_end=1306
  _globals['_UPDATEREQUEST']._serialized_start=1309
  _globals['_UPDATEREQUEST']._serialized_end=2498
  _globals['_UPDATECONFIGREQUEST']._serialized_start=2501
  _globals['_UPDATECONFIGREQUEST']._serialized_end=2641
  _globals['_OPERATOREVALUATIONREQUEST']._serialized_start=2644
  _globals['_OPERATOREVALUATIONREQUEST']._serialized_end=2826
  _globals['_CREATEOPERATORREQUEST']._serialized_start=2828
  _globals['_CREATEOPERATORREQUEST']._serialized_end=2931
  _globals['_OPERATORRESPONSE']._serialized_start=2934
  _globals['_OPERATORRESPONSE']._serialized_end=3878
  _globals['_LISTRESPONSE']._serialized_start=3881
  _globals['_LISTRESPONSE']._serialized_end=4038
  _globals['_GETSTATUSREQUEST']._serialized_start=4040
  _globals['_GETSTATUSREQUEST']._serialized_end=4111
  _globals['_GETSTATUSRESPONSE']._serialized_start=4113
  _globals['_GETSTATUSRESPONSE']._serialized_end=4148
  _globals['_LISTALLOPERATORSREQUEST']._serialized_start=4150
  _globals['_LISTALLOPERATORSREQUEST']._serialized_end=4175
  _globals['_LISTALLOPERATORSRESPONSE']._serialized_start=4177
  _globals['_LISTALLOPERATORSRESPONSE']._serialized_end=4218
  _globals['_OPERATORSERVICE']._serialized_start=4221
  _globals['_OPERATORSERVICE']._serialized_end=5064
# @@protoc_insertion_point(module_scope)