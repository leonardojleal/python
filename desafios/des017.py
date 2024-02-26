import math 

oposto = float(input('Digite o cateto oposto: '))
adjacente = float(input('Digite o cateto adjacente: '))
hipotenusa = math.hypot(oposto,adjacente)

print('O valor dos catetos oposto e adjacente, são respectivamente {} e {}, o comprimeito da hipotenusa é: {:.2f}'.format(oposto,adjacente,hipotenusa))