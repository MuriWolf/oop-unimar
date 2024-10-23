from abc import ABC

class Ingresso(ABC):
    def __init__(self, valor: float) -> None:
        self.valor: float = valor
# deixar como abstract method
    def retornar_valor(self):
        return self.valor

class Vip(Ingresso):
    def __init__(self, valor: float) -> None:
        super().__init__(valor)
        self.adicional: float = 0.075

    def retornar_valor(self):
        return self.valor * (1 + self.adicional)

class Normal(Ingresso):
    def __init__(self, valor: float) -> None:
        super().__init__(valor)

    def retornar_valor(self):
        return super().retornar_valor()

class CamaroteInferior(Vip):
    def __init__(self, valor: float, localizacao: str) -> None:
        super().__init__(valor)
        self.localizacao = localizacao

    def retornar_localizacao(self):
        return self.localizacao

class CamaroteSuperior(Vip):
    def __init__(self, valor: float) -> None:
        super().__init__(valor)
        self.adicional: float = 0.025

    def retornar_valor(self):
        return super().retornar_valor() * (1 + self.adicional)


