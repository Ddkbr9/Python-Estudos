#Escreva um programa que peça ao usuário uma letra e imprima se é uma vogal ou consoante.
letra = input('Digite a letra: ').strip()[0]

letra = letra.replace('A','a')
letra = letra.replace('E','e')
letra = letra.replace('I','i')
letra = letra.replace('O','o')
letra = letra.replace('U','u')

if letra == 'a':
    print('Vogal!')
elif letra == 'e':
    print('Vogal!')
elif letra == 'i':
    print('Vogal!')
elif letra == 'o':
    print('Vogal!')
elif letra == 'u':
    print('Vogal')
else:
    print('Consoante!')