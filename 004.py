#Escreva um programa que converta real para o Franco Congolês
from timeit import repeat

dinheiro = float(input('Digite a quantia para conversão :'))

franco_congoles = (dinheiro * 442.65)

print(f'{dinheiro} reais, equivalem a {franco_congoles}!')

