from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome: str, salario: float) -> None:
        self.nome = nome
        self.salario = salario

    @abstractmethod
    def calcular_desempenho(self) -> int:
        # deve retornar: [1, 100]
        pass

    @abstractmethod
    def calcular_bonus_salario(self) -> float:
        return 0.05
    
class FuncionarioVendas(Funcionario):
    def __init__(self, nome: str, salario: float, volume_vendas: int, meta_vendas: int) -> None:
        super().__init__(nome, salario)
        self.volume_vendas = volume_vendas
        self.meta_vendas = meta_vendas

    def calcular_desempenho(self) -> int:
        if self.volume_vendas > self.meta_vendas:
            return 100
        else:
            return int((self.volume_vendas / self.meta_vendas) * 100) 

    def calcular_bonus_salario(self) -> float:
        return 0.1 if self.calcular_desempenho() > 50 else super().calcular_bonus_salario()            

class FuncionarioTecnologia(Funcionario):
    def __init__(self, nome: str, salario: float, prazos_cumpridos: bool) -> None:
        super().__init__(nome, salario)
        self.prazos_cumpridos = prazos_cumpridos

    def calcular_desempenho(self) -> int:
        return 100 if self.prazos_cumpridos else 0 
        
    def calcular_bonus_salario(self) -> float:
        return 0.09 if self.calcular_desempenho() == 100 else super().calcular_bonus_salario()

class FuncionarioAdministrativo(Funcionario):
    def __init__(self, nome: str, salario: float, nota_avaliacao_anual: bool) -> None:
        super().__init__(nome, salario)
        self.nota_avaliacao_anual = nota_avaliacao_anual

    def calcular_desempenho(self) -> int:
        return self.nota_avaliacao_anual
        
    def calcular_bonus_salario(self) -> float:
        return 0.08 if self.calcular_desempenho() >= 70 else super().calcular_bonus_salario()
    
class Empresa:
    def __init__(self) -> None:
        pass

    def avaliar_funcionarios(self, funcionarios: list[Funcionario]):
        avaliacoes = [{}] * len(funcionarios)
        for index, funcionario in enumerate(funcionarios):
            dados = {'nome': funcionario.nome, 'desempenho': funcionario.calcular_desempenho(), 'bonus-salario': funcionario.calcular_bonus_salario()}
            avaliacoes[index] = dados
        return avaliacoes
    
funcionarioVendas01 = FuncionarioVendas(nome="Jose", salario=2000, volume_vendas=39, meta_vendas=49)
funcionarioTecnologia01 = FuncionarioTecnologia(nome="Maria", salario=3500, prazos_cumpridos=True)
funcionarioTecnologia02 = FuncionarioTecnologia(nome="Luiz", salario=4000, prazos_cumpridos=False)
funcionarioAdm01 = FuncionarioAdministrativo(nome="Joao", salario=5000, nota_avaliacao_anual=78)
funcionarioAdm02 = FuncionarioAdministrativo(nome="Roberto", salario=1400, nota_avaliacao_anual=53)
funcionarios = [funcionarioAdm01, funcionarioAdm02, funcionarioTecnologia01, funcionarioTecnologia02, funcionarioVendas01]

empresa = Empresa()
avaliacoes = empresa.avaliar_funcionarios(funcionarios) 

for avaliacao in avaliacoes:
    print(f"Nome: {avaliacao['nome']}, desempenho: {avaliacao['desempenho']}, bonus salario: {int(avaliacao['bonus-salario'] * 100)}%") 