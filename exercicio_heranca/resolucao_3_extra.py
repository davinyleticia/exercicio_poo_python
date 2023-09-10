# extra - exercício - Imovel


class Imovel:
    def __init__(self, endereco, nome_do_proprietario, preco_base):
        self.endereco = endereco
        self.nome_do_proprietario = nome_do_proprietario
        self.preco_base = preco_base
        
    def calcular_aluguel(self):
            return self.preco_base
        
class Casa(Imovel):
    def __init__(self, endereco, nome_do_proprietario, preco_base, area_terreno):
        super().__init__(endereco, nome_do_proprietario, preco_base)
        self.area_terreno = area_terreno
        
    def calcular_aluguel(self):
        resp =  self.preco_base + (self.area_terreno * 5)
        return resp
    
class Apartamento(Imovel):
    def __init__(self, endereco, nome_do_proprietario, preco_base, numero_quartos):
        super().__init__(endereco,nome_do_proprietario, preco_base)
        self.numero_quartos = numero_quartos
        
    def calcular_aluguel(self):
        resp =  self.preco_base + (self.numero_quartos * 300)
        return resp
    
    
casa_maria = Casa("122 Rua das Flores", "Maria", 1500, 300)
apartamento_carlos = Apartamento("333, Av. João Mendes", 'Carlos Jose', 1200, 2)


print(casa_maria.calcular_aluguel())