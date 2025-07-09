# DPF known types

Inputs or outputs of DPF operators and workflows are limited to the following types known by the framework.

## Standard types

<a id="standard-types"></a>

DPF understands most standard types out-of-the-box.
The following are standard types found in the current standard installation:

- bool
- char
- uint32
- uint64
- int32
- double
- string
- vector of bool
- vector of char
- vector of double
- vector of float
- vector of int32
- vector of string

## DPF basic types

The following is an exhaustive list of available DPF types.

### Any

<a id="any"></a>


The ``any`` type is the generic type of DPF. It allows to share on object without an explicit type.
Most DPF types can be cast as or from an ``Any`` which is useful when type enforcement is unnecessary. 

### Data processing

#### Operator

<a id="operator"></a>

The ``operator`` is the building block of DPF.
It holds data processing logic and generates outputs from its inputs when executed.

#### Workflow

<a id="workflow"></a>

The ``workflow`` is a connected set of operators.
It itself has inputs and outputs, and allows to package and share complex combinations of operators.

### File management

#### Data sources

<a id="data-sources"></a>

The ``data_sources`` holds information on files of interest such as:

- their path
- their associated namespace
- their associated key (usually the file extension)

#### Streaming

<a id="streams-container"></a>

The ``streams_container`` is the result of opening a stream to files in a ``data_sources``.
It enables streaming to and from the files and handles caching of data requests to the files.

The use of a ``streams_container`` is highly recommended whenever possible to benefit from IO performance features.

### Metadata

The following DPF objects hold light-weight data (metadata) relative to other DPF types.

#### Field metadata

<a id="field-definition"></a>

The ``field_definition`` holds metadata relative to a ``field``.

#### Mesh metadata

<a id="mesh-info"></a>

The ``mesh_info`` holds metadata relative to a ``meshed_region``.

Only available for CFF and LSDYNA.

#### Result file metadata

<a id="result-info"></a>

The ``result_info`` holds metadata relative to available results in files from a ``data_sources``.

### Data supports

<a id="support"></a>

Supports are entities dedicated to holding information about the model itself.

Every ``field`` requires a ``support`` for DPF to understand what its data is related to.

This concept allows DPF to manage simulation data efficiently.

#### Mesh

<a id="meshed-region"></a>

The ``meshed_region`` holds information relative to the mesh of the simulation model.

It gives access to several fields of data such as:
- the mesh connectivity
- the node coordinates
- the element types

#### Time and frequency

<a id="time-freq-support"></a>

For time and pseudo time based simulations or for frequency based simulations, the ``time_freq_support`` holds information about the 
simulation steps and sub-steps, time-steps, or mode/harmonic frequencies.

#### Cyclic

<a id="cyclic-support"></a>

For cyclic simulation models, the ``cyclic_support`` holds information about the number of sectors and the number of stages.

### Filtering

<a id="filtering"></a>

When handling large amounts of simulation data, you can select a subset of the data and filter it down to the data of interest to the analysis.

In the DPF ecosystem this is called ``scoping`` the data, and is managed with ``scoping`` entities.

#### Scoping

<a id="scoping"></a>

A ``scoping`` describes a typed list of IDs. 

It has a ``location``, which defines the type of entity the IDs apply to (nodes, elements, time-steps, parts...), and a list of ``ids``.

It allows you to select and filter data when given as input to operators, or data description when produced as output.

Each ``field`` data storage type has a ``scoping`` associated to it, describing the subset of its ``support`` that the data applies to. The data in a ``field`` is ordered the same way as the IDs in the ``scoping``.

### Data storage

<a id="data storage"></a>

The following DPF types allow you to store and describe data.

#### Data map

<a id="generic-data-container"></a>

The ``generic_data_container`` allows you to store any type known to DPF as a property with a given name.

#### Data tree

<a id="data-tree"></a>

The ``data_tree`` allows you to store DPF known types as named attributes of a data tree with sub-trees.

#### Data arrays

<a id="arrays"></a>

The following types represent arrays of data.

The data of a ``field`` is always associated to a ``scoping`` (entities associated to each value) and ``support`` (subset of the model where the data is), making the ``field`` a self-describing piece of data.

Example 1: a ``field`` that describes the evolution in time of the static pressure at a given face of a fluid model has a scoping comprised of the time step ids where the pressure is defined and a ``time-frequency`` support that stores the relationship between time ids and time values. 

Example 2: a ``field`` that describes the evolution in space of the stress at a given body of a structural model has a scoping comprised of the element ids where the stress is defined and a ``meshed_region`` support that contextualizes these element ids. 

##### Doubles

<a id="field"></a>

The ``field`` represents an array of double values.

##### Integers

<a id="property-field"></a>

The ``property_field`` represents an array of integer values.

##### Strings

<a id="string-field"></a>

The ``string_field`` represents an array of string values.

##### Custom

<a id="custom-type-field"></a>

The ``custom_type_field`` represents an array of values of a custom type as defined by the unitary type of the field.

### Collections

<a id="collections"></a>

DPF allows you to group DPF types in labeled collections.

A DPF ``collection`` has a set of associated labels, for which each entry has a value. This allows you to distinguish between entries and retrieve them. 

#### Label space
<a id="label-space"></a>

The ``label_space`` is a map of ("label": integer value) couples used to target a subset of entries in a collection.

For example, if a ``collection`` has labels ``material`` and ``part``, each entity in the collection has an associated unique map ``{"material": X, "part": Y}``.

A ``label_space`` such as ``{"material": X, "part": Y}`` then targets a single entity in the collection, whereas one such as ``{"material": X}`` targets all entries of material "X".

#### Base collection

<a id="collection"></a>

The ``collection`` is the generic type for collections of DPF entities.

#### Collection of any

<a id="any-collection"></a>

The ``any_collection`` is a collection of ``Any`` objects. 

#### Collection of fields of custom type

<a id="custom-type-fields-container"></a>

The ``custom_type_fields_container`` is a collection of ``custom_type_field`` instances.

#### Collection of fields of doubles

<a id="fields-container"></a>

The ``fields_container`` is a collection of ``field`` instances.

#### Collection of fields of integers

<a id="property-fields-container"></a>

The ``property_fields_container`` is a collection of ``property_field`` instances.

#### Collection of meshes

<a id="meshes-container"></a>

The ``meshes_container`` is a collection of ``meshed_region`` instances.

#### Collection of scopings

<a id="scopings-container"></a>

The ``scopings_container`` is a collection of ``scoping`` instances.

### Unit systems

Some operators take in a unit system, defined using the ``UnitSystem`` type.
