# class - Classes são moldes para criar novos objetos

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Lucas', 'Mateus')

p2 = Pessoa('Maria', 'Souza')
# p1.nome = 'Lucas'
# p1.sobrenome = 'Mateus Alves Lougon'
print(p1.nome, p1.sobrenome)

print(p2.nome, p2.sobrenome)