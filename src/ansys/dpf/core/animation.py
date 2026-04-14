# Copyright (C) 2020 - 2026 ANSYS, Inc. and/or its affiliates.
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

"""Utility functions for creating DPF-based animations."""

from __future__ import annotations

from typing import Any

import numpy as np

import ansys.dpf.core as dpf


def animate_mode(
    fields_container: dpf.FieldsContainer,
    mode_number: int = 1,
    type_mode: int = 0,
    frame_number: int | None = None,
    save_as: str = "",
    deform_scale_factor: float = 1.0,
    **kwargs,
) -> Any:
    """Animate a single mode shape by sweeping its displacement amplitude.

    Extracts the field for *mode_number* from *fields_container*, builds a
    :class:`~ansys.dpf.core.FieldsContainer` of N amplitude-scaled copies of
    that field, and delegates to
    :meth:`FieldsContainer.animate <ansys.dpf.core.FieldsContainer.animate>`.

    The per-frame overlay shows the current relative displacement amplitude
    (ranging from ``-1`` to ``1``) with the physical unit of the result field.

    Parameters
    ----------
    fields_container
        Container of modal results.  Must contain a ``"time"`` label whose IDs
        correspond to mode numbers.
    mode_number
        Mode number to animate.  Must be present in the container's ``"time"``
        label.  The default is ``1``.
    type_mode
        Amplitude profile to use across the frames:

        * ``0`` (default): full cycle, amplitude sweeps ``1 → -1 → 1``.
        * ``1``: positive half only, amplitude sweeps ``1 → 0 → 1``.
    frame_number
        Total number of frames in the animation.
        For ``type_mode=0`` the value is forced to be odd (decremented by one
        if even); defaults to ``41``.
        For ``type_mode=1`` defaults to ``21``.
    save_as
        Path of the file to save the animation to.  Supports any format
        accepted by :func:`pyvista.Plotter.write_frame`, e.g. ``.gif`` or
        ``.mp4``.  Defaults to ``""`` (no file written).
    deform_scale_factor
        Scale factor applied when warping the mesh by the displacement field.
        Defaults to ``1.0``.
    **kwargs
        Additional keyword arguments forwarded to
        :meth:`FieldsContainer.animate <ansys.dpf.core.FieldsContainer.animate>`
        and ultimately to :class:`pyvista.Plotter` (e.g. ``off_screen``,
        ``cpos``, ``framerate``, ``show_axes``).

    Returns
    -------
    Any
        The return value of :func:`pyvista.Plotter.show`.

    Raises
    ------
    ValueError
        If *mode_number* is not present in *fields_container*.
    ValueError
        If *type_mode* is not ``0`` or ``1``.

    Examples
    --------
    Animate the first mode of a modal analysis and save as a GIF.

    >>> import ansys.dpf.core as dpf
    >>> from ansys.dpf.core import animation, examples
    >>> model = dpf.Model(examples.download_modal_frame())
    >>> disp = model.results.displacement.on_all_time_freqs.eval()
    >>> animation.animate_mode(disp, mode_number=1, save_as="mode1.gif")  # doctest: +SKIP

    Use the absolute-value amplitude profile with a custom frame count.

    >>> animation.animate_mode(  # doctest: +SKIP
    ...     disp, mode_number=1, type_mode=1, frame_number=31, save_as="mode1_abs.gif"
    ... )

    """
    # Animation type

    if type_mode == 1:
        if frame_number is None:
            frame_number = 21
        scale_factor_per_frame = list(abs(np.linspace(-1, 1, frame_number, dtype=np.double)))
    elif type_mode == 0:
        if frame_number is None:
            frame_number = 41
        elif frame_number % 2 == 0:
            frame_number -= 1
        half_scale = np.linspace(-1, 1, int((frame_number + 1) / 2), dtype=np.double)
        scale_factor_per_frame = np.concatenate([np.flip(half_scale), half_scale[1:]])
    else:
        raise ValueError(
            f"The type_mode {type_mode} is not accepted. "
            + "Please select one in 'positive_disp' and 'full_disp'."
        )

    # Get fields
    available_mode_numbers = fields_container.get_available_ids_for_label("time")

    if mode_number not in available_mode_numbers:
        raise ValueError(f"The mode {mode_number} data is not available in field container.")
    fields_mode = fields_container.get_fields({"time": mode_number})

    # Merge fields if needed
    if len(fields_mode) > 1:
        merge_op = dpf.operators.utility.merge_fields()
        for i, field in enumerate(fields_mode):
            merge_op.connect(i, field)
        field_mode = merge_op.eval()
    else:
        field_mode = fields_mode[0]

    max_data = float(np.max(field_mode.data))

    # Build a FieldsContainer of N amplitude-scaled copies of the mode field.
    # Each entry is field_mode multiplied by one amplitude value from
    # scale_factor_per_frame, so the standard FieldsContainer.animate path
    # (extract_sub_fc → merge_fields → mesh.from_field) handles mode animation
    # exactly like any other collection, removing a bespoke code path.
    scaled_fields = [
        dpf.operators.math.scale(field=field_mode, weights=float(amp)).eval()
        for amp in scale_factor_per_frame
    ]
    scaled_fc = dpf.fields_container_factory.over_time_freq_fields_container(scaled_fields)

    # Override the TimeFreqSupport so the per-frame overlay shows the current
    # relative displacement amplitude rather than a bare integer frame index.
    amp_field = dpf.fields_factory.field_from_array(
        np.array(scale_factor_per_frame, dtype=np.double)
    )
    amp_field.unit = field_mode.unit
    tfs = dpf.TimeFreqSupport()
    tfs.time_frequencies = amp_field
    scaled_fc.time_freq_support = tfs

    kwargs.setdefault("clim", [0.0, max_data])

    return scaled_fc.animate(
        label="time",
        deform_by=scaled_fc,
        scale_factor=deform_scale_factor,
        save_as=save_as,
        **kwargs,
    )
