#Escreva um programa que peça ao usuário para adivinhar um número entre 1 e 10 e continue pedindo até que o usuário acerte o número. E no final, retorne também a quantidade de tentativas necessárias.
import random

pc = random.randint(1, 10)
tentativas = 1

while True:
    tentativa = int(input("Adivinhe um número entre 1 e 10: "))
    tentativas = tentativas + 1

    if tentativa == pc:
        print("Acertou!")
        print(f"Voçe usou {tentativas} tentativas!")
        break
    else:
        print("Errou tente novamente!")