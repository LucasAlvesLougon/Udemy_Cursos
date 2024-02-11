# Retorno de valores das funções (return)
import os

def nome():
    nome = input('Digite seu nome: ')
    os.system('cls')
    return nome
print(f'Seu nome é {nome()}')


def soma(x, y):
    return x + y

soma1 = soma(2, 40)
soma2 = soma(40, 3)
print(f'Você tem {soma1 + soma2} anos')