# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: base.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nbase.proto\x12\x15\x61nsys.api.dpf.base.v0\"\x07\n\x05\x45mpty\"6\n\x10\x45ntityIdentifier\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x16\n\x0eserver_address\x18\x02 \x01(\t\"\"\n\x0c\x44oubleVector\x12\x12\n\nrep_double\x18\x01 \x03(\x01\" \n\x0b\x46loatVector\x12\x11\n\trep_float\x18\x01 \x03(\x02\"\x1c\n\tIntVector\x12\x0f\n\x07rep_int\x18\x01 \x03(\x05\"\x1f\n\nByteVector\x12\x11\n\trep_bytes\x18\x01 \x01(\x0c\"\x1a\n\x08PBString\x12\x0e\n\x06string\x18\x01 \x01(\t\"\"\n\x0cStringVector\x12\x12\n\nrep_string\x18\x01 \x03(\t\"4\n\x03Ids\x12-\n\x03ids\x18\x01 \x01(\x0b\x32 .ansys.api.dpf.base.v0.IntVector\"\x1c\n\x08Location\x12\x10\n\x08location\x18\x01 \x01(\t\"\x1e\n\rCountResponse\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\"\x16\n\x05\x41rray\x12\r\n\x05\x61rray\x18\x01 \x01(\x0c\"V\n\rPluginRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x64llPath\x18\x02 \x01(\t\x12\x0e\n\x06symbol\x18\x03 \x01(\t\x12\x16\n\x0egenerate_files\x18\x04 \x01(\x08\"\x13\n\x11ServerInfoRequest\"\xef\x01\n\x12ServerInfoResponse\x12\x14\n\x0cmajorVersion\x18\x01 \x01(\x05\x12\x14\n\x0cminorVersion\x18\x02 \x01(\x05\x12\x11\n\tprocessId\x18\x03 \x01(\x04\x12\n\n\x02ip\x18\x04 \x01(\t\x12\x0c\n\x04port\x18\x05 \x01(\x05\x12M\n\nproperties\x18\x06 \x03(\x0b\x32\x39.ansys.api.dpf.base.v0.ServerInfoResponse.PropertiesEntry\x1a\x31\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"&\n\x0f\x44\x65scribeRequest\x12\x13\n\x0b\x64pf_type_id\x18\x01 \x01(\x05\"M\n\rDeleteRequest\x12<\n\x0b\x64pf_type_id\x18\x01 \x03(\x0b\x32\'.ansys.api.dpf.base.v0.EntityIdentifier\"S\n\x13\x44uplicateRefRequest\x12<\n\x0b\x64pf_type_id\x18\x01 \x01(\x0b\x32\'.ansys.api.dpf.base.v0.EntityIdentifier\"\'\n\x10\x44\x65scribeResponse\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\"X\n\x14\x44uplicateRefResponse\x12@\n\x0fnew_dpf_type_id\x18\x01 \x01(\x0b\x32\'.ansys.api.dpf.base.v0.EntityIdentifier\"2\n\x08\x46ileData\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x18\n\x10server_file_path\x18\x02 \x01(\t\"/\n\x13\x44ownloadFileRequest\x12\x18\n\x10server_file_path\x18\x01 \x01(\t\"E\n\x14\x44ownloadFileResponse\x12-\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x1f.ansys.api.dpf.base.v0.FileData\"r\n\x11UploadFileRequest\x12\x18\n\x10server_file_path\x18\x01 \x01(\t\x12\x14\n\x0cuse_temp_dir\x18\x02 \x01(\x08\x12-\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x1f.ansys.api.dpf.base.v0.FileData\".\n\x12UploadFileResponse\x12\x18\n\x10server_file_path\x18\x01 \x01(\t\"G\n\x10SerializeRequest\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.ansys.api.dpf.base.v0.EntityIdentifier\"\"\n\x11SerializeResponse\x12\r\n\x05\x61rray\x18\x01 \x01(\x0c\"c\n\x0e\x43onfigResponse\x12Q\n runtime_core_config_data_tree_id\x18\x01 \x01(\x0b\x32\'.ansys.api.dpf.base.v0.EntityIdentifier\">\n\x05\x45rror\x12\n\n\x02ok\x18\x01 \x01(\x08\x12\x12\n\nerror_code\x18\x02 \x01(\x05\x12\x15\n\rerror_message\x18\x03 \x01(\t\"K\n\x15InitializationRequest\x12\x0f\n\x07\x63ontext\x18\x01 \x01(\x05\x12\x0b\n\x03xml\x18\x02 \x01(\t\x12\x14\n\x0c\x66orce_reinit\x18\x03 \x01(\x08\"E\n\x16InitializationResponse\x12+\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1c.ansys.api.dpf.base.v0.Error*U\n\x0b\x43ountEntity\x12\x11\n\rNUM_COMPONENT\x10\x00\x12\x17\n\x13NUM_ELEMENTARY_DATA\x10\x01\x12\x0c\n\x08NUM_SETS\x10\x02\x12\x0c\n\x08NUM_DATA\x10\x03*\"\n\x07\x43omplex\x12\x08\n\x04REAL\x10\x00\x12\r\n\tIMAGINARY\x10\x01*;\n\x06Nature\x12\n\n\x06SCALAR\x10\x00\x12\n\n\x06VECTOR\x10\x01\x12\n\n\x06MATRIX\x10\x02\x12\r\n\tSYMMATRIX\x10\x05*\x8a\x03\n\x04Type\x12\n\n\x06STRING\x10\x00\x12\x07\n\x03INT\x10\x01\x12\n\n\x06\x44OUBLE\x10\x02\x12\x08\n\x04\x42OOL\x10\x03\x12\t\n\x05\x46IELD\x10\x04\x12\x0e\n\nCOLLECTION\x10\x05\x12\x0b\n\x07SCOPING\x10\x06\x12\x10\n\x0c\x44\x41TA_SOURCES\x10\x07\x12\x11\n\rMESHED_REGION\x10\x08\x12\x15\n\x11TIME_FREQ_SUPPORT\x10\t\x12\x0f\n\x0bRESULT_INFO\x10\n\x12\x12\n\x0e\x43YCLIC_SUPPORT\x10\x0b\x12\x12\n\x0ePROPERTY_FIELD\x10\x0c\x12\x0c\n\x08WORKFLOW\x10\r\x12\x07\n\x03RUN\x10\x0e\x12\x07\n\x03\x41NY\x10\x0f\x12\x0b\n\x07VEC_INT\x10\x10\x12\x0e\n\nVEC_DOUBLE\x10\x11\x12\x0b\n\x07SUPPORT\x10\x12\x12\x0c\n\x08OPERATOR\x10\x13\x12\r\n\tDATA_TREE\x10\x14\x12\x0e\n\nVEC_STRING\x10\x15\x12\x10\n\x0cSTRING_FIELD\x10\x16\x12\x15\n\x11\x43USTOM_TYPE_FIELD\x10\x17\x12\x1a\n\x16GENERIC_DATA_CONTAINER\x10\x18\x32\xb7\t\n\x0b\x42\x61seService\x12i\n\nInitialize\x12,.ansys.api.dpf.base.v0.InitializationRequest\x1a-.ansys.api.dpf.base.v0.InitializationResponse\x12\x64\n\rGetServerInfo\x12(.ansys.api.dpf.base.v0.ServerInfoRequest\x1a).ansys.api.dpf.base.v0.ServerInfoResponse\x12P\n\tGetConfig\x12\x1c.ansys.api.dpf.base.v0.Empty\x1a%.ansys.api.dpf.base.v0.ConfigResponse\x12J\n\x04Load\x12$.ansys.api.dpf.base.v0.PluginRequest\x1a\x1c.ansys.api.dpf.base.v0.Empty\x12[\n\x08\x44\x65scribe\x12&.ansys.api.dpf.base.v0.DescribeRequest\x1a\'.ansys.api.dpf.base.v0.DescribeResponse\x12L\n\x06\x44\x65lete\x12$.ansys.api.dpf.base.v0.DeleteRequest\x1a\x1c.ansys.api.dpf.base.v0.Empty\x12`\n\tSerialize\x12\'.ansys.api.dpf.base.v0.SerializeRequest\x1a(.ansys.api.dpf.base.v0.SerializeResponse0\x01\x12g\n\x0c\x44uplicateRef\x12*.ansys.api.dpf.base.v0.DuplicateRefRequest\x1a+.ansys.api.dpf.base.v0.DuplicateRefResponse\x12W\n\x0c\x43reateTmpDir\x12\x1c.ansys.api.dpf.base.v0.Empty\x1a).ansys.api.dpf.base.v0.UploadFileResponse\x12i\n\x0c\x44ownloadFile\x12*.ansys.api.dpf.base.v0.DownloadFileRequest\x1a+.ansys.api.dpf.base.v0.DownloadFileResponse0\x01\x12\x63\n\nUploadFile\x12(.ansys.api.dpf.base.v0.UploadFileRequest\x1a).ansys.api.dpf.base.v0.UploadFileResponse(\x01\x12M\n\x0fPrepareShutdown\x12\x1c.ansys.api.dpf.base.v0.Empty\x1a\x1c.ansys.api.dpf.base.v0.Empty\x12K\n\rReleaseServer\x12\x1c.ansys.api.dpf.base.v0.Empty\x1a\x1c.ansys.api.dpf.base.v0.EmptyB\x18\xaa\x02\x15\x41nsys.Api.Dpf.Base.V0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'base_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\025Ansys.Api.Dpf.Base.V0'
  _SERVERINFORESPONSE_PROPERTIESENTRY._options = None
  _SERVERINFORESPONSE_PROPERTIESENTRY._serialized_options = b'8\001'
  _globals['_COUNTENTITY']._serialized_start=1883
  _globals['_COUNTENTITY']._serialized_end=1968
  _globals['_COMPLEX']._serialized_start=1970
  _globals['_COMPLEX']._serialized_end=2004
  _globals['_NATURE']._serialized_start=2006
  _globals['_NATURE']._serialized_end=2065
  _globals['_TYPE']._serialized_start=2068
  _globals['_TYPE']._serialized_end=2462
  _globals['_EMPTY']._serialized_start=37
  _globals['_EMPTY']._serialized_end=44
  _globals['_ENTITYIDENTIFIER']._serialized_start=46
  _globals['_ENTITYIDENTIFIER']._serialized_end=100
  _globals['_DOUBLEVECTOR']._serialized_start=102
  _globals['_DOUBLEVECTOR']._serialized_end=136
  _globals['_FLOATVECTOR']._serialized_start=138
  _globals['_FLOATVECTOR']._serialized_end=170
  _globals['_INTVECTOR']._serialized_start=172
  _globals['_INTVECTOR']._serialized_end=200
  _globals['_BYTEVECTOR']._serialized_start=202
  _globals['_BYTEVECTOR']._serialized_end=233
  _globals['_PBSTRING']._serialized_start=235
  _globals['_PBSTRING']._serialized_end=261
  _globals['_STRINGVECTOR']._serialized_start=263
  _globals['_STRINGVECTOR']._serialized_end=297
  _globals['_IDS']._serialized_start=299
  _globals['_IDS']._serialized_end=351
  _globals['_LOCATION']._serialized_start=353
  _globals['_LOCATION']._serialized_end=381
  _globals['_COUNTRESPONSE']._serialized_start=383
  _globals['_COUNTRESPONSE']._serialized_end=413
  _globals['_ARRAY']._serialized_start=415
  _globals['_ARRAY']._serialized_end=437
  _globals['_PLUGINREQUEST']._serialized_start=439
  _globals['_PLUGINREQUEST']._serialized_end=525
  _globals['_SERVERINFOREQUEST']._serialized_start=527
  _globals['_SERVERINFOREQUEST']._serialized_end=546
  _globals['_SERVERINFORESPONSE']._serialized_start=549
  _globals['_SERVERINFORESPONSE']._serialized_end=788
  _globals['_SERVERINFORESPONSE_PROPERTIESENTRY']._serialized_start=739
  _globals['_SERVERINFORESPONSE_PROPERTIESENTRY']._serialized_end=788
  _globals['_DESCRIBEREQUEST']._serialized_start=790
  _globals['_DESCRIBEREQUEST']._serialized_end=828
  _globals['_DELETEREQUEST']._serialized_start=830
  _globals['_DELETEREQUEST']._serialized_end=907
  _globals['_DUPLICATEREFREQUEST']._serialized_start=909
  _globals['_DUPLICATEREFREQUEST']._serialized_end=992
  _globals['_DESCRIBERESPONSE']._serialized_start=994
  _globals['_DESCRIBERESPONSE']._serialized_end=1033
  _globals['_DUPLICATEREFRESPONSE']._serialized_start=1035
  _globals['_DUPLICATEREFRESPONSE']._serialized_end=1123
  _globals['_FILEDATA']._serialized_start=1125
  _globals['_FILEDATA']._serialized_end=1175
  _globals['_DOWNLOADFILEREQUEST']._serialized_start=1177
  _globals['_DOWNLOADFILEREQUEST']._serialized_end=1224
  _globals['_DOWNLOADFILERESPONSE']._serialized_start=1226
  _globals['_DOWNLOADFILERESPONSE']._serialized_end=1295
  _globals['_UPLOADFILEREQUEST']._serialized_start=1297
  _globals['_UPLOADFILEREQUEST']._serialized_end=1411
  _globals['_UPLOADFILERESPONSE']._serialized_start=1413
  _globals['_UPLOADFILERESPONSE']._serialized_end=1459
  _globals['_SERIALIZEREQUEST']._serialized_start=1461
  _globals['_SERIALIZEREQUEST']._serialized_end=1532
  _globals['_SERIALIZERESPONSE']._serialized_start=1534
  _globals['_SERIALIZERESPONSE']._serialized_end=1568
  _globals['_CONFIGRESPONSE']._serialized_start=1570
  _globals['_CONFIGRESPONSE']._serialized_end=1669
  _globals['_ERROR']._serialized_start=1671
  _globals['_ERROR']._serialized_end=1733
  _globals['_INITIALIZATIONREQUEST']._serialized_start=1735
  _globals['_INITIALIZATIONREQUEST']._serialized_end=1810
  _globals['_INITIALIZATIONRESPONSE']._serialized_start=1812
  _globals['_INITIALIZATIONRESPONSE']._serialized_end=1881
  _globals['_BASESERVICE']._serialized_start=2465
  _globals['_BASESERVICE']._serialized_end=3672
# @@protoc_insertion_point(module_scope)