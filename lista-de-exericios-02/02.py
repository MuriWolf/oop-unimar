class Cliente:
    def __init__(self, nome: str, endereco: str, restaurantes_favoritos: list[str]) -> None:
        self.nome = nome
        self.endereco = endereco
        self.restaurantes_favoritos = restaurantes_favoritos

    def adicionar_restaurante_favorito(self, nome_restaurante: str):
        self.restaurantes_favoritos.append(nome_restaurante)


class Pedido:
    def __init__(self, cliente: Cliente, itens: dict) -> None:
        self.cliente = cliente 
        self.itens = itens

    def calcular_valor_total(self):
        total: float = 0.0
        for item in self.itens:
            print(item)
            total = total + item

        return total 

    def exibir_detalhes(self):
        print(f"\nnome cliente: {self.cliente.nome}")
        print(f"endereco cliente: {self.cliente.endereco}")
        print("itens do pedido: ")
        for nome, valor in self.itens.items():
            print(f"{nome}, {valor} reais")

class Restaurante:
    def __init__(self, nome_estabelecimento: str, pedidos: list[Pedido]) -> None:
        self.nome_estabelecimento = nome_estabelecimento
        self.pedidos = pedidos

    def adicionar_pedido(self, pedido: Pedido):
        self.pedidos.append(pedido)

cliente_01: Cliente = Cliente("Jao do Pe", "Rua Maracuja, Bahia", ["Pe de Fava", "Ratao foods"])

pedido_01: Pedido = Pedido(cliente_01, {"lanche": 25, "refri": 7, "batata-frita": 20})

pedido_01.exibir_detalhes()

print(f"\nvalor total pedido: {pedido_01.calcular_valor_total} reais")

print("\nrestaurantes favoritos do cliente:")
for restaurante in cliente_01.restaurantes_favoritos:
    print(restaurante)