# Inicializa variáveis para armazenar os gastos em cada categoria
alimentação = float(input('Digite o valor gasto com Alimentação: R$ '))
transporte = float(input('Digite o valor gasto com o Transporte: R$'))
moradia = float(input('Digite o valor gasto em Moradia: R$ '))
lazer = float(input('Digite o valor gasto em Lazer: R$ '))

# calculando o valor do gasto mensal 
valor_total = alimentação + transporte + moradia + lazer


# exibindo o total de gasto mensal do usuário
print('\nTotal de gastos mensais: ')
print(f'Alimentação: R${alimentação:.2f}')
print(f'Transporte: R${transporte:.2f}')
print(f'Moradia: R${moradia:.2f}')
print(f'Lazer: R${lazer:.2f}')
print(f'Total: R${valor_total:.2f}')
