class Animal:
    def __init__(self, nome):
        self.nome = nome
    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'
    
    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)
leao = Animal('Leão')
print(leao.nome)
print(leao.comendo('Maçã'))
print(leao.executar('Carneiro'))
print(leao.executar('Boi'))
