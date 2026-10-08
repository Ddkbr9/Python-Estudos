#Crie um programa que leia vários números inteiros. O programa só vai parar quando o usuário digitar 0000. No final mostre quantos números foram digitados e qual a soma entre eles (desconsiderando o flag)

soma = 0
contador = 0
print('A soma dos produtos só sera vizualizada depois que o numero (0000) for digitado.')

while True:
    numero = input('Digite um número: ')

    if numero == '0000':
        break

    soma += 1
    contador += int(numero)



print(f'Quantidade de números digitados: {soma}')
print(f'Soma dos números: {contador}')