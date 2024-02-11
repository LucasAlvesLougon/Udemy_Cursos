# raise - lançando exceções (erros)

# redundância do erro
def divide(a, b):
    try:
        return a / b
    except Exception:
        raise

print(divide(8, 0))

def nao_aceita_zero(b):
    if b == 0:
        raise ZeroDivisionError('Você digitou zero')


def divide(a, b):
    return a / b

print(divide(8, 0))