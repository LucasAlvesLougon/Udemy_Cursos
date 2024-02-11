from ex_salva_classe_json_a import CAMINHO_ARQUIVO, Pessoa, fazer_dump
import json

fazer_dump()

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    print('FAZENDO O LOAD')
    pessoas = json.load(arquivo)
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])

    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)

print(__name__)