velocidade = float(input('Digite a velocidade do seu carro: '))
multa = (velocidade - 80) * 7

if velocidade > 80:
    print('Sua velocidade atual é {}Km e você foi MULTADO!'.format(velocidade))
    print('Você terá que pagar um valor de {:.1f}R$ como multa!'.format(velocidade, multa))    
else:
    print('Sua velocidade atual é {}Km e você está dentro do limite de velocidade. Diriga com SEGURANÇA! '.format(velocidade))    

