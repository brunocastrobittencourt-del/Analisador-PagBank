from src.services.leitor_pdf import LeitorPDF
from src.services.filtros import Filtros
from src.parsers.parser_factory import ParserFactory
from src.normalizadores.normalizador import Normalizador


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

        print("\nSelecionando parser...")

        parser = ParserFactory.obter(
            paginas
        )

        print(
            f"Parser selecionado: {parser.__class__.__name__}"
        )

        print("\nExtraindo movimentações...")

        movimentacoes = parser.processar(
            paginas
        )

        print(
            f"Movimentações encontradas: {len(movimentacoes)}"
        )

        print("\nNormalizando movimentações...")

        movimentacoes = Normalizador.normalizar(
            movimentacoes
        )

        print("\nAplicando filtros...")

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