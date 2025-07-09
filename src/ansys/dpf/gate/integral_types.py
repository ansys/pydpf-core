import ctypes
import numpy as np

class MutableInt32:
    def __init__(self, val=0):
        self.set(val)

    def ctypes_pointer(self):
        return ctypes.pointer(self.val)

    def set(self, val):
        self.val = ctypes.c_int32(val)

    def __int__(self):
        return self.val.value

class MutableUInt64:
    def __init__(self, val=0):
        self.set(val)

    def ctypes_pointer(self):
        return ctypes.pointer(self.val)

    def set(self, val):
        self.val = ctypes.c_uint64(val)

    def __int__(self):
        return self.val.value


class MutableListInt32:
    def __init__(self, size=0):
        self.val = ctypes.pointer(ctypes.c_int32(0))
        self._size = MutableInt32(size)
        if size != 0:
            tmp = list(range(size))
            self.val = (ctypes.c_int32 * len(tmp))(*tmp)

    def ctypes_pointer(self):
        return ctypes.pointer(self.val)

    @property
    def pointer(self):
        return self.val

    @property
    def np_type(self):
        return np.dtype(self.pointer._type_)

    @property
    def internal_size(self):
        return self._size

    def tolist(self):
        if isinstance(self.val, list):
            return self.val
        return [int(self.val[i]) for i in range(0, int(self._size))]

    def set(self, val: list):
        self.val = val
        self._size = len(val)


class MutableDouble:
    def __init__(self, val=0.):
        self.set(val)

    def ctypes_pointer(self):
        return ctypes.pointer(self.val)

    def set(self, val):
        self.val = ctypes.c_double(val)

    def __float__(self):
        return self.val.value


class MutableListDouble:
    def __init__(self):
        self.val = ctypes.pointer(ctypes.c_double(0))
        self._size = MutableInt32(0)

    def ctypes_pointer(self):
        return ctypes.pointer(self.val)

    @property
    def pointer(self):
        return self.val

    @property
    def np_type(self):
        return np.dtype(self.pointer._type_)

    @property
    def internal_size(self):
        return self._size

    def tolist(self):
        if isinstance(self.val, list):
            return self.val
        return [float(self.val[i]) for i in range(0, int(self._size))]

    def set(self, val: list):
        self.val = val
        self._size = len(val)


class MutableListChar:
    def __init__(self):
        self.val = ctypes.pointer(ctypes.c_char(0))
        self._size = MutableInt32(0)

    def ctypes_pointer(self):
        return ctypes.pointer(self.val)

    @property
    def pointer(self):
        return self.val

    @property
    def np_type(self):
        return np.dtype(self.pointer._type_)

    @property
    def internal_size(self):
        return self._size


class MutableString:
    def __init__(self, size):
        self.val = ctypes.create_string_buffer(size)

    def set_str(self, value_str):
        self.val = value_str

    def set(self, value_str):
        self.val = value_str

    def cchar_p_p(self):
        self.val = ctypes.c_char_p()
        self.val_p = ctypes.byref(self.val)
        return  ctypes.cast(self.val_p, ctypes.POINTER(ctypes.POINTER(ctypes.c_char)))

    def __str__(self):
        if hasattr(self.val, "value"):
            return self.val.value.decode("utf8")
        return str(self.val)


class MutableListString:
    def __init__(self, list=None):
        if list is not None:
            if hasattr(list, "__iter__"):
                self.val = (ctypes.c_char_p * len(list))()
                self.val[:] = [bytes(s, "utf8") for s in list]
                self._size = MutableInt32(len(list))
            else:
                self.val = (ctypes.c_char_p * list)()
                self._size = MutableInt32(list)
        else:
            self.val = ctypes.POINTER(ctypes.c_char_p)()
            self.val_p = ctypes.byref(self.val)
            self._size = MutableInt32(0)

    def tolist(self):
        if isinstance(self.val, list):
            return self.val
        return [val.decode("utf8") for val in self.val]

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self):
            self.n += 1
            return self.__getitem__(self.n-1)
        else:
            raise StopIteration

    def __getitem__(self, i):
        return self.val[i]

    def __len__(self):
        return int(self.internal_size.val.value)

    @property
    def np_type(self):
        return None

    @property
    def pointer(self):
        return self.cchar_p_p

    def cchar_p_p_p(self):
        return ctypes.cast(ctypes.byref(self.val), ctypes.POINTER(ctypes.POINTER(ctypes.POINTER(ctypes.c_char))))

    def cchar_p_p(self):
        return ctypes.cast(self.val, ctypes.POINTER(ctypes.POINTER(ctypes.c_char)))

    @property
    def internal_size(self):
        return self._size