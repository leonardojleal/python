valor_casa = float(input('Qual o valor da casa: '))
salario = float(input('Qual o seu salário: '))
tempo = int(input('Em quantos anos pretente pagar: '))

valor_prestacao = valor_casa / (tempo*12)
meses = tempo * 12
porcentagem = salario*30/100

if valor_casa / meses <= porcentagem:
    print('O seu emprestimo foi \033[1;37;42mAPROVADO\033[m! O valor mensal da sua prestação será de: R${:.2f}'.format(valor_prestacao))
else:
    print('Emprestimo NEGADO')    


print('----- Desenvolvido por Leonardo Leal -----')