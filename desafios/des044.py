produto = float(input('Digite o valor do produto: R$ '))

vista = produto - (produto*10/100) # Á vista no dinheiro / cheque
vistac = produto - (produto*5/100) # Á vista no cartão
x3 = produto + (produto*20/100) # 3 vezes ou mais no cartão

print('Para pagamentos á vista no dinheiro ou cheque, o produto terá 10% de desconto e seu novo valor será de: R$ {:.2f}'.format(vista))
print('Para pagamentos á vista no cartão, o produto terá 5% de desconto e seu novo valor será de: R$ {:.2f}'.format(vistac))
print('Para pagamentos em até 2x no cartão, valor normal de R$ {:.2f}'.format(produto))
print('Para 3x ou mais no cartão, o produto terá 20% de juros e seu novo valor será de: R$ {:.2f}'.format(x3))