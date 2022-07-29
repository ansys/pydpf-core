"""
time_freq_scoping_factory
=========================

Contains functions to simplify creating time frequency scopings.
"""

from ansys.dpf.core import Scoping
from ansys.dpf.core import errors as dpf_errors
from ansys.dpf.core.common import locations
from ansys.dpf.core.model import Model


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


def scoping_by_step_and_substep(
        load_step_id, subset_id, time_freq_support
):
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
        server=time_freq_support._server)
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
        Scoping based on a given step/substep of a model's time_freq_support."""
    return scoping_by_step_and_substep(
        load_step_id, subset_id, model.metadata.time_freq_support
    )


def scoping_on_all_time_freqs(tf_support_or_model):
    """Create a specific :class:`ansys.dpf.core.Scoping` with all time or
    frequency sets of a :class:`ansys.dpf.core.TimeFreqSupport` or a class:`ansys.dpf.core.Model`

    Parameters
    ----------
    tf_support_or_model : TimeFreqSupport, Model

    Returns
    -------
    scoping : Scoping
        Scoping with all time or frequency sets IDs.
    """
    if isinstance(tf_support_or_model, Model):
        tf_support_or_model = tf_support_or_model.metadata.time_freq_support
    return Scoping(
        ids=range(1, len(tf_support_or_model.time_frequencies) + 1),
        location=locations.time_freq,
        server=tf_support_or_model._server)
