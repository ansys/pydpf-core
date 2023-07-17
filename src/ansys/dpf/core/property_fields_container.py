"""
.. _ref_property_fields_container:

_MockPropertyFieldsContainer
============================
Contains classes associated with the _MockPropertyFieldsContainer.
"""
from __future__ import annotations

from collections.abc import Sequence
import copy
from typing import Dict, List, Union

import ansys.dpf.core as dpf
from ansys.dpf.core.server_types import BaseServer


class _LabelSpaceKV:
    """Class for internal use to associate a label space with a field."""

    def __init__(self, _dict: Dict[str, int], _field: dpf.Field):
        """Constructs an association between a dictionary and a field."""
        self._dict = _dict
        self._field = _field

    @property
    def dict(self) -> dict:
        """Returns the associated dictionary."""
        return self._dict

    @property
    def field(self) -> dpf.Field:
        """Returns the associated field."""
        return self._field

    @field.setter
    def field(self, value: dpf.Field):
        self._field = value

    def __str__(self):
        """Returns a string representation of the association."""
        field_str = str(self._field).replace("\n", "\n\t\t\t")
        return f"Label Space: {self._dict} with field\n\t\t\t{field_str}"


class _MockPropertyFieldsContainer(Sequence):
    """Minimal implementation of a FieldsContainer specialized for _MockPropertyFieldsContainer."""

    def __init__(
        self,
        fields_container: _MockPropertyFieldsContainer = None,
        server: BaseServer = None,
    ):
        """Constructs a _MockPropertyFieldsContainer."""
        # default constructor
        self._labels = []  # used by Dataframe
        self.scopings = []
        self._server = None  # used by Dataframe

        self.label_spaces = []
        self.ids = []

        # _MockPropertyFieldsContainer copy
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
    def __str__(self) -> str:
        """Returns a string representation of a _MockPropertyFieldsContainer."""
        txt = f"DPF PropertyFieldsContainer with {len(self)} fields\n"
        for idx, ls in enumerate(self.label_spaces):
            txt += f"\t {idx}: {ls}\n"

        return txt

    @property
    def labels(self) -> List[str]:
        """Returns all labels of the _MockPropertyFieldsContainer."""
        return self._labels

    @labels.setter
    def labels(self, labels: List[str]):
        """Sets all the label of the _MockPropertyFieldsContainer."""
        if len(self._labels) != 0:
            raise ValueError("labels already set")
        for l in labels:
            self.add_label(l)

    def add_label(self, label: str):
        """Adds a label."""
        if label not in self._labels:
            self._labels.append(label)
            self.scopings.append([])

    def has_label(self, label) -> bool:
        """Check if a _MockPropertyFieldsContainer contains a given label."""
        return label in self.labels

    # used by Dataframe
    def get_label_space(self, idx) -> Dict:
        """Get a Label Space at a given index."""
        return self.label_spaces[idx].dict

    # used by Dataframe
    def get_label_scoping(self, label="time") -> dpf.Scoping:
        """Returns a scoping on the fields concerned by the given label."""
        if label in self.labels:
            scoping_ids = self.scopings[self.labels.index(label)]
            return dpf.Scoping(ids=scoping_ids, location="")
        raise KeyError(f"label {label} not found")

    def add_entry(self, label_space: Dict[str, int], value: dpf.Field):
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

    def add_field(self, label_space: Dict[str, int], field: dpf.Field):
        """Add or update a field at a requested label space."""
        self.add_entry(label_space, field)

    def get_entries(self, label_space_or_index: Union[Dict[str, int], int]):
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
                        if key in ls.dict.keys():
                            if ls.dict[key] != val:
                                to_remove.add(idx)
                        else:
                            to_remove.add(idx)
                    remaining = remaining.difference(to_remove)

                idx_to_field = lambda idx: self.label_spaces[idx].field
                return list(map(idx_to_field, remaining))
            else:
                bad_idx = are_keys_in_labels.index(False)
                bad_key = list(_dict.keys())[bad_idx]
                raise KeyError(f"Key {bad_key} is not in labels: {self.labels}")

    def get_entry(self, label_space_or_index: Union[Dict[str, int], int]):
        """Returns the field or (first field found) corresponding to the given dictionary."""
        ret = self.get_entries(label_space_or_index)

        if len(ret) != 0:
            return ret[0]

        raise ValueError("Could not find corresponding entry")

    def _new_id(self) -> int:
        """Helper method generating a new id when calling add_entry(...)."""
        if len(self.ids) == 0:
            self.last_id = 1
            return self.last_id
        else:
            self.last_id += 1
            return self.last_id

    # used by Dataframe
    def get_fields(self, label_space: Dict[str, int]) -> List[dpf.Field]:
        """Returns the list of fields associated with given label space."""
        return self.get_entries(label_space)

    def get_field(self, label_space_or_index: Union[Dict[str, int], int]) -> dpf.Field:
        """Retrieves the field at a requested index or label space."""
        return self.get_entry(label_space_or_index)

    # used by Dataframe
    def __getitem__(self, key: Union[Dict[str, int], int]) -> dpf.Field:
        """Retrieve the field at a requested index."""
        return self.get_field(key)

    def __len__(self) -> int:
        """Retrieve the number of label spaces."""
        return len(self.label_spaces)
