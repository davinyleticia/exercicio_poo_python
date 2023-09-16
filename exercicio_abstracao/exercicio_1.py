# Exercício 1: Figuras Geométricas


from abc import ABC, abstractmethod
import math

class FiguraGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Retangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio ** 2

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

# Exemplo de uso
retangulo = Retangulo(5, 10)
circulo = Circulo(3)
triangulo = Triangulo(4, 6)

print(f"\nÁrea do Retângulo: {retangulo.calcular_area()}")
print(f"Área do Círculo: {circulo.calcular_area()}")
print(f"Área do Triângulo: {triangulo.calcular_area()}")