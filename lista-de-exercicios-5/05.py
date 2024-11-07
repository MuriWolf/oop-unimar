from abc import ABC, abstractmethod 
import math

class Recurso:
    def __init__(self) -> None:
        pass

    @abstractmethod 
    def calcular_custo(self, dias: int) -> float:
        pass

class Humano(Recurso):
    def __init__(self, taxa_diaria: float) -> None:
        super().__init__()
        self.taxa_diaria = taxa_diaria

    def calcular_custo(self, dias: int) -> float:
        return dias * self.taxa_diaria
    
class Equipamento(Recurso):
    def __init__(self, taxa_diaria: float, custo_instalacao: float) -> None:
        super().__init__()
        self.taxa_diaria = taxa_diaria
        self.custo_instalacao = custo_instalacao

    def calcular_custo(self, dias: int) -> float:
        return dias * self.taxa_diaria + self.custo_instalacao

class LicencaSoftware(Recurso):
    def __init__(self, taxa_mensal: float) -> None:
        super().__init__()
        self.taxa_mensal = taxa_mensal

    def calcular_custo(self, dias: int) -> float:
        return math.ceil(dias / 30) * self.taxa_mensal
    
class Projeto():
    def __init__(self, recursos: list[Recurso]) -> None:
        self.recursos = recursos

    def calcular_custo_total(self, dias: int):
        total = 0
        for recurso in self.recursos:
            total += recurso.calcular_custo(dias)

        return total
    
humano01 = Humano(taxa_diaria=30)
equipamento01 = Equipamento(taxa_diaria=10, custo_instalacao=200)
licensaSoftware01 = LicencaSoftware(taxa_mensal=300)

projeto = Projeto(recursos=[humano01, equipamento01, licensaSoftware01])

print(f"Custo total do projeto: R${projeto.calcular_custo_total(dias=31)}")