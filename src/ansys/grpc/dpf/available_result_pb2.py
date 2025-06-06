# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: available_result.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ansys.grpc.dpf.base_pb2 as base__pb2
import ansys.grpc.dpf.label_space_pb2 as label__space__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x61vailable_result.proto\x12!ansys.api.dpf.available_result.v0\x1a\nbase.proto\x1a\x11label_space.proto\"?\n\tSubResult\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07op_name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\"\xe5\x03\n\x17\x41vailableResultResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bphysicsname\x18\x02 \x01(\t\x12\r\n\x05ncomp\x18\x03 \x01(\x05\x12\x35\n\x0e\x64imensionality\x18\x04 \x01(\x0e\x32\x1d.ansys.api.dpf.base.v0.Nature\x12\x43\n\x0bhomogeneity\x18\x05 \x01(\x0e\x32..ansys.api.dpf.available_result.v0.Homogeneity\x12\x0c\n\x04unit\x18\x06 \x01(\t\x12=\n\x07sub_res\x18\x07 \x03(\x0b\x32,.ansys.api.dpf.available_result.v0.SubResult\x12^\n\nproperties\x18\x08 \x03(\x0b\x32J.ansys.api.dpf.available_result.v0.AvailableResultResponse.PropertiesEntry\x12<\n\nqualifiers\x18\t \x03(\x0b\x32(.ansys.api.dpf.label_space.v0.LabelSpace\x1a\x31\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01*\xde\n\n\x0bHomogeneity\x12\x10\n\x0c\x41\x43\x43\x45LERATION\x10\x00\x12\t\n\x05\x41NGLE\x10\x01\x12\x14\n\x10\x41NGULAR_VELOCITY\x10\x02\x12\x0b\n\x07SURFACE\x10\x03\x12\x0f\n\x0b\x43\x41PACITANCE\x10\x04\x12\x13\n\x0f\x45LECTRIC_CHARGE\x10\x05\x12\x1b\n\x17\x45LECTRIC_CHARGE_DENSITY\x10\x06\x12\x10\n\x0c\x43ONDUCTIVITY\x10\x07\x12\x0b\n\x07\x43URRENT\x10\x08\x12\x13\n\x0f\x43URRENT_DENSITY\x10\t\x12\x0b\n\x07\x44\x45NSITY\x10\n\x12\x10\n\x0c\x44ISPLACEMENT\x10\x0b\x12\x19\n\x15\x45LECTRIC_CONDUCTIVITY\x10\x0c\x12\x12\n\x0e\x45LECTRIC_FIELD\x10\r\x12\x19\n\x15\x45LECTRIC_FLUX_DENSITY\x10\x0e\x12\x18\n\x13\x45LECTRIC_RESISTANCE\x10\xe8\x07\x12\x18\n\x14\x45LECTRIC_RESISTIVITY\x10\x0f\x12\n\n\x06\x45NERGY\x10\x10\x12\x14\n\x10\x46ILM_COEFFICIENT\x10\x11\x12\t\n\x05\x46ORCE\x10\x12\x12\x13\n\x0f\x46ORCE_INTENSITY\x10\x13\x12\r\n\tFREQUENCY\x10\x14\x12\r\n\tHEAT_FLUX\x10\x15\x12\x13\n\x0fHEAT_GENERATION\x10\x16\x12\r\n\tHEAT_RATE\x10\x17\x12\x0e\n\nINDUCTANCE\x10\x18\x12\x12\n\x0eINVERSE_STRESS\x10\x19\x12\n\n\x06LENGTH\x10\x1a\x12\x1c\n\x18MAGNETIC_FIELD_INTENSITY\x10\x1b\x12\x11\n\rMAGNETIC_FLUX\x10\x1c\x12\x19\n\x15MAGNETIC_FLUX_DENSITY\x10\x1d\x12\x08\n\x04MASS\x10\x1e\x12\n\n\x06MOMENT\x10\x1f\x12\x13\n\x0fMOMENT_INTERTIA\x10 \x12\x12\n\x0eMOMENT_INERTIA\x10 \x12\x17\n\x13MOMENT_INERTIA_MASS\x10\x37\x12\x10\n\x0cPERMEABILITY\x10!\x12\x10\n\x0cPERMITTIVITY\x10\"\x12\x0b\n\x07POISSON\x10#\x12\t\n\x05POWER\x10$\x12\x0c\n\x08PRESSURE\x10%\x12\x19\n\x15RELATIVE_PERMEABILITY\x10&\x12\x19\n\x15RELATIVE_PERMITTIVITY\x10\'\x12\x13\n\x0fSECTION_MODULUS\x10(\x12\x11\n\rSPECIFIC_HEAT\x10)\x12\x13\n\x0fSPECIFIC_WEIGHT\x10*\x12\x10\n\x0cSHEAR_STRAIN\x10+\x12\r\n\tSTIFFNESS\x10,\x12\n\n\x06STRAIN\x10-\x12\n\n\x06STRESS\x10.\x12\x0c\n\x08STRENGTH\x10/\x12\x15\n\x11THERMAL_EXPANSION\x10\x30\x12\x0f\n\x0bTEMPERATURE\x10\x31\x12\x1a\n\x16TEMPERATURE_DIFFERENCE\x10N\x12\x08\n\x04TIME\x10\x32\x12\x0c\n\x08VELOCITY\x10\x33\x12\x0b\n\x07VOLTAGE\x10\x34\x12\n\n\x06VOLUME\x10\x35\x12\x1b\n\x17STRESS_INTENSITY_FACTOR\x10\\\x12\x14\n\x10THERMAL_GRADIENT\x10_\x12\x18\n\x14\x41NGULAR_ACCELERATION\x10?\x12\x11\n\rDIMENSIONLESS\x10u\x12\r\n\tVISCOSITY\x10v\x12\x14\n\x10\x44ISSIPATION_RATE\x10w\x12\x0c\n\x08MOMENTUM\x10x\x12\x14\n\x10VOLUME_FLOW_RATE\x10y\x12\x12\n\x0eMASS_FLOW_RATE\x10z\x12\x13\n\x0fSPECIFIC_ENERGY\x10{\x12\x14\n\x10SPECIFIC_ENTROPY\x10|\x12\x11\n\rFORCE_DENSITY\x10}\x12\x1d\n\x19MAGNETIC_VECTOR_POTENTIAL\x10~\x12\x0c\n\x07UNKNOWN\x10\x90N\x1a\x02\x10\x01\x42#\xaa\x02 Ansys.Api.Dpf.AvailableResult.V0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'available_result_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002 Ansys.Api.Dpf.AvailableResult.V0'
  _globals['_HOMOGENEITY']._options = None
  _globals['_HOMOGENEITY']._serialized_options = b'\020\001'
  _globals['_AVAILABLERESULTRESPONSE_PROPERTIESENTRY']._options = None
  _globals['_AVAILABLERESULTRESPONSE_PROPERTIESENTRY']._serialized_options = b'8\001'
  _globals['_HOMOGENEITY']._serialized_start=646
  _globals['_HOMOGENEITY']._serialized_end=2020
  _globals['_SUBRESULT']._serialized_start=92
  _globals['_SUBRESULT']._serialized_end=155
  _globals['_AVAILABLERESULTRESPONSE']._serialized_start=158
  _globals['_AVAILABLERESULTRESPONSE']._serialized_end=643
  _globals['_AVAILABLERESULTRESPONSE_PROPERTIESENTRY']._serialized_start=594
  _globals['_AVAILABLERESULTRESPONSE_PROPERTIESENTRY']._serialized_end=643
# @@protoc_insertion_point(module_scope)
