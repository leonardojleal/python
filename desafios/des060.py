'''import math

numero = int(input('Digite um número: '))

res = math.factorial(numero)
valor = 0

# print('O fatorial de {} é {}'.format(numero, res))

while True:
    if numero > valor:
        print('O fatorial de {} é {}'.format(numero, res))
        break
    else:
        print('Digite um numero inteiro!')
print('FIM')  '''

n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}.'.format(f))