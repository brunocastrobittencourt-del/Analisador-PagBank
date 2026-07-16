Clear-Host

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
chcp 65001 | Out-Null

$ErrorActionPreference = "Stop"

$Projeto = "AnalisePagBank"

$Versao = "2.0.0"

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "           ANALISADOR FINANCEIRO" -ForegroundColor Yellow
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Projeto : $Projeto"
Write-Host "Versão  : $Versao"
Write-Host "Data    : $(Get-Date)"
Write-Host ""
function Criar-Pasta {

    param($Pasta)

    if(!(Test-Path $Pasta)){

        New-Item `
            -ItemType Directory `
            -Path $Pasta `
            | Out-Null

        Write-Host "[OK] Pasta criada -> $Pasta" -ForegroundColor Green

    }
    else{

        Write-Host "[EXISTE] $Pasta" -ForegroundColor DarkGray

    }

}


function Criar-Arquivo {

    param($Arquivo)

    if(!(Test-Path $Arquivo)){

        New-Item `
            -ItemType File `
            -Path $Arquivo `
            | Out-Null

        Write-Host "[OK] Arquivo criado -> $Arquivo" -ForegroundColor Green

    }
    else{

        Write-Host "[EXISTE] $Arquivo" -ForegroundColor DarkGray

    }

}
$Pastas = @(

"arquivos",

"benchmark",

"docs",

"examples",

"logs",

"resultados",

"templates",

"tests",

"src",

"src\bancos",

"src\carteiras",

"src\classificadores",

"src\config",

"src\constants",

"src\core",

"src\excel",

"src\exceptions",

"src\exportadores",

"src\filtros",

"src\financeiro",

"src\models",

"src\normalizadores",

"src\parsers",

"src\plataformas",

"src\regras",

"src\services",

"src\utils",

"src\validadores",

"src\analisadores"

)

foreach($Pasta in $Pastas){

    Criar-Pasta $Pasta

}
Get-ChildItem src -Directory |
Where-Object { $_.Name -ne "__pycache__" } |
ForEach-Object{

}
$Arquivos = @(

".gitignore",

"README.md",

"CHANGELOG.md",

"LICENSE",

"requirements.txt",

".env",

".env.example",

"main.py"

)

foreach($Arquivo in $Arquivos){

    Criar-Arquivo $Arquivo

}

$Modulos = @{

"src\bancos"=@(
"bancodobrasil",
"banrisul",
"bradesco",
"c6",
"caixa",
"inter",
"itau",
"neon",
"nubank",
"santander",
"sicredi"
)

"src\carteiras"=@(
"mercadopago",
"pagbank",
"picpay"
)

"src\plataformas"=@(
"ifood",
"uber"
)

"src\exportadores"=@(
"excel_exportador",
"pdf_exportador",
"csv_exportador",
"json_exportador"
)

"src\analisadores"=@(
"renda_analisador",
"capacidade_analisador",
"score_analisador",
"fgts_analisador",
"mcmv_analisador",
"subsidio_analisador",
"parecer_analisador"
)

"src\classificadores"=@(
"aposta_classificador",
"emprestimo_classificador",
"familiar_classificador",
"fintech_classificador",
"investimento_classificador",
"marketplace_classificador",
"pix_classificador",
"receita_classificador",
"transferencia_classificador"
)

}

foreach($Pasta in $Modulos.Keys){

    foreach($Arquivo in $Modulos[$Pasta]){

        Criar-Arquivo "$Pasta\$Arquivo.py"

    }

}

$Bancos=@(

"pagbank",

"nubank",

"caixa",

"itau",

"bradesco",

"santander",

"banco_do_brasil",

"inter",

"sicredi",

"banrisul",

"mercadopago",

"picpay",

"neon",

"c6"

)

foreach($Banco in $Bancos){

    Criar-Pasta "tests\$Banco"

    Criar-Arquivo "tests\$Banco\README.md"

    Criar-Arquivo "tests\$Banco\esperado.json"

}

Criar-Arquivo "logs\execucao.log"

Criar-Arquivo "logs\parser.log"

Criar-Arquivo "logs\financeiro.log"

Criar-Arquivo "logs\erros.log"

Criar-Arquivo "benchmark\benchmark.py"

Criar-Arquivo "benchmark\resultado.csv"

Criar-Arquivo "examples\README.md"

Write-Host ""
Write-Host "======================================================" -ForegroundColor Cyan
Write-Host " BOOTSTRAP FINALIZADO COM SUCESSO " -ForegroundColor Green
Write-Host "======================================================" -ForegroundColor Cyan
Write-Host ""


