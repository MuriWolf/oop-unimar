import datetime

class Tarefa:
    def __init__(self, descricao: str, status: bool) -> None:
        self.descricao = descricao
        self.status = status
        self.data_criacao = datetime.datetime.now()
        self.data_conclusao: datetime = None

    def concluir(self, status: bool) -> None:
        if status:
            self.data_conclusao = datetime.datetime.now()
        else:
            self.data_conclusao = None
        self.status = status

    def exibir_detalhes(self) -> str:
        return f"Descricao: {self.descricao}\nStatus: {self.status}\nData de criacao: {self.data_criacao}\nData conclusao: {self.data_conclusao}"

    def verificar_atraso(self, prazo_limite: datetime) -> bool:
        return datetime.datetime.now() > prazo_limite and self.status == False
    
tarefa1: Tarefa = Tarefa(descricao="Fazer o almoco", status=False)
tarefa1.concluir(True)
print(tarefa1.verificar_atraso(datetime.datetime(year=2024, month=9, day=23, hour=13, minute=10)))

print(tarefa1.exibir_detalhes())