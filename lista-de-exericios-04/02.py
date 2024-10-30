from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, modelo: str, ano: int) -> None:
        self.modelo = modelo
        self.ano = ano

    @abstractmethod
    def frear(self) -> str:
        pass

    @abstractmethod
    def acelerar(self) -> str:
        pass

class Carro(Veiculo):
    def __init__(self, modelo: str, ano: int) -> None:
        super().__init__(modelo, ano)

    def frear(self):
        return "Freando com o carro."

    def acelerar(self) -> str:
        return "acelerando com o carro."


class Moto(Veiculo):
    def __init__(self, modelo: str, ano: int) -> None:
        super().__init__(modelo, ano)

    def frear(self):
        return "Freando com a moto."

    def acelerar(self) -> str:
        return "acelerando com a moto."

class Caminhao(Veiculo):
    def __init__(self, modelo: str, ano: int) -> None:
        super().__init__(modelo, ano)

    def frear(self):
        return "Freando com o caminhao."

    def acelerar(self) -> str:
        return "acelerando com o caminhao."

carro = Carro(modelo="ford", ano=2010)
print(carro.acelerar())
print(carro.frear())

moto = Moto(modelo="X1", ano=2011)
print(moto.acelerar())
print(moto.frear())

caminhao = Caminhao(modelo="ford", ano=2010)
print(caminhao.acelerar())
print(caminhao.frear())
