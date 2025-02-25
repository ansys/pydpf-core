"""
kmeans_clustering

Autogenerated DPF operator classes.
"""

from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class kmeans_clustering(Operator):
    """Apply kMeans clustering to group data depending on the data's non-
    linearity.

    Parameters
    ----------
    clusters_number : int, optional
        Number of the clusters (dafault is 3)
    formula : str, optional
        Formula ('dist'/'dotprod'), default is 'dist'
    fields_container : FieldsContainer
        An iunput fields container containing the
        data which will be used for the
        clustering
    component_number : int, optional
        Component number as an int (default is 0), ex
        '0' for x-displacement, '1' for
        y-displacement,...

    Returns
    -------
    scoping_clusters : ScopingsContainer
        Scopings container with the space scoping
        (entities' ids) corresponding to each
        of k-clusters

    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.compression.kmeans_clustering()

    >>> # Make input connections
    >>> my_clusters_number = int()
    >>> op.inputs.clusters_number.connect(my_clusters_number)
    >>> my_formula = str()
    >>> op.inputs.formula.connect(my_formula)
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_component_number = int()
    >>> op.inputs.component_number.connect(my_component_number)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.compression.kmeans_clustering(
    ...     clusters_number=my_clusters_number,
    ...     formula=my_formula,
    ...     fields_container=my_fields_container,
    ...     component_number=my_component_number,
    ... )

    >>> # Get output data
    >>> result_scoping_clusters = op.outputs.scoping_clusters()
    """

    def __init__(
        self,
        clusters_number=None,
        formula=None,
        fields_container=None,
        component_number=None,
        config=None,
        server=None,
    ):
        super().__init__(name="kmeans_operator", config=config, server=server)
        self._inputs = InputsKmeansClustering(self)
        self._outputs = OutputsKmeansClustering(self)
        if clusters_number is not None:
            self.inputs.clusters_number.connect(clusters_number)
        if formula is not None:
            self.inputs.formula.connect(formula)
        if fields_container is not None:
            self.inputs.fields_container.connect(fields_container)
        if component_number is not None:
            self.inputs.component_number.connect(component_number)

    @staticmethod
    def _spec():
        description = """Apply kMeans clustering to group data depending on the data's non-
            linearity."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="clusters_number",
                    type_names=["int32"],
                    optional=True,
                    document="""Number of the clusters (dafault is 3)""",
                ),
                1: PinSpecification(
                    name="formula",
                    type_names=["string"],
                    optional=True,
                    document="""Formula ('dist'/'dotprod'), default is 'dist'""",
                ),
                2: PinSpecification(
                    name="fields_container",
                    type_names=["fields_container"],
                    optional=False,
                    document="""An iunput fields container containing the
        data which will be used for the
        clustering""",
                ),
                3: PinSpecification(
                    name="component_number",
                    type_names=["int32"],
                    optional=True,
                    document="""Component number as an int (default is 0), ex
        '0' for x-displacement, '1' for
        y-displacement,...""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="scoping_clusters",
                    type_names=["scopings_container"],
                    optional=False,
                    document="""Scopings container with the space scoping
        (entities' ids) corresponding to each
        of k-clusters""",
                ),
            },
        )
        return spec

    @staticmethod
    def default_config(server=None):
        """Returns the default config of the operator.

        This config can then be changed to the user needs and be used to
        instantiate the operator. The Configuration allows to customize
        how the operation will be processed by the operator.

        Parameters
        ----------
        server : server.DPFServer, optional
            Server with channel connected to the remote or local instance. When
            ``None``, attempts to use the global server.
        """
        return Operator.default_config(name="kmeans_operator", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsKmeansClustering
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsKmeansClustering
        """
        return super().outputs


class InputsKmeansClustering(_Inputs):
    """Intermediate class used to connect user inputs to
    kmeans_clustering operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.compression.kmeans_clustering()
    >>> my_clusters_number = int()
    >>> op.inputs.clusters_number.connect(my_clusters_number)
    >>> my_formula = str()
    >>> op.inputs.formula.connect(my_formula)
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_component_number = int()
    >>> op.inputs.component_number.connect(my_component_number)
    """

    def __init__(self, op: Operator):
        super().__init__(kmeans_clustering._spec().inputs, op)
        self._clusters_number = Input(kmeans_clustering._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._clusters_number)
        self._formula = Input(kmeans_clustering._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._formula)
        self._fields_container = Input(
            kmeans_clustering._spec().input_pin(2), 2, op, -1
        )
        self._inputs.append(self._fields_container)
        self._component_number = Input(
            kmeans_clustering._spec().input_pin(3), 3, op, -1
        )
        self._inputs.append(self._component_number)

    @property
    def clusters_number(self):
        """Allows to connect clusters_number input to the operator.

        Number of the clusters (dafault is 3)

        Parameters
        ----------
        my_clusters_number : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.compression.kmeans_clustering()
        >>> op.inputs.clusters_number.connect(my_clusters_number)
        >>> # or
        >>> op.inputs.clusters_number(my_clusters_number)
        """
        return self._clusters_number

    @property
    def formula(self):
        """Allows to connect formula input to the operator.

        Formula ('dist'/'dotprod'), default is 'dist'

        Parameters
        ----------
        my_formula : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.compression.kmeans_clustering()
        >>> op.inputs.formula.connect(my_formula)
        >>> # or
        >>> op.inputs.formula(my_formula)
        """
        return self._formula

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator.

        An iunput fields container containing the
        data which will be used for the
        clustering

        Parameters
        ----------
        my_fields_container : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.compression.kmeans_clustering()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> # or
        >>> op.inputs.fields_container(my_fields_container)
        """
        return self._fields_container

    @property
    def component_number(self):
        """Allows to connect component_number input to the operator.

        Component number as an int (default is 0), ex
        '0' for x-displacement, '1' for
        y-displacement,...

        Parameters
        ----------
        my_component_number : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.compression.kmeans_clustering()
        >>> op.inputs.component_number.connect(my_component_number)
        >>> # or
        >>> op.inputs.component_number(my_component_number)
        """
        return self._component_number


class OutputsKmeansClustering(_Outputs):
    """Intermediate class used to get outputs from
    kmeans_clustering operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.compression.kmeans_clustering()
    >>> # Connect inputs : op.inputs. ...
    >>> result_scoping_clusters = op.outputs.scoping_clusters()
    """

    def __init__(self, op: Operator):
        super().__init__(kmeans_clustering._spec().outputs, op)
        self._scoping_clusters = Output(kmeans_clustering._spec().output_pin(0), 0, op)
        self._outputs.append(self._scoping_clusters)

    @property
    def scoping_clusters(self):
        """Allows to get scoping_clusters output of the operator

        Returns
        ----------
        my_scoping_clusters : ScopingsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.compression.kmeans_clustering()
        >>> # Connect inputs : op.inputs. ...
        >>> result_scoping_clusters = op.outputs.scoping_clusters()
        """  # noqa: E501
        return self._scoping_clusters
