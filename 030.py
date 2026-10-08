

from random import randint

vitorias = 0

while True:
    escolha = input('Escolha Par ou Ímpar [P/I]: ').upper()

    jogador = randint(1, 10)
    computador = randint(1, 10)

    total = jogador + computador

    print(f'J: {jogador}')
    print(f'PC: {computador}')


    if total % 2 == 0:
        resultado = 'P'
        print('Deu PAR!')
    else:
        resultado = 'I'
        print('Deu ÍMPAR!')

    if escolha == resultado:
        print('Você VENCEU!')
        vitorias += 1

    else:
        print('Você PERDEU!')
        break


print(f'Perdeu Otario KKKKKKK Você conseguiu {vitorias} vitória(s).')