from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, salario=0):
        self.nome = nome
        self.salario = salario

    @abstractmethod
    def calcular_pagamento(self):
        pass

class FuncionarioTemporario(Funcionario):
    def __init__(self, nome, salario_por_hora, horas_trabalhadas):
        super().__init__(nome)
        self.salario_por_hora = salario_por_hora
        self.horas_trabalhadas = horas_trabalhadas

    def calcular_pagamento(self):
        return self.salario_por_hora * self.horas_trabalhadas

class FuncionarioIntegral(Funcionario):
    def __init__(self, nome, salario_mensal):
        super().__init__(nome, salario_mensal)

    def calcular_pagamento(self):
        return self.salario

# Criar instâncias de FuncionarioTemporario e FuncionarioIntegral
temporario = FuncionarioTemporario("João", 15.0, 40)
integral = FuncionarioIntegral("Maria", 3000.0)

# Calcular e imprimir o pagamento de cada funcionário
print(f"Salário de {temporario.nome}: R${temporario.calcular_pagamento()}")
print(f"Salário de {integral.nome}: R${integral.calcular_pagamento()}")