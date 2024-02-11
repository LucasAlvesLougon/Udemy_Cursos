# Interando strings com while

nome = 'Lucas Mateus'

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = (nome[indice])
    novo_nome += f'{letra}_'
    indice += 1

print(novo_nome)