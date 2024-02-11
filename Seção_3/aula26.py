"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
 <- Contagem de complexidade (ruim)
 """

velocidade = input('Insira uma velocidade: ') # velocidade atual do carro
local_carro = input('Insira o local do carro: ') # local em que o carro está na estrada em KM
int_velocidade = int(velocidade)
int_local_carro = int(local_carro)

RADAR = 60 # velocidade maxima do radar 1
LOCAL = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # a distancia onde o radar pega

vel_carro_acima = int_velocidade > RADAR
# vel_carro_abaixo = int_velocidade < RADAR
local_carro_range1_radar = int_local_carro >= (LOCAL - RADAR_RANGE)
local_carro_range2_radar = int_local_carro <= (LOCAL + RADAR_RANGE)
carro_passou_radar = local_carro_range1_radar and local_carro_range2_radar


if vel_carro_acima:
    print(f'Você estava há {velocidade} Km/h')
    print('Você ultrapassou a velocidade maxima da via!')
else:
    print(f'Carro dentro do limite de velocidade')

if carro_passou_radar:
    print(f'Carro passou no radar há {velocidade} Km/h.')

if carro_passou_radar and vel_carro_acima:
    print('Carro multado em radar.')