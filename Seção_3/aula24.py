"""
Fatiamento de strings

 0 1 2 3 4 5 6 7 8
 O l á   m u n d o
-9 8 7 6 5 4 3 2 1

Fatiamento [i:f:p] [::]
Obs.: a função len retorna a quantidade(qtd) de caracteres da str
"""

var = 'Olá mundo'
print(var[:-2:-1])
print(len(var))
print(var[:9])
print(var[:9:4])
print(var[::-1])
print(var[-1:-10:-2])