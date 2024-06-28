#Algoritmo que compara a distância de dois pontos em um plano cartesiano.
#Considerando as distâncias maiores ou iguais a dez como longe, e distâncias menores que 10 como perto.
#O programa pede a digitação dos eixos x e y dos dois pontos e devolve uma mensagem de longe ou perto como valor da distância.

import math

x1=int(input('Eixo x do primeiro ponto:'))
y1=int(input('Eixo y do primeiro ponto:'))
x2=int(input('Eixo x do segundo ponto:'))
y2=int(input('Eixo y do segundo ponto:'))
dis=math.sqrt(((x1-x2)**2)+((y1-y2)**2))
if(dis>=10):
    print('A distância é longa,',dis,'unidades.')
else:
    print('A distância é curta,',dis,'unidades.')