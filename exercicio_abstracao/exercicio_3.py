# Exercício 3: Veículos


from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def frear(self):
        pass

class Carro(Veiculo):
    def acelerar(self):
        return "Carro acelerando"

    def frear(self):
        return "Carro freando"

class Moto(Veiculo):
    def acelerar(self):
        return "Moto acelerando"

    def frear(self):
        return "Moto freando"

class Caminhao(Veiculo):
    def acelerar(self):
        return "Caminhão acelerando"

    def frear(self):
        return "Caminhão freando"

# Exemplo de uso
carro = Carro()
moto = Moto()
caminhao = Caminhao()

print(carro.acelerar())
print(carro.frear())

print(moto.acelerar())
print(moto.frear())

print(caminhao.acelerar())
print(caminhao.frear())