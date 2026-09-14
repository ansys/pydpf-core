param ($pluginpath, $zippath, $pythonexe='python', $tempfolder=$env:TEMP)
Write-Host "Running script with args: "
Write-Host "-pluginpath" $pluginpath
Write-Host "-zippath" $zippath
Write-Host "-pythonexe" $pythonexe
Write-Host "-tempfolder" $tempfolder


Write-Host "make venv"
Start-Process $pythonexe -ArgumentList ("-m venv "+ $tempfolder+"\venv") -NoNewWindow -Wait


Write-Host "activate venv"
& ($tempfolder+"\venv\Scripts\Activate.ps1")


Write-Host "install deps"
Start-Process "python" -ArgumentList ("-m pip install -r "+$pluginpath+"\requirements.txt --disable-pip-version-check --use-pep517") -NoNewWindow -Wait
if (Test-Path ($tempfolder + "/venv/Lib/site-packages/__pycache__")){
    Write-Host "remove __pycache__"
    Remove-Item -Recurse -Force ($tempfolder + "/venv/Lib/site-packages/__pycache__")
}
$dirName=[System.IO.Path]::GetDirectoryName($zippath)
echo $dirName
if (-Not (Test-Path $dirName)){
    New-Item $dirName -Type directory
}
Compress-Archive ($tempfolder+"/venv/Lib/site-packages/*") -DestinationPath $zippath -Force

deactivate
Remove-Item -Recurse -Force ($tempfolder + "/venv")