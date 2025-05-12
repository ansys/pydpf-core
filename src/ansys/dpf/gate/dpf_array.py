import numpy as np


class DPFArray(np.ndarray):
    """Overload of numpy ndarray <https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html>`_
    managing DPFVector (memory owner of vector data in DPF C APIs) memory and updates.

    Parameters
    ----------
    vec : DPFVectorBase
        DPFVector instance to manage and optionally update when the DPFArray is deleted or committed.
    """

    def __new__(
            cls,
            vec
    ):
        """Allocate the array."""
        try:
            obj = vec.np_array.view(cls)
        except NotImplementedError as e:
            raise TypeError(e.args)
        obj.vec = vec
        return obj

    def __array_finalize__(self, obj):
        """Finalize array (associate with parent metadata)."""
        if np.shares_memory(self, obj):
            self.vec = getattr(obj, 'vec', None)
        else:
            self.vec = None

    def commit(self):
        """Updates the data server side when necessary"""
        if self.vec is not None:
            self.vec.commit()

    # def __setitem__(self, key, value):
    #     super().__setitem__(key, value)
    #     if self.vec:
    #         self.vec._modified = True
