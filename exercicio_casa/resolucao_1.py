class Veiculo:
    def __init__(self, modelo, ano, preco):
        self.modelo = modelo
        self.ano = ano
        self.preco = preco

    def calcular_imposto(self):
        return 0.10 * self.preco

class Carro(Veiculo):
    def __init__(self, modelo, ano, preco, marca):
        super().__init__(modelo, ano, preco)
        self.marca = marca

    def desconto(self):
        return 0.05 * self.preco

class Moto(Veiculo):
    def __init__(self, modelo, ano, preco, cilindrada):
        super().__init__(modelo, ano, preco)
        self.cilindrada = cilindrada

    def calcular_imposto(self):
        return 0.05 * self.preco

# Criar instâncias de Carro e Moto
carro = Carro("Toyota Corolla", 2022, 60000.0, "Toyota")
moto = Moto("Honda CBR", 2021, 12000.0, 600)

# Calcular e imprimir o imposto a ser pago por cada veículo
print(f"Imposto do carro: R${carro.calcular_imposto()}")
print(f"Imposto da moto: R${moto.calcular_imposto()}")