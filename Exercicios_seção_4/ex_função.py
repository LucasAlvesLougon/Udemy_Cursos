# Exercícios com funções
# print('Conta base:', 1*2*3*4*5)
# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# def multiplicacao(*args):
#     total = 1
#     for numero in args:
#         total *= numero
#     return total


# mult = multiplicacao(1, 2, 3, 4, 5)
# print(f'Retorno da função: {mult}')

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0
    if multiplo_de_dois:
        return f'O numero {numero} é par'
    return f'O numero {numero} é impar'


print(par_impar(2))
print(par_impar(3))
print(par_impar(345))
print(par_impar(56744))