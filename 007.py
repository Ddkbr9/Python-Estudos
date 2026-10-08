#Crie um algoritmo que leia um salário e simule um reajuste positivo de 60%.
salario = float(input('Digite seu salario: '))

porcentagem = 60

reajuste = salario * (porcentagem/ 100)

reajuste_1 = salario + reajuste

print(f'O reajuste salarial sera de: {reajuste}\n'
      f'O total sera de {reajuste_1}')

