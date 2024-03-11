contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')


while True:
   num = int(input('Digite um número de 0 a 20: '))
   if 0 <= num <= 20:
      break
   print('Tende novamente.', end='')
print(f'Você digitou o número {contagem[num]}')
while True:
   opcao = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
   if opcao == 'S':
      num = int(input('Digite um número de 0 a 20: '))
      print(f'Você digitou o número {contagem[num]}')  
   elif opcao == 'N':
      break   
    

    




