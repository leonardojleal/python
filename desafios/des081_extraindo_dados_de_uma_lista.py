from time import sleep
valores = list()

while True:
    valores.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Ss':      
      print('PROCESSANDO...')
      sleep(1)
    elif resp in 'Nn' or resp != 'Ss':
        print('PROCESSANDO...')
        sleep(1)
        break
print('-=' * 30) 
print(f'Você digitou {len(valores)} elementos.')   
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista.')

    