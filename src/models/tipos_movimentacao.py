from enum import Enum


class TipoMovimentacao(str, Enum):

    PIX_RECEBIDO = "PIX_RECEBIDO"
    PIX_ENVIADO = "PIX_ENVIADO"

    TED = "TED"
    DOC = "DOC"

    BOLETO = "BOLETO"

    CARTAO = "CARTAO"

    DEBITO = "DEBITO"

    CREDITO = "CREDITO"

    VENDA = "VENDA"

    CDB = "CDB"

    RESGATE = "RESGATE"

    TARIFA = "TARIFA"

    SAQUE = "SAQUE"

    SALDO = "SALDO"

    OUTROS = "OUTROS"