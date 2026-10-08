#Crie um programa que leia um nome, e mostre o primeiro e o último nome
nome = input('Nome: ').strip()

primeiro_nome = nome [0: nome.find(' ')]
mostrar_primeironome = primeiro_nome
ultimo_nome = nome [nome.rfind(' ') + 1 : ]
mostrar_segundonome = ultimo_nome

print(f'{nome}\n'
      f'Primeiro nome: {mostrar_primeironome}\n'
      f'Ultimo nome: {mostrar_segundonome}')

