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
Start-Process "python" -ArgumentList ("-m pip install -r "+$pluginpath+"\requirements.txt --disable-pip-version-check") -NoNewWindow -Wait
if (Test-Path ($tempfolder + "/venv/Lib/site-packages/__pycache__")){
    Write-Host "remove __pycache__"
    Remove-Item -Recurse -Force ($tempfolder + "/venv/Lib/site-packages/__pycache__")
}
Write-Host "Get zip directory"
$dirName=[System.IO.Path]::GetDirectoryName($zippath)
echo $dirName
if (-Not (Test-Path $dirName)){
    Write-Host "Creating the directory"
    New-Item $dirName -Type directory
}
Write-Host "Compressing the site-packages"
Compress-Archive ($tempfolder+"/venv/Lib/site-packages/*") -DestinationPath $zippath -Force

Write-Host "Deactivating the venv"
& ($tempfolder+"\venv\Scripts\deactivate.bat")
Write-Host "Removing the venv"
Remove-Item -Recurse -Force ($tempfolder + "/venv")
