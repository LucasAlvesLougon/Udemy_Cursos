# def duplica(numero):
#     return numero * 2
    
# def triplica(numero):
#     return numero * 3
        
# def quadruplica(numero):
#     return numero * 4

def multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplica = multiplicador(2)
triplica = multiplicador(3)
quadruplica = multiplicador(4)
print(duplica(2))
print(triplica(2))
print(quadruplica(2))