Write-Host ""
Write-Host "============================================="
Write-Host " ANALISADOR FINANCEIRO - SETUP"
Write-Host "============================================="
Write-Host ""

Write-Host "Limpando cache do Python..."

Get-ChildItem -Recurse -Directory -Filter "__pycache__" -ErrorAction SilentlyContinue |
Remove-Item -Recurse -Force

Get-ChildItem -Recurse -Filter "*.pyc" -ErrorAction SilentlyContinue |
Remove-Item -Force

Write-Host "OK"

Write-Host ""

Write-Host "Verificando estrutura..."

$pastas = @(
"arquivos",
"logs",
"resultados",
"templates",
"tests",
"src",
"src\models",
"src\services",
"src\parsers",
"src\core",
"src\constants",
"src\exceptions",
"src\regras"
)

foreach($p in $pastas){

    if(Test-Path $p){

        Write-Host "[OK] $p"

    }
    else{

        Write-Host "[ERRO] Pasta ausente: $p"

    }

}

Write-Host ""

Write-Host "Verificando Python..."

python --version

Write-Host ""

Write-Host "Verificando dependências..."

pip show pdfplumber
pip show openpyxl

Write-Host ""

Write-Host "============================================="
Write-Host "SETUP FINALIZADO"
Write-Host "============================================="