from abc import ABC, abstractmethod

class Produto(ABC):
    def __init__(self, nome: str, preco: float) -> None:
        super().__init__()
        self.nome = nome
        self.preco = preco
    
    @abstractmethod
    def calcular_preco(self) -> float:
        pass

class Livro(Produto):
    def __init__(self, nome: str, preco: float) -> None:
        super().__init__(nome, preco)

    def calcular_preco(self) -> float:
        return self.preco * 0.9 

class Eletronico(Produto):
    def __init__(self, nome: str, preco: float) -> None:
        super().__init__(nome, preco)

    def calcular_preco(self) -> float:
        return self.preco * 1.15

class Roupa(Produto):
    def __init__(self, nome: str, preco: float, importada: bool, estacao: bool) -> None:
        super().__init__(nome, preco)
        self.importada = importada
        self.estacao = estacao

    def calcular_preco(self) -> float:
        taxa = 0
        if self.importada:
            taxa += 0.05
        if self.estacao:
            taxa -= 0.2

        return self.preco * (1 + taxa)

class Carrinho:
    def __init__(self) -> None:
        self.produtos: list[Produto] = []
    
    def adicionar_produto(self, produto: Produto):
        self.produtos.append(produto)

    def calcular_valor_total(self):
        return sum(produto.calcular_preco() for produto in self.produtos)

livro = Livro(nome="A república - Platão", preco=60)
eletronico = Eletronico(nome="microondas Ultra", preco=400)
roupa = Roupa(nome="King t-shirt", preco=74, estacao=True, importada=True)

carrinho = Carrinho()

carrinho.adicionar_produto(livro)
carrinho.adicionar_produto(eletronico)
carrinho.adicionar_produto(roupa)

print(f"preco total do carrinho R$ {carrinho.calcular_valor_total():.2f}")
