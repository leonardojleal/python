salario = float(input('Digite o seu salário: '))

a1 = salario + (salario*10/100)
a2 = salario + (salario*15/100)

if salario > 1250:
    print('\033[1;32;40mVocê teve um aumento de 10% no salário, seu novo salário é {:.2f}\033[m'.format(a1))
elif salario <= 1250:
    print('\033[1;32;40mVocê teve um aumento de 15% no salário, seu novo salário é {:.2f}\033[m'.format(a2))  

print('-----Desenvolvido por Leonardo Leal-----')