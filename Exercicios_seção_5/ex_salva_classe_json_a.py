import json

CAMINHO_ARQUIVO = 'ex_classe.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def fazer_dump():
        with open(CAMINHO_ARQUIVO, 'w') as arquivo:
            print('FAZENDO DUMP')
            json.dump(bd, arquivo, ensure_ascii=False, indent=2)

p1 = Pessoa('Lucas', 18)
p2 = Pessoa('Maria', 20)
bd = [vars(p1), vars(p2)]


# print(p1.nome, p1.idade)
# print(p2.nome, p2.idade)