valor_produto = float(input('Digite o valor da sua passagem: '))
valor_em_conta = float(input('Digite o valor em sua conta: '))

print('Status da sua compra: ') 

if valor_produto > valor_em_conta:
    print('Seu saldo é insuficiente para completar a transação')
else:
    print('Transação realizada com sucesso!')    

   