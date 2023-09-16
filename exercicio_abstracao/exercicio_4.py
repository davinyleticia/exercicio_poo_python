#Exercício 4: Produtos


from abc import ABC, abstractmethod

class Produto(ABC):
    @abstractmethod
    def calcular_preco(self):
        pass

    @abstractmethod
    def descricao(self):
        pass

class Livro(Produto):
    def __init__(self, titulo, autor, preco):
        self.titulo = titulo
        self.autor = autor
        self.preco = preco

    def calcular_preco(self):
        return self.preco

    def descricao(self):
        return f"Livro: {self.titulo}, Autor: {self.autor}"

class Eletronico(Produto):
    def __init__(self, nome, preco, marca):
        self.nome = nome
        self.preco = preco
        self.marca = marca

    def calcular_preco(self):
        return self.preco

    def descricao(self):
        return f"Eletrônico: {self.nome}, Marca: {self.marca}"

class Alimento(Produto):
    def __init__(self, nome, preco, data_validade):
        self.nome = nome
        self.preco = preco
        self.data_validade = data_validade

    def calcular_preco(self):
        return self.preco

    def descricao(self):
        return f"Alimento: {self.nome}, Data de Validade: {self.data_validade}"

# Exemplo de uso
livro = Livro("\nO Senhor dos Anéis", "J.R.R. Tolkien", 49.99)
eletronico = Eletronico("\nSmartphone", 999.99, "Samsung")
alimento = Alimento("\nMaçã", 2.50, "2023-09-30")

print(livro.descricao())
print(f"\nPreço: R${livro.calcular_preco():.2f}")

print(eletronico.descricao())
print(f"\nPreço: R${eletronico.calcular_preco():.2f}")

print(alimento.descricao())
print(f"\nPreço: R${alimento.calcular_preco():.2f}")