produto =float(input('Qual o valor do produto: R$ '))

vista= produto - (produto*10/100)
parcelado =produto + (produto*15/100)

print('O produto custa R${:.2f} e para pagamento a vista, tem um desconto de 10%, ficando: R${:.2f}'.format(produto,vista))
print('Para pagamentos parcelados, o mesmo produto com valor de R${:.2f}, terá um aumento de 15% , ficando: R$ {:.2f}'.format(produto,parcelado))