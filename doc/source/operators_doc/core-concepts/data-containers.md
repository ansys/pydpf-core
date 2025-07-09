# Entities used in DPF operators

## Field

The field is the main simulation data container. In numerical simulations, results data are defined by values associated to entities (scoping), and these entities are a subset of a model (support). In DPF, field data is always associated to its scoping and support, making the field a self-describing piece of data. A field is also defined by its dimensionnality, unit, location... A field can for example, describe a displacement vector or norm, stresses and strains tensors, stresses and strains equivalent, min max over time of any result... It can be defined on a complete model or just on certain entities of the model thanks to its scoping. The data is stored as a vector of double values and each elementary entity has a number of components (thanks to the dimensionality, a displacement will have 3 components, a symmetrical stress matrix 6...)

## Scoping

The scoping is entities ids representing a subset of the model's support. Typically, scoping can represent node ids, element ids, time steps, frequencies, joints... Its location indicates what kind of entity the scoping is referring to. Scopings are used to identify the entities where a field is scoped or to choose (through an input pin) a subset on which an operator should compute its result.

## Data Sources

The data sources is a container of files on which the analysis results can be found.

## Streams

Streams is an entity containing the data sources. Once the files in the streams are opened, they stay opened and they keep some data in cache to make the next evaluations faster. To close the files, release the streams.

## Support

The support describes the model. It can be the mesh, geometric entities, time or frequency domain...

## Fields Container

The fields container is a container of fields, used mainly in transient, harmonic, modal or multi-steps static analysis, where we can have a field for each time step or for each frequency. Consequently the fields container can describle a complete analysis with all its details. The fields container is designed as a set of fields ordered through labels and ids. Labels identify how the fields are filtered. The most common fields container have the label "time" with ids corresponding to each time sets, the label "complex" will allow to separate real parts (id=0) from imaginary parts (id=1) in a harmonic analysis.

## Meshed Region

The meshed region is dpf's entity describing a mesh. Node and element scopings, element types, connectivity (list of node indices composing each element) and node coordinates are the fundamental entities composing the meshed region. It can also have materials, named selections...

## Time Freq Support

The time freq support describes an analysis'temporal or frequential space. For a transient analysis all the time sets cumulatives indices with their times are described. For a harmonic analysis, the real and imaginary frequencies, the RPMs, the load steps are described.

## Model

The model is a helper designed to give shortcuts to the user to access a model's metadata and to instanciate results provider for this model. A Model is able to open a DataSources or a Streams to read the metadata and expose it to the user. The metadata is made of all the entities describing a model: its MeshedRegion, its TimeFreqSupport and it's ResultInfo. With the model, the user can easily access information about the mesh, about the time/freq steps and substeps used in the analysis and the list of available results.

## Basic types


