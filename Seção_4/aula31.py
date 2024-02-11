
# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover / Restringir / Alterar
# Funções decoradoras são funções que decoram outra funções
# Decoradores são usados para fazer o Python usar as funçoes decoradoras em outras funções.
# Decoradores no Python são "Syntax Sugar"

def criar_funcao(func):
    def interna(*args, **kwargs):
        
        print('vou te decorar')

        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)

        print('Decorado')

        return resultado
    return interna

def inverte_string(string):
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')
    
inverte_string_checando_paramentro = criar_funcao(inverte_string)
inverte = inverte_string_checando_paramentro('123')
print(inverte)