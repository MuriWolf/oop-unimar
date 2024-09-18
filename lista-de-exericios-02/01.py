import datetime

class Hospede:
    def __init__(self, nome: str, cpf: str, data_nascimento: datetime.datetime) -> None:
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

    def retornar_idade(self):
        return self.data_nascimento

class ReservaHotel:
    def __init__(self, hospede: Hospede, numero: int, custo_diaria: float, estadia: int):
        self.hospede = hospede
        self.numero = numero
        self.custo_diaria = custo_diaria
        self.estadia = estadia

    def calcular_valor_total(self) -> float:
        return self.custo_diaria * self.estadia
    
    def exibir_detalhes(self) -> dict:
        print(f'''
Detalhes da hospedagem:
nome ho hospede: {self.hospede.nome}      
numero quarto: {self.numero}
duracao estadia: {self.estadia}
        ''')


novo_hospede: Hospede = Hospede("Murillo", "2312312211", datetime.datetime(2002, 3, 7))
nova_reserva: ReservaHotel = ReservaHotel(novo_hospede, 2132, 150, 3)

print(f"Custo total da estadia: {nova_reserva.calcular_valor_total()} reais")

nova_reserva.exibir_detalhes()
