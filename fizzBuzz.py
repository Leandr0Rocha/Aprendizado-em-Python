'''
Algoritmo que resolve o desafio FizzBuzz de programação.
O programa imprime Fizz para os múltiplos de 3, Buzz para os múltiplos de 5 e FizzBuzz para os múltiplos de ambos.
É requerida a digitação do valor incial e do valor limite do intervalo a ser analisado.
'''
x=int(input('Valor inicial do intervalo:'))
y=int(input('Valor limite do intervalo:'))
if((y-x)>=1000):
    print('Intervalo muito extenso!')
else:
    while(x<y):
        if(x%3==0 and x%5==0):
            print('FizzBuzz')
        elif(x%3==0):
            print('Fizz')
        elif(x%5==0):
            print('Buzz')
        else:
            print(x)
        x+=1