Write-Host ""

Write-Host "Arquivos Python"

(Get-ChildItem -Recurse *.py).Count

Write-Host ""

Write-Host "Linhas"

(Get-ChildItem -Recurse *.py |
Get-Content |
Measure-Object -Line).Lines

Write-Host ""

Write-Host "PDFs"

(Get-ChildItem arquivos *.pdf).Count

Write-Host ""

Pause