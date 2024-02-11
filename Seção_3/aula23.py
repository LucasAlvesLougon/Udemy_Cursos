# Formatação básica de strings
# s - string
# d - int
# f - float
# .<número de digitos>f
# x ou X - Hexadecimal
# ---------------------------------------------
# (Caractere) (><^) (Quantidade)
# > - Esquerda
# < - Direita
# ^ - Centro
# = - Força o número a aparecer antes dos zeros
# Sinal - + ou -
# Ex.: 0>-100,.1f
# ---------------------------------------------
# Conversion flags - !r !s !a
# !r = __repr__
# !s = __str__
# !a = __asc__

var = 'ABCD'
print(f'{var}')
print(f'{var: >10}')
print(f'{var: <10}')
print(f'{var: ^10}')
print(f'{1000.32423423:.2f}')

print(f'O hexadecimal de 1500 é {1500:08X}')