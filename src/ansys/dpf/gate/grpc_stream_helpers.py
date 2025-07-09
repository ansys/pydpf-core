import sys
import array
import numpy as np
from ansys.dpf.gate.dpf_vector import get_size_of_list


def _to_bytes(array):
    if isinstance(array, (np.generic, np.ndarray)):
        return array.tobytes()
    return array


def _set_array_to_request(request, bytes):
    request.array = bytes


def _array_unit(data):
    if isinstance(array, (np.generic, np.ndarray)):
        return data.dtype.name
    return "byte"


def _data_chunk_yielder(request, data, chunk_size=None, set_array=_set_array_to_request):
    from ansys.dpf.gate import misc
    if not chunk_size:
        chunk_size = misc.client_config()["streaming_buffer_size"]

    length = get_size_of_list(data)
    need_progress_bar = length > 1e6 and misc.COMMON_PROGRESS_BAR
    if need_progress_bar:
        bar = misc.COMMON_PROGRESS_BAR(
            "Sending data...", unit=_array_unit(data), tot_size=length
        )
        bar.start()
    sent_length = 0
    if length == 0:
        yield request
        return
    unitary_size = int(chunk_size // sys.getsizeof(data[0]))
    if length - sent_length < unitary_size:
        unitary_size = length - sent_length
    while sent_length < length:
        currentcopy = data[sent_length: sent_length + unitary_size]
        set_array(request, _to_bytes(currentcopy))
        sent_length = sent_length + unitary_size
        if length - sent_length < unitary_size:
            unitary_size = length - sent_length
        yield request
        try:
            if need_progress_bar:
                bar.update(sent_length)
        except:
            pass
    try:
        if need_progress_bar:
            bar.finish()
    except:
        pass


def dtype_to_array_type(dtype):
    if dtype == np.float64:
        return "d"
    elif dtype == np.byte:
        return "b"
    else:
        return "i"


def _data_get_chunk_(dtype, service, np_array=True, get_array=lambda chunk: chunk.array):
    from ansys.dpf.gate import misc
    tupleMetaData = service.initial_metadata()

    need_progress_bar = False
    size = 0
    for iMeta in range(len(tupleMetaData)):
        if tupleMetaData[iMeta].key == "size_tot":
            size = int(tupleMetaData[iMeta].value)

    itemsize = np.dtype(dtype).itemsize
    need_progress_bar = size // itemsize > 1e6 and misc.COMMON_PROGRESS_BAR
    if need_progress_bar:
        bar = misc.COMMON_PROGRESS_BAR(
            "Receiving data...", unit=np.dtype(dtype).name + "s", tot_size=size // itemsize
        )
        bar.start()

    if np_array:
        arr = np.empty(size // itemsize, dtype)
        i = 0
        for chunk in service:
            curr_size = len(get_array(chunk)) // itemsize
            arr[i: i + curr_size] = np.frombuffer(get_array(chunk), dtype)
            i += curr_size
            try:
                if need_progress_bar:
                    bar.update(i)
            except:
                pass

    else:
        arr = []
        atype = dtype_to_array_type(dtype)
        for chunk in service:
            arr.extend(array.array(atype, get_array(chunk)))
            try:
                if need_progress_bar:
                    bar.update(len(arr))
            except:
                pass
    try:
        if need_progress_bar:
            bar.finish()
    except:
        pass
    return arr


def _string_data_chunk_yielder(request, data, chunk_size=None):
    from ansys.dpf.gate import misc

    if not chunk_size:
        chunk_size = misc.client_config()["streaming_buffer_size"]

    length = len(data)
    sent_length = 0
    separator = b'\0'
    while sent_length < length:
        num_bytes = 0
        currentcopy = bytearray()
        while num_bytes <= chunk_size and sent_length < length:
            currentcopy.extend(data[sent_length])
            currentcopy.extend(separator)
            sent_length += 1
            num_bytes = len(currentcopy)

        request.array = bytes(currentcopy)
        yield request
    if length == 0:
        yield request


def _string_data_get_chunk_(service):
    from ansys.dpf.gate import misc
    tupleMetaData = service.initial_metadata()
    size = 0
    for iMeta in range(len(tupleMetaData)):
        if tupleMetaData[iMeta].key == "size_tot":
            size = int(tupleMetaData[iMeta].value)
    arr = []
    for chunk in service:
        arr.extend(chunk.array.decode("utf8").rstrip(u'\x00').split(u'\x00'))
    return arr
