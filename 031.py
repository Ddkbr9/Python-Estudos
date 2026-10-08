#Crie um programa que retorne a tabuada de um número, e só pare quando o número digitado for 0000


while True:
    n = int(input('Digite seu numero: '))

    if n == 0000:
        break

    print(f'Tabuada do numero {n}')

    for i in range(11):
        print(f'{n} X {i} = {n * i}')



