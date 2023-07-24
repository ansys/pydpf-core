set SPHINX_APIDOC_OPTIONS=inherited-members
call sphinx-apidoc -o ../docs/source/api ../src/ansys ../src/ansys/dpf/core/log.py ^
../src/ansys/dpf/core/help.py ../src/ansys/dpf/core/mapping_types.py ../src/ansys/dpf/core/ipconfig.py ^
../src/ansys/dpf/core/field_base.py ../src/ansys/dpf/core/cache.py ../src/ansys/dpf/core/misc.py ^
../src/ansys/dpf/core/check_version.py ../src/ansys/dpf/core/operators/build.py ../src/ansys/dpf/core/operators/specification.py ^
../src/ansys/dpf/core/vtk_helper.py ../src/ansys/dpf/core/label_space.py ../src/ansys/dpf/core/examples/python_plugins/* ^
../src/ansys/dpf/core/examples/examples.py ../src/ansys/dpf/core/property_fields_container.py ^
 -f --implicit-namespaces --separate  --no-headings
pushd .
cd ../docs/
call make clean
call make html -v -v -v -P

dir

rem Patch pyVista issue with elemental plots

xcopy /y source/examples/04-advanced/02-volume_averaged_stress/sphx_glr_02-volume_averaged_stress_001.png   build/html/_images/sphx_glr_02-volume_averaged_stress_001.png
xcopy /y source/examples/12-fluids/02-fluids_results/sphx_glr_02-fluids_results_001.png                     build/html/_images/sphx_glr_02-fluids_results_001.png
xcopy /y source/examples/12-fluids/02-fluids_results/sphx_glr_02-fluids_results_002.png                     build/html/_images/sphx_glr_02-fluids_results_002.png
xcopy /y source/examples/12-fluids/02-fluids_results/sphx_glr_02-fluids_results_003.png                     build/html/_images/sphx_glr_02-fluids_results_003.png
xcopy /y source/examples/12-fluids/02-fluids_results/sphx_glr_02-fluids_results_004.png                     build/html/_images/sphx_glr_02-fluids_results_004.png
xcopy /y source/examples/12-fluids/02-fluids_results/sphx_glr_02-fluids_results_005.png                     build/html/_images/sphx_glr_02-fluids_results_005.png
xcopy /y source/examples/12-fluids/02-fluids_results/sphx_glr_02-fluids_results_006.png                     build/html/_images/sphx_glr_02-fluids_results_006.png
xcopy /y source/examples/12-fluids/02-fluids_results/sphx_glr_02-fluids_results_007.png                     build/html/_images/sphx_glr_02-fluids_results_007.png
xcopy /y source/examples/12-fluids/02-fluids_results/sphx_glr_02-fluids_results_00_thumb.png                build/html/_images/sphx_glr_02-fluids_results_00_thumb.png
