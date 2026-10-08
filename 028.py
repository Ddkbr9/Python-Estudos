#Crie uma calculadora que após ler 3 valores, mostre e opere de acordo com as opções:
#1.	Somar
#2.	Multiplicar
#3.	Maior
#4.	Novos números
#5.	Sair do programa

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

numero = 0

while True:
    print('1.Somar')
    print('2.Multiplicar')
    print('3.maior')
    print('4.Novos Numeros')
    print('5.Sair do Programa')

    numero = int(input('Digite um dos 5 numeros: '))

    if numero == 1:
        print('Soma:', n1 + n2 + n3 )
    elif numero == 2:
        print('Multiplicação: ', n1 * n2 * n3 )
    elif numero == 3:
        maior =n1
        if n2 > maior:
            maior = n2
        if n3 > maior:
            maior = n3
        print(f'Maior numero: {maior}')
    elif numero == 4:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        n3 = int(input("Digite o terceiro número: "))
    elif numero == 5:
        print('Programa encerrado!')


    else:
        print('Opção invalida!')
    break





