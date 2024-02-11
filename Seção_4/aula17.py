# List comprehension em Python
# List comprehension é uma forma rápida para criar listas a partir de iteráveis
# print(list(range(10)))

# lista = []
# for num in range(10):
#     lista.append(num)
# print(lista)

lista = [num * 2 for num in range(10)] # List comprehension
print(lista)

# novos_produtos = [
#     {**produto, 'preco': produto['preco'] * 1.05}
#     if produto['preco'] > 20 else {**produto}
#     for produto in produtos
#     if (produto['preco'] * 1.05) > 10
# ]

# p(novos_produtos)