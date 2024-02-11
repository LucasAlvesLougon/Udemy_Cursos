# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# private / protected / public
# Código cliente - é o código que usa o seu código

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        return self.cor_tinta
    
#################################
        
caneta = Caneta('Azul')
print(caneta.cor)