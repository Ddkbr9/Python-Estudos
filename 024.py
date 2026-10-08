#Escreva um programa que verifique se uma frase é um palíndromo.
frase = input("Digite uma frase: ").strip().upper().replace(' ', '')

#2

if frase == frase[::-1]:
    print('É palindromo!')
else:
    print('Não é palindromo!')

#1

frase = frase.replace('', ' ').lower()

palindromo = True

for i in range(len(frase) // 2):
    if frase[i] != frase[len(frase) - 1 - i]:
        palindromo = False
        break

if palindromo:
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo!")


