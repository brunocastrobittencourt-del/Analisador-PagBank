import re
from models.movimentacao import Movimentacao


class ParserExtrato:

    def __init__(self):
        self.movimentacoes = []

    def processar(self, paginas):

        regex = re.compile(
            r'(\d{2}/\d{2}/\d{4})\s+(.*?)\s+(-?R\$\s?[\d\.,]+)'
        )

        for pagina in paginas:

            linhas = pagina.split("\n")

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

                valor = float(valor)

                tipo = ""
                nome = ""

                descricao_lower = descricao.lower()

                if "pix recebido" in descricao_lower:
                    tipo = "PIX_RECEBIDO"
                    partes = descricao.split("-", 1)
                    if len(partes) == 2:
                        nome = partes[1].strip()

                elif "pix enviado" in descricao_lower:
                    tipo = "PIX_ENVIADO"
                    partes = descricao.split("-", 1)
                    if len(partes) == 2:
                        nome = partes[1].strip()

                elif "vendas - disponivel" in descricao_lower:
                    tipo = "VENDA"

                elif "saldo do dia" in descricao_lower:
                    tipo = "SALDO"

                elif "cdb" in descricao_lower:
                    tipo = "CDB"

                else:
                    tipo = "OUTROS"

                movimentacao = Movimentacao(
                    data=data,
                    descricao=descricao,
                    nome=nome,
                    tipo=tipo,
                    valor=valor,
                    considerar=True
                )

                self.movimentacoes.append(movimentacao)

        return self.movimentacoes