soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0: #calculando se os números são divisiveis por 3
      cont = cont + 1
      soma = soma + c
print('A soma de todos os {} valores solicitados é {}'.format(cont,soma))      
