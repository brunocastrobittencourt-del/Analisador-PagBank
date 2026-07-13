from services.processador import ProcessadorExtrato
from services.agrupador import Agrupador
from excel.gerador_excel import GeradorExcel
from config.config import PASTA_RESULTADOS
from services.filtros import Filtros
import os

from services.leitor_pdf import LeitorPDF
from services.parser import ParserExtrato
from config.config import PASTA_ARQUIVOS


arquivos = [
    f for f in os.listdir(PASTA_ARQUIVOS)
    if f.lower().endswith(".pdf")
]

if not arquivos:
    print("Nenhum PDF encontrado.")
    input()
    quit()

arquivo = os.path.join(PASTA_ARQUIVOS, arquivos[0])

print("=" * 60)
print("ANALISADOR PAGBANK")
print("=" * 60)

processador = ProcessadorExtrato(
    arquivo,
    PASTA_RESULTADOS
)

movimentacoes = processador.executar()

print()

print("=" * 70)

print("PLANILHA GERADA COM SUCESSO")

print()


print()

print()
print("=" * 70)

print(f"TOTAL DE MOVIMENTAÇÕES: {len(movimentacoes)}")

print("=" * 70)

print("\nPRIMEIRAS 50 MOVIMENTAÇÕES\n")
print("=" * 100)

for indice, mov in enumerate(movimentacoes[:50], start=1):

    print(
        f"{indice:02d} | "
        f"{mov.data} | "
        f"{mov.tipo} | "
        f"{mov.nome} | "
        f"R$ {mov.valor:.2f} | "
        f"{mov.descricao}"
    )

print("=" * 100)