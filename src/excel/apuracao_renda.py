from openpyxl import load_workbook
import os


class ApuracaoRenda:

    COLUNAS = ["B", "C", "D", "E", "F", "G"]

    LINHA_MESES = 12
    LINHA_INICIAL_DIAS = 14
    LINHA_TOTAL = 45
    CELULA_MEDIA = "F47"

    def __init__(self, modelo, pasta_resultados):

        self.modelo = modelo
        self.pasta_resultados = pasta_resultados

    def gerar(self, apuracao):

        wb = load_workbook(self.modelo)

        ws = wb.active

        meses = list(apuracao.meses.keys())

        # -------------------------
        # Escreve os meses
        # -------------------------

        for indice, mes in enumerate(meses):

            if indice >= 6:
                break

            coluna = self.COLUNAS[indice]

            ws[f"{coluna}{self.LINHA_MESES}"] = mes

        # -------------------------
        # Escreve os valores diários
        # -------------------------

        for indice, mes in enumerate(meses):

            if indice >= 6:
                break

            coluna = self.COLUNAS[indice]

            dias = apuracao.meses[mes]

            for dia in range(1, 32):

                linha = self.LINHA_INICIAL_DIAS + (dia - 1)

                valor = dias[dia]

                if valor > 0:

                    ws[f"{coluna}{linha}"] = valor

        # -------------------------
        # Totais
        # -------------------------

        for indice, mes in enumerate(meses):

            if indice >= 6:
                break

            coluna = self.COLUNAS[indice]

            ws[f"{coluna}{self.LINHA_TOTAL}"] = apuracao.total_meses[mes]

        # -------------------------
        # Média
        # -------------------------

        ws[self.CELULA_MEDIA] = apuracao.media

        caminho = os.path.join(

            self.pasta_resultados,

            "Apuracao_Renda.xlsx"

        )

        wb.save(caminho)

        return caminho