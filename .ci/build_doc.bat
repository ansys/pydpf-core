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

REM Return to the original directory
popd
