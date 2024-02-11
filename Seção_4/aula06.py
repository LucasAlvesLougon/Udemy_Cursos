print(1+2+3+4+5+6+7+78+10)

def soma(*args):
    print(args)
    total = 0
    for numero in args:
        total += numero
        print(f'soma: {total} + {numero} = {total}')
    return total

soma_1 = soma(1, 2, 3)
print(soma_1)
soma_2 = soma(4, 5, 6)
print(soma_2)

print(soma(1, 2, 3, 4, 5, 6, 7, 78, 10))