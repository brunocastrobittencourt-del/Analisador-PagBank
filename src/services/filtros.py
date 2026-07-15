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

        movimentacoes_validas = []
        movimentacoes_excluidas = []

        for mov in movimentacoes:

            motivo = None

            if mov.tipo in cls.TIPOS_EXCLUIDOS:
                motivo = mov.tipo

            elif mov.nome.upper() in cls.NOMES_EXCLUIDOS:
                motivo = "FAMILIAR"

            if motivo:
                mov.motivo_exclusao = motivo
                movimentacoes_excluidas.append(mov)
            else:
                movimentacoes_validas.append(mov)

        return movimentacoes_validas, movimentacoes_excluidas