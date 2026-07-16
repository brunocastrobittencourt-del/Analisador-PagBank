import os

from src.config.config import (
    PASTA_ARQUIVOS,
    PASTA_RESULTADOS,
    MODELO_APURACAO
)

from src.services.processador import ProcessadorExtrato
from src.services.montador_apuracao import MontadorApuracao
from src.excel.apuracao_renda import ApuracaoRenda


def main():

    arquivos = [
        arquivo
        for arquivo in os.listdir(PASTA_ARQUIVOS)
        if arquivo.lower().endswith(".pdf")
    ]

    if not arquivos:

        print("=" * 70)
        print("NENHUM PDF ENCONTRADO.")
        print("=" * 70)

        input("\nENTER")
        return

    arquivo_pdf = os.path.join(
        PASTA_ARQUIVOS,
        arquivos[0]
    )

    print("=" * 70)
    print("ANALISADOR FINANCEIRO")
    print("=" * 70)

    processador = ProcessadorExtrato(
        arquivo_pdf,
        PASTA_RESULTADOS
    )

    movimentacoes = processador.executar()

    print()

    print("=" * 70)
    print("MONTANDO APURAÇÃO...")
    print("=" * 70)

    apuracao = MontadorApuracao.montar(
        movimentacoes
    )

    print()

    print("=" * 70)
    print("RESUMO DA APURAÇÃO")
    print("=" * 70)

    print(f"Movimentações válidas : {len(movimentacoes)}")
    print(f"Meses encontrados      : {apuracao.quantidade_meses}")
    print(f"Média dos meses        : R$ {apuracao.media:,.2f}")

    print()

    print("=" * 70)
    print("TOTAIS MENSAIS")
    print("=" * 70)

    for mes, total in apuracao.total_meses.items():
        print(f"{mes} -> R$ {total:,.2f}")

    print()

    print("=" * 70)
    print("GERANDO PLANILHA...")
    print("=" * 70)

    gerador = ApuracaoRenda(
        MODELO_APURACAO,
        PASTA_RESULTADOS
    )

    arquivo_excel = gerador.gerar(
        apuracao
    )

    print()

    print("=" * 70)
    print("PLANILHA GERADA COM SUCESSO")
    print("=" * 70)

    print(arquivo_excel)

    print()

    input("ENTER")


if __name__ == "__main__":
    main()