from ansys.dpf import core as dpf

"""
.. _ref_data_containers:

Data Containers
===============
This example explains how some DPF data containers are defined and manipulated. They are: Field, Fields Container and 
Generic Data container 

# When post-processing a simulation with DPF the typical basic steps are:
# 1- Load the result File
# 2- Access the data
# 3- Transform the data
# 4- Display the new results
# 5- Export the new results


When DPF uses operators to load and operate on data, it uses field containers and fields to store and return data. 
In order to execute the second and third basic steps we need to be aware of how the data is structured in the data 
containers. A field’s data is always associated to: 
    - The data 'Location': What typology of the finite element method was used to give the results.There are three 
    different spatial locations : 'Nodal', 'Elemental' and 'Elemental Nodal'.
    - The support: The simulation basis functions are integrated over a calculus domain, the support of the analysis. 
    This domain is a physical component, usually represented by: a mesh, geometrical component, time or frequency values    

So, when defining an operator, we need to specify the scoping of the field that we are interested in. The scoping is a 
spatial and/or temporal subset of the support.

A field can be created or directly by an instance of this class, by the 'fields_factory' class, or it can be an 
evaluated data from the 'Operator' class
"""

# First, import the DPF-Core module as ``dpf`` and import the included examples file.
from ansys.dpf import core as dpf
from ansys.dpf.core import examples

##########################################################################################
# Next, open an example and create the ``model`` object. The
# :class:`Model <ansys.dpf.core.model.Model>` class helps to organize access methods
# for the result by keeping track of the operators and data sources used by the result
# file.
#
# Printing the model displays:
#
# * Analysis type
# * Available results : with their name and location
# * Size of the mesh: number of nodes and elements in the mesh
# * Number of results: with the support type

my_model = dpf.Model(examples.download_transient_result())
# print(my_model)

##########################################################################################
# **Scoping**
# First of all, to begin the workflow set up, we need to define the extent of the results that we want to analyse. Thus,
# we define the scope, that allows us to define this specific group of results. The groups can be based on time or space
# domains.
# If the scoping is not specified the operators will get only the final result data.
# We can see in our model that the displacement results are available with a time support.
my_disp = my_model.results.displacement()  # create the displacement operator from the :class:'displacement' <ansys.dpf.core.operators.result.displacement> class
print(my_disp.eval())  # Print the results output

##########################################################################################
# There are several ways to scope the result, but they can be separate in two main categories:
# * Scope results over custom time domains
# * Scope results over custom space domains
# Specific examples about how to implement those scopings can be found at:
# * :mod:'ref_results_over_time'
# * :mod:'ref_results_over_space'

##########################################################################################
# **Fields Container**
# A field container is a collection of fields ordered by labels and IDs. Each field of the fields container has an ID
# for each label. These IDs allow splitting the fields on several criteria.

# Following with the displacement operator, we can verify that it gives us a field container as an output.
print(my_disp.outputs)  # Print the available output types

# We will get the displacement for all the time support to facilitate the fields container visualisation.
my_disp = my_model.results.displacement.on_all_time_freqs()  # time scoping with a helper for the class :class:'Result' <ansys.dpf.core.results.Result>
print(my_disp.eval())

##########################################################################################
# We see this field container has 35 fields with a 'time' label. So to access those fields there are several methods,
# either by Pythonic indexing, either by the function from the class :class:'FieldsContainer' <ansys.dpf.core.fields_container




# The GenericDataContainer operator is a class available as a submodule of the 'ansys.dpf.core' package. It maps
# properties to their DPF supported Data Types if they are not previously specified
#
# 1) function set_property()
# --------------------------
# If you ae