pessoa = {
    'nome': 'Lucas',
    'sobrenome': 'Mateus Alves Lougon',
}

pessoa.setdefault('idade', None)
print(pessoa['idade'])
# print(len(pessoa))
# print(pessoa['nome'], pessoa['sobrenome'])
# print(tuple(pessoa.keys()))

# for chave in pessoa.values():
#     print(chave)

# for chave, valor in pessoa.items():
#     print(chave, valor)