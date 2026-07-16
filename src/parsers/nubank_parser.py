import re

from src.parsers.base_parser import BaseParser
from src.models.movimentacao import Movimentacao


class NubankParser(BaseParser):

    MESES = {
        "JAN": "01",
        "FEV": "02",
        "MAR": "03",
        "ABR": "04",
        "MAI": "05",
        "JUN": "06",
        "JUL": "07",
        "AGO": "08",
        "SET": "09",
        "OUT": "10",
        "NOV": "11",
        "DEZ": "12",
    }

    def __init__(self):

        self.movimentacoes = []

    def identificar(self, paginas):

        if not paginas:
            return False

        return "NUBANK" in paginas[0].texto.upper()

    def processar(self, paginas):

        self.movimentacoes = []

        data_atual = None

        regex_data = re.compile(
            r"(\d{2})\s+(JAN|FEV|MAR|ABR|MAI|JUN|JUL|AGO|SET|OUT|NOV|DEZ)\s+(\d{4})"
        )

        regex_valor = re.compile(
            r"([+-]?\s?\d{1,3}(?:\.\d{3})*,\d{2})$"
        )

        for pagina in paginas:

            linhas = pagina.layout.split("\n")

            for linha in linhas:

                linha = linha.strip()

                if not linha:

                    continue

                # -------------------------
                # DATA
                # -------------------------

                data = regex_data.search(
                    linha.upper()
                )

                if data:

                    dia = data.group(1)

                    mes = self.MESES[data.group(2)]

                    ano = data.group(3)

                    data_atual = f"{dia}/{mes}/{ano}"

                    continue

                if not data_atual:

                    continue

                # -------------------------
                # Ignora cabeçalhos
                # -------------------------

                if "TOTAL DE ENTRADAS" in linha.upper():

                    continue

                if "TOTAL DE SAÍDAS" in linha.upper():

                    continue

                if "SALDO FINAL" in linha.upper():

                    continue

                if "MOVIMENTAÇÕES" in linha.upper():

                    continue

                # -------------------------
                # Procura valor
                # -------------------------

                valor = regex_valor.search(
                    linha
                )

                if not valor:

                    continue

                texto = linha[:valor.start()].strip()

                numero = (
                    valor.group(1)
                    .replace(".", "")
                    .replace(",", ".")
                    .replace("+", "")
                    .replace("-", "")
                    .strip()
                )

                try:

                    numero = float(numero)

                except Exception:

                    continue

                movimentacao = Movimentacao(

                    data=data_atual,

                    descricao=texto,

                    nome="",

                    tipo="",

                    valor=numero,

                    banco="NUBANK",

                    considerar=True

                )

                self.movimentacoes.append(
                    movimentacao
                )

                ...

                self.movimentacoes.append(
                    movimentacao
            )

                print("\n" + "=" * 80)
                print("PRIMEIRAS MOVIMENTAÇÕES ENCONTRADAS")
                print("=" * 80)

             for mov in self.movimentacoes[:10]:

                print(
                 mov.data,
                   "|",
                mov.descricao,
                   "|",
                mov.valor
          )

                print("=" * 80)

        return self.movimentacoes

      