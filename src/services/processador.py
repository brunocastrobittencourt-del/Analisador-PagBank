from services.leitor_pdf import LeitorPDF
from services.parser import ParserExtrato
from services.filtros import Filtros
from services.agrupador import Agrupador
from excel.gerador_excel import GeradorExcel


class ProcessadorExtrato:

    def __init__(self, arquivo_pdf, pasta_resultados):
        self.arquivo_pdf = arquivo_pdf
        self.pasta_resultados = pasta_resultados

    def executar(self):

        print("\nLendo PDF...")

        leitor = LeitorPDF(self.arquivo_pdf)
        paginas = leitor.extrair_texto()

        print("\nProcessando movimentações...")

        parser = ParserExtrato()
        movimentacoes = parser.processar(paginas)

        print(f"Movimentações encontradas: {len(movimentacoes)}")

        movimentacoes = Filtros.filtrar(movimentacoes)

        print(f"Movimentações válidas: {len(movimentacoes)}")

        print("\nAgrupando por data...")

        totais = Agrupador.agrupar_por_data(movimentacoes)

        receita_total = sum(totais.values())
        quantidade_dias = len(totais)

        media_diaria = (
            receita_total / quantidade_dias
            if quantidade_dias > 0 else 0
        )

        maior_dia = max(totais.values()) if totais else 0
        menor_dia = min(totais.values()) if totais else 0

        print("\nGerando planilhas...")

        arquivo = GeradorExcel.gerar(
            totais,
            self.pasta_resultados
        )

        GeradorExcel.gerar_movimentacoes(
            movimentacoes,
            self.pasta_resultados
        )

        GeradorExcel.gerar_resumo(
            receita_total,
            quantidade_dias,
            media_diaria,
            maior_dia,
            menor_dia,
            self.pasta_resultados
        )

        print("\nArquivos gerados com sucesso!")

        print(arquivo)

        return movimentacoes