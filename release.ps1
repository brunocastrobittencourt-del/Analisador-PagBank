Clear-Host

git add .

$mensagem = Read-Host "Mensagem do commit"

git commit -m $mensagem

git push

Write-Host ""

Write-Host "Release enviada."

Pause