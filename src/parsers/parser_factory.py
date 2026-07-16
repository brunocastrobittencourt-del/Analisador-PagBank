from src.core.detector_banco import (
    DetectorBanco,
    Banco
)


class ParserFactory:

    @staticmethod
    def obter(paginas):

        banco = DetectorBanco.detectar(
            paginas
        )

        print(f"Banco detectado: {banco.value}")

        # ======================================================
        # PAGBANK
        # ======================================================

        if banco == Banco.PAGBANK:

            from src.parsers.pagbank_parser import PagBankParser

            return PagBankParser()

        # ======================================================
        # NUBANK
        # ======================================================

        if banco == Banco.NUBANK:

            from src.parsers.nubank_parser import NubankParser

            return NubankParser()

        # ======================================================
        # CAIXA
        # ======================================================

        if banco == Banco.CAIXA:

            from src.parsers.caixa_parser import CaixaParser

            return CaixaParser()

        # ======================================================
        # ITAÚ
        # ======================================================

        if banco == Banco.ITAU:

            from src.parsers.itau_parser import ItauParser

            return ItauParser()

        # ======================================================
        # BRADESCO
        # ======================================================

        if banco == Banco.BRADESCO:

            from src.parsers.bradesco_parser import BradescoParser

            return BradescoParser()

        # ======================================================
        # BANCO DO BRASIL
        # ======================================================

        if banco == Banco.BANCO_DO_BRASIL:

            from src.parsers.banco_do_brasil_parser import BancoDoBrasilParser

            return BancoDoBrasilParser()

        # ======================================================
        # SANTANDER
        # ======================================================

        if banco == Banco.SANTANDER:

            from src.parsers.santander_parser import SantanderParser

            return SantanderParser()

        # ======================================================
        # INTER
        # ======================================================

        if banco == Banco.INTER:

            from src.parsers.inter_parser import InterParser

            return InterParser()

        # ======================================================
        # SICREDI
        # ======================================================

        if banco == Banco.SICREDI:

            from src.parsers.sicredi_parser import SicrediParser

            return SicrediParser()

        # ======================================================
        # BANRISUL
        # ======================================================

        if banco == Banco.BANRISUL:

            from src.parsers.banrisul_parser import BanrisulParser

            return BanrisulParser()

        # ======================================================
        # MERCADO PAGO
        # ======================================================

        if banco == Banco.MERCADO_PAGO:

            from src.parsers.mercadopago_parser import MercadoPagoParser

            return MercadoPagoParser()

        # ======================================================
        # PICPAY
        # ======================================================

        if banco == Banco.PICPAY:

            from src.parsers.picpay_parser import PicPayParser

            return PicPayParser()

        # ======================================================
        # C6
        # ======================================================

        if banco == Banco.C6:

            from src.parsers.c6_parser import C6Parser

            return C6Parser()

        # ======================================================
        # NEON
        # ======================================================

        if banco == Banco.NEON:

            from src.parsers.neon_parser import NeonParser

            return NeonParser()

        # ======================================================
        # UBER
        # ======================================================

        if banco == Banco.UBER:

            from src.parsers.uber_parser import UberParser

            return UberParser()

        # ======================================================
        # IFOOD
        # ======================================================

        if banco == Banco.IFOOD:

            from src.parsers.ifood_parser import IfoodParser

            return IfoodParser()

        # ======================================================

        raise Exception(

            f"Nenhum parser implementado para {banco.value}"

        )