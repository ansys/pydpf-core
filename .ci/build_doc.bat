@echo off

REM Move to the documentation directory
pushd .
cd ../doc/

REM Clean the previous build
call make clean

REM Build the HTML documentation
call make html -v -v -v -P

REM Display the directory contents for verification
dir

REM Patch pyVista issue with elemental plots by copying necessary images
xcopy source\examples\04-advanced\02-volume_averaged_stress\sphx_glr_02-volume_averaged_stress_001.png build\html\_images\ /y /f
xcopy source\examples\12-fluids\02-fluids_results\sphx_glr_02-fluids_results_001.png build\html\_images\ /y /f
xcopy source\examples\12-fluids\02-fluids_results\sphx_glr_02-fluids_results_002.png build\html\_images\ /y /f
xcopy source\examples\12-fluids\02-fluids_results\sphx_glr_02-fluids_results_003.png build\html\_images\ /y /f
xcopy source\examples\12-fluids\02-fluids_results\sphx_glr_02-fluids_results_004.png build\html\_images\ /y /f
xcopy source\examples\12-fluids\02-fluids_results\sphx_glr_02-fluids_results_005.png build\html\_images\ /y /f
xcopy source\examples\12-fluids\02-fluids_results\sphx_glr_02-fluids_results_006.png build\html\_images\ /y /f
xcopy source\examples\12-fluids\02-fluids_results\sphx_glr_02-fluids_results_007.png build\html\_images\ /y /f
xcopy source\examples\12-fluids\02-fluids_results\sphx_glr_02-fluids_results_thumb.png build\html\_images\ /y /f

REM Return to the original directory
popd
