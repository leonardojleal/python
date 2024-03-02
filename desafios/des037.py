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
      rio = str(bin(numero))
      print(rio)
    elif perguntanum == '2':
      cta = str(oct(numero))
      print(cta)  
    elif perguntanum == '3':
      exa = str(hex(numero))
      print(exa)  
    else:
      print('Opção Inválida')  
     

