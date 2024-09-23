from datetime import datetime, timedelta

class Projeto:
    def __init__(self, nome_projeto: str, data_inicio: datetime) -> None:
        self.nome_projeto = nome_projeto
        self.data_inicio = data_inicio
        self.membros: list['Membro'] = []

    def exibir_detalhes(self) -> None:
        print("Detalhes do projeto: ")
        print(f"- Nome: {self.nome_projeto}")
        print(f"- Data inicio: {self.data_inicio}")
        print(f"- Membros:")
        for membro in self.membros:
            print(f"nome: {membro.nome}, email: {membro.email}")

    # TODO: permitir a entrada de uma list de membros
    def adicionar_membro(self, novo_membro: 'Membro') -> None:
        self.membros.append(novo_membro)

    def calcular_duracao(self, data_final: datetime):
        return (data_final - self.data_inicio).days()

class Membro:
    def __init__(self, nome: str, email: str) -> None:
        self.nome = nome
        self.email = email

projeto_01: Projeto = Projeto("Site de vendas", datetime.now())

membro_01: Membro = Membro("Joao", "joao@hotmail")
membro_02: Membro = Membro("Lucas Palmito", "palmito@hotmail")

projeto_01.adicionar_membro(membro_01)
projeto_01.adicionar_membro(membro_02)

projeto_01.exibir_detalhes()

print(projeto_01.calcular_duracao(datetime(2025, 2, 2)))