from abc import ABC, abstractmethod


class BaseParser(ABC):

    @abstractmethod
    def identificar(self, paginas):
        """
        Retorna True se este parser consegue interpretar o PDF.
        """
        pass

    @abstractmethod
    def processar(self, paginas):
        """
        Retorna uma lista de Movimentacao.
        """
        pass