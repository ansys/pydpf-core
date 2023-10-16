param ($pluginpath, $zippath, $pythonexe='python', $tempfolder=$env:TEMP)
Write-Host "Running script with args: "
Write-Host "-pluginpath" $pluginpath
Write-Host "-zippath" $zippath
Write-Host "-pythonexe" $pythonexe
Write-Host "-tempfolder" $tempfolder

# Expand shortcut in path
$tempfolder = Resolve-Path -Path $tempfolder
$tempfolder = $tempfolder.ToString()

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
Write-Host "Create directory"
echo $dirName
if (-Not (Test-Path $dirName)){
    New-Item $dirName -Type directory
}
Write-Host "Compress archive"
Compress-Archive ($tempfolder+"/venv/Lib/site-packages/*") -DestinationPath $zippath -Force

Write-Host "Deactivate venv"
deactivate
Write-Host "Remove venv"
Remove-Item -Recurse -Force ($tempfolder + "/venv")
Write-Host "Done creating site-packages for gltf plugin"