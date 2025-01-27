# Copyright (C) 2020 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
time_freq_scoping_factory.

Contains functions to simplify creating time frequency scopings.
"""

from typing import Union

from ansys.dpf.core import Scoping, errors as dpf_errors, types
from ansys.dpf.core.common import locations
from ansys.dpf.core.data_sources import DataSources
from ansys.dpf.core.model import Model
from ansys.dpf.core.operators.metadata import time_freq_provider
from ansys.dpf.core.time_freq_support import TimeFreqSupport


def scoping_by_load_step(load_step: int, server=None):
    """Create a specific ``ansys.dpf.core.Scoping`` for a given load step.

    The returned scoping describes a specific time frequency support element
    for a given load step.

    Parameters
    ----------
    load_step : int
        Load step ID of the specific time frequency scoping.
    server : DpfServer, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Returns
    -------
    scoping : Scoping
        Scoping targeting one load step.
    """
    scoping = Scoping(server=server, ids=[load_step], location=locations.time_freq_step)
    return scoping


def scoping_by_load_steps(load_steps: list, server=None):
    """Create a specific :class:`ansys.dpf.core.Scoping` for a given list of load steps.

    The returned scoping describes a specific time frequency support element
    for a given list of load steps.

    Parameters
    ----------
    load_steps : list[int]
        List of load steps IDs of the specific time frequency scoping.
    server : DpfServer, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Returns
    -------
    scoping : Scoping
        Scoping targeting several load_steps.
    """
    if not isinstance(load_steps, list):
        raise dpf_errors.InvalidTypeError("list", "load_steps")
    scoping = Scoping(server=server, ids=load_steps, location=locations.time_freq_step)
    return scoping


def scoping_by_set(cumulative_set, server=None):
    """Create a specific :class:`ansys.dpf.core.Scoping` for a given cumulative set index.

    The returned scoping describes a specific time frequency support element for a given
    cumulative set index.

    Parameters
    ----------
    cumulative_set : int
        Cumulative index of the set.
    server : DpfServer, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Returns
    -------
    scoping : Scoping
        Scoping targeting one set (referenced by cumulative index).
    """
    scoping = Scoping(server=server, ids=[cumulative_set], location=locations.time_freq)
    return scoping


def scoping_by_sets(cumulative_sets, server=None):
    """Create a specific :class:`ansys.dpf.core.Scoping` for a given list of cumulative set indices.

    The returned scoping describes a specific time frequency support element for a given
    list of cumulative sets of indices.

    Parameters
    ----------
    cumulative_sets : list[int]
        List of cumulative indices of the sets.
    server : DpfServer, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Returns
    -------
    scoping : Scoping
        Scoping targeting severals sets (referenced by cumulative indices).
    """
    if not isinstance(cumulative_sets, list):
        raise dpf_errors.InvalidTypeError("list", "cumulative_sets")
    scoping = Scoping(server=server, ids=cumulative_sets, location=locations.time_freq)
    return scoping


def scoping_by_step_and_substep(load_step_id, subset_id, time_freq_support):
    """Create a specific :class:`ansys.dpf.core.Scoping` for a given step and subset.

    The returned scoping describes a specific time frequency support element for a given
    step and substep.

    Parameters
    ----------
    load_step_id : int
        ID of the load step.
    subset_id : int
        ID of the subset.
    time_freq_support : TimeFreqSupport

    Returns
    -------
    scoping : Scoping
        Scoping based on a given step and substep of a time frequency support.
    """
    set_index = time_freq_support.get_cumulative_index(load_step_id - 1, subset_id - 1)
    scoping = Scoping(
        ids=[set_index + 1],
        location=locations.time_freq,
        server=time_freq_support._server,
    )
    return scoping


def scoping_by_step_and_substep_from_model(load_step_id, subset_id, model, server=None):
    """Create a specific ``ansys.dpf.core.Scoping`` for a given step and substep.

    The returned scoping describes a specific model's time freq support element for a given
    step and substep.

    Parameters
    ----------
    load_step_id : int
        ID of the step.
    subset_id : int
        ID of the subset.
    model : Model
    server : DpfServer, optional
        Server with the channel connected to the remote or local instance.
        The default is ``None``, in which case an attempt is made to use the
        global server.

    Returns
    -------
    scoping : Scoping
        Scoping based on a given step/substep of a model's time_freq_support.
    """
    return scoping_by_step_and_substep(load_step_id, subset_id, model.metadata.time_freq_support)


def scoping_on_all_time_freqs(obj: Union[TimeFreqSupport, Model, DataSources]):
    """Create a Scoping with all time or frequency sets.

    Create a specific :class:`ansys.dpf.core.Scoping` with all time or
    frequency sets of a :class:`ansys.dpf.core.TimeFreqSupport` or a class:`ansys.dpf.core.Model`

    Parameters
    ----------
    tf_support_or_model : TimeFreqSupport, Model

    Returns
    -------
    scoping : Scoping
        Scoping with all time or frequency sets IDs.
    """
    tf_support = None
    if isinstance(obj, TimeFreqSupport):
        tf_support = obj
    elif isinstance(obj, Model):
        tf_support = obj.metadata.time_freq_support
    elif isinstance(obj, DataSources):
        tf_provider = time_freq_provider(data_sources=obj, server=obj._server)
        tf_support = tf_provider.get_output(output_type=types.time_freq_support)

    if tf_support == None:
        supported_types = f"{TimeFreqSupport}, {Model}, {DataSources}"
        raise TypeError(f"Given type was {type(obj)} while accepted types are {supported_types}")

    return Scoping(
        ids=range(1, len(tf_support.time_frequencies) + 1),
        location=locations.time_freq,
        server=tf_support._server,
    )
