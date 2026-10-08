#Escreva um programa que execute o cálculo da Função horária da posição no MRUV, e retorne de acordo com o tempo informado pelo usuário
posicao_inicial = int(input('Digite a posição inicial: '))
velocicade_inicial = int(input('Digite a velocidade inicial:'))
aceleracao = int(input('Digite a aceleração'))
tempo = int(input('Digite o tempo '))

posicao_inicial = (posicao_inicial + velocicade_inicial * tempo +  aceleracao * tempo ** 2 / 2)


print(f'a posição do objeto no tempo de {tempo} segundos é de {posicao_inicial} M')

