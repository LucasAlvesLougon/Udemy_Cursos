# Try, except, else e finally

# try:
#     a = 10
#     b = 0
#     c = a / b
#     print(c)
#     print('-' * 10)
# except Exception:
#     print('Erro desconhecido')
# print('continua') 

try: # tenta executar o código
    print(111)
    # 10/0
except Exception: # onde cai o erro
    print('Dividiu 0')
else:
    print('Não deu erro')
finally: # finally sempre será executado
    print(222)