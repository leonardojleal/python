valor_pedido = float(input('Qual o valor do produto: R$ '))

if valor_pedido >= 150:
    print('O valor do seu pedido é de R$ {:.2f} e a entrega será GRATIS'.format(valor_pedido))
elif valor_pedido >= 100 and valor_pedido < 150:
     v = valor_pedido + (valor_pedido * 5/100)
     print('O valor do seu pedido é de R$ {:.2f} e terá um acrescimo de 5% para a entrega, seu valor será de R$ {:.2f}'.format(valor_pedido, v))
else:
     v2 = valor_pedido + (valor_pedido * 10/100)
     print('O valor do seu pedido é de R$ {:.2f} e terá um acrescima de 10% para a entrega, seu valor será de R$ {:.2f}'.format(valor_pedido, v2))     