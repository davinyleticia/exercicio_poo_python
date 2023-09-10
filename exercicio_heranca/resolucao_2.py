# exercício 2 - Produtos

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    def descricao(self):
        return f'nome: {self.nome}, Preço R$ {self.preco}'
    
class ProdutoFisico(Produto):
    def __init__(self, nome, preco, peso, dimensoes):
        super().__init__(nome, preco)
        self.peso = peso
        self.dimensoes = dimensoes
        
        
    def descricao(self):
        return super().descricao() + f", Peso: {self.peso} kg, Dimensões: {self.dimensoes} cm"
    
class ProdutoDigital(Produto):
    def __init__(self, nome, preco, tamanho_arquivo):
        super().__init__(nome,preco)
        self.tamanho_arquivo = tamanho_arquivo
        
    def descricao(self):
        return super().descricao() + f", Tamanho do Arquivo: {self.tamanho_arquivo} MB"
    
    
produto_fisico_darla = ProdutoFisico('livro', 30.00, 0.5, '20x15x3')

print(produto_fisico_darla.descricao()) 

produto_digital_darla = ProdutoDigital('E-book', 50.00, 10)

print(produto_digital_darla.descricao())