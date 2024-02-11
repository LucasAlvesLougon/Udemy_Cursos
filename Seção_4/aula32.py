# Decoradores com parâmetros

def decoradora(func):
    print('Decoradora')

    def aninhada(*args, **kwargs):
        print('Aninhada')
        res = func(*args, **kwargs)
        return res * 10
    return aninhada

@decoradora
def soma(x, y):
    return x + y

soma = soma(10, 10)
print(soma)