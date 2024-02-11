# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
from itertools import zip_longest


cidade = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estado = ['BA', 'SP', 'MG', 'RJ']

# criando o zipper
def zipper(l1, l2):
    intervalo = (min(len(cidade), len(estado)))
    return [(l1[i], l2[i]) for i in range(intervalo)]
print(zipper(cidade, estado))
print()

# Junta de acordo com a MENOR lista
print(list(zip(cidade, estado)))
print()

# Junta de acordo com a MAIOR lista
print(list(zip_longest(cidade, estado)))