from src.core.detector_banco import (
    DetectorBanco,
    Banco
)

from src.parsers.pagbank_parser import PagBankParser


class ParserFactory:

    @staticmethod
    def obter(paginas):

        banco = DetectorBanco.detectar(
            paginas
        )

        print(f"Banco detectado: {banco.value}")

        if banco == Banco.PAGBANK:

            return PagBankParser()

        raise Exception(

            f"Nenhum parser implementado para {banco.value}"

        )