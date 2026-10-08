#Escreva um programa que execute o cálculo da Função horária da posição no MRUV, e retorne de acordo com o tempo informado pelo usuário
#A posição do objeto no tempo x é de y (m)

posicao_inicial = float(input(f'digite a posicao inicial '))
velocidade_inicial = float(input(f' digite a velocidade inicial'))
aceleracao = float(input(f' digite a aceleracao'))
tempo = float(input(f' digite o tempo'))
posicao_inicial = ( posicao_inicial + velocidade_inicial * tempo + (aceleracao * tempo ** 2 / 2))

print(f'a posicao do objeto no tempo {tempo} e a {posicao_inicial} m')









