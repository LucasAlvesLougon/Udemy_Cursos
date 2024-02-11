# Calculadora com while

while True:
    num_1 = input('Digite um numero: ')
    num_2 = input('Digite outro numero: ')
    operador = input('Digite a operação desejada (+-/*): ')

    num_validos = None
    num_1_float  = 0
    num_2_float  = 0

    try:
        num_1_float  = float(num_1)
        num_2_float  = float(num_2)
        num_validos = True
    except:
        num_validos = None

    if num_validos is None:
        print('Um ou ambos os numeros digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue

    if len(operador) > 1:
        print('Digite apenas 1(um) operador')
        continue

    adi = num_1_float + num_2_float
    sub = num_1_float - num_2_float
    div = num_1_float / num_2_float
    mul = num_1_float * num_2_float

    print('Realizando sua conta. Confira o resultado abaixo:')
    if operador == '+':
        print(f'{num_1_float} + {num_2_float} = {adi}')
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} = {sub}')
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} = {div}')
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} = {mul}')

    sair = input('Quer sair? [s]Sim: ').lower().startswith('s')

    if sair is True:
        break