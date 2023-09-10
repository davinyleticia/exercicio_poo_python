# 🍞 Mão na massa

Os exercicíos proposta para sala de aula:

## ✏️ Exercicío Classe, Atributo e Método

- Exercício 1: Exercício de Classe, Atributo e Método (Nível Básico): Conta Bancária

Você está criando um programa para representar contas bancárias. Cada conta bancária tem um número de conta, um titular da conta e um saldo. Você precisa criar uma classe ContaBancaria para representar essas contas e fornecer métodos para realizar operações básicas, como depósito e saque.

`Instruções:`

Crie uma classe chamada ContaBancaria com os seguintes atributos:

numero_conta: o número da conta (um número inteiro).
titular_conta: o nome do titular da conta (uma string).
saldo: o saldo da conta (um número decimal, inicialmente definido como 0).
Implemente os seguintes métodos na classe ContaBancaria:

`__init__(self, numero_conta, titular_conta)`: O construtor que inicializa os atributos da conta.
depositar(self, valor): Um método que permite ao titular da conta depositar dinheiro na conta.
sacar(self, valor): Um método que permite ao titular da conta sacar dinheiro da conta, desde que haja saldo suficiente.

Exemplo:

```python
# Exemplo de uso:
conta = ContaBancaria(12345, "João da Silva")
print(f"Saldo inicial da conta de {conta.titular_conta}: R${conta.saldo}")

conta.depositar(1000)
print(f"Saldo após depósito: R${conta.saldo}")

conta.sacar(500)
print(f"Saldo após saque: R${conta.saldo}")
```

- Exercício 2: Exercício de Classe, Atributo e Método (Nível Básico): Retângulo

Crie uma classe chamada Retangulo para representar retângulos. Cada retângulo tem largura e altura. A classe deve incluir métodos para calcular a área e o perímetro do retângulo.

Instruções:

Crie uma classe chamada Retangulo com os seguintes atributos:

largura: a largura do retângulo (um número decimal).
altura: a altura do retângulo (um número decimal).
Implemente os seguintes métodos na classe Retangulo:

__init__(self, largura, altura): O construtor que inicializa os atributos da largura e altura.
calcular_area(self): Um método que calcula a área do retângulo (área = largura * altura).
calcular_perimetro(self): Um método que calcula o perímetro do retângulo (perímetro = 2 * (largura + altura)).
Exemplo:

```python

# Exemplo de uso:
retangulo = Retangulo(5.0, 3.0)

area = retangulo.calcular_area()
perimetro = retangulo.calcular_perimetro()

print(f"Área do retângulo: {area}")
print(f"Perímetro do retângulo: {perimetro}")
```

## ✏️ Exercicío Herança

- Exercício 1: Veículos

Crie um sistema de gerenciamento de veículos. Crie uma classe base chamada Veiculo com os seguintes atributos:

    - marca: a marca do veículo.
    - modelo: o modelo do veículo.
    - ano: o ano de fabricação do veículo.

    
A classe Veiculo deve ter um método chamado `descricao()` que retorna uma descrição completa do veículo.

Crie duas subclasses concretas, Carro e Moto, que herdam da classe Veiculo. Adicione atributos específicos para cada tipo de veículo, como número de portas para carros e tipo de motor para motos.

Implemente o método `descricao()` em cada uma das subclasses para incluir informações específicas do tipo de veículo.

Crie instâncias de Carro e Moto, atribuindo valores adequados aos atributos de cada veículo. Use o método `descricao()` para exibir informações detalhadas sobre cada veículo.

- Exercício 2: Produtos

Crie um sistema de gerenciamento de produtos em uma loja. Crie uma classe base chamada Produto com os seguintes atributos:

nome: o nome do produto.
preco: o preço do produto.
A classe Produto deve ter um método chamado `descricao()` que retorna uma descrição completa do produto.

Crie duas subclasses concretas, ProdutoFisico e ProdutoDigital, que herdam da classe Produto. Adicione atributos específicos para cada tipo de produto, como peso e dimensões para produtos físicos e tamanho de arquivo para produtos digitais.

Implemente o método `descricao()` em cada uma das subclasses para incluir informações específicas do tipo de produto.

Crie instâncias de ProdutoFisico e ProdutoDigital, atribuindo valores adequados aos atributos de cada produto. Use o método `descricao()` para exibir informações detalhadas sobre cada produto.

Esses exercícios ajudarão você a praticar a criação de hierarquias de classes com herança em Python e a entender como compartilhar funcionalidades comuns e adicionar comportamentos específicos em subclasses.

 - Exercício 3 - Extra 

Implemente o método `calcular_aluguel()` em cada uma das subclasses para calcular o valor do aluguel com base em regras específicas:

Para Casa, o aluguel deve ser calculado como `preco_base + (area_terreno * 5)`.

Para Apartamento, o aluguel deve ser calculado como `preco_base + (numero_quartos * 300)`.

e superclass tem o atributo endereco e `nome_do_proprietario`

## ✏️ Encapsulamento


- Exercício 1: Catálogo de Produtos

Crie uma classe chamada Produto que represente um produto em um catálogo. A classe deve ter os seguintes atributos privados:

nome: o nome do produto. preco: o preço do produto. A classe deve incluir métodos públicos para definir e obter o nome e o preço do produto. Além disso, crie um método `__str` para exibir o produto de forma amigável.

- Exercício 2: Biblioteca

Crie uma classe chamada Livro que represente um livro em uma biblioteca. A classe deve ter os seguintes atributos privados:

titulo: o título do livro. autor: o autor do livro. `_disponivel`: um indicador de disponibilidade do livro (inicialmente definido como True se o livro estiver disponível para empréstimo). A classe deve incluir métodos públicos para emprestar o livro (definindo _disponivel como False) e devolvê-lo (definindo _disponivel como True). Além disso, crie um método `__str` para exibir informações sobre o livro.

- Exercício 3: Banco de Dados de Funcionários

Crie uma classe chamada Funcionario que represente um funcionário em um banco de dados de funcionários. A classe deve ter os seguintes atributos privados:

nome: o nome do funcionário. cargo: o cargo do funcionário. A classe deve incluir métodos públicos para definir e obter o nome e o cargo do funcionário. Além disso, crie um método `__str` para exibir informações sobre o funcionário.

- Exercício 4: Agenda de Compromissos

Crie uma classe chamada Compromisso que represente um compromisso na agenda de alguém. A classe deve ter os seguintes atributos privados:

data: a data do compromisso. descricao: a descrição do compromisso. A classe deve incluir métodos públicos para definir e obter a data e a descrição do compromisso. Além disso, crie um método `__str` para exibir informações sobre o compromisso.


## ✏️ Abstração

- Exercício 1: Figuras Geométricas

Crie uma classe abstrata chamada FiguraGeometrica com um método abstrato `calcular_area()`. Em seguida, crie subclasses concretas como Retangulo, Circulo e Triangulo que herdam da classe FiguraGeometrica. Cada uma das subclasses deve implementar o método calcular_area() de acordo com a fórmula apropriada para cada figura geométrica.

- Exercício 2: Animais

Crie uma classe abstrata chamada Animal com métodos abstratos `emitir_som()` e `mover()`. Em seguida, crie subclasses concretas como Cachorro, Gato e Pato que herdam da classe Animal. Cada uma das subclasses deve implementar os métodos emitir_som() e mover() de acordo com o comportamento apropriado para cada animal.

- Exercício 3: Veículos

Crie uma classe abstrata chamada Veiculo com métodos abstratos `acelerar()` e `frear()`. Em seguida, crie subclasses concretas como Carro, Moto e Caminhao que herdam da classe Veiculo. Cada uma das subclasses deve implementar os métodos `acelerar()` e `frear()` de acordo com o comportamento apropriado para cada tipo de veículo.

- Exercício 4: Produtos

Crie uma classe abstrata chamada Produto com métodos abstratos `calcular_preco()` e `descricao()`. Em seguida, crie subclasses concretas como Livro, Eletronico e Alimento que herdam da classe Produto. Cada uma das subclasses deve implementar os métodos `calcular_preco()` e descricao() de acordo com as características específicas de cada produto.

- Exercício 5: Formas de Pagamento

Crie uma classe abstrata chamada FormaPagamento com métodos abstratos `calcular_desconto()` e `calcular_parcelas()`. Em seguida, crie subclasses concretas como CartaoCredito, Boleto e Transferencia que herdam da classe FormaPagamento. Cada uma das subclasses deve implementar os métodos `calcular_desconto()` e `calcular_parcelas()` de acordo com as regras de pagamento específicas.


## Sobre

exercícios feito para aula da Reprograma turma 0n26 Python

criado por @github.com/davinyleticia

[https://daviny.dev](https://daviny.dev)