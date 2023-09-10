# exercício 1 - Conta Bancaria

class ContaBancaria:
    def __init__(self, numero_conta, titular_conta):
        self.numero_conta = numero_conta
        self.titular_conta = titular_conta
        self.saldo = 0.0 # saldo inicial definido com 0.0
    
    def depositar(self, valor):
        if valor > 0:
            text = f'Valor depositado de R${valor}, realizado com sucesso.'
            self.saldo =+ valor   # self.saldo = self.saldo + valor
            print(text)
        else:
            print('O valor do depósito deve ser maior que 0')
        
    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f'Saque de R${valor} realizado com sucesso')
            else: 
                print("saldo insuficiente para realizar o saque")
        else:
            print("O valor do saque deve ser maior que zero.")
            

contaDaviny = ContaBancaria(202301, "Daviny Letícia")

contaDaviny.depositar(100)

contaDaviny.sacar(10)

print(contaDaviny.saldo)

contaLais = ContaBancaria(202302, "Lais")

contaLais.depositar(80)

contaLais.sacar(1000)