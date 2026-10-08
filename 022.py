#screva um programa que leia o
#me, idade e sexo de 4 pessoas. No final mostre:

#média de idade do grupo
#al é o homem mais velho
#antas mulheres têm menos de 20 anos

soma_idade = 0
mlhr_mnr_que_20 = 0
idade_macho_mais_velho = 0
nome_homem_msvelho = ''


for i in range(4):
    nome = input('Digite o nome: ')
    idade = int(input('Digite a Idade: '))
    sexo = input('Digite o sexo [M/F]: ').strip().upper()[0]



    soma_idade = soma_idade + idade


    if sexo == 'M' and idade > idade_macho_mais_velho:
        idade_macho_mais_velho = idade
        nome_homem_msvelho = nome

    if sexo == 'F' and idade < 20:
         mlhr_mnr_que_20 += 1

print(f'A média de idade do grupo é: {soma_idade / 4}\n'
      f'O homem mais velho é: {nome_homem_msvelho}\n'
      f'Quantas mulheres têm menos de 20 anos: {mlhr_mnr_que_20}')















