#criando informações de entrada
peso = float(input('Qual o seu peso: '))
altura = float(input('Qual sua altura: '))

a = altura*10
p = peso

icm = a / p

#print('O seu ICM é de: {:.2f}'.format(icm)) - TESTANDO CALCULO

if icm < 18.5:
    print('Seu ICM é {:.1f} e você está abaixo do peso.'.format(icm))
elif icm >= 18.5 and icm <= 25:
    print('Seu ICM é {:.1f} e você está com o peso ideal'.format(icm))
elif icm == 25 and icm < 30:
    print('Seu ICM é {:.1f} e você está com sobrepeso'.format(icm))     
elif icm == 30 and icm < 40:
    print('Seu ICM é {:.1f} e você está com obesidade'.format(icm))
else:
    print('Seu ICM é {:.1f} e você está com obesidade morbida'.format(icm))           

