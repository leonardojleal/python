ingresso = float(input('Digite o valor do ingresso: R$ '))
meia = ingresso/2
desconto = ingresso - (ingresso*5/100)




print('-'*50)
print('O ingresso custa R${:.2f}, e você irá pagar meia entrada no valor de R${:.2f}'.format(ingresso,meia))
print('-'*50)
print('O valor do ingresso custa R${:.2f} e para pagamento a vista com 5% de desconto, pague o valor de R${:.2f}.'.format(ingresso,desconto))
print('-'*50)