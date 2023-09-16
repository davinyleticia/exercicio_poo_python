# Exercício 3: Banco de Dados de Funcionários

class Funcionario:
    def __init__(self, nome, cargo):
        self._nome = nome   # Atributo protegido
        self._cargo = cargo # Atributo protegido

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_cargo(self):
        return self._cargo

    def set_cargo(self, cargo):
        self._cargo = cargo

    def __str__(self):
        return f"Nome: {self._nome}, Cargo: {self._cargo}"

# Exemplo de uso
funcionario1 = Funcionario("João", "Analista")
print(funcionario1)
funcionario1.set_cargo("Gerente")
print(funcionario1)