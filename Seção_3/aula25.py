# Introdução ao try/except
# try -> tentar executar o código
# except -> ocorreu um erro ao tentar executar

numero_str = input('Vou dobrar o numero que você digitar: ')

try:
    numero_float = float(numero_str)
    numero_int = int(numero_str)
    print('INT: ',numero_int)
    print('FLOAT: ',numero_float)
    print(f'O dobro de {numero_float} é {numero_float * 2}')
except:
    print('Isso não é um numero.')