from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia_entrega: float, peso: float, prioridade: bool) -> None:
        self.distancia_entrega = distancia_entrega
        self.peso = peso
        self.prioridade = prioridade
        self.tipo_transporte = "transporte"

    @abstractmethod
    def calcular_custo_total(self) -> float:
        pass 

    @abstractmethod
    def calcular_tempo_estimado_entrega(self):
        pass

    def exibir_detalhes(self) -> str:
        return f"""
tipo transporte: {self.tipo_transporte}
distancia: {self.distancia_entrega} km
peso: {self.peso} kg
custo total: R$ {self.calcular_custo_total():.2f}
prioridade: {self.prioridade}
tempo estimado de entrega: {self.calcular_tempo_estimado_entrega():.1f} horas
"""

class Rodoviario(Transporte):
    def __init__(self, distancia_entrega: float, peso: float, prioridade: bool) -> None:
        super().__init__(distancia_entrega, peso, prioridade)
        self.tipo_transporte = "rodoviario"

    def calcular_custo_total(self) -> float:
        tarifa_distancia = 5
        tarifa_peso = 0.1
        custo_total = self.distancia_entrega * (1 + tarifa_distancia) + self.peso * (1 + tarifa_peso)

        pedagio = 0.05 * self.peso
        seguro = self.distancia_entrega % 100

        custo_total += pedagio + seguro 

        if (self.prioridade):
            custo_total *= 1.25

        return custo_total
    
    def calcular_tempo_estimado_entrega(self):
        # tempo em horas km/(km/h)
        return self.distancia_entrega / (60 * 1.3) if self.prioridade else self.distancia_entrega / 60

class Aereo(Transporte):
    def __init__(self, distancia_entrega: float, peso: float, prioridade: bool) -> None:
        super().__init__(distancia_entrega, peso, prioridade)
        self.tipo_transporte = "aereo"

    def calcular_custo_total(self) -> float:
        tarifa_distancia = 10
        tarifa_peso = 0.25
        custo_total = self.distancia_entrega * (1 + tarifa_distancia) + self.peso * (1 + tarifa_peso)

        pedagio = 0.05 * self.peso
        seguro = self.distancia_entrega % 100

        custo_total += pedagio + seguro 

        if (self.prioridade):
            custo_total *= 1.5

        return custo_total
    
    def calcular_tempo_estimado_entrega(self):
        # tempo em horas km/(km/h)
        return self.distancia_entrega / (800 * 1.2) if self.prioridade else self.distancia_entrega / 800
    
class Maritimo(Transporte):
    def __init__(self, distancia_entrega: float, peso: float, prioridade: bool) -> None:
        super().__init__(distancia_entrega, peso, prioridade)
        self.tipo_transporte = "maritimo"

    def calcular_custo_total(self) -> float:
        tarifa_distancia = 2
        tarifa_peso = 0.05
        custo_total = self.distancia_entrega * (1 + tarifa_distancia) + self.peso * (1 + tarifa_peso)

        pedagio = 0.05 * self.peso
        seguro = self.distancia_entrega % 100

        custo_total += pedagio + seguro 

        if (self.prioridade):
            custo_total *= 1.75

        return custo_total
    
    def calcular_tempo_estimado_entrega(self):
        # tempo em horas km/(km/h)
        return self.distancia_entrega / (30 * 1.5) if self.prioridade else self.distancia_entrega / 30
    
rodoviario01 = Rodoviario(distancia_entrega=450, peso=25, prioridade=True)
rodoviario02 = Rodoviario(distancia_entrega=450, peso=25, prioridade=False)

print(rodoviario01.exibir_detalhes())
print(rodoviario02.exibir_detalhes())

aereo01 = Aereo(distancia_entrega=2200, peso=50, prioridade=True)
aereo02 = Aereo(distancia_entrega=2200, peso=50, prioridade=False)

print(aereo01.exibir_detalhes())
print(aereo02.exibir_detalhes())

maritimo01 = Maritimo(distancia_entrega=4000, peso=300, prioridade=True)
maritimo02 = Maritimo(distancia_entrega=4000, peso=300, prioridade=False)

print(maritimo01.exibir_detalhes())
print(maritimo02.exibir_detalhes())