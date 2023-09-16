from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def emitir_som(self):
        pass

    @abstractmethod
    def mover(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Au Au"

    def mover(self):
        return "Correndo"

class Gato(Animal):
    def emitir_som(self):
        return "Miau"

    def mover(self):
        return "Andando"

class Pato(Animal):
    def emitir_som(self):
        return "Quack"

    def mover(self):
        return "Nadando"

# Exemplo de uso
cachorro = Cachorro()
gato = Gato()
pato = Pato()

print(f"\nCachorro faz: {cachorro.emitir_som()}, Movendo-se: {cachorro.mover()}")
print(f"Gato faz: {gato.emitir_som()}, Movendo-se: {gato.mover()}")
print(f"Pato faz: {pato.emitir_som()}, Movendo-se: {pato.mover()}")