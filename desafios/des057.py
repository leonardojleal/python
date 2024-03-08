sexo = str(input('Digite o seu sexo [F/M]: ')).upper()

while sexo == 'F' or sexo == 'M':
    print('Obrigado por participar da campanha!')
    break
if sexo != 'F' or sexo != 'M':
    sexo = str(input('Digite o seu sexo [F/M]: ')).upper()
    print('Obrigado por participar da campanha!')
print('FIM')   
