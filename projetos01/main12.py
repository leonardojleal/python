import math

conta = float(input('Valor em conta: '))
custo = float(input('Custo da viagem: '))
vf = conta - custo

print('Você estava com R${} em sua conta.'.format(conta))
print('Seu custo na viagem foi de R${}'.format(custo))
print('O valor atual em sua conta é de R${}'.format(vf))