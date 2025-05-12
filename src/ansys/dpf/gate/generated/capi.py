import ctypes
#-------------------------------------------------------------------------------
# Callbacks
#-------------------------------------------------------------------------------
UnknwonTypeDestructor = ctypes.CFUNCTYPE(None, ctypes.c_void_p)
ReleaseFileCallback = ctypes.CFUNCTYPE(None, ctypes.c_void_p)
DeleteCallback = ctypes.CFUNCTYPE(None, ctypes.c_void_p)
ExternalDataDeleter = ctypes.CFUNCTYPE(None, ctypes.c_void_p)
OperatorCallBack = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)
OperatorMainCallback = ctypes.CFUNCTYPE(None, ctypes.c_void_p)
StringCallback = ctypes.CFUNCTYPE(None, ctypes.c_char_p)
StringIntCallback = ctypes.CFUNCTYPE(None, ctypes.c_char_p, ctypes.c_int)
IntIntCallback = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)
GenericCallBackType = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_char_p)

def load_api(path):
	global dll
	dll = ctypes.cdll.LoadLibrary(path)

	#-------------------------------------------------------------------------------
	# Any
	#-------------------------------------------------------------------------------
	if hasattr(dll, "Any_WrappedTypeString"):
		dll.Any_WrappedTypeString.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_WrappedTypeString.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "Any_ObjectIsOfType"):
		dll.Any_ObjectIsOfType.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_ObjectIsOfType.restype = ctypes.c_bool

	if hasattr(dll, "Any_unwrap_to_real_type"):
		dll.Any_unwrap_to_real_type.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_unwrap_to_real_type.restype = ctypes.c_void_p

	if hasattr(dll, "Any_getAs_FieldsContainer"):
		dll.Any_getAs_FieldsContainer.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_getAs_FieldsContainer.restype = ctypes.c_void_p

	if hasattr(dll, "Any_getAs_ScopingsContainer"):
		dll.Any_getAs_ScopingsContainer.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_getAs_ScopingsContainer.restype = ctypes.c_void_p

	if hasattr(dll, "Any_getAs_Field"):
		dll.Any_getAs_Field.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_getAs_Field.restype = ctypes.c_void_p

	if hasattr(dll, "Any_getAs_Scoping"):
		dll.Any_getAs_Scoping.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_getAs_Scoping.restype = ctypes.c_void_p

	if hasattr(dll, "Any_getAs_DataSources"):
		dll.Any_getAs_DataSources.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_getAs_DataSources.restype = ctypes.c_void_p

	if hasattr(dll, "Any_getAs_MeshesContainer"):
		dll.Any_getAs_MeshesContainer.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_getAs_MeshesContainer.restype = ctypes.c_void_p

	if hasattr(dll, "Any_getAs_AnyCollection"):
		dll.Any_getAs_AnyCollection.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_getAs_AnyCollection.restype = ctypes.c_void_p

	if hasattr(dll, "Any_getAs_String"):
		dll.Any_getAs_String.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_getAs_String.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "Any_getAs_String_with_size"):
		dll.Any_getAs_String_with_size.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_getAs_String_with_size.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "Any_getAs_Int"):
		dll.Any_getAs_Int.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_getAs_Int.restype = ctypes.c_int32

	if hasattr(dll, "Any_getAs_Double"):
		dll.Any_getAs_Double.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_getAs_Double.restype = ctypes.c_double

	if hasattr(dll, "Any_getAs_IntCollection"):
		dll.Any_getAs_IntCollection.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_getAs_IntCollection.restype = ctypes.c_void_p

	if hasattr(dll, "Any_getAs_DoubleCollection"):
		dll.Any_getAs_DoubleCollection.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_getAs_DoubleCollection.restype = ctypes.c_void_p

	if hasattr(dll, "Any_getAs_CyclicSupport"):
		dll.Any_getAs_CyclicSupport.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_getAs_CyclicSupport.restype = ctypes.c_void_p

	if hasattr(dll, "Any_getAs_Workflow"):
		dll.Any_getAs_Workflow.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_getAs_Workflow.restype = ctypes.c_void_p

	if hasattr(dll, "Any_getAs_timeFreqSupport"):
		dll.Any_getAs_timeFreqSupport.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_getAs_timeFreqSupport.restype = ctypes.c_void_p

	if hasattr(dll, "Any_getAs_meshedRegion"):
		dll.Any_getAs_meshedRegion.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_getAs_meshedRegion.restype = ctypes.c_void_p

	if hasattr(dll, "Any_getAs_resultInfo"):
		dll.Any_getAs_resultInfo.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_getAs_resultInfo.restype = ctypes.c_void_p

	if hasattr(dll, "Any_getAs_MaterialsContainer"):
		dll.Any_getAs_MaterialsContainer.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_getAs_MaterialsContainer.restype = ctypes.c_void_p

	if hasattr(dll, "Any_getAs_streams"):
		dll.Any_getAs_streams.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_getAs_streams.restype = ctypes.c_void_p

	if hasattr(dll, "Any_getAs_propertyField"):
		dll.Any_getAs_propertyField.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_getAs_propertyField.restype = ctypes.c_void_p

	if hasattr(dll, "Any_getAs_DataTree"):
		dll.Any_getAs_DataTree.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_getAs_DataTree.restype = ctypes.c_void_p

	if hasattr(dll, "Any_getAs_Operator"):
		dll.Any_getAs_Operator.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_getAs_Operator.restype = ctypes.c_void_p

	if hasattr(dll, "Any_getAs_StringField"):
		dll.Any_getAs_StringField.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_getAs_StringField.restype = ctypes.c_void_p

	if hasattr(dll, "Any_getAs_GenericDataContainer"):
		dll.Any_getAs_GenericDataContainer.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_getAs_GenericDataContainer.restype = ctypes.c_void_p

	if hasattr(dll, "Any_getAs_CustomTypeFieldsContainer"):
		dll.Any_getAs_CustomTypeFieldsContainer.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_getAs_CustomTypeFieldsContainer.restype = ctypes.c_void_p

	if hasattr(dll, "Any_getAs_CustomTypeField"):
		dll.Any_getAs_CustomTypeField.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_getAs_CustomTypeField.restype = ctypes.c_void_p

	if hasattr(dll, "Any_getAs_Support"):
		dll.Any_getAs_Support.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_getAs_Support.restype = ctypes.c_void_p

	if hasattr(dll, "Any_makeObj_asAny"):
		dll.Any_makeObj_asAny.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_makeObj_asAny.restype = ctypes.c_void_p

	if hasattr(dll, "Any_newFrom_Int"):
		dll.Any_newFrom_Int.argtypes = (ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_newFrom_Int.restype = ctypes.c_void_p

	if hasattr(dll, "Any_newFrom_String"):
		dll.Any_newFrom_String.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_newFrom_String.restype = ctypes.c_void_p

	if hasattr(dll, "Any_newFrom_String_with_size"):
		dll.Any_newFrom_String_with_size.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.c_uint64, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_newFrom_String_with_size.restype = ctypes.c_void_p

	if hasattr(dll, "Any_newFrom_Double"):
		dll.Any_newFrom_Double.argtypes = (ctypes.c_double, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_newFrom_Double.restype = ctypes.c_void_p

	if hasattr(dll, "Any_newFrom_FieldsContainer"):
		dll.Any_newFrom_FieldsContainer.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_newFrom_FieldsContainer.restype = ctypes.c_void_p

	if hasattr(dll, "Any_newFrom_ScopingsContainer"):
		dll.Any_newFrom_ScopingsContainer.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_newFrom_ScopingsContainer.restype = ctypes.c_void_p

	if hasattr(dll, "Any_newFrom_Field"):
		dll.Any_newFrom_Field.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_newFrom_Field.restype = ctypes.c_void_p

	if hasattr(dll, "Any_newFrom_Scoping"):
		dll.Any_newFrom_Scoping.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_newFrom_Scoping.restype = ctypes.c_void_p

	if hasattr(dll, "Any_newFrom_DataSources"):
		dll.Any_newFrom_DataSources.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_newFrom_DataSources.restype = ctypes.c_void_p

	if hasattr(dll, "Any_newFrom_MeshesContainer"):
		dll.Any_newFrom_MeshesContainer.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_newFrom_MeshesContainer.restype = ctypes.c_void_p

	if hasattr(dll, "Any_newFrom_IntCollection"):
		dll.Any_newFrom_IntCollection.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_newFrom_IntCollection.restype = ctypes.c_void_p

	if hasattr(dll, "Any_newFrom_DoubleCollection"):
		dll.Any_newFrom_DoubleCollection.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_newFrom_DoubleCollection.restype = ctypes.c_void_p

	if hasattr(dll, "Any_newFrom_CyclicSupport"):
		dll.Any_newFrom_CyclicSupport.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_newFrom_CyclicSupport.restype = ctypes.c_void_p

	if hasattr(dll, "Any_newFrom_Workflow"):
		dll.Any_newFrom_Workflow.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_newFrom_Workflow.restype = ctypes.c_void_p

	if hasattr(dll, "Any_newFrom_timeFreqSupport"):
		dll.Any_newFrom_timeFreqSupport.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_newFrom_timeFreqSupport.restype = ctypes.c_void_p

	if hasattr(dll, "Any_newFrom_meshedRegion"):
		dll.Any_newFrom_meshedRegion.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_newFrom_meshedRegion.restype = ctypes.c_void_p

	if hasattr(dll, "Any_newFrom_resultInfo"):
		dll.Any_newFrom_resultInfo.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_newFrom_resultInfo.restype = ctypes.c_void_p

	if hasattr(dll, "Any_newFrom_MaterialsContainer"):
		dll.Any_newFrom_MaterialsContainer.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_newFrom_MaterialsContainer.restype = ctypes.c_void_p

	if hasattr(dll, "Any_newFrom_streams"):
		dll.Any_newFrom_streams.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_newFrom_streams.restype = ctypes.c_void_p

	if hasattr(dll, "Any_newFrom_propertyField"):
		dll.Any_newFrom_propertyField.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_newFrom_propertyField.restype = ctypes.c_void_p

	if hasattr(dll, "Any_newFrom_DataTree"):
		dll.Any_newFrom_DataTree.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_newFrom_DataTree.restype = ctypes.c_void_p

	if hasattr(dll, "Any_newFrom_Operator"):
		dll.Any_newFrom_Operator.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_newFrom_Operator.restype = ctypes.c_void_p

	if hasattr(dll, "Any_newFrom_StringField"):
		dll.Any_newFrom_StringField.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_newFrom_StringField.restype = ctypes.c_void_p

	if hasattr(dll, "Any_newFrom_GenericDataContainer"):
		dll.Any_newFrom_GenericDataContainer.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_newFrom_GenericDataContainer.restype = ctypes.c_void_p

	if hasattr(dll, "Any_newFrom_CustomTypeFieldsContainer"):
		dll.Any_newFrom_CustomTypeFieldsContainer.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_newFrom_CustomTypeFieldsContainer.restype = ctypes.c_void_p

	if hasattr(dll, "Any_newFrom_CustomTypeField"):
		dll.Any_newFrom_CustomTypeField.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_newFrom_CustomTypeField.restype = ctypes.c_void_p

	if hasattr(dll, "Any_newFrom_AnyCollection"):
		dll.Any_newFrom_AnyCollection.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_newFrom_AnyCollection.restype = ctypes.c_void_p

	if hasattr(dll, "Any_newFrom_Int_on_client"):
		dll.Any_newFrom_Int_on_client.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_newFrom_Int_on_client.restype = ctypes.c_void_p

	if hasattr(dll, "Any_newFrom_String_on_client"):
		dll.Any_newFrom_String_on_client.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_newFrom_String_on_client.restype = ctypes.c_void_p

	if hasattr(dll, "Any_newFrom_String_with_size_on_client"):
		dll.Any_newFrom_String_with_size_on_client.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_uint64, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_newFrom_String_with_size_on_client.restype = ctypes.c_void_p

	if hasattr(dll, "Any_newFrom_Double_on_client"):
		dll.Any_newFrom_Double_on_client.argtypes = (ctypes.c_void_p, ctypes.c_double, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_newFrom_Double_on_client.restype = ctypes.c_void_p

	if hasattr(dll, "Any_getCopy"):
		dll.Any_getCopy.argtypes = (ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Any_getCopy.restype = ctypes.c_void_p

	#-------------------------------------------------------------------------------
	# Client
	#-------------------------------------------------------------------------------
	if hasattr(dll, "Client_new"):
		dll.Client_new.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Client_new.restype = ctypes.c_void_p

	if hasattr(dll, "Client_new_full_address"):
		dll.Client_new_full_address.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Client_new_full_address.restype = ctypes.c_void_p

	if hasattr(dll, "Client_get_full_address"):
		dll.Client_get_full_address.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Client_get_full_address.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "Client_get_protocol_name"):
		dll.Client_get_protocol_name.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Client_get_protocol_name.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "Client_has_local_server"):
		dll.Client_has_local_server.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Client_has_local_server.restype = ctypes.c_bool

	if hasattr(dll, "Client_set_local_server"):
		dll.Client_set_local_server.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Client_set_local_server.restype = None

	if hasattr(dll, "Client_get_local_server"):
		dll.Client_get_local_server.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Client_get_local_server.restype = ctypes.c_void_p

	#-------------------------------------------------------------------------------
	# Collection
	#-------------------------------------------------------------------------------
	if hasattr(dll, "Collection_OfIntNew"):
		dll.Collection_OfIntNew.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_OfIntNew.restype = ctypes.c_void_p

	if hasattr(dll, "Collection_OfDoubleNew"):
		dll.Collection_OfDoubleNew.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_OfDoubleNew.restype = ctypes.c_void_p

	if hasattr(dll, "Collection_OfStringNew"):
		dll.Collection_OfStringNew.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_OfStringNew.restype = ctypes.c_void_p

	if hasattr(dll, "Collection_OfCharNew"):
		dll.Collection_OfCharNew.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_OfCharNew.restype = ctypes.c_void_p

	if hasattr(dll, "Collection_GetDataAsInt"):
		dll.Collection_GetDataAsInt.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_GetDataAsInt.restype = ctypes.POINTER(ctypes.c_int32)

	if hasattr(dll, "Collection_GetDataAsDouble"):
		dll.Collection_GetDataAsDouble.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_GetDataAsDouble.restype = ctypes.POINTER(ctypes.c_double)

	if hasattr(dll, "Collection_GetDataAsChar"):
		dll.Collection_GetDataAsChar.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_GetDataAsChar.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "Collection_AddIntEntry"):
		dll.Collection_AddIntEntry.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_AddIntEntry.restype = None

	if hasattr(dll, "Collection_AddDoubleEntry"):
		dll.Collection_AddDoubleEntry.argtypes = (ctypes.c_void_p, ctypes.c_double, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_AddDoubleEntry.restype = None

	if hasattr(dll, "Collection_AddStringEntry"):
		dll.Collection_AddStringEntry.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_AddStringEntry.restype = None

	if hasattr(dll, "Collection_SetIntEntry"):
		dll.Collection_SetIntEntry.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_SetIntEntry.restype = None

	if hasattr(dll, "Collection_SetDoubleEntry"):
		dll.Collection_SetDoubleEntry.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_double, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_SetDoubleEntry.restype = None

	if hasattr(dll, "Collection_SetStringEntry"):
		dll.Collection_SetStringEntry.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_SetStringEntry.restype = None

	if hasattr(dll, "Collection_GetIntEntry"):
		dll.Collection_GetIntEntry.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_GetIntEntry.restype = ctypes.c_int32

	if hasattr(dll, "Collection_GetDoubleEntry"):
		dll.Collection_GetDoubleEntry.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_GetDoubleEntry.restype = ctypes.c_double

	if hasattr(dll, "Collection_GetStringEntry"):
		dll.Collection_GetStringEntry.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_GetStringEntry.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "Collection_SetDataAsInt"):
		dll.Collection_SetDataAsInt.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_SetDataAsInt.restype = None

	if hasattr(dll, "Collection_SetDataAsDouble"):
		dll.Collection_SetDataAsDouble.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_double), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_SetDataAsDouble.restype = None

	if hasattr(dll, "Collection_GetDataAsInt_For_DpfVector"):
		dll.Collection_GetDataAsInt_For_DpfVector.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.POINTER(ctypes.c_int32)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_GetDataAsInt_For_DpfVector.restype = None

	if hasattr(dll, "Collection_GetDataAsDouble_For_DpfVector"):
		dll.Collection_GetDataAsDouble_For_DpfVector.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.POINTER(ctypes.c_double)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_GetDataAsDouble_For_DpfVector.restype = None

	if hasattr(dll, "Collection_OfScopingNew"):
		dll.Collection_OfScopingNew.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_OfScopingNew.restype = ctypes.c_void_p

	if hasattr(dll, "Collection_OfFieldNew"):
		dll.Collection_OfFieldNew.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_OfFieldNew.restype = ctypes.c_void_p

	if hasattr(dll, "Collection_OfMeshNew"):
		dll.Collection_OfMeshNew.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_OfMeshNew.restype = ctypes.c_void_p

	if hasattr(dll, "Collection_OfCustomTypeFieldNew"):
		dll.Collection_OfCustomTypeFieldNew.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_OfCustomTypeFieldNew.restype = ctypes.c_void_p

	if hasattr(dll, "Collection_OfAnyNew"):
		dll.Collection_OfAnyNew.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_OfAnyNew.restype = ctypes.c_void_p

	if hasattr(dll, "Collection_OfScopingNewWithData"):
		dll.Collection_OfScopingNewWithData.argtypes = (ctypes.POINTER(ctypes.c_void_p), ctypes.c_int32, ctypes.POINTER(ctypes.POINTER(ctypes.c_char)), ctypes.c_int32, ctypes.POINTER(ctypes.POINTER(ctypes.c_int32)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_OfScopingNewWithData.restype = ctypes.c_void_p

	if hasattr(dll, "Collection_OfFieldNewWithData"):
		dll.Collection_OfFieldNewWithData.argtypes = (ctypes.POINTER(ctypes.c_void_p), ctypes.c_int32, ctypes.POINTER(ctypes.POINTER(ctypes.c_char)), ctypes.c_int32, ctypes.POINTER(ctypes.POINTER(ctypes.c_int32)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_OfFieldNewWithData.restype = ctypes.c_void_p

	if hasattr(dll, "Collection_OfMeshNewWithData"):
		dll.Collection_OfMeshNewWithData.argtypes = (ctypes.POINTER(ctypes.c_void_p), ctypes.c_int32, ctypes.POINTER(ctypes.POINTER(ctypes.c_char)), ctypes.c_int32, ctypes.POINTER(ctypes.POINTER(ctypes.c_int32)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_OfMeshNewWithData.restype = ctypes.c_void_p

	if hasattr(dll, "Collection_OfCustomTypeFieldNewWithData"):
		dll.Collection_OfCustomTypeFieldNewWithData.argtypes = (ctypes.POINTER(ctypes.c_void_p), ctypes.c_int32, ctypes.POINTER(ctypes.POINTER(ctypes.c_char)), ctypes.c_int32, ctypes.POINTER(ctypes.POINTER(ctypes.c_int32)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_OfCustomTypeFieldNewWithData.restype = ctypes.c_void_p

	if hasattr(dll, "Collection_OfAnyNewWithData"):
		dll.Collection_OfAnyNewWithData.argtypes = (ctypes.POINTER(ctypes.c_void_p), ctypes.c_int32, ctypes.POINTER(ctypes.POINTER(ctypes.c_char)), ctypes.c_int32, ctypes.POINTER(ctypes.POINTER(ctypes.c_int32)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_OfAnyNewWithData.restype = ctypes.c_void_p

	if hasattr(dll, "Collection_GetNumLabels"):
		dll.Collection_GetNumLabels.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_GetNumLabels.restype = ctypes.c_int32

	if hasattr(dll, "Collection_GetLabel"):
		dll.Collection_GetLabel.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_GetLabel.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "Collection_AddLabel"):
		dll.Collection_AddLabel.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_AddLabel.restype = None

	if hasattr(dll, "Collection_AddLabelWithDefaultValue"):
		dll.Collection_AddLabelWithDefaultValue.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_AddLabelWithDefaultValue.restype = None

	if hasattr(dll, "Collection_AddEntry"):
		dll.Collection_AddEntry.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_AddEntry.restype = None

	if hasattr(dll, "Collection_PushBackEntry"):
		dll.Collection_PushBackEntry.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_PushBackEntry.restype = None

	if hasattr(dll, "Collection_SetEntryByIndex"):
		dll.Collection_SetEntryByIndex.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_SetEntryByIndex.restype = None

	if hasattr(dll, "Collection_GetObjByIndex"):
		dll.Collection_GetObjByIndex.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_GetObjByIndex.restype = ctypes.c_void_p

	if hasattr(dll, "Collection_GetObj"):
		dll.Collection_GetObj.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_GetObj.restype = ctypes.c_void_p

	if hasattr(dll, "Collection_GetObjLabelSpaceByIndex"):
		dll.Collection_GetObjLabelSpaceByIndex.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_GetObjLabelSpaceByIndex.restype = ctypes.c_void_p

	if hasattr(dll, "Collection_GetObjsForLabelSpace"):
		dll.Collection_GetObjsForLabelSpace.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_GetObjsForLabelSpace.restype = ctypes.POINTER(ctypes.c_void_p)

	if hasattr(dll, "Collection_GetNumObjForLabelSpace"):
		dll.Collection_GetNumObjForLabelSpace.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_GetNumObjForLabelSpace.restype = ctypes.c_int32

	if hasattr(dll, "Collection_GetObjByIndexForLabelSpace"):
		dll.Collection_GetObjByIndexForLabelSpace.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_GetObjByIndexForLabelSpace.restype = ctypes.c_void_p

	if hasattr(dll, "Collection_FillObjIndecesForLabelSpace"):
		dll.Collection_FillObjIndecesForLabelSpace.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_FillObjIndecesForLabelSpace.restype = None

	if hasattr(dll, "Collection_GetLabelScoping"):
		dll.Collection_GetLabelScoping.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_GetLabelScoping.restype = ctypes.c_void_p

	if hasattr(dll, "Collection_GetName"):
		dll.Collection_GetName.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_GetName.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "Collection_SetName"):
		dll.Collection_SetName.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_SetName.restype = None

	if hasattr(dll, "Collection_GetId"):
		dll.Collection_GetId.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_GetId.restype = ctypes.c_int32

	if hasattr(dll, "Collection_SetId"):
		dll.Collection_SetId.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_SetId.restype = None

	if hasattr(dll, "Collection_delete"):
		dll.Collection_delete.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_delete.restype = None

	if hasattr(dll, "Collection_GetSize"):
		dll.Collection_GetSize.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_GetSize.restype = ctypes.c_int32

	if hasattr(dll, "Collection_reserve"):
		dll.Collection_reserve.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_reserve.restype = None

	if hasattr(dll, "Collection_resize"):
		dll.Collection_resize.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_resize.restype = None

	if hasattr(dll, "Collection_GetSupport"):
		dll.Collection_GetSupport.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_GetSupport.restype = ctypes.c_void_p

	if hasattr(dll, "Collection_SetSupport"):
		dll.Collection_SetSupport.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_SetSupport.restype = None

	if hasattr(dll, "Collection_CreateSubCollection"):
		dll.Collection_CreateSubCollection.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_CreateSubCollection.restype = ctypes.c_void_p

	if hasattr(dll, "Collection_OfScopingNew_on_client"):
		dll.Collection_OfScopingNew_on_client.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_OfScopingNew_on_client.restype = ctypes.c_void_p

	if hasattr(dll, "Collection_OfFieldNew_on_client"):
		dll.Collection_OfFieldNew_on_client.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_OfFieldNew_on_client.restype = ctypes.c_void_p

	if hasattr(dll, "Collection_OfMeshNew_on_client"):
		dll.Collection_OfMeshNew_on_client.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_OfMeshNew_on_client.restype = ctypes.c_void_p

	if hasattr(dll, "Collection_OfAnyNew_on_client"):
		dll.Collection_OfAnyNew_on_client.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_OfAnyNew_on_client.restype = ctypes.c_void_p

	if hasattr(dll, "Collection_OfScoping_getCopy"):
		dll.Collection_OfScoping_getCopy.argtypes = (ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_OfScoping_getCopy.restype = ctypes.c_void_p

	if hasattr(dll, "Collection_OfField_getCopy"):
		dll.Collection_OfField_getCopy.argtypes = (ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_OfField_getCopy.restype = ctypes.c_void_p

	if hasattr(dll, "Collection_OfMesh_getCopy"):
		dll.Collection_OfMesh_getCopy.argtypes = (ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_OfMesh_getCopy.restype = ctypes.c_void_p

	if hasattr(dll, "Collection_OfAny_getCopy"):
		dll.Collection_OfAny_getCopy.argtypes = (ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_OfAny_getCopy.restype = ctypes.c_void_p

	if hasattr(dll, "Collection_OfIntNew_on_client"):
		dll.Collection_OfIntNew_on_client.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_OfIntNew_on_client.restype = ctypes.c_void_p

	if hasattr(dll, "Collection_OfDoubleNew_on_client"):
		dll.Collection_OfDoubleNew_on_client.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_OfDoubleNew_on_client.restype = ctypes.c_void_p

	if hasattr(dll, "Collection_OfStringNew_on_client"):
		dll.Collection_OfStringNew_on_client.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_OfStringNew_on_client.restype = ctypes.c_void_p

	if hasattr(dll, "Collection_OfStringNew_local"):
		dll.Collection_OfStringNew_local.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Collection_OfStringNew_local.restype = ctypes.c_void_p

	#-------------------------------------------------------------------------------
	# CyclicSupport
	#-------------------------------------------------------------------------------
	if hasattr(dll, "CyclicSupport_delete"):
		dll.CyclicSupport_delete.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CyclicSupport_delete.restype = None

	if hasattr(dll, "CyclicSupport_getNumSectors"):
		dll.CyclicSupport_getNumSectors.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CyclicSupport_getNumSectors.restype = ctypes.c_int32

	if hasattr(dll, "CyclicSupport_getNumStages"):
		dll.CyclicSupport_getNumStages.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CyclicSupport_getNumStages.restype = ctypes.c_int32

	if hasattr(dll, "CyclicSupport_getSectorsScoping"):
		dll.CyclicSupport_getSectorsScoping.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CyclicSupport_getSectorsScoping.restype = ctypes.c_void_p

	if hasattr(dll, "CyclicSupport_getCyclicPhase"):
		dll.CyclicSupport_getCyclicPhase.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CyclicSupport_getCyclicPhase.restype = ctypes.c_double

	if hasattr(dll, "CyclicSupport_getBaseNodesScoping"):
		dll.CyclicSupport_getBaseNodesScoping.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CyclicSupport_getBaseNodesScoping.restype = ctypes.c_void_p

	if hasattr(dll, "CyclicSupport_getBaseElementsScoping"):
		dll.CyclicSupport_getBaseElementsScoping.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CyclicSupport_getBaseElementsScoping.restype = ctypes.c_void_p

	if hasattr(dll, "CyclicSupport_getExpandedNodeIds"):
		dll.CyclicSupport_getExpandedNodeIds.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CyclicSupport_getExpandedNodeIds.restype = ctypes.c_void_p

	if hasattr(dll, "CyclicSupport_getExpandedElementIds"):
		dll.CyclicSupport_getExpandedElementIds.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CyclicSupport_getExpandedElementIds.restype = ctypes.c_void_p

	if hasattr(dll, "CyclicSupport_getCS"):
		dll.CyclicSupport_getCS.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CyclicSupport_getCS.restype = ctypes.c_void_p

	if hasattr(dll, "CyclicSupport_getLowHighMap"):
		dll.CyclicSupport_getLowHighMap.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CyclicSupport_getLowHighMap.restype = ctypes.c_void_p

	if hasattr(dll, "CyclicSupport_getHighLowMap"):
		dll.CyclicSupport_getHighLowMap.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CyclicSupport_getHighLowMap.restype = ctypes.c_void_p

	#-------------------------------------------------------------------------------
	# DataBase
	#-------------------------------------------------------------------------------
	if hasattr(dll, "DataBase_createAndHold"):
		dll.DataBase_createAndHold.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataBase_createAndHold.restype = ctypes.c_void_p

	if hasattr(dll, "DataBase_recordEntityByDbId"):
		dll.DataBase_recordEntityByDbId.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataBase_recordEntityByDbId.restype = ctypes.c_int32

	if hasattr(dll, "DataBase_recordEntity"):
		dll.DataBase_recordEntity.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataBase_recordEntity.restype = ctypes.c_int32

	if hasattr(dll, "DataBase_eraseEntity"):
		dll.DataBase_eraseEntity.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataBase_eraseEntity.restype = None

	if hasattr(dll, "DataBase_eraseEntityByDbId"):
		dll.DataBase_eraseEntityByDbId.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataBase_eraseEntityByDbId.restype = None

	if hasattr(dll, "DataBase_releaseEntity"):
		dll.DataBase_releaseEntity.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataBase_releaseEntity.restype = ctypes.c_void_p

	if hasattr(dll, "DataBase_releaseByDbId"):
		dll.DataBase_releaseByDbId.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataBase_releaseByDbId.restype = ctypes.c_void_p

	if hasattr(dll, "DataBase_getEntity"):
		dll.DataBase_getEntity.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataBase_getEntity.restype = ctypes.c_void_p

	if hasattr(dll, "DataBase_getByDbId"):
		dll.DataBase_getByDbId.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataBase_getByDbId.restype = ctypes.c_void_p

	if hasattr(dll, "DataBase_delete"):
		dll.DataBase_delete.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataBase_delete.restype = None

	if hasattr(dll, "DataBase_eraseAllHeldEntities"):
		dll.DataBase_eraseAllHeldEntities.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataBase_eraseAllHeldEntities.restype = None

	#-------------------------------------------------------------------------------
	# DataProcessing
	#-------------------------------------------------------------------------------
	if hasattr(dll, "DataProcessing_initialization"):
		dll.DataProcessing_initialization.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_initialization.restype = None

	if hasattr(dll, "DataProcessing_release"):
		dll.DataProcessing_release.argtypes = (ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_release.restype = ctypes.c_int32

	if hasattr(dll, "dataProcessing_initializeWithContext"):
		dll.dataProcessing_initializeWithContext.argtypes = (ctypes.c_int32, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.dataProcessing_initializeWithContext.restype = ctypes.c_int32

	if hasattr(dll, "dataProcessing_initializeWithContext_v2"):
		dll.dataProcessing_initializeWithContext_v2.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.dataProcessing_initializeWithContext_v2.restype = ctypes.c_int32

	if hasattr(dll, "dataProcessing_applyContext"):
		dll.dataProcessing_applyContext.argtypes = (ctypes.c_int32, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.dataProcessing_applyContext.restype = ctypes.c_int32

	if hasattr(dll, "dataProcessing_applyContext_v2"):
		dll.dataProcessing_applyContext_v2.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.dataProcessing_applyContext_v2.restype = ctypes.c_int32

	if hasattr(dll, "DataProcessing_set_debug_trace"):
		dll.DataProcessing_set_debug_trace.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_set_debug_trace.restype = None

	if hasattr(dll, "DataProcessing_set_trace_section"):
		dll.DataProcessing_set_trace_section.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_set_trace_section.restype = None

	if hasattr(dll, "DataProcessing_load_library"):
		dll.DataProcessing_load_library.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_load_library.restype = None

	if hasattr(dll, "DataProcessing_available_operators"):
		dll.DataProcessing_available_operators.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_available_operators.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "DataProcessing_duplicate_object_reference"):
		dll.DataProcessing_duplicate_object_reference.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_duplicate_object_reference.restype = ctypes.c_void_p

	if hasattr(dll, "DataProcessing_objects_holds_same_data"):
		dll.DataProcessing_objects_holds_same_data.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_objects_holds_same_data.restype = ctypes.c_bool

	if hasattr(dll, "DataProcessing_wrap_unknown"):
		dll.DataProcessing_wrap_unknown.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t, )
		dll.DataProcessing_wrap_unknown.restype = ctypes.c_void_p

	if hasattr(dll, "DataProcessing_unwrap_unknown"):
		dll.DataProcessing_unwrap_unknown.argtypes = (ctypes.c_void_p, ctypes.c_size_t, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_unwrap_unknown.restype = ctypes.c_void_p

	if hasattr(dll, "DataProcessing_delete_shared_object"):
		dll.DataProcessing_delete_shared_object.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_delete_shared_object.restype = None

	if hasattr(dll, "DataProcessing_delete_shared_object_array"):
		dll.DataProcessing_delete_shared_object_array.argtypes = (ctypes.POINTER(ctypes.c_void_p), ctypes.c_size_t, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_delete_shared_object_array.restype = None

	if hasattr(dll, "DataProcessing_unknown_has_given_hash"):
		dll.DataProcessing_unknown_has_given_hash.argtypes = (ctypes.c_void_p, ctypes.c_size_t, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_unknown_has_given_hash.restype = ctypes.c_bool

	if hasattr(dll, "DataProcessing_descriptionString"):
		dll.DataProcessing_descriptionString.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_descriptionString.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "DataProcessing_descriptionString_with_size"):
		dll.DataProcessing_descriptionString_with_size.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_descriptionString_with_size.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "DataProcessing_deleteString"):
		dll.DataProcessing_deleteString.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_deleteString.restype = None

	if hasattr(dll, "DataProcessing_String_post_event"):
		dll.DataProcessing_String_post_event.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_String_post_event.restype = None

	if hasattr(dll, "DataProcessing_list_operators_as_collection"):
		dll.DataProcessing_list_operators_as_collection.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_list_operators_as_collection.restype = ctypes.c_void_p

	if hasattr(dll, "DataProcessing_free_ints"):
		dll.DataProcessing_free_ints.argtypes = (ctypes.POINTER(ctypes.c_int32), )
		dll.DataProcessing_free_ints.restype = None

	if hasattr(dll, "DataProcessing_free_doubles"):
		dll.DataProcessing_free_doubles.argtypes = (ctypes.POINTER(ctypes.c_double), )
		dll.DataProcessing_free_doubles.restype = None

	if hasattr(dll, "DataProcessing_serialize"):
		dll.DataProcessing_serialize.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_serialize.restype = ctypes.c_void_p

	if hasattr(dll, "DataProcessing_deserialize"):
		dll.DataProcessing_deserialize.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.c_size_t, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_deserialize.restype = ctypes.c_void_p

	if hasattr(dll, "DataProcessing_deserializeMany"):
		dll.DataProcessing_deserializeMany.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.c_size_t, ctypes.POINTER(ctypes.c_size_t), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_deserializeMany.restype = ctypes.POINTER(ctypes.c_void_p)

	if hasattr(dll, "DataProcessing_getGlobalConfigAsDataTree"):
		dll.DataProcessing_getGlobalConfigAsDataTree.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_getGlobalConfigAsDataTree.restype = ctypes.c_void_p

	if hasattr(dll, "DataProcessing_getServerVersion"):
		dll.DataProcessing_getServerVersion.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_getServerVersion.restype = None

	if hasattr(dll, "DataProcessing_getOs"):
		dll.DataProcessing_getOs.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_getOs.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "DataProcessing_ProcessId"):
		dll.DataProcessing_ProcessId.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_ProcessId.restype = ctypes.c_uint64

	if hasattr(dll, "DataProcessing_create_param_tree"):
		dll.DataProcessing_create_param_tree.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_create_param_tree.restype = ctypes.c_void_p

	if hasattr(dll, "DataProcessing_logging_register_logger"):
		dll.DataProcessing_logging_register_logger.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_logging_register_logger.restype = ctypes.c_void_p

	if hasattr(dll, "DataProcessing_logging_get_logger"):
		dll.DataProcessing_logging_get_logger.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_logging_get_logger.restype = ctypes.c_void_p

	if hasattr(dll, "DataProcessing_logging_log_message"):
		dll.DataProcessing_logging_log_message.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_logging_log_message.restype = None

	if hasattr(dll, "DataProcessing_logging_flush"):
		dll.DataProcessing_logging_flush.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_logging_flush.restype = None

	if hasattr(dll, "DataProcessing_logging_flush_all"):
		dll.DataProcessing_logging_flush_all.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_logging_flush_all.restype = None

	if hasattr(dll, "DataProcessing_initialization_on_client"):
		dll.DataProcessing_initialization_on_client.argtypes = (ctypes.c_void_p, )
		dll.DataProcessing_initialization_on_client.restype = None

	if hasattr(dll, "DataProcessing_release_on_client"):
		dll.DataProcessing_release_on_client.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_release_on_client.restype = ctypes.c_int32

	if hasattr(dll, "dataProcessing_initializeWithContext_on_client"):
		dll.dataProcessing_initializeWithContext_on_client.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.dataProcessing_initializeWithContext_on_client.restype = ctypes.c_int32

	if hasattr(dll, "dataProcessing_applyContext_on_client"):
		dll.dataProcessing_applyContext_on_client.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.dataProcessing_applyContext_on_client.restype = ctypes.c_int32

	if hasattr(dll, "dataProcessing_applyContext_v2_on_client"):
		dll.dataProcessing_applyContext_v2_on_client.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.dataProcessing_applyContext_v2_on_client.restype = ctypes.c_int32

	if hasattr(dll, "DataProcessing_load_library_on_client"):
		dll.DataProcessing_load_library_on_client.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_load_library_on_client.restype = None

	if hasattr(dll, "DataProcessing_get_id_of_duplicate_object_reference"):
		dll.DataProcessing_get_id_of_duplicate_object_reference.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_get_id_of_duplicate_object_reference.restype = ctypes.c_int32

	if hasattr(dll, "DataProcessing_release_obj_by_id_in_db"):
		dll.DataProcessing_release_obj_by_id_in_db.argtypes = (ctypes.c_int32, ctypes.c_void_p, ctypes.c_bool, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_release_obj_by_id_in_db.restype = None

	if hasattr(dll, "DataProcessing_deleteString_for_object"):
		dll.DataProcessing_deleteString_for_object.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_deleteString_for_object.restype = None

	if hasattr(dll, "DataProcessing_get_client"):
		dll.DataProcessing_get_client.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_get_client.restype = ctypes.c_void_p

	if hasattr(dll, "DataProcessing_prepare_shutdown"):
		dll.DataProcessing_prepare_shutdown.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_prepare_shutdown.restype = None

	if hasattr(dll, "DataProcessing_release_server"):
		dll.DataProcessing_release_server.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_release_server.restype = None

	if hasattr(dll, "DataProcessing_String_post_event_for_object"):
		dll.DataProcessing_String_post_event_for_object.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_String_post_event_for_object.restype = None

	if hasattr(dll, "DataProcessing_free_ints_for_object"):
		dll.DataProcessing_free_ints_for_object.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), )
		dll.DataProcessing_free_ints_for_object.restype = None

	if hasattr(dll, "DataProcessing_free_doubles_for_object"):
		dll.DataProcessing_free_doubles_for_object.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_double), )
		dll.DataProcessing_free_doubles_for_object.restype = None

	if hasattr(dll, "DataProcessing_deserialize_on_client"):
		dll.DataProcessing_deserialize_on_client.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_size_t, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_deserialize_on_client.restype = ctypes.c_void_p

	if hasattr(dll, "DataProcessing_getGlobalConfigAsDataTree_on_client"):
		dll.DataProcessing_getGlobalConfigAsDataTree_on_client.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_getGlobalConfigAsDataTree_on_client.restype = ctypes.c_void_p

	if hasattr(dll, "DataProcessing_getClientConfigAsDataTree"):
		dll.DataProcessing_getClientConfigAsDataTree.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_getClientConfigAsDataTree.restype = ctypes.c_void_p

	if hasattr(dll, "DataProcessing_getServerVersion_on_client"):
		dll.DataProcessing_getServerVersion_on_client.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_getServerVersion_on_client.restype = None

	if hasattr(dll, "DataProcessing_getServerIpAndPort"):
		dll.DataProcessing_getServerIpAndPort.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_getServerIpAndPort.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "DataProcessing_getOs_on_client"):
		dll.DataProcessing_getOs_on_client.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_getOs_on_client.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "DataProcessing_DownloadFile"):
		dll.DataProcessing_DownloadFile.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_DownloadFile.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "DataProcessing_DownloadFiles"):
		dll.DataProcessing_DownloadFiles.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_DownloadFiles.restype = ctypes.c_void_p

	if hasattr(dll, "DataProcessing_list_operators_as_collection_on_client"):
		dll.DataProcessing_list_operators_as_collection_on_client.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_list_operators_as_collection_on_client.restype = ctypes.c_void_p

	if hasattr(dll, "DataProcessing_UploadFile"):
		dll.DataProcessing_UploadFile.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.c_bool, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_UploadFile.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "DataProcessing_ProcessId_on_client"):
		dll.DataProcessing_ProcessId_on_client.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_ProcessId_on_client.restype = ctypes.c_uint64

	if hasattr(dll, "DataProcessing_create_param_tree_on_client"):
		dll.DataProcessing_create_param_tree_on_client.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_create_param_tree_on_client.restype = ctypes.c_void_p

	if hasattr(dll, "DataProcessing_create_from_on_client"):
		dll.DataProcessing_create_from_on_client.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataProcessing_create_from_on_client.restype = ctypes.c_void_p

	#-------------------------------------------------------------------------------
	# DataProcessingError
	#-------------------------------------------------------------------------------
	if hasattr(dll, "DataProcessing_parse_error"):
		dll.DataProcessing_parse_error.argtypes = (ctypes.c_int32, ctypes.c_wchar_p, )
		dll.DataProcessing_parse_error.restype = ctypes.c_void_p

	if hasattr(dll, "DataProcessing_parse_error_to_str"):
		dll.DataProcessing_parse_error_to_str.argtypes = (ctypes.c_int32, ctypes.c_wchar_p, )
		dll.DataProcessing_parse_error_to_str.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "DpfError_new"):
		dll.DpfError_new.argtypes = None
		dll.DpfError_new.restype = ctypes.c_void_p

	if hasattr(dll, "DpfError_set_throw"):
		dll.DpfError_set_throw.argtypes = (ctypes.c_void_p, ctypes.c_bool, )
		dll.DpfError_set_throw.restype = None

	if hasattr(dll, "DpfError_set_code"):
		dll.DpfError_set_code.argtypes = (ctypes.c_void_p, ctypes.c_int32, )
		dll.DpfError_set_code.restype = None

	if hasattr(dll, "DpfError_set_message_text"):
		dll.DpfError_set_message_text.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), )
		dll.DpfError_set_message_text.restype = None

	if hasattr(dll, "DpfError_set_message_template"):
		dll.DpfError_set_message_template.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), )
		dll.DpfError_set_message_template.restype = None

	if hasattr(dll, "DpfError_set_message_id"):
		dll.DpfError_set_message_id.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), )
		dll.DpfError_set_message_id.restype = None

	if hasattr(dll, "DpfError_delete"):
		dll.DpfError_delete.argtypes = (ctypes.c_void_p, )
		dll.DpfError_delete.restype = None

	if hasattr(dll, "DpfError_duplicate"):
		dll.DpfError_duplicate.argtypes = (ctypes.c_void_p, )
		dll.DpfError_duplicate.restype = ctypes.c_void_p

	if hasattr(dll, "DpfError_code"):
		dll.DpfError_code.argtypes = (ctypes.c_void_p, )
		dll.DpfError_code.restype = ctypes.c_int32

	if hasattr(dll, "DpfError_to_throw"):
		dll.DpfError_to_throw.argtypes = (ctypes.c_void_p, )
		dll.DpfError_to_throw.restype = ctypes.c_bool

	if hasattr(dll, "DpfError_message_text"):
		dll.DpfError_message_text.argtypes = (ctypes.c_void_p, )
		dll.DpfError_message_text.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "DpfError_message_template"):
		dll.DpfError_message_template.argtypes = (ctypes.c_void_p, )
		dll.DpfError_message_template.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "DpfError_message_id"):
		dll.DpfError_message_id.argtypes = (ctypes.c_void_p, )
		dll.DpfError_message_id.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "DataProcessing_parse_error_to_str_for_object"):
		dll.DataProcessing_parse_error_to_str_for_object.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_wchar_p, )
		dll.DataProcessing_parse_error_to_str_for_object.restype = ctypes.POINTER(ctypes.c_char)

	#-------------------------------------------------------------------------------
	# DataSources
	#-------------------------------------------------------------------------------
	if hasattr(dll, "DataSources_new"):
		dll.DataSources_new.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataSources_new.restype = ctypes.c_void_p

	if hasattr(dll, "DataSources_delete"):
		dll.DataSources_delete.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataSources_delete.restype = None

	if hasattr(dll, "DataSources_SetResultFilePath"):
		dll.DataSources_SetResultFilePath.argtypes = (ctypes.c_void_p, ctypes.c_wchar_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataSources_SetResultFilePath.restype = None

	if hasattr(dll, "DataSources_SetResultFilePathWithKey"):
		dll.DataSources_SetResultFilePathWithKey.argtypes = (ctypes.c_void_p, ctypes.c_wchar_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataSources_SetResultFilePathWithKey.restype = None

	if hasattr(dll, "DataSources_SetDomainResultFilePathWithKey"):
		dll.DataSources_SetDomainResultFilePathWithKey.argtypes = (ctypes.c_void_p, ctypes.c_wchar_p, ctypes.POINTER(ctypes.c_char), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataSources_SetDomainResultFilePathWithKey.restype = None

	if hasattr(dll, "DataSources_AddFilePath"):
		dll.DataSources_AddFilePath.argtypes = (ctypes.c_void_p, ctypes.c_wchar_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataSources_AddFilePath.restype = None

	if hasattr(dll, "DataSources_AddFilePathWithKey"):
		dll.DataSources_AddFilePathWithKey.argtypes = (ctypes.c_void_p, ctypes.c_wchar_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataSources_AddFilePathWithKey.restype = None

	if hasattr(dll, "DataSources_AddFilePathForSpecifiedResult"):
		dll.DataSources_AddFilePathForSpecifiedResult.argtypes = (ctypes.c_void_p, ctypes.c_wchar_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataSources_AddFilePathForSpecifiedResult.restype = None

	if hasattr(dll, "DataSources_SetResultFilePathUtf8"):
		dll.DataSources_SetResultFilePathUtf8.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataSources_SetResultFilePathUtf8.restype = None

	if hasattr(dll, "DataSources_SetResultFilePathWithKeyUtf8"):
		dll.DataSources_SetResultFilePathWithKeyUtf8.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataSources_SetResultFilePathWithKeyUtf8.restype = None

	if hasattr(dll, "DataSources_SetDomainResultFilePathUtf8"):
		dll.DataSources_SetDomainResultFilePathUtf8.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataSources_SetDomainResultFilePathUtf8.restype = None

	if hasattr(dll, "DataSources_SetDomainResultFilePathWithKeyUtf8"):
		dll.DataSources_SetDomainResultFilePathWithKeyUtf8.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataSources_SetDomainResultFilePathWithKeyUtf8.restype = None

	if hasattr(dll, "DataSources_AddFilePathUtf8"):
		dll.DataSources_AddFilePathUtf8.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataSources_AddFilePathUtf8.restype = None

	if hasattr(dll, "DataSources_AddFilePathWithKeyUtf8"):
		dll.DataSources_AddFilePathWithKeyUtf8.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataSources_AddFilePathWithKeyUtf8.restype = None

	if hasattr(dll, "DataSources_AddDomainFilePathWithKeyUtf8"):
		dll.DataSources_AddDomainFilePathWithKeyUtf8.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataSources_AddDomainFilePathWithKeyUtf8.restype = None

	if hasattr(dll, "DataSources_AddFilePathForSpecifiedResultUtf8"):
		dll.DataSources_AddFilePathForSpecifiedResultUtf8.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataSources_AddFilePathForSpecifiedResultUtf8.restype = None

	if hasattr(dll, "DataSources_AddUpstreamDataSources"):
		dll.DataSources_AddUpstreamDataSources.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataSources_AddUpstreamDataSources.restype = None

	if hasattr(dll, "DataSources_AddUpstreamDataSourcesForSpecifiedResult"):
		dll.DataSources_AddUpstreamDataSourcesForSpecifiedResult.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataSources_AddUpstreamDataSourcesForSpecifiedResult.restype = None

	if hasattr(dll, "DataSources_AddUpstreamDomainDataSources"):
		dll.DataSources_AddUpstreamDomainDataSources.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataSources_AddUpstreamDomainDataSources.restype = None

	if hasattr(dll, "DataSources_GetResultKey"):
		dll.DataSources_GetResultKey.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataSources_GetResultKey.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "DataSources_GetResultKeyByIndex"):
		dll.DataSources_GetResultKeyByIndex.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataSources_GetResultKeyByIndex.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "DataSources_GetNumResultKeys"):
		dll.DataSources_GetNumResultKeys.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataSources_GetNumResultKeys.restype = ctypes.c_int32

	if hasattr(dll, "DataSources_GetNumKeys"):
		dll.DataSources_GetNumKeys.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataSources_GetNumKeys.restype = ctypes.c_int32

	if hasattr(dll, "DataSources_GetKey"):
		dll.DataSources_GetKey.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataSources_GetKey.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "DataSources_GetPath"):
		dll.DataSources_GetPath.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataSources_GetPath.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "DataSources_GetNamespace"):
		dll.DataSources_GetNamespace.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataSources_GetNamespace.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "DataSources_GetNewPathCollectionForKey"):
		dll.DataSources_GetNewPathCollectionForKey.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataSources_GetNewPathCollectionForKey.restype = ctypes.c_void_p

	if hasattr(dll, "DataSources_GetNewCollectionForResultsPath"):
		dll.DataSources_GetNewCollectionForResultsPath.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataSources_GetNewCollectionForResultsPath.restype = ctypes.c_void_p

	if hasattr(dll, "DataSources_GetSize"):
		dll.DataSources_GetSize.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataSources_GetSize.restype = ctypes.c_int32

	if hasattr(dll, "DataSources_GetPathByPathIndex"):
		dll.DataSources_GetPathByPathIndex.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataSources_GetPathByPathIndex.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "DataSources_GetKeyByPathIndex"):
		dll.DataSources_GetKeyByPathIndex.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataSources_GetKeyByPathIndex.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "DataSources_GetLabelSpaceByPathIndex"):
		dll.DataSources_GetLabelSpaceByPathIndex.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataSources_GetLabelSpaceByPathIndex.restype = ctypes.c_void_p

	if hasattr(dll, "DataSources_RegisterNamespace"):
		dll.DataSources_RegisterNamespace.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataSources_RegisterNamespace.restype = None

	if hasattr(dll, "DataSources_new_on_client"):
		dll.DataSources_new_on_client.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataSources_new_on_client.restype = ctypes.c_void_p

	if hasattr(dll, "DataSources_getCopy"):
		dll.DataSources_getCopy.argtypes = (ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DataSources_getCopy.restype = ctypes.c_void_p

	#-------------------------------------------------------------------------------
	# DpfDataTree
	#-------------------------------------------------------------------------------
	if hasattr(dll, "DpfDataTree_new"):
		dll.DpfDataTree_new.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfDataTree_new.restype = ctypes.c_void_p

	if hasattr(dll, "DpfDataTree_delete"):
		dll.DpfDataTree_delete.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfDataTree_delete.restype = None

	if hasattr(dll, "DpfDataTree_hasSubTree"):
		dll.DpfDataTree_hasSubTree.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfDataTree_hasSubTree.restype = ctypes.c_bool

	if hasattr(dll, "DpfDataTree_getSubTree"):
		dll.DpfDataTree_getSubTree.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfDataTree_getSubTree.restype = ctypes.c_void_p

	if hasattr(dll, "DpfDataTree_makeSubTree"):
		dll.DpfDataTree_makeSubTree.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfDataTree_makeSubTree.restype = ctypes.c_void_p

	if hasattr(dll, "DpfDataTree_hasAttribute"):
		dll.DpfDataTree_hasAttribute.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfDataTree_hasAttribute.restype = ctypes.c_bool

	if hasattr(dll, "DpfDataTree_getAvailableAttributesNamesInStringCollection"):
		dll.DpfDataTree_getAvailableAttributesNamesInStringCollection.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfDataTree_getAvailableAttributesNamesInStringCollection.restype = ctypes.c_void_p

	if hasattr(dll, "DpfDataTree_getAvailableSubTreeNamesInStringCollection"):
		dll.DpfDataTree_getAvailableSubTreeNamesInStringCollection.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfDataTree_getAvailableSubTreeNamesInStringCollection.restype = ctypes.c_void_p

	if hasattr(dll, "DpfDataTree_getIntAttribute"):
		dll.DpfDataTree_getIntAttribute.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfDataTree_getIntAttribute.restype = None

	if hasattr(dll, "DpfDataTree_getUnsignedIntAttribute"):
		dll.DpfDataTree_getUnsignedIntAttribute.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfDataTree_getUnsignedIntAttribute.restype = None

	if hasattr(dll, "DpfDataTree_getDoubleAttribute"):
		dll.DpfDataTree_getDoubleAttribute.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfDataTree_getDoubleAttribute.restype = None

	if hasattr(dll, "DpfDataTree_getStringAttribute"):
		dll.DpfDataTree_getStringAttribute.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.POINTER(ctypes.c_char)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfDataTree_getStringAttribute.restype = None

	if hasattr(dll, "DpfDataTree_getVecIntAttribute"):
		dll.DpfDataTree_getVecIntAttribute.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.POINTER(ctypes.c_int32)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfDataTree_getVecIntAttribute.restype = None

	if hasattr(dll, "DpfDataTree_getVecDoubleAttribute"):
		dll.DpfDataTree_getVecDoubleAttribute.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.POINTER(ctypes.c_double)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfDataTree_getVecDoubleAttribute.restype = None

	if hasattr(dll, "DpfDataTree_getIntAttributeWithCheck"):
		dll.DpfDataTree_getIntAttributeWithCheck.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfDataTree_getIntAttributeWithCheck.restype = None

	if hasattr(dll, "DpfDataTree_getUnsignedIntAttributeWithCheck"):
		dll.DpfDataTree_getUnsignedIntAttributeWithCheck.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfDataTree_getUnsignedIntAttributeWithCheck.restype = None

	if hasattr(dll, "DpfDataTree_getDoubleAttributeWithCheck"):
		dll.DpfDataTree_getDoubleAttributeWithCheck.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfDataTree_getDoubleAttributeWithCheck.restype = None

	if hasattr(dll, "DpfDataTree_getStringAttributeWithCheck"):
		dll.DpfDataTree_getStringAttributeWithCheck.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.POINTER(ctypes.c_char)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfDataTree_getStringAttributeWithCheck.restype = None

	if hasattr(dll, "DpfDataTree_getVecIntAttributeWithCheck"):
		dll.DpfDataTree_getVecIntAttributeWithCheck.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.POINTER(ctypes.c_int32)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfDataTree_getVecIntAttributeWithCheck.restype = None

	if hasattr(dll, "DpfDataTree_getVecDoubleAttributeWithCheck"):
		dll.DpfDataTree_getVecDoubleAttributeWithCheck.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.POINTER(ctypes.c_double)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfDataTree_getVecDoubleAttributeWithCheck.restype = None

	if hasattr(dll, "DpfDataTree_getStringCollectionAttribute"):
		dll.DpfDataTree_getStringCollectionAttribute.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfDataTree_getStringCollectionAttribute.restype = ctypes.c_void_p

	if hasattr(dll, "DpfDataTree_getStringCollectionAttributeWithCheck"):
		dll.DpfDataTree_getStringCollectionAttributeWithCheck.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfDataTree_getStringCollectionAttributeWithCheck.restype = ctypes.c_void_p

	if hasattr(dll, "DpfDataTree_setIntAttribute"):
		dll.DpfDataTree_setIntAttribute.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfDataTree_setIntAttribute.restype = None

	if hasattr(dll, "DpfDataTree_setUnsignedIntAttribute"):
		dll.DpfDataTree_setUnsignedIntAttribute.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfDataTree_setUnsignedIntAttribute.restype = None

	if hasattr(dll, "DpfDataTree_setVecIntAttribute"):
		dll.DpfDataTree_setVecIntAttribute.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfDataTree_setVecIntAttribute.restype = None

	if hasattr(dll, "DpfDataTree_setDoubleAttribute"):
		dll.DpfDataTree_setDoubleAttribute.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_double, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfDataTree_setDoubleAttribute.restype = None

	if hasattr(dll, "DpfDataTree_setVecDoubleAttribute"):
		dll.DpfDataTree_setVecDoubleAttribute.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_double), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfDataTree_setVecDoubleAttribute.restype = None

	if hasattr(dll, "DpfDataTree_setStringCollectionAttribute"):
		dll.DpfDataTree_setStringCollectionAttribute.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfDataTree_setStringCollectionAttribute.restype = None

	if hasattr(dll, "DpfDataTree_setStringAttribute"):
		dll.DpfDataTree_setStringAttribute.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfDataTree_setStringAttribute.restype = None

	if hasattr(dll, "DpfDataTree_setSubTreeAttribute"):
		dll.DpfDataTree_setSubTreeAttribute.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfDataTree_setSubTreeAttribute.restype = None

	if hasattr(dll, "DpfDataTree_saveToTxt"):
		dll.DpfDataTree_saveToTxt.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.POINTER(ctypes.c_char)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfDataTree_saveToTxt.restype = None

	if hasattr(dll, "DpfDataTree_readFromText"):
		dll.DpfDataTree_readFromText.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfDataTree_readFromText.restype = None

	if hasattr(dll, "DpfDataTree_saveToJson"):
		dll.DpfDataTree_saveToJson.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.POINTER(ctypes.c_char)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfDataTree_saveToJson.restype = None

	if hasattr(dll, "DpfDataTree_readFromJson"):
		dll.DpfDataTree_readFromJson.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfDataTree_readFromJson.restype = None

	if hasattr(dll, "DpfDataTree_new_on_client"):
		dll.DpfDataTree_new_on_client.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfDataTree_new_on_client.restype = ctypes.c_void_p

	#-------------------------------------------------------------------------------
	# DpfVector
	#-------------------------------------------------------------------------------
	if hasattr(dll, "DpfVector_new"):
		dll.DpfVector_new.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfVector_new.restype = ctypes.c_void_p

	if hasattr(dll, "DpfVector_double_free"):
		dll.DpfVector_double_free.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.POINTER(ctypes.c_double)), ctypes.POINTER(ctypes.c_int32), ctypes.c_bool, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfVector_double_free.restype = None

	if hasattr(dll, "DpfVector_char_free"):
		dll.DpfVector_char_free.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.POINTER(ctypes.c_char)), ctypes.POINTER(ctypes.c_int32), ctypes.c_bool, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfVector_char_free.restype = None

	if hasattr(dll, "DpfVector_int_free"):
		dll.DpfVector_int_free.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.POINTER(ctypes.c_int32)), ctypes.POINTER(ctypes.c_int32), ctypes.c_bool, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfVector_int_free.restype = None

	if hasattr(dll, "DpfVector_char_ptr_free_with_size"):
		dll.DpfVector_char_ptr_free_with_size.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.POINTER(ctypes.POINTER(ctypes.c_char))), ctypes.POINTER(ctypes.POINTER(ctypes.c_uint64)), ctypes.POINTER(ctypes.c_int32), ctypes.c_bool, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfVector_char_ptr_free_with_size.restype = None

	if hasattr(dll, "DpfVector_char_ptr_free_for_next_usage_with_size"):
		dll.DpfVector_char_ptr_free_for_next_usage_with_size.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.POINTER(ctypes.POINTER(ctypes.c_char))), ctypes.POINTER(ctypes.POINTER(ctypes.c_uint64)), ctypes.POINTER(ctypes.c_int32), ctypes.c_bool, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfVector_char_ptr_free_for_next_usage_with_size.restype = None

	if hasattr(dll, "DpfVector_char_ptr_free"):
		dll.DpfVector_char_ptr_free.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.POINTER(ctypes.POINTER(ctypes.c_char))), ctypes.POINTER(ctypes.c_int32), ctypes.c_bool, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfVector_char_ptr_free.restype = None

	if hasattr(dll, "DpfVector_char_ptr_free_for_next_usage"):
		dll.DpfVector_char_ptr_free_for_next_usage.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.POINTER(ctypes.POINTER(ctypes.c_char))), ctypes.POINTER(ctypes.c_int32), ctypes.c_bool, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfVector_char_ptr_free_for_next_usage.restype = None

	if hasattr(dll, "DpfVector_double_commit"):
		dll.DpfVector_double_commit.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_double), ctypes.c_int32, ctypes.c_bool, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfVector_double_commit.restype = None

	if hasattr(dll, "DpfVector_int_commit"):
		dll.DpfVector_int_commit.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.c_int32, ctypes.c_bool, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfVector_int_commit.restype = None

	if hasattr(dll, "DpfVector_char_commit"):
		dll.DpfVector_char_commit.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_int32, ctypes.c_bool, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfVector_char_commit.restype = None

	if hasattr(dll, "DpfVector_char_ptr_commit"):
		dll.DpfVector_char_ptr_commit.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.POINTER(ctypes.c_char)), ctypes.c_int32, ctypes.c_bool, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfVector_char_ptr_commit.restype = None

	if hasattr(dll, "DpfVector_char_ptr_commit_with_size"):
		dll.DpfVector_char_ptr_commit_with_size.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.POINTER(ctypes.c_char)), ctypes.POINTER(ctypes.c_uint64), ctypes.c_int32, ctypes.c_bool, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfVector_char_ptr_commit_with_size.restype = None

	if hasattr(dll, "DpfVector_delete"):
		dll.DpfVector_delete.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfVector_delete.restype = None

	if hasattr(dll, "DpfString_free"):
		dll.DpfString_free.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfString_free.restype = None

	if hasattr(dll, "DpfVector_duplicate_dpf_vector"):
		dll.DpfVector_duplicate_dpf_vector.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfVector_duplicate_dpf_vector.restype = ctypes.c_void_p

	if hasattr(dll, "DpfVector_double_extract_sub"):
		dll.DpfVector_double_extract_sub.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_double), ctypes.c_int32, ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.POINTER(ctypes.c_double)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfVector_double_extract_sub.restype = None

	if hasattr(dll, "DpfVector_int_extract_sub"):
		dll.DpfVector_int_extract_sub.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.c_int32, ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.POINTER(ctypes.c_int32)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfVector_int_extract_sub.restype = None

	if hasattr(dll, "DpfVector_char_extract_sub"):
		dll.DpfVector_char_extract_sub.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_int32, ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.POINTER(ctypes.c_char)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfVector_char_extract_sub.restype = None

	if hasattr(dll, "DpfVector_new_for_object"):
		dll.DpfVector_new_for_object.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfVector_new_for_object.restype = ctypes.c_void_p

	if hasattr(dll, "DpfString_free_for_object"):
		dll.DpfString_free_for_object.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.DpfString_free_for_object.restype = None

	#-------------------------------------------------------------------------------
	# ExternalData
	#-------------------------------------------------------------------------------
	if hasattr(dll, "ExternalData_wrap"):
		dll.ExternalData_wrap.argtypes = (ctypes.c_void_p, ctypes.c_void_p, )
		dll.ExternalData_wrap.restype = ctypes.c_void_p

	if hasattr(dll, "ExternalData_free"):
		dll.ExternalData_free.argtypes = (ctypes.c_void_p, )
		dll.ExternalData_free.restype = None

	if hasattr(dll, "ExternalData_get"):
		dll.ExternalData_get.argtypes = (ctypes.c_void_p, )
		dll.ExternalData_get.restype = ctypes.c_void_p

	#-------------------------------------------------------------------------------
	# ExternalOperator
	#-------------------------------------------------------------------------------
	if hasattr(dll, "ExternalOperator_record"):
		dll.ExternalOperator_record.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_record.restype = None

	if hasattr(dll, "ExternalOperator_record_with_derivative"):
		dll.ExternalOperator_record_with_derivative.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_record_with_derivative.restype = None

	if hasattr(dll, "ExternalOperator_recordWithAbstractCore"):
		dll.ExternalOperator_recordWithAbstractCore.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_recordWithAbstractCore.restype = None

	if hasattr(dll, "ExternalOperator_recordWithAbstractCore_with_derivative"):
		dll.ExternalOperator_recordWithAbstractCore_with_derivative.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_recordWithAbstractCore_with_derivative.restype = None

	if hasattr(dll, "ExternalOperator_recordInternalWithAbstractCore"):
		dll.ExternalOperator_recordInternalWithAbstractCore.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_recordInternalWithAbstractCore.restype = None

	if hasattr(dll, "ExternalOperator_recordInternalWithAbstractCore_with_derivative"):
		dll.ExternalOperator_recordInternalWithAbstractCore_with_derivative.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_recordInternalWithAbstractCore_with_derivative.restype = None

	if hasattr(dll, "ExternalOperator_recordWithAbstractCoreAndWrapper"):
		dll.ExternalOperator_recordWithAbstractCoreAndWrapper.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_recordWithAbstractCoreAndWrapper.restype = None

	if hasattr(dll, "ExternalOperator_recordWithAbstractCoreAndWrapper_with_derivative"):
		dll.ExternalOperator_recordWithAbstractCoreAndWrapper_with_derivative.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_recordWithAbstractCoreAndWrapper_with_derivative.restype = None

	if hasattr(dll, "ExternalOperator_putStatus"):
		dll.ExternalOperator_putStatus.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_putStatus.restype = None

	if hasattr(dll, "ExternalOperator_putException"):
		dll.ExternalOperator_putException.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_char), )
		dll.ExternalOperator_putException.restype = None

	if hasattr(dll, "ExternalOperator_putOutCollection"):
		dll.ExternalOperator_putOutCollection.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_putOutCollection.restype = None

	if hasattr(dll, "ExternalOperator_getNumInputs"):
		dll.ExternalOperator_getNumInputs.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_getNumInputs.restype = ctypes.c_int32

	if hasattr(dll, "ExternalOperator_hasInput"):
		dll.ExternalOperator_hasInput.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_hasInput.restype = ctypes.c_bool

	if hasattr(dll, "ExternalOperator_getInField"):
		dll.ExternalOperator_getInField.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_getInField.restype = ctypes.c_void_p

	if hasattr(dll, "ExternalOperator_putOutField"):
		dll.ExternalOperator_putOutField.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_putOutField.restype = None

	if hasattr(dll, "ExternalOperator_getInFieldsContainer"):
		dll.ExternalOperator_getInFieldsContainer.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_getInFieldsContainer.restype = ctypes.c_void_p

	if hasattr(dll, "ExternalOperator_getInDataSources"):
		dll.ExternalOperator_getInDataSources.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_getInDataSources.restype = ctypes.c_void_p

	if hasattr(dll, "ExternalOperator_putOutDataSources"):
		dll.ExternalOperator_putOutDataSources.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_putOutDataSources.restype = None

	if hasattr(dll, "ExternalOperator_getInScoping"):
		dll.ExternalOperator_getInScoping.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_getInScoping.restype = ctypes.c_void_p

	if hasattr(dll, "ExternalOperator_putOutScoping"):
		dll.ExternalOperator_putOutScoping.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_putOutScoping.restype = None

	if hasattr(dll, "ExternalOperator_getInScopingsContainer"):
		dll.ExternalOperator_getInScopingsContainer.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_getInScopingsContainer.restype = ctypes.c_void_p

	if hasattr(dll, "ExternalOperator_getInMeshedRegion"):
		dll.ExternalOperator_getInMeshedRegion.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_getInMeshedRegion.restype = ctypes.c_void_p

	if hasattr(dll, "ExternalOperator_putOutMeshedRegion"):
		dll.ExternalOperator_putOutMeshedRegion.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_putOutMeshedRegion.restype = None

	if hasattr(dll, "ExternalOperator_getInTimeFreq"):
		dll.ExternalOperator_getInTimeFreq.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_getInTimeFreq.restype = ctypes.c_void_p

	if hasattr(dll, "ExternalOperator_putOutTimeFreq"):
		dll.ExternalOperator_putOutTimeFreq.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_putOutTimeFreq.restype = None

	if hasattr(dll, "ExternalOperator_getInMeshesContainer"):
		dll.ExternalOperator_getInMeshesContainer.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_getInMeshesContainer.restype = ctypes.c_void_p

	if hasattr(dll, "ExternalOperator_getInCustomTypeFieldsContainer"):
		dll.ExternalOperator_getInCustomTypeFieldsContainer.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_getInCustomTypeFieldsContainer.restype = ctypes.c_void_p

	if hasattr(dll, "ExternalOperator_getInStreams"):
		dll.ExternalOperator_getInStreams.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_getInStreams.restype = ctypes.c_void_p

	if hasattr(dll, "ExternalOperator_putOutStreams"):
		dll.ExternalOperator_putOutStreams.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_putOutStreams.restype = None

	if hasattr(dll, "ExternalOperator_getInPropertyField"):
		dll.ExternalOperator_getInPropertyField.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_getInPropertyField.restype = ctypes.c_void_p

	if hasattr(dll, "ExternalOperator_getInGenericDataContainer"):
		dll.ExternalOperator_getInGenericDataContainer.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_getInGenericDataContainer.restype = ctypes.c_void_p

	if hasattr(dll, "ExternalOperator_putOutPropertyField"):
		dll.ExternalOperator_putOutPropertyField.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_putOutPropertyField.restype = None

	if hasattr(dll, "ExternalOperator_getInSupport"):
		dll.ExternalOperator_getInSupport.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_getInSupport.restype = ctypes.c_void_p

	if hasattr(dll, "ExternalOperator_getInDataTree"):
		dll.ExternalOperator_getInDataTree.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_getInDataTree.restype = ctypes.c_void_p

	if hasattr(dll, "ExternalOperator_getInWorkflow"):
		dll.ExternalOperator_getInWorkflow.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_getInWorkflow.restype = ctypes.c_void_p

	if hasattr(dll, "ExternalOperator_getInOperator"):
		dll.ExternalOperator_getInOperator.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_getInOperator.restype = ctypes.c_void_p

	if hasattr(dll, "ExternalOperator_getInExternalData"):
		dll.ExternalOperator_getInExternalData.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_getInExternalData.restype = ctypes.c_void_p

	if hasattr(dll, "ExternalOperator_getInAsAny"):
		dll.ExternalOperator_getInAsAny.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_getInAsAny.restype = ctypes.c_void_p

	if hasattr(dll, "ExternalOperator_getInRemoteWorkflow"):
		dll.ExternalOperator_getInRemoteWorkflow.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_getInRemoteWorkflow.restype = ctypes.c_void_p

	if hasattr(dll, "ExternalOperator_getInRemoteOperator"):
		dll.ExternalOperator_getInRemoteOperator.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_getInRemoteOperator.restype = ctypes.c_void_p

	if hasattr(dll, "ExternalOperator_getInStringField"):
		dll.ExternalOperator_getInStringField.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_getInStringField.restype = ctypes.c_void_p

	if hasattr(dll, "ExternalOperator_getInCustomTypeField"):
		dll.ExternalOperator_getInCustomTypeField.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_getInCustomTypeField.restype = ctypes.c_void_p

	if hasattr(dll, "ExternalOperator_getInLabelSpace"):
		dll.ExternalOperator_getInLabelSpace.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_getInLabelSpace.restype = ctypes.c_void_p

	if hasattr(dll, "ExternalOperator_putOutRemoteWorkflow"):
		dll.ExternalOperator_putOutRemoteWorkflow.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_putOutRemoteWorkflow.restype = None

	if hasattr(dll, "ExternalOperator_putOutOperator"):
		dll.ExternalOperator_putOutOperator.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_putOutOperator.restype = None

	if hasattr(dll, "ExternalOperator_putOutSupport"):
		dll.ExternalOperator_putOutSupport.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_putOutSupport.restype = None

	if hasattr(dll, "ExternalOperator_putOutAsAny"):
		dll.ExternalOperator_putOutAsAny.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_putOutAsAny.restype = None

	if hasattr(dll, "ExternalOperator_getInBool"):
		dll.ExternalOperator_getInBool.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_getInBool.restype = ctypes.c_bool

	if hasattr(dll, "ExternalOperator_putOutBool"):
		dll.ExternalOperator_putOutBool.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_bool, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_putOutBool.restype = None

	if hasattr(dll, "ExternalOperator_getInInt"):
		dll.ExternalOperator_getInInt.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_getInInt.restype = ctypes.c_int32

	if hasattr(dll, "ExternalOperator_putOutInt"):
		dll.ExternalOperator_putOutInt.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_putOutInt.restype = None

	if hasattr(dll, "ExternalOperator_getInDouble"):
		dll.ExternalOperator_getInDouble.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_getInDouble.restype = ctypes.c_double

	if hasattr(dll, "ExternalOperator_putOutDouble"):
		dll.ExternalOperator_putOutDouble.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_double, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_putOutDouble.restype = None

	if hasattr(dll, "ExternalOperator_getInLongLong"):
		dll.ExternalOperator_getInLongLong.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_getInLongLong.restype = ctypes.c_uint64

	if hasattr(dll, "ExternalOperator_putOutLongLong"):
		dll.ExternalOperator_putOutLongLong.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_uint64, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_putOutLongLong.restype = None

	if hasattr(dll, "ExternalOperator_getInString"):
		dll.ExternalOperator_getInString.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_getInString.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "ExternalOperator_putOutString"):
		dll.ExternalOperator_putOutString.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_putOutString.restype = None

	if hasattr(dll, "ExternalOperator_getInString_with_size"):
		dll.ExternalOperator_getInString_with_size.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_getInString_with_size.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "ExternalOperator_putOutString_with_size"):
		dll.ExternalOperator_putOutString_with_size.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_char), ctypes.c_uint64, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_putOutString_with_size.restype = None

	if hasattr(dll, "ExternalOperator_getInVecInt"):
		dll.ExternalOperator_getInVecInt.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_getInVecInt.restype = ctypes.POINTER(ctypes.c_int32)

	if hasattr(dll, "ExternalOperator_putOutVecint"):
		dll.ExternalOperator_putOutVecint.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_putOutVecint.restype = None

	if hasattr(dll, "ExternalOperator_getInVecDouble"):
		dll.ExternalOperator_getInVecDouble.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_getInVecDouble.restype = ctypes.POINTER(ctypes.c_double)

	if hasattr(dll, "ExternalOperator_getInVecStringAsCollection"):
		dll.ExternalOperator_getInVecStringAsCollection.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_getInVecStringAsCollection.restype = ctypes.c_void_p

	if hasattr(dll, "ExternalOperator_putOutDataTree"):
		dll.ExternalOperator_putOutDataTree.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_putOutDataTree.restype = None

	if hasattr(dll, "ExternalOperator_putOutWorkflow"):
		dll.ExternalOperator_putOutWorkflow.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_putOutWorkflow.restype = None

	if hasattr(dll, "ExternalOperator_putOutGenericDataContainer"):
		dll.ExternalOperator_putOutGenericDataContainer.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_putOutGenericDataContainer.restype = None

	if hasattr(dll, "ExternalOperator_putOutResultInfo"):
		dll.ExternalOperator_putOutResultInfo.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_putOutResultInfo.restype = None

	if hasattr(dll, "ExternalOperator_putOutStringField"):
		dll.ExternalOperator_putOutStringField.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_putOutStringField.restype = None

	if hasattr(dll, "ExternalOperator_putOutCustomTypeField"):
		dll.ExternalOperator_putOutCustomTypeField.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_putOutCustomTypeField.restype = None

	if hasattr(dll, "ExternalOperator_putOutExternalData"):
		dll.ExternalOperator_putOutExternalData.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_putOutExternalData.restype = None

	if hasattr(dll, "ExternalOperator_putOutCollectionAsVector"):
		dll.ExternalOperator_putOutCollectionAsVector.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_putOutCollectionAsVector.restype = None

	if hasattr(dll, "ExternalOperator_pinIsOfType"):
		dll.ExternalOperator_pinIsOfType.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_pinIsOfType.restype = ctypes.c_bool

	if hasattr(dll, "ExternalOperator_delegateRun"):
		dll.ExternalOperator_delegateRun.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_delegateRun.restype = None

	if hasattr(dll, "ExternalOperator_instantiateInternalOperator"):
		dll.ExternalOperator_instantiateInternalOperator.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_instantiateInternalOperator.restype = ctypes.c_void_p

	if hasattr(dll, "ExternalOperator_connectAllInputsToOperator"):
		dll.ExternalOperator_connectAllInputsToOperator.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_connectAllInputsToOperator.restype = None

	if hasattr(dll, "ExternalOperator_getOperatorName"):
		dll.ExternalOperator_getOperatorName.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_getOperatorName.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "ExternalOperator_getOperatorConfig"):
		dll.ExternalOperator_getOperatorConfig.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_getOperatorConfig.restype = ctypes.c_void_p

	if hasattr(dll, "ExternalOperator_getDerivativeOfInput"):
		dll.ExternalOperator_getDerivativeOfInput.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_getDerivativeOfInput.restype = ctypes.c_void_p

	if hasattr(dll, "ExternalOperator_forwardInput"):
		dll.ExternalOperator_forwardInput.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_forwardInput.restype = None

	if hasattr(dll, "ExternalOperator_setDerivative"):
		dll.ExternalOperator_setDerivative.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_setDerivative.restype = None

	if hasattr(dll, "ExternalOperator_forwardOutput"):
		dll.ExternalOperator_forwardOutput.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_forwardOutput.restype = None

	if hasattr(dll, "ExternalOperator_assertInstantiate"):
		dll.ExternalOperator_assertInstantiate.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_assertInstantiate.restype = ctypes.c_void_p

	if hasattr(dll, "ExternalOperator_connectToUpstreamDerivative"):
		dll.ExternalOperator_connectToUpstreamDerivative.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_connectToUpstreamDerivative.restype = None

	if hasattr(dll, "ExternalOperator_mapDownStreamDerivative"):
		dll.ExternalOperator_mapDownStreamDerivative.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ExternalOperator_mapDownStreamDerivative.restype = None

	#-------------------------------------------------------------------------------
	# FEModel
	#-------------------------------------------------------------------------------
	if hasattr(dll, "FEModel_new"):
		dll.FEModel_new.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.FEModel_new.restype = ctypes.c_void_p

	if hasattr(dll, "FEModel_new_withResultFile"):
		dll.FEModel_new_withResultFile.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.FEModel_new_withResultFile.restype = ctypes.c_void_p

	if hasattr(dll, "FEModel_new_empty"):
		dll.FEModel_new_empty.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.FEModel_new_empty.restype = ctypes.c_void_p

	if hasattr(dll, "FEModel_delete"):
		dll.FEModel_delete.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.FEModel_delete.restype = None

	if hasattr(dll, "FEModel_SetResultFilePath"):
		dll.FEModel_SetResultFilePath.argtypes = (ctypes.c_void_p, ctypes.c_wchar_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.FEModel_SetResultFilePath.restype = None

	if hasattr(dll, "FEModel_AddResult"):
		dll.FEModel_AddResult.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.FEModel_AddResult.restype = ctypes.c_void_p

	if hasattr(dll, "FEModel_AddPrimaryResult"):
		dll.FEModel_AddPrimaryResult.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.FEModel_AddPrimaryResult.restype = ctypes.c_void_p

	if hasattr(dll, "FEModel_AddResultWithScoping"):
		dll.FEModel_AddResultWithScoping.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.FEModel_AddResultWithScoping.restype = ctypes.c_void_p

	if hasattr(dll, "FEModel_DeleteResult"):
		dll.FEModel_DeleteResult.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.FEModel_DeleteResult.restype = None

	if hasattr(dll, "FEModel_GetMeshRegion"):
		dll.FEModel_GetMeshRegion.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.FEModel_GetMeshRegion.restype = ctypes.c_void_p

	if hasattr(dll, "FEModel_GetTimeFreqSupport"):
		dll.FEModel_GetTimeFreqSupport.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.FEModel_GetTimeFreqSupport.restype = ctypes.c_void_p

	if hasattr(dll, "FEModel_GetSupportQuery"):
		dll.FEModel_GetSupportQuery.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.FEModel_GetSupportQuery.restype = ctypes.c_void_p

	#-------------------------------------------------------------------------------
	# Field
	#-------------------------------------------------------------------------------
	if hasattr(dll, "Field_Delete"):
		dll.Field_Delete.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Field_Delete.restype = None

	if hasattr(dll, "Field_GetData"):
		dll.Field_GetData.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Field_GetData.restype = ctypes.POINTER(ctypes.c_double)

	if hasattr(dll, "Field_GetDataPointer"):
		dll.Field_GetDataPointer.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Field_GetDataPointer.restype = ctypes.POINTER(ctypes.c_int32)

	if hasattr(dll, "Field_GetScoping"):
		dll.Field_GetScoping.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Field_GetScoping.restype = ctypes.POINTER(ctypes.c_int32)

	if hasattr(dll, "Field_GetScopingToDataPointerCopy"):
		dll.Field_GetScopingToDataPointerCopy.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Field_GetScopingToDataPointerCopy.restype = None

	if hasattr(dll, "Field_GetEntityData"):
		dll.Field_GetEntityData.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Field_GetEntityData.restype = ctypes.POINTER(ctypes.c_double)

	if hasattr(dll, "Field_GetEntityDataById"):
		dll.Field_GetEntityDataById.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Field_GetEntityDataById.restype = ctypes.POINTER(ctypes.c_double)

	if hasattr(dll, "Field_GetUnit"):
		dll.Field_GetUnit.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Field_GetUnit.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "Field_GetLocation"):
		dll.Field_GetLocation.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Field_GetLocation.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "Field_GetNumberElementaryData"):
		dll.Field_GetNumberElementaryData.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Field_GetNumberElementaryData.restype = ctypes.c_int32

	if hasattr(dll, "Field_GetNumberElementaryDataByIndex"):
		dll.Field_GetNumberElementaryDataByIndex.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Field_GetNumberElementaryDataByIndex.restype = ctypes.c_int32

	if hasattr(dll, "Field_GetNumberElementaryDataById"):
		dll.Field_GetNumberElementaryDataById.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Field_GetNumberElementaryDataById.restype = ctypes.c_int32

	if hasattr(dll, "Field_GetNumberOfComponents"):
		dll.Field_GetNumberOfComponents.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Field_GetNumberOfComponents.restype = ctypes.c_int32

	if hasattr(dll, "Field_GetNumberOfEntities"):
		dll.Field_GetNumberOfEntities.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Field_GetNumberOfEntities.restype = ctypes.c_int32

	if hasattr(dll, "Field_ElementaryDataSize"):
		dll.Field_ElementaryDataSize.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Field_ElementaryDataSize.restype = ctypes.c_int32

	if hasattr(dll, "Field_GetDataSize"):
		dll.Field_GetDataSize.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Field_GetDataSize.restype = ctypes.c_int32

	if hasattr(dll, "Field_GetEShellLayers"):
		dll.Field_GetEShellLayers.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Field_GetEShellLayers.restype = ctypes.c_int32

	if hasattr(dll, "Field_PushBack"):
		dll.Field_PushBack.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Field_PushBack.restype = None

	if hasattr(dll, "CSField_Delete"):
		dll.CSField_Delete.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_Delete.restype = None

	if hasattr(dll, "CSField_GetData"):
		dll.CSField_GetData.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_GetData.restype = ctypes.POINTER(ctypes.c_double)

	if hasattr(dll, "CSField_SetData"):
		dll.CSField_SetData.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_SetData.restype = None

	if hasattr(dll, "CSField_SetDataWithCollection"):
		dll.CSField_SetDataWithCollection.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_SetDataWithCollection.restype = None

	if hasattr(dll, "CSField_SetDataPointer"):
		dll.CSField_SetDataPointer.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_SetDataPointer.restype = None

	if hasattr(dll, "CSField_SetDataPointerWithCollection"):
		dll.CSField_SetDataPointerWithCollection.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_SetDataPointerWithCollection.restype = None

	if hasattr(dll, "CSField_SetEntityData"):
		dll.CSField_SetEntityData.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_SetEntityData.restype = None

	if hasattr(dll, "CSField_SetSupport"):
		dll.CSField_SetSupport.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_SetSupport.restype = None

	if hasattr(dll, "CSField_SetUnit"):
		dll.CSField_SetUnit.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_SetUnit.restype = None

	if hasattr(dll, "CSField_SetLocation"):
		dll.CSField_SetLocation.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_SetLocation.restype = None

	if hasattr(dll, "CSField_SetMeshedRegionAsSupport"):
		dll.CSField_SetMeshedRegionAsSupport.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_SetMeshedRegionAsSupport.restype = None

	if hasattr(dll, "CSField_UpdateEntityDataByEntityIndex"):
		dll.CSField_UpdateEntityDataByEntityIndex.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_UpdateEntityDataByEntityIndex.restype = None

	if hasattr(dll, "CSField_PushBack"):
		dll.CSField_PushBack.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_PushBack.restype = None

	if hasattr(dll, "CSField_GetScoping"):
		dll.CSField_GetScoping.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_GetScoping.restype = ctypes.POINTER(ctypes.c_int32)

	if hasattr(dll, "CSField_GetDataPtr"):
		dll.CSField_GetDataPtr.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_GetDataPtr.restype = ctypes.POINTER(ctypes.c_int32)

	if hasattr(dll, "CSField_GetCScoping"):
		dll.CSField_GetCScoping.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_GetCScoping.restype = ctypes.c_void_p

	if hasattr(dll, "CSField_GetSharedFieldDefinition"):
		dll.CSField_GetSharedFieldDefinition.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_GetSharedFieldDefinition.restype = ctypes.c_void_p

	if hasattr(dll, "CSField_GetFieldDefinition"):
		dll.CSField_GetFieldDefinition.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_GetFieldDefinition.restype = ctypes.c_void_p

	if hasattr(dll, "CSField_GetSupport"):
		dll.CSField_GetSupport.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_GetSupport.restype = ctypes.c_void_p

	if hasattr(dll, "CSField_GetDataPointer"):
		dll.CSField_GetDataPointer.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_GetDataPointer.restype = ctypes.POINTER(ctypes.c_int32)

	if hasattr(dll, "CSField_SetFieldDefinition"):
		dll.CSField_SetFieldDefinition.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_SetFieldDefinition.restype = None

	if hasattr(dll, "CSField_SetFastAccessFieldDefinition"):
		dll.CSField_SetFastAccessFieldDefinition.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_SetFastAccessFieldDefinition.restype = None

	if hasattr(dll, "CSField_SetScoping"):
		dll.CSField_SetScoping.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_SetScoping.restype = None

	if hasattr(dll, "CSField_SetCScoping"):
		dll.CSField_SetCScoping.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_SetCScoping.restype = None

	if hasattr(dll, "CSField_GetEntityData"):
		dll.CSField_GetEntityData.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_GetEntityData.restype = ctypes.POINTER(ctypes.c_double)

	if hasattr(dll, "CSField_GetEntityDataById"):
		dll.CSField_GetEntityDataById.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_GetEntityDataById.restype = ctypes.POINTER(ctypes.c_double)

	if hasattr(dll, "CSField_GetUnit"):
		dll.CSField_GetUnit.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_GetUnit.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "CSField_GetLocation"):
		dll.CSField_GetLocation.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_GetLocation.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "CSField_GetNumberElementaryData"):
		dll.CSField_GetNumberElementaryData.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_GetNumberElementaryData.restype = ctypes.c_int32

	if hasattr(dll, "CSField_GetNumberElementaryDataByIndex"):
		dll.CSField_GetNumberElementaryDataByIndex.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_GetNumberElementaryDataByIndex.restype = ctypes.c_int32

	if hasattr(dll, "CSField_GetNumberElementaryDataById"):
		dll.CSField_GetNumberElementaryDataById.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_GetNumberElementaryDataById.restype = ctypes.c_int32

	if hasattr(dll, "CSField_GetNumberEntities"):
		dll.CSField_GetNumberEntities.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_GetNumberEntities.restype = ctypes.c_int32

	if hasattr(dll, "CSField_ElementaryDataSize"):
		dll.CSField_ElementaryDataSize.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_ElementaryDataSize.restype = ctypes.c_int32

	if hasattr(dll, "CSField_GetDataSize"):
		dll.CSField_GetDataSize.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_GetDataSize.restype = ctypes.c_int32

	if hasattr(dll, "CSField_GetEShellLayers"):
		dll.CSField_GetEShellLayers.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_GetEShellLayers.restype = ctypes.c_int32

	if hasattr(dll, "CSField_SetEShellLayers"):
		dll.CSField_SetEShellLayers.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_SetEShellLayers.restype = None

	if hasattr(dll, "CSField_ResizeData"):
		dll.CSField_ResizeData.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_ResizeData.restype = None

	if hasattr(dll, "CSField_ResizeDataPointer"):
		dll.CSField_ResizeDataPointer.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_ResizeDataPointer.restype = None

	if hasattr(dll, "CSField_GetNumberOfComponents"):
		dll.CSField_GetNumberOfComponents.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_GetNumberOfComponents.restype = ctypes.c_int32

	if hasattr(dll, "CSField_Resize"):
		dll.CSField_Resize.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_Resize.restype = None

	if hasattr(dll, "CSField_Reserve"):
		dll.CSField_Reserve.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_Reserve.restype = None

	if hasattr(dll, "CSField_GetName"):
		dll.CSField_GetName.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_GetName.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "CSField_SetName"):
		dll.CSField_SetName.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_SetName.restype = None

	if hasattr(dll, "CSField_GetStringProperty"):
		dll.CSField_GetStringProperty.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.POINTER(ctypes.c_char)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_GetStringProperty.restype = ctypes.c_bool

	if hasattr(dll, "CSField_AddStringProperty"):
		dll.CSField_AddStringProperty.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_AddStringProperty.restype = None

	if hasattr(dll, "CSField_DelStringProperty"):
		dll.CSField_DelStringProperty.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_DelStringProperty.restype = None

	if hasattr(dll, "CSField_GetSupportAsMeshedRegion"):
		dll.CSField_GetSupportAsMeshedRegion.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_GetSupportAsMeshedRegion.restype = ctypes.c_void_p

	if hasattr(dll, "CSField_GetSupportAsTimeFreqSupport"):
		dll.CSField_GetSupportAsTimeFreqSupport.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_GetSupportAsTimeFreqSupport.restype = ctypes.c_void_p

	if hasattr(dll, "CSField_GetEntityId"):
		dll.CSField_GetEntityId.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_GetEntityId.restype = ctypes.c_int32

	if hasattr(dll, "CSField_GetEntityIndex"):
		dll.CSField_GetEntityIndex.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_GetEntityIndex.restype = ctypes.c_int32

	if hasattr(dll, "CSField_GetData_For_DpfVector"):
		dll.CSField_GetData_For_DpfVector.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.POINTER(ctypes.c_double)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_GetData_For_DpfVector.restype = None

	if hasattr(dll, "CSField_GetDataPointer_For_DpfVector"):
		dll.CSField_GetDataPointer_For_DpfVector.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.POINTER(ctypes.c_int32)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_GetDataPointer_For_DpfVector.restype = None

	if hasattr(dll, "CSField_GetEntityData_For_DpfVector"):
		dll.CSField_GetEntityData_For_DpfVector.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.POINTER(ctypes.c_double)), ctypes.POINTER(ctypes.c_int32), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_GetEntityData_For_DpfVector.restype = None

	if hasattr(dll, "CSField_GetEntityDataById_For_DpfVector"):
		dll.CSField_GetEntityDataById_For_DpfVector.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.POINTER(ctypes.c_double)), ctypes.POINTER(ctypes.c_int32), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_GetEntityDataById_For_DpfVector.restype = None

	if hasattr(dll, "Field_new"):
		dll.Field_new.argtypes = (ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Field_new.restype = ctypes.c_void_p

	if hasattr(dll, "Field_newWithTransformation"):
		dll.Field_newWithTransformation.argtypes = (ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Field_newWithTransformation.restype = ctypes.c_void_p

	if hasattr(dll, "Field_newWith1DDimensionnality"):
		dll.Field_newWith1DDimensionnality.argtypes = (ctypes.c_int32, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Field_newWith1DDimensionnality.restype = ctypes.c_void_p

	if hasattr(dll, "Field_newWith2DDimensionnality"):
		dll.Field_newWith2DDimensionnality.argtypes = (ctypes.c_int32, ctypes.c_int32, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Field_newWith2DDimensionnality.restype = ctypes.c_void_p

	if hasattr(dll, "Field_getCopy"):
		dll.Field_getCopy.argtypes = (ctypes.c_void_p, ctypes.c_bool, ctypes.c_bool, ctypes.c_bool, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Field_getCopy.restype = ctypes.c_void_p

	if hasattr(dll, "Field_CloneToDifferentDimension"):
		dll.Field_CloneToDifferentDimension.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Field_CloneToDifferentDimension.restype = ctypes.c_void_p

	if hasattr(dll, "CSField_cursor"):
		dll.CSField_cursor.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.POINTER(ctypes.c_double)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSField_cursor.restype = ctypes.c_bool

	if hasattr(dll, "Field_fast_access_ptr"):
		dll.Field_fast_access_ptr.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Field_fast_access_ptr.restype = ctypes.c_void_p

	if hasattr(dll, "Field_fast_cursor"):
		dll.Field_fast_cursor.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.POINTER(ctypes.c_double)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), )
		dll.Field_fast_cursor.restype = ctypes.c_bool

	if hasattr(dll, "Field_new_on_client"):
		dll.Field_new_on_client.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Field_new_on_client.restype = ctypes.c_void_p

	if hasattr(dll, "Field_newWith1DDimensionnality_on_client"):
		dll.Field_newWith1DDimensionnality_on_client.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Field_newWith1DDimensionnality_on_client.restype = ctypes.c_void_p

	if hasattr(dll, "Field_newWith2DDimensionnality_on_client"):
		dll.Field_newWith2DDimensionnality_on_client.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Field_newWith2DDimensionnality_on_client.restype = ctypes.c_void_p

	if hasattr(dll, "Field_getCopy_on_client"):
		dll.Field_getCopy_on_client.argtypes = (ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Field_getCopy_on_client.restype = ctypes.c_void_p

	#-------------------------------------------------------------------------------
	# FieldMapping
	#-------------------------------------------------------------------------------
	if hasattr(dll, "Mapping_Delete"):
		dll.Mapping_Delete.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Mapping_Delete.restype = None

	if hasattr(dll, "Mapping_Map"):
		dll.Mapping_Map.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Mapping_Map.restype = ctypes.c_void_p

	#-------------------------------------------------------------------------------
	# FieldDefinition
	#-------------------------------------------------------------------------------
	if hasattr(dll, "FieldDefinition_new"):
		dll.FieldDefinition_new.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.FieldDefinition_new.restype = ctypes.c_void_p

	if hasattr(dll, "FieldDefinition_wrap"):
		dll.FieldDefinition_wrap.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.FieldDefinition_wrap.restype = ctypes.c_void_p

	if hasattr(dll, "FieldDefinition_Delete"):
		dll.FieldDefinition_Delete.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.FieldDefinition_Delete.restype = None

	if hasattr(dll, "FieldDefinition_GetFastAccessPtr"):
		dll.FieldDefinition_GetFastAccessPtr.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.FieldDefinition_GetFastAccessPtr.restype = ctypes.c_void_p

	if hasattr(dll, "FieldDefinition_GetUnit"):
		dll.FieldDefinition_GetUnit.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.FieldDefinition_GetUnit.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "FieldDefinition_FillUnit"):
		dll.FieldDefinition_FillUnit.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.FieldDefinition_FillUnit.restype = None

	if hasattr(dll, "FieldDefinition_GetShellLayers"):
		dll.FieldDefinition_GetShellLayers.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.FieldDefinition_GetShellLayers.restype = ctypes.c_int32

	if hasattr(dll, "FieldDefinition_GetLocation"):
		dll.FieldDefinition_GetLocation.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.FieldDefinition_GetLocation.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "FieldDefinition_FillLocation"):
		dll.FieldDefinition_FillLocation.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.FieldDefinition_FillLocation.restype = None

	if hasattr(dll, "FieldDefinition_GetDimensionality"):
		dll.FieldDefinition_GetDimensionality.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.FieldDefinition_GetDimensionality.restype = ctypes.POINTER(ctypes.c_int32)

	if hasattr(dll, "FieldDefinition_FillDimensionality"):
		dll.FieldDefinition_FillDimensionality.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.FieldDefinition_FillDimensionality.restype = None

	if hasattr(dll, "FieldDefinition_SetUnit"):
		dll.FieldDefinition_SetUnit.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_double), ctypes.c_int32, ctypes.c_double, ctypes.c_double, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.FieldDefinition_SetUnit.restype = None

	if hasattr(dll, "FieldDefinition_SetShellLayers"):
		dll.FieldDefinition_SetShellLayers.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.FieldDefinition_SetShellLayers.restype = None

	if hasattr(dll, "FieldDefinition_SetLocation"):
		dll.FieldDefinition_SetLocation.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.FieldDefinition_SetLocation.restype = None

	if hasattr(dll, "FieldDefinition_SetDimensionality"):
		dll.FieldDefinition_SetDimensionality.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.FieldDefinition_SetDimensionality.restype = None

	if hasattr(dll, "CSFieldDefinition_GetUnit"):
		dll.CSFieldDefinition_GetUnit.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSFieldDefinition_GetUnit.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "CSFieldDefinition_FillUnit"):
		dll.CSFieldDefinition_FillUnit.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSFieldDefinition_FillUnit.restype = None

	if hasattr(dll, "CSFieldDefinition_GetShellLayers"):
		dll.CSFieldDefinition_GetShellLayers.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSFieldDefinition_GetShellLayers.restype = ctypes.c_int32

	if hasattr(dll, "CSFieldDefinition_GetLocation"):
		dll.CSFieldDefinition_GetLocation.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSFieldDefinition_GetLocation.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "CSFieldDefinition_FillLocation"):
		dll.CSFieldDefinition_FillLocation.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSFieldDefinition_FillLocation.restype = None

	if hasattr(dll, "CSFieldDefinition_GetDimensionality"):
		dll.CSFieldDefinition_GetDimensionality.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSFieldDefinition_GetDimensionality.restype = ctypes.POINTER(ctypes.c_int32)

	if hasattr(dll, "CSFieldDefinition_FillDimensionality"):
		dll.CSFieldDefinition_FillDimensionality.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSFieldDefinition_FillDimensionality.restype = None

	if hasattr(dll, "CSFieldDefinition_SetUnit"):
		dll.CSFieldDefinition_SetUnit.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_double), ctypes.c_int32, ctypes.c_double, ctypes.c_double, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSFieldDefinition_SetUnit.restype = None

	if hasattr(dll, "CSFieldDefinition_SetShellLayers"):
		dll.CSFieldDefinition_SetShellLayers.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSFieldDefinition_SetShellLayers.restype = None

	if hasattr(dll, "CSFieldDefinition_SetLocation"):
		dll.CSFieldDefinition_SetLocation.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSFieldDefinition_SetLocation.restype = None

	if hasattr(dll, "CSFieldDefinition_SetDimensionality"):
		dll.CSFieldDefinition_SetDimensionality.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSFieldDefinition_SetDimensionality.restype = None

	if hasattr(dll, "CSFieldDefinition_SetQuantityType"):
		dll.CSFieldDefinition_SetQuantityType.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSFieldDefinition_SetQuantityType.restype = None

	if hasattr(dll, "CSFieldDefinition_GetNumAvailableQuantityTypes"):
		dll.CSFieldDefinition_GetNumAvailableQuantityTypes.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSFieldDefinition_GetNumAvailableQuantityTypes.restype = ctypes.c_int32

	if hasattr(dll, "CSFieldDefinition_GetQuantityType"):
		dll.CSFieldDefinition_GetQuantityType.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSFieldDefinition_GetQuantityType.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "CSFieldDefinition_IsOfQuantityType"):
		dll.CSFieldDefinition_IsOfQuantityType.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSFieldDefinition_IsOfQuantityType.restype = ctypes.c_bool

	if hasattr(dll, "CSFieldDefinition_GetName"):
		dll.CSFieldDefinition_GetName.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSFieldDefinition_GetName.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "CSFieldDefinition_SetName"):
		dll.CSFieldDefinition_SetName.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSFieldDefinition_SetName.restype = None

	if hasattr(dll, "CSFieldDefinition_FillName"):
		dll.CSFieldDefinition_FillName.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSFieldDefinition_FillName.restype = None

	if hasattr(dll, "Dimensionality_GetNumComp"):
		dll.Dimensionality_GetNumComp.argtypes = (ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Dimensionality_GetNumComp.restype = ctypes.c_int32

	if hasattr(dll, "FieldDefinition_new_on_client"):
		dll.FieldDefinition_new_on_client.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.FieldDefinition_new_on_client.restype = ctypes.c_void_p

	if hasattr(dll, "Dimensionality_GetNumComp_for_object"):
		dll.Dimensionality_GetNumComp_for_object.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Dimensionality_GetNumComp_for_object.restype = ctypes.c_int32

	#-------------------------------------------------------------------------------
	# FieldsContainer
	#-------------------------------------------------------------------------------
	if hasattr(dll, "FieldsContainer_new"):
		dll.FieldsContainer_new.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.FieldsContainer_new.restype = ctypes.c_void_p

	if hasattr(dll, "FieldsContainer_Delete"):
		dll.FieldsContainer_Delete.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.FieldsContainer_Delete.restype = None

	if hasattr(dll, "FieldsContainer_at"):
		dll.FieldsContainer_at.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.FieldsContainer_at.restype = ctypes.c_void_p

	if hasattr(dll, "FieldsContainer_setField"):
		dll.FieldsContainer_setField.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.FieldsContainer_setField.restype = None

	if hasattr(dll, "FieldsContainer_GetScoping"):
		dll.FieldsContainer_GetScoping.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.FieldsContainer_GetScoping.restype = ctypes.POINTER(ctypes.c_int32)

	if hasattr(dll, "FieldsContainer_numFields"):
		dll.FieldsContainer_numFields.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.FieldsContainer_numFields.restype = ctypes.c_int32

	#-------------------------------------------------------------------------------
	# LabelSpace
	#-------------------------------------------------------------------------------
	if hasattr(dll, "LabelSpace_new"):
		dll.LabelSpace_new.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.LabelSpace_new.restype = ctypes.c_void_p

	if hasattr(dll, "LabelSpace_delete"):
		dll.LabelSpace_delete.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.LabelSpace_delete.restype = None

	if hasattr(dll, "LabelSpace_AddData"):
		dll.LabelSpace_AddData.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.LabelSpace_AddData.restype = None

	if hasattr(dll, "LabelSpace_SetData"):
		dll.LabelSpace_SetData.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.LabelSpace_SetData.restype = None

	if hasattr(dll, "LabelSpace_EraseData"):
		dll.LabelSpace_EraseData.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.LabelSpace_EraseData.restype = None

	if hasattr(dll, "LabelSpace_GetSize"):
		dll.LabelSpace_GetSize.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.LabelSpace_GetSize.restype = ctypes.c_int32

	if hasattr(dll, "LabelSpace_MergeWith"):
		dll.LabelSpace_MergeWith.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.LabelSpace_MergeWith.restype = None

	if hasattr(dll, "LabelSpace_GetLabelsValue"):
		dll.LabelSpace_GetLabelsValue.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.LabelSpace_GetLabelsValue.restype = ctypes.c_int32

	if hasattr(dll, "LabelSpace_GetLabelsName"):
		dll.LabelSpace_GetLabelsName.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.LabelSpace_GetLabelsName.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "LabelSpace_HasLabel"):
		dll.LabelSpace_HasLabel.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.LabelSpace_HasLabel.restype = ctypes.c_bool

	if hasattr(dll, "LabelSpace_At"):
		dll.LabelSpace_At.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.LabelSpace_At.restype = ctypes.c_int32

	if hasattr(dll, "ListLabelSpaces_new"):
		dll.ListLabelSpaces_new.argtypes = (ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ListLabelSpaces_new.restype = ctypes.c_void_p

	if hasattr(dll, "ListLabelSpaces_pushback"):
		dll.ListLabelSpaces_pushback.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ListLabelSpaces_pushback.restype = None

	if hasattr(dll, "ListLabelSpaces_size"):
		dll.ListLabelSpaces_size.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ListLabelSpaces_size.restype = ctypes.c_int32

	if hasattr(dll, "ListLabelSpaces_at"):
		dll.ListLabelSpaces_at.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ListLabelSpaces_at.restype = ctypes.c_void_p

	if hasattr(dll, "LabelSpace_new_for_object"):
		dll.LabelSpace_new_for_object.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.LabelSpace_new_for_object.restype = ctypes.c_void_p

	if hasattr(dll, "ListLabelSpaces_new_for_object"):
		dll.ListLabelSpaces_new_for_object.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ListLabelSpaces_new_for_object.restype = ctypes.c_void_p

	#-------------------------------------------------------------------------------
	# MaterialsContainer
	#-------------------------------------------------------------------------------
	if hasattr(dll, "MaterialsContainer_delete"):
		dll.MaterialsContainer_delete.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MaterialsContainer_delete.restype = None

	if hasattr(dll, "MaterialsContainer_GetDpfMatIds"):
		dll.MaterialsContainer_GetDpfMatIds.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MaterialsContainer_GetDpfMatIds.restype = ctypes.POINTER(ctypes.c_int32)

	if hasattr(dll, "MaterialsContainer_GetVUUIDAtDpfMatId"):
		dll.MaterialsContainer_GetVUUIDAtDpfMatId.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MaterialsContainer_GetVUUIDAtDpfMatId.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "MaterialsContainer_GetNumOfMaterials"):
		dll.MaterialsContainer_GetNumOfMaterials.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MaterialsContainer_GetNumOfMaterials.restype = ctypes.c_int32

	if hasattr(dll, "MaterialsContainer_GetNumAvailablePropertiesAtVUUID"):
		dll.MaterialsContainer_GetNumAvailablePropertiesAtVUUID.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MaterialsContainer_GetNumAvailablePropertiesAtVUUID.restype = ctypes.c_int32

	if hasattr(dll, "MaterialsContainer_GetPropertyScriptingNameOfDpfMatIdAtIndex"):
		dll.MaterialsContainer_GetPropertyScriptingNameOfDpfMatIdAtIndex.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MaterialsContainer_GetPropertyScriptingNameOfDpfMatIdAtIndex.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "MaterialsContainer_GetNumAvailablePropertiesAtDpfMatId"):
		dll.MaterialsContainer_GetNumAvailablePropertiesAtDpfMatId.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MaterialsContainer_GetNumAvailablePropertiesAtDpfMatId.restype = ctypes.c_int32

	if hasattr(dll, "MaterialsContainer_GetMaterialPhysicNameAtVUUID"):
		dll.MaterialsContainer_GetMaterialPhysicNameAtVUUID.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MaterialsContainer_GetMaterialPhysicNameAtVUUID.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "MaterialsContainer_GetMaterialPhysicNameAtDpfMatId"):
		dll.MaterialsContainer_GetMaterialPhysicNameAtDpfMatId.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MaterialsContainer_GetMaterialPhysicNameAtDpfMatId.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "MaterialsContainer_GetDpfMatIdAtMaterialPhysicName"):
		dll.MaterialsContainer_GetDpfMatIdAtMaterialPhysicName.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MaterialsContainer_GetDpfMatIdAtMaterialPhysicName.restype = ctypes.c_int32

	if hasattr(dll, "MaterialsContainer_GetDpfMatIdAtVUUID"):
		dll.MaterialsContainer_GetDpfMatIdAtVUUID.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MaterialsContainer_GetDpfMatIdAtVUUID.restype = ctypes.c_int32

	#-------------------------------------------------------------------------------
	# MeshedRegion
	#-------------------------------------------------------------------------------
	if hasattr(dll, "MeshedRegion_New"):
		dll.MeshedRegion_New.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_New.restype = ctypes.c_void_p

	if hasattr(dll, "MeshedRegion_Delete"):
		dll.MeshedRegion_Delete.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_Delete.restype = None

	if hasattr(dll, "MeshedRegion_Reserve"):
		dll.MeshedRegion_Reserve.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_Reserve.restype = None

	if hasattr(dll, "MeshedRegion_GetNumNodes"):
		dll.MeshedRegion_GetNumNodes.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_GetNumNodes.restype = ctypes.c_int32

	if hasattr(dll, "MeshedRegion_GetNumElements"):
		dll.MeshedRegion_GetNumElements.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_GetNumElements.restype = ctypes.c_int32

	if hasattr(dll, "MeshedRegion_GetNumFaces"):
		dll.MeshedRegion_GetNumFaces.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_GetNumFaces.restype = ctypes.c_int32

	if hasattr(dll, "MeshedRegion_GetSharedNodesScoping"):
		dll.MeshedRegion_GetSharedNodesScoping.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_GetSharedNodesScoping.restype = ctypes.c_void_p

	if hasattr(dll, "MeshedRegion_GetSharedElementsScoping"):
		dll.MeshedRegion_GetSharedElementsScoping.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_GetSharedElementsScoping.restype = ctypes.c_void_p

	if hasattr(dll, "MeshedRegion_GetSharedFacesScoping"):
		dll.MeshedRegion_GetSharedFacesScoping.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_GetSharedFacesScoping.restype = ctypes.c_void_p

	if hasattr(dll, "MeshedRegion_GetUnit"):
		dll.MeshedRegion_GetUnit.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_GetUnit.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "MeshedRegion_GetHasSolidRegion"):
		dll.MeshedRegion_GetHasSolidRegion.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_GetHasSolidRegion.restype = ctypes.c_bool

	if hasattr(dll, "MeshedRegion_GetHasGasketRegion"):
		dll.MeshedRegion_GetHasGasketRegion.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_GetHasGasketRegion.restype = ctypes.c_bool

	if hasattr(dll, "MeshedRegion_GetHasShellRegion"):
		dll.MeshedRegion_GetHasShellRegion.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_GetHasShellRegion.restype = ctypes.c_bool

	if hasattr(dll, "MeshedRegion_GetHasSkinRegion"):
		dll.MeshedRegion_GetHasSkinRegion.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_GetHasSkinRegion.restype = ctypes.c_bool

	if hasattr(dll, "MeshedRegion_GetHasOnlySkinElements"):
		dll.MeshedRegion_GetHasOnlySkinElements.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_GetHasOnlySkinElements.restype = ctypes.c_bool

	if hasattr(dll, "MeshedRegion_GetHasPointRegion"):
		dll.MeshedRegion_GetHasPointRegion.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_GetHasPointRegion.restype = ctypes.c_bool

	if hasattr(dll, "MeshedRegion_GetHasBeamRegion"):
		dll.MeshedRegion_GetHasBeamRegion.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_GetHasBeamRegion.restype = ctypes.c_bool

	if hasattr(dll, "MeshedRegion_GetHasPolygons"):
		dll.MeshedRegion_GetHasPolygons.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_GetHasPolygons.restype = ctypes.c_bool

	if hasattr(dll, "MeshedRegion_GetHasPolyhedrons"):
		dll.MeshedRegion_GetHasPolyhedrons.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_GetHasPolyhedrons.restype = ctypes.c_bool

	if hasattr(dll, "MeshedRegion_GetNodeId"):
		dll.MeshedRegion_GetNodeId.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_GetNodeId.restype = ctypes.c_int32

	if hasattr(dll, "MeshedRegion_GetNodeIndex"):
		dll.MeshedRegion_GetNodeIndex.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_GetNodeIndex.restype = ctypes.c_int32

	if hasattr(dll, "MeshedRegion_GetElementId"):
		dll.MeshedRegion_GetElementId.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_GetElementId.restype = ctypes.c_int32

	if hasattr(dll, "MeshedRegion_GetElementIndex"):
		dll.MeshedRegion_GetElementIndex.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_GetElementIndex.restype = ctypes.c_int32

	if hasattr(dll, "MeshedRegion_GetNumNodesOfElement"):
		dll.MeshedRegion_GetNumNodesOfElement.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_GetNumNodesOfElement.restype = ctypes.c_int32

	if hasattr(dll, "MeshedRegion_GetNumCornerNodesOfElement"):
		dll.MeshedRegion_GetNumCornerNodesOfElement.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_GetNumCornerNodesOfElement.restype = ctypes.c_int32

	if hasattr(dll, "MeshedRegion_GetAdjacentNodesOfMidNodeInElement"):
		dll.MeshedRegion_GetAdjacentNodesOfMidNodeInElement.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_GetAdjacentNodesOfMidNodeInElement.restype = None

	if hasattr(dll, "MeshedRegion_GetNodeIdOfElement"):
		dll.MeshedRegion_GetNodeIdOfElement.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_GetNodeIdOfElement.restype = ctypes.c_int32

	if hasattr(dll, "MeshedRegion_GetNodeCoord"):
		dll.MeshedRegion_GetNodeCoord.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_GetNodeCoord.restype = ctypes.c_double

	if hasattr(dll, "MeshedRegion_GetElementType"):
		dll.MeshedRegion_GetElementType.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_GetElementType.restype = None

	if hasattr(dll, "MeshedRegion_GetElementShape"):
		dll.MeshedRegion_GetElementShape.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_GetElementShape.restype = None

	if hasattr(dll, "MeshedRegion_SetUnit"):
		dll.MeshedRegion_SetUnit.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_SetUnit.restype = None

	if hasattr(dll, "MeshedRegion_GetNumAvailableNamedSelection"):
		dll.MeshedRegion_GetNumAvailableNamedSelection.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_GetNumAvailableNamedSelection.restype = ctypes.c_int32

	if hasattr(dll, "MeshedRegion_GetNamedSelectionName"):
		dll.MeshedRegion_GetNamedSelectionName.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_GetNamedSelectionName.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "MeshedRegion_GetNamedSelectionScoping"):
		dll.MeshedRegion_GetNamedSelectionScoping.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_GetNamedSelectionScoping.restype = ctypes.c_void_p

	if hasattr(dll, "MeshedRegion_AddNode"):
		dll.MeshedRegion_AddNode.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_double), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_AddNode.restype = None

	if hasattr(dll, "MeshedRegion_AddElement"):
		dll.MeshedRegion_AddElement.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_AddElement.restype = None

	if hasattr(dll, "MeshedRegion_AddElementByShape"):
		dll.MeshedRegion_AddElementByShape.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_AddElementByShape.restype = None

	if hasattr(dll, "MeshedRegion_GetPropertyField"):
		dll.MeshedRegion_GetPropertyField.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_GetPropertyField.restype = ctypes.c_void_p

	if hasattr(dll, "MeshedRegion_HasPropertyField"):
		dll.MeshedRegion_HasPropertyField.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_HasPropertyField.restype = ctypes.c_bool

	if hasattr(dll, "MeshedRegion_GetNumAvailablePropertyField"):
		dll.MeshedRegion_GetNumAvailablePropertyField.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_GetNumAvailablePropertyField.restype = ctypes.c_int32

	if hasattr(dll, "MeshedRegion_GetPropertyFieldName"):
		dll.MeshedRegion_GetPropertyFieldName.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_GetPropertyFieldName.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "MeshedRegion_GetCoordinatesField"):
		dll.MeshedRegion_GetCoordinatesField.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_GetCoordinatesField.restype = ctypes.c_void_p

	if hasattr(dll, "MeshedRegion_FillName"):
		dll.MeshedRegion_FillName.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_FillName.restype = None

	if hasattr(dll, "MeshedRegion_SetName"):
		dll.MeshedRegion_SetName.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_SetName.restype = None

	if hasattr(dll, "MeshedRegion_SetPropertyField"):
		dll.MeshedRegion_SetPropertyField.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_SetPropertyField.restype = None

	if hasattr(dll, "MeshedRegion_SetCoordinatesField"):
		dll.MeshedRegion_SetCoordinatesField.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_SetCoordinatesField.restype = None

	if hasattr(dll, "MeshedRegion_SetNamedSelectionScoping"):
		dll.MeshedRegion_SetNamedSelectionScoping.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_SetNamedSelectionScoping.restype = None

	if hasattr(dll, "MeshedRegion_cursor"):
		dll.MeshedRegion_cursor.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.POINTER(ctypes.c_int32)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_cursor.restype = ctypes.c_bool

	if hasattr(dll, "MeshedRegion_fast_access_ptr"):
		dll.MeshedRegion_fast_access_ptr.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_fast_access_ptr.restype = ctypes.c_void_p

	if hasattr(dll, "MeshedRegion_fast_add_node"):
		dll.MeshedRegion_fast_add_node.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_double), ctypes.c_int32, )
		dll.MeshedRegion_fast_add_node.restype = None

	if hasattr(dll, "MeshedRegion_fast_add_element"):
		dll.MeshedRegion_fast_add_element.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.c_int32, )
		dll.MeshedRegion_fast_add_element.restype = None

	if hasattr(dll, "MeshedRegion_fast_reserve"):
		dll.MeshedRegion_fast_reserve.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, )
		dll.MeshedRegion_fast_reserve.restype = None

	if hasattr(dll, "MeshedRegion_fast_cursor"):
		dll.MeshedRegion_fast_cursor.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.POINTER(ctypes.c_int32)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), )
		dll.MeshedRegion_fast_cursor.restype = ctypes.c_bool

	if hasattr(dll, "MeshedRegion_New_on_client"):
		dll.MeshedRegion_New_on_client.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_New_on_client.restype = ctypes.c_void_p

	if hasattr(dll, "MeshedRegion_getCopy"):
		dll.MeshedRegion_getCopy.argtypes = (ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.MeshedRegion_getCopy.restype = ctypes.c_void_p

	#-------------------------------------------------------------------------------
	# Operator
	#-------------------------------------------------------------------------------
	if hasattr(dll, "Operator_new"):
		dll.Operator_new.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_new.restype = ctypes.c_void_p

	if hasattr(dll, "Operator_getSpecificationIfAny"):
		dll.Operator_getSpecificationIfAny.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_getSpecificationIfAny.restype = ctypes.c_void_p

	if hasattr(dll, "Operator_delete"):
		dll.Operator_delete.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_delete.restype = None

	if hasattr(dll, "Operator_record_instance"):
		dll.Operator_record_instance.argtypes = (ctypes.c_void_p, ctypes.c_bool, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_record_instance.restype = None

	if hasattr(dll, "Operator_record_with_new_name"):
		dll.Operator_record_with_new_name.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_record_with_new_name.restype = None

	if hasattr(dll, "Operator_set_config"):
		dll.Operator_set_config.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_set_config.restype = ctypes.c_int32

	if hasattr(dll, "Operator_get_config"):
		dll.Operator_get_config.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_get_config.restype = ctypes.c_void_p

	if hasattr(dll, "Operator_ById"):
		dll.Operator_ById.argtypes = (ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_ById.restype = ctypes.c_void_p

	if hasattr(dll, "Get_Operator_Id"):
		dll.Get_Operator_Id.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Get_Operator_Id.restype = ctypes.c_int32

	if hasattr(dll, "dpf_operator_ByName"):
		dll.dpf_operator_ByName.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.dpf_operator_ByName.restype = ctypes.c_void_p

	if hasattr(dll, "dpf_Operator_delete"):
		dll.dpf_Operator_delete.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.dpf_Operator_delete.restype = None

	if hasattr(dll, "Operator_connect_DpfType"):
		dll.Operator_connect_DpfType.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_connect_DpfType.restype = None

	if hasattr(dll, "Operator_connect_int"):
		dll.Operator_connect_int.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_connect_int.restype = None

	if hasattr(dll, "Operator_connect_bool"):
		dll.Operator_connect_bool.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_bool, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_connect_bool.restype = None

	if hasattr(dll, "Operator_connect_double"):
		dll.Operator_connect_double.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_double, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_connect_double.restype = None

	if hasattr(dll, "Operator_connect_string"):
		dll.Operator_connect_string.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_connect_string.restype = None

	if hasattr(dll, "Operator_connect_string_with_size"):
		dll.Operator_connect_string_with_size.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_char), ctypes.c_uint64, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_connect_string_with_size.restype = None

	if hasattr(dll, "Operator_connect_Scoping"):
		dll.Operator_connect_Scoping.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_connect_Scoping.restype = None

	if hasattr(dll, "Operator_connect_DataSources"):
		dll.Operator_connect_DataSources.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_connect_DataSources.restype = None

	if hasattr(dll, "Operator_connect_Field"):
		dll.Operator_connect_Field.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_connect_Field.restype = None

	if hasattr(dll, "Operator_connect_Collection"):
		dll.Operator_connect_Collection.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_connect_Collection.restype = None

	if hasattr(dll, "Operator_connect_MeshedRegion"):
		dll.Operator_connect_MeshedRegion.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_connect_MeshedRegion.restype = None

	if hasattr(dll, "Operator_connect_vector_int"):
		dll.Operator_connect_vector_int.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_connect_vector_int.restype = None

	if hasattr(dll, "Operator_connect_vector_double"):
		dll.Operator_connect_vector_double.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_double), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_connect_vector_double.restype = None

	if hasattr(dll, "Operator_connect_Collection_as_vector"):
		dll.Operator_connect_Collection_as_vector.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_connect_Collection_as_vector.restype = None

	if hasattr(dll, "Operator_connect_operator_output"):
		dll.Operator_connect_operator_output.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_connect_operator_output.restype = None

	if hasattr(dll, "Operator_connect_Streams"):
		dll.Operator_connect_Streams.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_connect_Streams.restype = None

	if hasattr(dll, "Operator_connect_PropertyField"):
		dll.Operator_connect_PropertyField.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_connect_PropertyField.restype = None

	if hasattr(dll, "Operator_connect_StringField"):
		dll.Operator_connect_StringField.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_connect_StringField.restype = None

	if hasattr(dll, "Operator_connect_CustomTypeField"):
		dll.Operator_connect_CustomTypeField.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_connect_CustomTypeField.restype = None

	if hasattr(dll, "Operator_connect_Support"):
		dll.Operator_connect_Support.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_connect_Support.restype = None

	if hasattr(dll, "Operator_connect_TimeFreqSupport"):
		dll.Operator_connect_TimeFreqSupport.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_connect_TimeFreqSupport.restype = None

	if hasattr(dll, "Operator_connect_Workflow"):
		dll.Operator_connect_Workflow.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_connect_Workflow.restype = None

	if hasattr(dll, "Operator_connect_CyclicSupport"):
		dll.Operator_connect_CyclicSupport.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_connect_CyclicSupport.restype = None

	if hasattr(dll, "Operator_connect_IAnsDispatch"):
		dll.Operator_connect_IAnsDispatch.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_connect_IAnsDispatch.restype = None

	if hasattr(dll, "Operator_connect_DataTree"):
		dll.Operator_connect_DataTree.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_connect_DataTree.restype = None

	if hasattr(dll, "Operator_connect_ExternalData"):
		dll.Operator_connect_ExternalData.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_connect_ExternalData.restype = None

	if hasattr(dll, "Operator_connect_RemoteWorkflow"):
		dll.Operator_connect_RemoteWorkflow.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_connect_RemoteWorkflow.restype = None

	if hasattr(dll, "Operator_connect_Operator_as_input"):
		dll.Operator_connect_Operator_as_input.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_connect_Operator_as_input.restype = None

	if hasattr(dll, "Operator_connect_Any"):
		dll.Operator_connect_Any.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_connect_Any.restype = None

	if hasattr(dll, "Operator_connect_LabelSpace"):
		dll.Operator_connect_LabelSpace.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_connect_LabelSpace.restype = None

	if hasattr(dll, "Operator_connect_GenericDataContainer"):
		dll.Operator_connect_GenericDataContainer.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_connect_GenericDataContainer.restype = None

	if hasattr(dll, "Operator_connect_ResultInfo"):
		dll.Operator_connect_ResultInfo.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_connect_ResultInfo.restype = None

	if hasattr(dll, "Operator_disconnect"):
		dll.Operator_disconnect.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_disconnect.restype = None

	if hasattr(dll, "Operator_getoutput_FieldsContainer"):
		dll.Operator_getoutput_FieldsContainer.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_getoutput_FieldsContainer.restype = ctypes.c_void_p

	if hasattr(dll, "Operator_getoutput_ScopingsContainer"):
		dll.Operator_getoutput_ScopingsContainer.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_getoutput_ScopingsContainer.restype = ctypes.c_void_p

	if hasattr(dll, "Operator_getoutput_Field"):
		dll.Operator_getoutput_Field.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_getoutput_Field.restype = ctypes.c_void_p

	if hasattr(dll, "Operator_getoutput_Scoping"):
		dll.Operator_getoutput_Scoping.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_getoutput_Scoping.restype = ctypes.c_void_p

	if hasattr(dll, "Operator_getoutput_DataSources"):
		dll.Operator_getoutput_DataSources.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_getoutput_DataSources.restype = ctypes.c_void_p

	if hasattr(dll, "Operator_getoutput_FieldMapping"):
		dll.Operator_getoutput_FieldMapping.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_getoutput_FieldMapping.restype = ctypes.c_void_p

	if hasattr(dll, "Operator_getoutput_MeshesContainer"):
		dll.Operator_getoutput_MeshesContainer.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_getoutput_MeshesContainer.restype = ctypes.c_void_p

	if hasattr(dll, "Operator_getoutput_CustomTypeFieldsContainer"):
		dll.Operator_getoutput_CustomTypeFieldsContainer.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_getoutput_CustomTypeFieldsContainer.restype = ctypes.c_void_p

	if hasattr(dll, "Operator_getoutput_CyclicSupport"):
		dll.Operator_getoutput_CyclicSupport.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_getoutput_CyclicSupport.restype = ctypes.c_void_p

	if hasattr(dll, "Operator_getoutput_Workflow"):
		dll.Operator_getoutput_Workflow.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_getoutput_Workflow.restype = ctypes.c_void_p

	if hasattr(dll, "Operator_getoutput_StringField"):
		dll.Operator_getoutput_StringField.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_getoutput_StringField.restype = ctypes.c_void_p

	if hasattr(dll, "Operator_getoutput_CustomTypeField"):
		dll.Operator_getoutput_CustomTypeField.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_getoutput_CustomTypeField.restype = ctypes.c_void_p

	if hasattr(dll, "Operator_getoutput_GenericDataContainer"):
		dll.Operator_getoutput_GenericDataContainer.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_getoutput_GenericDataContainer.restype = ctypes.c_void_p

	if hasattr(dll, "Operator_getoutput_string"):
		dll.Operator_getoutput_string.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_getoutput_string.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "Operator_getoutput_string_with_size"):
		dll.Operator_getoutput_string_with_size.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_getoutput_string_with_size.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "Operator_getoutput_bytearray"):
		dll.Operator_getoutput_bytearray.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_getoutput_bytearray.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "Operator_getoutput_int"):
		dll.Operator_getoutput_int.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_getoutput_int.restype = ctypes.c_int32

	if hasattr(dll, "Operator_getoutput_double"):
		dll.Operator_getoutput_double.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_getoutput_double.restype = ctypes.c_double

	if hasattr(dll, "Operator_getoutput_bool"):
		dll.Operator_getoutput_bool.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_getoutput_bool.restype = ctypes.c_bool

	if hasattr(dll, "Operator_getoutput_timeFreqSupport"):
		dll.Operator_getoutput_timeFreqSupport.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_getoutput_timeFreqSupport.restype = ctypes.c_void_p

	if hasattr(dll, "Operator_getoutput_meshedRegion"):
		dll.Operator_getoutput_meshedRegion.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_getoutput_meshedRegion.restype = ctypes.c_void_p

	if hasattr(dll, "Operator_getoutput_resultInfo"):
		dll.Operator_getoutput_resultInfo.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_getoutput_resultInfo.restype = ctypes.c_void_p

	if hasattr(dll, "Operator_getoutput_MaterialsContainer"):
		dll.Operator_getoutput_MaterialsContainer.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_getoutput_MaterialsContainer.restype = ctypes.c_void_p

	if hasattr(dll, "Operator_getoutput_streams"):
		dll.Operator_getoutput_streams.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_getoutput_streams.restype = ctypes.c_void_p

	if hasattr(dll, "Operator_getoutput_propertyField"):
		dll.Operator_getoutput_propertyField.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_getoutput_propertyField.restype = ctypes.c_void_p

	if hasattr(dll, "Operator_getoutput_anySupport"):
		dll.Operator_getoutput_anySupport.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_getoutput_anySupport.restype = ctypes.c_void_p

	if hasattr(dll, "Operator_getoutput_DataTree"):
		dll.Operator_getoutput_DataTree.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_getoutput_DataTree.restype = ctypes.c_void_p

	if hasattr(dll, "Operator_getoutput_Operator"):
		dll.Operator_getoutput_Operator.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_getoutput_Operator.restype = ctypes.c_void_p

	if hasattr(dll, "Operator_getoutput_ExternalData"):
		dll.Operator_getoutput_ExternalData.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_getoutput_ExternalData.restype = ctypes.c_void_p

	if hasattr(dll, "Operator_getoutput_IntCollection"):
		dll.Operator_getoutput_IntCollection.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_getoutput_IntCollection.restype = ctypes.c_void_p

	if hasattr(dll, "Operator_getoutput_DoubleCollection"):
		dll.Operator_getoutput_DoubleCollection.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_getoutput_DoubleCollection.restype = ctypes.c_void_p

	if hasattr(dll, "Operator_getoutput_AsAny"):
		dll.Operator_getoutput_AsAny.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_getoutput_AsAny.restype = ctypes.c_void_p

	if hasattr(dll, "Operator_has_output_when_evaluated"):
		dll.Operator_has_output_when_evaluated.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_has_output_when_evaluated.restype = ctypes.c_bool

	if hasattr(dll, "Operator_status"):
		dll.Operator_status.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_status.restype = ctypes.c_int32

	if hasattr(dll, "Operator_run"):
		dll.Operator_run.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_run.restype = None

	if hasattr(dll, "Operator_invalidate"):
		dll.Operator_invalidate.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_invalidate.restype = None

	if hasattr(dll, "Operator_derivate"):
		dll.Operator_derivate.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_derivate.restype = ctypes.c_void_p

	if hasattr(dll, "Operator_name"):
		dll.Operator_name.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_name.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "Operator_get_status"):
		dll.Operator_get_status.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_get_status.restype = ctypes.c_int32

	if hasattr(dll, "Operator_new_on_client"):
		dll.Operator_new_on_client.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_new_on_client.restype = ctypes.c_void_p

	if hasattr(dll, "Operator_getCopy"):
		dll.Operator_getCopy.argtypes = (ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_getCopy.restype = ctypes.c_void_p

	if hasattr(dll, "Operator_get_id_for_client"):
		dll.Operator_get_id_for_client.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_get_id_for_client.restype = ctypes.c_int32

	#-------------------------------------------------------------------------------
	# OperatorConfig
	#-------------------------------------------------------------------------------
	if hasattr(dll, "OperatorConfig_default_new"):
		dll.OperatorConfig_default_new.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.OperatorConfig_default_new.restype = ctypes.c_void_p

	if hasattr(dll, "OperatorConfig_empty_new"):
		dll.OperatorConfig_empty_new.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.OperatorConfig_empty_new.restype = ctypes.c_void_p

	if hasattr(dll, "OperatorConfig_get_int"):
		dll.OperatorConfig_get_int.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.OperatorConfig_get_int.restype = ctypes.c_int32

	if hasattr(dll, "OperatorConfig_get_double"):
		dll.OperatorConfig_get_double.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.OperatorConfig_get_double.restype = ctypes.c_double

	if hasattr(dll, "OperatorConfig_get_bool"):
		dll.OperatorConfig_get_bool.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.OperatorConfig_get_bool.restype = ctypes.c_bool

	if hasattr(dll, "OperatorConfig_set_int"):
		dll.OperatorConfig_set_int.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.OperatorConfig_set_int.restype = None

	if hasattr(dll, "OperatorConfig_set_double"):
		dll.OperatorConfig_set_double.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_double, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.OperatorConfig_set_double.restype = None

	if hasattr(dll, "OperatorConfig_set_bool"):
		dll.OperatorConfig_set_bool.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_bool, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.OperatorConfig_set_bool.restype = None

	if hasattr(dll, "OperatorConfig_get_num_config"):
		dll.OperatorConfig_get_num_config.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.OperatorConfig_get_num_config.restype = ctypes.c_int32

	if hasattr(dll, "OperatorConfig_get_config_option_name"):
		dll.OperatorConfig_get_config_option_name.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.OperatorConfig_get_config_option_name.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "OperatorConfig_get_config_option_printable_value"):
		dll.OperatorConfig_get_config_option_printable_value.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.OperatorConfig_get_config_option_printable_value.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "OperatorConfig_has_option"):
		dll.OperatorConfig_has_option.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.OperatorConfig_has_option.restype = ctypes.c_bool

	if hasattr(dll, "OperatorConfig_default_new_on_client"):
		dll.OperatorConfig_default_new_on_client.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.OperatorConfig_default_new_on_client.restype = ctypes.c_void_p

	if hasattr(dll, "OperatorConfig_empty_new_on_client"):
		dll.OperatorConfig_empty_new_on_client.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.OperatorConfig_empty_new_on_client.restype = ctypes.c_void_p

	#-------------------------------------------------------------------------------
	# OperatorSpecification
	#-------------------------------------------------------------------------------
	if hasattr(dll, "Operator_specification_new"):
		dll.Operator_specification_new.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_specification_new.restype = ctypes.c_void_p

	if hasattr(dll, "Operator_empty_specification_new"):
		dll.Operator_empty_specification_new.argtypes = None
		dll.Operator_empty_specification_new.restype = ctypes.c_void_p

	if hasattr(dll, "Operator_specification_delete"):
		dll.Operator_specification_delete.argtypes = (ctypes.c_void_p, )
		dll.Operator_specification_delete.restype = None

	if hasattr(dll, "Operator_specification_GetDescription"):
		dll.Operator_specification_GetDescription.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_specification_GetDescription.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "Operator_specification_SetDescription"):
		dll.Operator_specification_SetDescription.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_specification_SetDescription.restype = None

	if hasattr(dll, "Operator_specification_SetProperty"):
		dll.Operator_specification_SetProperty.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_specification_SetProperty.restype = None

	if hasattr(dll, "Operator_specification_GetNumPins"):
		dll.Operator_specification_GetNumPins.argtypes = (ctypes.c_void_p, ctypes.c_bool, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_specification_GetNumPins.restype = ctypes.c_int32

	if hasattr(dll, "Operator_specification_GetPinName"):
		dll.Operator_specification_GetPinName.argtypes = (ctypes.c_void_p, ctypes.c_bool, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_specification_GetPinName.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "Operator_specification_GetPinNumTypeNames"):
		dll.Operator_specification_GetPinNumTypeNames.argtypes = (ctypes.c_void_p, ctypes.c_bool, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_specification_GetPinNumTypeNames.restype = ctypes.c_int32

	if hasattr(dll, "Operator_specification_FillPinNumbers"):
		dll.Operator_specification_FillPinNumbers.argtypes = (ctypes.c_void_p, ctypes.c_bool, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_specification_FillPinNumbers.restype = None

	if hasattr(dll, "Operator_specification_GetPinTypeName"):
		dll.Operator_specification_GetPinTypeName.argtypes = (ctypes.c_void_p, ctypes.c_bool, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_specification_GetPinTypeName.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "Operator_specification_IsPinOptional"):
		dll.Operator_specification_IsPinOptional.argtypes = (ctypes.c_void_p, ctypes.c_bool, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_specification_IsPinOptional.restype = ctypes.c_bool

	if hasattr(dll, "Operator_specification_GetPinDocument"):
		dll.Operator_specification_GetPinDocument.argtypes = (ctypes.c_void_p, ctypes.c_bool, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_specification_GetPinDocument.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "Operator_specification_IsPinEllipsis"):
		dll.Operator_specification_IsPinEllipsis.argtypes = (ctypes.c_void_p, ctypes.c_bool, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_specification_IsPinEllipsis.restype = ctypes.c_bool

	if hasattr(dll, "Operator_specification_IsPinInPlace"):
		dll.Operator_specification_IsPinInPlace.argtypes = (ctypes.c_void_p, ctypes.c_bool, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_specification_IsPinInPlace.restype = ctypes.c_bool

	if hasattr(dll, "Operator_specification_GetProperties"):
		dll.Operator_specification_GetProperties.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_specification_GetProperties.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "Operator_specification_GetNumProperties"):
		dll.Operator_specification_GetNumProperties.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_specification_GetNumProperties.restype = ctypes.c_int32

	if hasattr(dll, "Operator_specification_GetPropertyKey"):
		dll.Operator_specification_GetPropertyKey.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_specification_GetPropertyKey.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "Operator_specification_SetPin"):
		dll.Operator_specification_SetPin.argtypes = (ctypes.c_void_p, ctypes.c_bool, ctypes.c_int32, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.c_int32, ctypes.POINTER(ctypes.POINTER(ctypes.c_char)), ctypes.c_bool, ctypes.c_bool, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_specification_SetPin.restype = None

	if hasattr(dll, "Operator_specification_SetPinDerivedClass"):
		dll.Operator_specification_SetPinDerivedClass.argtypes = (ctypes.c_void_p, ctypes.c_bool, ctypes.c_int32, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.c_int32, ctypes.POINTER(ctypes.POINTER(ctypes.c_char)), ctypes.c_bool, ctypes.c_bool, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_specification_SetPinDerivedClass.restype = None

	if hasattr(dll, "Operator_specification_SetPinAliases"):
		dll.Operator_specification_SetPinAliases.argtypes = (ctypes.c_void_p, ctypes.c_bool, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.POINTER(ctypes.c_char)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_specification_SetPinAliases.restype = None

	if hasattr(dll, "Operator_specification_AddPinAlias"):
		dll.Operator_specification_AddPinAlias.argtypes = (ctypes.c_void_p, ctypes.c_bool, ctypes.c_int32, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_specification_AddPinAlias.restype = None

	if hasattr(dll, "Operator_specification_AddBoolConfigOption"):
		dll.Operator_specification_AddBoolConfigOption.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_bool, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_specification_AddBoolConfigOption.restype = None

	if hasattr(dll, "Operator_specification_AddIntConfigOption"):
		dll.Operator_specification_AddIntConfigOption.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_int32, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_specification_AddIntConfigOption.restype = None

	if hasattr(dll, "Operator_specification_AddDoubleConfigOption"):
		dll.Operator_specification_AddDoubleConfigOption.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_double, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_specification_AddDoubleConfigOption.restype = None

	if hasattr(dll, "Operator_specification_GetNumConfigOptions"):
		dll.Operator_specification_GetNumConfigOptions.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_specification_GetNumConfigOptions.restype = ctypes.c_int32

	if hasattr(dll, "Operator_specification_GetConfigName"):
		dll.Operator_specification_GetConfigName.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_specification_GetConfigName.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "Operator_specification_GetConfigNumTypeNames"):
		dll.Operator_specification_GetConfigNumTypeNames.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_specification_GetConfigNumTypeNames.restype = ctypes.c_int32

	if hasattr(dll, "Operator_specification_GetConfigTypeName"):
		dll.Operator_specification_GetConfigTypeName.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_specification_GetConfigTypeName.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "Operator_specification_GetConfigPrintableDefaultValue"):
		dll.Operator_specification_GetConfigPrintableDefaultValue.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_specification_GetConfigPrintableDefaultValue.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "Operator_specification_GetConfigDescription"):
		dll.Operator_specification_GetConfigDescription.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_specification_GetConfigDescription.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "Operator_specification_GetPinDerivedClassTypeName"):
		dll.Operator_specification_GetPinDerivedClassTypeName.argtypes = (ctypes.c_void_p, ctypes.c_bool, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_specification_GetPinDerivedClassTypeName.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "Operator_specification_SetVersion"):
		dll.Operator_specification_SetVersion.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_specification_SetVersion.restype = None

	if hasattr(dll, "Operator_specification_GetVersion"):
		dll.Operator_specification_GetVersion.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_specification_GetVersion.restype = ctypes.c_void_p

	if hasattr(dll, "Operator_specification_GetPinNumAliases"):
		dll.Operator_specification_GetPinNumAliases.argtypes = (ctypes.c_void_p, ctypes.c_bool, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_specification_GetPinNumAliases.restype = ctypes.c_int32

	if hasattr(dll, "Operator_specification_GetPinAlias"):
		dll.Operator_specification_GetPinAlias.argtypes = (ctypes.c_void_p, ctypes.c_bool, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_specification_GetPinAlias.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "Operator_specification_new_on_client"):
		dll.Operator_specification_new_on_client.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Operator_specification_new_on_client.restype = ctypes.c_void_p

	#-------------------------------------------------------------------------------
	# PropertyField
	#-------------------------------------------------------------------------------
	if hasattr(dll, "PropertyField_Delete"):
		dll.PropertyField_Delete.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.PropertyField_Delete.restype = None

	if hasattr(dll, "PropertyField_GetData"):
		dll.PropertyField_GetData.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.PropertyField_GetData.restype = ctypes.POINTER(ctypes.c_int32)

	if hasattr(dll, "PropertyField_GetDataPointer"):
		dll.PropertyField_GetDataPointer.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.PropertyField_GetDataPointer.restype = ctypes.POINTER(ctypes.c_int32)

	if hasattr(dll, "PropertyField_GetScoping"):
		dll.PropertyField_GetScoping.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.PropertyField_GetScoping.restype = ctypes.POINTER(ctypes.c_int32)

	if hasattr(dll, "PropertyField_GetEntityData"):
		dll.PropertyField_GetEntityData.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.PropertyField_GetEntityData.restype = ctypes.POINTER(ctypes.c_int32)

	if hasattr(dll, "PropertyField_GetEntityDataById"):
		dll.PropertyField_GetEntityDataById.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.PropertyField_GetEntityDataById.restype = ctypes.POINTER(ctypes.c_int32)

	if hasattr(dll, "PropertyField_GetLocation"):
		dll.PropertyField_GetLocation.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.PropertyField_GetLocation.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "CSPropertyField_new"):
		dll.CSPropertyField_new.argtypes = (ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSPropertyField_new.restype = ctypes.c_void_p

	if hasattr(dll, "CSPropertyField_newWithTransformation"):
		dll.CSPropertyField_newWithTransformation.argtypes = (ctypes.c_int32, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSPropertyField_newWithTransformation.restype = ctypes.c_void_p

	if hasattr(dll, "CSPropertyField_Delete"):
		dll.CSPropertyField_Delete.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSPropertyField_Delete.restype = None

	if hasattr(dll, "CSPropertyField_GetData"):
		dll.CSPropertyField_GetData.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSPropertyField_GetData.restype = ctypes.POINTER(ctypes.c_int32)

	if hasattr(dll, "CSPropertyField_GetData_For_DpfVector"):
		dll.CSPropertyField_GetData_For_DpfVector.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.POINTER(ctypes.c_int32)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSPropertyField_GetData_For_DpfVector.restype = None

	if hasattr(dll, "CSPropertyField_GetDataPointer"):
		dll.CSPropertyField_GetDataPointer.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSPropertyField_GetDataPointer.restype = ctypes.POINTER(ctypes.c_int32)

	if hasattr(dll, "CSPropertyField_GetDataPointer_For_DpfVector"):
		dll.CSPropertyField_GetDataPointer_For_DpfVector.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.POINTER(ctypes.c_int32)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSPropertyField_GetDataPointer_For_DpfVector.restype = None

	if hasattr(dll, "CSPropertyField_GetCScoping"):
		dll.CSPropertyField_GetCScoping.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSPropertyField_GetCScoping.restype = ctypes.c_void_p

	if hasattr(dll, "CSPropertyField_GetEntityData"):
		dll.CSPropertyField_GetEntityData.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSPropertyField_GetEntityData.restype = ctypes.POINTER(ctypes.c_int32)

	if hasattr(dll, "CSPropertyField_GetEntityDataById"):
		dll.CSPropertyField_GetEntityDataById.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSPropertyField_GetEntityDataById.restype = ctypes.POINTER(ctypes.c_int32)

	if hasattr(dll, "CSPropertyField_GetNumberElementaryData"):
		dll.CSPropertyField_GetNumberElementaryData.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSPropertyField_GetNumberElementaryData.restype = ctypes.c_int32

	if hasattr(dll, "CSPropertyField_ElementaryDataSize"):
		dll.CSPropertyField_ElementaryDataSize.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSPropertyField_ElementaryDataSize.restype = ctypes.c_int32

	if hasattr(dll, "CSPropertyField_PushBack"):
		dll.CSPropertyField_PushBack.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSPropertyField_PushBack.restype = None

	if hasattr(dll, "CSPropertyField_SetData"):
		dll.CSPropertyField_SetData.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSPropertyField_SetData.restype = None

	if hasattr(dll, "CSPropertyField_SetDataWithCollection"):
		dll.CSPropertyField_SetDataWithCollection.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSPropertyField_SetDataWithCollection.restype = None

	if hasattr(dll, "CSPropertyField_SetDataPointerWithCollection"):
		dll.CSPropertyField_SetDataPointerWithCollection.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSPropertyField_SetDataPointerWithCollection.restype = None

	if hasattr(dll, "CSPropertyField_SetDataPointer"):
		dll.CSPropertyField_SetDataPointer.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSPropertyField_SetDataPointer.restype = None

	if hasattr(dll, "CSPropertyField_SetScoping"):
		dll.CSPropertyField_SetScoping.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSPropertyField_SetScoping.restype = None

	if hasattr(dll, "CSPropertyField_SetCScoping"):
		dll.CSPropertyField_SetCScoping.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSPropertyField_SetCScoping.restype = None

	if hasattr(dll, "CSPropertyField_SetEntityData"):
		dll.CSPropertyField_SetEntityData.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSPropertyField_SetEntityData.restype = None

	if hasattr(dll, "CSPropertyField_Resize"):
		dll.CSPropertyField_Resize.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSPropertyField_Resize.restype = None

	if hasattr(dll, "CSPropertyField_Reserve"):
		dll.CSPropertyField_Reserve.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSPropertyField_Reserve.restype = None

	if hasattr(dll, "CSPropertyField_GetEntityData_For_DpfVector"):
		dll.CSPropertyField_GetEntityData_For_DpfVector.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.POINTER(ctypes.c_int32)), ctypes.POINTER(ctypes.c_int32), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSPropertyField_GetEntityData_For_DpfVector.restype = None

	if hasattr(dll, "CSPropertyField_GetEntityDataById_For_DpfVector"):
		dll.CSPropertyField_GetEntityDataById_For_DpfVector.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.POINTER(ctypes.c_int32)), ctypes.POINTER(ctypes.c_int32), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSPropertyField_GetEntityDataById_For_DpfVector.restype = None

	if hasattr(dll, "CSProperty_GetDataFast"):
		dll.CSProperty_GetDataFast.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.POINTER(ctypes.c_int32)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSProperty_GetDataFast.restype = ctypes.c_bool

	if hasattr(dll, "CSPropertyField_GetLocation"):
		dll.CSPropertyField_GetLocation.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSPropertyField_GetLocation.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "CSPropertyField_GetDataSize"):
		dll.CSPropertyField_GetDataSize.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSPropertyField_GetDataSize.restype = ctypes.c_int32

	if hasattr(dll, "CSPropertyField_GetEntityId"):
		dll.CSPropertyField_GetEntityId.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSPropertyField_GetEntityId.restype = ctypes.c_int32

	if hasattr(dll, "CSPropertyField_GetEntityIndex"):
		dll.CSPropertyField_GetEntityIndex.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSPropertyField_GetEntityIndex.restype = ctypes.c_int32

	if hasattr(dll, "CSPropertyField_GetSharedFieldDefinition"):
		dll.CSPropertyField_GetSharedFieldDefinition.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSPropertyField_GetSharedFieldDefinition.restype = ctypes.c_void_p

	if hasattr(dll, "CSPropertyField_SetFieldDefinition"):
		dll.CSPropertyField_SetFieldDefinition.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSPropertyField_SetFieldDefinition.restype = None

	if hasattr(dll, "CSPropertyField_GetName"):
		dll.CSPropertyField_GetName.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSPropertyField_GetName.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "CSPropertyField_SetName"):
		dll.CSPropertyField_SetName.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSPropertyField_SetName.restype = None

	if hasattr(dll, "CSPropertyField_GetFastAccessPtr"):
		dll.CSPropertyField_GetFastAccessPtr.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSPropertyField_GetFastAccessPtr.restype = ctypes.c_void_p

	if hasattr(dll, "Property_GetDataFast"):
		dll.Property_GetDataFast.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.POINTER(ctypes.c_int32)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), )
		dll.Property_GetDataFast.restype = ctypes.c_bool

	if hasattr(dll, "CSPropertyField_new_on_client"):
		dll.CSPropertyField_new_on_client.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSPropertyField_new_on_client.restype = ctypes.c_void_p

	if hasattr(dll, "CSPropertyField_getCopy"):
		dll.CSPropertyField_getCopy.argtypes = (ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSPropertyField_getCopy.restype = ctypes.c_void_p

	#-------------------------------------------------------------------------------
	# RemoteWorkflow
	#-------------------------------------------------------------------------------
	if hasattr(dll, "RemoteWorkflow_new"):
		dll.RemoteWorkflow_new.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.RemoteWorkflow_new.restype = ctypes.c_void_p

	if hasattr(dll, "RemoteWorkflow_get_workflow_id"):
		dll.RemoteWorkflow_get_workflow_id.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.RemoteWorkflow_get_workflow_id.restype = ctypes.c_int32

	if hasattr(dll, "RemoteWorkflow_get_streams"):
		dll.RemoteWorkflow_get_streams.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.RemoteWorkflow_get_streams.restype = ctypes.c_void_p

	if hasattr(dll, "RemoteWorkFlow_delete"):
		dll.RemoteWorkFlow_delete.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.RemoteWorkFlow_delete.restype = None

	#-------------------------------------------------------------------------------
	# RemoteOperator
	#-------------------------------------------------------------------------------
	if hasattr(dll, "RemoteOperator_new"):
		dll.RemoteOperator_new.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.RemoteOperator_new.restype = ctypes.c_void_p

	if hasattr(dll, "RemoteOperator_get_streams"):
		dll.RemoteOperator_get_streams.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.RemoteOperator_get_streams.restype = ctypes.c_void_p

	if hasattr(dll, "RemoteOperator_get_operator_id"):
		dll.RemoteOperator_get_operator_id.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.RemoteOperator_get_operator_id.restype = ctypes.c_int32

	if hasattr(dll, "RemoteOperator_hold_streams"):
		dll.RemoteOperator_hold_streams.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.RemoteOperator_hold_streams.restype = None

	#-------------------------------------------------------------------------------
	# ResultDefinition
	#-------------------------------------------------------------------------------
	if hasattr(dll, "ResultDefinition_new"):
		dll.ResultDefinition_new.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultDefinition_new.restype = ctypes.c_void_p

	if hasattr(dll, "ResultDefinition_delete"):
		dll.ResultDefinition_delete.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultDefinition_delete.restype = None

	if hasattr(dll, "ResultDefinition_SetCriteria"):
		dll.ResultDefinition_SetCriteria.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultDefinition_SetCriteria.restype = None

	if hasattr(dll, "ResultDefinition_GetCriteria"):
		dll.ResultDefinition_GetCriteria.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultDefinition_GetCriteria.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "ResultDefinition_SetSubCriteria"):
		dll.ResultDefinition_SetSubCriteria.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultDefinition_SetSubCriteria.restype = None

	if hasattr(dll, "ResultDefinition_GetSubCriteria"):
		dll.ResultDefinition_GetSubCriteria.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultDefinition_GetSubCriteria.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "ResultDefinition_SetLocation"):
		dll.ResultDefinition_SetLocation.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultDefinition_SetLocation.restype = None

	if hasattr(dll, "ResultDefinition_GetLocation"):
		dll.ResultDefinition_GetLocation.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultDefinition_GetLocation.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "ResultDefinition_SetFieldCSLocation"):
		dll.ResultDefinition_SetFieldCSLocation.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultDefinition_SetFieldCSLocation.restype = None

	if hasattr(dll, "ResultDefinition_GetFieldCSLocation"):
		dll.ResultDefinition_GetFieldCSLocation.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultDefinition_GetFieldCSLocation.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "ResultDefinition_SetUserCS"):
		dll.ResultDefinition_SetUserCS.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultDefinition_SetUserCS.restype = None

	if hasattr(dll, "ResultDefinition_GetUserCS"):
		dll.ResultDefinition_GetUserCS.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultDefinition_GetUserCS.restype = ctypes.POINTER(ctypes.c_double)

	if hasattr(dll, "ResultDefinition_SetMeshScoping"):
		dll.ResultDefinition_SetMeshScoping.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultDefinition_SetMeshScoping.restype = None

	if hasattr(dll, "ResultDefinition_GetMeshScoping"):
		dll.ResultDefinition_GetMeshScoping.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultDefinition_GetMeshScoping.restype = ctypes.c_void_p

	if hasattr(dll, "ResultDefinition_SetCyclicSectorsScoping"):
		dll.ResultDefinition_SetCyclicSectorsScoping.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultDefinition_SetCyclicSectorsScoping.restype = None

	if hasattr(dll, "ResultDefinition_GetCyclicSectorsScoping"):
		dll.ResultDefinition_GetCyclicSectorsScoping.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultDefinition_GetCyclicSectorsScoping.restype = ctypes.c_void_p

	if hasattr(dll, "ResultDefinition_SetScopingByIds"):
		dll.ResultDefinition_SetScopingByIds.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultDefinition_SetScopingByIds.restype = None

	if hasattr(dll, "ResultDefinition_SetUnit"):
		dll.ResultDefinition_SetUnit.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultDefinition_SetUnit.restype = None

	if hasattr(dll, "ResultDefinition_GetUnit"):
		dll.ResultDefinition_GetUnit.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultDefinition_GetUnit.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "ResultDefinition_SetResultFilePath"):
		dll.ResultDefinition_SetResultFilePath.argtypes = (ctypes.c_void_p, ctypes.c_wchar_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultDefinition_SetResultFilePath.restype = None

	if hasattr(dll, "ResultDefinition_GetResultFilePath"):
		dll.ResultDefinition_GetResultFilePath.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultDefinition_GetResultFilePath.restype = ctypes.c_wchar_p

	if hasattr(dll, "ResultDefinition_SetIndexParam"):
		dll.ResultDefinition_SetIndexParam.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultDefinition_SetIndexParam.restype = None

	if hasattr(dll, "ResultDefinition_GetIndexParam"):
		dll.ResultDefinition_GetIndexParam.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultDefinition_GetIndexParam.restype = ctypes.c_bool

	if hasattr(dll, "ResultDefinition_SetCoefParam"):
		dll.ResultDefinition_SetCoefParam.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_double, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultDefinition_SetCoefParam.restype = None

	if hasattr(dll, "ResultDefinition_GetCoefParam"):
		dll.ResultDefinition_GetCoefParam.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultDefinition_GetCoefParam.restype = ctypes.c_bool

	#-------------------------------------------------------------------------------
	# ResultInfo
	#-------------------------------------------------------------------------------
	if hasattr(dll, "ResultInfo_new"):
		dll.ResultInfo_new.argtypes = (ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_new.restype = ctypes.c_void_p

	if hasattr(dll, "ResultInfo_delete"):
		dll.ResultInfo_delete.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_delete.restype = None

	if hasattr(dll, "ResultInfo_GetAnalysisType"):
		dll.ResultInfo_GetAnalysisType.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_GetAnalysisType.restype = ctypes.c_int32

	if hasattr(dll, "ResultInfo_GetPhysicsType"):
		dll.ResultInfo_GetPhysicsType.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_GetPhysicsType.restype = ctypes.c_int32

	if hasattr(dll, "ResultInfo_GetAnalysisTypeName"):
		dll.ResultInfo_GetAnalysisTypeName.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_GetAnalysisTypeName.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "ResultInfo_GetPhysicsTypeName"):
		dll.ResultInfo_GetPhysicsTypeName.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_GetPhysicsTypeName.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "ResultInfo_GetAnsysUnitSystemEnum"):
		dll.ResultInfo_GetAnsysUnitSystemEnum.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_GetAnsysUnitSystemEnum.restype = ctypes.c_int32

	if hasattr(dll, "ResultInfo_GetCustomUnitSystemStrings"):
		dll.ResultInfo_GetCustomUnitSystemStrings.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_GetCustomUnitSystemStrings.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "ResultInfo_GetUnitSystemName"):
		dll.ResultInfo_GetUnitSystemName.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_GetUnitSystemName.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "ResultInfo_GetNumberOfResults"):
		dll.ResultInfo_GetNumberOfResults.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_GetNumberOfResults.restype = ctypes.c_int32

	if hasattr(dll, "ResultInfo_GetResultNumberOfComponents"):
		dll.ResultInfo_GetResultNumberOfComponents.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_GetResultNumberOfComponents.restype = ctypes.c_int32

	if hasattr(dll, "ResultInfo_GetResultDimensionalityNature"):
		dll.ResultInfo_GetResultDimensionalityNature.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_GetResultDimensionalityNature.restype = ctypes.c_int32

	if hasattr(dll, "ResultInfo_GetResultHomogeneity"):
		dll.ResultInfo_GetResultHomogeneity.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_GetResultHomogeneity.restype = ctypes.c_int32

	if hasattr(dll, "ResultInfo_GetResultHomogeneityName"):
		dll.ResultInfo_GetResultHomogeneityName.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_GetResultHomogeneityName.restype = None

	if hasattr(dll, "ResultInfo_GetResultLocation"):
		dll.ResultInfo_GetResultLocation.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_GetResultLocation.restype = None

	if hasattr(dll, "ResultInfo_GetResultDescription"):
		dll.ResultInfo_GetResultDescription.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_GetResultDescription.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "ResultInfo_GetResultName"):
		dll.ResultInfo_GetResultName.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_GetResultName.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "ResultInfo_GetResultPhysicsName"):
		dll.ResultInfo_GetResultPhysicsName.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_GetResultPhysicsName.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "ResultInfo_GetResultScriptingName"):
		dll.ResultInfo_GetResultScriptingName.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_GetResultScriptingName.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "ResultInfo_GetResultUnitSymbol"):
		dll.ResultInfo_GetResultUnitSymbol.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_GetResultUnitSymbol.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "ResultInfo_GetNumberOfSubResults"):
		dll.ResultInfo_GetNumberOfSubResults.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_GetNumberOfSubResults.restype = ctypes.c_int32

	if hasattr(dll, "ResultInfo_GetSubResultName"):
		dll.ResultInfo_GetSubResultName.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_GetSubResultName.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "ResultInfo_GetSubResultOperatorName"):
		dll.ResultInfo_GetSubResultOperatorName.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_GetSubResultOperatorName.restype = None

	if hasattr(dll, "ResultInfo_GetSubResultDescription"):
		dll.ResultInfo_GetSubResultDescription.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_GetSubResultDescription.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "ResultInfo_GetCyclicSupport"):
		dll.ResultInfo_GetCyclicSupport.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_GetCyclicSupport.restype = ctypes.c_void_p

	if hasattr(dll, "ResultInfo_GetCyclicSymmetryType"):
		dll.ResultInfo_GetCyclicSymmetryType.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_GetCyclicSymmetryType.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "ResultInfo_HasCyclicSymmetry"):
		dll.ResultInfo_HasCyclicSymmetry.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_HasCyclicSymmetry.restype = ctypes.c_bool

	if hasattr(dll, "ResultInfo_FillResultDimensionality"):
		dll.ResultInfo_FillResultDimensionality.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_FillResultDimensionality.restype = None

	if hasattr(dll, "ResultInfo_GetSolverVersion"):
		dll.ResultInfo_GetSolverVersion.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_GetSolverVersion.restype = None

	if hasattr(dll, "ResultInfo_GetSolveDateAndTime"):
		dll.ResultInfo_GetSolveDateAndTime.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_GetSolveDateAndTime.restype = None

	if hasattr(dll, "ResultInfo_GetUserName"):
		dll.ResultInfo_GetUserName.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_GetUserName.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "ResultInfo_GetJobName"):
		dll.ResultInfo_GetJobName.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_GetJobName.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "ResultInfo_GetProductName"):
		dll.ResultInfo_GetProductName.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_GetProductName.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "ResultInfo_GetMainTitle"):
		dll.ResultInfo_GetMainTitle.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_GetMainTitle.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "ResultInfo_SetUnitSystem"):
		dll.ResultInfo_SetUnitSystem.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_SetUnitSystem.restype = None

	if hasattr(dll, "ResultInfo_SetCustomUnitSystem"):
		dll.ResultInfo_SetCustomUnitSystem.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_SetCustomUnitSystem.restype = None

	if hasattr(dll, "ResultInfo_AddResult"):
		dll.ResultInfo_AddResult.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_AddResult.restype = None

	if hasattr(dll, "ResultInfo_AddQualifiersForResult"):
		dll.ResultInfo_AddQualifiersForResult.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_AddQualifiersForResult.restype = None

	if hasattr(dll, "ResultInfo_AddQualifiersForAllResults"):
		dll.ResultInfo_AddQualifiersForAllResults.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_AddQualifiersForAllResults.restype = None

	if hasattr(dll, "ResultInfo_AddQualifiersSupport"):
		dll.ResultInfo_AddQualifiersSupport.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_AddQualifiersSupport.restype = None

	if hasattr(dll, "ResultInfo_GetQualifiersForResult"):
		dll.ResultInfo_GetQualifiersForResult.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_GetQualifiersForResult.restype = ctypes.c_void_p

	if hasattr(dll, "ResultInfo_GetQualifierLabelSupport"):
		dll.ResultInfo_GetQualifierLabelSupport.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_GetQualifierLabelSupport.restype = ctypes.c_void_p

	if hasattr(dll, "ResultInfo_GetAvailableQualifierLabelsAsStringColl"):
		dll.ResultInfo_GetAvailableQualifierLabelsAsStringColl.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_GetAvailableQualifierLabelsAsStringColl.restype = ctypes.c_void_p

	if hasattr(dll, "ResultInfo_AddStringProperty"):
		dll.ResultInfo_AddStringProperty.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_AddStringProperty.restype = None

	if hasattr(dll, "ResultInfo_AddIntProperty"):
		dll.ResultInfo_AddIntProperty.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_AddIntProperty.restype = None

	if hasattr(dll, "ResultInfo_GetStringProperty"):
		dll.ResultInfo_GetStringProperty.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_GetStringProperty.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "ResultInfo_GetIntProperty"):
		dll.ResultInfo_GetIntProperty.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.ResultInfo_GetIntProperty.restype = ctypes.c_int32

	#-------------------------------------------------------------------------------
	# Scoping
	#-------------------------------------------------------------------------------
	if hasattr(dll, "Scoping_new"):
		dll.Scoping_new.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Scoping_new.restype = ctypes.c_void_p

	if hasattr(dll, "Scoping_new_WithData"):
		dll.Scoping_new_WithData.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Scoping_new_WithData.restype = ctypes.c_void_p

	if hasattr(dll, "Scoping_delete"):
		dll.Scoping_delete.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Scoping_delete.restype = None

	if hasattr(dll, "Scoping_SetData"):
		dll.Scoping_SetData.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Scoping_SetData.restype = None

	if hasattr(dll, "Scoping_GetData"):
		dll.Scoping_GetData.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.POINTER(ctypes.c_char)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Scoping_GetData.restype = ctypes.POINTER(ctypes.c_int32)

	if hasattr(dll, "Scoping_SetIds"):
		dll.Scoping_SetIds.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Scoping_SetIds.restype = None

	if hasattr(dll, "Scoping_SetIdsWithCollection"):
		dll.Scoping_SetIdsWithCollection.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Scoping_SetIdsWithCollection.restype = None

	if hasattr(dll, "Scoping_GetIds"):
		dll.Scoping_GetIds.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Scoping_GetIds.restype = ctypes.POINTER(ctypes.c_int32)

	if hasattr(dll, "Scoping_GetIds_For_DpfVector"):
		dll.Scoping_GetIds_For_DpfVector.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.POINTER(ctypes.c_int32)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Scoping_GetIds_For_DpfVector.restype = None

	if hasattr(dll, "Scoping_GetSize"):
		dll.Scoping_GetSize.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Scoping_GetSize.restype = ctypes.c_int32

	if hasattr(dll, "Scoping_SetLocation"):
		dll.Scoping_SetLocation.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Scoping_SetLocation.restype = None

	if hasattr(dll, "Scoping_GetLocation"):
		dll.Scoping_GetLocation.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Scoping_GetLocation.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "Scoping_SetEntity"):
		dll.Scoping_SetEntity.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Scoping_SetEntity.restype = None

	if hasattr(dll, "Scoping_IdByIndex"):
		dll.Scoping_IdByIndex.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Scoping_IdByIndex.restype = ctypes.c_int32

	if hasattr(dll, "Scoping_IndexById"):
		dll.Scoping_IndexById.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Scoping_IndexById.restype = ctypes.c_int32

	if hasattr(dll, "Scoping_Resize"):
		dll.Scoping_Resize.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Scoping_Resize.restype = None

	if hasattr(dll, "Scoping_Reserve"):
		dll.Scoping_Reserve.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Scoping_Reserve.restype = None

	if hasattr(dll, "Scoping_GetIdsHash"):
		dll.Scoping_GetIdsHash.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Scoping_GetIdsHash.restype = ctypes.c_int32

	if hasattr(dll, "Scoping_fast_access_ptr"):
		dll.Scoping_fast_access_ptr.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Scoping_fast_access_ptr.restype = ctypes.c_void_p

	if hasattr(dll, "Scoping_fast_get_ids"):
		dll.Scoping_fast_get_ids.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), )
		dll.Scoping_fast_get_ids.restype = ctypes.POINTER(ctypes.c_int32)

	if hasattr(dll, "Scoping_fast_set_entity"):
		dll.Scoping_fast_set_entity.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, )
		dll.Scoping_fast_set_entity.restype = None

	if hasattr(dll, "Scoping_fast_id_by_index"):
		dll.Scoping_fast_id_by_index.argtypes = (ctypes.c_void_p, ctypes.c_int32, )
		dll.Scoping_fast_id_by_index.restype = ctypes.c_int32

	if hasattr(dll, "Scoping_fast_index_by_id"):
		dll.Scoping_fast_index_by_id.argtypes = (ctypes.c_void_p, ctypes.c_int32, )
		dll.Scoping_fast_index_by_id.restype = ctypes.c_int32

	if hasattr(dll, "Scoping_fast_get_size"):
		dll.Scoping_fast_get_size.argtypes = (ctypes.c_void_p, )
		dll.Scoping_fast_get_size.restype = ctypes.c_int32

	if hasattr(dll, "Scoping_new_on_client"):
		dll.Scoping_new_on_client.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Scoping_new_on_client.restype = ctypes.c_void_p

	if hasattr(dll, "Scoping_getCopy"):
		dll.Scoping_getCopy.argtypes = (ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Scoping_getCopy.restype = ctypes.c_void_p

	#-------------------------------------------------------------------------------
	# SemanticVersion
	#-------------------------------------------------------------------------------
	if hasattr(dll, "SemanticVersion_new"):
		dll.SemanticVersion_new.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.SemanticVersion_new.restype = ctypes.c_void_p

	if hasattr(dll, "SemanticVersion_getComponents"):
		dll.SemanticVersion_getComponents.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.SemanticVersion_getComponents.restype = None

	if hasattr(dll, "SemanticVersion_eq"):
		dll.SemanticVersion_eq.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.SemanticVersion_eq.restype = ctypes.c_bool

	if hasattr(dll, "SemanticVersion_lt"):
		dll.SemanticVersion_lt.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.SemanticVersion_lt.restype = ctypes.c_bool

	#-------------------------------------------------------------------------------
	# SerializationStream
	#-------------------------------------------------------------------------------
	if hasattr(dll, "SerializationStream_getOutputString"):
		dll.SerializationStream_getOutputString.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_size_t), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.SerializationStream_getOutputString.restype = ctypes.POINTER(ctypes.c_char)

	#-------------------------------------------------------------------------------
	# Session
	#-------------------------------------------------------------------------------
	if hasattr(dll, "sessionNew"):
		dll.sessionNew.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.sessionNew.restype = ctypes.c_void_p

	if hasattr(dll, "deleteSession"):
		dll.deleteSession.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.deleteSession.restype = None

	if hasattr(dll, "getSessionId"):
		dll.getSessionId.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.getSessionId.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "addWorkflow"):
		dll.addWorkflow.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.addWorkflow.restype = None

	if hasattr(dll, "getWorkflow"):
		dll.getWorkflow.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.getWorkflow.restype = ctypes.c_void_p

	if hasattr(dll, "getWorkflowByIndex"):
		dll.getWorkflowByIndex.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.getWorkflowByIndex.restype = ctypes.c_void_p

	if hasattr(dll, "flushWorkflows"):
		dll.flushWorkflows.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.flushWorkflows.restype = None

	if hasattr(dll, "getNumWorkflow"):
		dll.getNumWorkflow.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.getNumWorkflow.restype = ctypes.c_int32

	if hasattr(dll, "setLogger"):
		dll.setLogger.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.setLogger.restype = None

	if hasattr(dll, "setEventSystem"):
		dll.setEventSystem.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.setEventSystem.restype = None

	if hasattr(dll, "addBreakpoint"):
		dll.addBreakpoint.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.addBreakpoint.restype = ctypes.c_int32

	if hasattr(dll, "removeBreakpoint"):
		dll.removeBreakpoint.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.removeBreakpoint.restype = None

	if hasattr(dll, "resume"):
		dll.resume.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.resume.restype = None

	if hasattr(dll, "addEventHandler"):
		dll.addEventHandler.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.addEventHandler.restype = None

	if hasattr(dll, "createSignalEmitterInSession"):
		dll.createSignalEmitterInSession.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.createSignalEmitterInSession.restype = ctypes.c_void_p

	if hasattr(dll, "addExternalEventHandler"):
		dll.addExternalEventHandler.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.addExternalEventHandler.restype = None

	if hasattr(dll, "NotifyExternalEventHandlerDestruction"):
		dll.NotifyExternalEventHandlerDestruction.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.NotifyExternalEventHandlerDestruction.restype = None

	if hasattr(dll, "addWorkflowWithoutIdentifier"):
		dll.addWorkflowWithoutIdentifier.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.addWorkflowWithoutIdentifier.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "emitSignal"):
		dll.emitSignal.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.emitSignal.restype = None

	if hasattr(dll, "addEventHandlerType"):
		dll.addEventHandlerType.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.addEventHandlerType.restype = ctypes.c_bool

	if hasattr(dll, "addSignalEmitterType"):
		dll.addSignalEmitterType.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.addSignalEmitterType.restype = ctypes.c_bool

	if hasattr(dll, "sessionNew_on_client"):
		dll.sessionNew_on_client.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.sessionNew_on_client.restype = ctypes.c_void_p

	#-------------------------------------------------------------------------------
	# SpecificationExternalization
	#-------------------------------------------------------------------------------
	if hasattr(dll, "Specification_xml_export"):
		dll.Specification_xml_export.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Specification_xml_export.restype = None

	if hasattr(dll, "Specification_xml_import"):
		dll.Specification_xml_import.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Specification_xml_import.restype = None

	if hasattr(dll, "setSpecificationInCore"):
		dll.setSpecificationInCore.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.setSpecificationInCore.restype = None

	#-------------------------------------------------------------------------------
	# Streams
	#-------------------------------------------------------------------------------
	if hasattr(dll, "Streams_delete"):
		dll.Streams_delete.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Streams_delete.restype = None

	if hasattr(dll, "Streams_ReleaseHandles"):
		dll.Streams_ReleaseHandles.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Streams_ReleaseHandles.restype = None

	if hasattr(dll, "Streams_new"):
		dll.Streams_new.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Streams_new.restype = ctypes.c_void_p

	if hasattr(dll, "Streams_addExternalStream"):
		dll.Streams_addExternalStream.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Streams_addExternalStream.restype = None

	if hasattr(dll, "Streams_getExternalStream"):
		dll.Streams_getExternalStream.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Streams_getExternalStream.restype = ctypes.c_void_p

	if hasattr(dll, "Streams_addExternalStreamWithLabelSpace"):
		dll.Streams_addExternalStreamWithLabelSpace.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Streams_addExternalStreamWithLabelSpace.restype = None

	if hasattr(dll, "Streams_getExternalStreamWithLabelSpace"):
		dll.Streams_getExternalStreamWithLabelSpace.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Streams_getExternalStreamWithLabelSpace.restype = ctypes.c_void_p

	if hasattr(dll, "Streams_getDataSources"):
		dll.Streams_getDataSources.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Streams_getDataSources.restype = ctypes.c_void_p

	if hasattr(dll, "Streams_getCopy"):
		dll.Streams_getCopy.argtypes = (ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Streams_getCopy.restype = ctypes.c_void_p

	#-------------------------------------------------------------------------------
	# StringField
	#-------------------------------------------------------------------------------
	if hasattr(dll, "StringField_Delete"):
		dll.StringField_Delete.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.StringField_Delete.restype = None

	if hasattr(dll, "StringField_GetEntityData"):
		dll.StringField_GetEntityData.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.StringField_GetEntityData.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "StringField_GetNumberEntities"):
		dll.StringField_GetNumberEntities.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.StringField_GetNumberEntities.restype = ctypes.c_int32

	if hasattr(dll, "CSStringField_new"):
		dll.CSStringField_new.argtypes = (ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSStringField_new.restype = ctypes.c_void_p

	if hasattr(dll, "CSStringField_GetData_For_DpfVector"):
		dll.CSStringField_GetData_For_DpfVector.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.POINTER(ctypes.POINTER(ctypes.c_char))), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSStringField_GetData_For_DpfVector.restype = None

	if hasattr(dll, "CSStringField_GetEntityData_For_DpfVector"):
		dll.CSStringField_GetEntityData_For_DpfVector.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.POINTER(ctypes.POINTER(ctypes.c_char))), ctypes.POINTER(ctypes.c_int32), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSStringField_GetEntityData_For_DpfVector.restype = None

	if hasattr(dll, "CSStringField_GetEntityDataById_For_DpfVector"):
		dll.CSStringField_GetEntityDataById_For_DpfVector.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.POINTER(ctypes.POINTER(ctypes.c_char))), ctypes.POINTER(ctypes.c_int32), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSStringField_GetEntityDataById_For_DpfVector.restype = None

	if hasattr(dll, "StringField_GetEntityData_For_DpfVector"):
		dll.StringField_GetEntityData_For_DpfVector.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.POINTER(ctypes.POINTER(ctypes.c_char))), ctypes.POINTER(ctypes.c_int32), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.StringField_GetEntityData_For_DpfVector.restype = None

	if hasattr(dll, "StringField_GetEntityDataById_For_DpfVector"):
		dll.StringField_GetEntityDataById_For_DpfVector.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.POINTER(ctypes.POINTER(ctypes.c_char))), ctypes.POINTER(ctypes.c_int32), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.StringField_GetEntityDataById_For_DpfVector.restype = None

	if hasattr(dll, "CSStringField_GetData_For_DpfVector_with_size"):
		dll.CSStringField_GetData_For_DpfVector_with_size.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.POINTER(ctypes.POINTER(ctypes.c_char))), ctypes.POINTER(ctypes.POINTER(ctypes.c_uint64)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSStringField_GetData_For_DpfVector_with_size.restype = None

	if hasattr(dll, "CSStringField_GetEntityData_For_DpfVector_with_size"):
		dll.CSStringField_GetEntityData_For_DpfVector_with_size.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.POINTER(ctypes.POINTER(ctypes.c_char))), ctypes.POINTER(ctypes.POINTER(ctypes.c_uint64)), ctypes.POINTER(ctypes.c_int32), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSStringField_GetEntityData_For_DpfVector_with_size.restype = None

	if hasattr(dll, "CSStringField_GetEntityDataById_For_DpfVector_with_size"):
		dll.CSStringField_GetEntityDataById_For_DpfVector_with_size.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.POINTER(ctypes.POINTER(ctypes.c_char))), ctypes.POINTER(ctypes.POINTER(ctypes.c_uint64)), ctypes.POINTER(ctypes.c_int32), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSStringField_GetEntityDataById_For_DpfVector_with_size.restype = None

	if hasattr(dll, "StringField_GetEntityData_For_DpfVector_with_size"):
		dll.StringField_GetEntityData_For_DpfVector_with_size.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.POINTER(ctypes.POINTER(ctypes.c_char))), ctypes.POINTER(ctypes.POINTER(ctypes.c_uint64)), ctypes.POINTER(ctypes.c_int32), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.StringField_GetEntityData_For_DpfVector_with_size.restype = None

	if hasattr(dll, "StringField_GetEntityDataById_For_DpfVector_with_size"):
		dll.StringField_GetEntityDataById_For_DpfVector_with_size.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.POINTER(ctypes.POINTER(ctypes.c_char))), ctypes.POINTER(ctypes.POINTER(ctypes.c_uint64)), ctypes.POINTER(ctypes.c_int32), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.StringField_GetEntityDataById_For_DpfVector_with_size.restype = None

	if hasattr(dll, "CSStringField_GetCScoping"):
		dll.CSStringField_GetCScoping.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSStringField_GetCScoping.restype = ctypes.c_void_p

	if hasattr(dll, "CSStringField_GetDataSize"):
		dll.CSStringField_GetDataSize.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSStringField_GetDataSize.restype = ctypes.c_int32

	if hasattr(dll, "CSStringField_SetData"):
		dll.CSStringField_SetData.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.POINTER(ctypes.c_char)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSStringField_SetData.restype = None

	if hasattr(dll, "CSStringField_SetData_with_size"):
		dll.CSStringField_SetData_with_size.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.POINTER(ctypes.c_char)), ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSStringField_SetData_with_size.restype = None

	if hasattr(dll, "CSStringField_SetCScoping"):
		dll.CSStringField_SetCScoping.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSStringField_SetCScoping.restype = None

	if hasattr(dll, "CSStringField_SetDataPointer"):
		dll.CSStringField_SetDataPointer.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSStringField_SetDataPointer.restype = None

	if hasattr(dll, "CSStringField_PushBack"):
		dll.CSStringField_PushBack.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.POINTER(ctypes.c_char)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSStringField_PushBack.restype = None

	if hasattr(dll, "StringField_PushBack"):
		dll.StringField_PushBack.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.POINTER(ctypes.c_char)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.StringField_PushBack.restype = None

	if hasattr(dll, "CSStringField_PushBack_with_size"):
		dll.CSStringField_PushBack_with_size.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.POINTER(ctypes.c_char)), ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSStringField_PushBack_with_size.restype = None

	if hasattr(dll, "StringField_PushBack_with_size"):
		dll.StringField_PushBack_with_size.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.POINTER(ctypes.c_char)), ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.StringField_PushBack_with_size.restype = None

	if hasattr(dll, "CSStringField_Resize"):
		dll.CSStringField_Resize.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSStringField_Resize.restype = None

	if hasattr(dll, "CSStringField_Reserve"):
		dll.CSStringField_Reserve.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSStringField_Reserve.restype = None

	if hasattr(dll, "StringField_fast_access_ptr"):
		dll.StringField_fast_access_ptr.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.StringField_fast_access_ptr.restype = ctypes.c_void_p

	if hasattr(dll, "CSStringField_new_on_client"):
		dll.CSStringField_new_on_client.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSStringField_new_on_client.restype = ctypes.c_void_p

	if hasattr(dll, "CSStringField_getCopy"):
		dll.CSStringField_getCopy.argtypes = (ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSStringField_getCopy.restype = ctypes.c_void_p

	#-------------------------------------------------------------------------------
	# CustomTypeField
	#-------------------------------------------------------------------------------
	if hasattr(dll, "CSCustomTypeField_new"):
		dll.CSCustomTypeField_new.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.c_int32, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSCustomTypeField_new.restype = ctypes.c_void_p

	if hasattr(dll, "CSCustomTypeField_GetData_For_DpfVector"):
		dll.CSCustomTypeField_GetData_For_DpfVector.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSCustomTypeField_GetData_For_DpfVector.restype = None

	if hasattr(dll, "CSCustomTypeField_GetDataPointer_For_DpfVector"):
		dll.CSCustomTypeField_GetDataPointer_For_DpfVector.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.POINTER(ctypes.c_int32)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSCustomTypeField_GetDataPointer_For_DpfVector.restype = None

	if hasattr(dll, "CSCustomTypeField_GetEntityData_For_DpfVector"):
		dll.CSCustomTypeField_GetEntityData_For_DpfVector.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_int32), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSCustomTypeField_GetEntityData_For_DpfVector.restype = None

	if hasattr(dll, "CSCustomTypeField_GetEntityDataById_For_DpfVector"):
		dll.CSCustomTypeField_GetEntityDataById_For_DpfVector.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_int32), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSCustomTypeField_GetEntityDataById_For_DpfVector.restype = None

	if hasattr(dll, "CSCustomTypeField_GetCScoping"):
		dll.CSCustomTypeField_GetCScoping.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSCustomTypeField_GetCScoping.restype = ctypes.c_void_p

	if hasattr(dll, "CSCustomTypeField_GetNumberElementaryData"):
		dll.CSCustomTypeField_GetNumberElementaryData.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSCustomTypeField_GetNumberElementaryData.restype = ctypes.c_int32

	if hasattr(dll, "CSCustomTypeField_GetNumberOfComponents"):
		dll.CSCustomTypeField_GetNumberOfComponents.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSCustomTypeField_GetNumberOfComponents.restype = ctypes.c_int32

	if hasattr(dll, "CSCustomTypeField_GetDataSize"):
		dll.CSCustomTypeField_GetDataSize.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSCustomTypeField_GetDataSize.restype = ctypes.c_int32

	if hasattr(dll, "CSCustomTypeField_GetNumberEntities"):
		dll.CSCustomTypeField_GetNumberEntities.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSCustomTypeField_GetNumberEntities.restype = ctypes.c_int32

	if hasattr(dll, "CSCustomTypeField_GetPropertyDataTree"):
		dll.CSCustomTypeField_GetPropertyDataTree.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSCustomTypeField_GetPropertyDataTree.restype = ctypes.c_void_p

	if hasattr(dll, "CSCustomTypeField_SetData"):
		dll.CSCustomTypeField_SetData.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSCustomTypeField_SetData.restype = None

	if hasattr(dll, "CSCustomTypeField_SetDataPointer"):
		dll.CSCustomTypeField_SetDataPointer.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSCustomTypeField_SetDataPointer.restype = None

	if hasattr(dll, "CSCustomTypeField_SetCScoping"):
		dll.CSCustomTypeField_SetCScoping.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSCustomTypeField_SetCScoping.restype = None

	if hasattr(dll, "CSCustomTypeField_PushBack"):
		dll.CSCustomTypeField_PushBack.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSCustomTypeField_PushBack.restype = None

	if hasattr(dll, "CSCustomTypeField_SetDataWithCollection"):
		dll.CSCustomTypeField_SetDataWithCollection.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSCustomTypeField_SetDataWithCollection.restype = None

	if hasattr(dll, "CSCustomTypeField_SetDataPointerWithCollection"):
		dll.CSCustomTypeField_SetDataPointerWithCollection.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSCustomTypeField_SetDataPointerWithCollection.restype = None

	if hasattr(dll, "CSCustomTypeField_Resize"):
		dll.CSCustomTypeField_Resize.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSCustomTypeField_Resize.restype = None

	if hasattr(dll, "CSCustomTypeField_ResizeDataPointer"):
		dll.CSCustomTypeField_ResizeDataPointer.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSCustomTypeField_ResizeDataPointer.restype = None

	if hasattr(dll, "CSCustomTypeField_Reserve"):
		dll.CSCustomTypeField_Reserve.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSCustomTypeField_Reserve.restype = None

	if hasattr(dll, "CSCustomTypeField_GetType"):
		dll.CSCustomTypeField_GetType.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSCustomTypeField_GetType.restype = None

	if hasattr(dll, "CSCustomTypeField_GetSharedFieldDefinition"):
		dll.CSCustomTypeField_GetSharedFieldDefinition.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSCustomTypeField_GetSharedFieldDefinition.restype = ctypes.c_void_p

	if hasattr(dll, "CSCustomTypeField_GetSupport"):
		dll.CSCustomTypeField_GetSupport.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSCustomTypeField_GetSupport.restype = ctypes.c_void_p

	if hasattr(dll, "CSCustomTypeField_SetFieldDefinition"):
		dll.CSCustomTypeField_SetFieldDefinition.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSCustomTypeField_SetFieldDefinition.restype = None

	if hasattr(dll, "CSCustomTypeField_SetSupport"):
		dll.CSCustomTypeField_SetSupport.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSCustomTypeField_SetSupport.restype = None

	if hasattr(dll, "CSCustomTypeField_SetEntityData"):
		dll.CSCustomTypeField_SetEntityData.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSCustomTypeField_SetEntityData.restype = None

	if hasattr(dll, "CSCustomTypeField_GetName"):
		dll.CSCustomTypeField_GetName.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSCustomTypeField_GetName.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "CSCustomTypeField_SetName"):
		dll.CSCustomTypeField_SetName.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSCustomTypeField_SetName.restype = None

	if hasattr(dll, "CSCustomTypeField_GetEntityId"):
		dll.CSCustomTypeField_GetEntityId.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSCustomTypeField_GetEntityId.restype = ctypes.c_int32

	if hasattr(dll, "CSCustomTypeField_GetEntityIndex"):
		dll.CSCustomTypeField_GetEntityIndex.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSCustomTypeField_GetEntityIndex.restype = ctypes.c_int32

	if hasattr(dll, "CSCustomTypeField_new_on_client"):
		dll.CSCustomTypeField_new_on_client.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_int32, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSCustomTypeField_new_on_client.restype = ctypes.c_void_p

	if hasattr(dll, "CSCustomTypeField_getCopy"):
		dll.CSCustomTypeField_getCopy.argtypes = (ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.CSCustomTypeField_getCopy.restype = ctypes.c_void_p

	#-------------------------------------------------------------------------------
	# Support
	#-------------------------------------------------------------------------------
	if hasattr(dll, "Support_delete"):
		dll.Support_delete.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Support_delete.restype = None

	if hasattr(dll, "Support_isDomainMeshSupport"):
		dll.Support_isDomainMeshSupport.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Support_isDomainMeshSupport.restype = ctypes.c_bool

	if hasattr(dll, "Support_setAsDomainMeshSupport"):
		dll.Support_setAsDomainMeshSupport.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Support_setAsDomainMeshSupport.restype = None

	if hasattr(dll, "Support_getAsMeshedSupport"):
		dll.Support_getAsMeshedSupport.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Support_getAsMeshedSupport.restype = ctypes.c_void_p

	if hasattr(dll, "Support_getAsCyclicSupport"):
		dll.Support_getAsCyclicSupport.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Support_getAsCyclicSupport.restype = ctypes.c_void_p

	if hasattr(dll, "Support_getAsTimeFreqSupport"):
		dll.Support_getAsTimeFreqSupport.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Support_getAsTimeFreqSupport.restype = ctypes.c_void_p

	if hasattr(dll, "Support_getFieldSupportByProperty"):
		dll.Support_getFieldSupportByProperty.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Support_getFieldSupportByProperty.restype = ctypes.c_void_p

	if hasattr(dll, "Support_getPropertyFieldSupportByProperty"):
		dll.Support_getPropertyFieldSupportByProperty.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Support_getPropertyFieldSupportByProperty.restype = ctypes.c_void_p

	if hasattr(dll, "Support_getStringFieldSupportByProperty"):
		dll.Support_getStringFieldSupportByProperty.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Support_getStringFieldSupportByProperty.restype = ctypes.c_void_p

	if hasattr(dll, "Support_getPropertyNamesAsStringCollForFields"):
		dll.Support_getPropertyNamesAsStringCollForFields.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Support_getPropertyNamesAsStringCollForFields.restype = ctypes.c_void_p

	if hasattr(dll, "Support_getPropertyNamesAsStringCollForPropertyFields"):
		dll.Support_getPropertyNamesAsStringCollForPropertyFields.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Support_getPropertyNamesAsStringCollForPropertyFields.restype = ctypes.c_void_p

	if hasattr(dll, "Support_getPropertyNamesAsStringCollForStringFields"):
		dll.Support_getPropertyNamesAsStringCollForStringFields.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Support_getPropertyNamesAsStringCollForStringFields.restype = ctypes.c_void_p

	#-------------------------------------------------------------------------------
	# GenericSupport
	#-------------------------------------------------------------------------------
	if hasattr(dll, "GenericSupport_new"):
		dll.GenericSupport_new.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.GenericSupport_new.restype = ctypes.c_void_p

	if hasattr(dll, "GenericSupport_setFieldSupportOfProperty"):
		dll.GenericSupport_setFieldSupportOfProperty.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.GenericSupport_setFieldSupportOfProperty.restype = None

	if hasattr(dll, "GenericSupport_setPropertyFieldSupportOfProperty"):
		dll.GenericSupport_setPropertyFieldSupportOfProperty.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.GenericSupport_setPropertyFieldSupportOfProperty.restype = None

	if hasattr(dll, "GenericSupport_setStringFieldSupportOfProperty"):
		dll.GenericSupport_setStringFieldSupportOfProperty.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.GenericSupport_setStringFieldSupportOfProperty.restype = None

	if hasattr(dll, "GenericSupport_new_on_client"):
		dll.GenericSupport_new_on_client.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.GenericSupport_new_on_client.restype = ctypes.c_void_p

	#-------------------------------------------------------------------------------
	# GenericDataContainer
	#-------------------------------------------------------------------------------
	if hasattr(dll, "GenericDataContainer_new"):
		dll.GenericDataContainer_new.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.GenericDataContainer_new.restype = ctypes.c_void_p

	if hasattr(dll, "GenericDataContainer_getPropertyAny"):
		dll.GenericDataContainer_getPropertyAny.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.GenericDataContainer_getPropertyAny.restype = ctypes.c_void_p

	if hasattr(dll, "GenericDataContainer_setPropertyAny"):
		dll.GenericDataContainer_setPropertyAny.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.GenericDataContainer_setPropertyAny.restype = None

	if hasattr(dll, "GenericDataContainer_setPropertyDpfType"):
		dll.GenericDataContainer_setPropertyDpfType.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.GenericDataContainer_setPropertyDpfType.restype = None

	if hasattr(dll, "GenericDataContainer_getPropertyTypes"):
		dll.GenericDataContainer_getPropertyTypes.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.GenericDataContainer_getPropertyTypes.restype = ctypes.c_void_p

	if hasattr(dll, "GenericDataContainer_getPropertyNames"):
		dll.GenericDataContainer_getPropertyNames.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.GenericDataContainer_getPropertyNames.restype = ctypes.c_void_p

	if hasattr(dll, "GenericDataContainer_new_on_client"):
		dll.GenericDataContainer_new_on_client.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.GenericDataContainer_new_on_client.restype = ctypes.c_void_p

	if hasattr(dll, "GenericDataContainer_getCopy"):
		dll.GenericDataContainer_getCopy.argtypes = (ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.GenericDataContainer_getCopy.restype = ctypes.c_void_p

	#-------------------------------------------------------------------------------
	# SupportQuery
	#-------------------------------------------------------------------------------
	if hasattr(dll, "SupportQuery_AllEntities"):
		dll.SupportQuery_AllEntities.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.SupportQuery_AllEntities.restype = ctypes.c_void_p

	if hasattr(dll, "SupportQuery_ScopingByProperty"):
		dll.SupportQuery_ScopingByProperty.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.SupportQuery_ScopingByProperty.restype = ctypes.c_void_p

	if hasattr(dll, "SupportQuery_RescopingByProperty"):
		dll.SupportQuery_RescopingByProperty.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.SupportQuery_RescopingByProperty.restype = ctypes.c_void_p

	if hasattr(dll, "SupportQuery_ScopingByNamedSelection"):
		dll.SupportQuery_ScopingByNamedSelection.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_wchar_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.SupportQuery_ScopingByNamedSelection.restype = ctypes.c_void_p

	if hasattr(dll, "SupportQuery_TransposeScoping"):
		dll.SupportQuery_TransposeScoping.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.SupportQuery_TransposeScoping.restype = ctypes.c_void_p

	if hasattr(dll, "SupportQuery_TopologyByScoping"):
		dll.SupportQuery_TopologyByScoping.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.SupportQuery_TopologyByScoping.restype = ctypes.c_void_p

	if hasattr(dll, "SupportQuery_DataByScoping"):
		dll.SupportQuery_DataByScoping.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.SupportQuery_DataByScoping.restype = ctypes.c_void_p

	if hasattr(dll, "SupportQuery_StringField"):
		dll.SupportQuery_StringField.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.SupportQuery_StringField.restype = ctypes.c_void_p

	#-------------------------------------------------------------------------------
	# TimeFreqSupport
	#-------------------------------------------------------------------------------
	if hasattr(dll, "TimeFreqSupport_new"):
		dll.TimeFreqSupport_new.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.TimeFreqSupport_new.restype = ctypes.c_void_p

	if hasattr(dll, "TimeFreqSupport_delete"):
		dll.TimeFreqSupport_delete.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.TimeFreqSupport_delete.restype = None

	if hasattr(dll, "TimeFreqSupport_GetNumberSets"):
		dll.TimeFreqSupport_GetNumberSets.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.TimeFreqSupport_GetNumberSets.restype = ctypes.c_int32

	if hasattr(dll, "TimeFreqSupport_GetNumberSingularSets"):
		dll.TimeFreqSupport_GetNumberSingularSets.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.TimeFreqSupport_GetNumberSingularSets.restype = ctypes.c_int32

	if hasattr(dll, "TimeFreqSupport_SetSharedTimeFreqs"):
		dll.TimeFreqSupport_SetSharedTimeFreqs.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.TimeFreqSupport_SetSharedTimeFreqs.restype = None

	if hasattr(dll, "TimeFreqSupport_SetSharedImaginaryFreqs"):
		dll.TimeFreqSupport_SetSharedImaginaryFreqs.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.TimeFreqSupport_SetSharedImaginaryFreqs.restype = None

	if hasattr(dll, "TimeFreqSupport_SetSharedRpms"):
		dll.TimeFreqSupport_SetSharedRpms.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.TimeFreqSupport_SetSharedRpms.restype = None

	if hasattr(dll, "TimeFreqSupport_SetHarmonicIndices"):
		dll.TimeFreqSupport_SetHarmonicIndices.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.TimeFreqSupport_SetHarmonicIndices.restype = None

	if hasattr(dll, "TimeFreqSupport_GetSharedTimeFreqs"):
		dll.TimeFreqSupport_GetSharedTimeFreqs.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.TimeFreqSupport_GetSharedTimeFreqs.restype = ctypes.c_void_p

	if hasattr(dll, "TimeFreqSupport_GetSharedImaginaryFreqs"):
		dll.TimeFreqSupport_GetSharedImaginaryFreqs.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.TimeFreqSupport_GetSharedImaginaryFreqs.restype = ctypes.c_void_p

	if hasattr(dll, "TimeFreqSupport_GetSharedRpms"):
		dll.TimeFreqSupport_GetSharedRpms.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.TimeFreqSupport_GetSharedRpms.restype = ctypes.c_void_p

	if hasattr(dll, "TimeFreqSupport_GetSharedHarmonicIndices"):
		dll.TimeFreqSupport_GetSharedHarmonicIndices.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.TimeFreqSupport_GetSharedHarmonicIndices.restype = ctypes.c_void_p

	if hasattr(dll, "TimeFreqSupport_GetSharedHarmonicIndicesScoping"):
		dll.TimeFreqSupport_GetSharedHarmonicIndicesScoping.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.TimeFreqSupport_GetSharedHarmonicIndicesScoping.restype = ctypes.c_void_p

	if hasattr(dll, "TimeFreqSupport_GetTimeFreqCummulativeIndexByValue"):
		dll.TimeFreqSupport_GetTimeFreqCummulativeIndexByValue.argtypes = (ctypes.c_void_p, ctypes.c_double, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.TimeFreqSupport_GetTimeFreqCummulativeIndexByValue.restype = ctypes.c_int32

	if hasattr(dll, "TimeFreqSupport_GetTimeFreqCummulativeIndexByValueAndLoadStep"):
		dll.TimeFreqSupport_GetTimeFreqCummulativeIndexByValueAndLoadStep.argtypes = (ctypes.c_void_p, ctypes.c_double, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.TimeFreqSupport_GetTimeFreqCummulativeIndexByValueAndLoadStep.restype = ctypes.c_int32

	if hasattr(dll, "TimeFreqSupport_GetTimeFreqCummulativeIndexByStep"):
		dll.TimeFreqSupport_GetTimeFreqCummulativeIndexByStep.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.TimeFreqSupport_GetTimeFreqCummulativeIndexByStep.restype = ctypes.c_int32

	if hasattr(dll, "TimeFreqSupport_GetImaginaryFreqsCummulativeIndex"):
		dll.TimeFreqSupport_GetImaginaryFreqsCummulativeIndex.argtypes = (ctypes.c_void_p, ctypes.c_double, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.TimeFreqSupport_GetImaginaryFreqsCummulativeIndex.restype = ctypes.c_int32

	if hasattr(dll, "TimeFreqSupport_GetTimeFreqByStep"):
		dll.TimeFreqSupport_GetTimeFreqByStep.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.TimeFreqSupport_GetTimeFreqByStep.restype = ctypes.c_double

	if hasattr(dll, "TimeFreqSupport_GetImaginaryFreqByStep"):
		dll.TimeFreqSupport_GetImaginaryFreqByStep.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.TimeFreqSupport_GetImaginaryFreqByStep.restype = ctypes.c_double

	if hasattr(dll, "TimeFreqSupport_GetTimeFreqByCumulIndex"):
		dll.TimeFreqSupport_GetTimeFreqByCumulIndex.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.TimeFreqSupport_GetTimeFreqByCumulIndex.restype = ctypes.c_double

	if hasattr(dll, "TimeFreqSupport_GetImaginaryFreqByCumulIndex"):
		dll.TimeFreqSupport_GetImaginaryFreqByCumulIndex.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.TimeFreqSupport_GetImaginaryFreqByCumulIndex.restype = ctypes.c_double

	if hasattr(dll, "TimeFreqSupport_GetCyclicHarmonicIndex"):
		dll.TimeFreqSupport_GetCyclicHarmonicIndex.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.TimeFreqSupport_GetCyclicHarmonicIndex.restype = ctypes.c_int32

	if hasattr(dll, "TimeFreqSupport_GetStepAndSubStep"):
		dll.TimeFreqSupport_GetStepAndSubStep.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.TimeFreqSupport_GetStepAndSubStep.restype = ctypes.c_int32

	if hasattr(dll, "TimeFreqSupport_new_on_client"):
		dll.TimeFreqSupport_new_on_client.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.TimeFreqSupport_new_on_client.restype = ctypes.c_void_p

	if hasattr(dll, "TimeFreqSupport_getCopy"):
		dll.TimeFreqSupport_getCopy.argtypes = (ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.TimeFreqSupport_getCopy.restype = ctypes.c_void_p

	#-------------------------------------------------------------------------------
	# TmpDir
	#-------------------------------------------------------------------------------
	if hasattr(dll, "TmpDir_getDir"):
		dll.TmpDir_getDir.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.TmpDir_getDir.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "TmpDir_erase"):
		dll.TmpDir_erase.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.TmpDir_erase.restype = None

	if hasattr(dll, "TmpDir_getDir_on_client"):
		dll.TmpDir_getDir_on_client.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.TmpDir_getDir_on_client.restype = ctypes.POINTER(ctypes.c_char)

	#-------------------------------------------------------------------------------
	# Unit
	#-------------------------------------------------------------------------------
	if hasattr(dll, "Unit_GetHomogeneity"):
		dll.Unit_GetHomogeneity.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Unit_GetHomogeneity.restype = ctypes.c_int32

	if hasattr(dll, "Unit_GetConversionFactor"):
		dll.Unit_GetConversionFactor.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Unit_GetConversionFactor.restype = ctypes.c_double

	if hasattr(dll, "Unit_GetConversionShift"):
		dll.Unit_GetConversionShift.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Unit_GetConversionShift.restype = ctypes.c_double

	if hasattr(dll, "Unit_AreHomogeneous"):
		dll.Unit_AreHomogeneous.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Unit_AreHomogeneous.restype = ctypes.c_bool

	if hasattr(dll, "Unit_getSymbol"):
		dll.Unit_getSymbol.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Unit_getSymbol.restype = ctypes.c_int32

	if hasattr(dll, "Unit_multiply_s"):
		dll.Unit_multiply_s.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Unit_multiply_s.restype = ctypes.c_int32

	if hasattr(dll, "Unit_divide_s"):
		dll.Unit_divide_s.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Unit_divide_s.restype = ctypes.c_int32

	if hasattr(dll, "Unit_invert_s"):
		dll.Unit_invert_s.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Unit_invert_s.restype = ctypes.c_int32

	if hasattr(dll, "Unit_simplify_s"):
		dll.Unit_simplify_s.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Unit_simplify_s.restype = ctypes.c_int32

	if hasattr(dll, "Unit_pow_s"):
		dll.Unit_pow_s.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.c_double, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Unit_pow_s.restype = ctypes.c_int32

	if hasattr(dll, "Unit_GetHomogeneity_for_object"):
		dll.Unit_GetHomogeneity_for_object.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Unit_GetHomogeneity_for_object.restype = ctypes.c_int32

	if hasattr(dll, "Unit_GetConversionFactor_for_object"):
		dll.Unit_GetConversionFactor_for_object.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Unit_GetConversionFactor_for_object.restype = ctypes.c_double

	if hasattr(dll, "Unit_GetConversionShift_for_object"):
		dll.Unit_GetConversionShift_for_object.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Unit_GetConversionShift_for_object.restype = ctypes.c_double

	if hasattr(dll, "Unit_AreHomogeneous_for_object"):
		dll.Unit_AreHomogeneous_for_object.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Unit_AreHomogeneous_for_object.restype = ctypes.c_bool

	if hasattr(dll, "Unit_getSymbol_for_object"):
		dll.Unit_getSymbol_for_object.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Unit_getSymbol_for_object.restype = ctypes.c_int32

	if hasattr(dll, "Unit_multiply_s_for_object"):
		dll.Unit_multiply_s_for_object.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Unit_multiply_s_for_object.restype = ctypes.c_int32

	if hasattr(dll, "Unit_divide_s_for_object"):
		dll.Unit_divide_s_for_object.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Unit_divide_s_for_object.restype = ctypes.c_int32

	if hasattr(dll, "Unit_invert_s_for_object"):
		dll.Unit_invert_s_for_object.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Unit_invert_s_for_object.restype = ctypes.c_int32

	if hasattr(dll, "Unit_simplify_s_for_object"):
		dll.Unit_simplify_s_for_object.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Unit_simplify_s_for_object.restype = ctypes.c_int32

	if hasattr(dll, "Unit_pow_s_for_object"):
		dll.Unit_pow_s_for_object.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.c_double, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Unit_pow_s_for_object.restype = ctypes.c_int32

	#-------------------------------------------------------------------------------
	# Workflow
	#-------------------------------------------------------------------------------
	if hasattr(dll, "WorkFlow_new"):
		dll.WorkFlow_new.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_new.restype = ctypes.c_void_p

	if hasattr(dll, "WorkFlow_getCopy"):
		dll.WorkFlow_getCopy.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_getCopy.restype = ctypes.c_void_p

	if hasattr(dll, "WorkFlow_create_from_text"):
		dll.WorkFlow_create_from_text.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_create_from_text.restype = ctypes.c_void_p

	if hasattr(dll, "WorkFlow_getCopy_on_other_client"):
		dll.WorkFlow_getCopy_on_other_client.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_getCopy_on_other_client.restype = ctypes.c_void_p

	if hasattr(dll, "WorkFlow_delete"):
		dll.WorkFlow_delete.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_delete.restype = None

	if hasattr(dll, "WorkFlow_record_instance"):
		dll.WorkFlow_record_instance.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_bool, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_record_instance.restype = ctypes.c_int32

	if hasattr(dll, "WorkFlow_replace_instance_at_id"):
		dll.WorkFlow_replace_instance_at_id.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_char), ctypes.c_bool, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_replace_instance_at_id.restype = ctypes.c_bool

	if hasattr(dll, "WorkFlow_erase_instance"):
		dll.WorkFlow_erase_instance.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_erase_instance.restype = ctypes.c_bool

	if hasattr(dll, "WorkFlow_get_record_id"):
		dll.WorkFlow_get_record_id.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_get_record_id.restype = ctypes.c_int32

	if hasattr(dll, "WorkFlow_get_by_identifier"):
		dll.WorkFlow_get_by_identifier.argtypes = (ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_get_by_identifier.restype = ctypes.c_void_p

	if hasattr(dll, "WorkFlow_get_first_op"):
		dll.WorkFlow_get_first_op.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_get_first_op.restype = ctypes.c_void_p

	if hasattr(dll, "WorkFlow_get_last_op"):
		dll.WorkFlow_get_last_op.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_get_last_op.restype = ctypes.c_void_p

	if hasattr(dll, "WorkFlow_discover_operators"):
		dll.WorkFlow_discover_operators.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_discover_operators.restype = None

	if hasattr(dll, "WorkFlow_chain_with"):
		dll.WorkFlow_chain_with.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_chain_with.restype = None

	if hasattr(dll, "WorkFlow_chain_with_specified_names"):
		dll.WorkFlow_chain_with_specified_names.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_chain_with_specified_names.restype = None

	if hasattr(dll, "Workflow_create_connection_map"):
		dll.Workflow_create_connection_map.argtypes = (ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Workflow_create_connection_map.restype = ctypes.c_void_p

	if hasattr(dll, "Workflow_add_entry_connection_map"):
		dll.Workflow_add_entry_connection_map.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Workflow_add_entry_connection_map.restype = None

	if hasattr(dll, "WorkFlow_connect_with"):
		dll.WorkFlow_connect_with.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_connect_with.restype = None

	if hasattr(dll, "WorkFlow_connect_with_specified_names"):
		dll.WorkFlow_connect_with_specified_names.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_connect_with_specified_names.restype = None

	if hasattr(dll, "WorkFlow_add_operator"):
		dll.WorkFlow_add_operator.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_add_operator.restype = None

	if hasattr(dll, "WorkFlow_number_of_operators"):
		dll.WorkFlow_number_of_operators.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_number_of_operators.restype = ctypes.c_int32

	if hasattr(dll, "WorkFlow_operator_name_by_index"):
		dll.WorkFlow_operator_name_by_index.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_operator_name_by_index.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "WorkFlow_set_name_input_pin"):
		dll.WorkFlow_set_name_input_pin.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_set_name_input_pin.restype = None

	if hasattr(dll, "WorkFlow_set_name_output_pin"):
		dll.WorkFlow_set_name_output_pin.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_set_name_output_pin.restype = None

	if hasattr(dll, "WorkFlow_rename_input_pin"):
		dll.WorkFlow_rename_input_pin.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_rename_input_pin.restype = None

	if hasattr(dll, "WorkFlow_rename_output_pin"):
		dll.WorkFlow_rename_output_pin.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_rename_output_pin.restype = None

	if hasattr(dll, "WorkFlow_erase_input_pin"):
		dll.WorkFlow_erase_input_pin.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_erase_input_pin.restype = None

	if hasattr(dll, "WorkFlow_erase_output_pin"):
		dll.WorkFlow_erase_output_pin.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_erase_output_pin.restype = None

	if hasattr(dll, "WorkFlow_has_input_pin"):
		dll.WorkFlow_has_input_pin.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_has_input_pin.restype = ctypes.c_bool

	if hasattr(dll, "WorkFlow_has_output_pin"):
		dll.WorkFlow_has_output_pin.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_has_output_pin.restype = ctypes.c_bool

	if hasattr(dll, "WorkFlow_number_of_input"):
		dll.WorkFlow_number_of_input.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_number_of_input.restype = ctypes.c_int32

	if hasattr(dll, "WorkFlow_number_of_output"):
		dll.WorkFlow_number_of_output.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_number_of_output.restype = ctypes.c_int32

	if hasattr(dll, "WorkFlow_input_by_index"):
		dll.WorkFlow_input_by_index.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_input_by_index.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "WorkFlow_output_by_index"):
		dll.WorkFlow_output_by_index.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_output_by_index.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "WorkFlow_number_of_symbol"):
		dll.WorkFlow_number_of_symbol.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_number_of_symbol.restype = ctypes.c_int32

	if hasattr(dll, "WorkFlow_symbol_by_index"):
		dll.WorkFlow_symbol_by_index.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_symbol_by_index.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "WorkFlow_generate_all_derivatives_for"):
		dll.WorkFlow_generate_all_derivatives_for.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_generate_all_derivatives_for.restype = None

	if hasattr(dll, "WorkFlow_generate_derivatives_for"):
		dll.WorkFlow_generate_derivatives_for.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_generate_derivatives_for.restype = None

	if hasattr(dll, "WorkFlow_write_swf"):
		dll.WorkFlow_write_swf.argtypes = (ctypes.c_void_p, ctypes.c_wchar_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_write_swf.restype = None

	if hasattr(dll, "WorkFlow_load_swf"):
		dll.WorkFlow_load_swf.argtypes = (ctypes.c_void_p, ctypes.c_wchar_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_load_swf.restype = None

	if hasattr(dll, "WorkFlow_write_swf_utf8"):
		dll.WorkFlow_write_swf_utf8.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_write_swf_utf8.restype = None

	if hasattr(dll, "WorkFlow_load_swf_utf8"):
		dll.WorkFlow_load_swf_utf8.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_load_swf_utf8.restype = None

	if hasattr(dll, "WorkFlow_write_to_text"):
		dll.WorkFlow_write_to_text.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_write_to_text.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "WorkFlow_connect_DpfType"):
		dll.WorkFlow_connect_DpfType.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_connect_DpfType.restype = None

	if hasattr(dll, "WorkFlow_connect_int"):
		dll.WorkFlow_connect_int.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_connect_int.restype = None

	if hasattr(dll, "WorkFlow_connect_bool"):
		dll.WorkFlow_connect_bool.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_bool, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_connect_bool.restype = None

	if hasattr(dll, "WorkFlow_connect_double"):
		dll.WorkFlow_connect_double.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_double, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_connect_double.restype = None

	if hasattr(dll, "WorkFlow_connect_string"):
		dll.WorkFlow_connect_string.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_connect_string.restype = None

	if hasattr(dll, "WorkFlow_connect_string_with_size"):
		dll.WorkFlow_connect_string_with_size.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.c_uint64, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_connect_string_with_size.restype = None

	if hasattr(dll, "WorkFlow_connect_Scoping"):
		dll.WorkFlow_connect_Scoping.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_connect_Scoping.restype = None

	if hasattr(dll, "WorkFlow_connect_DataSources"):
		dll.WorkFlow_connect_DataSources.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_connect_DataSources.restype = None

	if hasattr(dll, "WorkFlow_connect_Streams"):
		dll.WorkFlow_connect_Streams.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_connect_Streams.restype = None

	if hasattr(dll, "WorkFlow_connect_Field"):
		dll.WorkFlow_connect_Field.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_connect_Field.restype = None

	if hasattr(dll, "WorkFlow_connect_Collection"):
		dll.WorkFlow_connect_Collection.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_connect_Collection.restype = None

	if hasattr(dll, "WorkFlow_connect_Collection_as_vector"):
		dll.WorkFlow_connect_Collection_as_vector.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_connect_Collection_as_vector.restype = None

	if hasattr(dll, "WorkFlow_connect_MeshedRegion"):
		dll.WorkFlow_connect_MeshedRegion.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_connect_MeshedRegion.restype = None

	if hasattr(dll, "WorkFlow_connect_PropertyField"):
		dll.WorkFlow_connect_PropertyField.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_connect_PropertyField.restype = None

	if hasattr(dll, "WorkFlow_connect_StringField"):
		dll.WorkFlow_connect_StringField.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_connect_StringField.restype = None

	if hasattr(dll, "WorkFlow_connect_CustomTypeField"):
		dll.WorkFlow_connect_CustomTypeField.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_connect_CustomTypeField.restype = None

	if hasattr(dll, "WorkFlow_connect_Support"):
		dll.WorkFlow_connect_Support.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_connect_Support.restype = None

	if hasattr(dll, "WorkFlow_connect_CyclicSupport"):
		dll.WorkFlow_connect_CyclicSupport.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_connect_CyclicSupport.restype = None

	if hasattr(dll, "WorkFlow_connect_TimeFreqSupport"):
		dll.WorkFlow_connect_TimeFreqSupport.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_connect_TimeFreqSupport.restype = None

	if hasattr(dll, "WorkFlow_connect_Workflow"):
		dll.WorkFlow_connect_Workflow.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_connect_Workflow.restype = None

	if hasattr(dll, "WorkFlow_connect_RemoteWorkflow"):
		dll.WorkFlow_connect_RemoteWorkflow.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_connect_RemoteWorkflow.restype = None

	if hasattr(dll, "WorkFlow_connect_vector_int"):
		dll.WorkFlow_connect_vector_int.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_connect_vector_int.restype = None

	if hasattr(dll, "WorkFlow_connect_vector_double"):
		dll.WorkFlow_connect_vector_double.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_double), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_connect_vector_double.restype = None

	if hasattr(dll, "WorkFlow_connect_operator_output"):
		dll.WorkFlow_connect_operator_output.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_connect_operator_output.restype = None

	if hasattr(dll, "WorkFlow_connect_ExternalData"):
		dll.WorkFlow_connect_ExternalData.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_connect_ExternalData.restype = None

	if hasattr(dll, "WorkFlow_connect_DataTree"):
		dll.WorkFlow_connect_DataTree.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_connect_DataTree.restype = None

	if hasattr(dll, "WorkFlow_connect_Any"):
		dll.WorkFlow_connect_Any.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_connect_Any.restype = None

	if hasattr(dll, "WorkFlow_connect_LabelSpace"):
		dll.WorkFlow_connect_LabelSpace.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_connect_LabelSpace.restype = None

	if hasattr(dll, "WorkFlow_connect_GenericDataContainer"):
		dll.WorkFlow_connect_GenericDataContainer.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_connect_GenericDataContainer.restype = None

	if hasattr(dll, "WorkFlow_getoutput_FieldsContainer"):
		dll.WorkFlow_getoutput_FieldsContainer.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_getoutput_FieldsContainer.restype = ctypes.c_void_p

	if hasattr(dll, "WorkFlow_getoutput_ScopingsContainer"):
		dll.WorkFlow_getoutput_ScopingsContainer.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_getoutput_ScopingsContainer.restype = ctypes.c_void_p

	if hasattr(dll, "WorkFlow_getoutput_Field"):
		dll.WorkFlow_getoutput_Field.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_getoutput_Field.restype = ctypes.c_void_p

	if hasattr(dll, "WorkFlow_getoutput_Scoping"):
		dll.WorkFlow_getoutput_Scoping.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_getoutput_Scoping.restype = ctypes.c_void_p

	if hasattr(dll, "WorkFlow_getoutput_timeFreqSupport"):
		dll.WorkFlow_getoutput_timeFreqSupport.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_getoutput_timeFreqSupport.restype = ctypes.c_void_p

	if hasattr(dll, "WorkFlow_getoutput_meshesContainer"):
		dll.WorkFlow_getoutput_meshesContainer.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_getoutput_meshesContainer.restype = ctypes.c_void_p

	if hasattr(dll, "WorkFlow_getoutput_meshedRegion"):
		dll.WorkFlow_getoutput_meshedRegion.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_getoutput_meshedRegion.restype = ctypes.c_void_p

	if hasattr(dll, "WorkFlow_getoutput_resultInfo"):
		dll.WorkFlow_getoutput_resultInfo.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_getoutput_resultInfo.restype = ctypes.c_void_p

	if hasattr(dll, "WorkFlow_getoutput_propertyField"):
		dll.WorkFlow_getoutput_propertyField.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_getoutput_propertyField.restype = ctypes.c_void_p

	if hasattr(dll, "WorkFlow_getoutput_anySupport"):
		dll.WorkFlow_getoutput_anySupport.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_getoutput_anySupport.restype = ctypes.c_void_p

	if hasattr(dll, "WorkFlow_getoutput_CyclicSupport"):
		dll.WorkFlow_getoutput_CyclicSupport.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_getoutput_CyclicSupport.restype = ctypes.c_void_p

	if hasattr(dll, "WorkFlow_getoutput_DataSources"):
		dll.WorkFlow_getoutput_DataSources.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_getoutput_DataSources.restype = ctypes.c_void_p

	if hasattr(dll, "WorkFlow_getoutput_Streams"):
		dll.WorkFlow_getoutput_Streams.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_getoutput_Streams.restype = ctypes.c_void_p

	if hasattr(dll, "WorkFlow_getoutput_Workflow"):
		dll.WorkFlow_getoutput_Workflow.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_getoutput_Workflow.restype = ctypes.c_void_p

	if hasattr(dll, "WorkFlow_getoutput_ExternalData"):
		dll.WorkFlow_getoutput_ExternalData.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_getoutput_ExternalData.restype = ctypes.c_void_p

	if hasattr(dll, "WorkFlow_getoutput_as_any"):
		dll.WorkFlow_getoutput_as_any.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_getoutput_as_any.restype = ctypes.c_void_p

	if hasattr(dll, "WorkFlow_getoutput_IntCollection"):
		dll.WorkFlow_getoutput_IntCollection.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_getoutput_IntCollection.restype = ctypes.c_void_p

	if hasattr(dll, "WorkFlow_getoutput_DoubleCollection"):
		dll.WorkFlow_getoutput_DoubleCollection.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_getoutput_DoubleCollection.restype = ctypes.c_void_p

	if hasattr(dll, "WorkFlow_getoutput_Operator"):
		dll.WorkFlow_getoutput_Operator.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_getoutput_Operator.restype = ctypes.c_void_p

	if hasattr(dll, "WorkFlow_getoutput_StringField"):
		dll.WorkFlow_getoutput_StringField.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_getoutput_StringField.restype = ctypes.c_void_p

	if hasattr(dll, "WorkFlow_getoutput_CustomTypeField"):
		dll.WorkFlow_getoutput_CustomTypeField.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_getoutput_CustomTypeField.restype = ctypes.c_void_p

	if hasattr(dll, "WorkFlow_getoutput_CustomTypeFieldsContainer"):
		dll.WorkFlow_getoutput_CustomTypeFieldsContainer.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_getoutput_CustomTypeFieldsContainer.restype = ctypes.c_void_p

	if hasattr(dll, "WorkFlow_getoutput_DataTree"):
		dll.WorkFlow_getoutput_DataTree.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_getoutput_DataTree.restype = ctypes.c_void_p

	if hasattr(dll, "WorkFlow_getoutput_GenericDataContainer"):
		dll.WorkFlow_getoutput_GenericDataContainer.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_getoutput_GenericDataContainer.restype = ctypes.c_void_p

	if hasattr(dll, "WorkFlow_getoutput_Unit"):
		dll.WorkFlow_getoutput_Unit.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_getoutput_Unit.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "WorkFlow_getoutput_string"):
		dll.WorkFlow_getoutput_string.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_getoutput_string.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "WorkFlow_getoutput_string_with_size"):
		dll.WorkFlow_getoutput_string_with_size.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_getoutput_string_with_size.restype = ctypes.POINTER(ctypes.c_char)

	if hasattr(dll, "WorkFlow_getoutput_int"):
		dll.WorkFlow_getoutput_int.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_getoutput_int.restype = ctypes.c_int32

	if hasattr(dll, "WorkFlow_getoutput_double"):
		dll.WorkFlow_getoutput_double.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_getoutput_double.restype = ctypes.c_double

	if hasattr(dll, "WorkFlow_getoutput_bool"):
		dll.WorkFlow_getoutput_bool.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_getoutput_bool.restype = ctypes.c_bool

	if hasattr(dll, "WorkFlow_has_output_when_evaluated"):
		dll.WorkFlow_has_output_when_evaluated.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_has_output_when_evaluated.restype = ctypes.c_bool

	if hasattr(dll, "WorkFlow_add_tag"):
		dll.WorkFlow_add_tag.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_add_tag.restype = None

	if hasattr(dll, "WorkFlow_has_tag"):
		dll.WorkFlow_has_tag.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_has_tag.restype = ctypes.c_bool

	if hasattr(dll, "WorkFlow_export_graphviz"):
		dll.WorkFlow_export_graphviz.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_export_graphviz.restype = ctypes.c_bool

	if hasattr(dll, "WorkFlow_export_json"):
		dll.WorkFlow_export_json.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.POINTER(ctypes.c_char)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_export_json.restype = None

	if hasattr(dll, "WorkFlow_import_json"):
		dll.WorkFlow_import_json.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_import_json.restype = None

	if hasattr(dll, "WorkFlow_make_from_template"):
		dll.WorkFlow_make_from_template.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_make_from_template.restype = ctypes.c_void_p

	if hasattr(dll, "WorkFlow_template_exists"):
		dll.WorkFlow_template_exists.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_template_exists.restype = ctypes.c_bool

	if hasattr(dll, "Workflow_get_operators_collection_for_input"):
		dll.Workflow_get_operators_collection_for_input.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.POINTER(ctypes.c_int32)), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Workflow_get_operators_collection_for_input.restype = ctypes.c_void_p

	if hasattr(dll, "Workflow_get_operator_for_output"):
		dll.Workflow_get_operator_for_output.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Workflow_get_operator_for_output.restype = ctypes.c_void_p

	if hasattr(dll, "Workflow_get_client_id"):
		dll.Workflow_get_client_id.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Workflow_get_client_id.restype = ctypes.c_int32

	if hasattr(dll, "WorkFlow_new_on_client"):
		dll.WorkFlow_new_on_client.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_new_on_client.restype = ctypes.c_void_p

	if hasattr(dll, "WorkFlow_create_from_text_on_client"):
		dll.WorkFlow_create_from_text_on_client.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_create_from_text_on_client.restype = ctypes.c_void_p

	if hasattr(dll, "WorkFlow_getCopy_on_client"):
		dll.WorkFlow_getCopy_on_client.argtypes = (ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_getCopy_on_client.restype = ctypes.c_void_p

	if hasattr(dll, "WorkFlow_get_by_identifier_on_client"):
		dll.WorkFlow_get_by_identifier_on_client.argtypes = (ctypes.c_int32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.WorkFlow_get_by_identifier_on_client.restype = ctypes.c_void_p

	if hasattr(dll, "Workflow_create_connection_map_for_object"):
		dll.Workflow_create_connection_map_for_object.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_wchar_p), )
		dll.Workflow_create_connection_map_for_object.restype = ctypes.c_void_p


