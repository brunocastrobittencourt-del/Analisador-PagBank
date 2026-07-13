import os

from services.leitor_pdf import LeitorPDF

from config.config import PASTA_ARQUIVOS


arquivos = [

    f for f in os.listdir(PASTA_ARQUIVOS)

    if f.lower().endswith(".pdf")

]

if len(arquivos) == 0:

    print("Nenhum PDF encontrado.")

    input()

    quit()

arquivo = os.path.join(PASTA_ARQUIVOS, arquivos[0])

print()

print("=" * 60)

print("ANALISADOR PAGBANK")

print("=" * 60)

print()

print(arquivo)

print()

pdf = LeitorPDF(arquivo)

print("Quantidade de páginas:")

print(pdf.total_paginas())

print()

texto = pdf.extrair_texto()

print()

print("Total de páginas lidas:")

print(len(texto))

input("ENTER")