#Algoritmo que aplica a fórmula de bhaskara em três variáveis(a, b e c) e encontra as raízes reais da equação, se houver.
#O programa pede a digitação dos valores a, b, e c, então realiza o cálculo da fórmula e retorna as raízes.

import math;

a=float(input('Valor de a:'))
b=float(input('Valor de b:'))
c=float(input('Valor de c:'))
delta=float(math.pow(b,2)-4*a*c)
if (delta<0):
    print('Esta equação não possui raízes reais.')
elif (delta==0):
    root1=(-b+math.sqrt(delta))/(2*a)
    print('As raízes são iguais nesta equação:',round(root1,2))
else:
    root1=(-b+math.sqrt(delta))/(2*a)
    root2=(-b-math.sqrt(delta))/(2*a)
    print('As raízes da equação são:',round(root1,2),'e',round(root2,2))