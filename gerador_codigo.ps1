function Escrever-Python {

    param(
        [string]$Arquivo,
        [string]$Conteudo
    )

    $Pasta = Split-Path $Arquivo

    if (!(Test-Path $Pasta)) {
        New-Item -ItemType Directory -Path $Pasta -Force | Out-Null
    }

    $Conteudo | Set-Content -Encoding UTF8 $Arquivo

    Write-Host "[OK] $Arquivo"
}

$datas = @'
MESES = {

    "JAN": "01",
    "FEV": "02",
    "MAR": "03",
    "ABR": "04",
    "MAI": "05",
    "JUN": "06",
    "JUL": "07",
    "AGO": "08",
    "SET": "09",
    "OUT": "10",
    "NOV": "11",
    "DEZ": "12"

}
'@

Escrever-Python "src/constants/datas.py" $datas

$mov = @'
class TipoMovimentacao:

    PIX_RECEBIDO = "PIX_RECEBIDO"
    PIX_ENVIADO = "PIX_ENVIADO"

    TED = "TED"
    DOC = "DOC"

    BOLETO = "BOLETO"

    VENDA = "VENDA"

    SALARIO = "SALARIO"

    CDB = "CDB"

    RESGATE = "RESGATE"

    INVESTIMENTO = "INVESTIMENTO"

    EMPRESTIMO = "EMPRESTIMO"

    FAMILIAR = "FAMILIAR"

    TRANSFERENCIA_PROPRIA = "TRANSFERENCIA_PROPRIA"

    MARKETPLACE = "MARKETPLACE"

    UBER = "UBER"

    IFOOD = "IFOOD"

    JOGO = "JOGO"

    TARIFA = "TARIFA"

    SAQUE = "SAQUE"

    ESTORNO = "ESTORNO"

    OUTROS = "OUTROS"
'@

Escrever-Python "src/constants/movimentacoes.py" $mov

function Gerar-Constants {

    Write-Host "Gerando Constants..."

}

function Gerar-Models {

    Write-Host "Gerando Models..."

}

function Gerar-Classificadores {

    Write-Host "Gerando Classificadores..."

}

function Gerar-Analisadores {

    Write-Host "Gerando Analisadores..."

}

function Gerar-Exportadores {

    Write-Host "Gerando Exportadores..."

}

function Gerar-MotorParser {

    Write-Host "Gerando Motor Parser..."

}

function Gerar-Parsers {

    Write-Host "Gerando Parsers..."

}

function Gerar-Testes {

    Write-Host "Gerando Testes..."

}

Clear-Host

Write-Host ""
Write-Host "==============================================="
Write-Host "      GERADOR DE CÓDIGO"
Write-Host "==============================================="
Write-Host ""

Write-Host "1 - Constants"

Write-Host "2 - Models"

Write-Host "3 - Classificadores"

Write-Host "4 - Analisadores"

Write-Host "5 - Exportadores"

Write-Host "6 - Motor Parser"

Write-Host "7 - Parser"

Write-Host "8 - Testes"

Write-Host "9 - Tudo"

Write-Host ""

$opcao = Read-Host "Escolha"

switch($opcao){

    "1" { Gerar-Constants }

    "2" { Gerar-Models }

    "3" { Gerar-Classificadores }

    "4" { Gerar-Analisadores }

    "5" { Gerar-Exportadores }

    "6" { Gerar-MotorParser }

    "7" { Gerar-Parsers }

    "8" { Gerar-Testes }

    "9" {

        Gerar-Constants

        Gerar-Models

        Gerar-Classificadores

        Gerar-Analisadores

        Gerar-Exportadores

        Gerar-MotorParser

        Gerar-Parsers

        Gerar-Testes

    }

}