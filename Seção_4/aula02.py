# Argumentos nomeados e não nomeados em funções Python
# Argumentos nomeados tem nome com o sinal de igual
# Argumentos não nomeado recebe apenas o argumento (valor)

def soma(x, y):
    # Definição
    resultado = x + y
    print(f'{x=} , {y=} | {x} + {y} = {resultado}')

soma(40, 10)