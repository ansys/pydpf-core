#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the ``ansys.dpf.core`` module
from ansys.dpf import core as dpf
# Import the math operators module
from ansys.dpf.core.operators import math as maths


# In[2]:


# Create four nodal 3D vector fields of size 2
num_entities = 2
field1 = dpf.Field(nentities=num_entities)
field2 = dpf.Field(nentities=num_entities)
field3 = dpf.Field(nentities=num_entities)
field4 = dpf.Field(nentities=num_entities)

# Set the scoping IDs
field1.scoping.ids = field2.scoping.ids = field3.scoping.ids = field4.scoping.ids = range(num_entities)

# Set the data for each field using flat lists (of size = num_entities * num_components)
field1.data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
field2.data = [7.0, 3.0, 5.0, 8.0, 1.0, 2.0]
field3.data = [6.0, 5.0, 4.0, 3.0, 2.0, 1.0]
field4.data = [4.0, 1.0, 8.0, 5.0, 7.0, 9.0]

# Print the fields
print("Field 1","\n", field1, "\n"); print("Field 2","\n", field2, "\n");
print("Field 3","\n", field3, "\n"); print("Field 4","\n", field4, "\n")


# In[3]:


# Create the field containers
fc1 = dpf.fields_container_factory.over_time_freq_fields_container(fields=[field1, field2])
fc2 = dpf.fields_container_factory.over_time_freq_fields_container(fields=[field3, field4])

# Print the field containers
print("FieldsContainer1","\n", fc1, "\n")
print("FieldsContainer2","\n", fc2, "\n")


# In[4]:


# Instantiate two nodal 3D vector fields of length 3
field5 = dpf.Field(nentities=3)
field6 = dpf.Field(nentities=3)

# Set the data for each field
field5.data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
field6.data = [5.0, 1.0, 6.0, 3.0, 8.0, 9.0, 7.0, 2.0, 4.0]

# Set the scoping IDs (here node IDs)
field5.scoping.ids = [1, 2, 3]
field6.scoping.ids = [3, 4, 5]

# Print the fields
print("Field 5", "\n", field5, "\n")
print("Field 6", "\n", field6, "\n")


# In[5]:


# Use the add operator
add_scop = dpf.operators.math.add(fieldA=field5, fieldB=field6).eval()

# Print the result
# The resulting field only contains data for entities where a match is found in the other field.
# It has the size of the intersection of the two scopings.
# Here this means the addition returns a field with data only for the node with ID=3.
# This behavior is specific to each operator.
print(add_scop, "\n")


# In[6]:


# Use the dot product operator
dot_scop = dpf.operators.math.generalized_inner_product(fieldA=field5, fieldB=field6).eval()
# ID 3: (7. * 5.) + (8. * 1.) + (9. * 6.)

# Print the result
# The operator returns zero for entities where no match is found in the other field.
# The resulting field is the size of the union of the two scopings.
# This behavior is specific to each operator.
print(dot_scop,"\n")
print(dot_scop.data,"\n")


# In[7]:


# Add the fields
add_field = maths.add(fieldA=field1, fieldB=field2).eval()
# id 0: [1.+7. 2.+3. 3.+5.] = [ 8.  5.  8.]
# id 1: [4.+8. 5.+1. 6.+2.] = [12.  6.  8.]

# Print the results
print("Addition field ", add_field , "\n")


# In[8]:


# Add the two field collections
add_fc = maths.add_fc(fields_container1=fc1, fields_container2=fc2).eval()
# {time: 1}: field1 + field3
#           -->      id 0: [1.+6. 2.+5. 3.+4.] = [7. 7. 7.]
#                    id 1: [4.+3. 5.+2. 6.+1.] = [7. 7. 7.]
#
# {time: 2}: field2 + field4
#           -->      id 0: [7.+4. 3.+1. 5.+8.] = [11. 4. 13.]
#                    id 1: [8.+5. 1.+7. 2.+9.] = [13. 8. 11.]

# Print the results
print("Addition FieldsContainers","\n", add_fc , "\n")
print(add_fc.get_field({"time":1}), "\n")
print(add_fc.get_field({"time":2}), "\n")


# In[9]:


# Compute the total sum of a field
tot_sum_field = maths.accumulate(fieldA=field1).eval()
# vector component 0 = 1. + 4. = 5.
# vector component 1 = 2. + 5. = 7.
# vector component 2 = 3. + 6. = 9.

# Print the results
print("Total sum fields","\n", tot_sum_field, "\n")


# In[10]:


# Find the total sum of the two field collections
tot_sum_fc = maths.accumulate_fc(fields_container=fc1).eval()
# {time: 1}: field1
#           -->      vector component 0 = 1.+ 4. = 5.
#                    vector component 1 = 2.+ 5. = 7.
#                    vector component 2 = 3.+ 6. = 9.
#
# {time: 2}: field2
#           -->      vector component 0 = 7.+ 8. = 15.
#                    vector component 1 = 3.+ 1. = 4.
#                    vector component 2 = 5.+ 2. = 7.

# Print the results
print("Total sum FieldsContainers","\n", tot_sum_fc , "\n")
print(tot_sum_fc.get_field({"time":1}), "\n")
print(tot_sum_fc.get_field({"time":2}), "\n")


# In[11]:


# Define the scale factor field
scale_vect = dpf.Field(nentities=num_entities, nature=dpf.natures.scalar)
# Set the scale factor field scoping IDs
scale_vect.scoping.ids = range(num_entities)
# Set the scale factor field data
scale_vect.data = [5., 2.]

# Compute the total sum of the field using a scaling field
tot_sum_field_scale = maths.accumulate(fieldA=field1, weights=scale_vect).eval()
# vector component 0 = (1.0 * 5.0) + (4.0 * 2.0) = 13.
# vector component 1 = (2.0 * 5.0) + (5.0 * 2.0) = 20.
# vector component 2 = (3.0 * 5.0) + (6.0 * 2.0) = 27.

# Print the results
print("Total weighted sum:","\n", tot_sum_field_scale, "\n")


# In[12]:


# Total scaled sum of the two field collections (accumulate)
tot_sum_fc_scale = maths.accumulate_fc(fields_container=fc1, weights=scale_vect).eval()
# {time: 1}: field1
#           -->      vector component 0 = (1.0 * 5.0) + (4.0 * 2.0) = 13.
#                    vector component 1 = (2.0 * 5.0) + (5.0 * 2.0) = 20.
#                    vector component 2 = (3.0 * 5.0) + (6.0 * 2.0) = 27.
#
# {time: 2}: field2
#           -->      vector component 0 = (7.0 * 5.0) + (8.0 * 2.0) = 51.
#                    vector component 1 = (3.0 * 5.0) + (1.0 * 2.0) = 17.
#                    vector component 2 = (5.0 * 5.0) + (2.0 * 2.0) = 29.

# Print the results
print("Total sum FieldsContainers scale","\n", tot_sum_fc_scale , "\n")
print(tot_sum_fc_scale.get_field({"time":1}), "\n")
print(tot_sum_fc_scale.get_field({"time":2}), "\n")


# In[13]:


# Subtraction of two 3D vector fields
minus_field = maths.minus(fieldA=field1, fieldB=field2).eval()
# id 0: [1.-7. 2.-3. 3.-5.] = [-6. -1. -2.]
# id 1: [4.-8. 5.-1. 6.-2.] = [-4. 4. 4.]

# Print the results
print("Subtraction field","\n", minus_field , "\n")


# In[14]:


# Subtraction of two field collections
minus_fc = maths.minus_fc(
    field_or_fields_container_A=fc1,
    field_or_fields_container_B=fc2
).eval()
# {time: 1}: field1 - field3
#           -->      id 0: [1.-6. 2.-5. 3.-4.] = [-5. -3. -1.]
#                    id 1: [4.-3. 5.-2. 6.-1.] = [1. 3. 5.]
#
# {time: 2}: field2 - field4
#           -->      id 0: [7.-4. 3.-1. 5.-8.] = [3. 2. -3.]
#                    id 1: [8.-5. 1.-7. 2.-9.] = [3. -6. -7.]

# Print the results
print("Subtraction field collection","\n", minus_fc , "\n")
print(minus_fc.get_field({"time":1}), "\n")
print(minus_fc.get_field({"time":2}), "\n")


# In[15]:


# Compute the Hadamard product of two fields
element_prod_field = maths.component_wise_product(fieldA=field1, fieldB=field2).eval()
# id 0: [1.*7. 2.*3. 3.*5.] = [7. 6. 15.]
# id 1: [4.*8. 5.*1. 6.*2.] = [32. 5. 12.]

# Print the results
print("Element-wise product field","\n", element_prod_field , "\n")


# In[16]:


# Cross product of each field in a collection and a single unique field
element_prod_fc = maths.component_wise_product_fc(fields_container=fc1, fieldB=field3).eval()
# {time: 1}: field1 and field3
#           -->      id 0: [1.*6. 2.*5. 3.*4.] = [6. 10. 12.]
#                    id 1: [4.*3. 5.*2. 6.*1.] = [12. 10. 6.]
#
# {time: 2}: field2 and field3
#           -->      id 0: [7.*6. 3.*5. 5.*4.] = [42. 15. 20.]
#                    id 1: [8.*3. 1.*2. 2.*1.] = [24. 2. 2.]

# Print the results
print("Element product FieldsContainer","\n", element_prod_fc , "\n")
print(element_prod_fc.get_field({"time":1}), "\n")
print(element_prod_fc.get_field({"time":2}), "\n")


# In[17]:


# Compute the cross product
cross_prod_field = maths.cross_product(fieldA=field1, fieldB=field2).eval()
# id 0: [(2.*5. - 3.*3.)  (3.*7. - 1.*5.)  (1.*3. - 2.*7.)] = [1. 16. -11.]
# id 1: [(5.*2. - 6.*1.)  (6.*8. - 4.*2.)  (4.*1. - 5.*8.)] = [4. 40. -36.]

# Print the results
print("Cross product field","\n", cross_prod_field , "\n")


# In[18]:


# Cross product of two field collections
cross_prod_fc = maths.cross_product_fc(field_or_fields_container_A=fc1,field_or_fields_container_B=fc2).eval()
# {time: 1}: field1 X field3
#           -->      id 0: [(2.*4. - 3.*5.)  (3.*6. - 1.*4.)  (1.*5. - 2.*6.)] = [-7. 14. -7.]
#                    id 1: [(5.*1. - 6.*2.)  (6.*3. - 4.*1.)  (4.*2. - 5.*3.)] = [-7. 14. -7.]
#
# {time: 2}: field2 X field4
#           -->      id 0: [(3.*8. - 5.*1.)  (5.*4. - 7.*8.)  (7.*1. - 3.*4.)] = [19. -36. -5]
#                    id 1: [(1.*9. - 2.*7.)  (2.*5. - 8.*9.)  (8.*7. - 1.*5.)] = [-5. -62. 51.]

# Print the results
print("Cross product FieldsContainer","\n", cross_prod_fc , "\n")
print(cross_prod_fc.get_field({"time":1}), "\n")
print(cross_prod_fc.get_field({"time":2}), "\n")


# In[19]:


# Generalized inner product of two fields
dot_prod_field = maths.generalized_inner_product(fieldA=field1, fieldB=field2).eval()
# id 0: (1. * 7.) + (2. * 3.) + (3. * 5.) = 28.
# id 1: (4. * 8.) + (5. * 1.) + (6. * 2.) = 49.

# Print the results
print("Dot product field","\n", dot_prod_field , "\n")


# In[20]:


# Generalized inner product of two field collections
dot_prod_fc = maths.generalized_inner_product_fc(field_or_fields_container_A=fc1, field_or_fields_container_B=fc2).eval()
# {time: 1}: field1 X field3
#           -->      id 0: (1. * 6.) + (2. * 5.) + (3. * 4.) = 28.
#                    id 1: (4. * 3.) + (5. * 2.) + (6. * 1.) = 28.
#
# {time: 2}: field2 X field4
#           -->      id 0: (7. * 4.) + (3. * 1.) + (5. * 8.) = 71.
#                    id 1: (8. * 5.) + (1. * 7.) + (2. * 9.) = 65.

# Print the results
print("Dot product FieldsContainer","\n", dot_prod_fc , "\n")
print(dot_prod_fc.get_field({"time":1}), "\n")
print(dot_prod_fc.get_field({"time":2}), "\n")


# In[21]:


# Overall dot product of two fields
overall_dot = maths.overall_dot(fieldA=field1, fieldB=field2).eval()
# id 1: (1. * 7.) + (2. * 3.) + (3. * 5.) + (4. * 8.) + (5. * 1.) + (6. * 2.) = 77.

# Print the results
print("Overall dot","\n", overall_dot , "\n")


# In[22]:


# Divide a field by another field
comp_wise_div = maths.component_wise_divide(fieldA=field1, fieldB=field2).eval()
# id 0: [1./7. 2./3. 3./5.] = [0.143 0.667 0.6]
# id 1: [4./8. 5./1. 6./2.] = [0.5 5. 3.]

# Print the results
print("Component-wise division field","\n", comp_wise_div , "\n")


# In[23]:


# Component-wise division between two field collections
comp_wise_div_fc = maths.component_wise_divide_fc(fields_containerA=fc1, fields_containerB=fc2).eval()
# {time: 1}: field1 - field3
#           -->      id 0: [1./6. 2./5. 3./4.] = [0.167 0.4 0.75]
#                    id 1: [4./3. 5./2. 6./1.] = [1.333 2.5 6.]
#
# {time: 2}: field2 - field4
#           -->      id 0: [7./4. 3./1. 5./8.] = [1.75 3. 0.625]
#                    id 1: [8./5. 1./7. 2./9.] = [1.6 0.143 0.222]

# Print the results
print("Component-wise division FieldsContainer","\n", comp_wise_div_fc , "\n")
print(comp_wise_div_fc.get_field({"time":1}), "\n")
print(comp_wise_div_fc.get_field({"time":2}), "\n")


# In[24]:


# Define the power factor
pow_factor = 3.0
# Compute the power of three of a field
pow_field = maths.pow(field=field1, factor=pow_factor).eval()
# id 0: [(1.^3.) (2.^3.) (3.^3.)] = [1. 8. 27.]
# id 1: [(4.^3.) (5.^3.) (6.^3.)] = [64. 125. 216.]

# Print the results
print("Power field","\n", pow_field , "\n")


# In[25]:


# Compute the power of three of a field collection
pow_fc = maths.pow_fc(fields_container=fc1, factor=pow_factor).eval()
# {time: 1}: field1
#           -->      id 0: [(1.^3.) (2.^3.) (3.^3.)] = [1. 8. 27.]
#                    id 1: [(4.^3.) (5.^3.) (6.^3.)] = [64. 125. 216.]
#
# {time: 2}: field2
#           -->      id 0: [(7.^3.) (3.^3.) (5.^3.)] = [343. 27. 125.]
#                    id 1: [(8.^3.) (1.^3.) (2.^3.)] = [512. 1. 8.]

# Print the results
print("Power FieldsContainer","\n", pow_fc , "\n")
print(pow_fc.get_field({"time":1}), "\n")
print(pow_fc.get_field({"time":2}), "\n")


# In[26]:


# Compute the power of two of a field
sqr_field = maths.sqr(field=field1).eval()
# id 0: [(1.^2.) (2.^2.) (3.^2.)] = [1. 4. 9.]
# id 1: [(4.^2.) (5.^2.) (6.^2.)] = [16. 25. 36.]

print("^2 field","\n", sqr_field , "\n")


# In[27]:


# Compute the power of two of a field collection
sqr_fc = maths.sqr_fc(fields_container=fc1).eval()
# {time: 1}: field1
#           -->      id 0: [(1.^2.) (2.^2.) (3.^2.)] = [1. 4. 9.]
#                    id 1: [(4.^2.) (5.^2.) (6.^2.)] = [16. 25. 36.]
#
# {time: 2}: field2
#           -->      id 0: [(7.^2.) (3.^2.) (5.^2.)] = [49. 9. 25.]
#                    id 1: [(8.^2.) (1.^2.) (2.^2.)] = [64. 1. 4.]

# Print the results
print("^2 FieldsContainer","\n", sqr_fc , "\n")
print(sqr_fc.get_field({"time":1}), "\n")
print(sqr_fc.get_field({"time":2}), "\n")


# In[28]:


# Compute the square-root of a field
sqrt_field = maths.sqrt(field=field1).eval()
# id 0: [(1.^0.5) (2.^0.5) (3.^0.5)] = [1. 1.414 1.732]
# id 1: [(4.^0.5) (5.^0.5) (6.^0.5)] = [2. 2.236 2.449]

print("^0.5 field","\n", sqrt_field , "\n")


# In[29]:


# Compute the square-root of a field collection
sqrt_fc = maths.sqrt_fc(fields_container=fc1).eval()
# {time: 1}: field1
#           -->      id 0: [(1.^.5) (2.^.5) (3.^.5)] = [1. 1.414 1.732]
#                    id 1: [(4.^.5) (5.^.5) (6.^.5)] = [2. 2.236 2.449]
#
# {time: 2}: field2
#           -->      id 0: [(7.^.5) (3.^.5) (5.^.5)] = [2.645 1.732 2.236]
#                    id 1: [(8.^.5) (1.^.5) (2.^.5)] = [2.828 1. 1.414]

# Print the results
print("Sqrt FieldsContainer","\n", sqrt_fc , "\n")
print(sqrt_fc.get_field({"time":1}), "\n")
print(sqrt_fc.get_field({"time":2}), "\n")


# In[30]:


# Compute the L2 norm of a field
norm_field = maths.norm(field=field1, scalar_int=2).eval()
# id 0: [(1.^2.) + (2.^2.) + (3.^2.)] ^1/2 = 3.742
# id 1: [(4.^2.) + (5.^2.) + (6.^2.)] ^1/2 = 8.775

# Print the results
print("Norm field","\n", norm_field , "\n")


# In[31]:


# Define the L2 norm of a field collection
norm_fc = maths.norm_fc(fields_container=fc1).eval()
# {time: 1}: field1
#           -->      id 0: [(1.^2.) + (2.^2.) + (3.^2.)] ^1/2 = 3.742
#                    id 1: [(4.^2.) + (5.^2.) + (6.^2.)] ^1/2 = 8.775
#
# {time: 2}: field2
#           -->      id 0: [(7.^2.) + (3.^2.) + (5.^2.)] ^1/2 = 9.110
#                    id 1: [(8.^2.) + (1.^2.) + (2.^2.)] ^1/2 = 8.307

# Print the results
print("Norm FieldsContainer","\n", norm_fc , "\n")
print(norm_fc.get_field({"time":1}), "\n")
print(norm_fc.get_field({"time":2}), "\n")

