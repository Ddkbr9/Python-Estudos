#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final mostre:
#Qual é o total gasto na compra
#Quantos produtos custam mais de R$1000,00
#Qual é o produto mais barato

total = 0
mais_de_1000 = 0
menor_preco = 0
produto_mais_barato = ''

while True:

    nome = input('Nome do produto: ')
    preco = float(input('Preço do produto: R$ '))

    total += preco

    if preco > 1000:
        mais_de_1000 += 1

    if menor_preco == 0 or preco < menor_preco:
        menor_preco = preco
        produto_mais_barato = nome

    continuar = input('Deseja continuar? [S/N]: ').strip().upper()

    if continuar == "N":
        break

print(f'Total gasto: R$ {total}')
print(f'Produtos que custam mais de R$ 1000: {mais_de_1000}')
print(f'Produto mais barato: {produto_mais_barato} com o preço de: R$ {menor_preco}')