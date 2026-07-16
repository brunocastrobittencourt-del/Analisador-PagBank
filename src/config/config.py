import os

# =====================================================
# DIRETÓRIO BASE DO PROJETO
# =====================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

# =====================================================
# PASTAS
# =====================================================

PASTA_ARQUIVOS = os.path.join(
    BASE_DIR,
    "arquivos"
)

PASTA_RESULTADOS = os.path.join(
    BASE_DIR,
    "resultados"
)

PASTA_TEMPLATES = os.path.join(
    BASE_DIR,
    "templates"
)

PASTA_LOGS = os.path.join(
    BASE_DIR,
    "logs"
)

# Garante que as pastas existam
os.makedirs(PASTA_ARQUIVOS, exist_ok=True)
os.makedirs(PASTA_RESULTADOS, exist_ok=True)
os.makedirs(PASTA_LOGS, exist_ok=True)

# =====================================================
# MODELO EXCEL
# =====================================================

MODELO_APURACAO = os.path.join(
    PASTA_TEMPLATES,
    "Modelo_Renda_Informal.xlsx"
)

# =====================================================
# CONFIGURAÇÃO DA PLANILHA
# =====================================================

COLUNAS_MESES = [
    "B",
    "C",
    "D",
    "E",
    "F",
    "G"
]

LINHA_MESES = 13

LINHA_INICIAL_DIAS = 14

LINHA_TOTAL = 45

CELULA_MEDIA = "F47"

LARGURAS_COLUNAS = {
    "A": 8,
    "B": 16,
    "C": 16,
    "D": 16,
    "E": 16,
    "F": 16,
    "G": 16,
}

FORMATO_MOEDA = 'R$ #,##0.00'

# =====================================================
# PADRÕES
# =====================================================

BANCO_PADRAO = "PAGBANK"

PROCESSO_PADRAO = "CCMCMV"

NOME_ARQUIVO_APURACAO = "APURACAO_DE_RENDA.xlsx"

# =====================================================
# TIPOS DE RECEITA
# =====================================================

TIPOS_RECEITA = [
    "PIX_RECEBIDO",
    "VENDA"
]

# =====================================================
# TIPOS EXCLUÍDOS
# =====================================================

TIPOS_EXCLUIR = [
    "PIX_ENVIADO",
    "TED",
    "DOC",
    "CDB",
    "RESGATE",
    "ESTORNO",
    "TARIFA",
    "SAQUE"
]