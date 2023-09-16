# Exercício 1: Catálogo de Produtos

class Produto:
    def __init__(self, nome, preco):
        self._nome = nome   # Atributo protegido
        self._preco = preco # Atributo protegido

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_preco(self):
        return self._preco

    def set_preco(self, preco):
        if preco >= 0:
            self._preco = preco

    def __str__(self):
        return f"Produto: {self._nome}, Preço: R${self._preco:.2f}"

# Exemplo de uso
produto1 = Produto("Camiseta", 29.99)
print(produto1)
produto1.set_preco(24.99)
print(produto1)