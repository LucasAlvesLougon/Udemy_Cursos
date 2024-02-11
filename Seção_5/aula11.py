# Agregação

class Carrinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum(self._produtos)
    
    def listar_produtos(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)
    
    def inserir_produtos(self, *produtos):
        self._produtos.extend(produtos)

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

carrinho = Carrinho()
p1, p2 = Produto('caneta', 1.20), Produto('Camiseta', 20)
carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()