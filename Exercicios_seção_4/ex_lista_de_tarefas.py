# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']


'''
---Comandos - listar, desfazer, refazer---

1 - A pessoa vai poder adicionar um item a lista
2 - ou digitar um comando
3 - se a pessa escolher listar, mas, não adicionar nada, printar que "adicione um item"
4 - se a pessoa escolher listar, printa a lista com os itens adicionados
5 - se a pessoa escolher desfazer, retire o ultimo item adicionado
6 - se a pessoa escolher refazer, volte com o que ela desfez
7 - se não houver nada para refazer, printar "Não há nada para se refazer"

'''

# ---MINHA SOLUÇÃO---
# def linha():
#     print('-' * 50)

# def tabela():
#     print(
#         '''
# LISTA DE TAREFAS

# Comandos:
# [1] adicionar
# [2] listar
# [3] desfazer
# [4] sair
#         '''
#         )

# def desfazer(indice):
#     lista.pop()
#     return indice

# lista = []

# while True:
#     linha()
#     tabela()
#     linha()

#     try:
#         opcao = input('Escolha um comando: ')
#         if opcao == '1':
#             tarefa = input('Digite sua tarefa: ')
#             lista.append(tarefa)
#             print('Tarefa adicionada')
#         elif opcao == '2':
#             for item in lista:
#                 print(item)
#         elif opcao == '3':
#             for item in lista:
#                 desfazer(lista)
#                 print(lista)
#         elif opcao == '4':
#             print('Saindo')
#             break
        
#     except:
#         print('Erro')

# ---SOLUÇÃO DO PROFESSOR---
import os
import json

def linha():
    print()
    print('-' * 50)
    print()


def listar(tarefas):
    linha()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return
    
    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    linha()

def desfazer(tarefas, tarefas_refazer):
    linha()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return
    
    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)


def refazer(tarefas, tarefas_refazer):
    linha()
    if not tarefas:
        print('Nenhuma tarefa para refazer')
        return
    
    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)

def adicionar(tarefa, tarefas):
    linha()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou nenhuma tarefa')
        return
    tarefas.append(tarefa)

def ler(tarefas, caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
        return dados
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho_arquivo)

def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
            dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados

CAMINHO_ARQUIVO = 'aula43.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('clear'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
        comandos['adicionar']
    comando()
    salvar(tarefas, CAMINHO_ARQUIVO)

# while True:
#     print('Comandos: listar, desfazer, refazer, clear, sair')
#     tarefa = input('Digite uma tarefa ou comando: ')
#     try:
#         if tarefa == 'listar':
#             listar(tarefas)
#             continue
#         elif tarefa == 'desfazer':
#             desfazer(tarefas, tarefas_refazer)
#             continue
#         elif tarefa == 'refazer':
#             refazer(tarefas, tarefas_refazer)
#             continue
#         elif tarefa == 'clear':
#             os.system('cls')
#             continue
#         elif tarefa == 'sair':
#             print('bye,bye!')
#             break
#         else:
#             adicionar(tarefa, tarefas)
#             continue
#     except ValueError:
#         print('Valor inadequado')