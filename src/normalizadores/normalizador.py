from src.models.tipos_movimentacao import TipoMovimentacao


class Normalizador:

    @staticmethod
    def normalizar(movimentacoes):

        for mov in movimentacoes:

            # Se o parser já identificou o tipo,
            # mantém a classificação.
            if mov.tipo:
                continue

            descricao = mov.descricao.upper()

            # PIX

            if "PIX" in descricao:

                if "RECEB" in descricao or "CREDITO" in descricao:

                    mov.tipo = TipoMovimentacao.PIX_RECEBIDO

                elif "ENVI" in descricao or "DEBITO" in descricao:

                    mov.tipo = TipoMovimentacao.PIX_ENVIADO

                else:

                    mov.tipo = TipoMovimentacao.OUTROS

            # TED

            elif "TED" in descricao:

                mov.tipo = TipoMovimentacao.TED

            # DOC

            elif "DOC" in descricao:

                mov.tipo = TipoMovimentacao.DOC

            # BOLETO

            elif "BOLETO" in descricao:

                mov.tipo = TipoMovimentacao.BOLETO

            # VENDA

            elif "VENDA" in descricao:

                mov.tipo = TipoMovimentacao.VENDA

            # CDB

            elif "CDB" in descricao:

                mov.tipo = TipoMovimentacao.CDB

            # RESGATE

            elif "RESGATE" in descricao:

                mov.tipo = TipoMovimentacao.RESGATE

            # TARIFA

            elif "TARIFA" in descricao:

                mov.tipo = TipoMovimentacao.TARIFA

            # SAQUE

            elif "SAQUE" in descricao:

                mov.tipo = TipoMovimentacao.SAQUE

            else:

                mov.tipo = TipoMovimentacao.OUTROS

        return movimentacoes