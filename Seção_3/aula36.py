"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""

lista = [10, 20, 30, 40]

# lista[2] = 300
# print(lista)
# print(lista[2])
# del lista[2]
# print(lista[2])

# lista.append(50)
# lista.pop()
# lista.append(60)
# lista.append(70)
# lista.pop()
# print(lista)

lista.append('Luiz')
nome = lista.pop()
lista.append(1233)
del lista[-1]
# lista.clear()
lista.insert(10, 5)
print(lista)