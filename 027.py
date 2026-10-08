#Escreva um programa que leia um número n inteiro qualquer e mostra na tela os n primeiros elementos de uma Sequência de Fibonacci
numero = int(input("Numero: "))

numero_1 = 0
numero_2 = 1
contador = 0
sequencia = ""

while contador < numero:
    sequencia = sequencia + str(numero_1) + " "

    proximo = numero_1 + numero_2
    numero_1 = numero_2
    numero_2 = proximo

    contador += 1

print(sequencia)
