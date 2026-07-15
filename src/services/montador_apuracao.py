from collections import defaultdict
from datetime import datetime

from models.apuracao import Apuracao


class MontadorApuracao:

    @staticmethod
    def montar(movimentacoes):

        apuracao = Apuracao()

        # Agrupamento por mês e dia
        meses = defaultdict(lambda: defaultdict(float))

        for mov in movimentacoes:

            if mov.tipo not in ["PIX_RECEBIDO", "VENDA"]:
                continue

            try:

                data = datetime.strptime(
                    mov.data,
                    "%d/%m/%Y"
                )

            except Exception:

                continue

            chave_mes = data.strftime("%m/%Y")

            meses[chave_mes][data.day] += mov.valor

        # Ordena os meses cronologicamente
        meses_ordenados = sorted(
            meses.keys(),
            key=lambda m: datetime.strptime(
                m,
                "%m/%Y"
            )
        )

        # Remove o primeiro mês se ele for parcial
        if meses_ordenados:

            primeiro = meses_ordenados[0]

            primeiro_dia = min(
                meses[primeiro].keys()
            )

            if primeiro_dia > 1:

                meses_ordenados.pop(0)

        # Mantém apenas os últimos 6 meses
        meses_ordenados = meses_ordenados[-6:]

        estrutura = {}

        totais = {}

        for mes in meses_ordenados:

            dias = {}

            total_mes = 0

            for dia in range(1, 32):

                valor = round(
                    meses[mes].get(dia, 0),
                    2
                )

                dias[dia] = valor

                total_mes += valor

            estrutura[mes] = dias

            totais[mes] = round(
                total_mes,
                2
            )

        apuracao.meses = estrutura

        apuracao.total_meses = totais

        apuracao.quantidade_meses = len(
            estrutura
        )

        if apuracao.quantidade_meses > 0:

            apuracao.media = round(

                sum(totais.values())

                / apuracao.quantidade_meses,

                2

            )

        return apuracao