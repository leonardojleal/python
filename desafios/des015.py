dias = int(input('Por quantos dias o carro foi alugado?  '))
kmr = float(input('Quantidade de Km rodados: '))
#pago = (dias*60) + (kmr*0.15) - Da para fazer desta forma, ou direto como no exemplo que está sendo utilizado. 

print('O carro foi alugado por {} dias e rodou por {:.0f}Km. O valor a ser pago será de: {:.2f}'.format(dias,kmr, dias*60+kmr*0.15))