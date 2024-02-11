# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.
# s0 = set() # set vazio
# s1 = {'Lucas'} # set com dados str
# s2 = {1, 2, 3} # set com dados int
# s3 = set('Lucas') # set retornando o valor ou item em ordem aleatoria

# print(s1, type(s1))
# print(s2, type(s2))
# print(s3, type(s3))


# s1 = {1, 2, 3, 3, 3, 3, 1}
# print(s1)

# # Métodos úteis
# s1 = set()
# s1.add(('Lucas')) # adiciona valores no set
# print(s1)
# s1.add(1)
# s1.update((1, 2, 3)) # atualiza valores no set
# # s1.discard('Lucas') # descarta valores do set
# # s1.clear() # limpa o set completamente
# print(s1)

# Operadores úteis
# união ( | )
# Intersecção ( & )
# Diferença ( - )
# Diferença simétrica ( ^ )


# s1 = {1, 2, 3}
# s2 = {2, 3, 4}

# # Exemplo de uso de set
# union = s1 | s2
# intersec = s1 & s2
# diferenca = s1 - s2
# diferenca_simetrica = s1 ^ s2

# print(f'União = {union}')
# print(f'Intersecção = {intersec}')
# print(f'Diferença = {diferenca}')
# print(f'Diferença simétrica = {diferenca_simetrica}')

letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('PARABENS!')
        break

print(letras)