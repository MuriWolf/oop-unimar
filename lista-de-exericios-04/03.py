from abc import ABC, abstractmethod

class Acomodacao(ABC):
    def __init__(self, nome_acomocadao: str, preco_basico_dia: float, dias_reservados: int) -> None:
        self.nome_acomocadao = nome_acomocadao
        self.preco_basico_dia = preco_basico_dia
        self.dias_reservados = dias_reservados
        self.servicos_extras = []

    def adicionar_servico_extra(self, nome: str, custo: float):
        self.servicos_extras.append({"nome": nome, "custo": custo})
 
    def calcular_custo_servico_extra(self):
        total = 0
        for servico in self.servicos_extras:
            total += servico["custo"]

        return total
    
    @abstractmethod
    def calcular_preco_total_estadia(self) -> float:
        return self.preco_basico_dia * self.dias_reservados

    @abstractmethod
    def exibir_detalhes_acomocadao(self) -> str:
        return f"\n\nnome: {self.nome_acomocadao}\npreco basico/dia: {self.preco_basico_dia}\ndias reservados: {self.dias_reservados}" 

class Hotel(Acomodacao):
    def __init__(self, nome_acomocadao: str, preco_basico_dia: float, dias_reservados: int) -> None:
        super().__init__(nome_acomocadao, preco_basico_dia, dias_reservados)

    def calcular_preco_total_estadia(self) -> float:
        preco_base = super().calcular_preco_total_estadia()
        preco_com_taxas = preco_base * 1.15 + self.calcular_custo_servico_extra()

        return preco_com_taxas

    def exibir_detalhes_acomocadao(self) -> str:
        mensagem = super().exibir_detalhes_acomocadao() + "\ntomar cafe da manha: sim"
        for servico in self.servicos_extras:
            mensagem += f"\n{servico["nome"]}"

        return mensagem

class Apartamento(Acomodacao):
    def __init__(self, nome_acomocadao: str, preco_basico_dia: float, dias_reservados: int) -> None:
        super().__init__(nome_acomocadao, preco_basico_dia, dias_reservados)

    def calcular_preco_total_estadia(self) -> float:
        preco_base = super().calcular_preco_total_estadia()
        preco_com_taxas = preco_base + 150 + self.calcular_custo_servico_extra()

        return preco_com_taxas

    def exibir_detalhes_acomocadao(self) -> str:
        mensagem = super().exibir_detalhes_acomocadao() + "\nlevar animal de estimacao: sim"
        for servico in self.servicos_extras:
            mensagem += f"\n{servico["nome"]}"

        return mensagem

class Pousada(Acomodacao):
    def __init__(self, nome_acomocadao: str, preco_basico_dia: float, dias_reservados: int) -> None:
        super().__init__(nome_acomocadao, preco_basico_dia, dias_reservados)

    def calcular_preco_total_estadia(self) -> float:
        preco_base = super().calcular_preco_total_estadia()
        # 1.30 pois são duas taxas: 100% + 15% + 15%
        preco_com_taxas = preco_base * 1.30 + self.calcular_custo_servico_extra()

        return preco_com_taxas

    def exibir_detalhes_acomocadao(self) -> str:
        mensagem = super().exibir_detalhes_acomocadao() + "\ntomar cafe da manha: sim" + "\ntomar cafe da manha: sim"
        for servico in self.servicos_extras:
            mensagem += f"\n{servico["nome"]}:"

        return mensagem

hotel = Hotel(nome_acomocadao="hotel lala", dias_reservados=6, preco_basico_dia=100)
hotel.adicionar_servico_extra(nome="servico de quarto", custo=50)
hotel.adicionar_servico_extra(nome="janta", custo=100)

print(hotel.exibir_detalhes_acomocadao())
print(f"\npreco total estadia: {hotel.calcular_preco_total_estadia()}")

apartamento = Apartamento(nome_acomocadao="apartamento xiu xin", dias_reservados=20, preco_basico_dia=300)

print(apartamento.exibir_detalhes_acomocadao())
print(f"\npreco total estadia: {apartamento.calcular_preco_total_estadia()}")


pousada = Pousada(nome_acomocadao="pousada burning hot", dias_reservados=12, preco_basico_dia=666)
pousada.adicionar_servico_extra(nome="piscina", custo=190)

print(pousada.exibir_detalhes_acomocadao())
print(f"\npreco total estadia: {pousada.calcular_preco_total_estadia()}")