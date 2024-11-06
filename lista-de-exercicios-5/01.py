from abc import ABC, abstractmethod

class Contribuinte(ABC):
    def __init__(self, nome: str) -> None:
        self.nome = nome

    @abstractmethod
    def calcular_valor_imposto(self, renda_bruta: float) -> float:
        pass

class PessoaJuridica(Contribuinte):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)

    def calcular_valor_imposto(self, renda_bruta: float) -> float:
        return renda_bruta * 0.1

class PessoaFisica(Contribuinte):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)

    def calcular_valor_imposto(self, renda_bruta: float) -> float:
        aliquota = 0
        parcela_deduzir = 0

        if renda_bruta <= 1400:
           pass
        elif renda_bruta <= 2100:
            aliquota = 0.1
            parcela_deduzir = 100
        elif renda_bruta <= 2800:
            aliquota = 0.15
            parcela_deduzir = 270
        elif renda_bruta <= 3600:
            aliquota = 0.25
            parcela_deduzir = 500
        else:
            aliquota = 0.3
            parcela_deduzir = 700

        return renda_bruta * aliquota - parcela_deduzir

fisica = PessoaFisica("Junior")
juridica = PessoaJuridica("luiz")

print(f"Valor de IR a ser pago (pessoa fisica): {fisica.calcular_valor_imposto(2500)}")
print(f"Valor de IR a ser pago (pessoa fisica): {fisica.calcular_valor_imposto(1500)}")
print(f"Valor de IR a ser pago (pessoa fisica): {fisica.calcular_valor_imposto(4000)}")

print(f"\nValor de IR a ser pago (pessoa juridica): {juridica.calcular_valor_imposto(2000)}")
print(f"Valor de IR a ser pago (pessoa juridica): {juridica.calcular_valor_imposto(4000)}")
print(f"Valor de IR a ser pago (pessoa juridica): {juridica.calcular_valor_imposto(2500)}")
