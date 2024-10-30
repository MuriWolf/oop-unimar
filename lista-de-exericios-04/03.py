from abc import ABC, abstractmethod

class Acomodacao(ABC):
    def __init__(self, nome_acomocadao: str, preco_basico_dia: float, dias_reservados: int) -> None:
        self.nome_acomocadao = nome_acomocadao
        self.preco_basico_dia = preco_basico_dia
        self.dias_reservados = dias_reservados

    @abstractmethod
    def calcular_preco_total_estadia(self) -> float:
        return self.preco_basico_dia * self.dias_reservados

    @abstractmethod
    def exibir_detalhes_acomocadao(self) -> str:
        return f"\n\nnome: {self.nome_acomocadao}\npreco basico/dia: {self.preco_basico_dia}\ndias reservados: {self.dias_reservados}" 

class Hotel(Acomodacao):
    def __init__(self, nome_acomocadao: str, preco_basico_dia: float, dias_reservados: int, tomar_cafe_da_manha: bool) -> None:
        super().__init__(nome_acomocadao, preco_basico_dia, dias_reservados)
        self.tomar_cafe_da_manha = tomar_cafe_da_manha

    def calcular_preco_total_estadia(self) -> float:
        preco_estadia = super().calcular_preco_total_estadia()

        if self.tomar_cafe_da_manha:
            preco_estadia *= 1.15

        return preco_estadia

    def exibir_detalhes_acomocadao(self) -> str:
        detalhes = super().exibir_detalhes_acomocadao()

        if self.tomar_cafe_da_manha:
            detalhes += "\ntomar cafe da manha: sim"
        else:
            detalhes += "\ntomar cafe da manha: nao"

        return detalhes

class Apartamento(Acomodacao):
    def __init__(self, nome_acomocadao: str, preco_basico_dia: float, dias_reservados: int, levar_animal: bool) -> None:
        super().__init__(nome_acomocadao, preco_basico_dia, dias_reservados)
        self.levar_animal = levar_animal

    def calcular_preco_total_estadia(self) -> float:
        preco_estadia = super().calcular_preco_total_estadia()
        
        if self.levar_animal:
            preco_estadia += 150

        return preco_estadia

    def exibir_detalhes_acomocadao(self) -> str:
        detalhes = super().exibir_detalhes_acomocadao()

        if self.levar_animal:
            detalhes += "\nlevar animal de estimacao: sim"
        else:
            detalhes += "\nlevar animal de estimacao: nao"

        return detalhes

class Pousada(Acomodacao):
    def __init__(self, nome_acomocadao: str, preco_basico_dia: float, dias_reservados: int, tomar_cafe_da_manha: bool, levar_animal: bool) -> None:
        super().__init__(nome_acomocadao, preco_basico_dia, dias_reservados)
        self.tomar_cafe_da_manha = tomar_cafe_da_manha
        self.levar_animal = levar_animal


    def calcular_preco_total_estadia(self) -> float:
        preco_estadia = super().calcular_preco_total_estadia()

        if self.tomar_cafe_da_manha:
            preco_estadia *= 1.15

        return preco_estadia

    def exibir_detalhes_acomocadao(self) -> str:
        detalhes = super().exibir_detalhes_acomocadao()

        if self.tomar_cafe_da_manha:
            detalhes += "\ntomar cafe da manha: sim"
        else:
            detalhes += "\ntomar cafe da manha: nao"

        return detalhes
hotel = Hotel(nome_acomocadao="hotel lala", dias_reservados=6, preco_basico_dia=100, tomar_cafe_da_manha=True)

print(hotel.exibir_detalhes_acomocadao())
print(f"\npreco total estadia: {hotel.calcular_preco_total_estadia()}")

apartamento = Apartamento(nome_acomocadao="apartamento xiu xin", dias_reservados=20, preco_basico_dia=300, levar_animal=True)

print(apartamento.exibir_detalhes_acomocadao())
print(f"\npreco total estadia: {apartamento.calcular_preco_total_estadia()}")

