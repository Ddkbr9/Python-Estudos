#Crie um programa para analisar o IMC de uma pessoa, e classifique se ela está entre a faixa ideal, acima ou abaixo do IMC ideal.
peso = float(input('Peso: '))
altura = float(input('altura:'))

imc = peso / altura ** 2

print(f'{imc}')

if imc > 25.0:
    print('Obeso!')
elif imc > 18.5:
    print('Normal!')
else:
    print('Abaixo do ideal!')



