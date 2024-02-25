carteira = float(input('Quanto você tem na carteira: R$ '))

dolar =carteira/5.00
euro =carteira/5.41
iene =carteira/0.033

print('Com a conversão atual, 25/02/2024, você ficaria com {:.2f} Dolares'.format(dolar))
print('Com a conversão atual, 25/02/2024, você ficaria com {:.2f} Euros'.format(euro))
print('Com a conversão atual, 25/02/2024, você ficaria com {:.2f} Ienes'.format(iene))