lista_a = (1, 2, 3, 4, 5, 6, 7)
lista_b = [1, 2, 3, 4]


# ---Solução1---
lista_soma = []
soma = None
for item_a in lista_a:
    for item_b in lista_b:
        if item_a == item_b:
            soma = item_a + item_b
            lista_soma.append(soma)
print(lista_soma)

# ---Solução2---
lista_soma = []
for i in range(len(lista_b)):
    lista_soma.append(lista_a[i] + lista_b[i])
print(lista_soma)

# ---Solução3---
lista_soma = []
for i, _ in enumerate(lista_b):
    lista_soma.append(lista_a[i] + lista_b[i])
print(lista_soma)
            
# ---Solução4---
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)       