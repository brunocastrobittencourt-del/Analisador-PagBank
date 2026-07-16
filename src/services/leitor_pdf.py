import pdfplumber

from src.models.pagina_pdf import PaginaPDF


class LeitorPDF:

    def __init__(self, arquivo):

        self.arquivo = arquivo

    def abrir(self):

        return pdfplumber.open(self.arquivo)

    def total_paginas(self):

        with pdfplumber.open(self.arquivo) as pdf:

            return len(pdf.pages)

    def extrair_texto(self):

        paginas = []

        with pdfplumber.open(self.arquivo) as pdf:

            total = len(pdf.pages)

            for numero, pagina in enumerate(pdf.pages):

                print(f"Lendo página {numero + 1} de {total}")

                texto = pagina.extract_text() or ""

                try:

                    layout = pagina.extract_text(
                        layout=True
                    ) or ""

                except Exception:

                    layout = texto

                try:

                    palavras = pagina.extract_words()

                except Exception:

                    palavras = []

                paginas.append(

                    PaginaPDF(

                        numero=numero + 1,

                        texto=texto,

                        layout=layout,

                        palavras=palavras

                    )

                )

        if paginas:

            print("\n" + "=" * 80)
            print("PRIMEIRA PÁGINA (TEXTO)")
            print("=" * 80)
            print(paginas[0].texto)

            print("\n" + "=" * 80)
            print("PRIMEIRA PÁGINA (LAYOUT)")
            print("=" * 80)
            print(paginas[0].layout)

            print("=" * 80)

        return paginas