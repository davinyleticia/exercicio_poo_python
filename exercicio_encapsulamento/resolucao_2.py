# Exercício 2: Biblioteca

class Livro:
    def __init__(self, titulo, autor):
        self._titulo = titulo    # Atributo protegido
        self._autor = autor      # Atributo protegido
        self._disponivel = True  # Atributo protegido (inicialmente disponível)

    def emprestar(self):
        if self._disponivel:
            self._disponivel = False
            return "Livro emprestado com sucesso!"
        else:
            return "Livro já emprestado."

    def devolver(self):
        if not self._disponivel:
            self._disponivel = True
            return "Livro devolvido com sucesso!"
        else:
            return "Livro já está disponível."

    def __str__(self):
        status = "disponível" if self._disponivel else "emprestado"
        return f"Título: {self._titulo}, Autor: {self._autor}, Status: {status}"

# Exemplo de uso
livro1 = Livro("Harry Potter", "J.K. Rowling")
print(livro1)
print(livro1.emprestar())
print(livro1.devolver())