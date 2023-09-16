#Exercício 5: Formas de Pagamento


from abc import ABC, abstractmethod

class FormaPagamento(ABC):
    @abstractmethod
    def calcular_desconto(self, valor):
        pass

    @abstractmethod
    def calcular_parcelas(self, valor, numero_parcelas):
        pass

class CartaoCredito(FormaPagamento):
    def calcular_desconto(self, valor):
        return valor * 0.05

    def calcular_parcelas(self, valor, numero_parcelas):
        return valor / numero_parcelas

class Boleto(FormaPagamento):
    def calcular_desconto(self, valor):
        return valor * 0.03

    def calcular_parcelas(self, valor, numero_parcelas):
        return valor / numero_parcelas

class Transferencia(FormaPagamento):
    def calcular_desconto(self, valor):
        return valor * 0.02

    def calcular_parcelas(self, valor, numero_parcelas):
        return valor / numero_parcelas

# Exemplo de uso
cartao = CartaoCredito()
boleto = Boleto()
transferencia = Transferencia()

valor_compra = 1000.0
numero_parcelas = 3

desconto_cartao = cartao.calcular_desconto(valor_compra)
parcelas_cartao = cartao.calcular_parcelas(valor_compra, numero_parcelas)

desconto_boleto = boleto.calcular_desconto(valor_compra)
parcelas_boleto = boleto.calcular_parcelas(valor_compra, numero_parcelas)

desconto_transferencia = transferencia.calcular_desconto(valor_compra)
parcelas_transferencia = transferencia.calcular_parcelas(valor_compra, numero_parcelas)

print("Pagamento com Cartão de Crédito:")
print(f"Desconto: R${desconto_cartao:.2f}")
print(f"Parcelas de R${parcelas_cartao:.2f} cada")

print("\nPagamento com Boleto:")
print(f"Desconto: R${desconto_boleto:.2f}")
print(f"Parcelas de R${parcelas_boleto:.2f} cada")

print("\nPagamento com Transferência:")
print(f"Desconto: R${desconto_transferencia:.2f}")
print(f"Parcelas de R${parcelas_transferencia:.2f} cada")