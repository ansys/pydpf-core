"""
.. _ref_property_fields_container:

PropertyFieldsContainer
===============
Contains classes associated with the PropertyFieldsContainer.
"""
from __future__ import annotations

from collections.abc import Sequence
import copy
from typing import Dict

import ansys.dpf.core as dpf
from ansys.dpf.core.property_field import PropertyField
import numpy as np


class _LabelSpaceKV:
    """Class for internal use to associate a label space with a field."""

    def __init__(self, _dict: Dict[str, int], _field):
        """Constructs an association between a dictionary and a field."""
        self._dict = _dict
        self._field = _field

    @property
    def dict(self):
        """Returns the associated dictionary."""
        return self._dict

    @property
    def field(self):
        """Returns the associated field."""
        return self._field

    @field.setter
    def field(self, value):
        self._field = value

    def __str__(self):
        """Returns a string representation of the association."""
        field_str = str(self._field).replace("\n", " ")
        return f"Label Space: {self._dict} with field {field_str}"


class PropertyFieldsContainer(Sequence):
    """Minimal implementation of a FieldsContainer specialized for PropertyFieldsContainer."""

    def __init__(self, fields_container=None, server=None):
        """Constructs an empty PropertyFieldsContainer or from a PropertyFieldsContainer."""
        # default constructor
        self._labels = []  # used by Dataframe
        self.scopings = []
        self._server = None  # used by Dataframe

        self.label_spaces = []
        self.ids = []

        # PropertyFieldsContainer copy
        if fields_container is not None:
            self._labels = copy.deepcopy(fields_container.labels)
            # self.scopings = copy.deepcopy(fields_container.scopings)
            self._server = fields_container._server

            # self.ids = copy.deepcopy(fields_container.ids)

            for ls in fields_container.label_spaces:
                self.add_entry(copy.deepcopy(ls.dict), ls.field.as_local_field())

        # server copy
        if server is not None:
            self._server = server

    # Collection
    def __str__(self):
        """Returns a string representation of a PropertyFieldsContainer."""
        txt = f"DPF PropertyFieldsContainer with {len(self)} fields\n"
        for idx, ls in enumerate(self.label_spaces):
            txt += f"\t {idx}: {ls}\n"

        return txt

    @property
    def labels(self):
        """Returns all labels of the PropertyFieldsContainer."""
        return self._labels

    @labels.setter
    def labels(self, vals):
        self.set_labels(vals)

    def set_labels(self, labels):
        """Sets all the label of the PropertyFieldsContainer."""
        if len(self._labels) != 0:
            raise ValueError("labels already set")

        for l in labels:
            self.add_label(l)

    def add_label(self, label):
        """Adds a label."""
        if label not in self._labels:
            self._labels.append(label)
            self.scopings.append([])

    def has_label(self, label):
        """Check if a PorpertyFieldsContainer contains a given label."""
        return label in self.labels

    # used by Dataframe
    def get_label_space(self, idx):
        """Get a Label Space at a given index."""
        return self.label_spaces[idx]._dict

    # used by Dataframe
    def get_label_scoping(self, label="time"):
        """Returns a scoping on the fields concerned by the given label."""
        if label in self.labels:
            scoping_ids = self.scopings[self.labels.index(label)]
            return dpf.Scoping(ids=scoping_ids, location="")
        raise KeyError("label {label} not found")

    def add_entry(self, label_space: Dict[str, int], value):
        """Adds a PropertyField associated with a dictionary."""
        new_id = self._new_id()

        if hasattr(value, "_server"):
            self._server = value._server

        # add Label Space
        self.label_spaces.append(_LabelSpaceKV(label_space, value))

        # Update IDs
        self.ids.append(new_id)

        # Update Scopings
        for label in label_space.keys():
            label_idx = self.labels.index(label)
            self.scopings[label_idx].append(new_id)

    def get_entries(self, label_space_or_index):
        """Returns a list of fields from a complete or partial specification of a dictionary."""
        if isinstance(label_space_or_index, int):
            idx: int = label_space_or_index
            return [self.label_spaces[idx].field]
        else:
            _dict: Dict[str, int] = label_space_or_index
            are_keys_in_labels = [key in self.labels for key in _dict.keys()]
            if all(are_keys_in_labels):
                remaining = set(range(len(self.label_spaces)))
                for key in _dict.keys():
                    val = _dict[key]
                    to_remove = set()
                    for idx in remaining:
                        ls = self.label_spaces[idx]
                        if ls.dict[key] != val:
                            to_remove.add(idx)
                    remaining = remaining.difference(to_remove)

                idx_to_field = lambda idx: self.label_spaces[idx].field
                return list(map(idx_to_field, remaining))
            else:
                bad_idx = are_keys_in_labels.index(False)
                bad_key = _dict.keys()[bad_idx]
                raise KeyError(f"Key {bad_key} is not in labels: {self.labels}")

    def get_entry(self, label_space_or_index):
        """Returns the field or (first field found) corresponding to the given dictionary."""
        ret = self.get_entries(label_space_or_index)

        if len(ret) != 0:
            return ret[0]

        raise IndexError("Could not find corresponding entry")

    def _new_id(self):
        """Helper method generating a new id when calling add_entry(...)."""
        if len(self.ids) == 0:
            self.last_id = 1
            return self.last_id
        else:
            self.last_id += 1
            return self.last_id

    # FieldsContainer
    def create_subtype(self, obj_by_copy):
        """Instantiate a PropertyField with given instance, using the server of the container."""
        return PropertyField(property_field=obj_by_copy, server=self._server)

    def get_fields_by_time_complex_ids(self, timeid=None, complexid=None):
        """Returns fields at a requested time or complex ID."""
        label_space = {"time": timeid, "complex": complexid}
        return self.get_fields(label_space)

    def get_field_by_time_complex_ids(self, timeid=None, complexid=None):
        """Returns field at a requested time or complex ID."""
        label_space = {"time": timeid, "complex": complexid}
        return self.get_field(label_space)

    def __time_complex_label_space__(self, timeid=None, complexid=None):
        """Not implemented."""
        raise NotImplementedError

    # used by Dataframe
    def get_fields(self, label_space):
        """Returns the list of fields associated with given label space."""
        return self.get_entries(label_space)

    def get_field(self, label_space_or_index):
        """Retrieves the field at a requested index or label space."""
        return self.get_entry(label_space_or_index)

    def get_field_by_time_id(self, timeid=None):
        """Retrieves the complex field at a requested timeid."""
        label_space = {"time": timeid}
        if self.has_label("complex"):
            label_space["complex"] = 0
            return self.get_field(label_space)

    def get_imaginary_fields(self, timeid=None):
        """Retrieve the complex fields at a requested timeid."""
        label_space = {"time": timeid, "complex": 1}
        return self.get_fields(label_space)

    def get_imaginary_field(self, timeid=None):
        """Retrieve the complex field at a requested time."""
        label_space = {"time": timeid, "complex": 1}
        return self.get_field(label_space)

    # used by Dataframe
    def __getitem__(self, key):
        """Retrieve the field at a requested index."""
        return self.get_field(key)

    def __len__(self):
        """Retrieve the number of label spaces."""
        return len(self.label_spaces)

    def add_field(self, label_space, field):
        """Add or update a field at a requested label space."""
        self.add_entry(label_space, field)

    def add_field_by_time_id(self, field, timeid=1):
        """Add or update a field at a requested timeid."""
        if not self.has_label("time"):
            self.add_label("time")

        label_space = {"time": timeid}

        if self.has_label("complex"):
            label_space["complex"] = 0

        self.add_field(label_space, field)

    def add_imaginary_field(self, field, timeid=1):
        """Add or update an imaginary field at a requested timeid."""
        if not self.has_label("time"):
            self.add_label("time")
        if not self.has_label("complex"):
            self.add_label("complex")

        label_space = {"time": timeid, "complex": 1}
        self.add_field(label_space, field)

    def select_component(self, index):
        """Not implemented."""
        raise NotImplementedError

    @property
    def time_freq_support(self):
        """Not implemented."""
        raise NotImplementedError

    @time_freq_support.setter
    def time_freq_support(self, value):
        """Not implemented."""
        raise NotImplementedError

    def deep_copy(self, server=None):
        """Not implemented."""
        raise NotImplementedError

    def get_time_scoping(self):
        """Retrieves the time scoping containing the time sets."""
        return self.get_label_scoping("time")

    def animate(self, save_as=None, deform_by=None, scale_factor=1.0, **kwargs):
        """Not implemented."""
        raise NotImplementedError

    def _set_field(self, ls_idx, field):
        self.label_spaces[ls_idx].field = field

    def rescope(self, scoping: dpf.Scoping):
        """Helper function to reproduce functionality of rescope_fc Operator."""
        copy_fc = PropertyFieldsContainer(self, server=None)
        for idx, label_space in enumerate(copy_fc.label_spaces):
            pfield = PropertyField(location=label_space.field.location)
            pfield.data = np.ravel(
                [label_space._field.get_entity_data_by_id(id) for id in scoping.ids]
            )
            pfield.scoping.ids = scoping.ids
            copy_fc._set_field(idx, pfield)
        return copy_fc
