'''
Exercício com classes
1 - criar uma classe Carro        (Nome)
2 - criar uma classe Motor        (Nome)
3 - criar uma classe Fabricante   (Nome)
4 - Faça a ligação entre Carro tem um  Motor
obs.: Um motor pode ser de vários carros
5 - Faça a ligação entre Carro e um Fabricante
Obs.: Um fabricante pode fabricar vários carros
Exiba o nome do carro, motor e fabricante na tela

'''
class Carro:
    def __init__(self, nome):
        self.nome = nome
        self.motor = None
        self.fabricante = None

    @property
    def motor(self, valor):
        self._motor = valor

    @motor.setter
    def motor(self):
        return self._motor
    
    @property
    def fabricante(self, valor):
        self._fabricante = valor

    @fabricante.setter
    def fabricante(self):
        return self._fabricante

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

fusca = Carro('Fusca')
volkwagen = Fabricante('Volkwagen')
motor_1_0 = Motor('1.0')
fusca.fabricante = volkwagen
fusca.motor = motor_1_0
print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)