# # ~~~~~~~ DATA APIs: DataSources ~~~~~~~ # #

# If you want to understand more about the DPF components organisation check the previous
# example "0.0-basic_DPF_implementation"

# DPF provides three main types of operators:
# - Operators for importing or reading data
# - Operators for transforming data
# - Operators for exporting data
#
# Those operators are defined in the subpackages and submodules of DPF.

# When post-processing a simulation with DPF the typical basic steps are:
# 1- Load the result File
# 2- Access the data
# 3- Transform the data
# 4- Display the new results
# 5- Export the new results


# The DataSources operator is a class available as a submodule of the 'ansys.dpf.core' package. It contains files
# with the analysis results. So this object is used in the first basic step: load the result File by defining
# where it is located.

# This example will describe the functionalities and functions of the class DataSources and can be generalised for all
# the files formats accepted by Py-DPF:

#   - MAPDL files: .rst, .mode, .rfrq, .rdsp
#   - LS-DYNA files: .d3plot, .binout
#   - Fluent files: CFF restart files(.cas/dat.h5) and Project files (.flprj)
#   - CFX files: CFF files(.cas/dat.cff.res) and Project files (.flprj)

##################################################################################################################

# # ~~~~~~~ 1) DataSources creation ~~~~~~~ # #

# 1.a) class 'DataSources()'
# If you are sure that your file has exactly the extensions keys listed above, the DataSources object can be created
# by directly calling the class with the file path as an argument :

from ansys.dpf import core as dpf
my_data_sources_a = dpf.DataSources(result_path=r'file.extension')

#   It is preferable to generate a raw string (by putting the letter 'r' before the file path string) in order to ensure
#   the file path will be correctly read

# 1.b) function 'set_result_file_path()'
# If the extension key is not written as listen above (For example: a file.binout can sometimes
# be named as 'file.binout0000') but you know what the extension key is, the DataSources object can be created by:
from ansys.dpf import core as dpf
my_data_sources_b = dpf.DataSources()
my_data_sources_b.set_result_file_path(filepath=r'file.extension1234', key='extension')

# 1.c) function 'guess_result_key()'
# - If the extension key is not written as listen above (For example: a file.binout can sometimes
# # be named as 'file.binout0000') but you don't know what the extension key is, the DataSources object can
# be created by:
from ansys.dpf import core as dpf
my_data_sources_c = dpf.DataSources()
my_file_key = my_data_sources_c.guess_file_key(filepath=r'file.extension1234')
my_data_sources_c.set_result_file_path(filepath=r'file.extension1234', key=my_file_key)

# 1.d) function 'add_file_path()'
# - If the results are not entirely in the same file you need to use this function. For example the '.d3plot' files does
# not contain information related to Units, however, if the simulation was run through Mechanical, a file.actunits file
# is produced and need to be added.
from ansys.dpf import core as dpf
my_data_sources_d = dpf.DataSources()
my_data_sources_d.set_result_file_path(filepath=r'file.extension', key='extension')
my_data_sources_d.add_file_path(filepath=r'file2.extension')

# 1.e) function 'guess_second_key()'
# - If the results file have more than one extension you need to use this function. The creation o the DataSources is
# the same as in the 1.b topic. However, we have a particular case for the Fluent and CFX results files that often have
# the model and the data in different files ('file.cas.h5' and 'file.dat.h5' respectively). In this case, besides using
# the 'guess_second_key_' function, you will need to use the 'add.file_path' function
from ansys.dpf import core as dpf
my_data_sources_e = dpf.DataSources()
my_file_key1 = my_data_sources_e.guess_file_key(filepath=r'file1.extension1.extension2')
my_file_key2 = my_data_sources_e.guess_file_key(filepath=r'file2.extension3.extension4')
my_data_sources_e.set_result_file_path(filepath=r'file1.extension1.extension2', key=my_file_key1)
my_data_sources_e.add_file_path(filepath=r'file2.extension3.extension4', key=my_file_key2)

# 1.f) function 'add_upstream()'
# - If you believe needing a recursive workflow you need to create a new object 'DataSouces' with the involved data
# and then add it as an upstream in the main 'DataSources' object. Upstream refers to data sources that provide data
# to a particular process. For example the expansion of the analysis results data is recursive in DPF.
from ansys.dpf import core as dpf
my_data_sources_f = dpf.DataSources()
my_data_sources_f.set_result_file_path(filepath=r'file0.extension0', key='extension0')

my_data_sources_upstream_f = dpf.DataSources()
my_data_sources_upstream_f.set_result_file_path(filepath=r'file1.extension1', key='extension1')

my_data_sources_f.add_upstream(upstream_data_sources=my_data_sources_upstream_f)

# 1.g) function 'set_domain_result_file_path()' and 'add_domain_file_path()'
# - If you need to post-process an analysis results that are distributed in two files, you can merge them directly at
# the DataSources indentation.
from ansys.dpf import core as dpf
my_data_sources_g = dpf.DataSources()
my_data_sources_g.set_domain_result_file_path(path=r"file0.extension", key='extension', domain_id=0)
my_data_sources_g.add_domain_file_path(filepath=r"file1.extension", key='extension', domain_id=1)

# - If you need to post-process an analysis results from/into different servers, you can also work in different
# remotes processe. This application is explained in details in the "Examples for postprocessing on distributed
# processes" section in the examples documentation webpage

# 1.h) function 'add_upstream_for_domain()'
# - If you believe needing a recursive workflow, and you have more then one results file, you need to create a new
# object 'DataSouces' with the involved data and then add it as an upstream in the correspondent main 'DataSources'
# object.
from ansys.dpf import core as dpf
my_data_sources_h = dpf.DataSources()
my_data_sources_h.set_domain_result_file_path(path=r"file0.extension", key='extension', domain_id=0)
my_data_sources_h.add_domain_file_path(filepath=r"file1.extension1", key='extension1', domain_id=1)

my_data_sources_upstream_g = dpf.DataSources()
my_data_sources_upstream_g.set_result_file_path(filepath=r'file2.extension2', key='extension2')

my_data_sources_g.add_upstream_for_domain(upstream_data_sources=my_data_sources_upstream_g, domain_id=1)

# 1.i) function 'add_file_path_for_specified_result()'

# 1.j) register_namespace()

##################################################################################################################

# # ~~~~~~~ 2) DataSources exploring ~~~~~~~ # #

# You can check some properties that your DataSources object have. They are:

# 2.k) result_key
# You can verify which file extension was used by your DataSources.
# - This extension correspond to the file that you set, either with the 'set_result_file_path()' function, either if you
# called the class with the file path as an argument
# - If the file that you set had more then one extension, only the first one will be returned

from ansys.dpf import core as dpf
my_data_sources_k = dpf.DataSources()
my_data_sources_k.set_result_file_path(filepath=r'file.extension', key='extension')

print(my_data_sources_k.result_key)
# 'extension'

# 2.l) result_files
# You can verify the list o List of result files contained in the data sources. It returns the file path of those files
# - If you use the 'set_result_file_path' function it will return only the file path given as an argument to this
# function
from ansys.dpf import core as dpf
my_data_sources_l1 = dpf.DataSources()
my_data_sources_l1.set_result_file_path(filepath=r'file.extension', key='extension')
my_data_sources_l1.add_file_path(filepath=r'file2.extension')

print(my_data_sources_l1.result_files)
# ['/folder/file.extension]

# - If you added an upstream result file, it will not be listed in the main DataSources object. You have to check
# directly in the DataSources object created to define the upstream data
from ansys.dpf import core as dpf
my_data_sources_l2 = dpf.DataSources(result_path=r'file0.extension0')

my_data_sources_upstream_l2 = dpf.DataSources(filepath=r'file1.extension1')
my_data_sources_upstream_l2.add_file_path(filepath=r'file2.extension2')

my_data_sources_l2.add_upstream(upstream_data_sources=my_data_sources_upstream_l2)

print(my_data_sources_l2.result_files)
# ['/folder/file0.extension0]

# - If your checking the DataSources object created to define the upstream data and the files do not have the same
# extension, only the first one will be listed
print(my_data_sources_upstream_l2.result_files)
# ['/folder/file1.extension1]

# - If you have a DataSources object with more then one domain, a empty list will be returned
from ansys.dpf import core as dpf
my_data_sources_l3 = dpf.DataSources()
my_data_sources_l3.set_domain_result_file_path(path=r"file0.extension", key='extension', domain_id=0)
my_data_sources_l3.add_domain_file_path(filepath=r"file1.extension", key='extension', domain_id=1)

print(my_data_sources_l3.result_files)
# [None,None]

