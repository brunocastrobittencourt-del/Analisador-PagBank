from collections import defaultdict


class Agrupador:

    @staticmethod
    def agrupar_por_data(movimentacoes):

        totais = defaultdict(float)

        for mov in movimentacoes:

            if mov.tipo not in ["PIX_RECEBIDO", "VENDA"]:
                continue

            totais[mov.data] += mov.valor

        return dict(sorted(totais.items()))