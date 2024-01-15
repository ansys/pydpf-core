@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=sphinx-build
)
set SOURCEDIR=source
set BUILDDIR=build

if "%1" == "" goto help
if "%1" == "clean" goto clean

%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
	echo.installed, then set the SPHINXBUILD environment variable to point
	echo.to the full path of the 'sphinx-build' executable. Alternatively you
	echo.may add the Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.http://sphinx-doc.org/
	exit /b 1
)

%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
goto end

:clean
echo.Cleaning files form previous build...
IF EXIST "build" (
    rmdir "build" /s /q
)
IF EXIST "source\images\auto-generated" (
    rmdir "source\images\auto-generated" /s /q
)
IF EXIST "source\examples\07-python-operators\plugins" (
    robocopy "source\examples\07-python-operators\plugins" "source\_temp\plugins" /E >nul 2>&1
)
IF EXIST "source\examples\04-advanced\02-volume_averaged_stress" (
    robocopy "source\examples\04-advanced\02-volume_averaged_stress" "source\_temp\04_advanced" /E >nul 2>&1
)
IF EXIST "source\examples\12-fluids\02-fluids_results" (
    robocopy "source\examples\12-fluids\02-fluids_results" "source\_temp\12_fluids" /E >nul 2>&1
)
IF EXIST "source\examples" (
    rmdir "source\examples" /s /q
)
IF EXIST "source\_temp\plugins" (
    robocopy "source\_temp\plugins" "source\examples\07-python-operators\plugins" /E >nul 2>&1
)
IF EXIST "source\_temp\04_advanced" (
    robocopy "source\_temp\04_advanced" "source\examples\04-advanced\02-volume_averaged_stress" /E >nul 2>&1
)
IF EXIST "source\_temp\12_fluids" (
    robocopy "source\_temp\12_fluids" "source\examples\12-fluids\02-fluids_results" /E >nul 2>&1
)
IF EXIST "source\_temp" (
    rmdir "source\_temp" /s /q
)

echo.Done.
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

:end
popd
