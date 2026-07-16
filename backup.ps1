$destino="backup"

New-Item -ItemType Directory -Force $destino | Out-Null

$data=Get-Date -Format "yyyyMMdd_HHmmss"

Compress-Archive `
-Path src,templates,main.py,requirements.txt `
-DestinationPath "$destino\backup_$data.zip"

Write-Host ""

Write-Host "Backup criado."

Pause