#Crie um programa que verifica se uma pessoa pode ser doadora de sangue, considerando a idade e os critérios de saúde.
idade = int(input('Idade: '))
if idade > 16 and idade < 69:
    peso = float(input('Peso: '))
    if peso > 50:
        sono = int(input('Tempo de descanso:'))
        if sono > 8:
            bebida = input('Consumiu Bebidas alcoolicas nas ultimas 12hrs? [N/S]: ').strip().upper()[0]
            if bebida == 'N':
                print('Pode Doar!')
            else:
                print('Não deveria ter bebido!')
        else:
            print('Tempo de sono nao condiz!')
    else:
        print('Fora do peso!')

else:
    print('Idade Incorreta!')




















































