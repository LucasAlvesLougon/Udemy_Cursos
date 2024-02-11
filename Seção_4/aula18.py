lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
lista = [
    [letra for letra in 'Lucas'] # list comprehension dentro de outra list comprehension
    for x in range(3)
]

print(lista)