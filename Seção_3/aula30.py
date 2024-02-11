# while dentro de while (laços internos)

q_linhas = 5
q_colunas = 5

linha = 1
while linha <= q_linhas:
    coluna = 1
    print(linha)
    while coluna <= q_colunas:
        print(f'{linha=}, {coluna=}')
        coluna += 1
    linha += 1

print('Acabou')