set SPHINX_APIDOC_OPTIONS=inherited-members
call sphinx-apidoc -o ../docs/source/api ../ansys ../ansys/dpf/core/log.py ^
../ansys/dpf/core/help.py ../ansys/dpf/core/mapping_types.py ../ansys/dpf/core/ipconfig.py ^
../ansys/dpf/core/field_base.py ../ansys/dpf/core/cache.py ../ansys/dpf/core/misc.py ^
../ansys/dpf/core/check_version.py ../ansys/dpf/core/operators/build.py ../ansys/dpf/core/operators/specification.py ^
../ansys/dpf/core/vtk_helper.py ../ansys/dpf/core/label_space.py ../ansys/dpf/core/examples/python_plugins/* ^
../ansys/dpf/core/examples/examples.py ^
 -f --implicit-namespaces --separate  --no-headings
pushd .
cd ../docs/
call make clean
call make html -v -v -v
popd
