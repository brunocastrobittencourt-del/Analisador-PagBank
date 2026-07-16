from dataclasses import dataclass


@dataclass
class PaginaPDF:

    numero: int

    texto: str

    layout: str

    palavras: list