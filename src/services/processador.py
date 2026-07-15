from services.leitor_pdf import LeitorPDF
from services.parser import ParserExtrato
from services.filtros import Filtros


class ProcessadorExtrato:

    def __init__(self, arquivo_pdf, pasta_resultados):

        self.arquivo_pdf = arquivo_pdf
        self.pasta_resultados = pasta_resultados

    def executar(self):

        print("\nLendo PDF...")

        leitor = LeitorPDF(
            self.arquivo_pdf
        )

        paginas = leitor.extrair_texto()

        print("\nProcessando movimentações...")

        parser = ParserExtrato()

        movimentacoes = parser.processar(
            paginas
        )

        print(
            f"Movimentações encontradas: {len(movimentacoes)}"
        )

        movimentacoes, movimentacoes_excluidas = Filtros.filtrar(
            movimentacoes
        )

        print(
            f"Movimentações válidas: {len(movimentacoes)}"
        )

        print(
            f"Movimentações excluídas: {len(movimentacoes_excluidas)}"
        )

        return movimentacoes