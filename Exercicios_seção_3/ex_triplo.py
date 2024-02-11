"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""


entrada = (input('Digite um numero inteiro: '))

if entrada.isdigit():
    entrada_int = int(entrada)

    if (entrada_int % 2 == 0):
        print('O numero que você digitou é par.')
    else:
        print('O numero que você digitou é ímpar.')
else:
    print('Você não digitou um numero inteiro. Repita o processo!')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""


entrada = input('Digite a hora: ')

try:
    hora = int(entrada)

    if (hora >= 0) and (hora <= 11):
        print(f'Bom dia, são {hora} horas!')
    elif (hora >= 12) and (hora <= 17):
        print(f'Boa tarde, são {hora} horas!')
    elif (hora >= 18) and (hora <= 24):
        print(f'Boa noite, são {hora} horas!')
    else:
        print('Hora inválida! Digite novamente')
except:
    print('Digite apenas numeros inteiros.')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""


nome = input('Informe seu primeiro nome: ')
tamanho = len(nome)
nome_curto = tamanho <= 4
nome_normal = (tamanho >= 5) and (tamanho <= 6)

if tamanho > 1:
    if nome_curto:
        print(f'Seu nome tem {tamanho} letras, ele é curto.')
    elif nome_normal:
        print(f'Seu nome tem {tamanho} letras, ele é normal.')
    else:
        print(f'Seu nome tem {tamanho} letras, ele é muito grande.')
else:
    print('Por favor, digite um nome valido!')