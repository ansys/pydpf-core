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

"""Cyclic Support."""

import traceback
import warnings

from ansys.dpf.core import field, property_field, server as server_module
from ansys.dpf.core.scoping import Scoping
from ansys.dpf.gate import cyclic_support_capi, cyclic_support_grpcapi


class CyclicSupport:
    """Represents a cyclic support, which describes a model with cyclic symmetry.

    The model has the necessary data for cyclic (and multistage) expansion.

    Parameters
    ----------
    cyclic_support : ansys.grpc.dpf.cyclic_support_pb2.CyclicSupport message
        Cyclic support.
    server : DPFServer , optional
        Server with the channel connected to the remote or local instance. The default is
        ``None``, in which case an attempt is made to use the global server.

    Examples
    --------
    Get a cyclic support from a model.

    >>> from ansys.dpf import core as dpf
    >>> from ansys.dpf.core import examples
    >>> multi_stage = examples.download_multi_stage_cyclic_result()
    >>> model = dpf.Model(multi_stage)
    >>> result_info = model.metadata.result_info
    >>> cyc_support = result_info.cyclic_support
    >>> cyc_support.num_sectors()
    6
    >>> cyc_support.num_stages
    2

    """

    def __init__(self, cyclic_support, server=None):
        """Initialize time frequency support with its `TimeFreqSupport` message (if possible)."""
        # step 1: get server
        self._server = server_module.get_or_create_server(
            cyclic_support._server if isinstance(cyclic_support, CyclicSupport) else server
        )

        # step 2: get api
        self._api = self._server.get_api_for_type(
            capi=cyclic_support_capi.CyclicSupportCAPI,
            grpcapi=cyclic_support_grpcapi.CyclicSupportGRPCAPI,
        )

        # step3: init environment
        self._api.init_cyclic_support_environment(self)  # creates stub when gRPC

        # step4: take object instance
        self._internal_obj = cyclic_support

    def __str__(self):
        """Describe the entity.

        Returns
        -------
        str
            Description of the entity.
        """
        from ansys.dpf.core.core import _description

        return _description(self._internal_obj, self._server)

    @property
    def num_stages(self) -> int:
        """Number of cyclic stages in the model.

        Examples
        --------
        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> multi_stage = examples.download_multi_stage_cyclic_result()
        >>> cyc_support = Model(multi_stage).metadata.result_info.cyclic_support
        >>> cyc_support.num_stages
        2

        Returns
        -------
        int
            Number of cyclic stages in the model.
        """
        return self._api.cyclic_support_get_num_stages(self)

    def num_sectors(self, stage_num=0) -> int:
        """Determine number of sectors to expand on 360 degrees.

        Parameters
        ----------
        stage_num : int , optional
            Number of the stages required (from 0 to num_stages).

        Returns
        -------
        int
            Number of sectors to expand on 360 degrees.

        Examples
        --------
        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> multi_stage = examples.download_multi_stage_cyclic_result()
        >>> cyc_support = Model(multi_stage).metadata.result_info.cyclic_support
        >>> cyc_support.num_sectors(0)
        6
        >>> cyc_support.num_sectors(1)
        12

        """
        return self._api.cyclic_support_get_num_sectors(self, stage_num)

    def base_nodes_scoping(self, stage_num=0) -> Scoping:
        """Retrieve a nodal scoping containing node IDs in the base sector of the given stage.

        Parameters
        ----------
        stage_num : int, optional
            Number of the stage required (from 0 to num_stages).

        Returns
        -------
        base_nodes_scoping : Scoping
            Nodes IDs in the base sector of the given stage.

        Examples
        --------
        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> multi_stage = examples.download_multi_stage_cyclic_result()
        >>> cyc_support = Model(multi_stage).metadata.result_info.cyclic_support
        >>> base = cyc_support.base_nodes_scoping(0)

        """
        base_node_scoping = self._api.cyclic_support_get_base_nodes_scoping(self, stage_num)
        return Scoping(scoping=base_node_scoping, server=self._server)

    def base_elements_scoping(self, stage_num=0) -> Scoping:
        """Retrieve an elemental scoping containing elements IDs in the base sector of the given stage.

        Parameters
        ----------
        stage_num : int, optional
            Number of the stage required (from 0 to num_stages).

        Returns
        -------
        base_elements_scoping : Scoping
            Elements ids in the base sector of the given stage.

        Examples
        --------
        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> multi_stage = examples.download_multi_stage_cyclic_result()
        >>> cyc_support = Model(multi_stage).metadata.result_info.cyclic_support
        >>> base = cyc_support.base_elements_scoping(stage_num=1)

        """
        base_element_scoping = self._api.cyclic_support_get_base_elements_scoping(self, stage_num)
        return Scoping(scoping=base_element_scoping, server=self._server)

    def sectors_set_for_expansion(self, stage_num=0) -> Scoping:
        """Retrieve a sector's scoping from expanded results and mesh, or list of sectors for default expansion.

        A sector's scoping starts from 0, with the maximum equal to num_sectors-1.

        Parameters
        ----------
        stage_num : int, optional
            Number of the stage required (from 0 to num_stages).

        Returns
        -------
        sectors_set_for_expansion : Scoping
            List of sectors (starting from 0 to max = num_sectors-1).

        Examples
        --------
        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> multi_stage = examples.download_multi_stage_cyclic_result()
        >>> cyc_support = Model(multi_stage).metadata.result_info.cyclic_support
        >>> sectors_scoping = cyc_support.sectors_set_for_expansion(stage_num=1)
        >>> print(sectors_scoping.ids)
        [...0... 1... 2... 3... 4... 5... 6... 7... 8... 9... 10... 11]

        """
        sectors_for_expansion = self._api.cyclic_support_get_sectors_scoping(self, stage_num)
        return Scoping(scoping=sectors_for_expansion, server=self._server)

    def expand_node_id(self, node_id, sectors=None, stage_num=0):
        """Retrieve the node IDs corresponding to the base sector node ID given in the input after expansion.

        Parameters
        ----------
        node_id : int
            Base sector's node ID to expand.
        sectors : Scoping , list of int, optional
            List of sectors to expand (from 0 to ``num_sectors - 1``).
            The default is ``None``, in which case all sectors are expanded.
        stage_num : int, optional
            Number of the stage required (from 0 to ``num_stages``).

        Returns
        -------
        sectors_set_for_expansion : Scoping
            List of sectors (starting from 0 to ``num_sectors - 1``).

        Examples
        --------
        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> multi_stage = examples.download_multi_stage_cyclic_result()
        >>> cyc_support = Model(multi_stage).metadata.result_info.cyclic_support
        >>> expanded_scoping = cyc_support.expand_node_id(1,stage_num=0)
        >>> print(expanded_scoping.ids)
        [...1... 3596... 5816... 8036... 10256... 12476]

        """
        if sectors is None:
            num_sectors = self._api.cyclic_support_get_num_sectors(self, stage_num)
            sectors = list(range(num_sectors))
        if isinstance(sectors, list):
            sectors = Scoping(ids=sectors, location="sectors", server=self._server)
        expanded_ids = self._api.cyclic_support_get_expanded_node_ids(
            self, node_id, stage_num, sectors
        )
        return Scoping(scoping=expanded_ids, server=self._server)

    def expand_element_id(self, element_id, sectors=None, stage_num=0):
        """Retrieve the element IDs corresponding to the base sector element ID given in the input after expansion.

        Parameters
        ----------
        element_id : int
            Base sector's element ID to expand.
        sectors : Scoping or list of int, optional
            List of sectors to expand (from 0 to ``num_sectors - 1``).
            The default is ``None``, in which case all sectors are expanded.
        stage_num : int, optional
            Number of the stage required (from 0 to ``num_stages``).

        Returns
        -------
        sectors_set_for_expansion : Scoping
            List of sectors (starting from 0 to ``num_sectors - 1``).

        Examples
        --------
        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> multi_stage = examples.download_multi_stage_cyclic_result()
        >>> cyc_support = Model(multi_stage).metadata.result_info.cyclic_support
        >>> expanded_scoping = cyc_support.expand_element_id(1,stage_num=0)
        >>> print(expanded_scoping.ids)
        [...1... 1558... 2533... 3508... 4483... 5458]

        """
        if sectors is None:
            num_sectors = self._api.cyclic_support_get_num_sectors(self, stage_num)
            sectors = list(range(num_sectors))
        if isinstance(sectors, list):
            sectors = Scoping(ids=sectors, location="sectors", server=self._server)
        expanded_ids = self._api.cyclic_support_get_expanded_element_ids(
            self, element_id, stage_num, sectors
        )
        return Scoping(scoping=expanded_ids, server=self._server)

    def cs(self) -> field.Field:
        """Coordinate system of the cyclic support.

        Examples
        --------
        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> multi_stage = examples.download_multi_stage_cyclic_result()
        >>> cyc_support = Model(multi_stage).metadata.result_info.cyclic_support
        >>> cs = cyc_support.cs()

        """
        cs = self._api.cyclic_support_get_cs(self)
        return field.Field(field=cs, server=self._server)

    def low_high_map(self, stage_num: int = 0) -> property_field.PropertyField:
        """Retrieve a property field containing node map from low to high base sector of the given stage.

        Parameters
        ----------
        stage_num:
            Number of the stage required (from 0 to num_stages).

        Returns
        -------
        low_high_map:
            Node correspondence between low to high in the base sector of the given stage.

        Examples
        --------
        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> multi_stage = examples.download_multi_stage_cyclic_result()
        >>> cyc_support = Model(multi_stage).metadata.result_info.cyclic_support
        >>> low_high_map = cyc_support.low_high_map(0)

        """
        low_high_map = self._api.cyclic_support_get_low_high_map(self, stage_num)
        return property_field.PropertyField(property_field=low_high_map, server=self._server)

    def high_low_map(self, stage_num: int = 0) -> property_field.PropertyField:
        """Retrieve a property field containing node map from high to low base sector of the given stage.

        Parameters
        ----------
        stage_num:
            Number of the stage required (from 0 to num_stages).

        Returns
        -------
        low_high_map:
            Node correspondence between high to low in the base sector of the given stage.

        Examples
        --------
        >>> from ansys.dpf.core import Model
        >>> from ansys.dpf.core import examples
        >>> multi_stage = examples.download_multi_stage_cyclic_result()
        >>> cyc_support = Model(multi_stage).metadata.result_info.cyclic_support
        >>> high_low_map = cyc_support.high_low_map(0)

        """
        high_low_map = self._api.cyclic_support_get_high_low_map(self, stage_num)
        return property_field.PropertyField(property_field=high_low_map, server=self._server)

    def __del__(self):
        """Delete this instance."""
        try:
            self._deleter_func[0](self._deleter_func[1](self))
        except:
            warnings.warn(traceback.format_exc())
