#Programa que converte um valor inteiro de segundos em quantidade de dias, horas, minutos e segundos.
#O algoritmo pede a digitação do número de segundos e mostra uma mensagem com os segundos convertidos em outras medidas de tempo.

num=int(input('Por favor, digitee o número de segundos que deseja converter:'))
dias=num//86400
horas=(num%86400)//3600
minutos=(num%3600)//60
segundos=(num%60)
print(num,'segundos em outras unidades de tempo equvale a:')
print(dias,'dia(s),',horas,'hora(s),',minutos,'minuto(s) e',segundos,'segundo(s).')