n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2)/2 #criando a média

if media < 5:
    print('Sua média foi {}, e você está  \033[1;41mREPROVADO!\033[m'.format(media))
elif media >= 5 and media <= 6.9:
    print('Sua média foi {}, e você está de \033[1;43mRECUPERAÇÃO!\033[m'.format(media))
else:
    print('Sua média foi {}, e você está \033[1;42mAPROVADO!\033[m'.format(media))        