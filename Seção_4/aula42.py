# problemas dos parâmetros mutáveis em funçoes python

# ---Problema---
def adiciona_clientes(nome, lista=[]):
    lista.append(nome)
    return lista

cliente = adiciona_clientes('Lucas')
adiciona_clientes('Maria', cliente)
print(cliente)

# ---Solução---
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adiciona_clientes('Lucas')
adiciona_clientes('Maria', cliente1)
print(cliente1)

cliente2 = adiciona_clientes('jao')
adiciona_clientes('dania', cliente2)
print(cliente2)