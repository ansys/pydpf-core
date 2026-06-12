param ($awp_root=$env:AWP_ROOT222, $pip_args)
Write-Host "Running script with args: "
Write-Host "-awp_root" $awp_root
Write-Host "-pip_args" $pip_args
$python=($awp_root + "\commonfiles\CPython\3_7\winx64\Release\python\python.exe")

if ($pip_args -eq $null){
    Start-Process $python -ArgumentList ("-m pip install ansys-dpf-core")
}
else {
    Start-Process $python -ArgumentList ("-m pip install ansys-dpf-core " + $pip_args)
}