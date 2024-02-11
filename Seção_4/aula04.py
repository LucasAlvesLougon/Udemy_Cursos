"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1 # valor estrito ao escopo global

# Escopo 1
def escopo():
    x = 10 # Valor estrito ao escopo 1
    # Escopo 2
    def outro_escopo():
        x = 24 # valor estrito ao escopo 2
        y = 2 # valor estrito ao escopo 2
        print(x, y)
    outro_escopo()
    print(x)

escopo()
print(x)