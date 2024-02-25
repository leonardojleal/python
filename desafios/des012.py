preco =float(input('Preço do produto: R$ '))
novo =preco*5/100
vf = preco-novo

print('O preço do produto com 5% de desconto é: {:.2f}'.format(vf))