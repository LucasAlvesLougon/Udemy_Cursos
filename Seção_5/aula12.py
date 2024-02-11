# Composição

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

cliente = Cliente('Maria')
cliente.inserir_endereco('av. brasil', 30)
print(cliente)