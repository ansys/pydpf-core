set SPHINX_APIDOC_OPTIONS=inherited-members
call sphinx-apidoc -o ../docs/source/api ../src/ansys ../src/ansys/dpf/core/log.py ^
../src/ansys/dpf/core/help.py ../src/ansys/dpf/core/mapping_types.py ../src/ansys/dpf/core/ipconfig.py ^
../src/ansys/dpf/core/field_base.py ../src/ansys/dpf/core/cache.py ../src/ansys/dpf/core/misc.py ^
../src/ansys/dpf/core/check_version.py ../src/ansys/dpf/core/operators/build.py ../src/ansys/dpf/core/operators/specification.py ^
../src/ansys/dpf/core/vtk_helper.py ../src/ansys/dpf/core/label_space.py ../src/ansys/dpf/core/examples/python_plugins/* ^
../src/ansys/dpf/core/examples/examples.py ../src/ansys/dpf/gate/* ../src/ansys/dpf/gatebin/* ../src/ansys/grpc/dpf/* ^
 ../src/ansys/dpf/core/property_fields_container.py ^
 -f --implicit-namespaces --separate  --no-headings
pushd .
cd ../docs/
call make clean
call make html -v -v -v -P
popd
