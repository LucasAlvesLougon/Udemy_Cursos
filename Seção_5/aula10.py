# Encapsulamento (modificadores de acesso: puclic, pretected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer classe
# _ (um underline) = pretected
#       não DEVE ser usado fora da classe ou suas subclasses
# __ (dois underlines) = private
#       "name mangling" (desfuguração de nomes) em Python
#       só DEVE ser usado na classe em que foi declarado

class Foo:
    def __init__(self):
        self.public = 'publico'
        self.protected = 'protegido'
        self.private = 'privado'