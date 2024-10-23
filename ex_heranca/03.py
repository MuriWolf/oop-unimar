class Pessoa:
    def __init__(self, nome: str, endereco: str, telefone: str) -> None:
     self.nome = nome
     self.endereco = endereco
     self.telefone = telefone

class Fornecedor(Pessoa):
    def __init__(self, nome: str, endereco: str, telefone: str, valor_credito: float, valor_divida: float) -> None:
       super().__init__(nome, endereco, telefone)
       self.valor_credito = valor_credito
       self.valor_divida = valor_divida

    def obter_saldo(self):
        return self.valor_credito - self.valor_divida

class Empregado(Pessoa):
    def __init__(self, nome: str, endereco: str, telefone: str, codigo_setor: int, salario_base: float, imposto: float) -> None:
       super().__init__(nome, endereco, telefone)
       self.codigo_setor = codigo_setor
       self.salario_base = salario_base
       self.imposto = imposto

    def retornar_salario_liquido(self):
        return self.salario_base * (1 - self.imposto)

class Administrador(Empregado):
    def __init__(self, nome: str, endereco: str, telefone: str, codigo_setor: int, salario_base: float, imposto: float, ajuda_de_custo: float) -> None:
       super().__init__(nome, endereco, telefone, codigo_setor, salario_base, imposto)
       self.ajuda_de_custo = ajuda_de_custo

    def retornar_salario_liquido(self):
        return (self.salario_base + self.ajuda_de_custo) * (1 - self.imposto)

class Vendedor(Empregado):
    def __init__(self, nome: str, endereco: str, telefone: str, codigo_setor: int, salario_base: float, imposto: float, valor_de_vendas: float, comissao: float) -> None:
        super().__init__(nome, endereco, telefone, codigo_setor, salario_base, imposto)
        self.valor_de_vendas = valor_de_vendas
        self.comissao = comissao

    def retornar_salario_liquido(self):
        return (self.salario_base + (self.valor_de_vendas * self.comissao)) * (1 - self.imposto)

