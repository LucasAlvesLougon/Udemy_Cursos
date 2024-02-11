# Métodos de classe + factories
# São métodos onde "self" será "cls", ou seja
# ao invés de receber a instância no primeiro
# parâmetro, recebemos a própria classe.

class Pessoa():
    ano = 2023 # atributo da classe

    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('deu certo')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anonima', idade)

p1 = Pessoa('lucas', 234)
p2 = Pessoa.criar_com_50_anos('Lucas')
p3 = Pessoa.criar_sem_nome(23)

print(p2.nome, p2.idade)
print(p3.nome, p3.idade)