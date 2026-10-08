#Crie um programa para jogar JOKEMPO, usando a função random.randint

import random
import time
pc = random.randint(1, 3 )
j = int(input(''
              '1. Papel\n'
              '2. Tesoura\n'
              '3. Pedra\n'
              'JOKEMPO: '))

time.sleep(1)
print('JO')
time.sleep(1)
print('KEM')
time.sleep(1)
print('PO')




if pc == j:
    print('Empate!')
elif (j == 1 and pc == 3) or (j == 2 and pc == 1) or (j == 3 and pc == 2 ):
    print('Ganhou!')
else:
    print('Perdeu!')
























# 1: papel
# 2: tesoura
# 3: pedra