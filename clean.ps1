Write-Host ""
Write-Host "Limpando cache..."

Get-ChildItem -Recurse -Directory -Filter "__pycache__" |
Remove-Item -Recurse -Force -ErrorAction SilentlyContinue

Get-ChildItem -Recurse *.pyc |
Remove-Item -Force -ErrorAction SilentlyContinue

Write-Host ""

Write-Host "Arquivos temporários removidos."

Write-Host ""

Pause