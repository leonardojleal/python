produtos = [] #criando uma lista vazia para armazenar os produtos e seus preços


# criando um loop para permitir que o usuario insira os produtos e preços
while True:
    produto = input('Digite o nome do produto (ou "fim" para encerrar): ')
    if produto.lower() == 'fim':
        break
    preco = float(input('Digite o valor do produto: R$ '))
    produtos.append((produto, preco))

# Calculando o total da compra e adicionando o desconto de 10%
total = sum(preco for produto, preco in produtos)    
desconto = total * 0.1
total_com_desconto = total - desconto

# Exibindo valor final a ser pago pelo usuário
print('Total da compra: R$ {:.2f}'.format(total))
print('Desconto (10%): R$ {:.2f}'.format(desconto))
print('Total a ser pago: R$ {:.2f}'.format(total_com_desconto))