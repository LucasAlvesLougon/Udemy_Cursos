# __dict__ e vars para atributos de instância
class Pessoa:
    # atributo da classe
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa('João', 35)
# p1.nome = ''

p1.__dict__['other'] = 'thing'
print(p1.__dict__)
print(vars(p1))
print(p1.other)