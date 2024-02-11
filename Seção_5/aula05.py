# Atributos de classe
class Pessoa:
    # atributo da classe
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa('João', 35)
p2 = Pessoa('Helena', 12)
print(f'{p1.nome} nasceu em {p1.get_ano_nascimento()}')
print(f'{p2.nome} nasceu em {p2.get_ano_nascimento()}')
