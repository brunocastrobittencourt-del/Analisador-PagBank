import re

from src.parsers.base_parser import BaseParser
from src.models.movimentacao import Movimentacao


class PagBankParser(BaseParser):

    def __init__(self):

        self.movimentacoes = []

    def identificar(self, paginas):

        if not paginas:
            return False

        return "PAGBANK" in paginas[0].texto.upper()

    def processar(self, paginas):

        self.movimentacoes = []

        regex = re.compile(
            r'(\d{2}/\d{2}/\d{4})\s+(.*?)\s+(-?R\$\s?[\d\.,]+)'
        )

        for pagina in paginas:

            linhas = pagina.texto.split("\n")

            for linha in linhas:

                linha = linha.strip()

                if not linha:
                    continue

                resultado = regex.search(linha)

                if not resultado:
                    continue

                data = resultado.group(1)

                descricao = resultado.group(2).strip()

                valor = (
                    resultado.group(3)
                    .replace("R$", "")
                    .replace(".", "")
                    .replace(",", ".")
                    .replace(" ", "")
                )

                try:

                    valor = float(valor)

                except ValueError:

                    continue

                nome = ""

                descricao_lower = descricao.lower()

                if "pix recebido" in descricao_lower:

                    partes = descricao.split("-", 1)

                    if len(partes) == 2:

                        nome = partes[1].strip()

                    tipo = "PIX_RECEBIDO"

                elif "pix enviado" in descricao_lower:

                    partes = descricao.split("-", 1)

                    if len(partes) == 2:

                        nome = partes[1].strip()

                    tipo = "PIX_ENVIADO"

                elif "vendas - disponivel" in descricao_lower:

                    tipo = "VENDA"

                elif "saldo do dia" in descricao_lower:

                    tipo = "SALDO"

                elif "cdb" in descricao_lower:

                    tipo = "CDB"

                else:

                    tipo = ""

                movimentacao = Movimentacao(

                    data=data,

                    descricao=descricao,

                    nome=nome,

                    tipo=tipo,

                    valor=valor,

                    considerar=True

                )

                self.movimentacoes.append(
                    movimentacao
                )

        return self.movimentacoes