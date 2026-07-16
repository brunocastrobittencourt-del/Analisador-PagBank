import re


class MotorParser:

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

    REGEX_DATA = re.compile(
        r"(\d{2})\s+"
        r"(JAN|FEV|MAR|ABR|MAI|JUN|JUL|AGO|SET|OUT|NOV|DEZ)"
        r"\s+(\d{4})",
        re.IGNORECASE
    )

    REGEX_VALOR = re.compile(
        r"([+-]?\s?\d{1,3}(?:\.\d{3})*,\d{2})$"
    )

    @classmethod
    def localizar_data(cls, linha):

        resultado = cls.REGEX_DATA.search(linha)

        if not resultado:
            return None

        dia = resultado.group(1)

        mes = cls.MESES[
            resultado.group(2).upper()
        ]

        ano = resultado.group(3)

        return f"{dia}/{mes}/{ano}"

    @classmethod
    def possui_data(cls, linha):

        return cls.localizar_data(linha) is not None

    @classmethod
    def localizar_valor(cls, linha):

        resultado = cls.REGEX_VALOR.search(linha)

        if not resultado:
            return None

        return cls.converter_valor(
            resultado.group(1)
        )

    @classmethod
    def possui_valor(cls, linha):

        return cls.localizar_valor(linha) is not None

    @staticmethod
    def converter_valor(valor):

        try:

            return float(

                valor
                .replace(".", "")
                .replace(",", ".")
                .replace("+", "")
                .replace("-", "")
                .strip()

            )

        except Exception:

            return None

    @classmethod
    def remover_valor(cls, linha):

        resultado = cls.REGEX_VALOR.search(linha)

        if not resultado:

            return linha.strip()

        return linha[:resultado.start()].strip()

    @staticmethod
    def limpar_texto(texto):

        return " ".join(

            texto
            .replace("\t", " ")
            .replace("\n", " ")
            .split()

        )

    @staticmethod
    def eh_linha_vazia(linha):

        return linha.strip() == ""

    @staticmethod
    def eh_cabecalho(linha):

        linha = linha.upper()

        cabecalhos = [

            "SALDO INICIAL",

            "SALDO FINAL",

            "MOVIMENTAÇÕES",

            "MOVIMENTACOES",

            "RENDIMENTO",

            "VALORES EM",

            "EXTRATO",

            "CPF",

            "AGÊNCIA",

            "AGENCIA",

            "CONTA"

        ]

        return any(

            cab in linha

            for cab in cabecalhos

        )

    @staticmethod
    def eh_total(linha):

        linha = linha.upper()

        return (

            "TOTAL DE ENTRADAS" in linha

            or "TOTAL DE SAÍDAS" in linha

            or "TOTAL DE SAIDAS" in linha

        )

    @staticmethod
    def eh_rodape(linha):

        linha = linha.upper()

        palavras = [

            "OUVIDORIA",

            "ATENDIMENTO",

            "EXTRATO GERADO",

            "NUBANK.COM.BR",

            "CAPITAIS",

            "REGIÕES METROPOLITANAS",

            "REGIOES METROPOLITANAS"

        ]

        return any(

            palavra in linha

            for palavra in palavras

        )