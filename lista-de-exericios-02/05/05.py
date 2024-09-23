from abc import ABC, abstractmethod

class MetodoPagamento(ABC):
    def __init__(self, nome, saldo) -> None:
        self.nome = nome
        self.saldo = saldo

    @abstractmethod
    def pagar():
        pass

class MetodoPix(MetodoPagamento):
    pass
