# Funções recursivas e recursividade
# - funções que podem ser chamar de volta

def recursiva(inicio=0, fim=4):
    # Caso de segurança
    if inicio >= fim:
        return fim
    
    print(inicio, fim)
    # Caso recursivo
    # Contar até chegar ao final
    inicio += 1
    return recursiva(inicio, fim)
print(recursiva())
print()

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
print(factorial(10))
print()
