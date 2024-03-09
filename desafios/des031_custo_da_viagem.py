distancia = int(input('Digite a distância da sua viagem: '))
vc = distancia * 0.50
vl = distancia * 0.45


#print('Sua viagem é de {:.0f}Km e o valor total é de: R$ {:.2f}'.format(distancia,vc))
#print('Sua viagem é de {:.0f}Km e o valor total é de: R$ {:.2f}'.format(distancia,vl))

if distancia <= 200:
    print('Sua viagem é de {:.0f}Km e o valor total é de: R$ {:.2f}'.format(distancia,vc))
else:
    print('Sua viagem é de {:.0f}Km e o valor total é de: R$ {:.2f}'.format(distancia,vl))    

print('-----Desenvolvido por Leonardo Leal-----')    