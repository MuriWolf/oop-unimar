class Conta:
    def __init__(self, valor_conta: float, quantidade_pessoas: int, pagar_gorjeta: bool) -> None:
        self.valor_conta = valor_conta
        self.quantidade_pessoas = quantidade_pessoas if quantidade_pessoas > 0 else 1
        self.pagar_gorjeta = pagar_gorjeta

    def retornar_valor_total_a_ser_pago(self) -> float:
        if self.pagar_gorjeta:
            return self.valor_conta * 1.1
        else:
            return self.valor_conta

    def retornar_valor_pessoa_a_ser_pago(self) -> float:
        return self.retornar_valor_total_a_ser_pago() / self.quantidade_pessoas

contas: list[Conta] = [Conta(1000.0, 5, False), Conta(500, 2, True)]

for conta in contas:
    print(f"""
Total a ser pago: {conta.retornar_valor_total_a_ser_pago()}
Por pessoa: {conta.retornar_valor_pessoa_a_ser_pago()}
{'Gorgeta paga, garçom -> :)' if conta.pagar_gorjeta else 'Gorgeta não paga, garçom -> :('}
""")
