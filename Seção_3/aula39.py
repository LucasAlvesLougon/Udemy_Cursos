# for in com listas

# Exiba os indices da lista
# 0 Maria
# 1 Helena
# 2 Luiz

lista = ['Maria', 'Helena', 'Luiz']
lista.append(input('Digite seu nome: '))
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])