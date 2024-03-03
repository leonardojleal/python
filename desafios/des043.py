#criando informações de entrada
peso = float(input('Qual o seu peso: (Kg) '))
altura = float(input('Qual sua altura: (m) '))

imc = peso / (altura ** 2)

#print('O seu ICM é de: {:.2f}'.format(icm)) - TESTANDO CALCULO

if imc < 18.5:
    print('Seu IMC é {:.1f} e você está abaixo do peso.'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Seu IMC é {:.1f} e você está com o peso ideal.'.format(imc))
elif imc == 25 and imc < 30:
    print('Seu IMC é {:.1f} e você está com sobrepeso.'.format(imc))     
elif imc == 30 and imc < 40:
    print('Seu IMC é {:.1f} e você está com obesidade.'.format(imc))
else:
    print('Seu IMC é {:.1f} e você está com obesidade morbida.'.format(imc))           

