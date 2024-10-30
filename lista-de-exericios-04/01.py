from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def processar_pagamento(self, valor: float) -> str:
        pass

class PagamentoCartao(Pagamento):
    def processar_pagamento(self, valor: float) -> str:
        return f"pagando no cartao o valor de {valor}" 

class PagamentoBoleto(Pagamento):
    def processar_pagamento(self, valor: float) -> str:
        return f"pagando no boleto o valor de {valor}" 

cartao = PagamentoCartao()
boleto = PagamentoBoleto()

print(cartao.processar_pagamento(100.50))

print(boleto.processar_pagamento(300))
