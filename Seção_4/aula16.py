# a, b = 1, 2
# a, b = b, a
# print(a, b)

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}
dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoa_completa = {
    **pessoa, **dados_pessoa
}
# print(pessoa_completa)

def mostra_argumentos_nomeados(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)

# mostra_argumentos_nomeados(nome='Lucas', idade= 18)
mostra_argumentos_nomeados(**pessoa_completa)