import sys
# Iterables e Iterators em python

# ---Possibilidade de transformar um dicionario em um iterator---
# iterable = ['Eu', 'Tenho', '__iter__']
# iterator = iter(iterable) # tem (__iter__) e (__next__) 
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# ---Generator expression---
lista = [n for n in range(1000)]
generator = (n for n in range(1000))
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))
