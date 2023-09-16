# Exercício 4: Agenda de Compromissos

class Compromisso:
    def __init__(self, data, descricao):
        self._data = data       # Atributo protegido
        self._descricao = descricao # Atributo protegido

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data

    def get_descricao(self):
        return self._descricao

    def set_descricao(self, descricao):
        self._descricao = descricao

    def __str__(self):
        return f"Data: {self._data}, Descrição: {self._descricao}"

# Exemplo de uso
compromisso1 = Compromisso("2023-09-10", "Reunião de equipe")
print(compromisso1)
compromisso1.set_descricao("Treinamento")
print(compromisso1)
