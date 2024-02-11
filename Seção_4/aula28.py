# Recarregando módulos, importilib e singleton

import importlib

import aula28_m
from aula28_m import variavel

print(variavel)

for i in range(10):
    print(i)
    importlib.reload(aula28_m)

print('FIM')