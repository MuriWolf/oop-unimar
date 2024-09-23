class Cliente:
    def __init__(self, nome: str, endereco: str, restaurantes_favoritos: list['Restaurante']) -> None:
        self.nome = nome
        self.endereco = endereco
        self.restaurantes_favoritos = restaurantes_favoritos

    def adicionar_restaurante_favorito(self, nome_restaurante: str):
        self.restaurantes_favoritos.append(nome_restaurante)


class Pedido:
    def __init__(self, cliente: Cliente, itens: dict[str, float]) -> None:
        self.cliente = cliente 
        self.itens = itens

    def calcular_valor_total(self) -> float:
        total: float = 0
        for nome, valor in self.itens.items():
            total = total + valor 

        return total 

    def exibir_detalhes(self) -> None:
        print(f"\nnome cliente: {self.cliente.nome}")
        print(f"endereco cliente: {self.cliente.endereco}")
        print("\nitens do pedido: ")
        for nome, valor in self.itens.items():
            print(f"{nome}, {valor} reais")

class Restaurante:
    def __init__(self, nome_estabelecimento: str) -> None:
        self.nome_estabelecimento = nome_estabelecimento
        self.pedidos: list[Pedido] = [] 

    def adicionar_pedido(self, pedido: Pedido) -> None:
        self.pedidos.append(pedido)


restaurante_01: Restaurante = Restaurante("Pe de Fava")
restaurante_02: Restaurante = Restaurante("Ratao Lanches")

cliente_01: Cliente = Cliente("Jao do Pe", "Rua Maracuja, Bahia", [restaurante_01] )
cliente_01.adicionar_restaurante_favorito(restaurante_02)

pedido_01: Pedido = Pedido(cliente_01, {"lanche": 25, "refri": 7, "batata-frita": 20})

pedido_01.exibir_detalhes()

print(f"\nvalor total pedido: {pedido_01.calcular_valor_total()} reais")

print("\nrestaurantes favoritos do cliente:")
for restaurante in cliente_01.restaurantes_favoritos:
    print(restaurante.nome_estabelecimento)
