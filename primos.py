'''
Programa que verifica a quantidade de divisores de um número e verifica se é um número primo ou não.
O programa pede a digitação do número e devolve uma mensagem com a confirmação e o número de divsores.
'''
n=int(input('Digite um número inteiro:'))
cont=0
i=n
while(i>0):
    if(n%i==0):
        cont+=1
    i-=1
if(cont==2):
    print('Primo, número de divisores:',cont,'.')
else:
    print('Não primo, número de divisores:',cont,'.')
