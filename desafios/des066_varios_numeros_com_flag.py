n = cont = s = 0

while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'Você digitou {cont} números e a soma é {s}')    
#print('Você digitou {} número e a soma entre eles é {}'.format(cont, s))