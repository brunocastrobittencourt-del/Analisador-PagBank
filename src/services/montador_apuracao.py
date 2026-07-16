from collections import defaultdict
from datetime import datetime

from src.models.apuracao import Apuracao


class MontadorApuracao:

    @staticmethod
    def montar(movimentacoes):

        apuracao = Apuracao()

        # ==========================
        # Cabeçalho
        # ==========================

        apuracao.banco = "PAGBANK"
        apuracao.processo = "CCMCMV"

        # ==========================
        # Agrupamento
        # ==========================

        meses = defaultdict(lambda: defaultdict(float))

        for mov in movimentacoes:

            if mov.tipo not in ["PIX_RECEBIDO", "VENDA"]:
                continue

            try:

                data = datetime.strptime(
                    mov.data,
                    "%d/%m/%Y"
                )

            except ValueError:
                continue

            chave_mes = data.strftime("%m/%Y")

            meses[chave_mes][data.day] += mov.valor

        # ==========================
        # Ordenação
        # ==========================

        meses_ordenados = sorted(
            meses.keys(),
            key=lambda m: datetime.strptime(
                m,
                "%m/%Y"
            )
        )

        # Remove primeiro mês parcial

        if meses_ordenados:

            primeiro = meses_ordenados[0]

            primeiro_dia = min(
                meses[primeiro].keys()
            )

            if primeiro_dia > 1:

                meses_ordenados.pop(0)

        # Mantém somente os últimos 6 meses

        meses_ordenados = meses_ordenados[-6:]

        estrutura = {}

        totais = {}

        # ==========================
        # Montagem da estrutura
        # ==========================

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

        # ==========================
        # Resultado
        # ==========================

        apuracao.meses = estrutura

        apuracao.total_meses = totais

        apuracao.quantidade_meses = len(
            estrutura
        )

        if apuracao.quantidade_meses > 0:

            apuracao.media = round(

                sum(
                    totais.values()
                )
                / apuracao.quantidade_meses,

                2

            )

        return apuracao
