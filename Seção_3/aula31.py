# frase = 'O Python é uma linguagem de programação ' \
#         'multiparadigma. ' \
#         'Python foi criado por Guido van Rossum.'

frase = 'aaaooo'

# print(frase.count('Python'))

i = 0
aparece_mais = 0
letra_aparece_mais = ''
while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    vezes_letra_aparece = frase.count(letra_atual)

    if aparece_mais < vezes_letra_aparece:
        aparece_mais = vezes_letra_aparece
        letra_aparece_mais = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_aparece_mais}" que apareceu '
    f'{aparece_mais}x'
        )