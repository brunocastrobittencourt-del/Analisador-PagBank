from dataclasses import dataclass


@dataclass
class Movimentacao:
    data: str
    descricao: str
    nome: str
    tipo: str
    valor: float
    considerar: bool = True