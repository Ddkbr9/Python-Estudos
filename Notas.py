'''
print('Bem vindo ao Senai')

#operações matematicas
print(58 + 56) #adição
print(89 - 9) #subtração
print(67 * 34) #multiplicação
print(58 / 9) #divisão
print(5 ** 9) #exponenciação
print(21 // 2) #resultado da divisão inteira
print(21 % 2) #resto da divisao inteira



#Variáveis
nome = 'daniel ferreira'
idade = 16

print(f'Seu nome é {nome}, com {idade} anos')



#Entrada de Dados


nome = input('Digite seu nome: ')

print(f'Seu nome é {nome}')


#Escreva um programa que leia duas idades separadamente, Realize a sua soma
#e retorne o resultado no terminal

idade1 = int(input('digite a sua idade'))

idade2 = int(input('digite a sua idade'))

resultado = idade1 + idade2

print(f'soma {idade1} + {idade2} e  {resultado}')





#strings
senai = 'Daniel Ferreira'

#fatiamento
print(senai[3])
print(senai[3:7])
print(senai[3:])
print(senai[:8])

#Analise
print(len(senai))
print(senai.count('d'))
print(senai.find('d'))
print(senai.rfind('d'))


#for
#1
for i in range(1,101):
    print(i)
#2
for i in range(1,11):
    print(i)
#3
for i in range(10,0,-1):
    print(i)

#4
soma = 0
for i in range(0, 5):
    n = int(input('N:' ))
    soma = soma + n
print(soma)



#While

#1
i = 0
while i < 10:
    print('Bem vindo ao Senai')
    i += 1 #-----> i = 1 + 1

#2
resposta = '5'
while resposta != 'N':
    print('Bem vindo ao Senai')
    resposta = input('Deseja continuar? [S/N]:').strip().upper()[0]



#while true:

#1
while True:
    resposta = input('Deseja continuar? [S/N]: ').strip().upper()
    if resposta == 'N':
        break

#2
while True:
    print('---------------------------------')
    menu = int(input('1. ola:'
                     '\n2. Oi:'
                     '\n3. sair:'))
    if menu == 1:
        print('Olá')
    elif menu == 2:
        print('Oi')
    elif menu == 3:
        break
    else:
        print('Digite uma opção valida:')





#Tratamento de erro

try:
    n = int(input('N: '))
    x = 1 / 0
except ValueError:
    print('Só aceitamos Números')
except ZeroDivisionError:
    print('Não dividimos por 0')



#Crie um programa que pede ao usuario 2 números e em seguida, divide
#o primeiro pelo segundo, Porém deve prever os erros de divisão por 0 e valor!

while True:
    try:
        n1 = int(input('N1: '))
        n2 = int(input('N2: '))
        print(f'A Divisão é {n1/n2}')
        break
    except ValueError:
        print('Só aceitamos números')
    except ZeroDivisionError:
        print('Não é possivel dividir por 0')



#Funções
#1
def quebra_linha():
    print('-*-' * 20)
   
#2
def mensagem(x):
    quebra_linha()
    print(x)
    quebra_linha()

#3
def area(x, y):
    return x * y
#4
def volume(x, y, z):
    return area(x, y) * z

mensagem('Daniel')


#Escreva um programa
#que tenha uma função media
#que receba 5 valores e retorne
#a sua media

def media (a,b,c,d,e):
    return (a+b+c+d+e) / 5
print(media(1,2,3,4,5))


#Estrutura de dados
#Tuplas
carro = ('Ferrari','Vermelha', 2026)

#Fatiamento
print(carro[0])
print(carro[0:2])
print(carro)

#Iterar
#1
for i in carro:
    print(i)

#2
for i in range(0, len(carro)):
    print(carro[i])

#3
for pos, carac in enumerate(carro):
    print(f'{pos} - {carac}')

idades = (8,9,10,45,55,64,13,14)
print(max(idades))
print(min(idades))
print(sum(idades))
print(sum(idades) / len(idades))
print(sorted(idades))
print(sorted(idades, reverse=True))




#crie uma tupla preenchido com os 10 filmes mais assistidos de todos os tempos
#1. Apenas os 3 primeiros
#2. Os dois últimos mais assisitidos
#3. A lista em ordem Alfabética
#4. Em que posição está o Rei Leão

filmes = ('Avatar'
              ,'Vingadores: ultimato'
              ,'Homem-Aranha: Um Novo Dia '
              ,'Avatar: O Caminho da Água'
              ,'Ne zha 2'
              ,'Titanic'
              ,'Star Wars: Episódio VII - O Despertar da Força'
              ,'Vingadores: Guerra Infinita'
              ,'Homem Aranha: Sem Volta Pra Casa'
              ,'O Rei Leão')

#Os Três Primeiros:
quebra_linha()
print(f'Os 3 Primeiros Filmes São:')
for i in range(3):
    print(filmes[i])

#Os Dois Ultimos Mais Assistidos:
quebra_linha()
print(f'Os Dois Últimos Filmes mais Assistidos São:')
for i in range(8, 10):
    print(filmes[i])

#A Lista em Ordem Alfabética:
quebra_linha()
print(f'A Lista Dos Filmes em Ordem Alfabética:')
for i in sorted(filmes):
    print(i)

#Posição do Filme Rei Leão:
quebra_linha()
print(f'Posição do Filme Rei Leão:')
for i in range(len(filmes)):
    if filmes[i] == 'O Rei Leão':
        print('O Rei Leão está na posição', i + 1)

'''