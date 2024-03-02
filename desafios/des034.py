salario = float(input('Digite o seu salário: '))

a1 = salario + (salario*10/100)
a2 = salario + (salario*15/100)

if salario > 1250:
    print('Você teve um aumento de 10% no salário, seu novo salário é {:.2f}'.format(a1))
elif salario <= 1250:
    print('Você teve um aumento de 15% no salário, seu novo salário é {:.2f}'.format(a2))  

print('-----Desenvolvido por Leonardo Leal-----')