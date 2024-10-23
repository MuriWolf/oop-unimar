from abc import ABC, abstractmethod

class Imovel(ABC):
    def __init__(self, endereco: str, preco_base: float) -> None:
        self.endereco = endereco
        self.preco_base = preco_base
    
    def apresentar_preco_base(self) -> float:
        return self.preco_base

    @abstractmethod
    def apresentar_preco_final(self) -> float:
        pass

class Novo(Imovel):
    def __init__(self, endereco: str, preco_base: float, porcentagem_adicional: float) -> None:
        super().__init__(endereco, preco_base)
        self.porcentagem_adicional = porcentagem_adicional

    def apresentar_preco_base(self) -> float:
        return super().apresentar_preco_base()

    def apresentar_preco_final(self) -> float:
        return self.preco_base * (1 + self.porcentagem_adicional)

    
class Usado(Imovel):
    def __init__(self, endereco: str, preco_base: float, porcentagem_desconto: float) -> None:
        super().__init__(endereco, preco_base)
        self.porcentagem_desconto = porcentagem_desconto 

    def apresentar_preco_base(self) -> float:
        return super().apresentar_preco_base()

    def apresentar_preco_final(self) -> float:
        return self.preco_base * (1 - self.porcentagem_desconto)

