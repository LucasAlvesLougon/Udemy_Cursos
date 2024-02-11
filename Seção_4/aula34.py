# Combiantions, Permutations e Product - Itertools
# Combination - Ordem não importa - iterável + tamanho do grupo
# Permutation - Ordem importa
# Product - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product

def print_iter(iterador):
    print(*list(iterador), sep='\n')
    print()

pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
]

print_iter(combinations(pessoas, 2))
print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))
