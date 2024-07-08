'''
Programa que calcula o perímetro e a área de um quadrado com base no valor de um dos lados.
É pedido ao usuário a digitação da medida de um dos lados e o programa mostra uma mensagem com os valores do perímmetro e da área.
'''
lados=int((input('Digite a medida de um dos lados do quadrado em centímetros:')))
perimetro=lados*4
area=lados**2
print('Esse quadrado possui perímetro =',perimetro,'cm e área =',area,'cm²')