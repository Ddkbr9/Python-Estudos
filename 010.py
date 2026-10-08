#Crie um programa que leia uma frase e mostre:
#Quantas vezes aparece a letra “a”
##Em que posição ela aparece na última vez

frase = input('Frase: ').strip()

frase = frase.replace('á', 'a')
frase = frase.replace('ã', 'a')
frase = frase.replace('â', 'a')
frase = frase.replace('à', 'a')
frase = frase.replace('A','a')

frase_a = frase.count('a')

primeira_posicao = frase.find('a') + 1
ultima_posicao = frase.rfind('a') + 1

print(f'{frase}\n'
      f'A quantidade de letras "a" é: {frase_a}\n'
      f'A primeira vez e posição é: {primeira_posicao}\n'
      f'A ultima vez e posição é: {ultima_posicao}')



