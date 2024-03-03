while True:

  numero = int(input('Digite um número inteiro: '))

  print('----'* 5)
  print('[1] - Binário')
  print('[2] - Octal')
  print('[3] - Hexadecimal')
  print('[x] - Sair')

  perguntanum = str(input('Esconha a opção que deseja converter.'))
  if perguntanum == 'x' or perguntanum == 'X':
    break
  elif perguntanum == '1' or perguntanum == '2' or perguntanum == '3':
    if perguntanum == '1':
      print('{} convertido para BINÁRIO é igual a {}'.format(numero, bin(numero)[2:])) # [2:] serve para fatiar, irá aparecer do 3 indíce até o final
    elif perguntanum == '2':
      print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero)[2:]))  
    elif perguntanum == '3':
      print('{} convertido para HEXADECIMAL é igual a {}.'.format(numero, hex(numero)[2:]))
    else:
      print('Opção Inválida')  
     

