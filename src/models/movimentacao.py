from dataclasses import dataclass


@dataclass
class Movimentacao:

    # Dados da movimentação
    data: str
    descricao: str
    nome: str
    tipo: str
    valor: float

    # Dados complementares
    documento: str = ""
    categoria: str = ""
    saldo: float = 0.0
    observacao: str = ""

    # Dados da conta
    banco: str = ""
    agencia: str = ""
    conta: str = ""

    # Controle interno
    considerar: bool = True