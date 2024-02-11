# enumerate - enumera iteráveis (indices)

lista = ['Maria', 'Helena', 'Luiz']
lista.append('Lucas')
# lista_enumerada = list(enumerate(lista))


for indice, nome in enumerate(lista):
    print(indice, '-', nome)