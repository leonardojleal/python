from time import sleep

print('{:=^40}'.format('LOJAS LEONARDO LEAL'))

preco = float(input('Preço das compras: R$ '))
print(''' FORMAS DE PAGAMENTO
[1] á vista dinheiro/cheque
[2] á vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
[5] cancelamento da compra''')      

opcao = int(input('Qual é a opção: '))

if opcao == 1:
    print('PROCESSANDO...')
    sleep(2)
    total = preco - (preco*10/100)
elif opcao == 2:
    print('PROCESSANDO...')
    sleep(2)
    total = preco - (preco*5/100) 
elif opcao == 3:
    print('PROCESSANDO...')
    sleep(2)
    total =  preco 
    parcela = preco / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    print('PROCESSANDO...')
    sleep(2)
    total = preco + (preco*20/100)
    total_parcelas = int(input('Quantas parcelas? '))
    parcela = total / total_parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(total_parcelas,parcela))
else:
    total = 0
    print('\033[37;41mOPÇÃO INVÁLIDA DE PAGAMENTO. TENTE NOVAMENTE.\033[m')    




print('Sua compra de R$ {:.2f} vai custar R$ \033[42m{:.2f}\033[m no final.'.format(preco,total))       
    