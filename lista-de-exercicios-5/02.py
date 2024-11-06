from abc import ABC, abstractmethod

class Remedio(ABC):
    def __init__(self, nome: str, valor: float) -> None:
        self.nome = nome
        self.valor = valor
    
    @abstractmethod
    def retornar_valor(self) -> float:
       return self.valor 

class RemedioGenerico(Remedio):
    def __init__(self, nome: str, valor: float) -> None:
        super().__init__(nome, valor)

    def retornar_valor(self) -> float:
        return self.valor * 0.8

class RemedioMarca(Remedio):
    def __init__(self, nome: str, valor: float, marca: str) -> None:
        super().__init__(nome, valor)
        self.marca = marca

    def retornar_valor(self) -> float:
        return super().retornar_valor()

class Farmacia:
    def __init__(self, remedios_genericos: list[RemedioGenerico], remedios_marca: list[RemedioMarca]) -> None:
        self.remedios_genericos = remedios_genericos
        self.remedios_marca = remedios_marca

    def calcular_valor_remedios_genericos(self) -> float:
        total: float = 0.0
        for remedio in self.remedios_genericos:
            total += remedio.retornar_valor()
        return total

    def calcular_valor_remedios_marca(self) -> float:
        total: float = 0.0
        for remedio in self.remedios_marca:
            total += remedio.retornar_valor()

        return total

    def calcular_valor_todos_remedios(self) -> float:
        return self.calcular_valor_remedios_marca() + self.calcular_valor_remedios_genericos()

remedioMarca01 = RemedioMarca(nome="clorofil", valor=50, marca="Umbrella Corporation")
remedioMarca02 = RemedioMarca(nome="dipirona", valor=100, marca="Farmacia bibi")

remedioGenerico01 = RemedioGenerico(nome="cloroquina", valor=32)
remedioGenerico02 = RemedioGenerico(nome="Dorflex", valor=12)
remedioGenerico03 = RemedioGenerico(nome="Extrato de uranio", valor=150)

farmacia = Farmacia(remedios_genericos=[remedioGenerico01, remedioGenerico02, remedioGenerico03], remedios_marca=[remedioMarca01, remedioMarca02])

print(f"Valor remedios genericos: {farmacia.calcular_valor_remedios_genericos()}")
print(f"Valor remedios de marca: {farmacia.calcular_valor_remedios_marca()}")
print(f"Valor de todos os remedios: {farmacia.calcular_valor_todos_remedios()}")
