#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas minúsculas
#Quantas letras ao
#Quantas letras tem o primeiro nome

nome = input('Digite seu nome completo:').strip()

nome_espaco = nome.replace(" ", '')
qntd_letras = len(nome_espaco)
posicao_1 = nome.find (' ')
primeiro_nome = nome [0: posicao_1 ]
qntd_letras_1 =len(primeiro_nome)

print(f'Seu nome em maisculo fica: {nome.upper()}\n'
      f'Seu nome em minusculo fica: {nome.lower()}\n'
      f'Quantidade de letras do seu nome:{qntd_letras}\n'
      f'Quantidade letras do seu primeiro nome: {qntd_letras_1}')










