from enum import Enum


class Banco(Enum):

    PAGBANK = "PAGBANK"
    NUBANK = "NUBANK"
    CAIXA = "CAIXA"
    ITAU = "ITAU"
    SANTANDER = "SANTANDER"
    BRADESCO = "BRADESCO"
    BANCO_DO_BRASIL = "BANCO_DO_BRASIL"
    SICREDI = "SICREDI"
    BANRISUL = "BANRISUL"
    INTER = "INTER"
    MERCADO_PAGO = "MERCADO_PAGO"
    PICPAY = "PICPAY"
    C6 = "C6"
    NEON = "NEON"
    IFOOD = "IFOOD"
    UBER = "UBER"

    DESCONHECIDO = "DESCONHECIDO"


class DetectorBanco:

    @staticmethod
    def detectar(paginas):

        if not paginas:

            return Banco.DESCONHECIDO

        texto = paginas[0].upper()

        if "PAGBANK" in texto or "PAGSEGURO" in texto:
            return Banco.PAGBANK

        if "NUBANK" in texto:
            return Banco.NUBANK

        if "CAIXA ECONÔMICA" in texto or "CAIXA ECONOMICA" in texto:
            return Banco.CAIXA

        if "ITAÚ" in texto or "ITAU" in texto:
            return Banco.ITAU

        if "SANTANDER" in texto:
            return Banco.SANTANDER

        if "BRADESCO" in texto:
            return Banco.BRADESCO

        if "BANCO DO BRASIL" in texto:
            return Banco.BANCO_DO_BRASIL

        if "SICREDI" in texto:
            return Banco.SICREDI

        if "BANRISUL" in texto:
            return Banco.BANRISUL

        if "INTER" in texto:
            return Banco.INTER

        if "MERCADO PAGO" in texto:
            return Banco.MERCADO_PAGO

        if "PICPAY" in texto:
            return Banco.PICPAY

        if "C6 BANK" in texto or "C6BANK" in texto:
            return Banco.C6

        if "NEON" in texto:
            return Banco.NEON

        return Banco.DESCONHECIDO