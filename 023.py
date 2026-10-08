#Escreva um programa que leia o peso de 7 pessoas, e no final, mostre qual foi o maior e o menor peso lidos
maior = 0
menor = 0

for i in range(7):
    peso = float(input('Digite seu peso: '))

    if i == 1:
        maior = peso
        menor = peso

    else:

        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso é {maior}kg')
print(f'O menor peso é {menor}kg')

















