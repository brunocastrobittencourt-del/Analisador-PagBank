"""
CONFIGURAÇÕES DO SISTEMA
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

PASTA_ARQUIVOS = os.path.join(BASE_DIR, "arquivos")
PASTA_RESULTADOS = os.path.join(BASE_DIR, "resultados")
PASTA_LOGS = os.path.join(BASE_DIR, "logs")

NOMES_EXCLUIDOS = [
    "ZELINDA AMARANTE DE LIMA",
    "JULIA DE LIMA CABRAL"
]

PALAVRAS_EXCLUIDAS = [

    "PIX ENVIADO",

    "QR CODE PIX ENVIADO",

    "APLICAÇÃO EM CDB",

    "RESGATE DE CDB",

    "ESTORNO",

    "DEVOLUÇÃO",

    "SAQUE",

    "TARIFA"

]

TIPOS_RECEITA = [

    "PIX RECEBIDO",

    "VENDAS - DISPONIVEL"

]