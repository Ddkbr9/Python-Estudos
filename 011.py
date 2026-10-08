#Escreva um programa que peça ao usuário um número e imprima se é positivo ou negativo.

numero = float(input('Numero: '))

if numero > 0:
    print('Positivo!')

elif numero == 0:
    print('Neutro!')
else:
    print('Negativo!')