import json

pessoa = {
    'nome': 'Lucas',
    'sobrenome': 'Lougon',
    'endereço': [
        {'rua': 'R1', 'numero': 108},
        {'rua': 'R2', 'numero': 103},
    ],
    'altura': 1.82,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open('teste.json', 'w', encoding='utf-8') as arquivo:
    json.dump(
        pessoa,
        arquivo,
        ensure_ascii=False,
        indent=2,
        )

with open('teste.json', 'r', encoding='utf-8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)