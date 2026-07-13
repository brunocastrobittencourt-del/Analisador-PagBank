class Filtros:

    NOMES_EXCLUIDOS = [

        "ZELINDA AMARANTE DE LIMA",

        "JULIA DE LIMA CABRAL"

    ]

    TIPOS_EXCLUIDOS = [

        "PIX_ENVIADO",

        "CDB",

        "SALDO",

        "ESTORNO"

    ]

    @classmethod
    def filtrar(cls, movimentacoes):

        resultado = []

        for mov in movimentacoes:

            if mov.tipo in cls.TIPOS_EXCLUIDOS:
                continue

            if mov.nome.upper() in cls.NOMES_EXCLUIDOS:
                continue

            resultado.append(mov)

        return resultado