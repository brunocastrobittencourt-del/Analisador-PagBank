import pdfplumber


class LeitorPDF:

    def __init__(self, arquivo):

        self.arquivo = arquivo

    def abrir(self):

        return pdfplumber.open(self.arquivo)

    def total_paginas(self):

        with pdfplumber.open(self.arquivo) as pdf:

            return len(pdf.pages)

    def extrair_texto(self):

        texto = []

        with pdfplumber.open(self.arquivo) as pdf:

            total = len(pdf.pages)

            for numero, pagina in enumerate(pdf.pages):

                print(f"Lendo página {numero + 1} de {total}")

                conteudo = pagina.extract_text()

                if conteudo:

                    texto.append(conteudo)

        # Apenas para depuração
        if texto:

            print("\n" + "=" * 80)
            print("PRIMEIRA PÁGINA DO PDF")
            print("=" * 80)
            print(texto[0])
            print("=" * 80)

        return texto