from collections import defaultdict
from datetime import datetime


class Agrupador:

    @staticmethod
    def agrupar_por_data(movimentacoes):

        totais = defaultdict(float)

        for mov in movimentacoes:

            if mov.tipo not in ["PIX_RECEBIDO", "VENDA"]:
                continue

            totais[mov.data] += mov.valor

        return dict(
            sorted(
                totais.items(),
                key=lambda item: datetime.strptime(item[0], "%d/%m/%Y")
            )
        )