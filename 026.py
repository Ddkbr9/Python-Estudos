#Faça um programa que leia um número e retorne o fatorial !
#4! = 4 x 3 x 2 x 1

numero =int(input('Numero: '))

fatorial = 1
contador = numero

while contador > 0:
    fatorial = fatorial * contador
    contador -=1
print(f'O fatorial de {numero} é {fatorial}')
