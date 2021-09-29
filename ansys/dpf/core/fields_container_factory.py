"""
fields_container_factory
========================

Contains functions to simplify creating a fields container.
"""

from ansys.dpf.core import FieldsContainer, TimeFreqSupport
from ansys.dpf.core import errors as dpf_errors
from ansys.dpf.core import fields_factory
from ansys.dpf.core.common import locations


def over_time_freq_fields_container(fields, time_freq_unit=None, server=None):
    """Create a fields container with one field by time set.

    This method can also set the time frequency support with the correct unit
    if needed.

    Parameters
    ----------
    fields : Dictionary(time_int_key : Field) or list of Field
        Dictionary of field entities to add to the fields container.
    time_freq_unit : str, optional
        Unit of the time frequency support, which is taken into
        account if the fields attribute has a dictionary type. The
        default is ``None``.
    server : ansys.dpf.core.server, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Returns
    -------
    fields_container : FieldsContainer
        Fields container containing one field by time step.

    Examples
    --------
    Create a fields container from scratch based on time labels.

    >>> from ansys.dpf import core as dpf
    >>> field1 = dpf.Field()
    >>> field2 = dpf.Field()
    >>> from ansys.dpf.core import fields_container_factory
    >>> my_fc = fields_container_factory.over_time_freq_fields_container([ field1, field2 ])

    """
    if not isinstance(fields, dict) and not isinstance(fields, list):
        raise dpf_errors.InvalidTypeError("dictionary/list", "fields")
    fc = FieldsContainer(server=server)
    fc.labels = {"time"}
    i = 0
    # dict case
    if isinstance(fields, dict):
        time_freq = []
        for field_key in fields:
            fc.add_field({"time": i + 1}, fields[field_key])
            time_freq.append(field_key)
            i += 1
        time_freq_field = fields_factory.create_scalar_field(
            len(fields), location=locations.time_freq, server=server
        )
        time_freq_field.append(time_freq, 1)
        time_freq_field.unit = time_freq_unit
        time_freq_support = TimeFreqSupport(server=server)
        time_freq_support.time_frequencies = time_freq_field
        fc.time_freq_support = time_freq_support
    # list case
    elif isinstance(fields, list):
        for field in fields:
            fc.add_field({"time": i + 1}, field)
            i += 1
    return fc


def over_time_freq_complex_fields_container(
    real_fields, imaginary_fields, time_freq_unit=None, server=None
):
    """Create a fields container with two fields (real and imaginary) by time set.

    If the inputs for the fields are dictionaries, this method sets the time frequency
    support with the correct unit if needed.

    Parameters
    ----------
    real_fields : Dictionary(time_int_key : Field) or list of Field
        Dictionary or list of field entities to add to the fields container.
    imaginary_fields : Dictionary(time_int_key : Field) or list of Field
        Dictionary or list of field entities to add to the fields container.
    time_freq_unit : str , optional
        Unit of the time frequency support, which is taken into account if
        the field's attribute has a dictionary type.
    server : ansys.dpf.core.server, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Returns
    -------
    fields_container : FieldsContainer
        Fields container containing two fields (real and imaginary) by time step.
    """
    if not isinstance(real_fields, dict) and not isinstance(real_fields, list):
        raise dpf_errors.InvalidTypeError("dictionary/list", "real_fields")
    if not isinstance(imaginary_fields, dict) and not isinstance(
        imaginary_fields, list
    ):
        raise dpf_errors.InvalidTypeError("dictionary/list", "imaginary_fields")

    errorString = (
        "Both real_fields and imaginary_fields must have the same type (list or dict)"
    )
    if isinstance(real_fields, dict):
        if not isinstance(imaginary_fields, dict):
            raise dpf_errors.DpfValueError(errorString)
    elif isinstance(real_fields, list):
        if not isinstance(imaginary_fields, list):
            raise dpf_errors.DpfValueError(errorString)

    fc = FieldsContainer(server=server)
    fc.labels = ["time", "complex"]
    i = 0
    # dict case
    if isinstance(real_fields, dict):
        time_freq = []
        for field_key in real_fields:
            fc.add_field({"time": i + 1, "complex": 0}, real_fields[field_key])
            time_freq.append(field_key)
            i += 1
        i = 0
        im_time_freq = []
        for field_key in imaginary_fields:
            fc.add_field({"time": i + 1, "complex": 1}, imaginary_fields[field_key])
            im_time_freq.append(field_key)
            i += 1
        time_freq_field = fields_factory.create_scalar_field(
            len(real_fields), locations.time_freq, server=server
        )
        time_freq_field.append(time_freq, 1)
        time_freq_field.unit = time_freq_unit
        im_time_freq_field = fields_factory.create_scalar_field(
            len(imaginary_fields), locations.time_freq, server=server
        )
        im_time_freq_field.append(im_time_freq, 1)
        im_time_freq_field.unit = time_freq_unit
        time_freq_support = TimeFreqSupport(server=server)
        time_freq_support.time_frequencies = time_freq_field
        time_freq_support.complex_frequencies = im_time_freq_field
        fc.time_freq_support = time_freq_support
    # list case
    if isinstance(real_fields, list):
        for field in real_fields:
            fc.add_field({"time": i + 1, "complex": 0}, field)
            i += 1
        i = 0
        for field in imaginary_fields:
            fc.add_field({"time": i + 1, "complex": 1}, field)
            i += 1
    return fc


def complex_fields_container(real_field, imaginary_field, server=None):
    """Create a fields container with two fields (real and imaginary) and only one time set.

    Parameters
    ----------
    real_fields : Field
        Real :class:`ansys.dpf.core.Field` entity to add to the fields container.
    imaginary_fields : Field
        Imaginary :class:`ansys.dpf.core.Field` entity to add to the fields container.
    server : ansys.dpf.core.server, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Returns
    -------
    fields_container : FieldsContainer
        Fields container with two fields (real and imaginary).
    """
    fc = FieldsContainer(server=server)
    fc.labels = ["complex"]
    fc.add_field({"complex": 0}, real_field)
    fc.add_field({"complex": 1}, imaginary_field)
    return fc
