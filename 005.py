#Escreva um programa que leia o raio de uma esfera, e calcule o seu volume e área.

esfera = float(input('Digite o volume da esfera:'))


v = 4//3 * 3.14 * esfera ** 3
a = 4 * 3.14 * esfera ** 2

print(f'Volume da esfera: {v} \nArea da esfera: {a}')